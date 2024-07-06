from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters.base import Language, TextSplitter
from langchain_community.llms import Ollama
import os

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
# model = ChatOpenAI(model="gpt-3.5-turbo")
llm=Ollama(model="llama3")

code_template = """
You are a highly skilled code developer. You will be provided with legacy code, and your task is to:
1. Identify the programming language and refactor the old code to be compatible with the latest version of the same.
2. Improve the code by making it more modular and adhering to proper coding principles and best practices.
3. Ensure the code follows proper coding guidelines and naming conventions.
4. Detect and automatically fix any errors in the code.

### Instructions:
- Convert any legacy code specific syntax to the newer version
- Modularize the code by breaking down large functions into smaller, reusable functions.
- Use appropriate naming conventions and add comments where necessary.
- Ensure the code is free of errors and can run successfully in that environment.
- Optimize the code for readability and performance. \n\n"

Just write the refactored  code below and nothimg else. Dont put ``` or anything else in code \n\n

"Legacy Code:\n{code_chunk}\n\n"
"Refactored Code:
"""

code_prompt = ChatPromptTemplate.from_template(code_template)

code_chain = code_prompt | llm | StrOutputParser()

# Create a RecursiveCharacterTextSplitter for Python
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=1000, chunk_overlap=0
)

def chunk_codes(codes):
    code_chunks = []
    # Use the splitter to create documents from the provided Python code
    python_docs = python_splitter.create_documents([codes])

    # Print the chunks of Python code
    for doc in python_docs:
        code_chunks.append(doc.page_content)
    
    return code_chunks


# Function to refactor legacy code
def refactor_legacy_code(code):
    chunks = chunk_codes(code)
    print(f"Chunks : ",chunks)
    refactored_code = []
    for chunk in chunks:
        result = code_chain.invoke({
            "code_chunk": chunk
        })
        refactored_code.append(result)
    print(f"Refactored code : ",refactored_code)
    return '\n'.join(refactored_code)

# Function to refactor all files in a folder
def refactor_files_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        print(f"Refactoring {filename}...")
        if filename.endswith('.py'):
            with open(os.path.join(input_folder, filename), 'r') as file:
                legacy_code = file.read()
            
            print(f"legacy code : ",legacy_code)
            refactored_code = refactor_legacy_code(legacy_code)
            
            output_filename = os.path.join(output_folder, filename)
            with open(output_filename, 'w') as file:
                file.write(refactored_code)
            
            print(f"Refactored {filename} and saved to {output_filename}")

# Example usage
input_folder = 'docs/legacy'
output_folder = 'docs/refactored'

refactor_files_in_folder(input_folder, output_folder)