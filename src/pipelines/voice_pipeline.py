from resemblyzer import VoiceEncoder,preprocess_wav  # create speaker embedding
import numpy as np
import io # input-output module -- treat bytes as file
import librosa 
import streamlit as st


@st.cache_resource  # stores model in memory
def load_voice_encoder():
    return VoiceEncoder()


def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()
        # sr -- sampling rate
        audio , sr = librosa.load(io.BytesIO(audio_bytes),sr=16000)
        wav = preprocess_wav(audio) # cleans voice
        embedding = encoder.embed_utterance(wav) # voice - 256D vector
        return embedding.tolist()
    except Exception as e:
        st.error("Voice recog error")
        return None
    

def identify_speaker(new_embedding,candidates_dict,threshold=0.65):
    if new_embedding is None or not candidates_dict:
        return None,0.0
    
    best_sid = None
    best_score = -1.0

    for sid,stored_embedding in candidates_dict.items():
        if stored_embedding:
            similarity = np.dot(new_embedding,stored_embedding)
            if similarity > best_score:
                best_score = similarity
                best_sid = sid

    if best_score >= threshold:
        return best_sid,best_score
    return None,best_score


def process_bulk_audio(audio_bytes,candidates_dict,threshold=0.65):
    try:
        encoder = load_voice_encoder()

        audio,sr = librosa.load(io.BytesIO(audio_bytes),sr=16000)
        segments = librosa.effects.split(audio,top_db=30) # separate speech from silence

        identified_results = {}

        for start,end in segments:
            if (end - start) < sr * 0.5: # ignore shorter clips
                continue

            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)
            embedding = encoder.embed_utterance(wav)

            sid,score = identify_speaker(embedding,candidates_dict,threshold)

            if sid:
                if sid not in identified_results  or score > identified_results[sid]:
                    identified_results[sid] = score

        return identified_results
    except Exception as e:
        st.error("Bulk process error")
        return {}       
    
# flow

# audio upload
#      |
# librosa load 
#      |
# preprocess audio 
#      |
# resemblyzer encoder 
#      |
# 256D voice embedding 
#      |
# compare wd stored embedding 
#      |
# dot prod similarity
#      |
# threshold check 
#      |
# attendance marked