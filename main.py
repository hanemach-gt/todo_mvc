from todolist import *


def print_menu(options):
    print("\n Please choose an option by typing an ordinal.\n")
    for i, opt in enumerate(options):
        print(" " + str(i+1), opt)
    print()


def get_string_from_input(prompt, max_len):
    in_str = ""
    while not in_str or len(in_str) > max_len:
        in_str = input(prompt)

    return in_str


def get_item_name_from_input():
    return get_string_from_input(" Please provide task name (max. 20 chars): ", 20)


def get_item_description_from_input():
    return get_string_from_input(" Please provide task description (max. 150 chars): ", 150)


def item_addition_handler(todolist):
    name = get_item_name_from_input()
    desc = get_item_description_from_input()
    todolist.add_item(name, desc)
    print(" Item added")


def grab_todolist_item_index_from_input(todolist):
    ordinal = None
    while True:
        try:
            ordinal = int(input("\nChoose item id: "))
        except ValueError:
            print(" Invalid input")
        else:
            if ordinal - 1 not in range(0, len(todolist.items)):
                print(" Input out of range")
            else:
                break
    return ordinal - 1


def item_deletion_handler(todolist):
    if not todolist.items:
        print(" The todo list is empty")
        return

    todolist.display_todolist()
    index = grab_todolist_item_index_from_input(todolist)
    todolist.delete_item(index)
    print(" Deleted item")


def item_modification_handler(todolist):
    if not todolist.items:
        print(" The todo list is empty")
        return

    todolist.display_todolist()
    index = grab_todolist_item_index_from_input(todolist)
    ans = ""
    while True:
        ans = input(" Write N for changing item name, D for changing its description: ")
        if ans.lower() == "n" or ans.lower() == "d":
            break

    if ans.lower() == "n":
        name = get_item_name_from_input()
        todolist.items[index].set_name(name)
        print(" Item name updated")
    else:
        desc = get_item_description_from_input()
        todolist.items[index].set_desc(desc)
        print(" Item description updated")


def item_marking_handler(todolist):
    if not todolist.items:
        print(" The todo list is empty")
        return

    todolist.display_todolist()
    index = grab_todolist_item_index_from_input(todolist)
    todolist.mark_item_as_done(index)
    print(" Marked item as done")


def item_displaying_handler(todolist):
    if not todolist.items:
        print(" The todo list is empty")
        return

    todolist.display_todolist()
    index = grab_todolist_item_index_from_input(todolist)
    todolist.display_todoitem_by_id(index)


def main():
    operations = ("Add todo item", "Modify existing item", "Delete item",
                  "Mark item as done", "Display todo list", "Display item by id",
                  "exit")

    todolist = TodoList()

    while True:
        print_menu(operations)
        # get option from input
        ordinal = None
        while True:
            try:
                ordinal = int(input("\nChoose operation: "))
            except ValueError:
                print(" Invalid input")
            else:
                if ordinal - 1 not in range(0, len(operations)):
                    print(" Input out of range")
                else:
                    break
        # examine input
        index = ordinal - 1
        if index == operations.index("Add todo item"):
            item_addition_handler(todolist)

        elif index == operations.index("Modify existing item"):
            item_modification_handler(todolist)

        elif index == operations.index("Delete item"):
            item_deletion_handler(todolist)

        elif index == operations.index("Mark item as done"):
            item_marking_handler(todolist)

        elif index == operations.index("Display todo list"):
            todolist.display_todolist()

        elif index == operations.index("Display item by id"):
            item_displaying_handler(todolist)

        elif index == operations.index("exit"):
            break


if __name__ == "__main__":
    main()
