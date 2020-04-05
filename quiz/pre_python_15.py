"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""

residentNumber = input('주민등록번호 : ')
splitString = residentNumber.split('-')

if splitString[1][0:1] == '1' or splitString[1][0:1] == '3':
    print('남자')

elif splitString[1][0:1] == '2' or splitString[1][0:1] == '4':
    print('여자')

else:
    print('입력오류')

