class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle = {};

        for(int a = 0; a < numRows; a++){
            if(a < 2){
                vector<int> temp = {};
                while(temp.size() < a+1){
                    temp.push_back(1);
                }
                triangle.push_back(temp);
            }

            else{
                vector<int> temp = {1};
                for(int b = 1; b < a; b++){
                    temp.push_back(triangle[a-1][b-1] + triangle[a-1][b]);
                }
                temp.push_back(1);
                triangle.push_back(temp);
            }
        }

        return triangle;
    }
};