# 자동차의 주행거리 == N킬로미터 
# N보다 크면서, 가장 작은 수로 늘려놓기
# 조작한 값은 서로 다른 K개의 숫자로 이루어짐 1000은 1과 0, 2개의 숫자
# N과 K를 줬을 때 조작할 수 있는 주행거리의 최솟값
import sys

def is_vaild_number(number, K):
    """
    입력 받은 숫자가 서로 다른 K개의 숫자인지 확인
    """
    return len(set(str(number))) == K

def find_distance_driven(N, K):
    """ 
    N보다 크면서 
    서로 다른 K개의 숫자로 이루어진 가장 작은 수 찾기
    """
    target_number = N + 1
    while not is_vaild_number(target_number, K):
        target_number += 1
    return target_number

input = sys.stdin.read
N, K = map(int, input().split())
result = find_distance_driven(N,K)
print(result)


    """
        /* 코드가 실행되는 중입니다... */
채점을 시작합니다...
================================
Case 1. 테스트를 통과했습니다! (+4)
Case 2. 실행 시간을 초과했습니다. (+0)
Case 3. 테스트를 통과했습니다! (+4)
Case 4. 테스트를 통과했습니다! (+4)
Case 5. 테스트를 통과했습니다! (+4)
Case 6. 테스트를 통과했습니다! (+4)
Case 7. 테스트를 통과했습니다! (+4)
Case 8. 테스트를 통과했습니다! (+4)
Case 9. 테스트를 통과했습니다! (+4)
Case 10. 테스트를 통과했습니다! (+4)
Case 11. 테스트를 통과했습니다! (+4)
Case 12. 테스트를 통과했습니다! (+4)
Case 13. 실행 시간을 초과했습니다. (+0)
Case 14. 테스트를 통과했습니다! (+4)
Case 15. 실행 시간을 초과했습니다. (+0)
Case 16. 테스트를 통과했습니다! (+4)
Case 17. 테스트를 통과했습니다! (+4)
Case 18. 테스트를 통과했습니다! (+4)
Case 19. 테스트를 통과했습니다! (+4)
Case 20. 실행 시간을 초과했습니다. (+0)
Case 21. 실행 시간을 초과했습니다. (+0)
Case 22. 테스트를 통과했습니다! (+4)
Case 23. 테스트를 통과했습니다! (+4)
Case 24. 테스트를 통과했습니다! (+4)
Case 25. 테스트를 통과했습니다! (+4)
================================
채점을 마쳤습니다.
총 점수: 80 / 100

/* 코드 실행이 완료되었습니다! */

    """