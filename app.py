from flask import Flask,request,render_template
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def main():
    if request.method == 'POST':
        inp1 = request.form.get("inp")
        sid=SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp1)
        if score["pos"] >  score["neg"] and score["pos"] >  score["neu"] :
            return render_template('home.html',messages="POSITIVE 😊",pos=score["pos"],neg=score["neg"],neu=score["neu"])
        if score["neg"] >  score["pos"] and score["neg"] >  score["neu"] :
            return render_template('home.html',messages="NEGATIVE 😠",pos=score["pos"],neg=score["neg"],neu=score["neu"])
        else :
            return render_template('home.html',messages="NEUTRAL 🙂",pos=score["pos"],neg=score["neg"],neu=score["neu"])
    return render_template('home.html')
if __name__ == '__main__':
	app.run(debug=True)