import whisper

def transcribe_audio(file_path):
    """Transcribe audio from a video file using Whisper"""
    
    
    model = whisper.load_model("base")  
    
    
    result = model.transcribe(file_path)
    
    
    return result["text"]
