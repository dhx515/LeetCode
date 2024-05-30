class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set([0])
        queue = deque([0])
            
        while queue:
            
            if len(visited) == len(rooms):
                return True 
            
            room_key = queue.popleft()
            for key in rooms[room_key]:
                if key in visited:
                    continue
                visited.add(key)
                queue.append(key)

        return False