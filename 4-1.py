while True:
    i=int(input("첫번째 숫자를 입력하세요"))
    
    j=str(input("사칙연산 기호를 입력하세요(+,-,/,*) [c: 재입력, e: 계산기 종료]"))
    
    k=int(input("두번째 숫자를 입력하세요"))

    if j == "+":
        print(i+k)
        
    elif j == "-":
        print(i-k)
        
    elif j== "/":
        print(i/k)
       
    elif j == "*":
        print(i*k)

    elif j=="e":
        break
    
    elif j=="c":
        print("재입력")

    else:
        print("다시 입력하세요")

   

'''
숫자 연산자 숫자 입력받고 결과값 출력ㅇ
c 재입력  e 계산기 종료
숫자나 연산자 잘못 입력시 다시 입력ㅇ
input 함수 3번만 사용ㅇ
종료 선언 전까지 계산기가 끝나면 안 됨
'''
