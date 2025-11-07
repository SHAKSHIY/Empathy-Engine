import os
from pydub import AudioSegment
from pydub.playback import play
import pyttsx3
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure VADER lexicon is available
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

analyzer = SentimentIntensityAnalyzer()

def detect_emotion(text):
    """Detect sentiment using VADER"""
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]
    if compound >= 0.3:
        emotion = "positive"
    elif compound <= -0.3:
        emotion = "negative"
    else:
        emotion = "neutral"
    return emotion, compound


def generate_empathic_audio(text, output_path="static/output.wav"):
    """Generate modulated speech based on detected emotion and intensity"""
    emotion, compound = detect_emotion(text)

    # Setup TTS engine
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    volume = engine.getProperty("volume")
    voices = engine.getProperty("voices")

    # Default to female voice for clarity
    engine.setProperty("voice", voices[1].id if len(voices) > 1 else voices[0].id)

    # Emotion-to-voice mapping with intensity scaling
    if emotion == "positive":
        engine.setProperty("rate", int(rate + 40 * compound))
        engine.setProperty("volume", min(volume + 0.3, 1.0))
    elif emotion == "negative":
        engine.setProperty("rate", int(rate - 30 * abs(compound)))
        engine.setProperty("volume", max(volume - 0.3, 0.3))
    else:
        engine.setProperty("rate", rate)
        engine.setProperty("volume", volume)

    # Save to file
    temp_path = "temp.wav"
    engine.save_to_file(text, temp_path)
    engine.runAndWait()

    # Modulate audio using pydub for more realism
    sound = AudioSegment.from_wav(temp_path)

    if emotion == "positive":
        sound = sound + (compound * 5)  # louder, brighter
    elif emotion == "negative":
        sound = sound - (abs(compound) * 8)  # softer
        sound = sound.low_pass_filter(2000)  # dull tone for sad effect
    else:
        sound = sound  # neutral

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    sound.export(output_path, format="wav")
    os.remove(temp_path)

    return emotion, compound, output_path
