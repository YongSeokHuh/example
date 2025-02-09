def solution(num_list):
    if num_list[-1] > num_list[-2]:  # 마지막 원소가 그 전 원소보다 크면
        return num_list + [num_list[-1] - num_list[-2]]  # 마지막 원소에서 그 전 원소를 뺀 값을 추가
    else:  # 그렇지 않으면 마지막 원소를 두 배한 값을 추가
        return num_list + [num_list[-1] * 2]