# 🎙️ The Empathy Engine — Giving AI a Human Voice

<img width="952" height="735" alt="image" src="https://github.com/user-attachments/assets/f1e2b1c1-4471-4844-9856-2ea737432c93" />


## 🌟 Overview
This project dynamically modulates synthesized speech to match the **emotion** of input text.
It bridges text sentiment and vocal expression using Python and Flask.

---

## 🚀 Features
- Emotion Detection using NLTK VADER (Positive / Negative / Neutral)
- Voice Modulation via `pyttsx3` + `pydub`
- Emotion-to-Voice Mapping for rate, pitch, and volume
- Web UI with real-time emotion + emoji display
- Extensible: plug in ElevenLabs or Google TTS for premium voices

---

## 🧩 Setup Instructions

```bash
# 1. Clone repository
git clone https://github.com/SHAKSHIY/empathy-engine.git
cd empathy-engine

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download VADER lexicon (only once)
python -c "import nltk; nltk.download('vader_lexicon')"

# 5. Run the app
python app.py

Visit: http://127.0.0.1:5000

## 🎛️ Emotion-to-Voice Mapping

| Emotion | Rate Change | Volume Change | Audio Filter |
|----------|--------------|----------------|----------------|
| 😊 **Positive** | Faster (+40%) | Louder (+30%) | Brighter tone |
| 😔 **Negative** | Slower (-30%) | Softer (-30%) | Low-pass filter |
| 😐 **Neutral**  | Default | Default | None |

**Author**: Shakshi
