"""
    https://leetcode.com/problems/cheapest-flights-within-k-stops/

    Time Complexity:    O(N + E * K * lg(E * K))
    Space Complexity:   O(N + E * K)

    Reference:
    https://leetcode.com/problems/cheapest-flights-within-k-stops/editorial/comments/1690938
    https://leetcode.com/problems/cheapest-flights-within-k-stops/editorial/

    @author: Leon
"""


from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n, flights, source, destination, k):
        distances = {}
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))
        heap = [(0, 0, source)]
        while heap:
            cost, distance, cur = heapq.heappop(heap)
            if cur == destination and distance - 1 <= k:
                return cost
            if cur not in distances or distances[cur] > distance:
                distances[cur] = distance
                for neighbor, price in adj[cur]:
                    heapq.heappush(
                        heap, (cost + price, distance + 1, neighbor))
        return -1
