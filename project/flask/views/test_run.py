#from flask.templating import render_template
#from flask import Blueprint, url_for, render_template, flash, request, session, g, jsonify
import requests
import timer

ad = None

@timer.logging_time
def check():
    subprocess.run(['python3 /home/pi/speaker_project/project/url/test.py'], shell=True)
    data = "0"
    url = "http://localhost:10001/index/tt"
    datas = {'data':data}
    requests.post(url, json=datas)

while True:
    url = "http://localhost:10001/index/t"
    data = " "
    datas = {'data':data}
    ad = requests.post(url, json=datas)
    if ad == "1":
        check()
