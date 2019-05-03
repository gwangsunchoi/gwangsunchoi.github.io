str = "멋쟁이 사자처럼"
str2 = "dms 좋은 동아리 입니다."

#print(str[0], str[1]) 
#print(str[1:4])

# 문자열의 길이 : len(문자열 함수)
# print(len(str))

#특정문자 등장 횟수 : 문자열변수.count('특정문자')
#print(str.count('사'))

#문자열 (특정 기준으로) 나누기 : 문자열 변수.split()
#print(str.split()) 실행하면 공백 기준으로 결과 출력 ['멋쟁이', '사자처럼']

# 특정 문자 인덱스 찾기 : find('문자'), index('문자')
print(str.index('사'))