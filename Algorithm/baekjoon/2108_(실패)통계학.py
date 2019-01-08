#여기에 코드를 작성하세요.

korean = int(input("국어 점수를 입력하세요."))
english = int(input("영어 점수를 입력하세요."))
math = int(input("수학 점수를 입력하세요."))
science = int(input("과학 점수를 입력하세요."))

if(0>korean or 0>english or 0>math or 0>science or korean>100 or english>100 or math>100 or science>100):
    print('잘못된 점수')

else:
    sum1 = korean + english + math + science
    avg1 = sum1/4
    
    if(avg1>=80):
        print('합격') 
    else:
        print('불합격')
