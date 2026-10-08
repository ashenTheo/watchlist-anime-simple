from anime import NAME


def get_key(row, column):
    """The value used to compare rows. Names ignore upper/lower case."""
    if column == NAME:
        return row[NAME].lower()
    return row[column]


def selection_sort(data, column, show_process):
    """Sort the 2D list by one column (smallest to largest, A to Z) using selection sort."""
    n = len(data)

    for i in range(n - 1):
        
        best = i
        for j in range(i + 1, n):
            if get_key(data[j], column) < get_key(data[best], column):
                best = j
        
        if best != i:
            temp = data[i]
            data[i] = data[best]
            data[best] = temp
        
        if show_process:
            if best != i:
                print("\nStep", i + 1, ": swap position", i + 1, "with position", best + 1)
            else:
                print("\nStep", i + 1, ": no swap needed")
            for k in range(n):
                mark = " "
                if k <= i:
                    mark = "*"  
                print(f"  {mark}{k + 1:>3}. {data[k][NAME][:25]:<25} {data[k][column]}")


def linear_search(data, column, value):
    """Check every row one by one. Returns a list of matching row indexes.
    startswith is used so that 'watching' also matches 'watching 6/24'."""
    result = []
    for i in range(len(data)):
        if data[i][column].startswith(value):
            result.append(i)
    return result


def binary_search(data, name):
    """Search a name. The data MUST already be sorted by name (ascending).
    Returns a list of all row indexes with that name (different seasons)."""
    target = name.lower()
    left = 0
    right = len(data) - 1
    found = -1

    while left <= right:
        middle = (left + right) // 2
        middle_name = data[middle][NAME].lower()

        if middle_name == target:
            found = middle
            break
        elif middle_name < target:
            left = middle + 1
        else:
            right = middle - 1

    if found == -1:
        return []

    
    first = found
    while first > 0 and data[first - 1][NAME].lower() == target:
        first = first - 1

    last = found
    while last < len(data) - 1 and data[last + 1][NAME].lower() == target:
        last = last + 1

    return list(range(first, last + 1))