"""Flask application for emotion detection using Watson NLP."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze emotion from text and return formatted result."""
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    output = "For the given statement, the system response is "
    output += "'anger': " + str(response['anger']) + ", "
    output += "'disgust': " + str(response['disgust']) + ", "
    output += "'fear': " + str(response['fear']) + ", "
    output += "'joy': " + str(response['joy']) + ", "
    output += "'sadness': " + str(response['sadness']) + ". "
    output += "The dominant emotion is " + response['dominant_emotion'] + "."
    return output

@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
