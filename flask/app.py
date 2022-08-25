from contextlib import redirect_stderr
from typing import Collection
from click import password_option
from flask import *
import pymongo
from flask_login import LoginManager
import json
import requests
from random import randint

client = pymongo.MongoClient(
    "mongodb+srv://root:zxc50053@mycluster.7tjho.mongodb.net/?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')
db = client.member_system


app = Flask(
    __name__,
    static_folder="static",  # 靜態檔案的資料夾名稱,
    static_url_path="/")  # 靜態檔案對應的網址路徑

# 所有在 static 資料夾底下的檔案，都對應到網址路徑/檔案名稱

app.secret_key = "zxc50053"
# app.route("/")


@app.route("/")
def index():
    if request.method == 'GET':
        return render_template("index.html")

# Rasa test


@app.route("/msgsend", methods=["POST"])
def msgsend():
    val = request.form['text']
    data = json.dumps({"sender": "Rasa", "message": val})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    res = requests.post(
        'http://localhost:5005/webhooks/rest/webhook', data=data, headers=headers)
    res = res.json()
    print('------------------------')
    print(res)
    print('------------------------')
    if len(res) == 1:
        # val = res[0]['text']
        # return val
        return json.dumps([{'type': 'text', 'data': res[0]['text']}])
    else:
        return_val = []  # 要回傳的陣列
        for rr in res:
            rr_list = list(rr.keys())  # 抓陣列value
            # 如果value=text就是文字
            # 如果png在image裡就是圖片
            # 不然就是影片
            print(rr_list)
            if rr_list[1] == 'text':
                return_val.append({'type': 'text', 'data': rr['text']})
            elif '.jpg' in rr['image'] or '.png' in rr['image']:
                return_val.append({'type': 'image', 'data': rr['image']})
            else:
                return_val.append({'type': 'video', 'data': rr['image']})
        print(return_val)
        return json.dumps(return_val)

        # print(res)
        # val = {
        #     "data": res[0]['text'],
        #     "pic": res[1]['image']
        # }
        # print(val)
        # return val

    # val = res[0]['text']
    # return val


@app.route("/member")
def member():
    if "nickname" in session:
        return render_template("member.html")
    else:
        return redirect("/")


@app.route("/error")  # /error?msg=錯誤訊息
def error():
    message = request.args.get("msg", "發生錯誤，請聯繫客服")
    return render_template("error.html", message=message)


@app.route("/signup", methods=["POST"])
def signup():
    # 從前端接收資料
    nickname = request.form["nickname"]
    email = request.form["email"]
    password = request.form["password"]
    # 根據接收到的資料，和資料庫互動
    collection = db.user
    if email is None:
        return redirect("/error?msg=帳號不可為空白")
    # 檢查是否有相同 Email 的文件資料
    result = collection.find_one({
        "email": email
    })
    if result != None:
        return redirect("/error?msg=信箱已經被註冊")
    # 把資料放進資料庫，完成註冊

    print(email)
    collection.insert_one({
        "nickname": nickname,
        "email": email,
        "password": password
    })
    return redirect("/test")


@app.route("/signin", methods=["POST"])
def signin():
    email = request.form["email"]
    password = request.form["password"]

    collection = db.user
    # 檢查信箱密碼是否正確
    result = collection.find_one({
        "$and": [
            {"email": email},
            {"password": password}
        ]
    })
    # 找不到對應資料，登入失敗，導向到錯誤頁面
    if result == None:
        return redirect("/error?msg=帳號或密碼輸入錯誤")
    # 登入成功，導向到會員頁面
    session["nickname"] = result["nickname"]
    return redirect("/member")


@app.route("/signout")
def signout():
    del session["nickname"]
    return redirect("/")


# @app.route("/register")
# def register():
#     return render_template("register.html")


# @app.route("/login")
# def login():
#     return render_template("login.html")


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/record", methods=["POST"])
def record():
    record = db.record
    name = request.values['studentname']
    date = request.values['date']
    before = request.values['before']
    problem = request.values['problem']
    solution = request.values['solution']

    record.insert_one({
        "studentname": name,
        "date": date,
        "before": before,
        "problem": problem,
        "solution": solution,
    })
    return redirect("/member")


app.run(port=8080)
