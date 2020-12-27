int64_t pre[100005];
int64_t preidx[100005];
int64_t idx[100005];
class Solution {
public:
    int minMoves(vector<int>& nums, int k) {
        int n=nums.size();
        memset(idx,0,sizeof(idx));

        for(int i=0;i<n;i++){
            pre[i+1]=pre[i];
            if(nums[i]==0) {
                idx[i] = i;
                pre[i + 1] += 1;
            }
        }
        for(int i=0;i<n;i++){
            preidx[i+1]=preidx[i]+idx[i];
        }
        vector<int> onepos;
        for(int i=0;i<n;i++){
            if(nums[i]==1)
                onepos.push_back(i);
        }
        int midpos=k/2;
        int l=onepos[0],r=onepos[0],sum=1;
        int64_t ret=INT64_MAX;
        while(r<n){
            while(r<n&&sum<k){
                r++;
                if(r==n)
                    break;
                sum+=nums[r];
            }
            if(r==n)
                break;
            if(midpos>=onepos.size())
                break;
            int64_t mid=onepos[midpos];
            int64_t before = pre[mid + 1] - pre[l], after = pre[r + 1] - pre[mid + 1];
            int64_t targetbefore = caclbefore(l, before), targetafter = caclafter(r, after);
            int64_t realbefore = preidx[mid + 1] - preidx[l], realafter = preidx[r + 1] - preidx[mid + 1];
            ret = min(ret, realbefore - targetbefore + targetafter - realafter);
            while(sum==k){
                sum-=nums[l++];
            }
            midpos++;
        }
        return ret;
    }
    int64_t caclbefore(int64_t start,int64_t num){
        return (start+start+num-1)*num/2;
    }
    int64_t caclafter(int64_t end,int64_t num){
        return (end-num+1+end)*num/2;
    }
};
/*
作者：jklp2
链接：https://leetcode-cn.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/solution/qiu-jiang-0yi-dong-dao-liang-ce-de-zui-x-evee/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/