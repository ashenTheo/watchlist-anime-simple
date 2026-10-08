NAME = 0
SEASON = 1
EPISODES = 2
RATING = 3
RELEASE = 4
WATCH = 5

RELEASE_OPTIONS = ["onair", "completed", "hiatus", "belum release"]
WATCH_OPTIONS = ["watch later", "watching", "finished", "dropped"]


def ask_text(question, old=None):
    while True:
        if old is None:
            text = input(question + ": ")
        else:
            text = input(question + " [" + str(old) + "]: ")
        text = text.strip()

        if text == "" and old is not None:
            return old
        if text == "":
            print("Cannot be empty.")
        elif "|" in text:
            print("Please do not use the | character.")
        else:
            return text


def ask_int(question, low, high, old=None):
    
    if old is not None and (old < low or old > high):
        old = None

    while True:
        if old is None:
            text = input(question + ": ")
        else:
            text = input(question + " [" + str(old) + "]: ")
        text = text.strip()

        if text == "" and old is not None:
            return old

        try:
            number = int(text)
        except ValueError:
            print("Please type a whole number.")
            continue

        if number < low or number > high:
            print("The number must be between", low, "and", high)
        else:
            return number


def ask_float(question, low, high, old=None):
    while True:
        if old is None:
            text = input(question + ": ")
        else:
            text = input(question + " [" + str(old) + "]: ")
        text = text.strip()

        if text == "" and old is not None:
            return old

        try:
            number = float(text)
        except ValueError:
            print("Please type a number (example: 5.5).")
            continue

        if number < low or number > high:
            print("The number must be between", low, "and", high)
        else:
            return number


def ask_choice(question, options, old=None):
    """Show a numbered list and return the chosen option (as text)."""
    print(question)
    for i in range(len(options)):
        print("  " + str(i + 1) + ". " + options[i])

    while True:
        if old is None:
            text = input("Choose number: ")
        else:
            text = input("Choose number [" + old + "]: ")
        text = text.strip()

        if text == "" and old is not None:
            return old

        if text.isdigit() and 1 <= int(text) <= len(options):
            return options[int(text) - 1]
        print("Invalid choice.")


def get_watch_status(watch):
    """Return only the status word: 'watching 6/24' -> 'watching'."""
    if watch.startswith("watching"):
        return "watching"
    if watch.startswith("dropped"):
        return "dropped"
    if watch.startswith("finished"):
        return "finished"
    return "watch later"


def get_watch_progress(watch):
    """Return the watched episode number: 'watching 6/24' -> 6."""
    if watch.startswith("watching") or watch.startswith("dropped"):
        part = watch.split(" ")[1]      
        return int(part.split("/")[0])  
    return None


def ask_watch(episodes, release, old=None):
    
    if release == "belum release":
        print("Watch progress is set to 'watch later' (anime is not released yet).")
        return "watch later"

    old_status = None
    old_progress = None
    if old is not None:
        old_status = get_watch_status(old)
        old_progress = get_watch_progress(old)

    status = ask_choice("Watch progress:", WATCH_OPTIONS, old_status)

    if status == "watching" or status == "dropped":
        if status != old_status:
            old_progress = None  
        progress = ask_int("Episodes watched (0-" + str(episodes) + ")",
                           0, episodes, old_progress)
        return status + " " + str(progress) + "/" + str(episodes)

    return status  


def show_rows(data, positions):
    """Show the rows at the given positions (a list of row indexes)."""
    if len(positions) == 0:
        print("(no data)")
        return

    print()
    print(f"{'No':<4}{'Name':<28}{'S':<4}{'Ep':<6}{'Rating':<9}{'Release':<15}{'Watch'}")
    print("-" * 85)

    for i in positions:
        row = data[i]
        rating_text = str(row[RATING]) + "/10"
        print(f"{i + 1:<4}{row[NAME][:26]:<28}{row[SEASON]:<4}{row[EPISODES]:<6}"
              f"{rating_text:<9}{row[RELEASE]:<15}{row[WATCH]}")


def show_all(data):
    positions = list(range(len(data)))
    show_rows(data, positions)


def add_anime(data):
    print("\n=== Add Anime ===")
    name = ask_text("Name")
    season = ask_int("Season number", 1, 100)
    episodes = ask_int("Number of episodes in this season", 1, 100000)
    rating = ask_float("Rating (1-10, example 5.5)", 1, 10)
    release = ask_choice("Release status:", RELEASE_OPTIONS)
    watch = ask_watch(episodes, release)

    data.append([name, season, episodes, rating, release, watch])
    print("Anime added.")


def edit_anime(data):
    """Edit one anime. Returns True if the NAME was changed, otherwise False."""
    if len(data) == 0:
        print("There is no data yet.")
        return False

    show_all(data)
    number = ask_int("\nNumber of the anime to edit (0 = cancel)", 0, len(data))
    if number == 0:
        return False

    row = data[number - 1]
    old_name = row[NAME]

    print("\n=== Edit Anime (press Enter to keep the old value) ===")
    name = ask_text("Name", row[NAME])
    season = ask_int("Season number", 1, 100, row[SEASON])
    episodes = ask_int("Number of episodes in this season", 1, 100000, row[EPISODES])
    rating = ask_float("Rating (1-10)", 1, 10, row[RATING])
    release = ask_choice("Release status:", RELEASE_OPTIONS, row[RELEASE])
    watch = ask_watch(episodes, release, row[WATCH])

    data[number - 1] = [name, season, episodes, rating, release, watch]
    print("Anime updated.")

    return name.lower() != old_name.lower()


def delete_anime(data):
    """Delete one anime. Returns True if something was deleted."""
    if len(data) == 0:
        print("There is no data yet.")
        return False

    show_all(data)
    number = ask_int("\nNumber of the anime to delete (0 = cancel)", 0, len(data))
    if number == 0:
        return False

    answer = ask_choice("Delete '" + data[number - 1][NAME] + "'?", ["yes", "no"])
    if answer == "yes":
        data.pop(number - 1)
        print("Anime deleted.")
        return True

    print("Cancelled.")
    return False