class Solution:
    def removeStones(self, stones: [[int]]) -> int:
        columns = set()
        rows = set()
        count = 0

        firstx = stones[0][0]
        firsty = stones[0][-1]
        columns.add(firstx)
        rows.add(firsty)

        for location in stones[1:]:
            x = location[0]
            y = location[-1]
            if (x in columns) or (y in rows):
                count += 1
                print(x,y)
            columns.add(x)
            rows.add(y)
        return count


print(Solution().removeStones([[0,1],[1,0],[1,1]]))