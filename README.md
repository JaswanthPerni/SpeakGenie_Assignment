# SpeakGenie - AI/Tech Internship Task Submission

This project is a Real-Time AI Voice English Tutor created for the SpeakGenie AI/Tech internship selection process. The application is designed as an AI-powered English speaking and communication tool for students, providing a fun and effective way to learn through conversation.

## Features

The application is built with two primary modes as specified in the task requirements:

### 1. AI Chatbot - Speak with a Tutor
* **Voice-to-Voice Interaction**: Users can speak to the AI tutor, which listens and responds verbally.
* **Speech-to-Text**: Utilizes AI to transcribe the student's spoken words into text.
* **Intelligent Responses**: Leverages a GPT API to generate child-friendly, educational replies.
* **Text-to-Speech**: The AI's text response is converted back into speech for the user to hear.

### 2. Roleplay Mode - Real-Life Conversations
* **Scenario-Based Learning**: Students can practice their English speaking skills in various everyday scenarios.
* **Interactive Scenarios**: The application includes the following conversation modes:
    * At School
    * At the Store
    * At Home

### Bonus Features Implemented
*(You can edit this section. Delete any bonus features you did not add.)*
* **Safe, Child-Friendly AI Personality**: The AI is prompted to be consistently encouraging and appropriate for young learners.
* **Smart Speaking Tips**: The AI can provide helpful tips to improve the user's English.
* **Native Language Playback**: The AI's responses can be played back in regional languages like Hindi.

## Technologies Used
* **Python**: Core programming language.
* **OpenAI**:
    * **Whisper**: For Speech-to-Text transcription.
    * **GPT-3.5-Turbo**: For generating intelligent and conversational AI responses.
* **gTTS (Google Text-to-Speech)**: For converting the AI's text replies into audio.
* **Gradio**: To create the fast and interactive web-based user interface.
* **python-dotenv**: For securely managing API keys.

## Setup and Installation

To run this project on your local machine, please follow these steps:

**1. Prerequisites**
* Python 3.7 or newer must be installed.

**2. Clone the Repository or Download Files**
* Download the project files to a local directory.

**3. Create a Virtual Environment**
* Navigate to the project directory in your terminal and create a virtual environment:
    ```bash
    python -m venv venv
    ```
* Activate the environment:
    * **On Windows:** `.\venv\Scripts\activate`
    * **On Mac/Linux:** `source venv/bin/activate`

**4. Install Dependencies**
* Install all the necessary libraries from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

**5. Configure API Key**
* Create a file named `.env` in the root of the project directory.
* Add your OpenAI API key to this file in the following format:
    ```
    OPENAI_API_KEY="sk-YourSecretApiKeyHere"
    ```

## How to Run the Application

1.  Make sure your virtual environment is activated and dependencies are installed.
2.  Run the following command in your terminal from the project's root directory:
    ```bash
    python app.py
    ```
3.  The application will start, and a local URL (e.g., `http://127.0.0.1:7860`) will be displayed in the terminal. Open this URL in your web browser to use the AI English Tutor.