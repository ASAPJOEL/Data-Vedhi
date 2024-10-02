# Create a list
my_list = []

# Append elements to the list
def to_append_list(element):
    my_list.append(element)
    print(f"Appended {element} to the list. Current list: {my_list}")

# Delete element from the list by value
def to_delete_from_list(element):
    if element in my_list:
        my_list.remove(element)
        print(f"Deleted {element} from the list. Current list: {my_list}")
    else:
        print(f"{element} not found in the list.")

# Example usage
append_to_list(10)
delete_from_list(20)

