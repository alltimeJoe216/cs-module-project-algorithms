'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    
    single_numbers = set()

    for number in arr:
    	if number not in single_numbers:
    		single_numbers.add(number)
    	else: 
    		single_numbers.remove(number)
    return single_numbers.pop()


if __name__ == '__main__':
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    print(f"The odd-number-out is {single_number(arr)}")



