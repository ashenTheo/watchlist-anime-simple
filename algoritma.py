# algoritma.py
# Bubble sort and linear search.
from anime import NAME


def get_key(row, column):
    """The value used to compare rows. Names ignore upper/lower case."""
    if column == NAME:
        return row[NAME].lower()
    return row[column]


def bubble_sort(data, column, show_process):
    """Sort the 2D list by one column (smallest to largest, A to Z) using bubble sort.
    Each pass compares neighbours and swaps them if they are in the wrong order,
    so the largest value 'bubbles up' to the end of the list."""
    n = len(data)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if get_key(data[j], column) > get_key(data[j + 1], column):
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
                swapped = True

        # Print the current state of the list after this pass
        if show_process:
            if swapped:
                print("\nPass", i + 1, ": swaps were made")
            else:
                print("\nPass", i + 1, ": no swaps, the list is already sorted")
            for k in range(n):
                mark = " "
                if k >= n - 1 - i:
                    mark = "*"  # * = already in its final place
                print(f"  {mark}{k + 1:>3}. {data[k][NAME][:25]:<25} {data[k][column]}")

        # If nothing was swapped, the list is sorted, so we can stop early
        if not swapped:
            break


def linear_search(data, column, value):
    """Check every row one by one. Returns a list of matching row indexes.
    startswith is used so that 'watching' also matches 'watching 6/24'."""
    result = []
    for i in range(len(data)):
        if data[i][column].startswith(value):
            result.append(i)
    return result


def linear_search_name(data, text):
    """Check every row one by one for a name that contains the text
    (upper/lower case is ignored). Returns a list of matching row indexes."""
    result = []
    text = text.lower()
    for i in range(len(data)):
        if text in data[i][NAME].lower():
            result.append(i)
    return result