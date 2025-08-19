import openai
import os
import gradio as gr
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found. Please set it in your .env file.")
openai.api_key = api_key
def get_ai_response(user_message, system_prompt):
    """Generates a response from the AI based on user input and a system role."""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling OpenAI: {e}")
        return "Sorry, I encountered an error. Please try again."

def convert_text_to_speech(text):
    """Converts text to speech and returns the path to the audio file."""
    try:
        tts = gTTS(text=text, lang='en')
        audio_path = "response.mp3"
        tts.save(audio_path)
        return audio_path
    except Exception as e:
        print(f"Error in gTTS: {e}")
        return None

def transcribe_audio(audio_file_path):
    """Transcribes audio using OpenAI Whisper."""
    try:
        with open(audio_file_path, "rb") as audio_file:
            transcript = openai.audio.transcriptions.create(
              model="whisper-1", 
              file=audio_file
            )
        return transcript.text
    except Exception as e:
        print(f"Error in transcription: {e}")
        return ""

chatbot_prompt = "You are a friendly and encouraging English tutor for a child. Your name is Genie. Keep answers simple and short."
roleplay_prompts = {
    "At School": "You are a friendly teacher at a school. A student is asking you a question. Start a simple conversation with them.",
    "At the Store": "You are a helpful shopkeeper. A child has entered your store. Start a friendly conversation and ask what they are looking for.",
    "At Home": "You are a caring parent at home. Your child wants to talk to you about their day. Start a warm and simple conversation."
}

def voice_chat_tutor(audio_input):
    """Handles the main chatbot logic."""
    if audio_input is None:
        return "Please speak first.", None
    
    user_text = transcribe_audio(audio_input)
    if not user_text:
        return "Sorry, I couldn't hear you clearly.", None
        
    ai_text_response = get_ai_response(user_text, chatbot_prompt)
    ai_audio_response = convert_text_to_speech(ai_text_response)
    
    return user_text, ai_audio_response

def voice_chat_roleplay(audio_input, scenario):
    """Handles the roleplay logic."""
    if audio_input is None:
        return "Please speak first.", None, scenario

    system_prompt = roleplay_prompts.get(scenario, chatbot_prompt)
    user_text = transcribe_audio(audio_input)
    if not user_text:
        return "Sorry, I couldn't hear you clearly.", None, scenario

    ai_text_response = get_ai_response(user_text, system_prompt)
    ai_audio_response = convert_text_to_speech(ai_text_response)
    
    return user_text, ai_audio_response, scenario


with gr.Blocks() as demo:
    gr.Markdown("# SpeakGenie AI English Tutor")
    
    with gr.Tab("AI Chatbot - Speak with a Tutor"):
        with gr.Row():
            audio_input_chatbot = gr.Audio(sources=["microphone"], type="filepath", label="Speak to Genie")
            audio_output_chatbot = gr.Audio(label="Genie's Response", autoplay=True)
        text_output_chatbot = gr.Textbox(label="Conversation Transcript")
        
        audio_input_chatbot.change(
            fn=voice_chat_tutor,
            inputs=audio_input_chatbot,
            outputs=[text_output_chatbot, audio_output_chatbot]
        )

    with gr.Tab("Roleplay Mode - Real-Life Conversations"):
        scenario_dropdown = gr.Dropdown(
            choices=list(roleplay_prompts.keys()), 
            label="Choose a Scenario",
            value="At School"
        )
        with gr.Row():
            audio_input_roleplay = gr.Audio(sources=["microphone"], type="filepath", label="Start Speaking")
            audio_output_roleplay = gr.Audio(label="Response", autoplay=True)
        text_output_roleplay = gr.Textbox(label="Conversation Transcript")
        
        audio_input_roleplay.change(
            fn=voice_chat_roleplay,
            inputs=[audio_input_roleplay, scenario_dropdown],
            outputs=[text_output_roleplay, audio_output_roleplay, scenario_dropdown]
        )

demo.launch()