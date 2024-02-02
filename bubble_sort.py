"""
Bubble Sort Visualization

This Python script demonstrates the Bubble Sort algorithm using matplotlib to visualize the sorting process.

Usage:
- The script generates a random list of integers for demonstration purposes.
- The algorithm sorts the list in ascending order, providing a step-by-step visualization.

Dependencies:
- matplotlib: A data visualization library for creating static, animated, and interactive visualizations in Python.

Author: Karthik

Date: 12-12-2023

"""

import matplotlib.pyplot as plt
import numpy as np

def bubble_sort_visualization(lst):
    """
    Sorts a list using the Bubble Sort algorithm and visualizes each step.

    Parameters:
    - lst (list): The input list to be sorted.

    Returns:
    None
    """

    amount = len(lst)
    x = np.arange(0, amount, 1)

    # Iterate through each element in the list
    for i in range(amount):
        # Compare and swap adjacent elements to bubble up the largest element
        for j in range(0, amount-i-1):
            # Visualize the current state of the list using a bar chart
            plt.bar(x, lst)
            plt.pause(0.001)
            plt.clf()

            # Swap if the element at position j is greater than the next element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    # Display the final sorted list
    plt.show()

# Example usage
amount = 15
lst_to_sort = np.random.randint(0, 100, amount)

bubble_sort_visualization(lst_to_sort)
