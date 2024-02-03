"""
Radix Sort Visualization

This Python script demonstrates the Radix Sort algorithm using matplotlib to visualize the sorting process.

Usage:
- The script generates a random list of integers for demonstration purposes.
- The algorithm sorts the list in ascending order, providing a step-by-step visualization.

Dependencies:
- matplotlib: A data visualization library for creating static, animated, and interactive visualizations in Python.

Author: Karthik

Date: 05-01-2024

"""

import matplotlib.pyplot as plt
import numpy as np

def counting_sort(lst, exp):
    """
    Helper function to perform Counting Sort on a specific digit (exp) of the input list.

    Parameters:
    - lst (list): The input list to be sorted.
    - exp (int): The current digit position.

    Returns:
    - list: The sorted list.
    """
    n = len(lst)
    output = [0] * n
    counting_array = [0] * 10  # Counting array for digits 0 to 9

    # Count the frequency of each digit at the current position
    for i in range(n):
        index = lst[i] // exp
        counting_array[index % 10] += 1

    # Update the counting array to store the position of each element in the output array
    for i in range(1, 10):
        counting_array[i] += counting_array[i - 1]

    # Build the output array by placing elements in their sorted order
    i = n - 1
    while i >= 0:
        index = lst[i] // exp
        output[counting_array[index % 10] - 1] = lst[i]
        counting_array[index % 10] -= 1
        i -= 1

    # Visualize the current state of the sorted list
    x_sorted = np.arange(0, len(output), 1)
    plt.bar(x_sorted, output, color='gold')
    plt.pause(0.5)
    plt.clf()

    return output

def radix_sort_visualization(lst):
    """
    Sorts a list using the Radix Sort algorithm and visualizes each step.

    Parameters:
    - lst (list): The input list to be sorted.

    Returns:
    None
    """
    max_value = max(lst)
    exp = 1

    # Visualize the input list
    x = np.arange(0, len(lst), 1)
    plt.bar(x, lst, color='lightblue')
    plt.pause(0.5)
    plt.clf()

    # Perform counting sort for each digit place (units, tens, hundreds, etc.)
    while max_value // exp > 0:
        lst = counting_sort(lst, exp)
        exp *= 10

    # Display the final sorted list
    x_sorted_final = np.arange(0, len(lst), 1)
    plt.bar(x_sorted_final, lst, color='gold')
    plt.pause(0.5)
    plt.show()

# Example usage
amount = 15
lst_to_sort = np.random.randint(0, 1000, amount)

# Sorting the entire list
radix_sort_visualization(lst_to_sort)
