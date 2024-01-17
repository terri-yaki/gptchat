<h1>README.md for ChatGPT Script</h1>
Overview

This script is a simple Python-based interface for interacting with OpenAI's GPT models. It allows users to engage in a conversation with an AI, where each response is generated based on the input provided. The script also includes functionality to save the conversation history to a file.
Requirements

    Python 3.x
    OpenAI Python library (install with pip install openai)

Setup

    Replace "YOUR-OPENAI-API" with your OpenAI API key.
    Ensure Python 3.x is installed on your system.
    Install the OpenAI Python library using pip.

Usage

Run the script using Python. Enter your queries after "You: " prompt. To exit, type "exit", "break", or "quit".
Features

    Interact with OpenAI's GPT models.
    Save conversation history to a text file.
    Customizable model selection (default is set to "gpt-4-1106-preview").
    The conversation is saved in the saved_conversation/ directory.

Customization

    Change the model by modifying the model parameter in the chatgpt function.
    Modify the save directory by changing save_folder variable.


Note:

Keep your API key secure and do not share the script with the key embedded.

<em>**DISCLAIMER**</em>

This script is for educational purposes. Be aware of OpenAI's usage policies and costs associated with API calls.
