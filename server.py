"""
server.py


This module handles server-side logic for the web application.
"""
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

# emotionDetctor
@app.route("/emotionDetector")
def sent_analyzer():
    """
    Processes incoming HTTP requests.

    Args:
        request (Request): The incoming request object.

    Returns:
        Response: The processed response object.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the label is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return  f"For the given statement, the system response is " \
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, " \
            f"'joy': {joy}, and 'sadness': {sadness}.\nThe dominant emotion is {dominant_emotion}."


@app.route("/")
def render_index_page():
    """
    Processes incoming HTTP requests.

    Args:
        request (Request): The incoming request object.

    Returns:
        Response: The processed response object.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
