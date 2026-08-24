

# yani ik alag type ka document strucutr
# jesy programming code

# ab is k liye different type  k 
# seperaters hoty hain 

# ye recursiveCharacter hi hy lekin is me bus seperater hum different use kr rhy hain or ye kafi sary hain nez sy dekho 
# yani html k liye alag 
# python k liye alag 
# and so on....

from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text_splitter = RecursiveCharacterTextSplitter(
    separators=[
        "\n\n",   # paragraph
        "\n",     # line
        " ",      # word
        ""        # character
    ],
    chunk_size=100,
    chunk_overlap=10
)



# ------------from_language----------------


from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    Language
)

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=10
)


# from_language() Python, JavaScript, Markdown, HTML, Java, C++, etc. ke liye predefined appropriate separators provide karta hai.

# Isliye tumhara point correct tha:

# Recursive splitter mein separators sirf manually "\n\n", "\n", " " tak limited nahi hain; LangChain mein different programming/document languages ke liye predefined separator sets bhi hain.