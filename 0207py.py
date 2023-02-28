# leetcode 0207 - Course Schedule
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
# that you must take course bi first if you want to take course ai.
#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # loop to map each course to its prerequisite list
        preMap = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            preMap[course].append(prerequisite)

        visitingSet = set()

        def dfs(course):
            if course in visitingSet:  # cycle, cannot complete
                return False
            if preMap[course] == []:  # course has no prerequisites
                return True

            # this work does not need to be done next call if we set preMap[course] to [] at the end of this function
            visitingSet.add(course)
            for prerequisite in preMap[course]:
                if not dfs(prerequisite):  # if this function returns false for any course the whole thing is false
                    return False
            visitingSet.remove(course)  # we are no longer visiting this course
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True
