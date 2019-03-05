def Game(Alex,Lee,piles):
    if piles:
        Alex1 = Alex + piles[0]
        Lee1 = Lee + piles[-1]
        if Game(Alex1,Lee1,piles[1:len(piles)-1]):
            return True

        Alex2 = Alex + piles[-1]
        Lee2 = Lee + piles[0]
        if Game(Alex2,Lee2,piles[1:len(piles)-1]):
            return True
    else:
        if Alex > Lee:
            return True
        else:
            return False

piles = [5,3,4,5]
print(Game(0,0,piles))
