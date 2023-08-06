# Python_Package

This is a simple Python script that generates random passwords of varying lengths. The generated passwords include at least one lowercase letter, one uppercase letter, and one number to enhance security.
Usage

To use this password generator, you need to call the gen_pass() function. It will return a randomly generated password based on the provided length.

python

import random
import string

def gen_pass():
    # Function code here

# Example usage:
password = gen_pass()
print(password)

How It Works

    The gen_pass() function generates a random password with a length between 5 and 10 characters.

    It uses the random module to choose the password's length randomly.

    The password is constructed by randomly selecting one lowercase letter, one uppercase letter, and one number to ensure a mix of characters.

    The remaining characters are filled with random choices from lowercase letters, uppercase letters, and numbers.

    Finally, the password is shuffled to create a more random arrangement of characters.

Dependencies

    None. This script only relies on Python's built-in random and string modules.

Contributing

If you find any issues or have suggestions for improvements, feel free to create a pull request or open an issue. Your contributions are highly appreciated!
License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as per the terms of this license.
