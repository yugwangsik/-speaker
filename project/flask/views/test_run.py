
def check():
    url = "http://localhost:10001/index/t"
    datas = {'data':data}
    ad = requests.post(url, json=datas)
    if ad == "1":
        subprocess.run(['python3 /home/pi/speaker_project/project/url/test.py'], shell=True)
        data = "0"
        url = "http://localhost:10001/index/tt"
        datas = {'data':data}
        requests.post(url json=datas)

while True:
    check()
