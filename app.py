from TTS.api import TTS
import gradio as gr

# Load multilingual voice cloning model
tts = TTS("tts_models/multilingual/multi-dataset/your_tts")

def generate_voice(input_text, reference_wav):
    """
    Generates speech from text using a reference voice.
    """
    output_path = "output.wav"
    tts.tts_to_file(
        text=input_text,
        speaker_wav=reference_wav.name,
        language="en",  # Required for multilingual model
        file_path=output_path
    )
    return output_path

# Build Gradio UI
ui = gr.Interface(
    fn=generate_voice,
    inputs=[
        gr.Textbox(label="Enter Text", placeholder="Type the text you want to convert to speech..."),
        gr.File(label="Upload Reference WAV File", file_types=[".wav"])
    ],
    outputs=gr.Audio(label="Generated Voice"),
    title="Voice Cloner UI",
    description="Upload a reference .wav file and input text to generate speech in that voice."
)

# Launch the UI
ui.launch()