# Django_SNS_PJ
Django로 구현한 SNS Project

<br>

# 프로젝트 개요
* 프로젝트 명 : Django_SNS_PJ
* 개발 인원 : 1명
* 개발 기간 : 2023.04 ~ 2023.06
* 개발 언어 : Python 3.10
* 개발 환경 : Django 4.2, Docker 24.0.2, bootstrap5, django-storages 1.13.2
* DB : MariaDB 11.2.0
* 버전 관리 : git&github

<br>

# 요구사항 분석
### 1. 메인
1. 비로그인 시 로그인, 회원 가입 페이지로 이동할 수 있다.
2. 로그인 시 유저 페이지로 이동할 수 있다.
3. 모든 피드를 볼 수 있으며, 새로운 피드를 작성할 수 있다.
4. 사용자를 검색할 수 있다.

### 2. 회원 가입
1. 아이디는 150자 이하(문자, 숫자)만 가능하다. (특수문자는 "@.+-_"만 가능)
2. 비밀번호는 최소 8자 이상이어야 한다.
3. 비밀번호는 숫자와 문자의 조합으로 이루어져야 하며, 아이디와 같을 수 없다.
4. 이미 존재하는 유저의 아이디는 사용할 수 없다.

### 3. 로그인
1. 로그인에 성공하면 아래에 기능을 이용할 수 있다.
   - 피드 생성, 상세, 수정, 삭제
   - 프로필, 비밀번호 수정
   - 계정 삭제
   - 팔로우
   - 댓글 작성, 수정, 삭제
   - 좋아요
2. 아이디와 비밀번호의 대/소문자를 구별한다.

### 4. 피드
1. 피드(제목, 내용, 이미지)를 작성할 수 있다.
2. 피드의 내용은 공백일 수 없다.
3. 비로그인 시 로그인을 위해 로그인 페이지로 이동한다.

### 5. 피드 상세
1. 로그인 시 아래에 기능을 이용할 수 있다.
   - 댓글 작성, 수정, 삭제
   - 좋아요
   - 피드 작성자의 상세 페이지로 이동
2. 비로그인 시 로그인을 위해 로그인 페이지로 이동한다.

### 6. 댓글
1. 로그인한 유저만 작성, 수정, 삭제 가능하다.
2. 내용을 반드시 입력해야 한다.
3. 피드가 삭제되면 댓글도 같이 삭제된다.

### 7. 프로필
1. 프로필(이미지, 닉네임, 소개, 이메일, 성별)을 설정, 삭제할 수 있다.
2. 프로필은 이미지, 닉네임, 소개만 수정할 수 있다.

### 8. 비밀번호 변경 페이지
1. 비밀번호를 변경할 수 있다.

### 9. 계정 삭제 페이지
1. 계정을 삭제할 수 있다.

### 10. 팔로우
1. 유저를 팔로우, 취소 할 수 있다. 
2. 팔로우, 팔로워 목록을 확인할 수 있다.

### 11. 검색
1. 유저를 검색할 수 있다. (아이디 기준)

<br>

# UI 설계
### 1. 메인 페이지
<img width="800" alt="home" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/bdfe1606-17b8-4c4d-8665-07004a7f53ab">

### 2. 로그인
<img width="350" height="400" alt="login" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/5181fc68-c07c-4cf4-bea4-af991b64b6a3">

### 3. 피드
<img width="846" alt="feed_detail" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/b398413c-0cd5-429a-8ed9-80aa6d9e5def">

### 4. 유저
<img width="1069" alt="user_detail" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/51d63521-72bb-483d-aa6c-6ebe0a7d5519">

### 5. 프로필
<img width="400" alt="profile_update" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/5104bccc-c4e6-410e-beae-fe9ecf222040">

### 6. 검색
<img width="700" alt="search_ui" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/0c8525c0-ccf9-4e84-8683-750b94d00cd9">

<br>

# DB 설계
### ERD
<img width="800" alt="ERD" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/79869d60-e509-4598-b1c0-c8949f13f887">

<br>

# API 설계
### Feeds
![feeds](https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/58435f06-1c87-4984-9ba7-328d0c0e88d2)

### Accounts
![accounts](https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/b7a9ba12-e614-4249-b6e4-84eb39e15428)

### Profile
![profile](https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/7fb856e2-7a26-4ff7-a819-022ac49f19b2)

### Comments
![comments](https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/b0712a27-4213-4dd4-b297-8f1aea1432f2)

### Follow
![follow](https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/8a9c4e6d-c313-460a-80ca-3acde86c590a)

### Like
![like](https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/8efdc211-badd-4def-bc60-2b39759e654a)

### Search
![search](https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/0c01ce60-1c86-4fad-8531-dc297a284f4f)

<br>

# 개선 및 유지보수
### 기능 추가
* 채팅기능

### 보완
* 비밀번호 찾기