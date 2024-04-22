import json

def find_subarray_with_highest_average(array, length):
    """
    Will find the subarray within an array that has the highest average value.
    (Can be adapted to also return the subarray itself)

    Args:
        array, length of subarray

    Returns:
        Highest average value
    """

    assert isinstance(array, list), "Input array must be a list"
    assert all(isinstance(x, int) for x in array), "Input array must contain only integers"

    # Set low max and empty target subarray
    max_average = -100
    subarray_with_max_average = []

    # iterate through array finding subarray with highest average value.
    for i in range(len(array) - length):
        subarray = array[i: i+length]
        average = sum(subarray) / length

        if average > max_average: # Set the new max average and save that subarray
            max_average = average
            subarray_with_max_average = subarray
    
    return max_average

def main():

    try: # Get array from json file
        
        file_name = input("What is the name of the file holding an array?\n")

        with open(file_name) as file:
            data = json.load(file)

        # Check if file has an array.
        if not isinstance(data, dict) or "array" not in data:
            raise ValueError("File does not contain 'array' key or is not in JSON format.")

        array = data["array"]

        # Check is array is a list of integers.
        if not isinstance(array, list) or not all(isinstance(x, int) for x in array):
            raise ValueError("The value associated with 'array' key is not a list of integers.")

    except FileNotFoundError:
        print(f"Cannot find file: '{file_name}'.")
        return
    except ValueError:
        print(f"Error reading file: {ValueError}")
        return

    length_of_subarray = int(input("What is the size of the sub-array?\n"))
    while length_of_subarray > len(array):
        length_of_subarray = int(input("You have entered sub-array size greater than the size of the array\nWhat is the size of the sub-array?\n"))
    
    assert length_of_subarray <= len(array), "Sub-array size must be less than or equal to the size of the array"

    print(f"The highest average of subarray of {length_of_subarray} is: {find_subarray_with_highest_average(array, length_of_subarray)}")

if __name__ == "__main__":
    main()

