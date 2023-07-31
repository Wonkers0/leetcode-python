#
# @lc app=leetcode id=2079 lang=python
#
# [2079] Watering Plants
#


# @lc code=start
class Solution(object):
    def wateringPlants(self, plants, capacity):
        currentPlant = 0
        currentWater = capacity
        moves = 1

        while currentPlant < len(plants) - 1:
            while currentWater >= plants[currentPlant]:
                currentWater -= plants[currentPlant]
                currentPlant += 1

                if currentPlant >= len(plants):
                    return moves

                moves += 1

            currentWater = capacity
            moves += currentPlant * 2

        return moves


# @lc code=end

solution = Solution()
print(solution.wateringPlants([2, 2, 3, 3], 5))  # Expected Answer: 14
print(solution.wateringPlants([7, 7, 7, 7, 7, 7, 7], 8))  # Expected Answer: 49
print(solution.wateringPlants([1, 1, 1, 4, 2, 3], 4))  # Expected Answer: 30
print(solution.wateringPlants([1, 3, 2, 2], 5))  # Expected Answer: 8
print(solution.wateringPlants([2, 2, 3, 3], 5))  # Expected Answer: 14
