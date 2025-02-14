import os
from langchain_predictionguard import PredictionGuard
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence

# Initialize Prediction Guard LLM
pg_llm = PredictionGuard(
    predictionguard_api_key=os.getenv("PREDICTIONGUARD_API_KEY"),
    model="Hermes-3-Llama-3.1-70B"
)

# Define Prompt Template for Purchase Terms
prompt_template = PromptTemplate(
    input_variables=["custom_terms"],
    template=(
        "Generate a list of purchase terms for the sales agreement. "
        "If there are custom terms provided, include them. Otherwise, use standard terms. "
        "Output 3-5 points clearly.\n\n"
        "Custom Terms (if any):\n{custom_terms}\n\n"
        "Output Format:\n"
        "- Term 1\n"
        "- Term 2\n"
        "- Term 3"
    ),
)

# Create RunnableSequence for the pipeline
chain = prompt_template | pg_llm

def generate_terms(custom_terms=""):
    """Generate standard or custom purchase terms using Prediction Guard."""
    try:
        response = chain.invoke({"custom_terms": custom_terms})
        return response.strip()
    except Exception as e:
        return f"[ERROR] {e}"