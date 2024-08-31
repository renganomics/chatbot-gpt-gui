import openai
import os

password = os.environ["CHATPASS"]


class Chatbot:
    def __init__(self):
        openai.api_key = password

    def get_response(self, user_input):
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=3000,
            temperature=0.5
        ).choices[0].message.content
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about a bird.")
    print(response)
