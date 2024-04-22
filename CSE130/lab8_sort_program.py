# 1. Name:
#      Isaiah Page
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      The program asks for a file name, and then uses the array within the file
#      and sorts it. The sorted array is then printed to the terminal.
# 4. What was the hardest part? Be as specific as possible.
#      The most difficult part of this assignment was determining the assert statements possible and best
#      locations. Since I am new to assert statements, it was tempting to go gung-ho and put them
#      at every place I could. But after consideration, I realized most of it was unnecessary.
#      I ended up taking a long time deliberating, and did additional research and reread some of the textbook material.
#      That part was definitely the most difficult for me.
# 5. How long did it take for you to complete the assignment?
#      It took me around 3 hours.

import json

def main():
    # Get name of file from user
    file_name = input("What is the name of the file?\n")

    try: 
        with open(file_name) as file:   # Try to open the file and load the array
            loaded_file = json.load(file)

            array = loaded_file["array"]

        assert len(array) > 0, "Loaded array is empty"
        
        if len(array) == 1:
            print(f"The list only has one item:\n\t{array[0]}")
        else:
            sort_and_print_list(array)

    except FileNotFoundError:
        print(f"Cannot find file: '{file_name}'.")

def sort_and_print_list(array):

    Sorted_Array = []
    count = len(array) - 1

    while count >= 0:

        largest_item = array[count]

        for i in range(count, -1, -1):
            if array[i] > largest_item:
                largest_item = array[i]

        Sorted_Array.insert(0, largest_item)
        array.remove(largest_item)
        count -= 1

    assert len(Sorted_Array) >= 0, "The sorted array has a negative length"

    for item in Sorted_Array:
        print("\t", item)
    

if __name__ == "__main__":
    main()