from model_loder import ModelLoader
from chat_memory import ChatMemory
import wikipedia
from textblob import TextBlob


def fetch_from_wikipedia(query):
    try:
        corrected_query = str(TextBlob(query).correct()).title()
        results = wikipedia.search(corrected_query)
        if not results:
            return None

        for result in results:
            if corrected_query.lower() in result.lower():
                summary = wikipedia.summary(result, sentences=2)
                if result.lower() in summary.lower():
                    return summary

        fallback = results[0]
        summary = wikipedia.summary(fallback, sentences=2)
        if fallback.lower() in summary.lower():
            return summary

        return None
    except Exception:
        return None


# improved keyword handler to filter general knowledge lookups
KEYWORD_TRIGGERS = [
    "capital of", "find about", "search", "ceo of", "who is", "president of", "prime minister of"
]


def main():
    print("\n🤖 Chatbot started. Type '/exit' to quit, '/reset' to clear memory, '/offline' to disable internet mode, or '/online' to enable it.\n")

    model_loader = ModelLoader()
    generator = model_loader.load()
    memory = ChatMemory(max_length=3)
    online_mode = True

    while True:
        user_input = input("User: ")
        normalized_input = user_input.strip().lower()

        if normalized_input == "/exit":
            print("\n👋 Exiting chatbot. Goodbye!\n")
            break

        if normalized_input == "/reset":
            memory = ChatMemory(max_length=3)
            print("🔄 Memory reset.\n")
            continue

        if normalized_input == "/offline":
            online_mode = False
            print("📴 Switched to offline mode.\n")
            continue

        if normalized_input == "/online":
            online_mode = True
            print("🌐 Switched to online mode.\n")
            continue

        if "your name" in normalized_input:
            bot_reply = "My name is KyBot."
            print(f"Bot: {bot_reply}\n")
            memory.add_turn(user_input, bot_reply)
            continue
        elif "who created you" in normalized_input or "your boss" in normalized_input:
            bot_reply = "I was created by Narottam Kumar."
            print(f"Bot: {bot_reply}\n")
            memory.add_turn(user_input, bot_reply)
            continue

        if online_mode and any(kw in normalized_input for kw in KEYWORD_TRIGGERS):
            wiki_reply = fetch_from_wikipedia(user_input)
            if wiki_reply:
                print(f"Bot (📡 Live): {wiki_reply}\n")
                memory.add_turn(user_input, wiki_reply)
                continue

        instruction = (
            "You are KyBot, a helpful chatbot created by Narottam Kumar. "
            "You assist students with well-explained answers. "
            "If asked, your name is KyBot and your creator is Narottam Kumar.\n"
        )

        dialogue_history = memory.get_context() + f"\nUser: {user_input}\nBot:"
        full_input = instruction + dialogue_history

        if len(full_input.split()) > 300:
            print("⚠️ Input too long. Try shortening your question or restart the chat.\n")
            continue

        response = generator(full_input, max_new_tokens=100)[0]['generated_text']
        bot_reply = response.strip().split("Bot:")[-1].strip()

        print(f"Bot: {bot_reply}\n")
        memory.add_turn(user_input, bot_reply)


if __name__ == "__main__":
    main()
