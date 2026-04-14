from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
from langdetect import detect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    translated_text = ""
    detected_lang = ""

    if request.method == 'POST':
        text = request.form['text'].strip()
        target_lang = request.form['language']

        if len(text) < 2:
            translated_text = "Please enter a longer text."
        else:
            try:

                detected_lang = detect(text).upper()

                translated_text = GoogleTranslator(
                    source='auto',
                    target=target_lang
                ).translate(text)

            except Exception as e:
                translated_text = "Error: " + str(e)

    return render_template("index.html",
                           translated_text=translated_text,
                           detected_lang=detected_lang)

if __name__ == '__main__':
    app.run(debug=True)