"""
Sanyerlis Camacaro - CSC235 - Sancamac@uat.edu Assignment:
Assignment 5.1: Final Project - AI Sentiment Analysis

"Music Mood"
MusicMood is a unique application that suggests music based on your mood.

For access, open code folder, enter cmd in code path, type to run: python app.py
Gain access to server and type http://127.0.0.1:5000/MusicMood in your web browser to load page.

In this app, users will be able to:

Enter text into a form (like a movie review or a tweet).
Have your AI model process the text and classify the sentiment.
Display the classification to the user (positive, negative, or neutral).
"""
# Import the necessary libraries:
# - Flask for the web application
# - TextBlob for sentiment analysis

from flask import Flask, render_template, request
from textblob import TextBlob

# Initialize a Flask app instance
app = Flask(__name__)

# Create a class to manage our Music Library
class MusicLibrary:
    
    # Constructor method to initialize the music library
    def __init__(self):
        # Define a dictionary to store songs categorized by mood
        self.music_library = {
            "happy": ["Don't Stop Me Now - Queen", "Happy - Pharrell Williams", "I Wanna Dance with Somebody - Whitney Houston"],
            "sad": ["Someone Like You - Adele", "Say Something - A Great Big World", "The Sound of Silence - Simon & Garfunkel"],
            "neutral": ["Let It Be - The Beatles", "Imagine - John Lennon", "Counting Stars - OneRepublic"],
            "angry": ["Break Stuff - Limp Bizkit", "Given Up - Linkin Park", "Platypus (I Hate You) - Green Day"]
        }

    # Function to get the list of songs based on a given mood
    def get_music(self, mood):
        return self.music_library.get(mood, [])

# Define a function for sentiment analysis
def sentiment_analysis(text):
    # Use TextBlob to analyze the sentiment of the text
    analysis = TextBlob(text)
    # Categorize sentiment into moods based on polarity
    if analysis.sentiment.polarity > 0.5:
        return 'happy', analysis.sentiment.polarity
    elif analysis.sentiment.polarity < -0.5:
        return 'angry', analysis.sentiment.polarity
    elif analysis.sentiment.polarity == 0:
        return 'neutral', analysis.sentiment.polarity
    else:
        return 'sad', analysis.sentiment.polarity

# Flask route for the home page
@app.route('/MusicMood', methods=['GET', 'POST'])
def index():
    # Initialize variables for sentiment, polarity, and songs list
    sentiment, polarity, songs = None, None, []
    
    # Check if the request method is a POST
    if request.method == 'POST':
        # Get the text entered by the user
        text = request.form['text']
        
        # Get the sentiment and polarity of the text
        sentiment, polarity = sentiment_analysis(text)
        
        # Fetch song recommendations based on sentiment
        music_library = MusicLibrary()
        songs = music_library.get_music(sentiment)
    
    # Render the index.html template and pass in sentiment, polarity, and songs data
    return render_template('index.html', sentiment=sentiment, polarity=polarity, songs=songs)

# Main entry point for the Flask app
if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode


