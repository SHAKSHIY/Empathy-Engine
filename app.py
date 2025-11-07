from flask import Flask, render_template, request, jsonify, send_file
from empathy_engine import generate_empathic_audio, detect_emotion
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "Please enter some text!"}), 400

    emotion, compound, audio_path = generate_empathic_audio(text)
    return jsonify({
        "emotion": emotion,
        "compound": compound,
        "audio": audio_path
    })

if __name__ == "__main__":
    app.run(debug=True)
