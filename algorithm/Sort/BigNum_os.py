#https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = list(map(str, numbers)) #numbers를 문자열로 변경
    numbers.sort(key=lambda x: x*3, reverse=True) #number하나하나를 3자리로 늘려서 비교
    return str(int(''.join(numbers))) #0일수도있어서 int로 변환한다음 다시 str로
