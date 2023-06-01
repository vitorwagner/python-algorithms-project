def find_duplicate(nums):
    if type(nums) != list or len(nums) == 0:
        return False

    newNums = list()

    for i in nums:
        if type(i) != int or i < 0:
            return False
        if i not in newNums:
            newNums.append(i)
        else:
            return i
    return False
# https://www.trainingint.com/how-to-find-duplicates-in-a-python-list.html
