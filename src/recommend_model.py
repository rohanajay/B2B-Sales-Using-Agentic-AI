import os
from dotenv import load_dotenv
from predictionguard import PredictionGuard
from langchain_core.prompts import PromptTemplate
from load_meeting_notes import load_meeting_notes, get_meeting_summary

# Load environment variables
load_dotenv()
api_key = os.getenv("PREDICTIONGUARD_API_KEY")

if not api_key:
    raise ValueError("[ERROR] PREDICTIONGUARD_API_KEY is not set. Add it to .env or venv.")

# Initialize Prediction Guard client
client = PredictionGuard(api_key=api_key)

# Define prompt template
prompt_template = PromptTemplate.from_template(
    "Based on the following business use case, recommend the most suitable subscription model "
    "(choose between 'On-Prem' or 'Managed Cloud') and provide a short reason.\n\n"
    "Business Use Case:\n{overall_summary}\n\n"
    "Format your answer as:\n"
    "Model: <On-Prem or Managed Cloud>\n"
    "Reason: <brief reason>"
)

def recommend_subscription(overall_summary):
    """Use LLM to recommend a subscription model based on cleaned meeting summary."""
    try:
        prompt = (
            "Based on the following business use case, recommend the most suitable subscription model "
            "(choose between 'On-Prem' or 'Managed Cloud') and provide a short reason.\n\n"
            f"Business Use Case:\n{overall_summary}\n\n"
            "Format your answer as:\n"
            "Model: <On-Prem or Managed Cloud>\n"
            "Reason: <brief reason>"
        )

        response = client.completions.create(
            model="Hermes-3-Llama-3.1-70B",
            prompt=prompt,
            max_tokens=200,
            temperature=0.5
        )

        return response['choices'][0]['text'].strip()

    except Exception as e:
        return f"[ERROR] Failed to get recommendation: {e}"