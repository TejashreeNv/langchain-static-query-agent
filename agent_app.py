# ==========================================
# Milestone 1 - Multi-Tool AI Agent
# ==========================================

from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint

# ----------------------------
# 1. Load Environment Variables
# ----------------------------

load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not hf_token:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in .env file")

# ----------------------------
# 2. Load Hugging Face Model
# ----------------------------

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    task="text2text-generation",
    huggingfacehub_api_token=hf_token,
    max_new_tokens=150,
    temperature=0.5
)

# ----------------------------
# 3. Prompt Template + Output Parser
# ----------------------------

prompt = ChatPromptTemplate.from_template(
    "Answer the following question clearly and concisely:\n{question}"
)

parser = StrOutputParser()
chain = prompt | llm | parser

# ----------------------------
# 4. Static Knowledge Base
# ----------------------------

knowledge_base = {
    "langchain": "LangChain is a framework for building LLM-powered applications using chains, agents, memory, and tools.",
    "python": "Python is a high-level programming language widely used in AI and Data Science.",
    "ai": "Artificial Intelligence refers to systems that simulate human intelligence.",
    "agent": "An AI agent is a system that perceives its environment and takes actions to achieve goals.",
    "llm": "A Large Language Model (LLM) is trained on massive text data to understand and generate language."
}

# ----------------------------
# 5. Tool Functions
# ----------------------------

def search_knowledge(query: str):
    query_lower = query.lower()
    for key in knowledge_base:
        if key in query_lower:
            return knowledge_base[key]
    return None


def count_words(text: str):
    words = text.split()
    return f"The text contains {len(words)} words."


def calculate_math(expression: str):
    try:
        # Safe evaluation (basic math only)
        allowed_chars = "0123456789+-*/(). "
        if all(char in allowed_chars for char in expression):
            result = eval(expression)
            return f"The result is {result}"
        else:
            return None
    except:
        return "Invalid mathematical expression."


# ----------------------------
# 6. Query Router
# ----------------------------

def process_query(user_input: str):
    lower = user_input.lower()

    # Word Count Tool
    if "count words in" in lower:
        text = user_input.split("count words in", 1)[1].strip()
        return count_words(text)

    # Math Tool
    math_result = calculate_math(user_input)
    if math_result:
        return math_result

    # Knowledge Base
    kb_result = search_knowledge(user_input)
    if kb_result:
        return kb_result

    # LLM Fallback
    return chain.invoke({"question": user_input})


# ----------------------------
# 7. Console Interface
# ----------------------------

print("=" * 60)
print("Milestone 1: Multi-Tool AI Agent")
print("=" * 60)
print("Capabilities:")
print("• Knowledge base (AI, Python, LangChain, Agents, LLM)")
print("• Word counter")
print("• Math calculator (+ - * /)")
print("• LLM fallback")
print("\nType 'exit' to quit\n")

while True:
    try:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Agent: Goodbye Teju 👋")
            break

        response = process_query(user_input)
        print("Agent:", response)

    except KeyboardInterrupt:
        print("\nAgent: Session interrupted. Goodbye 👋")
        break

    except Exception as e:
        print("Error:", str(e))