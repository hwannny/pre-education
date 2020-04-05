"""7. 1부터 100까지 수의 합을 계산하고 있다. 
이 때 합이 최초로 1000을 넘게 하는 수가 무엇인지 코드를 만들고 답을 구하시오


<출력>
 45
"""
# 기준 수
baseNumber = 1000
sumNumber = 0

for i in range(1, 101):
    sumNumber = sumNumber + i
    if sumNumber > 1000:
        num = i
        break

print(num)