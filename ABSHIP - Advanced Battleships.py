'''You managed to beat your friend in Battleships and take his Internet Points! Perfectly legitimately, of course. However, for some strange reason he’s upset, and now challenges you to a rematch - this time at the game of Advanced Battleships, and with even higher stakes!

You each have a grid consisting of $M$ rows of $N$ cells eacg ($1 \leq M,N \leq 500$). Each cell is either empty or contains part of a player’s ship. What makes this game so “advanced” is the fact that each ship consists of a maximal set of 1 or more adjacent, nonempty cells. Two cells are considered adjacent if they share a common side. Of course, this means that ships can have some very strange shapes. No two ships can be adjacent to one another, of course.

You know for a fact that you can distract your friend for a brief moment, this time by telling him that someone proved that P = NP, but this trick will again only work exactly once. While he isn’t looking, you’ll have time to snatch up some of his ships with one hand. Your hand can cover a square of exactly $S$x$S$ cells ($1 \leq S \leq min\{M,N\}$), and you can gather all the ships that are at least partially within such a square at once.

Of course, your friend is no fool, so he’s got his grid well concealed. As such, you don’t know anything about it except its size, so when the time comes, you’ll just choose a random square of size $S$x$S$ that’s completely within the grid.

As usual, these bets attract large crowds. One of the bystanders who can see your opponent’s grid knows your plan, and is curious as to the expected number of ships that you will grab (in other words, the average number of ships out of all the possible snatches you could make). Nerdy though he is, he can’t calculate it in his head, so he runs over to a computer and codes up a program...

### Input

Line $1$: 3 integers, $M$, $N$, and $S$

Next $M$ lines: $N$ characters each, representing your opponent’s grid – an ‘X’ represents a ship, while a ‘.’ represents an empty cell

### Output

A single number – the expected number of ships that you’ll grab, rounded to 6 decimal places.'''



class UnionFind:
    def __init__(self,size):
        self.parents = [i for i in range(size)]

    def getRoot(self,index):
        x = self.parents[index]
        tmp = index
        while x != tmp:
            tmp = x
            x = self.parents[x]
        return x


    def union(self,index1,index2):
        '''
        make subtree for element at index2 child of subtree for element at index1
        :param index1:
        :param index2:
        :return:
        '''
        root1 = self.getRoot(index1)
        root2  = self.getRoot(index2)

        self.parents[root2] = root1

    def getNumOfClasses(self):
        return len(set(self.parents)) - 1


def getIndexIn1D(i,j,width):
    return i * width + j


def func(string:str):
    # 1. parse string
    lines = string.split('\n')
    m,n,s = map(int,lines[0].split(' '))

    def getElem(i,j):
        return lines[i+1][j]


    uf = UnionFind(m*n)
    for i in range(m):
        for j in range(n):
            elem = getElem(i,j)
            index = getIndexIn1D(i,j,n)
            if elem == 'X':
                if j + 1 < n:
                    if getElem(i,j+1) == 'X':  uf.union(index,index+1)


                if i+1 < m:
                    if getElem(i+1,j) == 'X': uf.union(index,index+n)

            else:
                uf.parents[index] = -1



    res = []
    for i in range(m-s+1):
        for j in range(n-s+1):
            cls = set()
            for deltaI in range(s):
                for deltaJ in range(s):
                    index = getIndexIn1D(i+deltaI,j+deltaJ,n)
                    if uf.parents[index] != -1:
                        cls.add(uf.parents[index])
            res.append(len(cls))

    return round(sum(res) / len(res),6)


inputString = input() + '\n'
m = int(inputString.split(' ')[0])
for i in range(m):
    inputString += input() + '\n'

print(func(inputString))


# print(inputString)
















#
# inputString = '''5 5 2
# XXXX.
# X..X.
# X..X.
# X....
# .XX..
# '''

