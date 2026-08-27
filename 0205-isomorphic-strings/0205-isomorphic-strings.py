class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        sd = Counter(s)
        td = Counter(t)
        if len(sd) == len(td):
            table = str.maketrans(s, t)
            isomorphic = s.translate(table)
            return (isomorphic == t)
        return False
        
        