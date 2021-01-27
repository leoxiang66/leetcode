#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <iomanip>
#define getIndexIn1D(i,j,width) (i)*(width)+(j)
using namespace std;


class UnionFind{
    public:
    int* parents;
    UnionFind(int size){
        parents = new int[size];
        for (size_t i = 0; i < size; i++)
        {
            parents[i] = i;

        }
    }
    int getRoot(int index){
        int x = this->parents[index];
        int tmp = index;
        while (x != tmp)
        {
            tmp = x;
            x = this->parents[x];
        }
        return x;
        
    }

    void union_(int index1, int index2){
        int root1 = this->getRoot(index1);
        int root2 = this->getRoot(index2);
        this->parents[root2] = root1;
        
    }

    int getNumOfClasses(){
        set<int> set1;
        for (size_t i = 0; i < sizeof(this->parents)/sizeof(int); i++)
        {
            set1.insert(this->parents[i]);
        }
        return set1.size()-1;
    }

};



float func(int m, int n, int s, string lines[]){
    UnionFind uf(m*n);
    for (size_t i = 0; i < m; i++)
    {
        for (size_t j = 0; j < n; j++)
        {
            char elem = lines[i][j];
            int index = getIndexIn1D(i,j,n);
            if (elem == 'X')
            {
                if (j+1 < n && lines[i][j+1] == 'X'){
                    uf.union_(index,index+1);
                }

                if(i+1 < m && lines[i+1][j] == 'X'){
                    uf.union_(index,index+n);
                }
            }
            else{
                uf.parents[index] = -1;
            }
            
        }
        
    }

    vector<int> res;
    for (size_t i = 0; i < m-s+1; i++)
    {
        for (size_t j = 0; j < n-s+1 ; j++)
        {
            set<int> cls;
            for (size_t deltaI = 0; deltaI < s; deltaI++)
            {
                for (size_t deltaJ = 0; deltaJ < s; deltaJ++)
                {
                    int index = getIndexIn1D(i+deltaI,j+deltaJ,n);
                    if(uf.parents[index] != -1){
                        cls.insert(uf.parents[index]);
                    }
                }
                
            }

            
            res.push_back(cls.size());
            
        }
        
    }


    
    

    int sum = 0;
    for (auto &&i : res)
    {
        sum += i;
    }

    double ret =(double)sum/res.size();

    return ret;

    



    
    
    
}



int main() {

    int m, n, s;
    cin >> m;
    cin >> n;
    cin >> s;
    getchar();
    string lines[m];
    for (size_t i = 0; i < m; i++)
    {
        
        getline(cin,lines[i]);

    }
    
    
    double ret = func(m,n,s,lines);

    std::cout << std::fixed;
    std::cout << std::setprecision(6);
    std::cout << ret<<endl;	
}

