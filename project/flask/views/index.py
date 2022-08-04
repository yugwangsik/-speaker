from flask.templating import render_template
from flask import Blueprint, url_for, render_template, flash, request, session, g, jsonify
import os
import subprocess
#import timer_test
import time



bp = Blueprint('index', __name__, url_prefix='/index')

val = "0"       # 센서 서버 전송 판단 변수( 0이면 전송X, 1이면 전송O )

def logging_time(original_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = original_fn(*args, **kwargs)
        end_time = time.time()
        print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time-start_time))
        return result
    return wrapper_fn

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


@bp.route("/tt", methods=["GET", "POST"])   # '그만' 명령시 val값 변경
@logging_time
def tt():
    print("Check")
    #subprocess.run(['python3 /home/pi/speaker_project/project/url/test.py'], shell=True)
    os.system("chromium-browser --kiosk http://34.64.199.227:9876/counter")
    return " "
