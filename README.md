# Password Manager

This is a simple command-line password manager written in Python. It allows you to store and manage your website passwords securely. You can add, view, list, and delete passwords for different websites.

## Features

- Add a new password entry.
- View the username and password for a specific website.
- List all the websites for which you have stored passwords.
- Delete a password entry for a website.
- Save and load password data to/from a JSON file for persistence.

## Prerequisites

Before running the password manager, make sure you have Python installed on your system.

## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the repository directory in your terminal.

## Usage

To use the password manager, run the following command in your terminal:

```python
python password_manager.py
```

You will be presented with a menu of options:

- Enter `1` to add a new password.
- Enter `2` to view the username and password for a specific website.
- Enter `3` to list all the websites for which you have stored passwords.
- Enter `4` to delete a password entry for a website.
- Enter `5` to quit the program and save your password data to `passwords.json`.

Follow the on-screen prompts to interact with the password manager.

## Sample Usage

Here is a sample interaction with the password manager:

```plaintext
Options:
1. Add Password
2. View Password
3. List Websites
4. Delete Password
5. Quit
Enter your choice: 1
Enter the website: google
Enter the username: your_username
Enter the password: 12345678
Password added successfully!

Options:
1. Add Password
2. View Password
3. List Websites
4. Delete Password
5. Quit
Enter your choice: 2
Enter the website to view the password: google
Website: google
Username: your_username
Password: 12345678

Options:
1. Add Password
2. View Password
3. List Websites
4. Delete Password
5. Quit
Enter your choice: 3
Stored Websites:
example.com
anotherwebsite.com
google

Options:
1. Add Password
2. View Password
3. List Websites
4. Delete Password
5. Quit
Enter your choice: 4
Enter the website to delete the password: google
Password deleted successfully!

Options:
1. Add Password
2. View Password
3. List Websites
4. Delete Password
5. Quit
Enter your choice: 5
```

## Data Storage

The password data is stored in a JSON file named `passwords.json`. You can manually edit this file if needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This password manager was created as a simple project to practice Python programming.
- Feel free to contribute to the project or use it as a starting point for your own password manager.

## Author

Farheen Fathima

## Contact

For any questions or issues, please contact farheennfathima@gmail.com
