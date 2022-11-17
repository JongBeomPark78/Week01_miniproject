from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.bkcsdxn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# JWT 토큰을 만들 때 필요한 비밀문자열입니다. 아무거나 입력해도 괜찮습니다.
# 이 문자열은 서버만 알고있기 때문에, 내 서버에서만 토큰을 인코딩(=만들기)/디코딩(=풀기) 할 수 있습니다.
SECRET_KEY = 'SPARTA'

# JWT 패키지를 사용합니다. (설치해야할 패키지 이름: PyJWT)
import jwt

# 토큰에 만료시간을 줘야하기 때문에, datetime 모듈도 사용합니다.
import datetime

# 회원가입 시엔, 비밀번호를 암호화하여 DB에 저장해두는 게 좋습니다.
# 그렇지 않으면, 개발자(=나)가 회원들의 비밀번호를 볼 수 있으니까요.^^;
import hashlib


#################################
##  HTML을 주는 부분             ##
#################################

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/playerinfo')
def playerinfo():
    return render_template('playerinfo.html')

#################################
##  승률 API                  ##
#################################
@app.route("/winning_rate", methods=["GET"])
def winning_rate():
    winning_rate_list = list(db.winning_rate.find({}, {'_id': False}))
    return jsonify({'winning_rate': winning_rate_list})


@app.route("/winning_rate/increase", methods=["POST"])
def increase():
    try:
        token_receive = request.cookies.get('mytoken')
        country_num_receive = request.form['country_num_give']
        korea_receive = request.form['korea_give']
        drow_receive = request.form['drow_give']
        country_receive = request.form['country_give']
        print(country_num_receive)
        print(korea_receive)
        print(drow_receive)
        print(country_receive)

        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        userinfo = db.user.find_one({'id': payload['id']}, {'_id': 0})

        usercheck = db.increase.find_one({'country_key': int(country_num_receive), "userid": userinfo['id']})
        print(userinfo['id'])
        print(usercheck)

        if (usercheck):
            return jsonify({'msg': '이미 투표하셨습니다.'})
        else:
            country_map = db.winning_rate.find_one({'country_num': int(country_num_receive)})
            if (int(korea_receive) == 1):
                db.winning_rate.update_one({'country_num': int(country_num_receive)},
                                           {'$set': {
                                               'winning_rate_count_korea': country_map[
                                                                               'winning_rate_count_korea'] + 1}})
                doc = {
                    "userid": userinfo['id'],
                    "country_key": int(country_num_receive),
                }
                db.increase.insert_one(doc)
                return jsonify({'msg': '한국 투표 완료!'})
            elif (int(drow_receive) == 2):
                db.winning_rate.update_one({'country_num': int(country_num_receive)},
                                           {'$set': {
                                               'drow_count': country_map['drow_count'] + 1}})
                doc = {
                    "userid": userinfo['id'],
                    "country_key": int(country_num_receive),
                }
                db.increase.insert_one(doc)
                return jsonify({'msg': '무승부 투표 완료!'})
            else:
                db.winning_rate.update_one({'country_num': int(country_num_receive)},
                                           {'$set': {
                                               'winning_rate_count_country': country_map[
                                                                                 'winning_rate_count_country'] + 1}})
                doc = {
                    "userid": userinfo['id'],
                    "country_key": int(country_num_receive),
                }
                db.increase.insert_one(doc)
                if (int(country_num_receive) == 1):
                    return jsonify({'msg': '포르투갈 투표 완료!'})
                elif (int(country_num_receive) == 2):
                    return jsonify({'msg': '가나 투표 완료!'})
                else:
                    return jsonify({'msg': '우루과이 투표 완료!'})

    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


#################################
##  코멘트 API                  ##
#################################

# 코멘트 저장
@app.route("/comment", methods=["POST"])
def comment_post():
    try:
        token_receive = request.cookies.get('mytoken')
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        userinfo = db.user.find_one({'id': payload['id']}, {'_id': 0})

        comment_receive = request.form['comment_give']
        comments_count = db.Counts.find_one({'counts': "counts"}, {'_id': False})
        count = comments_count['comments_count'] + 1

        doc = {
            'num': count,
            'comment': comment_receive,
            'done': 0
        }
        db.Comments.insert_one(doc)
        db.Counts.update_one({'counts': 'counts'}, {'$set': {'comments_count': count}})

        return jsonify({'msg': '등록 완료!'})
    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


# 코멘트 불러오기
@app.route("/comment", methods=["GET"])
def comment_get():
    comment_list = list(db.Comments.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


# 코멘트 삭제
@app.route("/comment/delete", methods=["POST"])
def comment_delete():
    num_receive = request.form['num_give']
    db.Comments.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})


#################################
##  로그인을 위한 API            ##
#################################

# [회원가입 API]
# id, pw, nickname을 받아서, mongoDB에 저장합니다.
# 저장하기 전에, pw를 sha256 방법(=단방향 암호화. 풀어볼 수 없음)으로 암호화해서 저장합니다.
@app.route('/api/register', methods=['POST'])
def api_register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    db.user.insert_one({'id': id_receive, 'pw': pw_hash, 'nick': nickname_receive})

    return jsonify({'result': 'success'})


# [로그인 API]
# id, pw를 받아서 맞춰보고, 토큰을 만들어 발급합니다.
@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # 회원가입 때와 같은 방법으로 pw를 암호화합니다.
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # id, 암호화된pw을 가지고 해당 유저를 찾습니다.
    result = db.user.find_one({'id': id_receive, 'pw': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


# [유저 정보 확인 API]
# 로그인된 유저만 call 할 수 있는 API입니다.
# 유효한 토큰을 줘야 올바른 결과를 얻어갈 수 있습니다.
# (그렇지 않으면 남의 장바구니라든가, 정보를 누구나 볼 수 있겠죠?)
@app.route("/login_check", methods=["POST"])
def login_check():
    try:
        token_receive = request.cookies.get('mytoken')
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        userinfo = db.user.find_one({'id': payload['id']}, {'_id': 0})
        return jsonify({'result': 'success'})
    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail'})


#################################
##  선수카드 API            ##
#################################


@app.route("/player", methods=["GET"])
def player_get():
    player_list = list(db.player.find({}, {'_id': False}))
    return jsonify({'player': player_list})


@app.route("/athlete_like_post", methods=["POST"])
def Like():
    # 로그인된 상태인지 확인한다. 프론트에서 보내주는 토큰을 받아서 decode 한 후 id값을 찾는다.
    # 만약 user_info가 Like_list(DB)에서 안찾아지면 좋아요를 누르적이 없다는 뜻이다. 그럼 DB에 추가하고 증가하는
    # 작업이 진행되게 한다.
    # 만약 user_info가 Like_list(DB)에서 찾아진다면 이미 좋아요를 눌렀다는 뜻. 그럼 취소가 되어야 하기 때문에
    # Like_list(DB)에서 id를 삭제하고 like 삭제 작업을 진행해야 한다.
    # 궁금증 ?? 만약 아이디가 찾아진다면 여기서 삭제를 해야하는가? 아니면 다른 곳에서 삭제해야하는가?
    try:
        token_receive = request.cookies.get('mytoken')
        number_receive = request.form['card_number']

        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        userinfo = db.user.find_one({'id': payload['id']}, {'_id': 0})
        user_info = db.Like_list.find_one({'id': userinfo['id']})
        print(user_info)

        Like_Count = db.player.find_one({"Card_number": int(number_receive)})
        print(Like_Count['Like_Count'])
        if (user_info):
            db.player.update_one({'Card_number': int(number_receive)}, {'$set': {'Like_Count': Like_Count['Like_Count'] - 1}})
            db.Like_list.delete_one({'id': userinfo['id']})
            return jsonify({'msg': '좋아요 취소'})
        else:
            # ID 추가해주기
            doc = {'id': payload['id'], 'Card_number': int(number_receive)}
            db.Like_list.insert_one(doc)
            # COUNT 값 1 더해주기

            db.player.update_one({'Card_number': int(number_receive)}, {'$set': {'Like_Count': Like_Count['Like_Count'] + 1}})

            return jsonify({'msg': '좋아요 완료'})

    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
