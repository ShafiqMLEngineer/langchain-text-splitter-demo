# big text file 1000 pages 
# divide into chunks 
# its called splitting


# every llm have limit of context token
# splitter solve this problem
#  

# Length Based Splitting | character splitter
# -----------------
# length =100 
# jo chunks ki length set krain gy us word tak 
# jesy phnchy ga first chunks ban jaye ga 
# ---------------
# ye nhi dekhta meaning pora hoa ya nhi ye cut kr deta hy
# yahi iski problem hy 
# or is sy jo embedding bany gi us me meaning sahi nhi hoga
# 
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

text = """
LangChain is a framework for building applications with LLMs.
It provides tools for RAG, agents, prompts and document processing.
"""
splitter = CharacterTextSplitter(
    separator="",
    chunk_size=20,
    chunk_overlap=2 
    # Yani previous chunk ke last 2 characters next chunk mein repeat honge.
)

chukns = splitter.split_text(text)
print(chukns)

# big data ki bjye choty chunk me convert
#  kr ky unky embeddings find krny sy embedding 
# quality barh jaye gi ..

# sementic search... similarity :: agr chunking k bad
# sementic search krty hain to acha result ata hy 

# -------------------------------------
# TYPE OF TextSplitters

# - Length Based
# - Text Structure Based
# - Document Structure Based
# - Sementic Meaning Based
# --------------------------------------

# Length Based TextSplitting::

# ye bht fast or simple way hy..
# isme ham pehly hi decide kr lain gy har chunk ka size kia hoga ..
# like chunk size=100 / Token size b rkh skty hain
# Disadvantage ...
# word k beech me hi aksar cut kr deta hy jaha length 
# k equal phnch jata hy ..
# half info aik chunk me or half kisi dosry chunk me,,