class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        smoothed = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                total = 0  
                count = 0  

                for di in range(-1, 2):  
                    for dj in range(-1, 2):  
                        ni = i + di 
                        nj = j + dj
                        if 0 <= ni < rows and 0 <= nj < cols:
                            total += int(img[ni][nj])
                            count += 1  
                smoothed[i][j] = total // count 
        return smoothed
  
