"""
Insertion Sort Visualization

This Python script demonstrates the Insertion Sort algorithm using matplotlib to visualize the sorting process.

Usage:
- The script generates a random list of integers for demonstration purposes.
- The algorithm sorts the list in ascending order, providing a step-by-step visualization.

Dependencies:
- matplotlib: A data visualization library for creating static, animated, and interactive visualizations in Python.

Author: Karthik

Date: 02-02-2024

"""

import matplotlib.pyplot as plt
import numpy as np

def insertion_sort_visualization(lst):
    """
    Sorts a list using the Insertion Sort algorithm and visualizes each step.

    Parameters:
    - lst (list): The input list to be sorted.

    Returns:
    None
    """

    amount = len(lst)
    x = np.arange(0, amount, 1)

    # Iterate through each element in the list
    for i in range(1, amount):
        key = lst[i]  # Current element to be inserted into the sorted part
        j = i - 1

        # Move elements greater than key to one position ahead of their current position
        while j >= 0 and key < lst[j]:
            plt.bar(x, lst, color='lightblue')
            plt.bar(j + 1, lst[j], color='red')  # Highlight the element being shifted
            plt.pause(0.5)
            plt.clf()

            lst[j + 1] = lst[j]
            j -= 1

        plt.bar(x, lst, color='lightblue')
        plt.bar(j + 1, key, color='green')  # Highlight the key being inserted
        plt.pause(0.5)
        plt.clf()

        lst[j + 1] = key  # Insert the key into its correct position

    # Display the final sorted list
    plt.bar(x, lst, color='lightblue')
    plt.pause(0.5)
    plt.show()

# Example usage
amount = 15
lst_to_sort = np.random.randint(0, 100, amount)

insertion_sort_visualization(lst_to_sort)
