def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks -1, startPeg, 6 - startPeg - endPeg)
        print(startPeg, "th peg's", ndisks, "th disk move to ", endPeg, "th peg")
        hanoi(ndisks -1, 6 - startPeg - endPeg, endPeg)
hanoi(ndisks=3)

