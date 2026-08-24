


# Text_Structure_Based ::
# iska mtlb 
# > Paragrapgh 
# > line 
# > word 
# > characters


# isme splitter pehly paragrapgh ki base pr split krta hy
# phir isko line ki base pr split krta hy 
# phir isko word ki base pr split krta hy
# phir isko character ki base pr krta hy
# yani jaha b splitting pori ho jye waha tak
# ye krny ki koshish krta rhta hy..

# yani agr 2 pragrapgh 20 ..20
# length k hain or hamny chunk size 30 de dia
# to ye paragrapgh ki base pr split kry ga
# to hmry pass 2 paragrapgh agye 20..20
# lekin hamny to 30 size dia is liye wo 
# ab line ki base pr tor k jorny ki koshish
# kry ga or jesy hi krny lgy ga to dekhy ga k dono ka alag alag size chota hogiga hy 30 sy to mazeed agy nhi jaye ga


# Recursive splitter pehle natural boundaries 
# par split karta hai; agar koi individual 
# piece chunk_size se bada ho, tab us piece 
# ko smaller boundaries se recursively todta hai.

from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Artificial intelligence is transforming modern 
technology by enabling machines to understand 
language, recognize images, generate content, 
and solve complex problems. Machine learning 
allows computers to learn patterns from data 
without explicit programming. Deep learning uses 
neural networks to handle large datasets and 
perform advanced tasks efficiently across different 
real world applications.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap=0
)

chunk = splitter.split_text(text)

print(len(chunk))
print(chunk)


a = """
`CharacterTextSplitter` text ko **ek specific separator** (jaise `\n\n`) ki base par split karta hai aur `chunk_size` ke according chunks banane ki koshish karta hai, lekin agar koi ek piece `chunk_size` se bada ho jaye to usko further todne ke liye automatically next separator par nahi jata. Jabke `RecursiveCharacterTextSplitter` **multiple separators ko priority ke sath use karta hai** — pehle paragraph (`\n\n`), phir line (`\n`), phir space/word (`" "`), aur zarurat par character (`""`) — isliye agar text `chunk_size` se bada ho to ye gradually smaller boundaries par ja kar usko tod deta hai.

"""