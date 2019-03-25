import collections
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        res = 0
        rooms = [[0]]
        Next_rooms = []
        AllRooms = []
        for i in range(len(graph)):
            AllRooms.append(i)
        AllRooms = set(AllRooms)

        while True:
            res += 1
            for i in range(3):
                for room in rooms:
                    for node in room:
                        for next in graph[node]:
                            Next_One_room = room + [next]
                            Next_rooms.append(Next_One_room)
                            if set(Next_rooms) == AllRooms:
                                return res



graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output = 4
Explanation = [0,1,4,2,3]

res = 0
rooms = [[0]]
Next_rooms = []
AllRooms = []
for i in range(len(graph)):
    AllRooms.append(i)
AllRooms = set(AllRooms)
print(AllRooms)

for i in range(5):
    for room in rooms:
        for node in room:
            for next in graph[node]:
                Next_One_room = room + [next]
                print(Next_One_room)
                if set(Next_One_room) == AllRooms:
                    print(Next_One_room)
                Next_rooms.append(Next_One_room)
    rooms = Next_rooms
    Next_rooms = []

print(rooms)