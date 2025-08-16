
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#
# 3. Add one new pet if there’s room on the bus.  
#    - Use MAX_SEATS to limit capacity.  
#    - Dynamically assign the next seat number.  
#    - Print the updated roster showing all pets after pickup.  
#
# 4. Ask which pet leaves early.  
#    - Remove that pet from the bus.  
#    - Print a message saying they’ve headed home.  
#
# 5. Print a final roster listing the remaining pets and their dropoff times.
# def main():
dict1={
    'name': 'Jhon',
    'breed':'golden retriver',
    'pickup time':12,
    'dropoff time': 12,
}
dict2={
    'name': 'Charles',
    'breed':'pitbull',
    'pickup time':12,
    'dropoff time': 12,
}
dict3={
    'name': 'Hienz',
    'breed':'german shepard',
    'pickup time':12,
    'dropoff time': 12,
}
maindict={
    list(dict1.values())[0] : 1,
    list(dict2.values())[0] : 2,
    list(dict3.values())[0] : 3,
    }

# {'name': 'Jhon', 'breed': 'golden retriver', 'pickup time': 12, 'dropoff time': 12}
# {'name': 'Charles', 'breed': 'pitbull', 'pickup time': 12, 'dropoff time': 12}
# {'name': 'Hienz', 'breed': 'german shepard', 'pickup time': 12, 'dropoff time': 12}
# {'Jhon': 1, 'Charles': 2, 'Hienz': 3}

#========================= Implementation 1 =========================#
# for i in dict1, dict2, dict3:
#     print(f"""
#         Name        : {i['name']}
#         Pickup Time : {i['pickup time']}
#         Seat Number : {maindict[i['name']]}
#     """)
#---------------------------------------------------------------------

#========================= Implementation 2 =========================#
# super_dict = {}
# counter = 1

# for i in dict1, dict2, dict3, maindict:
#     super_dict[counter] = i
#     counter += 1

# for i in range(1, 4):
#     print(f"""
#     Name        : {super_dict[i]['name']}
#     Pickup Time : {super_dict[i]['pickup time']}
#     Seat Number : {super_dict[4][super_dict[i]['name']]}
#     """)

#========================= Implementation 3 =========================#
# bus = {
#   1: {"name": "Milo", "breed": "Labrador", "pickup": "8:00 AM", "dropoff": "4:00 PM"},
#   2: {"name": "Otis", "breed": "French Bulldog", "pickup": "8:15 AM", "dropoff": "4:15 PM"},
#   3: {"name": "Willow", "breed": "Border Collie", "pickup": "8:30 AM", "dropoff": "4:30 PM"},
# }

# print("-- Starting roster --")
# for seat, info in bus.items():
#   print(f"Seat {seat}: {info['name']} (pickup {info['pickup']})")


#----------------------Local & Global Variables------------------------------#
# b = 0
# def sum(a):
#     # print(a + b)
#     b = 6
#     a = a + b
#     return a

# def mul(n):
#     return n * b

# print(sum(3), mul(5))

