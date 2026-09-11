// 수의 계절은 (Easy) - 코드트리 Trail1 Chapter4 Lesson11
// 몇 월인지(M)를 입력받아 어떤 계절인지 출력한다.
// 3~5월: Spring, 6~8월: Summer, 9~11월: Fall, 12~2월: Winter
// 제한 조건: 1 <= M <= 12

#include <iostream>

using namespace std;

int main() {
    // 변수 선언
    int m;

    // 입력
    cin >> m;
    
    // 출력
    if (m >= 12 || m <= 2)
        cout << "Winter" << endl;
    else if (m <= 5)
        cout << "Spring" << endl;
    else if (m <= 8)
        cout << "Summer" << endl;
    else
        cout << "Fall" << endl;
    
    return 0;
}
