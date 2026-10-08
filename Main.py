import storage
import statistik
import algoritma
from anime import (NAME, EPISODES, RATING, RELEASE, WATCH,
                   RELEASE_OPTIONS, WATCH_OPTIONS,
                   ask_text, ask_int, ask_choice,
                   show_all, show_rows,
                   add_anime, edit_anime, delete_anime)


def menu_search(data):
    print("\n=== Search (linear search) ===")
    print("1. Release status")
    print("2. Watch status")
    print("3. Name")
    choice = ask_int("Choose", 1, 3)

    if choice == 1:
        value = ask_choice("Release status:", RELEASE_OPTIONS)
        result = algoritma.linear_search(data, RELEASE, value)
    elif choice == 2:
        value = ask_choice("Watch status:", WATCH_OPTIONS)
        result = algoritma.linear_search(data, WATCH, value)
    else:
        text = ask_text("Name to search")
        result = algoritma.linear_search_name(data, text)

    print("\nFound", len(result), "result(s).")
    show_rows(data, result)


def menu_sort(data):
    print("\n=== Sort (bubble sort, smallest to largest) ===")
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

    algoritma.bubble_sort(data, column, show_process)
    print("\nSorted!")
    show_all(data)


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
            storage.save_data(data)

        elif choice == 3:
            edit_anime(data)
            storage.save_data(data)

        elif choice == 4:
            deleted = delete_anime(data)
            if deleted:
                storage.save_data(data)

        elif choice == 5:
            menu_search(data)

        elif choice == 6:
            menu_sort(data)
            storage.save_data(data)

        elif choice == 7:
            menu_statistics(data)

        else:
            print("Goodbye!")
            break


main()