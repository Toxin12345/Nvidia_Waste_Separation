from flask import Flask, request, render_template, jsonify
from util import processText

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    result = None
    if request.method == 'POST':
        user_text = request.form["text"].strip(" ")
        result = processText(user_text)

        return jsonify({'result': result})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
