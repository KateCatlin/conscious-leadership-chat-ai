# conscious-leadership-chat-ai

> A simple, personal AI chatbot that brings the 15 Commitments of Conscious Leadership to life,  powered entirely by **GitHub Models** and your own GitHub token. 🎉

## ✨ What This Is

This is a minimal, expressive demo app showing how you can spin up an AI-powered chat experience using nothing more than:

- Your own **GitHub account + Personal Access Token**
- GitHub’s **free Models API** (currently in preview)
- **Copilot** to write all your code

You write your prompts, manage them in the GitHub UI, and GitHub handles the inference pipeline. No OpenAI billing, no complex setup.

## 💡 What It Does

Users write something about their day, and the app responds with a thoughtful, supportive message grounded in one of the [15 Commitments of Conscious Leadership](https://conscious.is/15-commitments). Think of it as a self-coaching moment, elevated by AI.

It’s great for moments of reflection, but also serves as a **starter kit** to show just how easy GitHub has made it to run personalized LLM applications.

## 🔧 Why I Made This

I’ve done code bootcamps in Java and Ruby, but I have no prior experience with Python. I wanted to see:

- What can I build with AI using **GitHub Models**?
- How fast can I get it running with **just Copilot**?
- Can I host something useful that people might actually use?

The answer to all of the above: **yes**. This app came together through Copilot-generated scaffolding, edits, and chat assistance — and GitHub Models is doing all the AI inference in real time behind the scenes.

## 🔍 Try It & Explore the Prompts

If you're curious about how the prompts actually work, GitHub has made it incredibly easy to see and edit them:

1. Go to the GitHub repo
2. Click the new **"Models"** tab
3. Choose the system or user prompt to view/edit in the UI

This makes collaborating on prompt design **way easier** — especially if you want to fine-tune tone, behavior, or structure as a team.

I'll be making a video soon walking through how I'm using the Models tab to improve and manage my prompts using GitHub's new **prompt tooling and evaluations features**.

## ✨ Features

- 🧘‍♀️ **Conscious Leadership Coaching:** Grounded in the 15 commitments
- ✍️ **Daily Reflection Input:** Just type how you're feeling today
- 🤖 **GitHub Models Integration:** Handles AI response generation

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, Vanilla JS
- **Backend:** Python Flask
- **AI Engine:** GitHub Models (no third-party API key required!)
- **Other Tools:** Dotenv, GitHub Copilot for development

## ⚙️ Setup

```bash
# 1. Clone the repo
git clone https://github.com/KateCatlin/conscious-leadership-chat-ai.git

# 2. Navigate to it
cd conscious-leadership-chat-ai

# 3. Create a virtual environment
python -m venv venv && source venv/bin/activate

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Add your GitHub token to a .env file
echo "GITHUB_TOKEN=your_personal_token_here" > .env

# 6. Start the app
python app.py
```

Then open `http://localhost:5000` in your browser and start chatting with the AI.

## 🙋‍♀️ Want to Contribute?

Yes please! If you're interested in exploring GitHub Models with your own prompts, or improving this chat UI, here’s how to dive in:

1. Fork the repo
2. Open the Models tab to tweak the system/user prompts
3. Submit a PR or open an issue with ideas

This is a very open and early project. Contributions, UI feedback, or prompt experiments are welcome.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Acknowledgements

*   **Conscious Leadership Group:** For their foundational work on the 15 Commitments of Conscious Leadership.
*   **GitHub Models:** — For the API powering the AI in this project. 
*   **GitHub Copilot:** — For writing almost all of this code for me 😄

## Links

- Prompts: Click the "Models" tab on this repo
- Commitments Info: conscious.is/15-commitments
- Improve This App: [GitHub Repo](https://github.com/KateCatlin/conscious-leadership-chat-ai)
