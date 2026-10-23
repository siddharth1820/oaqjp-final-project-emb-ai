
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again.", 400

    try:
        result = emotion_detector(text_to_analyze)
        if result["dominant_emotion"] is None:
            return "Invalid text! Please try again.", 400
        return str(result)
    except Exception as error:
        return f"Emotion detection failed: {error}", 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
