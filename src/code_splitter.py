from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters.base import Language, TextSplitter

# Create a RecursiveCharacterTextSplitter for Python
python_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON, chunk_size=1000, chunk_overlap=0)

def chunk_codes(codes):
    code_chunks = []
    # Use the splitter to create documents from the provided Python code
    python_docs = python_splitter.create_documents(codes)

    # Print the chunks of Python code
    for doc in python_docs:
        code_chunks.append(doc.page_content)
    
    return code_chunks