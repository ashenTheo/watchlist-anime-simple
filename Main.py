import storage
import statistik
import algoritma
from anime import (NAME, EPISODES, RATING, RELEASE, WATCH,
                   RELEASE_OPTIONS, WATCH_OPTIONS,
                   ask_text, ask_int, ask_choice,
                   show_all, show_rows,
                   add_anime, edit_anime, delete_anime)


def menu_search(data, sorted_by_name):
    print("\n=== Search ===")
    print("1. Linear search (release status)")
    print("2. Linear search (watch status)")
    print("3. Binary search (name)")
    choice = ask_int("Choose", 1, 3)

    if choice == 1:
        value = ask_choice("Release status:", RELEASE_OPTIONS)
        result = algoritma.linear_search(data, RELEASE, value)
    elif choice == 2:
        value = ask_choice("Watch status:", WATCH_OPTIONS)
        result = algoritma.linear_search(data, WATCH, value)
    else:
        if not sorted_by_name:
            print("Binary search needs sorted data.")
            print("Please sort by name first using the Sort menu.")
            return
        name = ask_text("Name to search")
        result = algoritma.binary_search(data, name)

    print("\nFound", len(result), "result(s).")
    show_rows(data, result)


def menu_sort(data):
    """Sorts the data (always ascending). Returns True if the data is now sorted by name."""
    print("\n=== Sort ===")
    print("1. Rating")
    print("2. Name")
    print("3. Number of episodes")
    choice = ask_int("Sort by", 1, 3)

    if choice == 1:
        column = RATING
    elif choice == 2:
        column = NAME
    else:
        column = EPISODES

    show = ask_choice("Show the sorting process?", ["yes", "no"])
    show_process = (show == "yes")

    algoritma.selection_sort(data, column, show_process)
    print("\nSorted!")
    show_all(data)

    
    return column == NAME


def menu_statistics(data):
    print("\n=== Statistics ===")
    print("1. Total episodes of all anime")
    print("2. Total finished anime")
    print("3. Total watching anime")
    print("4. Average rating")
    print("5. Show all")
    choice = ask_int("Choose", 1, 5)
    print()

    if choice == 1 or choice == 5:
        print("Total episodes   :", statistik.total_episodes(data))
    if choice == 2 or choice == 5:
        print("Total finished   :", statistik.count_watch_status(data, "finished"))
    if choice == 3 or choice == 5:
        print("Total watching   :", statistik.count_watch_status(data, "watching"))
    if choice == 4 or choice == 5:
        print(f"Average rating   : {statistik.average_rating(data):.2f}/10")


def main():
    data = storage.load_data()
    sorted_by_name = False  

    while True:
        print("\n===== ANIME TRACKER =====")
        print("1. Show all anime")
        print("2. Add")
        print("3. Edit")
        print("4. Delete")
        print("5. Search")
        print("6. Sort")
        print("7. Statistics")
        print("0. Exit")
        choice = ask_int("Choose a menu", 0, 7)

        if choice == 1:
            show_all(data)

        elif choice == 2:
            add_anime(data)
            sorted_by_name = False   
            storage.save_data(data)

        elif choice == 3:
            name_changed = edit_anime(data)
            if name_changed:
                sorted_by_name = False
            storage.save_data(data)

        elif choice == 4:
            deleted = delete_anime(data)
            if deleted:
                sorted_by_name = False
                storage.save_data(data)

        elif choice == 5:
            menu_search(data, sorted_by_name)

        elif choice == 6:
            sorted_by_name = menu_sort(data)
            storage.save_data(data)

        elif choice == 7:
            menu_statistics(data)

        else:
            print("Goodbye!")
            break


main()