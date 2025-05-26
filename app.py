import os
import yaml
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage

load_dotenv()

app = Flask(__name__)

GITHUB_MODELS_ENDPOINT = "https://models.github.ai/inference"

def load_prompt_config():
    """Load the entire prompt configuration from the YAML file"""
    try:
        with open('conscious-leadership-assistant.prompt.yml', 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print("Warning: conscious-leadership-assistant.prompt.yml not found")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None

def get_system_prompt_content(prompt_config):
    """Extract the system message content from the prompt config"""
    if not prompt_config or 'messages' not in prompt_config:
        return None
    
    # Find the system message in the messages array
    for message in prompt_config['messages']:
        if message.get('role') == 'system':
            return message.get('content', '')
    
    return None

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

    # Load prompt configuration from YAML file
    prompt_config = load_prompt_config()
    if not prompt_config:
        return jsonify({"response": "Server error: Unable to load prompt configuration."}), 500

    # Extract system prompt content
    system_prompt_content = get_system_prompt_content(prompt_config)
    if not system_prompt_content:
        return jsonify({"response": "Server error: Unable to find system prompt."}), 500

    # Get model and parameters from YAML (with fallbacks)
    model = prompt_config.get('model', 'openai/gpt-4.1')
    model_params = prompt_config.get('modelParameters', {})
    temperature = model_params.get('temperature', 0.7)
    top_p = model_params.get('top_p', 0.95)

    messages_for_api = [
        SystemMessage(content=system_prompt_content),
        UserMessage(content=user_message)
    ]

    try:
        client = ChatCompletionsClient(
            endpoint=GITHUB_MODELS_ENDPOINT,
            credential=AzureKeyCredential(github_token)
        )
        response = client.complete(
            model=model,
            messages=messages_for_api,
            temperature=temperature,
            top_p=top_p
        )
        ai_response = response.choices[0].message.content.strip()
        return jsonify({"response": ai_response})
    except Exception as e:
        print(f"Error during API call: {e}")
        return jsonify({"response": "Sorry, there was an error processing your request."}), 500

if __name__ == "__main__":
    app.run(debug=True)