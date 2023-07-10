# Kivy Login App

This is a simple login app developed using the Kivy framework. The app allows users to sign up, log in, and view quotes based on their feelings. The app utilizes JSON files to store user information and quote data.

## Installation

1. Make sure you have Python installed (version 3.7 or higher).
2. Install the required dependencies by running the following command:
   ```
   pip install kivy
   ```

## Usage

1. Clone the repository or download the source code files.
2. Navigate to the project directory.
3. Run the `main.py` file using Python:
   ```
   python main.py
   ```
4. The login app will be launched.
5. You can sign up by clicking the "Sign Up" button and providing a username and password.
6. After signing up, you can log in with your credentials on the login screen.
7. Upon successful login, you will be redirected to the login success screen.
8. On the login success screen, you can click the "Log Out" button to return to the login screen.
9. Additionally, you can enter a feeling in the text input and click the "Get Quote" button to display a random quote related to the entered feeling.

## File Structure

- `main.py`: The main Python file that launches the Kivy app and sets up the screens.
- `design.kv`: The Kivy language file containing the design layout of the app screens.
- `users.json`: A JSON file used to store user information (username, password, and creation date).
- `quotes/`: A directory containing text files with quotes categorized by feelings.

## Screens

The app consists of the following screens:

- Login Screen: Allows users to log in or navigate to the sign-up screen.
- Sign Up Screen: Allows users to create a new account.
- Sign Up Success Screen: Shown after successful account creation, provides an option to navigate back to the login screen.
- Login Success Screen: Shown after successful login, provides options to log out or get a random quote based on a feeling.

## Custom Widgets

- `ImageButton`: A custom widget that combines the behaviors of `ButtonBehavior` and `HoverBehavior` with an `Image` widget.
