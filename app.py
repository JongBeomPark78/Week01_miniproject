from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.wd6li.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

from flask import Flask, render_template, request, jsonify, redirect, session
app = Flask(__name__)

import certifi
ca = certifi.where()

SECRET_KEY = 'SPARTA'

import jwt
import datetime
import hashlib






@app.route('/')
def home():
   return render_template('index.html')

@app.route('/playerinfo')
def playerinfo():
    return render_template('playerinfo.html')



@app.route("/player", methods=["GET"])
def player_get():
    player_list = list(db.player.find({}, {'_id': False}))
    return jsonify({'player':player_list})

@app.route("/athlete_like_post", methods=["POST"])
def Like():
    number_receive = request.form['card_Number']

    #로그인된 상태인지 확인한다. 프론트에서 보내주는 토큰을 받아서 decode 한 후 id값을 찾는다.
    #만약 user_info가 Like_list(DB)에서 안찾아지면 좋아요를 누르적이 없다는 뜻이다. 그럼 DB에 추가하고 증가하는
    #작업이 진행되게 한다.
    #만약 user_info가 Like_list(DB)에서 찾아진다면 이미 좋아요를 눌렀다는 뜻. 그럼 취소가 되어야 하기 때문에
    #Like_list(DB)에서 id를 삭제하고 like 삭제 작업을 진행해야 한다.
    #궁금증 ?? 만약 아이디가 찾아진다면 여기서 삭제를 해야하는가? 아니면 다른 곳에서 삭제해야하는가?
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.Like_list.find_one({"id": payload['id']})

        if user_info is None:
            # ID 추가해주기
            doc = {'ID': payload['id'], 'Card_number': number_receive}
            db.Like_list.insert_one(doc)
            # COUNT 값 1 더해주기
            db.player.update_one({'Card_number': number_receive}, {'$set': {'Like_Count': 'Like_Count' + 1}})

            return jsonify({'msg': '좋아요 완료'})

        else:
            db.player.update_one({'Card_number': number_receive}, {'$set': {'Like_Count': 'Like_Count' - 1}})
            db.Like_list.delete_one({'id': payload['id']})
            return jsonify({'msg': '좋아요 취소'})

    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})





if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)