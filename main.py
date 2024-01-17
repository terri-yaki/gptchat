import openai
import os

openai.api_key = "YOUR-OPENAI-API"

def chatgpt(prompt):

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview", #change to use different openAI models
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    conversation_history = []
    save_folder = "saved_conversation/"

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    while True:
        user_input = input("You: ")
        conversation_history.append("You: " + user_input + "\n")

        if user_input.lower() in ["exit", "break", "quit"]:
            save_conversation = input("Save conversation? [y/n] ").lower()
            if save_conversation == 'y':
                file_title = input("Enter a title for the conversation file: ")
                file_name = file_title + ".txt"  # Create filename from title
                full_path = os.path.join(save_folder, file_name)
                with open(full_path, "w") as file:  # Use full_path here
                    file.write("\n".join(conversation_history))
                print(f"Conversation saved as '{full_path}'.")
            break

        response = chatgpt(user_input)
        conversation_history.append("GPT: " + response + "\n")  # Add AI response to history
        print("GPT: ", response)
