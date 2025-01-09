# 암호 만들기
# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다.
# 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측됨.
# 새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다.
# C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성
def code(n):
    if n == L:
        vowel = 0   # 암호의 모음 수
        consonant = 0   # 암호의 자음 수
        str = ''
        for c in pw:
            if c in ['a', 'e', 'i', 'o', 'u']:
                vowel += 1
            else:
                consonant += 1
            str += c
        # 최소 한 개의 모음과 두 개의 자음이 포함 되었을때만 최종 result에 append
        if vowel > 0 and consonant > 1:
            result.append(str)
        return

    for c in char:
        # 중복된 문자가 pw 리스트에 들어가지 않도록록
        if c not in pw:
            # 알파벳이 증가하는순서대로 배열되어야 하므로 가장 끝 암호 문자의 아스키 코드 값이이 현재 문자보다 크면 append 제외
            if len(pw) and ord(pw[-1]) > ord(c):
                continue
            pw.append(c)
            code(n + 1)
            pw.pop()

L, C = map(int, input().split())
char = list(input().split())

pw = [] # 예상 암호 저장할 리스트
result = [] # 가능성 있는 모든 암호들 저장할 리스트

code(0)
# 사전식으로 가능성 있는 암호를 출력하기 위해 정렬렬
result.sort()

for r in result:
    print(r)
