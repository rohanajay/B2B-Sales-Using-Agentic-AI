import os
import json
import base64
from getpass import getpass
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import pandas as pd
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_predictionguard import PredictionGuard

# Load environment variables
load_dotenv()

# Securely input API key if not in environment
if not os.getenv("PREDICTIONGUARD_API_KEY"):
    api_key = getpass("Enter your Prediction Guard API Key: ")
    os.environ["PREDICTIONGUARD_API_KEY"] = api_key

# Initialize Prediction Guard LLM
llm = PredictionGuard(
    model="Hermes-3-Llama-3.1-70B",
    predictionguard_api_key=os.environ["PREDICTIONGUARD_API_KEY"],
    temperature=0.75,
    max_tokens=200,
    stop=["000"]
)

# Function to load and decrypt meeting notes securely
def load_transcripts(encrypted_file="data/encrypted_transcripts.enc", key_file="config/encryption_key.key"):
    """ Load and decrypt meeting transcripts """
    with open(key_file, "rb") as key_f:
        key = key_f.read()
    cipher = Fernet(key)
    
    with open(encrypted_file, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = cipher.decrypt(encrypted_data).decode("utf-8")
    return json.loads(decrypted_data)

# Define a summarization prompt template
prompt_template = PromptTemplate(
    input_variables=["notes"],
    template="Summarize the following meeting notes in bullet points:\n\n{notes}"
)

# Create a summarization chain
summarization_chain = LLMChain(llm=llm, prompt=prompt_template)

# Function to summarize meeting notes
def summarize_notes(notes):
    try:
        if not isinstance(notes, str) or notes.strip() == "":
            return "No valid notes available."

        summary = summarization_chain.run({"notes": notes})
        return summary.strip() if summary else "Summarization failed."
    except Exception as e:
        return f"Error: {str(e)}"

# Function to determine next steps based on summarized notes
def deduce_next_steps(summary):
    if "self-hosted" in summary.lower():
        return "Follow up with security and IT teams for deployment feasibility."
    elif "budget concerns" in summary.lower():
        return "Schedule a cost-benefit discussion with financial stakeholders."
    elif "pilot agreement" in summary.lower():
        return "Send pilot agreement document and schedule next review meeting."
    else:
        return "Send follow-up email summarizing key discussion points."

# Load meeting notes
transcripts = load_transcripts()

# Process each transcript and generate summary & next steps
data = []
for meeting in transcripts:
    summary = summarize_notes(meeting["discussion"])
    next_steps = deduce_next_steps(summary)
    
    data.append({
        "Date": meeting["date"],
        "Attendees": ", ".join(meeting["attendees"]),
        "Summary": summary,
        "Next Steps": next_steps
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save processed output
df.to_csv("data/sales_pipeline_summaries.csv", index=False)
print(df.head())
