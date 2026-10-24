# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0                 # 터뜨려서 사라진 인형 개수
    stack = []                 # 바구니 (뽑은 인형을 쌓는 스택)

    for m in moves:            # 크레인이 움직이는 열 번호를 하나씩 확인
        for row in range(len(board)):           # 위(0행)부터 아래로 탐색
            doll = board[row][m - 1]            # 문제의 열 번호는 1부터 시작하므로 m - 1 사용
            if doll != 0:                       # 인형을 찾았으면
                board[row][m - 1] = 0           # 그 칸을 비움 (인형을 집어 올림)

                # 바구니 맨 위 인형과 같으면 두 개가 터짐
                if stack and stack[-1] == doll:
                    stack.pop()                 # 바구니 맨 위 인형 제거
                    answer += 2                 # 터진 인형 2개 추가
                else:
                    stack.append(doll)          # 같지 않으면 바구니에 쌓음

                break                           # 이 열에서 인형 하나를 뽑았으므로 다음 move로 이동
                                                # 인형이 없는 열(0만 있음)이면 아무 일도 없이 다음 move로

    return answer