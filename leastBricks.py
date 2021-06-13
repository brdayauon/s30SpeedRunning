class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
      '''
        [[1,2,2,1],
         [3,1,2],
         [1,3,2],
         [2,4],
         [3,1,2],
         [1,3,1,1]]
      maxNumberGaps = minTotalBricks
      HAPPY CASE
        RAW         DIAGRAM
Input: [[1, 2, 3],  | |  |   |
        [1, 3, 2],  | |   |  |
        [4, 1, 1]   |    | | |
        ]
        Output: 1

      U - 
      M - HashMap
      P -
        - Iterate through each row
        - Increment the numb of gaps for each position
        - Iter through the map, and find the pos with max gaps
        - Return width - max gaps

      [|, ,|, , ,|, , ,|]

      1, 2, 3 => 1, 3
      1, 3, 2 => 1, 4
      4, 1, 1 => 4, 5

      col 1, 2 gaps
      col 4, 2 gaps
      3 - 2 => 1

        RAW         DIAGRAM
Input: [[3],        |     |
        [3],        |     |
        [3]         |     |
        ]
Output: 3

        {
            1: 2
            3: 1
            4: 2
            5: 1

        }
      '''

      gaps = {}
      for i in range(len(wall)):
        gap = 0
        for j in range(len(wall[i])-1):
            gap += wall[i][j]
            if gap not in gaps.keys():
                gaps[gap] = 0
            
            gaps[gap] += 1
    
      max_gaps = 0
      for pos, num_gap in gaps.items():
        max_gaps = max(max_gaps, num_gap)
    
      return len(wall) - max_gaps


