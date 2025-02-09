def solution(num_list):
    total = 0    
    goap = 1
    length = len(num_list)
    if length >= 11:
        for j in range(length):
            total += num_list[j]
        answer = total
    elif total <= 10:
        for i in range(length):
            goap *= num_list[i]
        answer = goap
    return answer
    
  