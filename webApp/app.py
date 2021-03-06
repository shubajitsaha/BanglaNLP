from flask import Flask, request, render_template
from flask import send_file,session,jsonify
import string
import random
from random import randrange
import pymongo
import urllib 

app = Flask(__name__,template_folder='static')
f = open('vocab.txt',encoding='utf8')

vocab = []
for line in f:
    vocab.append(line.split('\t')[0])
lv = len(vocab)



@app.route('/')
def home():
    w = vocab[randrange(lv)]
    return render_template('index.html',word=w)

if __name__ == '__main__':
    app.run()

app.run(host='0.0.0.0', debug=True)
