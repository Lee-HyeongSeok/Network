## 2차 설계 - DDoS 공격

***

<br> 

### :pushpin: 실습 환경(로컬 내에서 실습)

- 공격자 : 칼리 리눅스

  - IP : 192.168.219.176
  - apache bench 웹 부하 테스트 툴 사용(HTTP Get Flooding)
  - python code 사용(HTTP CC Attack)
  - python code 사용(Dynamic HTTP Request Flooding)

- 웹 서버 : 우분투

  - IP : 192.168.219.126
  - web server port : 8080
  - URL : http://192.168.219.126:8080/freeweb-1.0.0-BUILD-SNAPSHOT/home/main
  - apache2 사용
  - Tomcat 8 사용 
  - MySql 8.0.23 사용 

  <br> 

### :pushpin: HTTP Get Flooding

- Apache Bench를 사용하여 Get Flooding 실습

- 칼리 리눅스에 apache bench 설치

- **sudo ab -n 10000 -c 100 http://192.168.0.152:8080/freeweb-1.0.0-BUILD-SNAPSHOT/home/main** 명령어 수행

  - 100 명의 클라이언트가 10000 번의 Get Request를 전송

- 결과

  ![getFlooding결과](https://user-images.githubusercontent.com/55940552/121564975-f87ef480-ca56-11eb-9965-4251d9f8a7f7.PNG) 

<br>

### :pushpin: HTTP CC Attack

- [alienwhatever's Github](https://github.com/alienwhatever/TakeitDown) 에서 칼리 리눅스에 **TakeitDown**을 다운로드

- 대상 웹서버(우분투)의 URL이 hosting이 되어있지 않기 때문에 takeitdown.py에서 header 직접 수정

  - IP 부분을 대상 웹 서버의 IP로 변경시켜 준다.
  - **172.30.1.19:8080** 을 **192.168.219.126:8080** 으로 변경해야 한다.

  ![python코드1](https://user-images.githubusercontent.com/55940552/121565733-b904d800-ca57-11eb-8b49-1006e3b1b4c1.PNG) 

- 칼리 리눅스에서 **python3 takeitdown.py 192.168.219.126 8080** 명령어 실행

  > 기본 실행 format
  >
  > **python3 takeitdown.py <host> <port>**

- 결과

  ![패킷캡쳐결과](https://user-images.githubusercontent.com/55940552/121566342-5eb84700-ca58-11eb-9dfa-b1514df32cb6.PNG) 

<br>



### :pushpin: Dynamic HTTP Request Flooding

- python3 명령어 실행 시 인수 값으로 아무것도 전달하지 않고 실행한다.

- 내부 코드에서 호스트를 지정해야 한다.

- **python3 dynamic_request.py** 실행

- while문으로 socket send를 계속보내기 떄문에 Ctrl+c 인터럽트로 종료해야 한다.

- 결과

  ![패킷구집](https://user-images.githubusercontent.com/55940552/122660672-11f21000-d1be-11eb-9a4b-af86eae64edb.PNG) 

- 공격 실패

  - 실패 요인은 Internal Server Error로 추정
  - 여러 페이지를 요청하는 패킷은 캡쳐되는 것으로 확인

***

<br> **[출처]**

[alienwhatever's Github](https://github.com/alienwhatever/TakeitDown)

[한국산업기술대학교](www.kpu.ac.kr)

