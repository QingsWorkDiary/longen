def twoSum(nums, target):   
    num_dict = {}  
      
    start = 0  
    end = len(nums) - 1  
      
    for i in range(len(nums)):
        for j in [m for m in range(i+1, len(nums))]:
            if nums[i]+nums[j]==target:
                print(i,j)

a=[1,2,3,4,5,6,7,8,9,10]
twoSum(a,10)

