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

def recommend_subscription(company_name):
    """Fetch the meeting summary and use AI to recommend a subscription model."""
    df = load_meeting_notes()
    if df is None:
        return "[ERROR] Failed to load meeting notes."

    meeting_summary = get_meeting_summary(company_name, df)
    if not meeting_summary:
        return f"[ERROR] No meeting summary found for '{company_name}'."

    try:
        # Direct call to Prediction Guard model
        response = client.completions.create(
            model="Hermes-3-Llama-3.1-70B",
            prompt=prompt_template.format(overall_summary=meeting_summary),
            max_tokens=200,
            temperature=0.5
        )

        raw_output = response.get("choices", [{}])[0].get("text", "").strip()

        # Extract Model and Reason
        lines = raw_output.split("\n")
        model = lines[0].replace("Model:", "").strip() if "Model:" in lines[0] else "Unknown"
        reason = lines[1].replace("Reason:", "").strip() if len(lines) > 1 else "No reason provided."

        return f"Model: {model}\nReason: {reason}"

    except Exception as e:
        return f"[ERROR] Failed to get recommendation: {e}"