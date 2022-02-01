import os
from flask import Flask, render_template, request
import pickle
import pandas as pd
import re
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import warnings
import pickle
from googletrans import Translator

warnings.simplefilter('ignore')

app = Flask(__name__, static_folder="Static", template_folder="Templates")
df = pd.read_csv('./DataSet.csv')
X = df["Text"]
y = df["Language"]
le = LabelEncoder()
y = le.fit_transform(y)
data_list = []
for text in X:         
    text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
    text = re.sub(r'[[]]', ' ', text)
    text = text.lower()
    data_list.append(text)
cv = CountVectorizer()
X = cv.fit_transform(data_list).toarray()
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=42)
model = pickle.load(open('predictor.pkl', 'rb'))
y_pred = model.predict(x_test)
langs = pickle.load(open('langs.pkl', 'rb'))
cv = CountVectorizer()
X = cv.fit_transform(data_list).toarray()
def predictLanguage(text):
  x = cv.transform([text]).toarray()
  lang = model.predict(x)
  lang = le.inverse_transform(lang)
  return f"Language: {lang[0]}", lang[0]
def translateText(text, from_lang, to_lang):
  translator = Translator()
  translatedText = translator.translate(text, src=from_lang, dest=to_lang)
  return translatedText.text
def resultingText(text, to_lang):
  lang = predictLanguage(text)
  translatedText = translateText(text, langs[lang[1]], to_lang)
  return f"<span style='font-weight: 500'>Text Language:</span> {lang[1]}<br><span style='font-weight: 500'>Translated Text:</span> {translatedText}", translatedText

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    if request.form['toLang'] == 'None':
      result = predictLanguage(request.form['text'])
    else:
      result = resultingText(request.form['text'], request.form['toLang'])
    return render_template('index.html', result=result, langs=langs, keys=list(langs.keys()))
  return render_template('index.html', result="", langs=langs, keys=list(langs.keys()))

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5001)