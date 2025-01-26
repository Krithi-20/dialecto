from flask import render_template, request, redirect, url_for
from app import app
import os
from scripts.transcription import transcribe_audio  
from scripts.translation import translate_text  
from scripts.subtitle_generation import generate_subtitles  
from scripts.video_processing import embed_subtitles  
import subprocess


def extract_audio_from_video(video_path, audio_path):
    """Extract audio from the video using FFmpeg"""
    command = [
        'ffmpeg', '-i', video_path, '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', audio_path
    ]
    subprocess.run(command, check=True)  

@app.route('/')
def index():
    """Render the homepage with the upload form"""
    return render_template('index.html')  

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and video processing"""
    if 'file' not in request.files:  
        return redirect(request.url)  
    
    file = request.files['file']  
    
    if file.filename == '':  
        return redirect(request.url)  

    if file:
        
        filename = os.path.join('data', file.filename)
        file.save(filename)

    
        audio_filename = os.path.join('data', 'audio.wav')  
        extract_audio_from_video(filename, audio_filename)

        
        transcribed_text = transcribe_audio(audio_filename)

        
        translated_text = translate_text(transcribed_text, target_language="hi")

      
        subtitles = generate_subtitles(translated_text)

        
        subtitle_file = 'outputs/output_subtitles.srt'
        with open(subtitle_file, 'w', encoding='utf-8') as f:  
            f.write(subtitles)

        
        output_video = os.path.join('app', 'static', 'output_video_with_subtitles.mp4')
        embed_subtitles(filename, subtitle_file, output_video)

        
        return redirect(url_for('result', filename=file.filename))

@app.route('/result/<filename>')
def result(filename):
    """Render the result page with the download link"""
    return render_template('result.html', filename=filename)  

