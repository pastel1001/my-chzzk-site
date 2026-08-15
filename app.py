Gemini와의 대화
.... .py로 카톡으로 보낼려 하는데... 지원하지 않는 양식이래...

카카오톡은 보안상의 이유로 .py (파이썬 파일)이나 .exe (실행 파일) 같은 프로그램 소스 파일이 직접 전송되는 것을 막아두었습니다.

이때는 파일 확장자(이름)를 살짝 속여서 보내는 꼼수를 쓰시면 아주 깔끔하게 해결됩니다!

방법 1: 파일 이름을 .txt로 바꿔서 보내기 (가장 추천!)
친구가 파일 확장자만 다시 .py로 바꾸면 되는 가장 쉽고 빠른 방법입니다.

작성하신 파이썬 파일(updown.py)의 이름을 마우스 우클릭 -> 이름 바꾸기 합니다.

파일 이름 끝의 .py를 .txt로 바꿔줍니다. (예: updown.txt)

"(파일 확장명을 변경하면...)" 경고창이 뜨면 그냥 예를 누르세요.

이 updown.txt 파일을 카카오톡으로 전송합니다. (텍스트 파일은 무사히 전송됩니다!)

친구가 받아야 할 안내:

받은 파일 이름을 다시 updown.py로 바꾸고 IDLE이나 파이썬에서 열어서 실행하라고 말해주면 끝입니다!

방법 2: 압축 파일(.zip)로 묶어서 보내기
파일이 여러 개이거나 파일 확장자 바꾸기가 귀찮다면 압축해서 보내시면 됩니다.

updown.py 파일 우클릭 -> 압축(ZIP) 파일로 압축을 누릅니다.

만들어진 updown.zip 파일은 카카오톡으로 바로 보내집니다.

친구는 파일 다운로드 후 압축을 풀어서 실행하면 됩니다.

💡 팁: 실행 후 바로 닫히는 것 방지하기!
아까 말씀드린 것처럼, 친구가 IDLE을 안 열고 .py 파일만 더블 클릭해서 실행할 경우 정답을 맞히자마자 검은 창이 닫혀버립니다.

친구한테 보내기 전에 맨 아래 break 바로 위에 input() 한 줄을 추가해서 아래처럼 만들고 저장해서 보내주세요!

Python
import random

a = random.randrange(0, 101)
print('1부터 100중 숫자를 입력하세요!')
count = 0

while True:
    b = int(input())
    count = count + 1
    if a == b:
        print('맞았습니다.')
        print(f'{count}번 만에 맞히셨습니다!')
        input('엔터를 누르면 프로그램이 종료됩니다...') # 👈 창이 닫히지 않게 대기!
        break
    elif a > b:
        print('업!')
    else:
        print('다운!')
이렇게 이름만 .txt로 바꿔서 카톡으로 슥 보내보세요! 친구가 몇 번 만에 맞히는지 후기도 들어보세요.

친구한테 성공적으로 보낸 후엔 어떤 걸 해볼까요?

두 번째 미니 프로젝트: '영어 단어장 퀴즈' 만들기

두 번째 미니 프로젝트: 'To-Do List 메모장' 만들기
우리가 계정 만들 때 아이디, 비밀번호, 비밀번호 확인을 입력하잖아? 비밀 번호, 비밀번호 확인 입력 코드는 이건가?



a = input('비밀번호')

b = input('비밀번호 확인')

if a == b:

    print('확인')

else:

    print('일치하지 않습니다')

네, 맞습니다! 아주 정확하게 핵심 로직을 잘 작성하셨습니다! 🎯

비밀번호 입력과 비밀번호 확인 문자가 서로 똑같은지 비교하는 로직은 작성하신 코드 그대로 a == b를 체크하는 if-else 문이 맞습니다.

조금 더 발전시켜 본다면?
실제 웹사이트나 회원가입 프로그램에서는 비밀번호가 틀렸을 때 "다시 일치할 때까지" 반복해서 입력받도록 만듭니다.

방금 만든 업다운 게임에서 쓰셨던 while 문을 응용하면 아주 멋진 비밀번호 설정 로직이 됩니다!

Python
a = input('비밀번호를 입력하세요: ')

while True:
    b = input('비밀번호 확인을 입력하세요: ')
    
    if a == b:
        print('비밀번호가 일치합니다! 회원가입을 계속합니다.')
        break  # 일치하니까 반복문 탈출!
    else:
        print('비밀번호가 일치하지 않습니다. 다시 입력해주세요.\n')
💡 한 걸음 더: 비밀번호 글자 수 제한 규칙 (선택)
"비밀번호는 8자리 이상이어야 합니다" 같은 규칙도 파이썬의 len() 함수(길이를 세어주는 함수)를 써서 아주 쉽게 추가할 수 있습니다.

Python
while True:
    a = input('비밀번호를 입력하세요 (8자리 이상): ')
    
    # 비밀번호 길이가 8자 이상인지 체크
    if len(a) < 8:
        print('비밀번호가 너무 짧습니다! 8자리 이상으로 해주세요.\n')
        continue  # 아래 코드를 실행하지 않고 while 문 처음으로 돌아감
    
    b = input('비밀번호 확인: ')
    
    if a == b:
        print('비밀번호 설정 완료!')
        break
    else:
        print('비밀번호가 일치하지 않습니다. 다시 시도해주세요.\n')
어떤가요? 아이디/비밀번호 입력받기까지 직접 해보셨으니, 진짜 회원가입 기능의 80%는 완성된 것이나 다름없습니다!

다음으로 어떤 기능을 구현해 볼까요?

아이디/비밀번호 저장 및 로그인 프로그램 완성하기

영어 단어장/To-Do List 미니 프로젝트로 넘어가기
실수로 무한 반복 시켰는데 어케 끔?

당황하지 마세요! 아주 흔하게 하는 실수이고, 끄는 방법도 아주 간단합니다.

실행하고 계신 환경(프로그램)에 따라 아래 키를 누르시면 즉시 강제 종료됩니다.

1. IDLE (Shell 창) 또는 터미널(검은 창)에서 실행 중일 때
Ctrl + C 키를 누르세요.

(Mac은 Cmd + C 또는 Ctrl + C)

파이썬에 강제 종료 신호(KeyboardInterrupt)를 보내서 반복문을 즉시 멈춥니다.

2. IDLE 스크립트 창(에디터)에서 F5로 실행했을 때
코드가 미친 듯이 올라가고 있는 IDLE Shell (파란 글씨 창)을 클릭해서 맨 앞으로 가져옵니다.

상단 메뉴에서 Shell -> Restart Shell을 클릭합니다.

(단축키: Ctrl + F6)

3. 그래도 안 멈추고 먹통(강제 정지)이 되었을 때
창 자체가 하얗게 변하면서 굳어버렸다면, 그냥 우측 상단의 X (창 닫기) 버튼을 눌러서 창을 강제로 닫아버리시면 됩니다!

💡 팁: while True: 같은 무한 반복문을 작성할 때는 항상 안에 break가 잘 동작하는지 확인하거나, 테스트할 때 import time 후 time.sleep(1)을 넣어서 천천히 출력되게 만드는 습관을 들이면 좋습니다.

5번 틀리면 안 되는 걸로 만듬



a = input('비밀번호')

count = 0

while count < 5:

    

    b = input('비밀번호 확인')

    count = count + 1

    if a == b:

        print('확인')

        break

    else:

        print('일치하지 않습니다')

        continue

print('다음에 다시 시도해주세요')

아주 훌륭합니다! while count < 5 조건과 카운트 변수를 활용해서 5번 제한을 두는 로직을 정말 잘 구현하셨어요. 👏

다만, 지금 작성하신 코드에는 작은 문제 하나가 있습니다!

비밀번호를 한 번만에 맞혀서 break로 나와도 맨 마지막줄 print('다음에 다시 시도해주세요')가 무조건 출력되는 문제입니다.

무엇이 문제이고, 어떻게 고치나요?
break는 while 반복문만 탈출하게 해줍니다. 반복문이 끝난 뒤에 있는 print('다음에 다시 시도해주세요')는 정답을 맞혔든, 5번 틀렸든 상관없이 실행되는 위치에 있기 때문입니다.

이 문제는 while - else 문을 활용하거나, 성공 여부를 체크하는 변수를 만들어서 아주 쉽게 해결할 수 있습니다!

방법 1: while - else 문 활용하기 (파이썬만의 꿀팁! 🍯)
파이썬에서는 while 문 뒤에 else:를 붙일 수 있습니다. 이 else:는 "중간에 break를 만나지 않고, 5번을 다 채워서 정상 종료되었을 때만" 실행됩니다.

Python
a = input('비밀번호를 입력하세요: ')
count = 0

while count < 5:
    b = input('비밀번호 확인: ')
    count = count + 1
    
    if a == b:
        print('확인! 비밀번호가 일치합니다.')
        break  # 맞혔으니 탈출! (아래 else 블록은 실행 안 됨)
    else:
        print('일치하지 않습니다.')

else:  # break로 탈출하지 못하고 5번 다 틀렸을 때만 실행!
    print('5회 이상 실패했습니다. 다음에 다시 시도해주세요.')
방법 2: 성공했는지 확인하는 상태 변수 쓰기
다른 프로그래밍 언어에서도 자주 쓰는 가장 직관적인 방법입니다.

Python
a = input('비밀번호를 입력하세요: ')
count = 0
success = False  # 성공 여부를 기록할 변수

while count < 5:
    b = input('비밀번호 확인: ')
    count = count + 1
    
    if a == b:
        print('확인! 비밀번호가 일치합니다.')
        success = True  # 성공했다고 표시!
        break
    else:
        print('일치하지 않습니다.')

# 반복문이 끝나고 실패했을 때만 출력
if not success:
    print('5회 이상 실패했습니다. 다음에 다시 시도해주세요.')
💡 팁: continue는 없어도 괜찮아요!
작성하신 코드에서 else: 블록 안의 continue는 지우셔도 똑같이 작동합니다! 어차피 else: 블록의 마지막 줄이 끝나면 파이썬은 자동으로 while 문의 처음으로 돌아가기 때문입니다.

직접 조건문이나 반복문의 제약 조건까지 고민해서 코드로 옮기시는 모습을 보니, 파이썬 감각이 정말 빠르게 늘고 계십니다!

다음으로 어떤 걸 도전해 볼까요?

아이디까지 입력받는 진짜 회원가입/로그인 프로그램 만들기

비밀번호 틀린 횟수(예: 1/5회) 표시해 주기
continue아까 써 놓고 까먹고 안 지움 ㅋㅋㅋ

ㅋㅋㅋㅋ 그럴 때 진짜 많아요! 코딩하다 보면 시험해 보려고 썼다가 까먹고 놔두는 흔적들이 꼭 하나씩 생기죠.

그래도 실행하는 데 오류는 안 나는 문법이라 천만다행입니다.

방금 만드신 '5회 제한 비밀번호 확인 프로그램'은 스스로 조건(while count < 5)이랑 카운트 로직까지 생각해서 짜신 거라 진짜 대단한 발전이에요!

while-else 구문이나 성공 체크 방식 적용해서 실행해 보셨나요? 제대로 딱 작동할 때 느껴지는 그 소소한 쾌감이 진짜 코딩의 재미입니다! 👍

이제 로그인 조건식까지 완벽하게 감 잡으셨는데, 여기서 '아이디+비밀번호 로그인 시스템'으로 조금 더 발전시켜 보실래요, 아니면 아까 이야기했던 '영어 단어장'이나 'To-Do List' 같은 다른 미니 프로젝트로 넘어가 보실래요?

다음으로 어떤 걸 해볼까요?

아이디와 비밀번호로 로그인하는 프로그램 만들기

두 번째 미니 프로젝트 (영어 단어장 퀴즈) 시작하기

세 번째 미니 프로젝트 (To-Do List 메모장) 시작하기
세 번째 미니 프로젝트인 '터미널 할 일 관리 메모장' 만들기 가이드 줘!

Python을 사용하여 터미널(CLI) 기반 '할 일 관리 메모장'을 직접 만들어볼 수 있도록 가이드를 구성했습니다.

이 프로젝트에서는 할 일 추가, 목록 조회, 완료 처리, 삭제, 그리고 파일 저장/불러오기(데이터 지속성) 기능을 구현합니다.

1. 프로젝트 구조 및 기능 설계
주요 기능
할 일 추가 (Add): 새로운 할 일 항목을 입력받아 목록에 추가합니다.

할 일 목록 보기 (View): 현재 추가된 모든 할 일 목록과 완료 여부([ ] 또는 [X])를 표시합니다.

할 일 완료 표시 (Complete): 특정 번호의 할 일을 완료 상태로 변경합니다.

할 일 삭제 (Delete): 특정 번호의 할 일을 목록에서 제거합니다.

데이터 저장/불러오기 (JSON): 프로그램이 종료되어도 할 일 목록이 유지되도록 todos.json 파일에 자동 저장 및 불러오기를 수행합니다.

2. 전체 파이썬 소스 코드 (todo.py)
아래 코드를 작성하여 todo.py 파일로 저장하세요.

Python
import json
import os

FILENAME = "todos.json"

def load_todos():
    """파일에서 할 일 목록을 불러옵니다."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_todos(todos):
    """할 일 목록을 파일에 저장합니다."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)

def show_todos(todos):
    """현재 할 일 목록을 화면에 출력합니다."""
    print("\n" + "=" * 35)
    print("      📋 할 일 목록 (To-Do)")
    print("=" * 35)
    
    if not todos:
        print("등록된 할 일이 없습니다.")
    else:
        for idx, todo in enumerate(todos, 1):
            status = "[X]" if todo["completed"] else "[ ]"
            print(f"{idx}. {status} {todo['title']}")
            
    print("=" * 35)

def add_todo(todos):
    """새로운 할 일을 추가합니다."""
    title = input("추가할 할 일을 입력하세요: ").strip()
    if title:
        todos.append({"title": title, "completed": False})
        save_todos(todos)
        print(f"\''{title}\'\' 항목이 추가되었습니다.")
    else:
        print("내용을 입력하지 않았습니다.")

def complete_todo(todos):
    """할 일을 완료 상태로 처리합니다."""
    show_todos(todos)
    if not todos:
        return
    
    try:
        num = int(input("완료 처리할 번호를 입력하세요: "))
        if 1 <= num <= len(todos):
            todos[num - 1]["completed"] = True
            save_todos(todos)
            print(f"\''{todos[num - 1]['title']}\'\' 항목이 완료 처리되었습니다!")
        else:
            print("올바른 번호를 입력해 주세요.")
    except ValueError:
        print("숫자를 입력해 주세요.")

def delete_todo(todos):
    """할 일을 삭제합니다."""
    show_todos(todos)
    if not todos:
        return
    
    try:
        num = int(input("삭제할 번호를 입력하세요: "))
        if 1 <= num <= len(todos):
            removed = todos.pop(num - 1)
            save_todos(todos)
            print(f"\''{removed['title']}\'\' 항목이 삭제되었습니다.")
        else:
            print("올바른 번호를 입력해 주세요.")
    except ValueError:
        print("숫자를 입력해 주세요.")

def main():
    todos = load_todos()
    
    while True:
        print("\n--- [ 터미널 할 일 관리 메모장 ] ---")
        print("1. 목록 보기")
        print("2. 할 일 추가")
        print("3. 할 일 완료")
        print("4. 할 일 삭제")
        print("5. 종료")
        
        choice = input("원하는 작업 번호를 선택하세요 (1-5): ").strip()
        
        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            delete_todo(todos)
        elif choice == "5":
            print("프로그램을 종료합니다. 좋은 하루 되세요!")
            break
        else:
            print("잘못된 입력입니다. 1~5 사이의 숫자를 입력해 주세요.")

if __name__ == "__main__":
    main()
3. 핵심 포인트 및 학습 내용
자료구조 활용 (List & Dict)

각 할 일 항목은 {"title": "공부하기", "completed": False} 형태의 딕셔너리로 저장되며, 전체 목록은 리스트([])로 관리됩니다.

데이터 파일 입출력 (JSON)

json.dump()와 json.load()를 사용하여 프로그램이 다시 실행되어도 이전 데이터가 그대로 유지됩니다.

예외 처리 (try - except)

숫자가 아닌 값을 입력했을 때 프로그램이 비정상 종료되는 것을 방지합니다.

4. 확장 아이디어 (추가로 도전해볼 기능)
기본 기능을 작성해본 뒤 아래 기능들을 직접 추가해 보세요!

마감일/날짜 추가: 딕셔너리에 due_date 필드를 추가하여 마감 기한도 함께 기록

카테고리 구분: '공부', '운동', '개인' 등 카테고리별로 모아보기 기능 구현

검색 기능: 특정 키워드가 포함된 할 일만 찾아 출력하는 기능

원하는 추가 확장 기능(마감일, 카테고리 등) 코드를 함께 작성해볼까요?

예
음 내가 안 배운 모듈이 있어서 못 하는건데??

아, 맞아요! 방금 보여드린 전체 코드는 json이나 os 같은 모듈, 그리고 def 함수 정의까지 섞여 있어서 아직 배우지 않은 개념 때문에 당연히 막막하고 어렵게 느껴지셨을 겁니다. 정말 죄송해요!

지금 단계에서는 모듈이나 어려운 기능 전혀 없이, 지금까지 Do it! 첫 파이썬에서 배운 순수한 기본 개념(리스트, while, if, input)만 가지고 100% 혼자 힘으로 만들 수 있습니다!

아래 단계별 가이드를 보고 하나씩 천천히 만들어볼까요?

우리가 사용할 문법 3가지
list (리스트): 할 일들을 차곡차곡 담아둘 바구니 (todos = [])

while True: 메뉴판을 계속 띄워줄 무한 반복문

if - elif - else: 메뉴 선택에 따라 다른 행동 하기

1단계: 뼈대 만들기 (메뉴판 띄우기)
IDLE에서 새 창(Ctrl + N)을 열고 아래 코드를 직접 적어보세요.

Python
todos = []  # 할 일들을 저장할 빈 리스트!

while True:
    print("\n--- [ 할 일 관리 메모장 ] ---")
    print("1. 할 일 목록 보기")
    print("2. 할 일 추가하기")
    print("3. 종료하기")
    
    select = input("원하는 메뉴 번호를 입력하세요: ")
    
    if select == '1':
        print("목록을 보여줍니다.")
    elif select == '2':
        print("할 일을 추가합니다.")
    elif select == '3':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다. 다시 선택해주세요.")
이걸 먼저 실행해서 1, 2, 3을 눌렀을 때 제대로 반응하는지 확인해보세요!

2단계: 할 일 추가하고 목록 보기 기능 채우기
메뉴판이 잘 작동하면, elif select == '2': 부분과 if select == '1': 부분을 우리가 배운 리스트 명령어(append, for 문)로 채워 넣으면 됩니다!

할 일 추가하기: todos.append(새로운_할일)

목록 보여주기: for 문으로 리스트 안의 내용 하나씩 출력하기

Python
import random # (필요시 쓰지만 여긴 모듈 안 써도 됨!)

todos = []

while True:
    print("\n--- [ 할 일 관리 메모장 ] ---")
    print("1. 할 일 목록 보기")
    print("2. 할 일 추가하기")
    print("3. 종료하기")
    
    select = input("원하는 메뉴 번호를 입력하세요: ")
    
    if select == '1':
        if len(todos) == 0:
            print("등록된 할 일이 없습니다!")
        else:
            print("\n[ 나의 할 일 목록 ]")
            # enumerate 대신 단순 for문이나 인덱스로 보여주기
            num = 1
            for item in todos:
                print(f"{num}. {item}")
                num = num + 1

    elif select == '2':
        work = input("추가할 할 일을 입력하세요: ")
        todos.append(work)
        print(f"'{work}' 할 일이 추가되었습니다!")

    elif select == '3':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다. 다시 선택해주세요.")
어때요? 이 코드는 모듈(import)도 없고, 어려운 함수(def)도 전혀 없죠?
오직 아시는 리스트, 반복문, 조건문만 가지고 만든 진짜 할 일 메모장입니다!

직접 IDLE에 쳐보시면서 작동시켜 보세요. 배운 문법만으로도 이렇게 멋진 프로그램을 만들 수 있다는 게 느껴지실 거예요!

다음으로 무엇을 수정해 볼까요?

리스트에서 할 일을 지우는(삭제) 기능 추가해보기

영단어장 퀴즈 미니 프로젝트로 바꿔서 도전해보기
아냐 아무래도 내가 잘 못한 것 같아 아이디와 비밀번호로 로그인하는 프로그램 만드는게 나을것 같아

전혀 아닙니다! 절대 잘못하신 게 아니라, 내가 알고 있는 문법 수준에 딱 맞는 주제를 직접 선택하는 것도 훌륭한 코딩 감각입니다.

아까 만든 '비밀번호 5번 제한 확인 로직'을 확장해서 아이디와 비밀번호로 로그인하는 프로그램을 만드는 것이 지금 상황에 100% 딱 맞는 최고의 선택입니다!

배운 것만 가지고 깔끔하게 만드는 3단계 가이드를 드릴게요.

1. 우리가 사용할 문법 3가지
변수: 가입할 아이디(user_id)와 비밀번호(user_pw) 저장

while 문 & 카운트: 로그인 시도 횟수 제한 (5번)

if - elif - else: 아이디/비밀번호가 맞는지 비교하기

1단계: 회원가입 (아이디와 비밀번호 등록하기)
먼저 사용자가 사용할 아이디와 비밀번호를 설정받습니다.

Python
print("=== [ 회원가입 ] ===")
user_id = input("사용할 아이디를 입력하세요: ")
user_pw = input("사용할 비밀번호를 입력하세요: ")
print("회원가입이 완료되었습니다!\n")
2단계: 로그인 시도하기 (5번 기회)
아까 만드셨던 while count < 5 로직을 그대로 가져와서 "아이디 검사"와 "비밀번호 검사"를 함께 합니다!

Python
print("=== [ 로그인 ] ===")
count = 0  # 실패 횟수 카운트

while count < 5:
    login_id = input("아이디 입력: ")
    login_pw = input("비밀번호 입력: ")
    
    # 아이디와 비밀번호가 둘 다 맞는지 확인!
    if login_id == user_id and login_pw == user_pw:
        print(f"\n로그인 성공! 환영합니다, {user_id}님!")
        break  # 로그인 성공했으니 반복문 탈출
    else:
        count = count + 1
        print(f"아이디 또는 비밀번호가 틀렸습니다. (실패 횟수: {count}/5회)\n")

# 5번 다 틀려서 break를 못 만나고 끝났을 때
if count == 5:
    print("로그인 5회 실패! 비밀번호 찾기를 이용해 주세요.")
3단계: 전체 코드 합치기!
IDLE 새 창(Ctrl + N)에 아래 전체 코드를 적고 F5를 눌러 실행해 보세요.

Python
# 1. 회원가입 단계
print("=== [ 회원가입 ] ===")
user_id = input("사용할 아이디를 입력하세요: ")
user_pw = input("사용할 비밀번호를 입력하세요: ")
print("회원가입이 완료되었습니다!\n")

# 2. 로그인 단계 (5회 제한)
print("=== [ 로그인 ] ===")
count = 0

while count < 5:
    login_id = input("아이디 입력: ")
    login_pw = input("비밀번호 입력: ")
    
    # and 연산자로 둘 다 일치하는지 체크!
    if login_id == user_id and login_pw == user_pw:
        print(f"\n로그인 성공! 환영합니다, {user_id}님!")
        break
    else:
        count = count + 1
        print(f"아이디 또는 비밀번호가 틀렸습니다. (실패 횟수: {count}/5회)\n")

if count == 5:
    print("로그인 5회 실패! 비밀번호 찾기를 이용해 주세요.")
💡 포인트: and 연산자
login_id == user_id and login_pw == user_pw처럼 and를 붙이면 "아이디도 맞고, 비밀번호도 맞아야 참(True)"이 됩니다.

배우신 문법만으로 딱 작동하는 진짜 회원가입/로그인 프로그램이 완성됩니다! 직접 타이핑해서 실행해 보세요.

다음으로 어떤 기능을 추가해 볼까요?

아이디가 틀렸는지 비밀번호가 틀렸는지 따로 알려주기

로그인 성공 후 간단한 기능(프로필 보기 등) 이어지게 하기
완성했다!!!!



id = input('아이디')





while True:

    password = input('비밀번호(8자이상)')

    if len(password) >= 8:

        break

    else:

        print('8자가 넘지 않습니다. 다시 설정해 주십시오')

        continue

while True:

    password_check = input('비밀번호 확인')

    if password == password_check:

        print('확인')

        break

    else:

        print('일치하지 않습니다')

        continue

    

print('login')

attempt = 0

while attempt == 0:

    id_login = input('아이디')

    if id_login == id:

        break

    else:

        print('일치하는 아이디가 없습니다')

        continue



while attempt < 5:

    if id_login == id:

        password_login = input('비밀번호')

        if password_login == password:

            print('로그인 되었습니다')

            break

        else:

            print('비밀번호가 잘못되었습니다')

            attempt = attempt + 1

            continue

else:

    print('다음에 다시 시도해 주세요')

와, 진짜 멋집니다! 👏👏👏

개념을 완벽하게 조합하셨어요!

len() 함수로 비밀번호 8자 이상 검사

비밀번호 재확인 로직

아이디 일치할 때까지 재입력받기

비밀번호 5회 실패 시 while-else로 차단하기

이 모든 흐름이 파이썬 기초 문법만으로 완벽하게 이어졌습니다. 스스로 필요하다고 생각한 조건들을 코드로 직접 설계하고 다듬어서 완성하셨다는 게 정말 대단합니다!

💡 살짝 다듬으면 더 좋아지는 꿀팁 2가지
지금 코드로도 완벽하게 동작하지만, 한 단계 더 깔끔하게 다듬을 수 있는 부분도 있습니다.

id는 파이썬 예약어(내장 함수 이름)예요!

파이썬에는 원래 id()라는 기본 함수가 있어서, 변수 이름을 id 대신 user_id나 my_id처럼 쓰면 더 안전합니다.

while attempt == 0: 활용

아이디를 맞힐 때까지 무한 반복하는 부분은 while True:를 쓰면 훨씬 직관적입니다. (attempt 변수는 아래 비밀번호 틀린 횟수 세는 데 집중할 수 있어요!)

직접 만든 첫 '회원가입 & 로그인 System'
불과 조금 전까지만 해도 "파이썬 기초만 겨우 떼서 어쩌지..." 하셨는데, 지금은 조건문, 반복문, 변수, 문자열 함수, 카운팅, 예외 조건까지 다 다루는 멋진 프로그램을 혼자 만들어내셨습니다!

이게 진짜 프로그래밍 실력이 늘어나는 순간입니다.

이제 자신감을 완전히 가져도 됩니다! 배운 문법만으로도 이렇게 당당하게 프로그램을 만들어내셨으니까요. 🎉

다음으로 어떤 걸 도전해 볼까요?

로그인 성공 후 '비밀번호 변경' 기능 추가해보기

두 번째 미니 프로젝트: '영어 단어장 퀴즈' 도전하기
비밀 번호 변경 기능 만들래!!

최고의 선택입니다! 방금 만드신 코드에 로그인 성공 후 '비밀번호 변경' 메뉴를 이어 붙이면 진짜 완성도 높은 회원가입/로그인 프로그램이 됩니다.

비밀번호 변경 기능은 [1] 기존 비밀번호 확인 ➔ [2] 새 비밀번호 8자 이상 검사 ➔ [3] 새 비밀번호 재확인 과정으로 만들면 완벽합니다.

기존 코드 끝에 연결하는 '비밀번호 변경' 코드
작성하신 로그인 성공 부분(print('로그인 되었습니다')) 바로 아래에 아래 흐름을 추가해 주시면 됩니다.

Python
# --- 방금 만드신 로그인 성공 구문 아래에 이어붙이기 ---
print('\n로그인 되었습니다!')

while True:
    print("\n--- [ 마이페이지 ] ---")
    print("1. 비밀번호 변경")
    print("2. 로그아웃 (종료)")
    
    menu = input("원하는 작업 번호를 입력하세요: ")
    
    if menu == '1':
        print("\n--- [ 비밀번호 변경 ] ---")
        
        # 1. 기존 비밀번호 확인
        old_pw = input("현재 비밀번호를 입력하세요: ")
        if old_pw != password:
            print("현재 비밀번호가 일치하지 않습니다. 변경 실패!")
            continue
            
        # 2. 새 비밀번호 입력 (8자 이상 조건)
        while True:
            new_pw = input("새 비밀번호 입력(8자 이상): ")
            if len(new_pw) >= 8:
                break
            else:
                print("8자 이상이어야 합니다. 다시 입력해 주세요.")
                
        # 3. 새 비밀번호 재확인
        while True:
            new_pw_check = input("새 비밀번호 확인: ")
            if new_pw == new_pw_check:
                password = new_pw  # ⭐️ 기존 password 변수의 값을 새 비밀번호로 교체!
                print("비밀번호가 성공적으로 변경되었습니다!")
                break
            else:
                print("비밀번호가 일치하지 않습니다. 다시 입력해 주세요.")
                
    elif menu == '2':
        print("로그아웃 되었습니다. 프로그램을 종료합니다.")
        break
    else:
        print("잘못된 번호입니다. 다시 선택해 주세요.")
💡 핵심 포인트: password = new_pw
비밀번호 변경의 핵심은 맨 마지막에 password = new_pw를 써서 기존 변수에 저장되어 있던 옛날 비밀번호를 새 비밀번호로 바꿔치기해 주는 것입니다!

이렇게 하면 비밀번호를 바꾼 후 다시 로그인할 때 새 비밀번호로 로그인해야 정상 작동하게 됩니다.

기존 만드신 코드 아래에 직접 붙여서 실행해 보세요! 정말 근사한 회원 관리 프로그램이 완성될 겁니다! 👍

비밀번호 변경까지 완성한 후엔 무엇을 해볼까요?

변경한 비밀번호로 다시 로그인되는지 테스트해보기

두 번째 미니 프로젝트: '영어 단어장 퀴즈' 도전하기
id = input('아이디')





while True:

    password = input('비밀번호(8자이상)')

    if len(password) >= 8:

        break

    else:

        print('8자가 넘지 않습니다. 다시 설정해 주십시오')

        continue

while True:

    password_check = input('비밀번호 확인')

    if password == password_check:

        print('확인')

        break

    else:

        print('일치하지 않습니다')

        continue

    

print('login')

attempt = 0

while True:

    id_login = input('아이디')

    if id_login == id:

        break

    else:

        print('일치하는 아이디가 없습니다')

        continue



while attempt < 5:

    if id_login == id:

        password_login = input('비밀번호')

        if password_login == password:

            print('로그인 되었습니다')

            break

        else:

            print('비밀번호가 잘못되었습니다')

            attempt = attempt + 1

            continue

else:

    print('다음에 다시 시도해 주세요')



print('비밀 번호를 변경하시겠습니까?')

exchange = input('변경을 원하신다면 y, 변경을 원하시지 않는다면 n을 눌러주십시오')

if exchange == 'y':

    while True:

        password = input('비밀번호(8자이상)')

        if len(password) >= 8:

            break

        else:

            print('8자가 넘지 않습니다. 다시 설정해 주십시오')

            continue

    while True:

        password_check = input('비밀번호 확인')

        if password == password_check:

            print('확인')

            input('Enter를 누를 시 종료 됩니다.')

            break

        else:

            print('일치하지 않습니다')

            continue

else:

    input('Enter를 누를 시 종료 됩니다.')

짜놓으신 코드 흐름이 정말 깔끔하고 좋습니다! 질문자님만의 방식으로 비밀번호 변경 입력(y/n)과 마지막 종료 대기 문구(input)까지 아주 자연스럽게 완성하셨네요.

다만, 실제 실행해보면 딱 1가지 놓칠 수 있는 오점(버그)이 숨어 있습니다!

⚠️ 발견된 문제점: 로그인에 실패해도 비밀번호 변경이 실행됨!
비밀번호를 5번 틀려서 print('다음에 다시 시도해 주세요')가 출력되고 실패했을 때를 상상해보세요.

로그인 실패 후 반복문이 끝나고 그대로 아래로 내려가기 때문에, 로그인을 못 한 사람에게도 "비밀 번호를 변경하시겠습니까?" 문구가 떠버립니다!

Python
# ❌ 현재 코드의 문제 흐름
# 5번 실패 -> '다음에 다시 시도해 주세요' 출력 
# -> 곧바로 '비밀 번호를 변경하시겠습니까?' 문구 출력! (로그인 실패자에게도 변경 기회가 줌)
💡 깔끔하게 해결하는 방법: 성공했을 때만 들어가게 만들기!
로그인 성공 여부를 알 수 있게 is_login = False 같은 상태 체크 변수를 만들거나, 로그인 실패 시 프로그램을 바로 종료시키는 문장을 넣어주면 해결됩니다.

로그인 성공 시 is_login = True로 바꿔서 로그인에 성공한 사용자만 비밀번호를 변경하도록 수정한 완성형 코드입니다!

Python
id = input('아이디')

while True:
    password = input('비밀번호(8자이상)')
    if len(password) >= 8:
        break
    else:
        print('8자가 넘지 않습니다. 다시 설정해 주십시오')
        continue

while True:
    password_check = input('비밀번호 확인')
    if password == password_check:
        print('확인')
        break
    else:
        print('일치하지 않습니다')
        continue

print('login')
attempt = 0

while True:
    id_login = input('아이디')
    if id_login == id:
        break
    else:
        print('일치하는 아이디가 없습니다')
        continue

is_login = False  # ⭐️ 로그인 성공 여부를 기록할 변수!

while attempt < 5:
    if id_login == id:
        password_login = input('비밀번호')
        if password_login == password:
            print('로그인 되었습니다')
            is_login = True  # ⭕️ 로그인 성공 표시!
            break
        else:
            print('비밀번호가 잘못되었습니다')
            attempt = attempt + 1
            continue
else:
    print('다음에 다시 시도해 주세요')

# ⭐️ 로그인에 성공했을 때만 비밀번호 변경 절차 진행!
if is_login:
    print('비밀 번호를 변경하시겠습니까?')
    exchange = input('변경을 원하신다면 y, 변경을 원하시지 않는다면 n을 눌러주십시오: ')
    if exchange == 'y':
        while True:
            password = input('비밀번호(8자이상)')
            if len(password) >= 8:
                break
            else:
                print('8자가 넘지 않습니다. 다시 설정해 주십시오')
                continue
        while True:
            password_check = input('비밀번호 확인')
            if password == password_check:
                print('확인! 비밀번호가 정상적으로 변경되었습니다.')
                input('Enter를 누를 시 종료 됩니다.')
                break
            else:
                print('일치하지 않습니다')
                continue
    else:
        input('Enter를 누를 시 종료 됩니다.')
else:
    # 로그인 실패자는 바로 종료되도록 안내
    input('Enter를 누를 시 종료 됩니다.')
🎉 진짜 대단합니다!
오류를 잡아내는 과정까지 포함해서, 배운 내용(변수, 조건문, while 무한루프, break, continue, len() 함수, 로그인 횟수 제한, 상태 변수)을 조합하여 하나의 완성된 시스템 프로젝트를 만들어내셨습니다.

처음에 IDLE 오류 때문에 헷갈려하던 모습에서 여기까지 오신 건 엄청난 발전이에요!

이 프로젝트는 여기서 마무리하고 친구들에게 자랑해보셔도 좋겠습니다. 다음엔 어떤 프로젝트를 도전해보고 싶으신가요?

다음 단계로 어떤 걸 해볼까요?

두 번째 미니 프로젝트: '영어 단어장 퀴즈' 도전하기

새로 바꾼 비밀번호로 '다시 로그인' 해보는 반복 기능 추가하기
id = input('아이디')

login = 0



while True:

    password = input('비밀번호(8자이상)')

    if len(password) >= 8:

        break

    else:

        print('8자가 넘지 않습니다. 다시 설정해 주십시오')

        continue

while True:

    password_check = input('비밀번호 확인')

    if password == password_check:

        print('확인')

        break

    else:

        print('일치하지 않습니다')

        continue

    

print('login')

attempt = 0

while True:

    id_login = input('아이디')

    if id_login == id:

        break

    else:

        print('일치하는 아이디가 없습니다')

        continue



while attempt < 5:

    if id_login == id:

        password_login = input('비밀번호')

        if password_login == password:

            print('로그인 되었습니다')

            login = 1

            break

        else:

            print('비밀번호가 잘못되었습니다')

            attempt = attempt + 1

            continue

else:

    print('다음에 다시 시도해 주세요')



if login == 1:

    print('비밀 번호를 변경하시겠습니까?')

    exchange = input('변경을 원하신다면 y, 변경을 원하시지 않는다면 n을 눌러주십시오')

    if exchange == 'y':

        while True:

            password = input('비밀번호(8자이상)')

            if len(password) >= 8:

                break

            else:

                print('8자가 넘지 않습니다. 다시 설정해 주십시오')

                continue

        while True:

            password_check = input('비밀번호 확인')

            if password == password_check:

                print('확인')

                input('Enter를 누를 시 종료 됩니다.')

                break

            else:

                print('일치하지 않습니다')

                continue

    else:

        input('Enter를 누를 시 종료 됩니다.')

와, login = 1이라는 상태 기록 변수(플래그 변수)를 직접 아이디어 내서 적용하신 건가요? 🔥

방금 하신 방식이 프로그래머들이 실제로 로그인 상태나 게임 오버 상태를 관리할 때 쓰는 가장 핵심적인 테크닉입니다!

login 변수 하나를 추가했을 뿐인데, 로그인 실패 시 예외 처리와 비밀번호 변경 흐름이 완벽하게 정리되었습니다.

코드 분석: 완벽하게 작동하는 이유
맨 위에 login = 0으로 "로그인 안 됨" 상태 설정

로그인 성공 시 login = 1로 "로그인 됨" 상태 변경

맨 아래 if login == 1: 조건으로 성공한 사람만 비밀번호 변경 기회를 주고, 실패한 사람은 그대로 통과

진짜 깔끔하고 완벽한 논리 흐름입니다! 버그 없이 의도한 대로 100% 작동합니다.

🏆 첫 완성형 프로젝트 축하합니다!
불과 얼마 전까지만 해도 IDLE에서 에러 나면 당황하시던 모습이었는데, 이제는:

사용자 입력 받기 (input)

조건 제어 (if - elif - else)

무한 반복 및 탈출 (while, break, continue)

입력값 조건 검사 (len())

상태 기록 변수 활용 (login = 0 / 1)

횟수 제한 제어 (attempt, while-else)

이 모든 파이썬 핵심 개념들을 스스로 조합해서 동작하는 프로그램으로 만들어내셨습니다. 이건 단순 연습이 아니라 진짜 "개발"을 해내신 거예요!

이 프로젝트는 이제 어디 내놓아도 손색없는 훌륭한 결과물입니다. 정말 수고 많으셨습니다! 🎉

자, 이제 회원가입/로그인 마스터하셨으니 다음 단계로 가볼까요?

두 번째 프로젝트: '영어 단어장 퀴즈' 만들기

방금 만든 코드를 친구에게 보낼 수 있게 파일로 정리하기
영어 단어장은 단어 일일이 치는게 귀찮긴 한데...

맞아요 ㅋㅋㅋ 단어 20~30개씩 코드에 {"apple": "사과", ...} 이렇게 일일이 치고 있으면 개발이 아니라 타자 연습하는 느낌 들죠!

실제 개발자들도 절대 그런 귀찮은 노가다는 하지 않습니다.

노가다 없이 아주 편하고 재밌게 만드는 2가지 방법이 있어요!

방법 1: 딱 3개짜리 사전(복붙용)으로 로직만 맛보기 💡
단어를 50개 입력할 필요 전혀 없습니다! 단어 3개만 들어간 사전(딕셔너리)을 코드에 복사-붙여넣기 해두고, 퀴즈가 돌아가는 재미있는 핵심 코드(랜덤으로 문제 내기, 정답 체크, 점수 세기)만 만들면 끝납니다.

Python
# 굳이 직접 안 치고 이 3개만 복붙해서 시작하면 됩니다!
vocab = {
    "apple": "사과",
    "banana": "바나나",
    "computer": "컴퓨터"
}
방법 2: 단어장이 귀찮다면 다른 미니 프로젝트로 변경! 🎮
단어장 만드는 게 끌리지 않는다면, 타자 칠 일 전혀 없는 훨씬 재밌는 프로젝트로 바로 넘어가도 됩니다!

🎮 컴퓨터와 맞붙는 '가위바위보 게임': (import random 써서 컴퓨터가 내는 가위바위보와 대결, 연승 기록 세우기)

🏰 선택지로 진행되는 '텍스트 모험(RPG) 게임': ("왼쪽 동굴로 갈까? 오른쪽 숲으로 갈까?" 선택에 따라 엔딩이 달라지는 게임)

🎰 오늘 뭐 먹지? '랜덤 메뉴 추천기': (메뉴 추가 기능 + 랜덤 뽑기 기능)

어떤 방식으로 진행해 볼까요? 편한 방법만 골라주세요!

어떤 방법으로 가볼까요?

단어 3개만 복붙해서 '영단어 퀴즈' 쉽고 빠르게 만들기

타자 칠 일 없는 '컴퓨터와 가위바위보 게임' 만들기

선택에 따라 엔딩이 바뀌는 '텍스트 RPG 게임' 만들기
아니 이런 것보단 살짝 다른 앱? 또는 사이트 연동해서 하고 싶음

오, 훨씬 재밌는 아이디어입니다! 단순히 화면에 글자만 찍는 게 아니라 웹사이트의 진짜 데이터(날씨, 뉴스, 영화 순위 등)를 실시간으로 가져와서 보여주는 앱을 만들고 싶으신 거군요!

외부 연동을 하면 파이썬이 진짜 현실 세상과 연결되는 서비스가 됩니다.

우리가 이미 배웠던 리스트, 조건문(if), 반복문(while)을 똑같이 활용하면서, 파이썬 기본 탑재 라이브러리인 urllib.request를 사용해 외부 사이트의 데이터를 가져오는 가장 쉬운 연동 프로젝트 3가지를 추천해 드립니다.

🌐 1. 실시간 네이버 검색어/뉴스 헤드라인 가져오기
원리: 네이버 뉴스나 메인 페이지의 웹 주소(URL)를 파이썬이 대신 접속해서, 지금 가장 핫한 실시간 뉴스 제목들을 1위부터 10위까지 쭉 글자로 긁어오는 프로그램입니다.

재미 포인트: 실행할 때마다 뉴스 제목이 실시간으로 계속 바뀝니다!

🌤️ 2. 오늘 서울/동네 실시간 날씨 & 옷차림 추천 앱
원리: 기상청이나 날씨 제공 사이트의 데이터를 파이썬으로 쏙 가져옵니다.

재미 포인트: 파이썬이 "오늘 서울 기온은 24도입니다! 반팔에 가디건을 챙기세요." 하고 날씨에 맞춰 문구를 알려주게 만듭니다.

🎬 3. 실시간 박스오피스 영화 순위 조회기
원리: 영화관 관련 사이트에서 현재 상영 중인 영화 순위와 예매율을 파이썬으로 불러옵니다.

재미 포인트: 영화 제목과 예매율을 터미널에 예쁜 순위표로 딱 출력해 줍니다.

외부 사이트 데이터를 긁어오는 건 urllib.request라는 파이썬 기본 기능 딱 몇 줄만 적으면 작동하기 때문에 별도로 복잡하게 설치할 것도 전혀 없습니다!

이 중에서 어떤 사이트나 데이터를 파이썬으로 가져와 보고 싶으신가요?

어떤 외부 데이터 연동을 해볼까요?

1. 실시간 뉴스 헤드라인 가져오기 도전

2. 오늘 실시간 날씨 & 옷차림 추천 앱 도전

3. 영화 박스오피스 순위 조회기 도전
3개중에 뭐가 가장 쉬워?

셋 중에서 2번 '실시간 날씨 & 옷차림 추천 앱'이 제일 쉽고 가장 깔끔하게 만들어집니다! ☀️🌤️

왜 2번이 가장 쉬운지, 그리고 왜 뉴스나 영화보다 만들기 편한지 이유가 있습니다.

💡 왜 날씨 앱이 가장 쉬울까요?
복잡한 코드가 없어요!

뉴스나 영화 사이트는 디자인(HTML)이 너무 복잡해서 글자 뽑아내기가 조금 까다롭습니다.

날씨 정보는 open-meteo 같은 무료 날씨 전송 전용 서비스에서 온도 숫딱 하나만 깔끔하게 빼올 수 있어서 코드가 아주 짧아집니다.

우리가 배웠던 if-else문으로 바로 완성!

날씨 온도(숫자)만 파이썬으로 쏙 가져온 다음에, 아까 만든 로그인 프로그램처럼 if temperature > 20: 같은 조건문만 몇 줄 적어주면 끝납니다!

🌤️ 날씨 앱이 일하는 방식 (미리보기)
파이썬 기본 내장 모듈(urllib.request, json) 딱 두 개를 써서 외부 사이트에서 기온 데이터를 훔쳐(?)옵니다.

Python
# 파이썬이 알아서 외부 인터넷 주소로 접속해서
# "지금 기온 몇 도야?" 하고 가져옵니다.

# 기온이 가져와지면 우리가 배운 if문 시작!
if temp >= 28:
    print("너무 덥습니다! 반팔, 반바지, 손선풍기를 챙기세요!")
elif temp >= 20:
    print("날씨가 딱 좋습니다! 얇은 셔츠나 가디건을 추천해요.")
elif temp >= 10:
    print("쌀쌀합니다. 자켓이나 트렌치코트를 입으세요!")
else:
    print("너무 춥습니다! 패딩과 목도리를 꼭 챙기세요!")
어때요? 기온 숫자만 딱 가져오면 그 뒤는 지금까지 배운 if-elif-else 조건문으로 완전히 요리할 수 있겠죠?

어려운 설치 없이 파이썬 기본 IDLE 창에서 바로 실행할 수 있는 '실시간 날씨 & 옷차림 추천 앱' 코드로 바로 만들어볼까요?

어떤 단계로 진행해 볼까요?

실시간 날씨 가져오기 기본 코드 작성해보기

뉴스나 영화 순위 가져오는 방식도 살짝 설명 듣기
나 그거 하고 싶어짐 치지직 알지? 치지직 이랑 연동해서 팔로우 및 구독 기간 확인하는 앱

네, 네이버의 스트리밍 플랫폼 치지직(CHZZK) 말씀이시죠! 요즘 트위치에서 다들 치지직으로 옮겨가서 스트리머들 방송 볼 때 완전 필수 앱이죠! 🟢

네이버 치지직도 내부적으로 오픈 API(인터넷 데이터 제공 통로) 형태의 웹 주소를 가지고 있어서, 파이썬으로 스트리머 채널 정보나 내 구독/팔로우 정보를 쏙 가져오는 앱을 충분히 만들 수 있습니다!

💡 하지만 만들기 전에 꼭 알아두어야 할 점!
치지직에서 "특정 사용자의 팔로우 목록 및 구독 기간" 같은 개인 계정 정보를 가져오려면 크게 2가지 조건이 필요합니다.

치지직 개발자 센터 API 신청 (또는 로그인 쿠키 필요)

개인의 "팔로우/구독 내역"은 공개된 정보가 아니라 네이버 로그인이 필요한 비밀 정보입니다.

그래서 파이썬 코드 안에 나의 네이버 로그인 인증 정보(쿠키 값)를 살짝 넣어주어야 파이썬이 네이버인 척 접속해서 내 팔로우/구독 기간을 읽어올 수 있습니다.

기본 작동 방식 (우리가 만들 앱의 구조)

내가 팔로우하거나 구독한 스트리머의 채널 ID를 입력합니다.

파이썬이 치지직 서버에 접속해서 "이 스트리머의 생방송 상태(라이브 중인지)", "팔로우 날짜 / 구독 개월 수" 데이터를 받아옵니다.

화면에 예쁘게 "OOO 스트리머 구독 3개월 차 (팔로우 진행 중 / 방송 라이브 ON!)" 형태로 띄워줍니다!

🚀 어떤 기능부터 만들어볼까요?
치지직 연동 앱은 난이도별 단계로 나누어 만들어보면 훨씬 쉽고 재미있습니다!

1단계 (쉬움): 내가 좋아하는 스트리머 채널 ID만 넣으면 현재 생방송 중인지 + 팔로워 수 실시간으로 가져오는 앱 (로그인 불필요!)

2단계 (조금 더 깊게): 내 쿠키값을 활용해서 내 계정의 팔로우 목록 & 구독 기간/개월 수 쫙 조회해서 보여주는 앱

지금 바로 파이썬 기본 코드부터 1단계로 차근차근 시작해 볼까요?

어떤 단계부터 도전해 볼까요?

1단계: 스트리머 생방송 여부 및 채널 정보 가져오기

2단계: 내 계정 쿠키 넣어서 팔로우/구독 기간 조회하기
치지직 스트리머 생방송 여부와 채널 정보를 파이썬으로 가져오는 1단계 코드 작성해줘.

네이버 치지직(CHZZK)의 스트리머 채널 정보와 현재 생방송(라이브) 진행 여부를 파이썬 기본 모듈만으로 불러오는 1단계 코드입니다!

치지직은 외부 프로그램(파이썬)이 그냥 접근하면 차단하는 경우가 있어서, 파이썬 코드 안에 User-Agent (웹 브라우저인 척하는 신분증) 헤더를 살짝 넣어주어야 정보를 잘 가져옵니다.

1. 스트리머 Channel ID(채널 아이디) 찾기
치지직 사이트(chzzk.naver.com)에서 자주 보는 스트리머의 채널 페이지로 들어갑니다.
주소창을 보시면 아래처럼 길고 복잡한 영어+숫자 조합이 있습니다.

예시 주소: [https://chzzk.naver.com/45e711760420703e6545722129532d56](https://chzzk.naver.com/45e711760420703e6545722129532d56)

여기서 45e711760420703e6545722129532d56 부분이 바로 채널 ID입니다!

2. 파이썬 소스 코드 (chzzk_check.py)
IDLE 새 창(Ctrl + N)에 아래 코드를 적고 실행해 보세요!

Python
import json
import urllib.request

# 1. 정보를 조회하고 싶은 스트리머의 채널 ID를 여기에 넣으세요!
# (아래 ID는 예시용 채널 ID입니다)
channel_id = "45e711760420703e6545722129532d56"

# 치지직 오픈 API 주소
url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"

# 웹 브라우저처럼 보이게 만들어주는 헤더 설정 (차단 방지)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

try:
    # 파이썬으로 치지직 서버에 요청 보내기
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        
        # 가져온 데이터에서 필요한 정보만 쏙쏙 뽑기
        channel_info = data['content']
        channel_name = channel_info['channelName']      # 스트리머 이름
        follower_count = channel_info['followerCount']  # 팔로워 수
        open_live = channel_info['openLive']            # 생방송 여부 (True / False)

        print("\n" + "=" * 35)
        print(f"🟢 스트리머: {channel_name}")
        print(f"👥 팔로워 수: {follower_count:,}명")
        
        # 우리가 배운 if-else문으로 생방송 상태에 따라 다르게 출력하기!
        if open_live:
            print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")
        else:
            print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")
        print("=" * 35)

except Exception as e:
    print("채널 정보를 가져오는 데 실패했습니다. 채널 ID를 다시 확인해 주세요!")
    print(f"오류 내용: {e}")
💡 코드 분석 (우리가 배웠던 내용 연결하기!)
urllib.request & json: 네이버 치지직 인터넷 주소에 접속해서 데이터를 텍스트 형태로 긁어오는 파이썬 기본 부품입니다.

open_live (True / False): 네이버 치지직이 방송 중이면 True, 안 켜졌으면 False라는 값을 보내줍니다.

if open_live:: 이 조건문 하나만 가지고 현재 생방송 중인지 아닌지를 판별해서 멋지게 문구를 출력해 줍니다!

원하는 스트리머의 채널 ID로 바꿔서 실행해 보세요. 방송이 켜져 있을 때와 꺼져 있을 때 문구가 바뀌는 걸 직접 확인하실 수 있습니다!

다음으로 어떤 기능을 추가해 볼까요?

2단계: 내 로그인 쿠키 넣어서 '팔로우/구독 기간' 조회 도전하기

여러 명의 스트리머를 한 번에 조회하는 리스트 기능 추가하기
흠.... 내가 파이썬을 공부한 이유가 사라지게 만드는 녀석이군... 이럴거면 공부 왜 했나... 너가 딸깍하면 만들잖아...

아이고, 어떤 마음이신지 너무 잘 알 것 같아요! 😂

내가 몇 날 며칠 고민해서 if, while, count 변수 고쳐가며 로그인 프로그램 짜고 있었는데, AI한테 한마디 하니까 순식간에 코드를 툭 뱉어내는 걸 보면 "현타(현실 타격)"가 오는 게 지극히 당연합니다.

하지만 전혀 그렇게 낙담하실 필요가 없습니다! 왜 파이썬 공부를 하신 게 의미 있고 대단한 일인지 딱 3가지로 말씀드릴게요.

1. AI는 '엔진'이고, 코딩을 아는 사람이 '운전수'입니다 🚗
AI가 코드를 잘 짜는 건 맞지만, 우리가 문법과 흐름을 모르면 AI가 준 코드가 맞는지, 틀렸는지, 왜 에러가 나는지 전혀 알 수가 없습니다.

아까 무한 루프 걸렸을 때 Ctrl + C로 끄거나 break 위치를 잡으셨던 것 기억하시나요?

비밀번호 5번 틀렸는데 변경 창이 뜨는 버그를 발견하고 login = 1 플래그 변수를 써서 스스로 고치셨던 것 기억하시죠?

만약 파이썬 기초를 안 배우셨다면 AI가 준 코드에 오류가 났을 때 아무것도 못 하고 멍하니 계셨을 거예요. AI를 내 마음대로 조종하고 감독하려면 기본 문법을 아는 사람이어야만 가능합니다.

2. '딸깍'으로 만든 코드는 금방 무너집니다 🏗️
AI는 내가 요청한 부분만 거창하게 짜줄 뿐, 전체 프로그램의 논리 구조를 처음부터 끝까지 혼자서 완벽하게 유지하진 못합니다.

방금 만든 회원가입/로그인 프로그램처럼:

아이디 입력받고

비밀번호 8자 체크하고

틀리면 5번 카운트하고

성공했을 때만 비밀번호 변경 넘어가고

이 전체 설계도와 아이디어는 질문자님 머릿속에서 나온 논리였습니다! AI는 그저 주문받은 대로 벽돌을 쌓아주는 일꾼일 뿐이고, 건축가는 바로 질문자님인 거죠.

3. 계산기가 나왔다고 수학을 안 배우지 않는 것과 같습니다 🧮
계산기 버튼만 누르면 덧셈·뺄셈·곱셈이 다 되지만, 우리는 학교에서 연산 원리를 배웁니다. 원리를 알아야 무엇을 계산해야 할지 알 수 있으니까요.

파이썬 공부도 똑같습니다!
기초를 배운 덕분에 "아, 치지직 API 데이터를 가져와서 if문으로 뱅온 여부를 판별하면 되겠구나!" 하고 프로그램이 돌아가는 원리와 구조를 이해할 수 있게 된 것입니다.

지금 질문자님은 단순히 책 보고 따라 친 게 아니라, 문제를 정의하고, 조건문을 설계하고, 버그를 잡아서 완성시키는 '진짜 개발자의 사고방식'을 경험하셨습니다.

AI라는 아주 똑똑한 보조 도구를 얻었다고 생각하시고, 앞으로 만들고 싶은 앱이 있을 때 AI를 심부름꾼처럼 부려먹으시면 됩니다! 🔥

AI를 일꾼으로 부려먹으면서 나만의 앱/프로젝트 계속 만들어볼까요?

예
import json

import urllib.request



# 1. 정보를 조회하고 싶은 스트리머의 채널 ID를 여기에 넣으세요!

# (아래 ID는 예시용 채널 ID입니다)

channel_id = "b5ed5db484d04faf4d150aedd362f34b"



# 치지직 오픈 API 주소

url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"



# 웹 브라우저처럼 보이게 만들어주는 헤더 설정 (차단 방지)

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

}



try:

    # 파이썬으로 치지직 서버에 요청 보내기

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:

        data = json.loads(response.read().decode('utf-8'))

        

        # 가져온 데이터에서 필요한 정보만 쏙쏙 뽑기

        channel_info = data['content']

        channel_name = channel_info['channelName']      # 스트리머 이름

        follower_count = channel_info['followerCount']  # 팔로워 수

        open_live = channel_info['openLive']            # 생방송 여부 (True / False)



        print("\n" + "=" * 35)

        print(f"🟢 스트리머: {channel_name}")

        print(f"👥 팔로워 수: {follower_count:,}명")

        

        # 우리가 배운 if-else문으로 생방송 상태에 따라 다르게 출력하기!

        if open_live:

            print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")

        else:

            print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")

        print("=" * 35)



except Exception as e:

    print("채널 정보를 가져오는 데 실패했습니다. 채널 ID를 다시 확인해 주세요!")

    print(f"오류 내용: {e}")



    # 1. 정보를 조회하고 싶은 스트리머의 채널 ID를 여기에 넣으세요!

# (아래 ID는 예시용 채널 ID입니다)

channel_id = "45e71a76e949e16a34764deb962f9d9f"



# 치지직 오픈 API 주소

url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"



# 웹 브라우저처럼 보이게 만들어주는 헤더 설정 (차단 방지)

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

}



try:

    # 파이썬으로 치지직 서버에 요청 보내기

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:

        data = json.loads(response.read().decode('utf-8'))

        

        # 가져온 데이터에서 필요한 정보만 쏙쏙 뽑기

        channel_info = data['content']

        channel_name = channel_info['channelName']      # 스트리머 이름

        follower_count = channel_info['followerCount']  # 팔로워 수

        open_live = channel_info['openLive']            # 생방송 여부 (True / False)



        print("\n" + "=" * 35)

        print(f"🟢 스트리머: {channel_name}")

        print(f"👥 팔로워 수: {follower_count:,}명")

        

        # 우리가 배운 if-else문으로 생방송 상태에 따라 다르게 출력하기!

        if open_live:

            print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")

        else:

            print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")

        print("=" * 35)



except Exception as e:

    print("채널 정보를 가져오는 데 실패했습니다. 채널 ID를 다시 확인해 주세요!")

    print(f"오류 내용: {e}")

    



# 1. 정보를 조회하고 싶은 스트리머의 채널 ID를 여기에 넣으세요!

# (아래 ID는 예시용 채널 ID입니다)

channel_id = "36ddb9bb4f17593b60f1b63cec86611d"



# 치지직 오픈 API 주소

url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"



# 웹 브라우저처럼 보이게 만들어주는 헤더 설정 (차단 방지)

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

}



try:

    # 파이썬으로 치지직 서버에 요청 보내기

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:

        data = json.loads(response.read().decode('utf-8'))

        

        # 가져온 데이터에서 필요한 정보만 쏙쏙 뽑기

        channel_info = data['content']

        channel_name = channel_info['channelName']      # 스트리머 이름

        follower_count = channel_info['followerCount']  # 팔로워 수

        open_live = channel_info['openLive']            # 생방송 여부 (True / False)



        print("\n" + "=" * 35)

        print(f"🟢 스트리머: {channel_name}")

        print(f"👥 팔로워 수: {follower_count:,}명")

        

        # 우리가 배운 if-else문으로 생방송 상태에 따라 다르게 출력하기!

        if open_live:

            print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")

        else:

            print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")

        print("=" * 35)



except Exception as e:

    print("채널 정보를 가져오는 데 실패했습니다. 채널 ID를 다시 확인해 주세요!")

    print(f"오류 내용: {e}")



    # 1. 정보를 조회하고 싶은 스트리머의 채널 ID를 여기에 넣으세요!

# (아래 ID는 예시용 채널 ID입니다)

channel_id = "a6c4ddb09cdb160478996007bff35296"



# 치지직 오픈 API 주소

url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"



# 웹 브라우저처럼 보이게 만들어주는 헤더 설정 (차단 방지)

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

}



try:

    # 파이썬으로 치지직 서버에 요청 보내기

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:

        data = json.loads(response.read().decode('utf-8'))

        

        # 가져온 데이터에서 필요한 정보만 쏙쏙 뽑기

        channel_info = data['content']

        channel_name = channel_info['channelName']      # 스트리머 이름

        follower_count = channel_info['followerCount']  # 팔로워 수

        open_live = channel_info['openLive']            # 생방송 여부 (True / False)



        print("\n" + "=" * 35)

        print(f"🟢 스트리머: {channel_name}")

        print(f"👥 팔로워 수: {follower_count:,}명")

        

        # 우리가 배운 if-else문으로 생방송 상태에 따라 다르게 출력하기!

        if open_live:

            print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")

        else:

            print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")

        print("=" * 35)



except Exception as e:

    print("채널 정보를 가져오는 데 실패했습니다. 채널 ID를 다시 확인해 주세요!")

    print(f"오류 내용: {e}")





# 1. 정보를 조회하고 싶은 스트리머의 채널 ID를 여기에 넣으세요!

# (아래 ID는 예시용 채널 ID입니다)

channel_id = "4325b1d5bbc321fad3042306646e2e50"



# 치지직 오픈 API 주소

url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"



# 웹 브라우저처럼 보이게 만들어주는 헤더 설정 (차단 방지)

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

}



try:

    # 파이썬으로 치지직 서버에 요청 보내기

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:

        data = json.loads(response.read().decode('utf-8'))

        

        # 가져온 데이터에서 필요한 정보만 쏙쏙 뽑기

        channel_info = data['content']

        channel_name = channel_info['channelName']      # 스트리머 이름

        follower_count = channel_info['followerCount']  # 팔로워 수

        open_live = channel_info['openLive']            # 생방송 여부 (True / False)



        print("\n" + "=" * 35)

        print(f"🟢 스트리머: {channel_name}")

        print(f"👥 팔로워 수: {follower_count:,}명")

        

        # 우리가 배운 if-else문으로 생방송 상태에 따라 다르게 출력하기!

        if open_live:

            print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")

        else:

            print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")

        print("=" * 35)



except Exception as e:

    print("채널 정보를 가져오는 데 실패했습니다. 채널 ID를 다시 확인해 주세요!")

    print(f"오류 내용: {e}")





# 1. 정보를 조회하고 싶은 스트리머의 채널 ID를 여기에 넣으세요!

# (아래 ID는 예시용 채널 ID입니다)

channel_id = "b044e3a3b9259246bc92e863e7d3f3b8"



# 치지직 오픈 API 주소

url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"



# 웹 브라우저처럼 보이게 만들어주는 헤더 설정 (차단 방지)

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

}



try:

    # 파이썬으로 치지직 서버에 요청 보내기

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:

        data = json.loads(response.read().decode('utf-8'))

        

        # 가져온 데이터에서 필요한 정보만 쏙쏙 뽑기

        channel_info = data['content']

        channel_name = channel_info['channelName']      # 스트리머 이름

        follower_count = channel_info['followerCount']  # 팔로워 수

        open_live = channel_info['openLive']            # 생방송 여부 (True / False)



        print("\n" + "=" * 35)

        print(f"🟢 스트리머: {channel_name}")

        print(f"👥 팔로워 수: {follower_count:,}명")

        

        # 우리가 배운 if-else문으로 생방송 상태에 따라 다르게 출력하기!

        if open_live:

            print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")

        else:

            print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")

        print("=" * 35)



except Exception as e:

    print("채널 정보를 가져오는 데 실패했습니다. 채널 ID를 다시 확인해 주세요!")

    print(f"오류 내용: {e}")





# 1. 정보를 조회하고 싶은 스트리머의 채널 ID를 여기에 넣으세요!

# (아래 ID는 예시용 채널 ID입니다)

channel_id = "4515b179f86b67b4981e16190817c580"



# 치지직 오픈 API 주소

url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"



# 웹 브라우저처럼 보이게 만들어주는 헤더 설정 (차단 방지)

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

}



try:

    # 파이썬으로 치지직 서버에 요청 보내기

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:

        data = json.loads(response.read().decode('utf-8'))

        

        # 가져온 데이터에서 필요한 정보만 쏙쏙 뽑기

        channel_info = data['content']

        channel_name = channel_info['channelName']      # 스트리머 이름

        follower_count = channel_info['followerCount']  # 팔로워 수

        open_live = channel_info['openLive']            # 생방송 여부 (True / False)



        print("\n" + "=" * 35)

        print(f"🟢 스트리머: {channel_name}")

        print(f"👥 팔로워 수: {follower_count:,}명")

        

        # 우리가 배운 if-else문으로 생방송 상태에 따라 다르게 출력하기!

        if open_live:

            print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")

        else:

            print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")

        print("=" * 35)



except Exception as e:

    print("채널 정보를 가져오는 데 실패했습니다. 채널 ID를 다시 확인해 주세요!")

    print(f"오류 내용: {e}")





# 1. 정보를 조회하고 싶은 스트리머의 채널 ID를 여기에 넣으세요!

# (아래 ID는 예시용 채널 ID입니다)

channel_id = "64d76089fba26b180d9c9e48a32600d9"



# 치지직 오픈 API 주소

url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"



# 웹 브라우저처럼 보이게 만들어주는 헤더 설정 (차단 방지)

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

}



try:

    # 파이썬으로 치지직 서버에 요청 보내기

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:

        data = json.loads(response.read().decode('utf-8'))

        

        # 가져온 데이터에서 필요한 정보만 쏙쏙 뽑기

        channel_info = data['content']

        channel_name = channel_info['channelName']      # 스트리머 이름

        follower_count = channel_info['followerCount']  # 팔로워 수

        open_live = channel_info['openLive']            # 생방송 여부 (True / False)



        print("\n" + "=" * 35)

        print(f"🟢 스트리머: {channel_name}")

        print(f"👥 팔로워 수: {follower_count:,}명")

        

        # 우리가 배운 if-else문으로 생방송 상태에 따라 다르게 출력하기!

        if open_live:

            print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")

        else:

            print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")

        print("=" * 35)



except Exception as e:

    print("채널 정보를 가져오는 데 실패했습니다. 채널 ID를 다시 확인해 주세요!")

    print(f"오류 내용: {e}")





# 1. 정보를 조회하고 싶은 스트리머의 채널 ID를 여기에 넣으세요!

# (아래 ID는 예시용 채널 ID입니다)

channel_id = "8fd39bb8de623317de90654718638b10"



# 치지직 오픈 API 주소

url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"



# 웹 브라우저처럼 보이게 만들어주는 헤더 설정 (차단 방지)

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

}



try:

    # 파이썬으로 치지직 서버에 요청 보내기

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:

        data = json.loads(response.read().decode('utf-8'))

        

        # 가져온 데이터에서 필요한 정보만 쏙쏙 뽑기

        channel_info = data['content']

        channel_name = channel_info['channelName']      # 스트리머 이름

        follower_count = channel_info['followerCount']  # 팔로워 수

        open_live = channel_info['openLive']            # 생방송 여부 (True / False)



        print("\n" + "=" * 35)

        print(f"🟢 스트리머: {channel_name}")

        print(f"👥 팔로워 수: {follower_count:,}명")

        

        # 우리가 배운 if-else문으로 생방송 상태에 따라 다르게 출력하기!

        if open_live:

            print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")

        else:

            print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")

        print("=" * 35)



except Exception as e:

    print("채널 정보를 가져오는 데 실패했습니다. 채널 ID를 다시 확인해 주세요!")

    print(f"오류 내용: {e}")





# 1. 정보를 조회하고 싶은 스트리머의 채널 ID를 여기에 넣으세요!

# (아래 ID는 예시용 채널 ID입니다)

channel_id = "516937b5f85cbf2249ce31b0ad046b0f"



# 치지직 오픈 API 주소

url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"



# 웹 브라우저처럼 보이게 만들어주는 헤더 설정 (차단 방지)

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

}



try:

    # 파이썬으로 치지직 서버에 요청 보내기

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:

        data = json.loads(response.read().decode('utf-8'))

        

        # 가져온 데이터에서 필요한 정보만 쏙쏙 뽑기

        channel_info = data['content']

        channel_name = channel_info['channelName']      # 스트리머 이름

        follower_count = channel_info['followerCount']  # 팔로워 수

        open_live = channel_info['openLive']            # 생방송 여부 (True / False)



        print("\n" + "=" * 35)

        print(f"🟢 스트리머: {channel_name}")

        print(f"👥 팔로워 수: {follower_count:,}명")

        

        # 우리가 배운 if-else문으로 생방송 상태에 따라 다르게 출력하기!

        if open_live:

            print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")

        else:

            print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")

        print("=" * 35)



except Exception as e:

    print("채널 정보를 가져오는 데 실패했습니다. 채널 ID를 다시 확인해 주세요!")

    print(f"오류 내용: {e}")





# 1. 정보를 조회하고 싶은 스트리머의 채널 ID를 여기에 넣으세요!

# (아래 ID는 예시용 채널 ID입니다)

channel_id = "4d812b586ff63f8a2946e64fa860bbf5"



# 치지직 오픈 API 주소

url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"



# 웹 브라우저처럼 보이게 만들어주는 헤더 설정 (차단 방지)

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

}



try:

    # 파이썬으로 치지직 서버에 요청 보내기

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:

        data = json.loads(response.read().decode('utf-8'))

        

        # 가져온 데이터에서 필요한 정보만 쏙쏙 뽑기

        channel_info = data['content']

        channel_name = channel_info['channelName']      # 스트리머 이름

        follower_count = channel_info['followerCount']  # 팔로워 수

        open_live = channel_info['openLive']            # 생방송 여부 (True / False)



        print("\n" + "=" * 35)

        print(f"🟢 스트리머: {channel_name}")

        print(f"👥 팔로워 수: {follower_count:,}명")

        

        # 우리가 배운 if-else문으로 생방송 상태에 따라 다르게 출력하기!

        if open_live:

            print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")

        else:

            print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")

        print("=" * 35)



except Exception as e:

    print("채널 정보를 가져오는 데 실패했습니다. 채널 ID를 다시 확인해 주세요!")

    print(f"오류 내용: {e}")







완성

보내주신 코드를 보니 여러 채널 ID에 대해 동일한 비즈니스 로직(API 요청, JSON 파싱, 방송 상태 출력)이 계속 복사-붙여넣기되어 반복되고 있습니다!

지금처럼 코드가 길어지면 나중에 수정이 필요할 때 모든 블록을 다 고쳐야 하는 문제가 생깁니다. 파이썬에서는 이럴 때 리스트(List)와 for 반복문, 그리고 함수(Function)를 활용해 깔끔하게 정돈할 수 있습니다.

🛠 리팩토링된 최적화 코드
중복 코드를 제거하고, 채널 ID 리스트를 for문으로 돌려 한 번에 처리하도록 개선한 버전입니다.

Python
import json
import urllib.request

# 1. 조회하고 싶은 스트리머 채널 ID 목록
channel_ids = [
    "b5ed5db484d04faf4d150aedd362f34b",
    "45e71a76e949e16a34764deb962f9d9f",
    "36ddb9bb4f17593b60f1b63cec86611d",
    "a6c4ddb09cdb160478996007bff35296",
    "4325b1d5bbc321fad3042306646e2e50",
    "b044e3a3b9259246bc92e863e7d3f3b8",
    "4515b179f86b67b4981e16190817c580",
    "64d76089fba26b180d9c9e48a32600d9",
    "8fd39bb8de623317de90654718638b10",
    "516937b5f85cbf2249ce31b0ad046b0f",
    "4d812b586ff63f8a2946e64fa860bbf5"
]

# 차단 방지용 헤더
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def get_channel_info(channel_id):
    """채널 ID를 입력받아 치지직 방송 상태 및 정보를 출력하는 함수"""
    url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            channel_info = data['content']
            channel_name = channel_info['channelName']
            follower_count = channel_info['followerCount']
            open_live = channel_info['openLive']

            print("\n" + "=" * 35)
            print(f"🟢 스트리머: {channel_name}")
            print(f"👥 팔로워 수: {follower_count:,}명")
            
            if open_live:
                print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")
            else:
                print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")
            print("=" * 35)

    except Exception as e:
        print(f"\n[ID: {channel_id}] 채널 정보를 가져오는 데 실패했습니다.")
        print(f"오류 내용: {e}")

# 2. 반복문을 통해 등록된 모든 채널 조회
print("🚀 치지직 스트리머 방송 상태 조회를 시작합니다...")
for cid in channel_ids:
    get_channel_info(cid)
✨ 코드에서 개선된 점
유지보수성 향상: 출력을 변경하거나 기능을 추가하고 싶을 때 get_channel_info() 함수 내부의 코드만 한 번 고치면 됩니다.

채널 추가/삭제 용이: 새로운 스트리머를 추가하고 싶다면 channel_ids 리스트에 ID 문자열만 더해주면 끝납니다.

가독성 향상: 똑같은 구조가 수백 줄 이어지던 코드가 50여 줄로 압축되었습니다.

이 코드에서 추가로 확장해보고 싶은 기능이 있으신가요?

방송 중인 스트리머 목록만 따로 모아서 보기

일정 시간마다 자동으로 감시하는 모니터링 만들기

discord 보트나 알림 연결 방법 알아보기
현재 방송 보고 있는 시청자 수 보는 것도 추가해줘

치지직 API에서 현재 방송 중인 시청자 수(concurrentUserCount)를 함께 가져오려면, 채널 정보 API(.../channels/{channel_id})가 아니라 라이브 정보 API ([https://api.chzzk.naver.com/service/v2/channels/](https://api.chzzk.naver.com/service/v2/channels/){channel_id}/live-detail)를 함께 조회해야 합니다.

기존 코드에 라이브 상세 정보 요청을 추가하여, 방송 중일 때 현재 시청자 수와 방송 제목까지 함께 출력하도록 수정한 코드입니다.

Python
import json
import urllib.request

# 1. 조회하고 싶은 스트리머 채널 ID 목록
channel_ids = [
    "b5ed5db484d04faf4d150aedd362f34b",
    "45e71a76e949e16a34764deb962f9d9f",
    "36ddb9bb4f17593b60f1b63cec86611d",
    "a6c4ddb09cdb160478996007bff35296",
    "4325b1d5bbc321fad3042306646e2e50",
    "b044e3a3b9259246bc92e863e7d3f3b8",
    "4515b179f86b67b4981e16190817c580",
    "64d76089fba26b180d9c9e48a32600d9",
    "8fd39bb8de623317de90654718638b10",
    "516937b5f85cbf2249ce31b0ad046b0f",
    "4d812b586ff63f8a2946e64fa860bbf5"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def fetch_json(url):
    """API URL을 입력받아 JSON 데이터를 반환하는 공통 함수"""
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))

def get_channel_info(channel_id):
    """채널 정보 및 방송 중일 때 현재 시청자 수를 가져오는 함수"""
    channel_url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"
    live_url = f"https://api.chzzk.naver.com/service/v2/channels/{channel_id}/live-detail"
    
    try:
        # 1. 채널 기본 정보 가져오기
        channel_data = fetch_json(channel_url)['content']
        channel_name = channel_data['channelName']
        open_live = channel_data['openLive']

        print("\n" + "=" * 40)
        print(f"🟢 스트리머: {channel_name}")
        
        if open_live:
            # 2. 방송 중일 경우 라이브 상세 정보에서 시청자 수 조회
            live_data = fetch_json(live_url)['content']
            live_title = live_data.get('liveTitle', '제목 없음')
            user_count = live_data.get('concurrentUserCount', 0)
            category = live_data.get('liveCategoryValue', '카테고리 없음')

            print("🔴 상태: [생방송 중 (LIVE)]")
            print(f"📌 방송 제목: {live_title}")
            print(f"🎮 카테고리: {category}")
            print(f"👀 현재 시청자 수: {user_count:,}명")
        else:
            print("⚪️ 상태: [방송 꺼짐 (OFF)]")
            
        print("=" * 40)

    except Exception as e:
        print(f"\n[ID: {channel_id}] 정보를 가져오는 데 실패했습니다: {e}")

# 실행
print("🚀 치지직 라이브 시청자 수 및 방송 상태 조회를 시작합니다...")
for cid in channel_ids:
    get_channel_info(cid)
💡 주요 변경 사항
live-detail API 추가: 방송이 켜져 있을 때(openLive == True) 해당 API를 추가로 호출합니다.

concurrentUserCount 가져오기: 현재 실시간으로 시청하고 있는 사용자 수를 표기합니다.

추가 정보 출력: 시청자 수 외에도 방송 이해에 도움 되는 방송 제목과 게임/카테고리 정보도 함께 출력되도록 구성했습니다.

다음으로 어떤 기능을 구현해 볼까요?

시청자 수 순서대로 정렬해서 보기

특정 시청자 수 이상일 때만 알림 출력하기
이걸 사이트화 시킬 수 있을까?

네, 충분히 사이트(웹 애플리케이션)로 만들 수 있습니다!

지금 만드신 파이썬 코드는 백엔드(서버) 역할을 하는 로직입니다. 이걸 웹사이트로 바꾸려면 크게 두 가지 방법이 있습니다.

🛠️ 사이트화하는 2가지 방법
방법 1. 파이썬만 사용해서 빠르게 만들기 (Streamlit 추천)
웹 프론트엔드(HTML/CSS/JS)를 전혀 몰라도 파이썬 코드만으로 깔끔한 웹 사이트를 만들어주는 라이브러리입니다. 초보자나 개인 프로젝트용으로 가장 추천하는 방식입니다.

장점: 기존 파이썬 코드를 90% 이상 그대로 활용 가능, 디자인 자동 완성, 무료 배포 가능(Streamlit Community Cloud).

단점: 디자인 세부 수정에 한계가 있음.

방법 2. 본격적인 웹 서비스로 만들기 (Flask 또는 FastAPI + HTML/CSS)
파이썬 백엔드 웹 프레임워크(Flask 등)를 이용해 API 서버를 만들고, 웹 브라우저 화면(HTML, CSS, JavaScript)을 연결하는 정석적인 방식입니다.

장점: 내가 원하는 대로 예쁘게 UI/UX 디자인 가능, 서비스 확장성 높음.

단점: HTML, CSS, JavaScript 기초 지식이 필요함.

🚀 [방법 1] Streamlit으로 바로 웹사이트 만드는 코드
먼저 터미널(명령 프롬프트)에서 Streamlit을 설치합니다.

Bash
pip install streamlit
그 후 아래 코드를 app.py라는 파일로 저장하고 실행해보세요!

Python
import json
import urllib.request
import streamlit as st

# 차단 방지용 헤더
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def fetch_json(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))

# Streamlit 웹 화면 구성
st.set_page_config(page_title="치지직 라이브 모니터", page_icon="📺", layout="wide")
st.title("📺 치지직 스트리머 실시간 방송 상태")

# 등록할 스트리머 채널 ID 리스트
channel_ids = [
    "b5ed5db484d04faf4d150aedd362f34b",
    "45e71a76e949e16a34764deb962f9d9f",
    "36ddb9bb4f17593b60f1b63cec86611d",
    "a6c4ddb09cdb160478996007bff35296",
    "4325b1d5bbc321fad3042306646e2e50",
    "b044e3a3b9259246bc92e863e7d3f3b8",
    "4515b179f86b67b4981e16190817c580",
    "64d76089fba26b180d9c9e48a32600d9",
    "8fd39bb8de623317de90654718638b10",
    "516937b5f85cbf2249ce31b0ad046b0f",
    "4d812b586ff63f8a2946e64fa860bbf5"
]

if st.button("🔄 새로고침"):
    st.rerun()

cols = st.columns(3) # 3열 카드로 배치

for idx, cid in enumerate(channel_ids):
    col = cols[idx % 3] # 카드 배치 위치
    channel_url = f"https://api.chzzk.naver.com/service/v1/channels/{cid}"
    live_url = f"https://api.chzzk.naver.com/service/v2/channels/{cid}/live-detail"

    try:
        channel_data = fetch_json(channel_url)['content']
        channel_name = channel_data['channelName']
        open_live = channel_data['openLive']

        with col:
            if open_live:
                live_data = fetch_json(live_url)['content']
                live_title = live_data.get('liveTitle', '제목 없음')
                user_count = live_data.get('concurrentUserCount', 0)
                category = live_data.get('liveCategoryValue', '카테고리 없음')

                st.success(f"🔴 **{channel_name}** (LIVE)")
                st.write(f"**제목:** {live_title}")
                st.write(f"**카테고리:** {category}")
                st.metric(label="현재 시청자 수", value=f"{user_count:,}명")
                st.link_button("방송 보러가기", f"https://chzzk.naver.com/live/{cid}")
            else:
                st.gray(f"⚪ **{channel_name}** (OFF)")
                st.caption("현재 방송 꺼짐")
    except Exception as e:
        col.error(f"불러오기 실패 ({cid[:6]}...)")
실행 방법
터미널에 아래 명령어를 입력하면 자동으로 웹 브라우저가 열리면서 웹사이트 형태로 표출됩니다!

Bash
streamlit run app.py
어떤 방향으로 진행해보고 싶으신가요?

Streamlit 코드로 만든 웹사이트 인터넷에 무료로 배포하기

HTML/CSS로 직접 디자인하는 Flask 방식 알아보기

웹사이트에 채널 ID를 직접 입력해 추가하는 기능 만들기
내가 HTML/CSS 지식이 없더라도 AI활용해서 가능해? Flask방식이

네, 100% 가능합니다!

요즘은 AI(ChatGPT, Claude, Gemini 등)에게 "내가 원하는 웹페이지 모양과 기능"만 구체적으로 말하면 HTML, CSS, JavaScript 코드를 전부 다 짜주기 때문에, HTML/CSS를 하나도 몰라도 Flask 방식을 충분히 만들 수 있습니다.

실제로 작성하시는 과정은 개발자가 되는 느낌이라기보다는 "AI 디자이너/개발자에게 지시를 내리는 관리자" 역할에 가깝습니다.

🤖 AI를 활용해 Flask 웹사이트 만드는 흐름
HTML/CSS 지식이 없을 때 AI를 다루는 가장 쉬운 3단계 방법입니다.

[1단계: AI에게 코드 요청]  ➔  [2단계: 폴더에 파일 복사-붙여넣기]  ➔  [3단계: 실행 및 수정]
1단계: Flask 프로젝트 기본 구조 만들기
Flask는 파일들을 약속된 폴더에 넣어두어야 동작합니다. 내 컴퓨터에 아래처럼 폴더와 파일만 만들어두시면 됩니다.

Plaintext
my_chzzk_site/
├── app.py           <-- 파이썬 (백엔드 로직)
└── templates/
    └── index.html   <-- HTML/CSS (화면 디자인 - AI가 전부 작성)
2단계: AI에게 이렇게 요청하기 (프롬프트 예시)
HTML/CSS 코드를 직접 쓸 필요 없이, AI에게 아래처럼 요청해보세요.

AI에게 보낼 질문 예시:
"치지직 스트리머 방송 상태 모니터링 사이트를 Flask로 만들려고 해.

app.py에 들어갈 파이썬 백엔드 코드 작성해줘.

templates/index.html에 들어갈 디자인 예쁜 웹 화면 코드 작성해줘. HTML/CSS 몰라도 바로 복사해서 쓸 수 있게 통합해서 만들어줘.

네이버 치지직 느낌이 나도록 **어두운 테마(Dark Mode)**와 네온 초록색 강조를 사용해줘.

방송 중인 채널은 빨간색 LIVE 태그와 함께 시청자 수, 방송 제목, 카테고리를 카드 형태로 깔끔하게 보여줘."

3단계: AI가 짜준 예시 코드 (바로 테스트해보기)
AI가 출력해줄 법한 완성본 코드입니다. 한번 실행 구조를 확인해보세요!

① app.py (파이썬 파일)
Python
import json
import urllib.request
from flask import Flask, render_template

app = Flask(__name__)

headers = {"User-Agent": "Mozilla/5.0"}

CHANNEL_IDS = [
    "b5ed5db484d04faf4d150aedd362f34b",
    "45e71a76e949e16a34764deb962f9d9f",
    "36ddb9bb4f17593b60f1b63cec86611d"
]

def get_data(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode('utf-8'))
    except:
        return None

@app.route('/')
def home():
    streamers = []
    for cid in CHANNEL_IDS:
        ch_info = get_data(f"https://api.chzzk.naver.com/service/v1/channels/{cid}")
        if not ch_info or not ch_info.get('content'):
            continue
        
        name = ch_info['content']['channelName']
        is_live = ch_info['content']['openLive']
        
        live_data = {}
        if is_live:
            detail = get_data(f"https://api.chzzk.naver.com/service/v2/channels/{cid}/live-detail")
            if detail and detail.get('content'):
                c = detail['content']
                live_data = {
                    'title': c.get('liveTitle', '제목 없음'),
                    'users': c.get('concurrentUserCount', 0),
                    'category': c.get('liveCategoryValue', '일반')
                }
        
        streamers.append({
            'id': cid,
            'name': name,
            'is_live': is_live,
            'live': live_data
        })
        
    return render_template('index.html', streamers=streamers)

if __name__ == '__main__':
    app.run(debug=True)
② templates/index.html (HTML + CSS 파일)
HTML
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>치지직 라이브 대시보드</title>
    <!-- AI가 예쁜 디자인 스타일을 이렇게 만들어줍니다 -->
    <style>
        body { background-color: #0f0f12; color: #ffffff; font-family: sans-serif; padding: 20px; }
        h1 { color: #00ffa3; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; margin-top: 20px; }
        .card { background: #1a1b20; border-radius: 12px; padding: 16px; border: 1px solid #2d2e36; }
        .live-badge { background: #ff4b4b; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 12px; }
        .off-badge { background: #555; color: #ccc; padding: 4px 8px; border-radius: 4px; font-size: 12px; }
        .count { font-size: 1.2rem; color: #00ffa3; font-weight: bold; margin-top: 8px; }
        a { display: inline-block; margin-top: 10px; color: #00ffa3; text-decoration: none; }
    </style>
</head>
<body>
    <h1>📺 치지직 라이브 모니터</h1>
    <div class="grid">
        {% for s in streamers %}
        <div class="card">
            <h3>
                {{ s.name }}
                {% if s.is_live %}
                    <span class="live-badge">LIVE</span>
                {% else %}
                    <span class="off-badge">OFF</span>
                {% endif %}
            </h3>
            
            {% if s.is_live %}
                <p>📌 {{ s.live.title }}</p>
                <p>🎮 {{ s.live.category }}</p>
                <div class="count">👀 {{ "{:,}".format(s.live.users) }}명 시청 중</div>
                <a href="https://chzzk.naver.com/live/{{ s.id }}" target="_blank">▶ 방송 보기</a>
            {% else %}
                <p style="color: #888;">현재 방송이 꺼져 있습니다.</p>
            {% endif %}
        </div>
        {% endfor %}
    </div>
</body>
</html>
💡 디자인을 수정하고 싶을 때 AI 조종 팁
HTML/CSS를 고치고 싶을 때도 코드를 직접 수정할 필요가 없습니다. 화면을 캡처하거나 원하는 점을 AI에게 말해보세요.

예시 1: "카드를 클릭하면 바로 치지직 방송으로 이동하게 만들어줘."

예시 2: "배경색을 좀 더 밝은 그레이 톤으로 바꿔주고 카드 마우스 올렸을 때 살짝 뜨는 효과 넣어줘."

예시 3: "모바일 화면(핸드폰)에서도 카드가 깨지지 않고 1열로 예쁘게 나오게 해줘."

AI가 수정된 코드만 쏙 뽑아주므로 복사해서 index.html에 덮어쓰기만 하면 됩니다.

어떤 것부터 시도해볼까요?

이 Flask 코드 내 컴퓨터에서 실행하는 방법 시작하기

AI에게 전달할 더 구체적인 HTML/CSS 디자인 프롬프트 모음 보기
위의 Flask 코드를 내 컴퓨터에서 폴더 만들고 실행하는 방법까지 단계별로 차근차근 알려줘.

컴퓨터에 파이썬만 설치되어 있다면 딱 5단계로 바로 실행해 볼 수 있습니다!

폴더 생성부터 첫 실행까지 차근차근 따라 해보세요.

1
프로젝트 폴더 및 파일 구성하기
파일 이름과 위치를 꼭 맞춰주세요
바탕화면 등 원하는 곳에 폴더를 만들고, 아래 구조처럼 파일과 폴더를 만들어주세요.

폴더 생성: my_chzzk_site 폴더 만들기

하위 폴더 생성: my_chzzk_site 폴더 안에 templates 폴더 만들기

파일 생성:

my_chzzk_site/app.py

my_chzzk_site/templates/index.html

📁 전체 폴더 구조 모양:

Plaintext
    > my_chzzk_site/
    > ├── app.py
    > └── templates/
    >     └── index.html
    > ```
  

  
    1. **`app.py`** 파일을 메모장이나 VS Code로 열고, 위에서 제공해 드린 파이썬(Flask) 코드를 그대로 복사해서 붙여넣고 저장(`Ctrl + S`)합니다.
    2. **`templates/index.html`** 파일을 열고, 위에서 제공해 드린 HTML/CSS 코드를 그대로 복사해서 붙여넣고 저장(`Ctrl + S`)합니다.
  

  
    1. `my_chzzk_site` 폴더를 열어둡니다.
    2. 폴더 상단의 **주소창**을 클릭하여 전체 선택한 뒤, `cmd`를 입력하고 **Enter**를 누릅니다.
    3. 까만색 터미널(명령 프롬프트) 창이 열리면서 현재 위치가 해당 폴더로 자동 설정됩니다.
  

  
    열린 터미널 창에 아래 명령어를 입력하고 **Enter**를 누릅니다.

bash
pip install flask

*(설치가 진행되며 `Successfully installed flask...` 문구가 나오면 준비 완료입니다.)*



1. 터미널 창에 아래 명령어를 입력하고 **Enter**를 누릅니다.

bash
python app.py


2. 실행이 정상적으로 완료되면 터미널에 아래와 비슷한 문구가 출력됩니다.

text
* Running on http://127.0.0.1:5000


3. 크롬 등 웹 브라우저를 열고 주소창에 **`[http://127.0.0.1:5000](http://127.0.0.1:5000)`** 을 입력하고 이동하면 내가 만든 웹사이트가 나타납니다! 🚀



💡 알아두면 유용한 팁
서버 종료하기: 터미널 창에서 Ctrl + C를 누르면 웹 서버가 꺼집니다.

코드 수정 반영: app.py 파일의 맨 아래 app.run(debug=True)로 설정되어 있어, 파이썬이나 HTML 코드를 수정하고 저장하면 웹 페이지를 새로고침만 해도 바로 변경사항이 반영됩니다.

다음 단계로 어떤 작업을 해볼까요?

채널 추가/삭제를 웹 화면에서 가능하게 만들기

자동으로 방송 상태를 새로고침하는 기능 추가하기
그니까 파일 만드는 법이랑 다 알려줘야 하는데...

컴퓨터 작업을 처음 해보시거나 익숙하지 않으시다면 파일이나 폴더를 직접 만드는 것부터 막힐 수 있습니다! 당연한 부분이니 차근차근 따라 해보세요.

윈도우(Windows) 기준으로 텍스트 파일(메모장)을 이용해서 폴더와 파일을 새로 만드는 방법 전체 과정을 스크린샷 보듯 세세하게 알려드릴게요.

1
1. 폴더 새로 만들기
바탕화면에 프로젝트용 작업 공간 만들기
바탕화면의 빈 곳에 마우스 우클릭을 합니다.

메뉴에서 [새로 만들기(N)] ➔ **[폴더(F)]**를 클릭합니다.

생성된 폴더 이름을 my_chzzk_site 라고 적고 Enter를 누릅니다.

2
2. 파일 확장명(확장자) 보이게 설정하기
가장 중요한 필수 설정 단계입니다!
윈도우는 기본적으로 파일 뒤의 .txt, .py, .html 같은 확장명을 숨겨놓습니다. 이를 풀어주어야 코딩용 파일로 바꿀 수 있습니다.

방금 만든 my_chzzk_site 폴더를 더블 클릭해서 들어갑니다.

폴더 창 맨 위 메뉴에서 [보기] ➔ [표시] ➔ **[파일 확장명]**을 **체크(클릭)**해 줍니다.
(윈도우 10은 상단 '보기' 탭 클릭 후 '파일 확장명' 체크박스 체크)

3
3. app.py 파일 만들기
파이썬 백엔드 코드 파일 만들기
my_chzzk_site 폴더 안의 빈 공간에 마우스 우클릭을 합니다.

[새로 만들기(N)] ➔ **[텍스트 문서]**를 클릭합니다.

이름이 새 텍스트 문서.txt로 나오는데, 이름 전체를 지우고 app.py 로 바꾼 뒤 Enter를 누릅니다.

"파일의 확장명을 변경하면 사용할 수 없게 될 수도 있습니다. 변경하시겠습니까?" 라는 경고창이 뜨면 **[예]**를 누릅니다.

이제 app.py 파일을 마우스 우클릭 ➔ [연결 프로그램] ➔ **[메모장]**으로 엽니다.

이전에 안내해 드린 **app.py용 파이썬 코드를 복사해서 붙여넣고 저장(Ctrl + S)**한 뒤 메모장을 닫습니다.

4
4. templates 폴더 및 index.html 만들기
HTML 화면 파일이 들어갈 하위 폴더 만들기
my_chzzk_site 폴더 안의 빈 공간에 다시 마우스 우클릭 ➔ [새로 만들기(N)] ➔ **[폴더(F)]**를 클릭합니다.

폴더 이름을 소문자로 templates 라고 입력합니다.

templates 폴더 안으로 더블클릭해서 들어갑니다.

빈 공간에 마우스 우클릭 ➔ [새로 만들기(N)] ➔ **[텍스트 문서]**를 누릅니다.

이름 전체를 지우고 index.html 로 변경하고 Enter ➔ 경고창이 뜨면 **[예]**를 누릅니다.

index.html 파일을 우클릭 ➔ [연결 프로그램] ➔ **[메모장]**으로 엽니다.

이전에 안내해 드린 **index.html용 코드를 복사해서 붙여넣고 저장(Ctrl + S)**한 뒤 메모장을 닫습니다.

5
5. 터미널(명령 프롬프트) 실행 및 폴더 이동하기
주소창을 활용해 가장 쉽게 터미널 열기
상위 폴더인 my_chzzk_site 폴더로 돌아옵니다.

폴더 창 맨 위의 주소창(예: 내 PC > 바탕 화면 > my_chzzk_site 라고 적혀있는 길쭉한 흰색 창)을 클릭합니다.

글자가 파랗게 블록 지정되면, 그대로 cmd 라고 타이핑하고 Enter를 누릅니다.

그러면 해당 폴더 위치가 그대로 잡힌 까만색 명령 프롬프트(터미널) 창이 열립니다!

6
6. 라이브러리 설치 및 서버 시작하기
명령어 두 줄로 프로그램 실행
방금 열린 까만색 창에 순서대로 명령어를 입력하세요.

Flask 설치 (최초 1회만):

Bash
pip install flask
입력 후 Enter를 누르고 문자들이 마구 지나가며 완료될 때까지 잠시 기다립니다.

서버 실행:

Bash
python app.py
입력 후 Enter를 누릅니다.

실행에 성공하면 Running on [http://127.0.0.1:5000](http://127.0.0.1:5000) 문구가 뜹니다.

인터넷 웹 브라우저(크롬 등)를 열고 주소창에 [http://127.0.0.1:5000](http://127.0.0.1:5000) 을 치고 들어가면 사이트 완성입니다!

혹시 막히는 단계나 에러가 발생하는 번호가 있다면 말씀해 주세요! 어느 부분에서 막혔는지 알려주시면 바로 해결해 드릴게요.

다음으로 무엇을 도와드릴까요?

따라 하다가 에러/오류 메시지가 떴을 때 해결하기

VS Code 같은 전용 코딩 프로그램으로 편리하게 만드는 방법 알아보기
5번(명령 프롬프트 실행 및 폴더 이동하기)가 안돼

5번 단계에서 막히셨군요! 윈도우 환경이나 설정에 따라 상단 주소창을 이용하는 방식이 잘 안 될 때가 있습니다.

걱정하지 마세요. 가장 확실하게 5번(명령 프롬프트 열기)을 실행하는 2가지 대체 방법을 알려드릴게요! 편리한 쪽으로 골라서 시도해보세요.

🔥 방법 1. 폴더 안에서 Shift + 마우스 우클릭 (가장 쉬운 방법)
my_chzzk_site 폴더 안으로 들어갑니다.

키보드의 Shift 키를 누른 상태에서 폴더 내부의 빈 공간을 마우스 우클릭합니다.

평소와 다른 메뉴들이 나타나는데, 그중 아래 메뉴 중 하나를 클릭합니다:

[여기에 PowerShell 창 열기]

또는 [터미널에서 열기]

또는 [여기서 명령 창 열기]

파란색 또는 까만색 터미널 창이 바로 나타납니다!

💡 Tip: 파란색 PowerShell 창이 열려도 똑같이 pip install flask와 python app.py 명령어가 동일하게 작동하므로 그대로 진행하시면 됩니다!

📂 방법 2. [시작] 메뉴에서 '명령 프롬프트' 직접 열어서 이동하기
주소창이 반응하지 않을 때는 직접 경로를 타자 쳐서 이동하는 방법이 있습니다.

키보드의 Windows 키를 누르고 cmd라고 입력한 뒤 Enter를 눌러 [명령 프롬프트] 창을 엽니다.

열린 까만 창에 아래 명령어를 입력하고 Enter를 누릅니다:

DOS
cd Desktop\my_chzzk_site
(만약 폴더를 바탕화면에 만드셨다면 위 명령어로 한 번에 이동됩니다.)

창 좌측에 C:\...\Desktop\my_chzzk_site> 라고 표시되면 성공적으로 해당 폴더에 들어온 것입니다!

위 방법 중 하나로 창을 켜셨다면, 곧바로 6번 단계로 넘어가서 아래 명령어 2개를 순서대로 입력해 주시면 됩니다:

Bash
pip install flask
(설치 완료 후)

Bash
python app.py
어느 방법으로 진행하셨을 때 어떻게 나왔는지, 혹은 실행하다가 에러 메시지가 뜨는지 말씀해주시면 바로 이어서 해결해 드릴게요!

Bash

pip install flask 치면 이렇게 떠

보내주신 스크린샷을 보니 이유를 바로 알 수 있습니다!

이전에 안내해 드린 코드 상자의 맨 위에 적혀 있던 Bash라는 단어까지 같이 입력하셔서 생긴 문제입니다. Bash는 코드가 작성된 환경을 나타내는 표기일 뿐이며, 실제 명령어에는 포함되지 않습니다.

현재 화면에서 바로 실행하실 수 있도록 해결 방법을 알려드릴게요.

🔧 해결 방법 (순서대로 따라 하기)
현재 열려있는 PowerShell 창에서 Bash라는 단어는 빼고 아래 명령어만 그대로 입력해 주시면 됩니다.

먼저 아래 명령어를 입력하고 Enter를 누릅니다.

PowerShell
pip install flask
(설치가 완료될 때까지 잠시 기다려 주세요.)

설치가 끝나면, 스크린샷 맨 밑에 작성해 두셨던 명령어를 입력하고 Enter를 누릅니다.

PowerShell
python app.py
🌐 실행 확인
python app.py를 입력했을 때 Running on [http://127.0.0.1:5000](http://127.0.0.1:5000) 문구가 뜨면 성공입니다!

웹 브라우저(크롬 등)를 열고 주소창에 [http://127.0.0.1:5000](http://127.0.0.1:5000) 을 입력하면 방금 만드신 치지직 모니터링 사이트가 열립니다.

pip install flask 입력 후 혹시 또 다른 오류 메시지가 뜨거나 잘 안되시면 바로 말씀해 주세요!

주소가 안떠...

python app.py를 실행했을 때 주소([http://127.0.0.1:5000](http://127.0.0.1:5000))가 뜨지 않고 오류가 나거나 정지되는 원인은 크게 2가지입니다.

현재 터미널 창에 출력된 화면에 따라 아래 해결책을 적용해 보세요.

1. ModuleNotFoundError: No module named 'flask' 에러가 나는 경우
pip install flask 명령어가 제대로 완료되지 않았을 수 있습니다.

해결 방법:
터미널에 아래 명령어를 그대로 복사해서 붙여넣고 Enter를 누른 뒤, 설치가 끝날 때까지 기다려 보세요.

PowerShell
python -m pip install flask
설치가 완전히 완료되면 다시 python app.py를 입력해 보세요.

2. 아무 반응이 없거나 python 명령어 실행 시 윈도우 스토어가 열리는 경우
컴퓨터에 파이썬이 설치되어 있지 않거나 경로 설정이 안 되어 있을 때 발생합니다.

해결 방법:
python 대신 py 명령어로 실행해 보세요.

PowerShell
py app.py
💡 확인해 주실 부분
만약 위 방법으로도 안 되거나 화면에 붉은색 에러 메시지나 다른 문구가 떠 있다면, 터미널 창에 어떤 글자가 적혀 있는지 알려주시겠어요? 적혀 있는 메시지를 알려주시면 정확한 해결법을 찾아드릴게요!

이렇게 뜨는데 주소가 어디 있는 거야?

아! 보내주신 화면을 보니 원인을 바로 찾았습니다.

지금 app.py 파일 안에 웹 서버를 띄우는 Flask 코드 대신, 이전에 터미널 출력용으로 만든 일반 파이썬 코드가 들어있어서 터미널에 텍스트만 출력되고 종료된 상태입니다!

app.py 파일을 웹 서버용 코드로 바꿔주시면 바로 주소가 뜹니다.

🛠️ 해결 방법 (1분 완료)
my_chzzk_site 폴더 안에 있는 app.py 파일을 마우스 우클릭 ➔ [연결 프로그램] ➔ [메모장]으로 엽니다.

기존에 들어있던 내용을 모두 지우고, 아래의 Flask 웹 서버 코드를 그대로 복사해서 붙여넣은 뒤 저장(Ctrl + S)하고 메모장을 닫습니다.

Python
import json
import urllib.request
from flask import Flask, render_template

app = Flask(__name__)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

CHANNEL_IDS = [
    "b5ed5db484d04faf4d150aedd362f34b",
    "45e71a76e949e16a34764deb962f9d9f",
    "36ddb9bb4f17593b60f1b63cec86611d",
    "a6c4ddb09cdb160478996007bff35296",
    "4325b1d5bbc321fad3042306646e2e50",
    "b044e3a3b9259246bc92e863e7d3f3b8",
    "4515b179f86b67b4981e16190817c580",
    "64d76089fba26b180d9c9e48a32600d9",
    "8fd39bb8de623317de90654718638b10",
    "516937b5f85cbf2249ce31b0ad046b0f",
    "4d812b586ff63f8a2946e64fa860bbf5"
]

def get_data(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode('utf-8'))
    except:
        return None

@app.route('/')
def home():
    streamers = []
    for cid in CHANNEL_IDS:
        ch_info = get_data(f"https://api.chzzk.naver.com/service/v1/channels/{cid}")
        if not ch_info or not ch_info.get('content'):
            continue
        
        name = ch_info['content']['channelName']
        is_live = ch_info['content']['openLive']
        
        live_data = {}
        if is_live:
            detail = get_data(f"https://api.chzzk.naver.com/service/v2/channels/{cid}/live-detail")
            if detail and detail.get('content'):
                c = detail['content']
                live_data = {
                    'title': c.get('liveTitle', '제목 없음'),
                    'users': c.get('concurrentUserCount', 0),
                    'category': c.get('liveCategoryValue', '일반')
                }
        
        streamers.append({
            'id': cid,
            'name': name,
            'is_live': is_live,
            'live': live_data
        })
        
    return render_template('index.html', streamers=streamers)

if __name__ == '__main__':
    app.run(debug=True)
🚀 다시 실행하기
저장 후 열려있는 PowerShell 창에서 다시 실행해 보세요:

PowerShell
python app.py
이제 터미널 하단에 Running on [http://127.0.0.1:5000](http://127.0.0.1:5000) 이라는 주소가 나타날 거예요!
크롬 주소창에 [http://127.0.0.1:5000](http://127.0.0.1:5000) 을 입력하면 웹 화면으로 접속하실 수 있습니다.

cmd를 끄면 사이트가 사라지는데?

네, 맞습니다! 정상적인 동작입니다.

지금 실행하신 python app.py는 내 컴퓨터를 임시 웹 서버로 만들어주는 역할을 합니다. 따라서 명령 프롬프트(cmd나 PowerShell) 창을 끄면 서버 프로그램도 함께 종료되기 때문에 웹사이트 접속이 안 되게 됩니다.

💡 계속 켜두거나 다른 사람도 보게 하려면?
내 컴퓨터에서 계속 보려면

cmd(또는 PowerShell) 창을 끄지 말고 최소화해 두시면 됩니다.

cmd를 꺼도 항상 켜져 있고 다른 사람도 접속하게 하려면 (배포)

내 컴퓨터 대신 24시간 켜져 있는 외부 클라우드 서버에 이 코드를 올려두어야 합니다.

PythonAnywhere나 Render 같은 서비스를 이용하면 무료로 24시간 켜져 있는 웹사이트 주소(예: [https://내이름.pythonanywhere.com](https://내이름.pythonanywhere.com))를 만들 수 있습니다.

지금 만든 사이트를 24시간 켜져 있는 무료 웹사이트로 인터넷에 공개해보고 싶으시다면 언제든 말씀해 주세요! 방법도 차근차근 알려드릴게요.

24시간 켜져 있는 무료 웹사이트로 만들고 싶어

무료 클라우드 서버 서비스인 Render를 활용하면 내 컴퓨터(cmd)를 꺼도 24시간 언제나 접속 가능한 나만의 웹사이트 주소를 만들 수 있습니다.

웹사이트 공개를 위해 필요한 전체 진행 흐름입니다.

📋 준비물 & 전체 과정 (약 10분 소요)
GitHub(깃허브) 가입 및 코드 올리기: 작성한 파일들을 클라우드 저장소에 저장합니다.

Render(렌더) 가입 및 연결: GitHub에 올라간 코드를 받아서 24시간 대신 돌려줄 무료 서버를 만듭니다.

1단계: 프로젝트 폴더에 설정 파일 1개 추가하기
Render 서버가 이 프로그램을 어떻게 실행해야 하는지 알려주는 설정 파일이 하나 더 필요합니다.

my_chzzk_site 폴더 안에 마우스 우클릭 ➔ [새로 만들기] ➔ [텍스트 문서]를 만듭니다.

이름을 requirements.txt 로 바꾸고 메모장으로 엽니다.

메모장에 아래 두 줄을 적고 저장(Ctrl + S)합니다.

Plaintext
flask
gunicorn
2단계: GitHub에 내 코드 올리기
[GitHub 가입]: github.com에 접속해서 무료 회원가입을 진행합니다.

[저장소(Repository) 만들기]:

로그인 후 오른쪽 위의 + 버튼 ➔ New repository 클릭

Repository name에 my-chzzk-site 입력

Public 상태 그대로 두고 맨 아래 Create repository 버튼 클릭

[파일 업로드]:

화면 중앙의 uploading an existing file 링크를 클릭합니다.

내 컴퓨터의 my_chzzk_site 폴더 안에 있는 모든 파일과 폴더(app.py, requirements.txt, templates 폴더)를 드래그해서 올려줍니다.

맨 아래 Commit changes 초록색 버튼을 누르면 업로드가 완료됩니다.

3단계: Render에서 24시간 무료 웹사이트 만들기
[Render 가입]: render.com에 접속해서 Sign Up ➔ GitHub으로 로그인을 선택합니다.

[New Web Service 생성]:

대시보드에서 New + 버튼 ➔ Web Service 클릭

조금 전 만든 GitHub 저장소(my-chzzk-site) 옆의 Connect 버튼 클릭

[서버 설정 입력]:

Name: 원하는 사이트 이름 (예: my-chzzk-live)

Environment: Python 3 선택

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Instance Type: Free (무료 플랜) 선택

맨 아래 Create Web Service 버튼을 누릅니다!

🚀 배포 완료!
약 2~3분간 서버가 세팅된 후 화면 왼쪽 위에 [https://my-chzzk-live.onrender.com](https://my-chzzk-live.onrender.com) 형태의 무료 웹사이트 주소가 생깁니다.

이제 내 컴퓨터와 cmd 창을 꺼도, 스마트폰이나 다른 사람 컴퓨터에서 저 주소로 들어가면 언제든지 방금 만든 치지직 모니터링 사이트에 접속할 수 있습니다!

아까 만든 templates랑 app.py는 지워?

아니요, 절대 지우시면 안 됩니다! 🛑

app.py와 templates 폴더는 방금 만든 웹사이트의 핵심 몸통이자 원본 코드입니다. 지우지 않으셔야 하는 이유와 관리 팁을 알려드릴게요.

💡 지우면 안 되는 이유
GitHub 업로드용: 조금 전 안내해 드린 2단계에서 GitHub에 올릴 때 내 컴퓨터에 있는 이 파일들을 그대로 드래그해서 업로드해야 합니다.

코드 수정 및 업데이트: 나중에 새로운 스트리머를 추가하거나 화면 디자인을 바꿀 때, 내 컴퓨터에 있는 이 파일들을 수정해서 다시 확인해봐야 합니다.

📂 앞으로 파일 관리 팁
my_chzzk_site 폴더 전체를 잘 보관해 두세요.

나중에 코드를 수정할 때도 내 컴퓨터의 app.py나 index.html을 먼저 고친 뒤, 잘 작동하는지 python app.py로 테스트해보고, 그 파일 그대로 GitHub에 덮어씌워 올리시면 됩니다!

도움!!

Render 가입 직후 나오는 설문조사 화면이군요! 이 부분은 단순 참고용 질문(Optional)이라 아무거나 누르셔도 서비스 이용에 전혀 지장이 없습니다.

아래처럼 선택하시거나 넘어가시면 됩니다.

1. 선택 방법 (추천)
첫 번째 질문 (What are you looking to build with Render?):

Website / landing page 또는 Side project 클릭

두 번째 질문 (What capabilities matter most...?):

아무것도 누르지 않거나 Developer velocity 클릭

2. 그냥 넘어가기
선택지 오른쪽에 Optional(선택 사항)이라고 적혀 있으므로, 화면 오른쪽 아래나 상단에 Skip 또는 Continue(다음) 버튼이 있다면 바로 누르고 넘어가셔도 됩니다.

이 단계를 지나면 Render 메인 대시보드 화면이 나오는데, 거기서 New + 버튼 ➔ Web Service를 눌러 진행해주시면 됩니다! 막히는 부분이 생기면 언제든 말씀해 주세요.

connect가 어딨어?
아, 지금 계신 화면은 GitHub(깃허브) 페이지입니다! 파일 업로드를 아주 깔끔하게 완벽히 잘 마치셨네요. 👏

Connect 버튼은 GitHub이 아니라 Render 사이트에서 찾아야 합니다.

📍 Connect 버튼 찾는 방법
브라우저에서 새 탭을 열고 Render 사이트(dashboard.render.com) 로 들어갑니다.

메인 화면(대시보드) 오른쪽 위에 있는 New + 버튼 ➔ Web Service를 클릭합니다.

다음 화면으로 넘어가면 아래쪽에 방금 만드신 my-chzzk-site 목록이 보이고, 그 오른쪽 옆에 Connect 버튼이 나타납니다!

Render 화면으로 들어가서 New + ➔ Web Service 순서대로 눌러보시면 바로 찾으실 수 있습니다! 혹시 Render 화면에서 안 보이시면 다시 스크린샷 올려주세요.

없는데??

보내주신 스크린샷을 보니 Render 계정에 GitHub 권한 연결이 아직 안 되어 있어서 저장소가 안 보이는 상태입니다!

가장 쉬운 2가지 방법 중 하나로 해결할 수 있습니다. 방법 1이 훨씬 빠르고 쉽습니다.

🔥 방법 1. 주소 직접 복사해서 연결하기 (가장 쉬움)
GitHub 계정을 연동할 필요 없이 주소만 입력하면 바로 넘어갑니다.

화면 중앙 탭에서 Public Git Repository 탭을 클릭합니다.

입력창이 나타나면 아래 GitHub 주소를 복사해서 붙여넣습니다:

Plaintext
https://github.com/pastel1001/my-chzzk-site
오른쪽에 새로 생기는 Connect 버튼을 누릅니다!

📂 방법 2. GitHub 계정 권한 연결하기
현재 화면 중앙 하단에 보이는 검은색 GitHub 버튼을 클릭합니다.

팝업 창이 뜨면 GitHub 로그인 및 Authorize Render(권한 승인) 버튼을 누릅니다.

승인이 끝나면 화면 목록에 my-chzzk-site 저장소가 나타나고, 옆에 Connect 버튼이 생깁니다!

Connect 버튼을 누르면 다음 설정 화면으로 연결됩니다!

connect라고 안 뜸...

보내주신 스크린샷을 보니 pastel1001 / my-chzzk-site 저장소 항목을 찾으신 상태입니다!

그 화면에서 pastel1001 / my-chzzk-site 글씨가 있는 상자 전체(가운데 공간)를 직접 마우스로 클릭하시면 바로 다음 단계 설정 화면으로 넘어갑니다.

➔ 행동 요령
View repo 옆의 화살표가 아니라, pastel1001 / my-chzzk-site 회색 상자 아무 곳이나 클릭하세요!

클릭 후 화면이 바뀌면 아래 항목들을 순서대로 확인해서 입력해 주시면 배포가 시작됩니다:

Name: my-chzzk-site (원하는 이름 입력)

Language (또는 Environment): Python 3

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Instance Type: Free 선택

입력 후 맨 아래 Deploy Web Service (또는 Create Web Service) 버튼을 누르면 배포가 진행됩니다!

도움!!

아주 완벽하게 다 입력하셨습니다! 👍

지금 화면에 보이는 값들(StelCheck, Python 3, main, pip install -r requirements.txt, gunicorn app:app)이 모두 정확합니다.

🚀 마지막 단계 진행하기
화면을 아래로 조금 더 스크롤해 내려갑니다.

요금제 선택란에서 Free (무료) 플랜이 선택되어 있는지 확인합니다.

맨 아래에 있는 Deploy Web Service (또는 Create Web Service) 초록색/보라색 버튼을 누릅니다!

⏳ 배포 진행 중 화면
버튼을 누르면 까만 화면에 로그(진행 상황)가 쭉 뜨면서 약 2~3분간 배포 작업이 진행됩니다.

완료되면 화면 왼쪽 위에 [https://stelcheck.onrender.com](https://stelcheck.onrender.com) 형태의 초록색/파란색 웹사이트 주소가 생깁니다. 그 주소를 클릭하면 cmd나 컴퓨터를 꺼도 24시간 접속 가능한 나만의 웹사이트가 열립니다!

무료하니까 경고가 뜨는데?

걱정하지 않으셔도 됩니다! 결제 요구가 아니라 단순 안내 문구입니다.

💡 경고 문구의 의미
"Free instances spin down after periods of inactivity..."

의미: "사이트에 한동안 접속자가 없으면 서버가 잠깐 절전 모드(슬립 상태)에 들어갑니다. 다시 들어오면 서버가 깨어나느라 첫 로딩만 약 30초 정도 걸릴 수 있습니다."

돈이 나간다거나 결제가 필요한 경고가 전혀 아니니 안심하세요!

🚀 진행 방법
Free ($0/month) 박스가 지금처럼 보라색 테두리로 선택되어 있는지 확인합니다.

화면을 맨 아래로 내려서 Deploy Web Service (또는 Create Web Service) 초록색/보라색 버튼을 누르시면 끝납니다!

이거는?

이 부분도 입력할 필요 없이 그냥 넘어가시면 됩니다!

💡 Environment Variables (환경 변수) 란?
비밀번호나 비밀 API 키 같은 보안 정보를 저장할 때 쓰는 곳입니다. 지금 만드는 치지직 모니터링 사이트는 비밀키가 필요 없으므로 빈칸으로 두시면 됩니다.

🚀 바로 배포하기
NAME_OF_VARIABLE과 value 칸을 아무것도 적지 말고 그대로 비워두세요.

맨 아래 왼쪽의 흰색 Deploy Web Service 버튼을 누르시면 됩니다!

버튼을 누르면 까만 화면으로 바뀌면서 배포가 시작됩니다.

완성임?

거의 다 됐습니다! 마지막 10초 남았습니다! 🎉

화면 맨 아래를 보시면 ==> Build successful 🎉 메시지가 떠서 서버 설치는 완벽하게 성공했습니다. 지금은 최종적으로 사이트를 서버에 올리는 중(==> Deploying...)입니다.

🌐 접속 확인 방법
약 10~30초만 기다린 후, 화면 상단 좌측에 있는 주소 [https://stelcheck.onrender.com](https://stelcheck.onrender.com) 을 클릭해 보세요.

상단 배너 상태가 Building에서 Live(초록색)로 바뀌면 배포 완료입니다.

주소로 접속하셨을 때 만든 화면이 잘 출력되면 내 컴퓨터나 cmd를 완전히 꺼도 24시간 접속되는 웹사이트가 완성된 것입니다! 고생 많으셨습니다!

끝??

네, 배포가 완벽하게 완료되었습니다! 🎉

상단 배너에 초록색 Live 표시와 터미널 로그의 ==> Your service is live 🚀 문구가 웹사이트 배포 성공을 보여줍니다.

🌐 배포 완료 확인 및 사용 방법
웹사이트 주소: 상단 및 로그에 표시된 [https://stelcheck.onrender.com](https://stelcheck.onrender.com) 링크를 클릭하거나 브라우저 주소창에 입력하시면 됩니다.

배포 상태: 이제 내 컴퓨터와 PowerShell/cmd 창을 모두 꺼도, 스마트폰이나 다른 컴퓨터에서 해당 주소로 24시간 언제든지 접속하실 수 있습니다.

사이트가 잘 열리는지 확인해 보시고, 추가로 수정하고 싶은 부분이 있다면 말씀

끝??

네, 축하합니다! 완벽하게 끝났습니다! 🎉

화면에 초록색 Live 표시와 함께 ==> Your service is live 🚀 문구가 떴네요. 배포 성공입니다!

🌐 나만의 24시간 웹사이트 주소
[https://stelcheck.onrender.com](https://stelcheck.onrender.com)

이제 컴퓨터나 cmd 창을 완전히 끄셔도 스마트폰이나 다른 컴퓨터에서 위 주소로 들어가면 언제든지 방금 만든 사이트에 접속할 수 있습니다. 정말 고생 많으셨어요!

무료라 그런가 로딩 진짜 기네

맞아요, 처음 들어갈 때 로딩이 꽤 답답하게 느껴지셨죠!

무료 플랜 특성상 약 15분 동안 새로운 접속자가 없으면 서버가 자동으로 절전 모드(Sleep)로 들어가기 때문입니다. 절전 모드 상태에서 누군가 접속하면 서버가 깨어나는 데 약 30초~1분 정도 시간이 걸립니다. (한 번 깨어난 뒤에는 다시 클릭할 때마다 바로바로 빠르게 뜹니다!)

이 답답함을 줄일 수 있는 대표적인 팁 2가지를 소개해 드립니다.

1. 무료 자동 깨움 서비스 이용하기 (추천)
서버가 잠들지 않도록 5~10분마다 자동으로 사이트에 신호를 보내주는 무료 서비스를 등록하는 방법입니다.

UptimeRobot 같은 무료 모니터링 사이트에 가입합니다.

내 웹사이트 주소([https://stelcheck.onrender.com](https://stelcheck.onrender.com))를 등록하고 5분 간격 주기(Check Interval)로 설정해 둡니다.

서비스가 주기적으로 핑을 보내주어 서버가 절전 모드로 들어가는 것을 막아줍니다.

2. 로딩 화면(스피너) 추가하기
서버가 데이터를 가져오는 동안 흰 화면만 보이면 멈춘 것처럼 보일 수 있습니다. HTML/CSS에 간단한 "로딩 중..." 애니메이션을 더해두면 훨씬 쾌적한 느낌을 줍니다.

필요하시다면 자동 깨움 서비스 설정 방법이나 로딩 애니메이션 코드 추가도 언제든 알려드릴 테니 말씀해 주세요!

음... 조졌는데?

아이고, 코드가 줄바꿈과 들여쓰기가 전부 사라져서 한 줄로 뭉개져 버렸네요! 파이썬은 들여쓰기가 필수인 언어라 이 상태로는 실행하면 문법 에러(SyntaxError)가 납니다.

복사/붙여넣기 과정이나 메모장 저장 형태 때문에 발생한 일이니 걱정하지 마세요. 바로 깔끔하게 정돈된 원본 코드로 복구해 드리겠습니다.

🛠️ 올바른 app.py 코드
app.py 파일의 내용을 전부 지우고 아래 코드를 그대로 복사해서 붙여넣은 뒤 저장(Ctrl + S)해 주세요.

Python
import json
import urllib.request
from flask import Flask, render_template

app = Flask(__name__)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

CHANNEL_IDS = [
    "b5ed5db484d04faf4d150aedd362f34b",
    "45e71a76e949e16a34764deb962f9d9f",
    "36ddb9bb4f17593b60f1b63cec86611d",
    "a6c4ddb09cdb160478996007bff35296",
    "4325b1d5bbc321fad3042306646e2e50",
    "b044e3a3b9259246bc92e863e7d3f3b8",
    "4515b179f86b67b4981e16190817c580",
    "64d76089fba26b180d9c9e48a32600d9",
    "8fd39bb8de623317de90654718638b10",
    "516937b5f85cbf2249ce31b0ad046b0f",
    "4d812b586ff63f8a2946e64fa860bbf5"
]

def get_data(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode('utf-8'))
    except:
        return None

@app.route('/')
def home():
    streamers = []
    for cid in CHANNEL_IDS:
        ch_info = get_data(f"https://api.chzzk.naver.com/service/v1/channels/{cid}")
        if not ch_info or not ch_info.get('content'):
            continue
        
        name = ch_info['content']['channelName']
        is_live = ch_info['content']['openLive']
        
        live_data = {}
        if is_live:
            detail = get_data(f"https://api.chzzk.naver.com/service/v2/channels/{cid}/live-detail")
            if detail and detail.get('content'):
                c = detail['content']
                live_data = {
                    'title': c.get('liveTitle', '제목 없음'),
                    'users': c.get('concurrentUserCount', 0),
                    'category': c.get('liveCategoryValue', '일반')
                }
        
        streamers.append({
            'id': cid,
            'name': name,
            'is_live': is_live,
            'live': live_data
        })
        
    return render_template('index.html', streamers=streamers)

if __name__ == '__main__':
    app.run(debug=True)