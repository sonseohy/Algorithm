# 프렌즈 4블록

def solution(m, n, board):
    # 입력은 문자열 리스트이므로 값을 바꿀 수 있도록 2차원 리스트로 변환
    board = [list(row) for row in board]
    # 지금까지 지워진 블록의 총 개수
    answer = 0

    while True:
        # 1) 이번 턴에 지울 칸을 모두 찾아서 표시
        # 같은 칸이 여러 2x2에 겹칠 수 있으므로 중복을 막기 위해 집합 사용
        marked = set()
        for r in range(m - 1):          # 2x2의 왼쪽 위 행 (아래 행 r+1이 있어야 하므로 m-1까지)
            for c in range(n - 1):      # 2x2의 왼쪽 위 열 (오른쪽 열 c+1이 있어야 하므로 n-1까지)
                num = board[r][c]       # 기준 칸의 값
                # 빈칸이 아니고, 2x2의 네 칸이 모두 같은 블록이면 표시
                if num != '-' and num == board[r][c+1] == board[r+1][c] == board[r+1][c+1]:
                    # update는 리스트 안의 원소를 각각 넣고, add는 인자 하나만 넣을 수 있음
                    marked.update([(r, c), (r, c+1), (r+1, c), (r+1, c+1)])

        # 2) 표시된 칸이 없으면 더 지울 것이 없으므로 반복 종료
        if not marked:
            break

        # 3) 표시된 블록 지우기
        # 이번 턴에 지워지는 블록 수(집합 크기)를 누적
        answer += len(marked)
        # 표시된 모든 칸을 빈칸('-')으로 변경
        for r, c in marked:
            board[r][c] = '-'

        # 4) 열마다 중력 적용 (두 포인터 방식으로 블록을 아래로 옮기기)
        for c in range(n):
            w = m - 1                   # 다음 블록을 놓을 행 번호 (맨 아래부터 시작)
            # 아래에서 위로 훑으면서 살아 있는 블록을 발견하면
            for r in range(m - 1, -1, -1):
                if board[r][c] != '-':
                    # 그 블록을 w행으로 옮기고 (자기 자리일 수도 있음)
                    board[w][c] = board[r][c]
                    # 다음 블록은 한 칸 위에 놓아야 하므로 w를 위로 이동
                    w -= 1
            # 블록을 모두 옮긴 뒤, 위쪽에 남은 칸(0~w행)은 빈칸으로 채움
            while w >= 0:
                board[w][c] = '-'
                w -= 1

    # 모든 턴이 끝난 후 총 지워진 블록 수 반환
    return answer