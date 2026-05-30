import streamlit as st


def subject_card(name, code, section, stats=None):

        st.markdown("""
            <div class="subject-card">
        """, unsafe_allow_html=True)

        st.markdown(
            f"""
            ## {name}
            """
        )

        info1, info2 = st.columns(2)

        with info1:
            st.metric(
                label="Subject Code",
                value=code
            )

        with info2:
            st.metric(
                label="Section",
                value=section
            )

        if stats:

            cols = st.columns(len(stats))

            for col, (icon, label, value) in zip(cols, stats):

                with col:

                    st.metric(
                        label=f"{icon} {label}",
                        value=value
                    )

        st.markdown("""
            </div>
        """, unsafe_allow_html=True)