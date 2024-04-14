# Chatbot

This repository contains the source code for a chatbot powered by OpenAI's GPT-3. The chatbot utilizes the GPT3-turbo for maintaining sessions and the Gradio library for the frontend interface, offering a rich, interactive user experience.

## Features

- **Natural Language Understanding**: Leverages GPT-3 for processing and understanding natural language queries.
- **Session Management**: Uses `gpt3-turbo` for handling conversation states and session data.
- **Interactive UI**: Implements Gradio to create a dynamic and user-friendly web interface.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or later
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/moayyad16/Chatbot.git
   ```
2. Install Openai library using pip
   ```
   pip install openai    #try pip3 if it's not working
   ```
### Configuration
Obtain an API key from OpenAI and set it in your environment variables:
```
export OPENAI_API_KEY='Your-OpenAI-API-Key-Here'
```
And run

## Usage
After launching the application, visit http://localhost:8000 in your browser to interact with the chatbot. Enter your questions or messages, and the chatbot will respond accordingly.
