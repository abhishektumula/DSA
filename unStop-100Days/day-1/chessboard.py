#https://unstop.com/code/challenge-assessment/250904?moduleId=372
# the aim is check wheather the mentioned box is either black or white ...
#
# chess grids are mentioned in alphabets on x axis and numbers in y -axis 
#

def checkChessBlock (position : str) -> str :
    pos1, pos2 = ord(position[0]) - ord("a"), int(position[1])
    return ((pos1 + pos2) % 2 == 0 )


a = 1
while a :
    n = input("Enter any position valid in the ChessBoard(a-h)(1-8): ")
    if checkChessBlock(n):
        print(f"{n} is White Block ..")
    else:
        print(f"{n} is Black Block ..")

    n = (input("do you want to check again..? (y/n)").lower())
    if n == "n":
        print(f"Exitng succesfully...")
        a = 0


