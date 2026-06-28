class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity: O(N) - 배열을 딱 한 번만 돕니다.
        # Space Complexity: O(N) - 지나온 숫자들을 기억할 딕셔너리 공간이 필요합니다.

        # 1. { 숫자 : 인덱스 } 형태로 저장할 빈 딕셔너리(num_map)를 만든다.
        # 2. nums를 인덱스(i)와 값(num)을 동시에 추출하며 한 번만 루프를 돈다. (enumerate 활용)
        # 3. 내가 지금 찾는 짝꿍(target - num)이 이미 딕셔너리(num_map)에 들어있는지 확인한다.
        #    - 들어있다면? 정답 발견! [짝꿍의 인덱스, 현재 인덱스(i)]를 바로 return!
        # 4. 주머니에 없다면? 
        #    - 현재 숫자와 인덱스를 딕셔너리에 저장하고 다음 숫자로 넘어간다.

        nm = {}
        
        for i, num in enumerate(nums):
            nm[num] = i

        for i in range(len(nums)):
            fnum = target - nums[i]
            if fnum in nm:
                if i != nm[fnum]:
                    return [i, nm[fnum]]