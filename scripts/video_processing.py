import subprocess

def embed_subtitles(input_video, subtitle_file, output_video):
    """Embed subtitles into the video using FFmpeg."""
    
    command = [
        'ffmpeg', '-i', input_video, '-vf', f"subtitles={subtitle_file}",
        '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental', output_video
    ]
    subprocess.run(command, check=True)  
