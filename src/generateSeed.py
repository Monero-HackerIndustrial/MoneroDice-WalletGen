# import monero

from monero.seed import Seed


# Generating from dice rolls. This is simulated dice rolls
# import random
import hashlib

TERMWIDTH = 80
LINEBREAK = '-' * TERMWIDTH
LINEBREAK2 = '_' * TERMWIDTH
VERSION = 0.1
dice_rolls = ""
index = 0
#flip debug for testing. This hardcodes the seed as "1" for every roll. Only for testing
DEBUG = False


def breakLine():
    print(f"{LINEBREAK2}")

def banner():
    print()
    print(f"Welcome to MoneroDice-WalletGen version:{VERSION}")
    print(f"{LINEBREAK}")
    print(f"The script requires you to roll a 6 sided dice 100 times.")
    print(f"Don't worry the following prompt will walk you through each step")
    print(f"{LINEBREAK}")
    _start = input("Are you ready to begin? Y/N: ")
    print(f"{LINEBREAK}")
    if _start.lower() == "y":
        return True
    else:
        return False

def verifyRange(_roll):
    try:
        _roll = int(_roll)
        if 1 <= _roll <= 6:
            return True
        else:
            False
    except:
        return False

def getUserRoll(_index):
    while True:
        _roll = input(f"What is value (1-6) of your dice roll? [roll #: {_index + 1}/100]: ").strip()
        if verifyRange(_roll):
            break
        else:
            print(f"wrong input, please only submit a number between 1-6. Try again")
    return _roll


start = banner()


if not start:
    print("Program exiting... ")
    quit()

print("Let's generate entropy with dice!")


while index < 100:
    if DEBUG:
        roll = "1"
    else:
        roll = getUserRoll(index)
    dice_rolls += roll
    index += 1

print(f"Finished generating your entropy.")

input("Ready to print your Monero seed. Please press any key to continue: ")

#Generated 32 bytes of entropy
entropy_bytes = hashlib.sha256(dice_rolls.encode()).digest()

hex = entropy_bytes

hex = hex.hex()
s = Seed(hex)
phrase = s.phrase
public_address = s.public_address()


breakLine()
print(f"The seed Phrase:")
print(f"{phrase}")

breakLine()
print(f"The PUBLIC ADDRESS:")
print(f"{public_address}")


breakLine()
print()
