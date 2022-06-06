import monero

from monero.seed import Seed


# Generating from dice rolls. This is simulated dice rolls
import random
import hashlib


dice_rolls = ""

for i in range(0,99):
    #This is not truly random. This is to simulate dicerolls
    #DONT USE IN PROD
    dice_rolls += str(random.randint(0,5))

#Generated 32 bytes of entropy
entropy_bytes = hashlib.sha256(dice_rolls.encode()).digest()

hex = entropy_bytes

hex = hex.hex()
s = Seed(hex)
phrase = s.phrase

print(f"The seed Phrase:")
print(f"{phrase}")
