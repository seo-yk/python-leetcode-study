class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        visited = set([startGene])
        queue = deque([(startGene, 0)])
        genes = ['A', 'C', 'G', 'T']

        while queue:
            cur, steps = queue.popleft()

            if cur == endGene:
                return steps

            for i in range(len(cur)):
                for g in genes:
                    next_gene = cur[:i] + g + cur[i+1:]

                    if next_gene in bank_set and next_gene not in visited:
                        visited.add(next_gene)
                        queue.append((next_gene, steps+1))

        return -1