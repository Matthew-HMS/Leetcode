#include<iostream>
#include<vector>
using namespace std;

class MyHashMap {
public:
  
    vector<int> ans = {};
    vector<vector<int>> map = {};
    int map_length = 0;
    MyHashMap() {
        return ans;
    }
    
    void put(int key, int value) {
        for (int i=0; i<map.size(); i++){
            if (map[i][0] == key){
                map[i][1] = value;
                ans.push_back(NULL);
                return;
            }
        }
        vector<int> temp = {key, value};
        map.push_back(temp);
        ans.push_back(NULL);
    }
    
    int get(int key) {
        if (map.size() < key+1){
            ans.push_back(-1);
            return -1;
        }
        else {
            ans.push_back(1);
            return 1;
        }
    }
    
    void remove(int key) {
        if (map.size() < key+1){
            ans.push_back(-1);
            return;
        }
        else ans.push_back(NULL);
    }
};

int main(){
    // vector<string> function = {"MyHashMap","put","put","get","get","put","get","remove","get"};
    // vector<vector<int>> nums = {{},{1,1},{2,2},{1},{3},{2,1},{2},{2},{2}};
    MyHashMap* obj = new MyHashMap();

    obj->put(1,1);
    int get1 = obj->get(1);
    obj->remove(1);

    cout << get1 << endl;

    return 0;
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */