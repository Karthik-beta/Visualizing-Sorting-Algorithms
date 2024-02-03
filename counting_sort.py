"""
Counting Sort Visualization

This Python script demonstrates the Counting Sort algorithm using matplotlib to visualize the sorting process.

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

def counting_sort_visualization(lst):
    """
    Sorts a list using the Counting Sort algorithm and visualizes each step.

    Parameters:
    - lst (list): The input list to be sorted.

    Returns:
    None
    """
    max_value = max(lst)
    min_value = min(lst)
    range_size = max_value - min_value + 1

    # Create a counting array to store the frequency of each element
    counting_array = [0] * range_size

    # Visualize the input list
    x = np.arange(0, len(lst), 1)
    plt.bar(x, lst, color='lightblue')
    plt.pause(0.5)
    plt.clf()

    # Count the frequency of each element
    for num in lst:
        counting_array[num - min_value] += 1

    # Visualize the counting array
    x_counting = np.arange(min_value, max_value + 1, 1)
    plt.bar(x_counting, counting_array, color='lightgreen')
    plt.pause(0.5)
    plt.clf()

    # Generate the sorted list using the counting array
    sorted_list = []
    for i in range(min_value, max_value + 1):
        while counting_array[i - min_value] > 0:
            sorted_list.append(i)
            counting_array[i - min_value] -= 1

            # Visualize the current state of the sorted list
            x_sorted = np.arange(0, len(sorted_list), 1)
            plt.bar(x_sorted, sorted_list, color='gold')
            plt.pause(0.5)
            plt.clf()

    # Display the final sorted list
    x_sorted_final = np.arange(0, len(sorted_list), 1)
    plt.bar(x_sorted_final, sorted_list, color='gold')
    plt.pause(0.5)
    plt.show()

# Example usage
amount = 15
lst_to_sort = np.random.randint(0, 10, amount)

# Sorting the entire list
counting_sort_visualization(lst_to_sort)
