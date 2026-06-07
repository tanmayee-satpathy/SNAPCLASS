import html
import streamlit as st

# prvt func - generate unique streamlit key
def _subject_card_key(name, code, section):
    raw = f"{name}-{code}-{section}".lower()
    # remove special ch
    safe = "".join(ch if ch.isalnum() else "-" for ch in raw)
    return f"subject-card-{safe.strip('-') or 'item'}"


def _metric_card(title, value, gradient, label_color):
    return (
        f"<div style='background:{gradient};border:1px solid rgba(255,255,255,0.10);"
        "border-radius:18px;padding:18px;box-shadow:0 10px 24px rgba(0,0,0,0.30);"
        "backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);'>"
        f"<div style='color:{label_color};font-size:0.95rem;font-weight:600;margin-bottom:10px;'>{title}</div>"
        f"<div style='color:white;font-size:2.15rem;font-weight:800;line-height:1.05;'>{value}</div>"
        "</div>"
    )


def subject_card(name, code, section, stats=None, footer_callback=None):
    stats = stats or [("", "", 0), ("", "", 0)]
    students = stats[0][2] if len(stats) > 0 and len(stats[0]) > 2 else 0
    classes = stats[1][2] if len(stats) > 1 and len(stats[1]) > 2 else 0
# protects from HTML injection
    safe_name = html.escape(str(name))
    safe_code = html.escape(str(code))
    safe_section = html.escape(str(section))
    card_key = _subject_card_key(safe_name, safe_code, safe_section)

    st.markdown(
        f"""
<style>
  .st-key-{card_key} {{
    border: 1.2px solid transparent;
    border-radius: 20px;
    padding: 18px 16px 12px 16px;
    background:
      linear-gradient(
        145deg,
        rgba(12, 12, 24, 0.90),
        rgba(18, 18, 34, 0.86)
      ) padding-box,
      linear-gradient(
        132deg,
        rgba(255, 241, 182, 0.72) 0%,
        rgba(255, 213, 110, 0.56) 28%,
        rgba(212, 148, 57, 0.45) 62%,
        rgba(255, 233, 166, 0.68) 100%
      ) border-box;
    position: relative;
    overflow: hidden;
    box-shadow:
      0 14px 34px rgba(0, 0, 0, 0.36),
      0 0 18px rgba(255, 215, 120, 0.12),
      0 0 0 1px rgba(255, 245, 210, 0.12) inset;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    margin-bottom: 12px;
    transition: all 0.28s ease;
  }}

  .st-key-{card_key}::before {{
    content: "";
    position: absolute;
    inset: 0;
    border-radius: 20px;
    pointer-events: none;
    background:
      radial-gradient(circle at 14% 9%, rgba(167,139,250,0.16), transparent 34%),
      radial-gradient(circle at 84% 88%, rgba(251,191,36,0.12), transparent 36%);
    opacity: 0.72;
  }}

  .st-key-{card_key}:hover {{
    transform: translateY(-3px);
    box-shadow:
      0 20px 44px rgba(0, 0, 0, 0.46),
      0 0 28px rgba(255, 215, 120, 0.22),
      0 0 0 1px rgba(255, 245, 210, 0.22) inset;
  }}
</style>
        """,
        unsafe_allow_html=True,
    )

    with st.container(border=False, key=card_key):
        st.markdown(
            (
                "<div style='text-align:center;color:white;font-size:2rem;font-weight:800;"
                f"margin-bottom:16px;letter-spacing:-0.5px;'>{safe_name}</div>"
            ),
            unsafe_allow_html=True,
        )
# subject code & section
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                _metric_card(
                    "Subject Code",
                    safe_code,
                    "linear-gradient(145deg, rgba(124,92,255,0.24), rgba(71,49,151,0.16))",
                    "#DCC6FF",
                ),
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                _metric_card(
                    "Section",
                    safe_section,
                    "linear-gradient(145deg, rgba(156,88,226,0.22), rgba(90,47,146,0.16))",
                    "#E7C9FF",
                ),
                unsafe_allow_html=True,
            )

# adds vertical gap
        st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

# students & classes
        col3, col4 = st.columns(2)
        with col3:
            st.markdown(
                _metric_card(
                    "Students",
                    students,
                    "linear-gradient(145deg, rgba(124,92,255,0.24), rgba(71,49,151,0.16))",
                    "#DCC6FF",
                ),
                unsafe_allow_html=True,
            )
        with col4:
            st.markdown(
                _metric_card(
                    "Classes",
                    classes,
                    "linear-gradient(145deg, rgba(156,88,226,0.22), rgba(90,47,146,0.16))",
                    "#E7C9FF",
                ),
                unsafe_allow_html=True,
            )

        if footer_callback:
            st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
            footer_callback()
