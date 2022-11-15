from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.7exaue2.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

@app.route('/')
def main():
   return render_template('main.html')

@app.route('/cheer')
def cheer():
   return render_template('cheer.html')

@app.route("/comment", methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']

    comment_list = list(db.comment.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num':count,
        'comment':comment_receive,
        'done': 0
    }
    db.comment.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})

@app.route("/comment", methods=["GET"])
def comment_get():
    comment_list = list(db.comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route("/comment/delete", methods=["POST"])
def comment_delete():
    num_receive = request.form['num_give']
    db.comment.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5001, debug=True)