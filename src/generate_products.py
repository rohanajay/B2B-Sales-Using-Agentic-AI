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

def generate_products(overall_summary):
    """Use LLM to generate a list of recommended products based on meeting summary."""
    try:
        prompt = (
            "Given the following business use case, recommend Prediction Guard products/services that best suit the company’s needs.\n\n"
            f"Business Use Case:\n{overall_summary}\n\n"
            "Format your answer as:\n"
            "- <Product Name>: <Reason for recommendation>\n\n"
            "Only suggest Prediction Guard products."
        )

        response = client.completions.create(
            model="Hermes-3-Llama-3.1-70B",
            prompt=prompt,
            max_tokens=250,
            temperature=0.5
        )

        return response['choices'][0]['text'].strip()

    except Exception as e:
        return f"[ERROR] Failed to generate product recommendations: {e}"