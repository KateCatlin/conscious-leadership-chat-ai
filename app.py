import os
import yaml
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage

load_dotenv()

app = Flask(__name__)

# 15 Conscious Leadership Principles
CONSCIOUS_LEADERSHIP_PRINCIPLES = [
    "1. Taking radical responsibility.",
    "2. Learning through curiosity.",
    "3. Feeling all feelings.",
    "4. Speaking candidly.",
    "5. Eliminating gossip.",
    "6. Practicing integrity.",
    "7. Generating appreciation.",
    "8. Exercising your genius.",
    "9. Living a life of play and rest.",
    "10. Creating win-for-all solutions.",
    "11. Being the resolution.",
    "12. Seeing abundance.",
    "13. Sourcing approval, control, and security from within.",
    "14. Experiencing the world as an ally.",
    "15. Creating a life of 'enough.'"
]

GITHUB_MODELS_ENDPOINT = "https://models.github.ai/inference"
GITHUB_MODELS_MODEL = "openai/gpt-4.1"

def load_prompts(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

# Load prompts from .prompts.yml
PROMPTS = load_prompts("prompts.yml")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"response": "Please enter a message."}), 400

    github_token = os.environ.get("GITHUB_TOKEN")
    if not github_token:
        return jsonify({"response": "Server error: GITHUB_TOKEN not set."}), 500

    system_prompt_content = PROMPTS["messages"][0]["content"]
    user_prompt_template = PROMPTS["messages"][1]["content"]
    user_prompt_content = user_prompt_template.replace("{{input}}", user_message)
    messages_for_api = [
        SystemMessage(content=system_prompt_content),
        UserMessage(content=user_prompt_content)
    ]
    try:
        client = ChatCompletionsClient(
            endpoint=GITHUB_MODELS_ENDPOINT,
            credential=AzureKeyCredential(github_token)
        )
        response = client.complete(
            model=GITHUB_MODELS_MODEL,
            messages=messages_for_api,
            temperature=0.7,
            top_p=0.95
        )
        ai_response = response.choices[0].message.content.strip()
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"response": "Sorry, there was an error processing your request."}), 500

if __name__ == "__main__":
    app.run(debug=True)
