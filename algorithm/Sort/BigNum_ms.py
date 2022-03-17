#https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    arr = [] #수의 범위가 1<= num <= 1000 까지여서 4자리 수까지 늘린 수와 원래 길이를 저장하여는 리스트
    for i in numbers:
        a = (str(i)*4)[:4] #길이가 1이상이면 *4를 했을 때 4자리가 넘어가기때문에 0~3까지만 넣어줌
        arr.append((a,len(str(i)))) #4자리로 늘린 문자열과 원래 길이를 저장

    arr.sort(key= lambda x:x, reverse=True) #해당 리스트를 역순 정렬
    
    s = 0 #총 합이 0일 때를 찾기위해 변수 설정
    for (a, length) in arr: 
        s += int(a) #a를 다 더해서
        if s == 0: #0일 때 색출
            return '0'
        answer += a[:length] #원래 길이만큼 answer 문자열에 추가
    return answer
