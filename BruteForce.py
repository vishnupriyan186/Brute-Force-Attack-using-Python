import pyautogui
import itertools
import string


password = pyautogui.password("Enter the password here:")


character_set = string.ascii_lowercase + string.digits


def brute_force(password):
   
    for length in range(1, len(password) + 1):
        for guess in itertools.product(character_set, repeat=length):
            guess_password = ''.join(guess)
            print(f"Trying password: {guess_password}")
            
            if guess_password == password:
                return guess_password


found_password = brute_force(password)
if found_password:
    print(f"Your password is: {found_password}")
else:
    print("Failed to find the password.")
