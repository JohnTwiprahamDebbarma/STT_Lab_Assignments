"""
Hi! I am John (22110108). This is for the purpose of lab assignment 1 for the course "Software Tools and Techniques for CSE".
My module below implements the Merge Sort algorithm to sort an array in ascending order.
It divides the array into smaller subarrays, recursively sorts them, and merges them back together.
"""

def merge_sort(input_array):
    """
    This function sorts an input array using the Merge Sort algorithm.

    Args:
    input_array (list): A list of elements to be sorted.

    Returns:
    None: The list is sorted in place.
    """
    if len(input_array) > 1:
        mid = len(input_array) // 2  # Finding the middle of the array
        left_half = input_array[:mid]  # Dividing the elements into two halves
        right_half = input_array[mid:]

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Merging the sorted halves:
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                input_array[k] = left_half[i]
                i += 1
            else:
                input_array[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left in the left half:
        while i < len(left_half):
            input_array[k] = left_half[i]
            i += 1
            k += 1

        # Checking if any element was left in the right half:
        while j < len(right_half):
            input_array[k] = right_half[j]
            j += 1
            k += 1


# Example usage
if __name__ == "__main__":
    example_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", example_array)

    merge_sort(example_array)

    print("Sorted array:", example_array)
