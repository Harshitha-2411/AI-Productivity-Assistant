import ollama

def get_intent(user_input):

    prompt = f"""
Classify the user request into one of these intents:

add_task
show_tasks
complete_task
delete_task
plan_day
chat

User request: {user_input}

Respond with only the intent name.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role":"user","content":prompt}]
    )

    intent = response["message"]["content"].strip().lower()

    return intent


def chat_with_ai(message):

    response = ollama.chat(
        model="llama3",
        messages=[{"role":"user","content":message}]
    )

    return response["message"]["content"]