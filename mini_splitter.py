import streamlit as st

from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    TokenTextSplitter
)


st.title("🔪 LangChain Text Splitter Demo")


# --------------------------------------------------
# TEXT INPUT
# --------------------------------------------------

text = st.text_area(
    "Enter your text:",
    """
Pakistan is a beautiful country.
It has many cities.
Lahore is famous for its food.
Islamabad is famous for its beauty.
Karachi is famous for its beaches.
"""
)


# --------------------------------------------------
# SPLITTER SELECTION
# --------------------------------------------------

splitter_name = st.selectbox(
    "Select Splitter:",
    [
        "CharacterTextSplitter",
        "RecursiveCharacterTextSplitter",
        "TokenTextSplitter"
    ]
)


# --------------------------------------------------
# SETTINGS
# --------------------------------------------------

chunk_size = st.slider(
    "Chunk Size",
    min_value=10,
    max_value=200,
    value=50
)


chunk_overlap = st.slider(
    "Chunk Overlap",
    min_value=0,
    max_value=50,
    value=10
)


# Separator sirf Character aur Recursive ke liye
if splitter_name != "TokenTextSplitter":

    separator = st.text_input(
        "Separator:",
        value=" "
    )


# --------------------------------------------------
# CREATE SPLITTER
# --------------------------------------------------

if st.button("Split Text"):

    if splitter_name == "CharacterTextSplitter":

        splitter = CharacterTextSplitter(
            separator=separator,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )


    elif splitter_name == "RecursiveCharacterTextSplitter":

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )


    elif splitter_name == "TokenTextSplitter":

        splitter = TokenTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )


    # --------------------------------------------------
    # SPLIT
    # --------------------------------------------------

    chunks = splitter.split_text(text)


    # --------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------

    st.subheader(
        f"Results — {splitter_name}"
    )

    st.write(
        f"Total Chunks: **{len(chunks)}**"
    )


    for i, chunk in enumerate(chunks):

        st.markdown(
            f"### Chunk {i + 1}"
        )

        st.code(chunk)

        st.write(
            f"Characters: {len(chunk)}"
        )

        st.divider()