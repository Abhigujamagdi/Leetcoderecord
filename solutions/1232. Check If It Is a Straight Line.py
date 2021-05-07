class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(len(coordinates)):
            for j in range(len(coordinates[i])):
                if coordinates[i][1] == coordinates[j][0]:
                    return True
       
