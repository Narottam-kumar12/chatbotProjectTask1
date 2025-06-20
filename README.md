# 🧠 KyBot - CLI Chatbot using Hugging Face & Wikipedia

**KyBot** is a command-line chatbot built with the `google/flan-t5-large` model from Hugging Face Transformers. It provides assignment-style and factual answers to user questions. It also supports live internet lookup using Wikipedia and has a memory buffer for contextual conversation.

---

## 🚀 Features

- 🤖 **Instruction-tuned language model** for well-structured answers.
- 🌐 **Online/offline toggle**: Uses Wikipedia search for real-time info.
- 💬 **Conversation memory** to maintain context across turns.
- 🔁 **Command shortcuts** like `/exit`, `/reset`, `/online`, `/offline`.
- 🧠 **Spell and intent correction** (e.g., `/omline` → `/online`, `manister` → `minister`).
- 🔒 **Safeguards hallucinations** from the model like repeating “KyBot is a helpful bot...”.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourname/kybot-chatbot
cd kybot-chatbot 

Install Dependencies
pip install transformers torch wikipedia textblob
python -m textblob.download_corpora



//Example Coversation
User: What is the capital of India?
Bot (📡 Live): New Delhi is the capital of India...

User: Who created you?
Bot: I was created by Narottam Kumar.

User: /offline
📴 Switched to offline mode.

User: Explain polymorphism in OOP.
Bot: Polymorphism allows functions to behave differently based on input types...

📁 Project Structure
.
├── interface.py        # CLI entry point
├── model_loader.py     # Hugging Face model loader
├── chat_memory.py      # Memory buffer to simulate conversation
├── README.md


✅ Commands Reference
Command	       Function
.....................................................
/exit	         Quit the chatbot                     .
/reset	       Reset conversation memory            .
/offline	     Turn off live Wikipedia search       .
/online	       Enable live information mode         .
.....................................................

# Demo Video
link-> https://drive.google.com/file/d/1V7JJ3r7deX4r-9ApZ1bcAo1oTWsp02Cd/view?usp=drivesdk
