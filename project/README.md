
## Text.py
- #### def tts(text)
tts() 함수를 호출할 때 매겨변수로 string을 넘겨주면 해당 데이터를 text변수로 활용한다. text변수는 Google Text-To-Speech API를 통해 MP3파일로 리턴 받을 수 있다.

- #### def success()
success() 함수를 호출하면 사용자가 운동 횟수를 모두 달성하면 운동이 종료 되었다고 알려주는 음성이 재생 된다.

- #### def count(cnt)
count() 함수를 호출할 때 매겨변수로 string을 넘겨주면 해당 데이터를 cnt변수로 활용한다. cnt변수는 현재 사용자가 진행한 운동 횟수에 따라서 그에 맞는 음성이 재생 된다.


## Nordic.py
주변 블루투스 기기 중 Nordic 기기에 해당하는 것만 Mac 주소를 list로 만든 후 해당 기기들의 UART에 해당하는 UUID를 획득한다.

