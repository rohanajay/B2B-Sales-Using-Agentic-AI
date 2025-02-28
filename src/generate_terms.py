import os
from dotenv import load_dotenv
from predictionguard import PredictionGuard

# Load environment variables
load_dotenv()
api_key = os.getenv("PREDICTIONGUARD_API_KEY")

if not api_key:
    raise ValueError("[ERROR] PREDICTIONGUARD_API_KEY is not set. Add it to .env or venv.")

# Initialize Prediction Guard client
client = PredictionGuard(api_key=api_key)

def generate_terms(custom_terms=None):
    """Use AI to generate standard and optional custom purchase terms for a sales agreement."""
    try:
        prompt = (
            "Generate a list of purchase terms for the sales agreement. "
            "If there are custom terms provided, include them. Otherwise, use standard terms.\n\n"
            "Custom Terms (if any):\n"
        )

        if custom_terms:
            prompt += "\n".join(f"- {term}" for term in custom_terms)

        prompt += (
            "\n\nOutput Format:\n"
            "- Term 1\n"
            "- Term 2\n"
            "- Term 3\n"
        )

        response = client.completions.create(
            model="Hermes-3-Llama-3.1-70B",
            prompt=prompt,
            max_tokens=200,
            temperature=0.5
        )

        raw_output = response.get("choices", [{}])[0].get("text", "").strip()
        return raw_output

    except Exception as e:
        return f"[ERROR] Failed to generate terms: {e}"