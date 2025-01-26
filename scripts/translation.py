from transformers import pipeline

def translate_text(text, target_language="hi"):
    """Translate text to a target language using Hugging Face's pre-trained models."""
    
    
    translator = pipeline("translation", model=f"Helsinki-NLP/opus-mt-en-{target_language}")
    translated = translator(text)
    
    return translated[0]['translation_text']

