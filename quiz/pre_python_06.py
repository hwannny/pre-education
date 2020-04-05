"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★

예시
<입력>
숫자를 입력하세요 : 4

<출력>
    ★
   ★★
  ★★★
 ★★★★
  ★★★
   ★★
    ★


"""

number = int(input('숫자를 입력하세요 : '))

# 증가 출력
for j in range(1, number+1):
    for i in range(number):
        if i < number-j:
            print(' ', end='')
        else:
            print('★', end='')
    print()

# 감소 출력
for j in range(number-1, 0, -1):
    for i in range(number):
        if i < number-j:
            print(' ', end='')
        else:
            print('★', end='')
    print()


