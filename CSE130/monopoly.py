# 1. Name:
#      Isaiah Page
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      The program takes all of the monopoly rules into consideration to tell the user if they are able to purchase a hotel or not.
# 4. What was the hardest part? Be as specific as possible.
#      The most difficult part was actually last weeks assignment, which was creating a flowchart for the program.
#      I made several mistakes in the syntax of the flowchart, which I had to spend time this week fixing.
#      After I had a correct flowchart, however, I was able to do the coding relatively quickly. I was shocked
#      at how much of a difference having a flowchart of your program before coding it made.
# 5. How long did it take for you to complete the assignment?
#      In total, it took me 3 hours to complete this assignment. This includes reading the assignment and alterations to my
#      previous flowchart, as well as actually coding the program.

def main():
    while True:
        # if you have all of the green properties
        all_props = int(input("Do you own all of the green properties?\n1. Yes\n2. No\n\nPlease enter 1 or 2.\n"))
        if all_props == 2:
            print("You cannot purchase a hotel until you own all of the properties of a given color group.")
            return False
        # Are there any hotels for purchase
        hotel = int(input("\n\nIs there a hotel to purchase?\n1. Yes\n2. No\n\nPlease enter 1 or 2.\n"))
        if hotel == 2:
            print("There are no hotels available to purchase right now.")
            return False
        # How many houses are on each property
        pennsylvania_avenue = int(input("\n\nWhat is on Pennsylvania Avenue?\n0. Nothing\n1. One house\n2. Two houses\n3. Three houses\n4. Four houses\n5. A hotel\n\nPlease enter a number.\n"))
        if pennsylvania_avenue == 5:
            print("You cannot purchase a hotel if your property already has one.")
            return False
        north_carolina_avenue = int(input("\n\nWhat is on North Carolina Avenue?\n0. Nothing\n1. One house\n2. Two houses\n3. Three houses\n4. Four houses\n5. A hotel\n\nPlease enter a number.\n"))
        if north_carolina_avenue == 5:
            print("Swap North Carolina's hotel with four houses from Pennsylvania Avenue.")
            return False
        pacific_avenue = int(input("\n\nWhat is on Pacific Avenue?\n0. Nothing\n1. One house\n2. Two houses\n3. Three houses\n4. Four houses\n5. A hotel\n\nPlease enter a number.\n"))
        if pacific_avenue == 5:
            print("Swap Pacific Avenue's hotel with four houses from Pennsylvania Avenue.")
            return False
        # Calculating how many houses are needed to purchase to get a hotel
        houses_needed = 12 - (pennsylvania_avenue + north_carolina_avenue + pacific_avenue)
        # Are there enough houses to buy
        houses_available = int(input("\nHow many houses are there to purhase?\n\n"))
        if houses_needed > houses_available:
            print("There are not enough houses available for purchase at this time")
            return False
        # How much cash you have and if it is enough
        funds = int(input("\nHow much cash do you have to spend? Please answer in an integer. (i.e. 1600)\n\n"))
        cost = (houses_needed * 200) + 200
        if cost > funds:
            print("You do not have sufficient funds to purchase a hotel at this time.")
            return False
        # Returning the specific cases
        if houses_needed == 0:
            print(f"\nThis will cost ${cost}.\nPurchase one hotel.\nPlace the hotel on Pennsylvania Avenue and return its houses to the bank.")
        elif houses_needed > 0:
            if (north_carolina_avenue and pacific_avenue) < 5:
                print(f"\nThis will cost ${cost}\nPurchase 1 hotel and {houses_needed} houses.\nPut 1 hotel on Pennsylvania and return any houses to the bank.\nPut {4 - north_carolina_avenue} houses on North Carolina.\nPut {4 - pacific_avenue} houses on Pacific Avenue.")
                return False
            elif north_carolina_avenue < 5:
                print(f"\nThis will cost ${cost}\nPurchase 1 hotel and {houses_needed} houses.\nPut 1 hotel on Pennsylvania and return any houses to the bank.\nPut {4 - north_carolina_avenue} houses on North Carolina.")
                return False
            else:
                print(f"\nThis will cost ${cost}\nPurchase 1 hotel and {houses_needed} houses.\nPut 1 hotel on Pennsylvania and return any houses to the bank.\nPut {4 - pacific_avenue} houses on Pacific Avenue.")
                return False

if __name__ == "__main__":
    main()