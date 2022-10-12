
def qucik_srot(nums):
    length = len(nums)

    if length <= 1: # Return List if nothing is contained
        return nums
    else:
        pivot = nums.pop()  # Chooses the last item as the Pivot

    items_greater = []
    items_lower = []

    for item in nums: # Starts comparing If other items are greater than of less that pivot 
        if item> pivot:
            items_greater.append(item)   
        else:
            items_lower.append(item)
    #Makes two seperate list for items
    #Using Funtion recursion to loop this function untill there is no items left
    return qucik_srot(items_lower) + [pivot] + qucik_srot(items_greater) 


print(qucik_srot([3,7,4,2,8,5,9]))