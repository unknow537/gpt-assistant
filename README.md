# GPT Assistant

GPT Assistant is an AI-powered chatbot that uses OpenAI's GPT-3 model to provide intelligent, human-like responses to any user input. This project provides a simple API that allows users to interact with the chatbot in real-time.

## Features

- User registration and login
- JWT-based authentication
- Protected endpoints (require valid token)
- Basic role-based access control
- Follows RESTful conventions
- Easily extendable

## Requirements

Make sure you have Python 3.8+ installed.

You also need to have an OpenAI API key. You can get one by signing up on [OpenAI](https://beta.openai.com/signup/). ( or look into "API_KEY_SETUP.md"

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/gpt-assistant.git
    cd gpt-assistant
    ```

2. Create a virtual environment and install the dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install required libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. Add your OpenAI API key in the `app.py` file:

    ```python
    openai.api_key = "your-openai-api-key-here"
    ```

5. Run the application:

    ```bash
    python app.py
    ```

6. You can now access the chatbot API at `http://localhost:5000/chat`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
