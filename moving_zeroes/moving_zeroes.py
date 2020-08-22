'''
Input: a List of integers
Returns: a List of integers
'''

# this solution takes 0(1) but runs in 0(n^2) time 
#itearte through numbers
#if number is not zero, increment the index
#if number is zero, append to end of array

# def moving_zeroes(arr):
#     i = 0
#     end = len(arr)

#     while i < end:
#         if arr[i] == 0:
#             arr.append(arr.pop(i))
#             end -= 1
#         else:
#             i += 1

#     return arr



# O(1) space and runs in O(n) time 

def moving_zeroes(arr):

	#swap positions until pointers meet in the middle

	i = 0
	j = len(arr) - 1

	while i < j:
		#is i 0?
		if arr[i] == 0:
			# while i is less than j
			# if j isn't zero, swap and break
			while i < j:
				if arr[j] != 0:
					arr[i], arr[j] = arr[j], arr[i]
					i += 1
					j -= 1
					break
			else:
				j -= 1
		else:
			i += 1
	return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

