"""
Heap Sort Visualization

This Python script demonstrates the Heap Sort algorithm using matplotlib to visualize the sorting process.

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

def heapify(lst, n, i):
    """
    Heapify a subtree rooted at index i.

    Parameters:
    - lst (list): The input list to be heapified.
    - n (int): Size of the heap.
    - i (int): Root index of the subtree to be heapified.

    Returns:
    None
    """
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if left child exists and is greater than the root
    if left_child < n and lst[left_child] > lst[largest]:
        largest = left_child

    # Check if right child exists and is greater than the root
    if right_child < n and lst[right_child] > lst[largest]:
        largest = right_child

    # Swap the root if needed
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]

        # Visualize the current state of the heap using a bar chart
        x = np.arange(0, len(lst), 1)
        plt.bar(x, lst, color='lightblue')
        plt.bar([i, largest], [lst[i], lst[largest]], color=['green', 'red'])  # Highlight the elements being swapped
        plt.pause(0.5)
        plt.clf()

        # Recursively heapify the affected subtree
        heapify(lst, n, largest)

def heap_sort_visualization(lst):
    """
    Sorts a list using the Heap Sort algorithm and visualizes each step.

    Parameters:
    - lst (list): The input list to be sorted.

    Returns:
    None
    """
    n = len(lst)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]  # Swap the root (maximum) element with the last element
        heapify(lst, i, 0)  # Heapify the reduced heap

# Example usage
amount = 15
lst_to_sort = np.random.randint(0, 100, amount)

# Sorting the entire list
heap_sort_visualization(lst_to_sort)
