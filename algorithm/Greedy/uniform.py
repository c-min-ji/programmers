def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
            
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    
    len_lost = len(lost)
    answer = n - len_lost
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer += 1

    return answer
