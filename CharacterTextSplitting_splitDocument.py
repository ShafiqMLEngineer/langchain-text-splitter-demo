from langchain_huggingface import HuggingFaceEmbeddings,ChatHuggingFace
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

textSPlitter = CharacterTextSplitter(
    separator="",
    chunk_size=20, # 100
    chunk_overlap=2 # 10...20 ... 20% tak
)

loader = PyPDFLoader("../Documents_Loader/SHAFIQ_AHMAD_RESUME_.pdf")

docs = loader.load()

text = textSPlitter.split_documents(docs)

for i in text:  

    print("*************",i.page_content,"************")
    # har chunk ka apna ik metadata hy 
    # or page_content hy....



a = """
`CharacterTextSplitter` text ko **ek specific separator** (jaise `\n\n`) ki base par split karta hai aur `chunk_size` ke according chunks banane ki koshish karta hai, lekin agar koi ek piece `chunk_size` se bada ho jaye to usko further todne ke liye automatically next separator par nahi jata. Jabke `RecursiveCharacterTextSplitter` **multiple separators ko priority ke sath use karta hai** — pehle paragraph (`\n\n`), phir line (`\n`), phir space/word (`" "`), aur zarurat par character (`""`) — isliye agar text `chunk_size` se bada ho to ye gradually smaller boundaries par ja kar usko tod deta hai.

"""