# 1. 목표와 기능
<h2>목표</h2>
starcraft blog 만들기

<h2>기능</h2>
<ul>
  <li>회원가입</li>
  <li>로그인/로그아웃</li>
  <li>CRUD</li>
  <li>댓글 작성 가능</li>
  <li>조회수 체크</li>
</ul>

# 2. 요구사항
<h3>2.1</h3>
<ul>
  <li>UI 스타일 제작</li>
  <li>클래스형 뷰 개발</li>
  <li>모놀리식 장고로 개발</li>
  <li>데이터베이스 구조 설계(필수)</li>
</ul>

<h3>2.2 단계별 요구사항(0~3단계)</h3>
<ul>
  <li>0단계: Django Admin을 이용한 게시글 읽기 및 메인페이지 구현하기</li>
  <li>1단계: 블로그 CRUD 기능 구현하기</li>
  <li>2단계: 로그인/회원가입 기능을 이용하여 블로그 구현하기(인증 기능 추가)</li>
  <li>3단계: 블로그 기능 외 추가 기능 작성 및 배포</li>
</ul>

# 3. 프로젝트 구조
<h2>- urls 구조</h2>
<br>
<br>

|APP|URL|Views Func Name|HTML File Name|Note|
|------|---|---|---|---|
|blog|'/'|post_list|post_list.html|게시판 목록|
|blog|'write/'|post_write|post_write.html|게시글 작성|
|blog|'<int:pk>/'|post_detail|post_detail.html|게시글 내용|
|blog|'edit/<int:pk>/'|post_edit|post_edit.html|게시글 수정|
|blog|'delete/<int:pk>/'|post_delete|post_delete.html|게시글 삭제|
|blog|'comment_new/<int:pk>/'|comment_new|comment_new.html|게시글 댓글 작성|
<br>
<br>

|APP|URL|Views Func Name|HTML File Name|Note|
|------|---|---|---|---|
|accounts|'register/'|register|register.html|회원가입
|accounts|'login/'|login|login.html|로그인
|accounts|'logout/'|logout|logout.html|로그아웃
|accounts|'profile/'|profile|profile.html|유저정보


<br>
<br>

<pre>
<h2>- TREE 구조</h2>
--blog_project
│── mysite
│   ├── accounts
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── admin.cpython-312.pyc
│   │   │   ├── apps.cpython-312.pyc
│   │   │   ├── models.cpython-312.pyc
│   │   │   ├── urls.cpython-312.pyc
│   │   │   └── views.cpython-312.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       └── __init__.cpython-312.pyc
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── blog
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── admin.cpython-312.pyc
│   │   │   ├── apps.cpython-312.pyc
│   │   │   ├── forms.cpython-312.pyc
│   │   │   ├── models.cpython-312.pyc
│   │   │   ├── urls.cpython-312.pyc
│   │   │   └── views.cpython-312.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── 0001_initial.cpython-312.pyc
│   │   │       └── __init__.cpython-312.pyc
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── blog_project_ERD.png
│   ├── db.sqlite3
│   ├── manage.py
│   ├── media
│   │   └── blog
│   │       └── images
│   │           └── 2023
│   │               └── 11
│   │                   └── 07
│   │                       ├── 빨무.png
│   │                       ├── 빨무_eFc615g.png
│   │                       └── 빨무_t8xAlWT.png
│   ├── requirements.txt
│   ├── static
│   │   └── 배경.png
│   ├── templates
│   │   ├── 404.html
│   │   ├── accounts
│   │   │   ├── form.html
│   │   │   └── profile.html
│   │   └── blog
│   │       ├── form.html
│   │       ├── post_confirm_delete.html
│   │       ├── post_detail.html
│   │       └── post_list.html
│   └── tutorialdjango
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-312.pyc
│       │   ├── settings.cpython-312.pyc
│       │   ├── urls.cpython-312.pyc
│       │   └── wsgi.cpython-312.pyc
│       ├── asgi.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
├── Readme.html
</pre>


<h2>- ERD 구조</h2>

![blog_project](https://github.com/Charles0823/blog_project/assets/142385973/1cb6dcdc-340d-4ff3-8ca8-0e84a2511fc7)


# 4. 개발 환경
<img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=HTML&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS&logoColor=white"/>
<img src="https://img.shields.io/badge/PYTHON-3776AB?style=flat-square&logo=PYTHON&logoColor=white"/>
<img src="https://img.shields.io/badge/DJANGO-092E20?style=flat-square&logo=DJANGO&logoColor=white"/>

# 5. 메인 기능
<ul>
  <li>회원가입, 로그인, 프로필 확인
  </li>
</ul>

  ![회원가입,로그인,프로필](https://github.com/Charles0823/blog_project/assets/142385973/712fe431-eb92-4ab7-82c7-637c874350da)
  <ul>
    <li>비로그인시 글작성 및 댓글작성 불가
    </li>
  </ul>
  
  ![비로그인_글,댓글작성](https://github.com/Charles0823/blog_project/assets/142385973/333485d7-20d9-4974-9a8c-fc4b7584f501)
  <ul>
    <li>로그인 후 글작성 및 댓글작성, 수정
    </li>
  </ul>
  
![로그인_글,댓글작성,수정](https://github.com/Charles0823/blog_project/assets/142385973/2ac87200-6efe-459a-8652-33d5d331db4b)

<ul>
  <li>본인이 작성한 글 삭제
  </li>
</ul>

![글 삭제 취소,확인](https://github.com/Charles0823/blog_project/assets/142385973/480a3f30-e7b5-4968-b59b-771de5617ecf)

<ul>
  <li>존제하지 않는 페이지 접속시
  </li>
</ul>

![404페이지](https://github.com/Charles0823/blog_project/assets/142385973/e65a587e-c2f5-429d-8ff9-4b5ee5807682)



# 6. 개발하면서 느낀점
오류가나오면 오류를 읽고 해결하려고 하기 보다는 새로 해버리는 식으로 했는데 이번 블로그 프로젝트를 진행하면서 오류가 나도 뭐때문인지 알지 못해 한참을 해매서 진행이 자꾸 막히게 되어 답답함을 느꼈고 오류를 일일이 확인하고 해결하고 모르는게 많으니 좀 더 열심히 공부 해야겠다고 생각했습니다. 그리고 WBS를 작성하지 않고 그날 그날 진행 순서를 정하지 않고 하다보니 너무 중구난방식으로 프로젝트가 진행된다는걸 느꼈고 왜 WBS를 만들고 진행하는지를 알게 되었습니다.
프로젝트를 시작할때 굉장히 막막했는데 배운걸 차근차근 하나씩 작성해보니 부족하더라도 조금씩 만들어지는 모습을 보면서 앞으로 더욱 많은걸 배우고 코드를 작성하다 보면 추후 스스로 만족할 만한 수준의 프로젝트를 혼자서도 만들 수 있을것 같다는 생각이 들었습니다.
