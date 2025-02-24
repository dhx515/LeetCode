class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start > destination:
            start, destination = destination, start  # 항상 start < destination 유지
        
        # 시계 방향 거리
        clockwise_distance = sum(distance[start:destination])
        # 전체 거리
        total_distance = sum(distance)
        # 반시계 방향 거리
        counterclockwise_distance = total_distance - clockwise_distance
        
        return min(clockwise_distance, counterclockwise_distance)