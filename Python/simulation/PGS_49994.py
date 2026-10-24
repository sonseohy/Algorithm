# 방문 길이

def solution(dirs):
    # 지나간 길을 저장하는 set
    # 각 원소는 ((x1, y1), (x2, y2)) 형태의 튜플 = 길 하나
    visited = set()

    # 현재 위치 (시작은 원점 (0, 0))
    r, c = 0, 0

    # 명령어별 좌표 변화량 (행 변화, 열 변화)
    moves = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}

    for d in dirs:
        # 이동한 뒤의 좌표 계산
        nr, nc = r + d[d][0], c + d[d][1]

        # 다음 좌표가 좌표평면(-5 ~ 5)을 벗어나면 이 명령은 무시
        if -5 <= nr <= 5 and -5 <= nc <= 5:
            # 길 표시
            # 시작점과 도착점을 정렬해서 방향을 없앰 (A→B와 B→A를 같은 길로 취급)
            # sorted는 리스트를 반환하므로 tuple로 바꿔서 set에 넣을 수 있게 함
            edge = tuple(sorted([(r, c), (nr, nc)]))

            # 같은 길이면 set에 이미 있으므로 중복 저장되지 않음
            visited.add(edge)

            # 실제로 이동
            r, c = nr, nc

    # 지나간 서로 다른 길의 개수 = 답
    return len(visited)
