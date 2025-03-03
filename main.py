# This lists will invite 6 pepole to dinner and of them would not be able to make it so also need to send request to someone else


# Create a function to print invitations 
def send_invitations(guests_list):

    """Prints personalized invitation messages for each guests."""

    print("\nDinner Invitations: ")
    for guest in guests_list:
        print(f"Dear {guest}, you are invited to the dinner party! ")

# Greet the user
print("Welcome to the dinner inviting program! ")

# Ask the user how many people they want to invite
while True:
    try:
        num_guests = int(input("How many people do you want to invite to the dinner party?: "))
        if num_guests > 0:
            break
        else:
            print("Please enter the number of the people who you want to invite. ")
    expect ValueError:
        print("Invalid input. Please enter a valid number. ")
    
# list for the names of the guests.
guests = [] 

# loop for the guest names
for i in range(num_guests):
    while True:
        try:
            name = input(f"Enter the name of guests {i+1}: ").strip()
            if name:
                guests.append(name) # this is to append the guests name
                break
            else:
                print("Name cannot be empty. Please evter a valid name. ")
        except EOFError:
            print("Invalid input! ")
            name = f"Guest{i+1}"
            guests.append(name)
            break

# Print a letter for each of them 
send_invitations(guests)

# Ask the user if they want to add or remove anyone from the invitation
while True:
    try:
        replace = input("Do you want to replace a guest? [yes/no] ").strip().lower()
        if replace in ["yes", "no"]:
            break
        else:
            print("Invalid input! Please enter 'yes or 'no' ")
    except EOFError:
        print("Invalid input! ") 
        replace = 'no'
        break

# replace a guest if the user wants to
if replace == "yes":
    while True:
        try:
            old_guest = input("Enter the name of the huest to replace: ").strip()
            if old_guest in guests:
                new_guest = input("Enter the name of the new guest: ").strip()
                if new_guest:
                    guests[guests.index(old_guest)] = new_guest #this replaces the old guest with the old one.
                    break
                else:
                    print("New guest name cannot be empty. Try again. ")
            else:
                print(f"{old_guest} is not in the guest list. Try again. ")
        except EOFError:
            print("Input is not available. ")
            break

# list the guests invitation in alphabetic order
guests.sort()
send_invitations(guests)

# print the total number of the guests.
print(f"Total number of the guests invited: {len(guests)}")








