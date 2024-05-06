from typing import List


def count_deep_lake(depth_list: List[int]) -> int | str:
    if len(depth_list) < 3:
        return "At least three depths are required to calculate the depth of the lake."
    max_left_depth = 0
    max_right_depth = 0
    left = 0
    right = len(depth_list) - 1
    max_depth = 0
    while left < right:
        if depth_list[left] < depth_list[right]:
            if max_left_depth < depth_list[left]:
                max_left_depth = depth_list[left]
            else:
                max_depth = max(max_depth, (max_left_depth - depth_list[left]))
            left += 1
        else:
            if max_right_depth < depth_list[right]:
                max_right_depth = depth_list[right]
            else:
                max_depth = max(max_depth, (max_right_depth - depth_list[right]))
            right -= 1
    if max_depth > 0:
        return max_depth
    return "There are no lakes filled with water here."


depths = [1, 2, 6, 1, 2, 2, 3, 0, 1, 5, 7]
assert count_deep_lake([1, 2, 6, 1, 2, 2, 3, 0, 1, 5, 7]) == 6
assert count_deep_lake([1, 2]) == "At least three depths are required to calculate the depth of the lake."
assert count_deep_lake([]) == "At least three depths are required to calculate the depth of the lake."
assert count_deep_lake([1, 2, 5]) == "There are no lakes filled with water here."
assert count_deep_lake([7, 4, 1]) == "There are no lakes filled with water here."
