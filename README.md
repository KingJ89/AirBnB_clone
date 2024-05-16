# hbnb Console Application

This is a command-line interface (CLI) application for managing users.

## Features

- Create a new user
- Read user details by ID
- Update an existing user
- Delete a user by ID

## Usage

1. Clone the repository:


4. Follow the on-screen instructions to interact with the console.

## Commands

- `create_user <id> <name> <email>`: Create a new user.
- `read_user <id>`: Read user details by ID.
- `update_user <id> <name> <email>`: Update an existing user.
- `delete_user <id>`: Delete a user by ID.
- `quit`: Exit the console.

## Testing

To run the tests, execute the following command:

1. Creating a User

To create a new user, use the create_user command followed by the user's ID, name, and email address. For example:

ruby

$ create_user 1 John john@example.com
User created successfully.

2. Reading User Details

To read user details by their ID, use the read_user command followed by the user's ID. For example:

yaml

$ read_user 1
ID: 1, Name: John, Email: john@example.com

3. Updating a User

To update an existing user, use the update_user command followed by the user's ID, new name, and new email address. For example:

ruby

$ update_user 1 Jane jane@example.com
User updated successfully.

4. Deleting a User

To delete a user by their ID, use the delete_user command followed by the user's ID. For example:

ruby

$ delete_user 1
User deleted successfully.

5. Quitting the Console

To exit the console, simply type quit:

ruby

$ quit

