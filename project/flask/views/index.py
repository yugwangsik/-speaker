from flask.templating import render_template
from flask import Blueprint, url_for, render_template, flash, request, session, g, jsonify
import os


bp = Blueprint('index', __name__, url_prefix='/index')

val = "0"       # 센서 서버 전송 판단 변수( 0이면 전송X, 1이면 전송O )



@bp.route("/test", methods=["GET", "POST"])
def test():
    global keyword
    rawData = request.get_json()
    print(rawData["data"])
    return " "



@bp.route("/sign", methods=["GET", "POST"])    # '스캔' 명령시 val값 변경
def sign():
    global val
    rawData = request.get_json()
    val = rawData["val"]
    return " "



@bp.route("/check", methods=["GET", "POST"])   # 센서 실행 파일에서 지속적으로 확인
def check():
    global val
    return jsonify({
        "val":val
    })



@bp.route("/change", methods=["GET", "POST"])   # '그만' 명령시 val값 변경
def change():
    global val
    rawData = request.get_json()
    val = rawData["val"]
    return " "


@bp.route("/update", methods=["GET", "POST"])   # '그만' 명령시 val값 변경
def update():
    os.system("sshpass -p raspberry scp /home/pi/upload/test.txt pi@192.168.1.50:/home/pi/upload")
    return " "
