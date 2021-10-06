from googletrans import *
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/', methods=['post', 'get'])
def translater():

    code_dict = {'Russian': 'ru', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de'}

    translator = Translator()

    if request.method == 'POST':
        trans = request.form.get('trans')  # запрос к данным формы
        lang = request.form.get('lang')
        if lang in code_dict.keys():
            translation = translator.translate(trans, dest=code_dict[lang])
            translated_message = translation.text
            return render_template('index.html', my_string=translated_message,
                                   lang='Your native language is ' + translation.src.upper())
        else:
            error_message = 'Try to enter last-language again'
            return render_template('index.html', error=error_message)
    return render_template('index.html')



#output: 'The sky is blue and I like bananas'

if __name__ == '__main__':
    app.run(port=3000)