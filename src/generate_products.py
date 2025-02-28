import os
import re
from dotenv import load_dotenv
from predictionguard import PredictionGuard
from load_meeting_notes import load_meeting_notes, get_meeting_summary

# Load environment variables
load_dotenv()
api_key = os.getenv("PREDICTIONGUARD_API_KEY")

if not api_key:
    raise ValueError("[ERROR] PREDICTIONGUARD_API_KEY is not set. Add it to .env or venv.")

# Initialize Prediction Guard client
client = PredictionGuard(api_key=api_key)

# Predefined list of Prediction Guard's products and services
pg_offerings = [
    {
        "name": "Self-Hosted Models",
        "description": "Deploy popular model families (Llama 3.1, Mistral, Neural Chat, DeepSeek) privately within your infrastructure."
    },
    {
        "name": "Security Checks",
        "description": "Protect against vulnerabilities like prompt injections and model supply chain threats."
    },
    {
        "name": "Essential Integrations",
        "description": "Integrate seamlessly with AI tools such as LangChain, LlamaIndex, and code assistants, ensuring data remains within your network."
    },
    {
        "name": "Privacy Filters and Output Validations",
        "description": "Prevent issues like hallucinations, toxic outputs, and leaks of personally identifiable information (PII)."
    },
    {
        "name": "Managed Cloud Deployment",
        "description": "Fully hosted and managed by Prediction Guard. Quick setup (<1 day), stateless (no data storage), and HIPAA compliant."
    },
    {
        "name": "Self-Hosted Deployment",
        "description": "Host within your infrastructure with flexible compute options, optimized for cost-effective performance at enterprise scale."
    },
    {
        "name": "Single-Tenant Deployment",
        "description": "Dedicated, isolated deployment managed by Prediction Guard, ensuring security without the need to manage your own infrastructure."
    }
]

def generate_products(company_name):
    """Generate a list of recommended Prediction Guard products and services for a given company."""
    df = load_meeting_notes()
    if df is None:
        return "[ERROR] Failed to load meeting notes."

    meeting_summary = get_meeting_summary(company_name, df)
    if not meeting_summary:
        return f"[ERROR] No meeting summary found for '{company_name}'."

    try:
        # Construct the prompt for the AI model
        prompt = (
            "Based on the following business use case, recommend the most suitable Prediction Guard products and services "
            "from the provided list. For each recommendation, provide the product name and a brief description explaining "
            "why it's a good fit for the company's needs.\n\n"
            f"Business Use Case:\n{meeting_summary}\n\n"
            "Prediction Guard Offerings:\n"
        )

        # Append each offering to the prompt
        for offering in pg_offerings:
            prompt += f"- {offering['name']}: {offering['description']}\n"

        prompt += "\nFormat the response as:\n"
        prompt += "- <Product Name>: <Reason for recommendation>\n"

        # Generate the AI response
        response = client.completions.create(
            model="Hermes-3-Llama-3.1-70B",
            prompt=prompt,
            max_tokens=400,  # Increased token limit for full responses
            temperature=0.7
        )

        raw_output = response.get("choices", [{}])[0].get("text", "").strip()

        # === POST-PROCESSING: CLEAN & FORMAT OUTPUT === #
        # Ensure consistent bullet formatting
        formatted_output = re.sub(r"\n\s*\n", "\n", raw_output)  # Remove excessive newlines
        formatted_output = re.sub(r"^-", "\n- ", formatted_output)  # Ensure each bullet point starts correctly

        return formatted_output.strip()

    except Exception as e:
        return f"[ERROR] Failed to generate products: {e}"