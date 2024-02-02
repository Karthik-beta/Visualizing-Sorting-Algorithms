"""
Selection Sort Visualization

This Python script demonstrates the Selection Sort algorithm using matplotlib to visualize the sorting process.

Usage:
- The script generates a random list of integers for demonstration purposes.
- The algorithm sorts the list in ascending order, providing a step-by-step visualization.

Dependencies:
- matplotlib: A data visualization library for creating static, animated, and interactive visualizations in Python.

Author: karthik

Date: 23-12-2023

"""

import matplotlib.pyplot as plt
import numpy as np

def selection_sort_visualization(lst):
    """
    Sorts a list using the Selection Sort algorithm and visualizes each step.

    Parameters:
    - lst (list): The input list to be sorted.

    Returns:
    None
    """

    amount = len(lst)
    x = np.arange(0, amount, 1)

    # Iterate through each element in the list
    for i in range(amount):
        # Assume the current index as the minimum
        min_index = i

        # Iterate through the remaining unsorted part to find the minimum element
        for j in range(i+1, amount):
            if lst[j] < lst[min_index]:
                min_index = j

        # Visualize the current state of the list using a bar chart with color-coded elements
        plt.bar(x, lst, color='lightblue')
        plt.bar(min_index, lst[min_index], color='red')  # Highlight the minimum element
        plt.bar(i, lst[i], color='green')  # Highlight the element being swapped
        plt.pause(0.5)
        plt.clf()

        # Swap the found minimum element with the first element of the unsorted part
        lst[i], lst[min_index] = lst[min_index], lst[i]

    # Display the final sorted list
    plt.bar(x, lst, color='lightblue')
    plt.pause(0.5)
    plt.show()

# Example usage
amount = 15
lst_to_sort = np.random.randint(0, 100, amount)

selection_sort_visualization(lst_to_sort)
