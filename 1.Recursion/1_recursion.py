def recursive(n):
    # 재귀함수 : 자기 자신을 호출
    if n <= 0:
        # 종료 조건
        return
    print('hello')
    recursive(n-1)


recursive(10)
