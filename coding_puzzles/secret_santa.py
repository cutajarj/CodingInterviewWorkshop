import random


# Your friends have decided to have a secret santa gift scheme this Christmas.
# This is when all your colleagues and yourselves write their names in a small piece of paper,
# then you all put the names in a hat. Every person then picks a name from the hat and buys a small gift to that person.
# Your task is two write this algorithm, so that we don't waste paper.
# Implement a function that accepts a list of names and outputs a random pairing,
# of whose buying a Christmas present to whom.
# Everyone should buy and receive only one gift from a person that is not him/herself.
#
# gift_paring(["James", "Ruth", "Isabel"]) can return [("Ruth", "James"), ("James", "Isabel"), ("Isabel", "Ruth")]
# Assume that there will be at least 2 names in the list
# Assume that all names are unique too
def gift_paring(names):
    result = []
    random.shuffle(names)
    for i in range(len(names)):
        pair = names[i], names[(i + 1) % len(names)]
        result.append(pair)
    return result


if __name__ == '__main__':
    print(gift_paring(["James", "Ruth", "Isabel", "Michael", "Luis", "Oliver"]))

