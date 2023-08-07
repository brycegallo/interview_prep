# leetcode 0621 - Task Scheduler
# Medium - Heap / Priority Queue
#
# Given a characters array tasks, representing the tasks a CPU needs to do,
# where each letter represents a different task. Tasks could be done in any order.
# Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown period between two same tasks
# (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
#
# Return the least number of units of times that the CPU will take to finish all the given tasks.
# Time: O(n) Memory: O(m * n * log(26)) where m is the number of tasks, n is the cooldown time
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
