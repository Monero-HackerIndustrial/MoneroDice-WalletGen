# MoneroDice-WalletGen
A Monero Diceware seed generator. Generate Monero wallet seeds by rolling dice. Can be used offline.


## New UI
![moneroDice2-1](https://user-images.githubusercontent.com/106575456/173973660-40559fa4-4e73-4937-90d1-c8c1c2bfc486.png)
### Now outputs public base address:
![moneroDice2](https://user-images.githubusercontent.com/106575456/173973687-8b94642e-f2bb-4d52-b921-87a86385dc83.png)




## Requirements

The script currently requires the following python packages :
- monero
- hashlib

In a future version I would look into creating a portable version that doesn't require any external requirements.


## How to use


To use the script you will need one 6-sided dice. The dice is used as a form of entropy for the random hex that the seed is generated from.
run:
`
python3 generateSeed.py
`

The script will ask you to roll a dice an input the roll. For proper entropy the script takes 100 rolls. After rolling 100 rolls the output will be a 25 word Monero seed. This seed can be used with official Monero GUI or wallet. 


## Entropy 
The script generates 100 dice rolls for a little bit over 256 bit entropy. 

Based on some Math from coldcard, a d6 dice provides 2.585 bits of additional entropy per roll
This means:
50 rolls for 128 bit
99 rolls for 256 bit
