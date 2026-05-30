import streamlit as st


def subject_card(name, code, section, stats=None):

    students = stats[0][2]
    classes = stats[1][2]

    with st.container(border=True):

        # TITLE
        st.markdown(
            f"""
            <div style="
                text-align:center;
                color:white;
                font-size:2rem;
                font-weight:800;
                margin-bottom:28px;
                letter-spacing:-1px;
            ">
                {name}
            </div>
            """,
            unsafe_allow_html=True
        )

        # TOP ROW
        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                f"""
                <div style="
                    background:linear-gradient(
                        145deg,
                        rgba(139,92,246,0.18),
                        rgba(91,33,182,0.10)
                    );

                    border:1px solid rgba(255,255,255,0.08);

                    border-radius:20px;

                    padding:24px;

                    box-shadow:
                        0 8px 24px rgba(0,0,0,0.25);

                    backdrop-filter:blur(12px);
                ">

                    <div style="
                        color:#D8B4FE;
                        font-size:1rem;
                        font-weight:600;
                        margin-bottom:12px;
                    ">
                        Subject Code
                    </div>

                    <div style="
                        color:white;
                        font-size:2.6rem;
                        font-weight:800;
                        line-height:1;
                    ">
                        {code}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
                <div style="
                    background:linear-gradient(
                        145deg,
                        rgba(236,72,153,0.16),
                        rgba(190,24,93,0.08)
                    );

                    border:1px solid rgba(255,255,255,0.08);

                    border-radius:20px;

                    padding:24px;

                    box-shadow:
                        0 8px 24px rgba(0,0,0,0.25);

                    backdrop-filter:blur(12px);
                ">

                    <div style="
                        color:#F9A8D4;
                        font-size:1rem;
                        font-weight:600;
                        margin-bottom:12px;
                    ">
                        Section
                    </div>

                    <div style="
                        color:white;
                        font-size:2.6rem;
                        font-weight:800;
                        line-height:1;
                    ">
                        {section}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

        # BOTTOM ROW
        col3, col4 = st.columns(2)

        with col3:

            st.markdown(
                f"""
                <div style="
                    background:linear-gradient(
                        145deg,
                        rgba(139,92,246,0.18),
                        rgba(91,33,182,0.10)
                    );

                    border:1px solid rgba(255,255,255,0.08);

                    border-radius:20px;

                    padding:24px;

                    box-shadow:
                        0 8px 24px rgba(0,0,0,0.25);

                    backdrop-filter:blur(12px);
                ">

                    <div style="
                        color:#D8B4FE;
                        font-size:1rem;
                        font-weight:600;
                        margin-bottom:12px;
                    ">
                        🫂 Students
                    </div>

                    <div style="
                        color:white;
                        font-size:2.6rem;
                        font-weight:800;
                        line-height:1;
                    ">
                        {students}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        with col4:

            st.markdown(
                f"""
                <div style="
                    background:linear-gradient(
                        145deg,
                        rgba(236,72,153,0.16),
                        rgba(190,24,93,0.08)
                    );

                    border:1px solid rgba(255,255,255,0.08);

                    border-radius:20px;

                    padding:24px;

                    box-shadow:
                        0 8px 24px rgba(0,0,0,0.25);

                    backdrop-filter:blur(12px);
                ">

                    <div style="
                        color:#F9A8D4;
                        font-size:1rem;
                        font-weight:600;
                        margin-bottom:12px;
                    ">
                        📚 Classes
                    </div>

                    <div style="
                        color:white;
                        font-size:2.6rem;
                        font-weight:800;
                        line-height:1;
                    ">
                        {classes}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)