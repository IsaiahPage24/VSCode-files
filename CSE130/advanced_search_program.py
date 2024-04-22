# 1. Name:
#      Isaiah Page
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      The program will take a file name and a target name, open the file and use the array withing to find
#      out if the target is within the file or not.
# 4. Algorithmic Efficiency
#      The efficiency of this program is 0(log n). I figured this out by looking at the one loop in the function I created
#      and matching it to the criteria of a log n efficient program. I verified this by checking the math behind the iterations needed
#      for each file size. I found out that as the file size increased exponentially, the iterations increased less and less.
#      By looking at the relationship between the two, I was able to find out that it was exactly logorithmic.
#      I then used huge numbers to verify, like 3 million, 1 billion, and that was the final piece of evidence to show a logorithmic efficiency.
# 5. What was the hardest part? Be as specific as possible.
#      The programming of the function itself was extrememly easy thanks to last weeks assignment. The hardest part for me was getting
#      the correct file and then accessing the array. Our assignment two weeks ago was the first time I had worked on json files,
#      so I am grateful for the extra experience I'm getting now.
#      At first I was typing the file name in wrong, so that didn't help. But then, I just completely forgot to even
#      open the file at all. After I remembered to add with open(file) in main, I couldn't figure out how to use the array in the file. 
#      I was still using the file as the array to put in my function, and that treated it as if the word "array" itself was the list I needed.
#      Thanks to Google, I was able to find out what I was doing wrong and how to fix it.
# 6. How long did it take for you to complete the assignment?
#      It took me a little over 3 hours to complete this assignment.

import json

def main():
    file_name = input("What is the name of the file? ")
    item_desired = input("What is the name we are looking for? ")

    try: 
        with open(file_name) as file:
            data = json.load(file)

        array = data["array"]

        is_in_list(array, item_desired, file_name)

    except FileNotFoundError:
        print(f"Cannot find file: '{file_name}'.")


def is_in_list(arr, target, file_name):
    if len(arr) == 0:
        return print(f"{file_name} is empty.")
    
    # testing if the length of the arr is correct
    # print(len(arr))

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            print(f"We found {mid_val} in {file_name}.")
            return
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return print(f"We could not find {target} in {file_name}.")

if __name__ == "__main__":
    main()