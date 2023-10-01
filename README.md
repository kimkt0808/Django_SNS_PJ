# Django_SNS_PJ
Django_SNS_PJ는 사용자들이 실시간으로 정보를 공유하고 소통할 수 있는 소셜 네트워크 서비스입니다.

이 SNS 서비스는 사용자가 자신의 생각과 경험을 게시글 형태로 공유하고, 다른 유저들의 게시글에 댓글을 달거나 좋아요를 표시하는 등의 인터랙션을 할 수 있습니다.

또한, 팔로우 시스템을 통해 특정 유저의 게시글만 모아 볼 수 있으며, 채팅(Public, Private) 기능도 제공하여 유저간 직접적으로 대화를 나누는 것도 가능합니다.

<br>

# 프로젝트 개요
* 프로젝트 명 : Django_SNS_PJ
* 개발 인원 : 1명
* 개발 기간 : 2023.04 ~ 2023.09
* 개발 언어 : Python 3.10
* 개발 환경 : Django 4.2, Docker 24.0.2
* DB : MariaDB 11.2.0
* 버전 관리 : git&github

<br>

# 요구사항 분석
### 0. 헤더
- 로그인
  - 나의 계정 상세 페이지로 이동할 수 있다.
  - 나의 DM 목록을 확인할 수 있다.
- 비 로그인
  - 회원가입, 로그인 페이지로 이동할 수 있다.
- 공통
  - 피드 메인, 채팅 메인으로 이동할 수 있다.
  - 유저를 검색할 수 있다.

### 1. 메인
- 로그인
  - 특정 유저의 피드 상세 페이지로 이동할 수 있다.
  - 새 피드를 작성할 수 있다.

- 공통
  - 모든 유저들은 다른 유저의 피드를 랜덤으로 확인할 수 있다.

### 2. 회원 가입
- 새로운 유저는 아이디와 비밀번호 등 필요한 정보를 입력하여 등록할 수 있다.
- 제약 사항
  - 아이디는 150자 이하(문자/숫자)만 가능하다. (특수문자는 "@.+-_"만 가능)
  - 비밀번호는 최소 8자 이상이어야 한다.
  - 비밀번호는 숫자와 문자의 조합으로 이루어져야 하며, 아이디와 같을 수 없다.
  - 이미 존재하는 유저의 아이디는 사용할 수 없다.

### 3. 로그인
- 등록된 유저는 아이디와 비밀번호를 입력 후 서비스를 이용할 수 있다.
- 아래에 기능을 이용할 수 있다.
   - 피드 (생성/상세/수정/삭제)
   - 프로필/비밀번호 수정
   - 계정 삭제
   - 팔로우
   - 댓글 (작성/수정/삭제)
   - 좋아요
   - 채팅 (Public/Private)
- 아이디와 비밀번호의 대/소문자를 구분한다.
- 아이디 또는 비밀번호가 일치하지 않는 경우 "올바른 사용자 이름과 비밀번호를 입력하십시오."를 보여준다.

### 4. 피드
- 로그인
  - 피드 (제목/내용/이미지)를 작성할 수 있다.
  - 피드 (제목/내용/이미지)를 필수로 입력해야 하며, 그렇지 앟은 경우 "이 입력란을 작성하세요."를 보여준다.

### 5. 피드 상세
- 로그인
  - 해당 피드의 내용, 작성자 정보, 댓글 목록 등을 확인할 수 있다.
  - 해당 피드에 좋아요를 누를 수 있다.
  - 해당 피드에 댓글을 작성하고, 작성한 댓글을 수정하거나 삭제할 수 있다.

### 6. 댓글
- 로그인
  - 피드에 댓글을 작성할 수 있다.
  - 자신이 작성한 댓글을 수정하거나 삭제할 수 있다.
  - 댓글은 모든 유저가 볼 수 있어야 한다.

### 7. 채팅(Public)
- 로그인
  - 공개 채팅방을 생성할 수 있다.
  - 채팅방은 썸네일, 제목, 설명을 입력하여 생성한다.
  - 선택적으로 패스워드를 설정하여 접근 제어를 할 수 있다.
- 공통
  - 채팅방 목록을 확인할 수 있다. (제목/설명/생성 날짜)

### 8. 채팅(Private)
- 로그인
  - 다른 유저와 개인적으로 1:1 대화를 나눌 수 있는 비공개 채팅방을 생성할 수 있다.
  - 자신이 참여 중인 채팅방 목록을 볼 수 있어야 한다.

### 9. 프로필
- 로그인
  - 자신의 프로필(이미지/닉네임/소개/이메일/성별) 정보를 설정하고 확인할 수 있다.
  - 자신의 피드 목록을 확인할 수 있다.
  - 자신의 프로필 정보 중 이미지, 닉네임, 소개 등 일부 항목만 수정 가능하다.

### 10. 비밀번호 변경 페이지
- 로그인
  - 유저는 변경할 비밀번호를 입력 후 비밀번호 변경을 요청한다.

### 11. 계정 삭제 페이지
- 로그인
  - 계정과 관련된 모든 데이터와 함께 계정을 영구삭제를 요청한다.

### 12. 팔로우
- 로그인
  - 유저간 팔로우/언팔로우가 가능하다.
  - 내가 팔로우한 유저의 목록을 확인할 수 있다.

### 13. 검색
- 공통
  - 아이디를 기준으로 유저들 중 원하는 유저를 검색할 수 있다.
  - 채팅방(Public)은 최신 순으로 정렬되며 내가 생성한 채팅방 순으로 정렬할 수 있다.

<br>

# UI 설계
### 1. 메인 페이지
<img width="800" alt="home" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/3a68f3cc-6bbd-4347-9010-da7446c5eaf9">

### 2. 로그인
<img width="500" height="600" alt="login" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/5181fc68-c07c-4cf4-bea4-af991b64b6a3">

### 3. 피드
<img width="846" alt="feed_detail" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/c021b8dc-6b4c-4ab5-be98-616aac40b28d">

### 4. 유저
<img width="1069" alt="user_detail" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/51d63521-72bb-483d-aa6c-6ebe0a7d5519">

### 5. 프로필
<img width="400" alt="profile_update" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/5104bccc-c4e6-410e-beae-fe9ecf222040">

### 6. 검색
<img width="700" alt="search_ui" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/0c8525c0-ccf9-4e84-8683-750b94d00cd9">

### 7. 채팅(Public)
<img width="1279" alt="채팅메인" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/97d9a4f9-5b14-4a85-a23f-e1eb02964cb9">
<img width="1012" alt="채팅방생성" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/5b6bb9d6-c9bc-4d08-982d-119412c03388">
<img width="1001" alt="채팅방상세" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/b0251dd8-9821-4c63-b005-757868e19fc4">

### 8. 채팅(Private)
<img width="1000" alt="디엠상세" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/5d1e9eb6-a09f-40b0-bc08-4647fe5e0729">

<br>

# DB 설계
### ERD
<img width="750" alt="erd" src="https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/f24800fb-57fa-4ad1-acca-4fdaec2b9dc8">

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

### Chat(Public)
![room](https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/7d02ebdb-487f-49b4-8325-0a8c76686874)

### Chat(Private)
![private_room](https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/06fe6ce7-5e9e-496f-b33b-df9b4c5bf663)

### Like
![like](https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/8efdc211-badd-4def-bc60-2b39759e654a)

### Search
![search](https://github.com/8azelnut/Django_SNS_PJ/assets/130894141/7e0f4c65-f516-46fd-9711-a5b2bc85f908)