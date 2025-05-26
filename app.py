import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage

load_dotenv()

app = Flask(__name__)

# 15 Conscious Leadership Commitments
CONSCIOUS_LEADERSHIP_COMMITMENTS = [
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
    print(f"GITHUB_TOKEN: {github_token}")
    if not github_token:
        return jsonify({"response": "Server error: GITHUB_TOKEN not set."}), 500

    commitments_string = "\n".join(CONSCIOUS_LEADERSHIP_COMMITMENTS)
    system_prompt_content = f"""You are an insightful and supportive AI assistant. Your goal is to help users reflect on their day using the 15 Conscious Leadership Commitments.\nHere are the 15 Conscious Leadership Commitments:\n{commitments_string}\n\nWhen the user shares something about their day:\n1.  Analyze their message carefully.\n2.  From the list above, choose the SINGLE most relevant Conscious Leadership Commitment that could offer them a helpful perspective or insight related to what they've shared.\n3.  Craft a concise (2-4 sentences), supportive, and empathetic response to the user.\n4.  In your response, naturally weave in the name or essence of the commitment you selected, and briefly explain how it might apply to their situation. Do not explicitly state 'I have chosen commitment X'. Simply use it.\n"""
    messages_for_api = [
        SystemMessage(content=system_prompt_content),
        UserMessage(content=user_message)
    ]

    try:
        client = ChatCompletionsClient(
            endpoint=GITHUB_MODELS_ENDPOINT,
            credential=AzureKeyCredential(github_token)
        )
        print("ChatCompletionsClient initialized successfully.")
    except Exception as e:
        print(f"Error initializing ChatCompletionsClient: {e}")
        return jsonify({"response": "Server error: Unable to initialize AI client."}), 500

    try:
        response = client.complete(
            model=GITHUB_MODELS_MODEL,
            messages=messages_for_api,
            temperature=0.7,
            top_p=0.95
        )
        ai_response = response.choices[0].message.content.strip()
        return jsonify({"response": ai_response})
    except Exception as e:
        print(f"Error during API call: {e}")
        return jsonify({"response": "Sorry, there was an error processing your request."}), 500

if __name__ == "__main__":
    app.run(debug=True)