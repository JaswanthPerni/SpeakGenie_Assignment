# SpeakGenie - AI/Tech Internship Task Submission

[cite_start]This project is a Real-Time AI Voice English Tutor created for the SpeakGenie AI/Tech internship selection process[cite: 6]. [cite_start]The application is designed as an AI-powered English speaking and communication tool for students[cite: 3], providing a fun and effective way to learn through conversation.

## Features

The application is built with two primary modes as specified in the task requirements:

### [cite_start]1. AI Chatbot - Speak with a Tutor [cite: 8]
* [cite_start]**Voice-to-Voice Interaction**: Users can speak to the AI tutor, which listens and responds verbally[cite: 10, 13].
* [cite_start]**Speech-to-Text**: Utilizes AI to transcribe the student's spoken words into text[cite: 10].
* [cite_start]**Intelligent Responses**: Leverages a GPT API to generate child-friendly, educational replies[cite: 12].
* [cite_start]**Text-to-Speech**: The AI's text response is converted back into speech for the user to hear[cite: 13].

### [cite_start]2. Roleplay Mode - Real-Life Conversations [cite: 17]
* [cite_start]**Scenario-Based Learning**: Students can practice their English speaking skills in various everyday scenarios[cite: 18].
* **Interactive Scenarios**: The application includes the following conversation modes:
    * [cite_start]At School [cite: 20]
    * [cite_start]At the Store [cite: 22]
    * [cite_start]At Home [cite: 23]

### Bonus Features Implemented
*(You can edit this section. Delete any bonus features you did not add.)*
* [cite_start]**Safe, Child-Friendly AI Personality**: The AI is prompted to be consistently encouraging and appropriate for young learners[cite: 35].
* [cite_start]**Smart Speaking Tips**: The AI can provide helpful tips to improve the user's English[cite: 35].
* [cite_start]**Native Language Playback**: The AI's responses can be played back in regional languages like Hindi[cite: 25].

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