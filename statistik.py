from anime import EPISODES, RATING, WATCH


def total_episodes(data, index=0):
    if index == len(data):  
        return 0
    return data[index][EPISODES] + total_episodes(data, index + 1)


def count_watch_status(data, status, index=0):
    """Count rows whose watch status starts with 'finished', 'watching', etc."""
    if index == len(data):  
        return 0

    if data[index][WATCH].startswith(status):
        this_row = 1
    else:
        this_row = 0
    return this_row + count_watch_status(data, status, index + 1)


def sum_ratings(data, index=0):
    if index == len(data):  
        return 0
    return data[index][RATING] + sum_ratings(data, index + 1)


def average_rating(data):
    if len(data) == 0:  
        return 0
    return sum_ratings(data) / len(data)