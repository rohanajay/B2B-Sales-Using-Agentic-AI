import os
from langchain_predictionguard import PredictionGuard
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence

# Initialize PredictionGuard with correct parameters
pg_llm = PredictionGuard(
    predictionguard_api_key=os.getenv("PREDICTIONGUARD_API_KEY"),
    model="Hermes-3-Llama-3.1-70B"
)

# Create the Prompt Template
prompt_template = PromptTemplate(
    input_variables=["overall_summary"],
    template=(
        "Based on the following business use case, recommend the most suitable subscription model "
        "(choose between 'On-Prem' or 'Managed Cloud') and provide a short reason.\n\n"
        "Business Use Case:\n{overall_summary}\n\n"
        "Format your answer as:\n"
        "Model: <On-Prem or Managed Cloud>\n"
        "Reason: <brief reason>"
    ),
)

# Use RunnableSequence (as per new LangChain syntax)
chain = prompt_template | pg_llm

def recommend_subscription(overall_summary):
    """Generate a subscription recommendation using Prediction Guard."""
    try:
        response = chain.invoke({"overall_summary": overall_summary})
        return response.strip()
    except Exception as e:
        return f"[ERROR] {e}"