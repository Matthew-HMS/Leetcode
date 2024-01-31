#include<iostream>
#include<vector>
using namespace std;

class MyHashMap {
public:
  
    int data[1000001];
    MyHashMap() {
        fill(data, data+1000000, -1);
    }
    
    void put(int key, int value) {
        data[key] = value;
    }
    
    int get(int key) {
        return data[key];
    }
    
    void remove(int key) {
        data[key] = -1;
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