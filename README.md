# Django_SNS_PJ
Django로 구현한 SNS Project

<br>

# 프로젝트 개요
* 프로젝트 명 : Django_SNS_PJ
* 개발 인원 : 1명
* 개발 기간 : 2023.04 ~ 2023.06
* 개발 언어 : Python 3.10
* 개발 환경 : Django 4.2
* DB : MariaDB
* 버전 관리 : git&github

<br>

# 요구사항 분석
### 1. HOME
1. 로그인 시
    - 사용자 상세 페이지로 이동할 수 있다.
    - 로그아웃할 수 있다.
2. 비로그인 시
    - 로그인, 회원가입 페이지로 이동할 수 있다.
3. 공통
    - 사용자를 검색할 수 있다.
    - 모든 피드를 볼 수 있다.
    - 피드 작성 페이지로 이동할 수 있다.

### 2. 피드 생성
1. 로그인 시
    - 피드(제목, 내용, 이미지)를 작성할 수 있다.
2. 비로그인 시
    - 로그인을 위해 로그인 페이지로 이동한다.

### 3. 피드 상세 페이지
1. 로그인 시(본인)
    - 피드를 수정, 삭제할 수 있다.
2. 로그인 시(타인)
    - 피드를 확인할 수 있다.
3. 비로그인 시
    - 로그인을 위해 로그인 페이지로 이동한다.
4. 공통
    - 댓글을 남길 수 있어야 한다.
    - 본인의 댓글을 수정, 삭제 할 수 있다.
    - 좋아요가 몇 개인지, 누가 눌렀는지 확인할 수 있다.
    - 좋아요를 누를 수 있다.
    - 피드 작성자의 상세 페이지로 이동할 수 있다.

### 4. 피드 수정 페이지
1. 로그인 시
    - 피드(제목, 내용, 이미지)를 수정할 수 있다.

### 5. 댓글 수정 페이지
1. 로그인 시
    - 댓글을 수정할 수 있다.

### 6. 댓글 삭제 페이지
1. 로그인 시
    - 댓글을 삭제할 수 있다.

### 7. 프로필 생성
1. 프로필(이미지, 닉네임, 자기소개, 이메일, 성별)을 설정할 수 있다.

### 8. 프로필 수정
1. 프로필(이미지, 닉네임, 자기소개)을 수정할 수 있다.

### 9. 비밀번호 변경
1. 비밀번호를 변경할 수 있다.

### 10. 계정 삭제
1. 계정을 삭제할 수 있다.

### 11. 팔로우
1. 사용자를 팔로우 할 수 있다.
2. 팔로우를 취소할 수 있다.
3. 팔로우 목록을 확인할 수 있다.
4. 팔로워 목록을 확인할 수 있다.

<br>

# UI 설계
### 1. 메인 페이지
<img width="800" alt="home" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/bdfe1606-17b8-4c4d-8665-07004a7f53ab">

### 2. 로그인
<img width="400" alt="login" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/5181fc68-c07c-4cf4-bea4-af991b64b6a3">

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