n = 10
result = 1
for i in range(1, n + 1) :
    result = result  * i
print(f"{n}! = {result}")

reportCard = {"Tomas": 100, "Tom" : 10}

def GetScore(score = 0) :
    if score >= 90 :
        return "A"
    elif score >= 80 :
        return "B"
    elif score >= 70 :
        return "C"
    elif score >= 60 :
        return "D"
    else :
        return "F"


while True :
    try:
        code = input("""
                 
성적 관리 프로그램
1. 성적 입력
2. 학생 조회
3. 학점 조회
4. 종료
선택 : """)
    
        if code == "1":
            create = input("이름 : ")
            score = input("성적 : ")
            reportCard.update(create, score)
            pass
        elif code == "2":
            for name in reportCard.keys() :
                print(name)
        elif code == "3":
            name = input("조회할 학생 : ")
            if name not in reportCard.keys() :
                print("학생을 조회할 수 없습니다.")
                continue
            score = reportCard.get(name)
            print(f"{name} 학생의 학점은 {GetScore(score)} 입니다.")
        elif code == "4":
            break
        else :
            print("존재하지 않는 명령입니다.")

    except KeyboardInterrupt:
        print("종료합니다.")
        break
    except:
        print("알 수 없는 에러가 발생했습니다.")
        break
    else:
        print("다시 반복합니다.")
    finally:
        print("명령 수행 완료.")
