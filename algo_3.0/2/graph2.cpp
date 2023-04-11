#include <map>
#include <iostream>
#include <set>
#include <vector>

void dfs()

int main() {
    int V, E, c = 0;
    std::cin >> V >> E;
    std::map<int, int> res;
    for (int i = 0; i < E; i++) {
        int v1, v2;
        std::cin >> v1 >> v2;
        if (res.find(v1) != res.end()) {
            if (res.find(v2) == res.end()) {
                res[v2] = res[v1];
            }
            else {  
                if (res[v1] != res[v2]) {
                    int a = res[v2];
                    for (auto& x: res) {
                        if (x.second == a) {
                            x.second = res[v1];
                        }
                    }
                }
            }
        }
        else {
            if (res.find(v2) != res.end()) {
                res[v1] = res[v2];
            }
            else {
                c++;
                res[v2] = c;
                res[v1] = c;
            }
        }
    }
    for (int i = 1; i < V+1; i++) {
        if (res.find(i) == res.end()) {
            c++;
            res[i] = c;
        }
    }
    std::map<int, std::vector<int>> answer;
    for (auto& x: res) {
        answer[x.second].push_back(x.first);
    }
    std::cout << answer.size() << std::endl;
    for (auto& x: answer) {
        std::cout << x.second.size() << std::endl;
        for (int& i: x.second) {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}