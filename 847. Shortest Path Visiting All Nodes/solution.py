class Solution:
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        if len(graph) == 1:
            return 0
        n = len(graph)
        end = (1 << n) - 1

        q = [(1 << i, i, 0) for i in range(n)]
        visited = set([ele[:2] for ele in q])
        i = 0
        while i < len(q):
            v, h, s = q[i]
            i += 1
            for c in graph[h]:
                nv = v | (1 << c)
                if nv == end:
                    return s + 1
                if (nv, c) not in visited:
                    visited.add((nv, c))
                    q.append((nv, c, s + 1))
        return -1


graph = [[2,5,7],[2,4],[0,1],[5],[5,6,1],[4,10,8,0,3],[4,9],[0],[5],[6],[5]]
p = Solution()
print(p.shortestPathLength(graph))