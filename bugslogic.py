nums=[11.11,12.11,13.11,14.11]

is_assending = all(nums[p] <= nums[p+1] for p in range(len(nums)-1))

assert is_assending ,f"IT IS NOT IN THE ASSENDING ORDER"
print("assetion is passed in the assending orde")


