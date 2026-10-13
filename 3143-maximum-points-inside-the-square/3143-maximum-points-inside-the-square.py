class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:

        if len(s) == 1:
            return 1
        
        len_arr = []
        for i in range(len(points)):
            max_len = max(abs(points[i][0]), abs(points[i][1]))
            len_arr.append((max_len, s[i]))
        
        len_arr.sort(key=lambda x: x[0])
        print(len_arr)

        tags = set()
        max_dist = 0
        cnt = 0

        for (dist, tag) in len_arr:
            if dist != max_dist:
                max_dist = dist
                cnt = 0
            
            if tag in tags:
                return len(tags) - cnt
            else:
                tags.add(tag)
                cnt += 1

        return len(tags)

