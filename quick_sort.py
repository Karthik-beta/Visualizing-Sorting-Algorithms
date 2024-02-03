"""
Quicksort Visualization

This Python script demonstrates the Quicksort algorithm using matplotlib to visualize the sorting process.

Usage:
- The script generates a random list of integers for demonstration purposes.
- The algorithm sorts the list in ascending order, providing a step-by-step visualization.

Dependencies:
- matplotlib: A data visualization library for creating static, animated, and interactive visualizations in Python.

Author: Karthik

Date: 03-02-2024

"""

import matplotlib.pyplot as plt
import numpy as np

def quicksort_visualization(lst, low, high):
    """
    Sorts a list using the Quicksort algorithm and visualizes each step.

    Parameters:
    - lst (list): The input list to be sorted.
    - low (int): The starting index of the list or sub-list.
    - high (int): The ending index of the list or sub-list.

    Returns:
    None
    """

    def partition(lst, low, high):
        """
        Partitions the list and returns the pivot index.

        Parameters:
        - lst (list): The input list to be partitioned.
        - low (int): The starting index of the list or sub-list.
        - high (int): The ending index of the list or sub-list.

        Returns:
        - int: The pivot index.
        """
        pivot = lst[high]
        i = low - 1

        for j in range(low, high):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        return i + 1

    if low < high:
        # Find the pivot element such that elements smaller than pivot are on the left, and greater on the right
        pivot_index = partition(lst, low, high)

        # Visualize the current state of the list using a bar chart
        x = np.arange(0, len(lst), 1)
        plt.bar(x, lst, color='lightblue')
        plt.bar(pivot_index, lst[pivot_index], color='red')  # Highlight the pivot element
        plt.pause(0.5)
        plt.clf()

        # Recursively sort the sub-lists on either side of the pivot
        quicksort_visualization(lst, low, pivot_index - 1)
        quicksort_visualization(lst, pivot_index + 1, high)

# Example usage
amount = 15
lst_to_sort = np.random.randint(0, 100, amount)

# Sorting the entire list
quicksort_visualization(lst_to_sort, 0, len(lst_to_sort) - 1)
