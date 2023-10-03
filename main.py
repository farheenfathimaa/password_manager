import json

# Function to load passwords from a JSON file
def load_passwords(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save passwords to a JSON file
def save_passwords(filename, passwords):
    with open(filename, 'w') as file:
        json.dump(passwords, file, indent=4)

# Function to add a new password
def add_password(passwords, website, username, password):
    passwords[website] = {"Username": username, "Password": password}
    print("Password added successfully!")

# Function to view a password
def view_password(passwords, website):
    if website in passwords:
        username = passwords[website]["Username"]
        password = passwords[website]["Password"]
        print(f"Website: {website}")
        print(f"Username: {username}")
        print(f"Password: {password}")
    else:
        print("Website not found in the password manager.")

# Function to list all stored websites
def list_websites(passwords):
    if passwords:
        print("Stored Websites:")
        for website in passwords:
            print(website)
    else:
        print("No passwords stored.")

# Function to delete a password
def delete_password(passwords, website):
    if website in passwords:
        del passwords[website]
        print("Password deleted successfully!")
    else:
        print("Website not found in the password manager.")

# Main function
if __name__ == "__main__":
    password_file = "passwords.json"
    passwords = load_passwords(password_file)

    while True:
        print("\nOptions:")
        print("1. Add Password")
        print("2. View Password")
        print("3. List Websites")
        print("4. Delete Password")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            website = input("Enter the website: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            add_password(passwords, website, username, password)
        elif choice == '2':
            website = input("Enter the website to view the password: ")
            view_password(passwords, website)
        elif choice == '3':
            list_websites(passwords)
        elif choice == '4':
            website = input("Enter the website to delete the password: ")
            delete_password(passwords, website)
        elif choice == '5':
            save_passwords(password_file, passwords)
            break
        else:
            print("Invalid choice. Please try again.")
 


