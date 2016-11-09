# Python program for implementation of Bubble Sort

def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place, so the inner loops will run until it reaches the last i elements
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater than the next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]


def modifiedBubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):
        # Taking a flag variable
		flag = 0
		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]
				# Setting the flag, if swapping occurs
				flag = 1

		# If not swapped, that means the list has already sorted
		if flag == 0:
		    break

# Main code
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
# modifiedBubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i]),
