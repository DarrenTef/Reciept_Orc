import re
# Goal is to parse the words from result.txt
# Problem: 
# Given an input of two lists where one is an item and the other is the amount with name[i] associated with amount[i]
# Make it so that if we input a list of people and associate items to each sets of people. Allowing us to evenly
# Divide the costs among different groups.

# input of people
def get_people():
    people = []
    person = input("Please state people of your party; type done if finished: \n")
    while person != "done":
        people.append(person)
        person = input(f"{people}\n")
    return people

# Extracts data from result.txt as an array of lines
# The input must be of 2 verticle columns, where the first column is a description of the item, and the second column is prices
def extract_data_from_file(file_path):
    item_dict = {}
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

        for line in lines:
            parts = line.split()
            description = ' '.join(parts[:-1])
            amount = float(parts[-1])
            item_dict[description] = amount
    except FileNotFoundError:
        print(f"{file_path} does not exist")
    
    except Exception as e:
        print(f"Error reading file: {e}")

    return item_dict

# Given a list of people, a dictionary with key = description and value = amount we want to return a dictionary where:
# items will be the keys and people will be the value
# def assign_people_to_items(people_list, items_dict):
#     assignment = {}

#     for item in description_amount:
#         item[0] = []
#         print(f"Who wanted the {item[0]} which costs {item[1]}")
#         survey = input("Please put all names on a newline or type all for everyone")
#         while survey != "all":
            
            


        




# Now I have the number of people, and their names and also the number of items and their amounts
# Solutions:
# 1) For every item, label it with all the people who want it and divide item cost by people // Time = O(people * items) = O(n^2) Space O(people * items) = O(n^2)
# For every person see who wants it O(n)


# Space complexity: O(people * items) = O(n^2)



# for description, amount in zip(descriptions, amounts):
#     print(f"{description.ljust(20)} {str(amount).rjust(10)}\n")