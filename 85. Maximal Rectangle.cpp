/*Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。*/
////////////////////// Dynamic Programming//////////////////////////////////////
/*
heights[i][j]代表[i，j]的高度
heights[i][j] = matrix[i][j]=='1'? heights[i-1][j] + 1:0

dp[i][j][k] 代表以[i,j]为右下角，高度为k可以组成的面积
dp[i][j][k] = matrix[i][j]=='1'? dp[i][j-1][k] + k : 0

作者：leeyupeng
链接：https://leetcode-cn.com/problems/maximal-rectangle/solution/dong-tai-gui-hua-by-leeyupeng-5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/

class Solution {
public:
	int maximalRectangle(vector<vector<char>>& matrix) {
		int n = matrix.size();
		int m = 0;
		if (n > 0) { m = matrix[0].size(); }
		vector<vector<int>> heights(n + 1,vector<int>(m + 1,0));
		vector<vector<vector<int>>> dp(n + 1,vector<vector<int>>(m + 1, vector<int>(n + 1, 0)));
		int ans = 0;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (matrix[i-1][j-1] == '0') { continue; }
				heights[i][j] = heights[i-1][j] + 1;
				for (int k = 1; k <= heights[i][j]; k++) {
					dp[i][j][k] = dp[i][j-1][k] + k;
					ans = max(ans, dp[i][j][k]);
				}
			}
		}
		return ans;
	}
};
