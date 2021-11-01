# A program to find a pair of number from a given list whose sum is equal to the given target sum
# Brute force method 
# O(n^2) time | O(1) space
def twoNumberSum1(array,targetSum):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==targetSum:
                return [array[i],array[j]]
    
    return []
print(twoNumberSum1([3,5,-4,8,11,1,-1,6],10))

# O(n) time | O(n) space
def twoNumberSum2(array,targetSum):
    nums={}
    for num in array:
        if targetSum-num in nums:
            return [targetSum-num,num]
        else:
            nums[num]=True
    return []
print(twoNumberSum2([3,5,-4,8,11,1,-1,6],10))

# O(nlogn) time | O(1) space
def twoNumberSum3(array,targetSum):
    array.sort()
    left=0
    right=len(array)-1
    while left<right:
        currentSum=array[left]+array[right]
        if currentSum==targetSum:
            return [array[left],array[right]]
        elif currentSum<targetSum:
            left+=1
        elif currentSum>targetSum:
            right-=1
    return []
print(twoNumberSum3([3,5,-4,8,11,1,-1,6],10))

