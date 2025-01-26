import srt
from datetime import timedelta

def generate_subtitles(translated_text, duration_per_line=4):
    """Generate subtitles in SRT format from translated text."""
    
    
    lines = translated_text.split('\n')  
    subtitles = []
    start_time = timedelta(seconds=0)

    for i, line in enumerate(lines):
        end_time = start_time + timedelta(seconds=duration_per_line)  
        subtitle = srt.Subtitle(
            index=i + 1,
            start=start_time,
            end=end_time,
            content=line
        )
        subtitles.append(subtitle)
        start_time = end_time  

    return srt.compose(subtitles)

def format_time(seconds):
    """Format time into SRT-compliant HH:MM:SS,MS format."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{milliseconds:03}"
