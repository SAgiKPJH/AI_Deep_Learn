todo = ["Wake Up", "Sleeping"]

while True :
    code = input("""
                 
할 일 목록 관리자
1. 할 일 추가
2. 할 일 삭제
3. 할 일 목록 보기
4. 종료
선택 : """)
    
    if code == "1":
        create = input("추가할 할 일 : ")
        todo.append(create)
        continue
    elif code == "2":
        delete = input("삭제할 할 일 : ")
        if (delete not in todo) :
            print("존재하지 않는 할 일입니다.")
            pass
        todo.remove(delete)
    elif code == "3":
        print(todo)
    elif code == "4":
        break
    else :
        print("존재하지 않는 명령입니다.")