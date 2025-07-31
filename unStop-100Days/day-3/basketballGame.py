def basketBallGame (ops : str) -> int:
    scoreBoard = []
    opsTokens = ops.split(" ")
    def isScore (value):
        try:
            int(value)
            return True
        except ValueError:
            return False
        
    # print(opsTokens)
    for each in opsTokens:
        if each == " ":
            continue

        
        if isScore(each):
            scoreBoard.append(int(each))
        else :
            if each == "+":
                scoreBoard.append(scoreBoard[-1] + scoreBoard[-2])
            elif each == "C":
                scoreBoard.pop() 
            elif each == "D":
                scoreBoard.append(scoreBoard[-1] * 2)
            else:
                pass

    return sum(scoreBoard)

print(basketBallGame("1 2 + C D 8 D +"))
print(basketBallGame("15788 25148 -24609 24869 D -23282 14614 -2921 C -26517 1891 C -18324 + + -23184 D -12585 C D 7308 -11988 -16148 + 8834 + + D 19519 + 11289 + D C -13033 D + -278 -14043 0"))
print(basketBallGame("15788 25148 -24609 24869 D -23282 14614 -2921 C -26517 1891 C -18324 + + -23184 D -12585 C D 7308 -11988 -16148 + 8834 + + D 19519 + 11289 + D C -13033 D + -278 -14043 C -906 C 28518 C -29295 "))