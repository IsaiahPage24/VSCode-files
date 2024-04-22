# 1. Name:
#      Isaiah Page
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      The program uses a json file with a list of usernames and passwords to verify the user's identity and grant access.
# 4. What was the hardest part? Be as specific as possible.
#      The most difficult part by far was incorporating the json file into my program. I remembered how to access the file, and did a lot of research on json files,
#       but for some reason I was assuming I needed to take the file, load it into python, and then create a new dictionary within my program itself in order to use the data.
#       So I was trying to split the lists and loop through to add them to two separate lists. After a while, I reread some material online and realized that
#       once I loaded in the json info that it was already accessible and I didn't have to take any further measures. After I figured that out, the rest was relatively simple.
# 5. How long did it take for you to complete the assignment?
#      Close to 4 hours.

import json

def main():
    file_accessed = False
    try:
        with open("CSE130/Lab02.json") as list_file :
            references = json.load(list_file)
            file_accessed = True
    except FileNotFoundError:
        print("Unable to open file Lab02.json.")


    if file_accessed:
        username = input("Username: ")
        password = input("Password: ")
        check1 = False
        check2 = False

        for i in references['username']:
            if i == username:
                check1 = True

        for i in references['password']:
            if i == password:
                check2 = True

        if check1 and check2:
            print("You are authenticated!")
        else:
            print("You are not authorized to use the system.")


if __name__ == "__main__":
    main()