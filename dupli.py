def checkDuplicate(nums):
	nums.sort()
	for i in range(1, len(nums)):
		if nums[i] == nums[i - 1]:
			return True
	return False
numbers = input().split()
numbers = [int(n) for n in numbers]
print(checkDuplicate(numbers))