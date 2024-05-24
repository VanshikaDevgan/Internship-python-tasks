def remove_common_characters(name1, name2):
    name1_list = list(name1)
    name2_list = list(name2)
    
    for char in name1:
        if char in name2_list:
            name1_list.remove(char)
            name2_list.remove(char)
    
    return name1_list, name2_list

def flames_count(name1_list, name2_list):
    count = len(name1_list) + len(name2_list)
    return count

def get_flames_result(count):
    flames = ["F", "L", "A", "M", "E", "S"]
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    
    return flames[0]

def get_relationship(flames_result):
    relationships = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }
    return relationships[flames_result]

def flames_game(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    name1_list, name2_list = remove_common_characters(name1, name2)
    count = flames_count(name1_list, name2_list)
    flames_result = get_flames_result(count)
    
    relationship = get_relationship(flames_result)
    return relationship

# Input names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Get and print the relationship result
result = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")
