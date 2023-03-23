class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        indices_pairs=[]
        for row in range(len(matrix)): 		
            for col in range(len(matrix[0])):
                if matrix[row][col]==0: 
                    indices_pairs.append((row,col)) 
        for indices_pairs in indices_pairs:
            row,col=indices_pairs  
            for j in range(len(matrix[0])):
                matrix[row][j]=0           
            for j in range(len(matrix)): 
                 matrix[j][col]=0

                
        