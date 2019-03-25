class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """

        rooms = []
        visit_set = []
        n = len(graph)

        for i in range(len(graph)):
            rooms.append([i])
            visit_set.append(i)
        Next_rooms = []
        next_visit_set = []

        while True:
            for i,node in enumerate(visit_set):
                for next in graph[node]:
                    Next_One_room = rooms[i] + [next]
                    next_visit_set = next_visit_set + graph[next]
                    if len(set(Next_One_room)) == n:
                        return len(Next_One_room) - 1
                    Next_rooms.append(Next_One_room)
            visit_set = next_visit_set
            next_visit_set = []
            rooms = Next_rooms




graph = [[2,5,7],[2,4],[0,1],[5],[5,6,1],[4,10,8,0,3],[4,9],[0],[5],[6],[5]]
p = Solution()
print(p.shortestPathLength(graph))
