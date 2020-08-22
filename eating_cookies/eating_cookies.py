'''
Input: an integer
Returns: an integer
'''
#def eating_cookies(n):

# check for 0 cookies first, then check fi there are negative cookies left (this doesn't count)
# return the total of the possibilites of eating 1, 2, or 3 at a time
    
   # if n == 0: 
   # 	return 1
  #  elif n< 0:
  #  	return 0

   # return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


def eating_cookies(n, cache):
	if n == 0:
		return 1
	elif n < 0:
		return 0 
	elif cache[n] > 0:
		return cache[n]
	else:
		cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
		return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
