#include<iostream>
#include<vector>
#include<map>
using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

void inorderTraversal(TreeNode* node, vector<int>& nodes) {
    if (node == nullptr) {
        return;
    }

    inorderTraversal(node->left, nodes);
    // std::cout << node->val << std::endl;
    if (node != nullptr) {
        nodes.push_back(node->val);
    }

    inorderTraversal(node->right, nodes);
}

class Solution {
public:
    vector<int> findMode(TreeNode* node) {
        vector<int> nodes, ans;
        map<int, int> mymap;
        inorderTraversal(node, nodes);

        for (int i = 0; i < nodes.size(); i++){
            mymap[nodes[i]]++;
        }

        int max = mymap[nodes[0]];
        for (const auto& pair : mymap){
            if (pair.second > max){
                max = pair.second;
            }
        }

        for (const auto& pair : mymap){
            if (pair.second == max){
                ans.push_back(pair.first);
            }
        }
        

        return ans;

    }
};



int main() {

    Solution s;
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(2);

    vector<int> ans = s.findMode(root);

    for (int c : ans){
        cout << c << endl;
    }

    // Don't forget to delete the nodes to avoid memory leak
    // delete root->right->left;
    // delete root->right;
    // delete root;

    return 0;
}

