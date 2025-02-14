import os
from langchain_predictionguard import PredictionGuard
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence

# Initialize Prediction Guard LLM
pg_llm = PredictionGuard(
    predictionguard_api_key=os.getenv("PREDICTIONGUARD_API_KEY"),
    model="Hermes-3-Llama-3.1-70B"
)

# Define Prompt Template for Product Descriptions
prompt_template = PromptTemplate(
    input_variables=["overall_summary"],
    template=(
        "Based on the customer's business use case described below, list the recommended products and services "
        "for their pilot program. Provide 2-4 services with brief descriptions.\n\n"
        "Business Use Case:\n{overall_summary}\n\n"
        "Format the output as:\n"
        "- <Product/Service>: <Brief Description>"
    ),
)

# Use RunnableSequence to create the generation pipeline
chain = prompt_template | pg_llm

def generate_products(overall_summary):
    """Generate recommended products and services based on overall summary."""
    try:
        response = chain.invoke({"overall_summary": overall_summary})
        return response.strip()
    except Exception as e:
        return f"[ERROR] {e}"