import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(FOLDER, "data.txt")


def load_data():
    """Read data.txt and return a 2D list (a list of rows)."""
    data = []

    try:
        file = open(FILE_NAME, "r")
    except FileNotFoundError:
        return data  

    for line in file:
        line = line.strip()
        if line == "":
            continue  

        parts = line.split("|")
        row = [parts[0], int(parts[1]), int(parts[2]), float(parts[3]),
               parts[4], parts[5]]
        data.append(row)

    file.close()
    return data


def save_data(data):
    """Write the whole 2D list back into data.txt."""
    file = open(FILE_NAME, "w")

    for row in data:
        line = (row[0] + "|" + str(row[1]) + "|" + str(row[2]) + "|" +
                str(row[3]) + "|" + row[4] + "|" + row[5])
        file.write(line + "\n")

    file.close()