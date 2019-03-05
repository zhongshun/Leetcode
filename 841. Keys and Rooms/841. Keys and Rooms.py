class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        def ExploreNext(num,room,visited):
            for i in room[num]:
                if i not in visited:
                    visited.append(i)
                    if ExploreNext(i,room,visited):
                        return True
                if len(visited) == len(room):
                    return True
            return False

        num = 0
        visited = [0]
        room = rooms

        return ExploreNext(num,room,visited)



room = [[1],[2],[3],[]]
p = Solution()
print(p.canVisitAllRooms(room))

visited = [0] * len(room)
print(visited)
visited[1] = 2
print(visited)
