def polishnotation(ops : list ) -> int:
    numbers = []
    snj = ["+", "-", "*", "/"]
    for each in ops:
        if each not in snj:
            numbers.append(int(each))
        else:
            if len(numbers) < 2:
                return False 
            a = numbers.pop()
            b = numbers.pop()
            if each == "+":
                numbers.append(b+a)
            elif each == "-":
                numbers.append(b-a)
            elif each == "*":
                numbers.append(b*a)
            else:
                numbers.append( b//a)
    return (numbers[0])

print(polishnotation(["1","2","+","3","*","4","-"]))
print(polishnotation(["2", "1", "+"]))
print(polishnotation(["2", "1", "+", "3", "*"]))       # Expected: 9
print(polishnotation(["4", "13", "5", "/", "+"]))      # Expected: 6
print(polishnotation(["10", "6", "9", "3", "/", "-", "*"]))  # Expected: 30
print(polishnotation(["3", "4", "+", "2", "*", "7", "/"]))   # Expected: 2
print(polishnotation(["5", "1", "2", "+", "4", "*", "+", "3", "-"]))  # Expected: 14
print(polishnotation(["2", "3", "*", "4", "+"]))       # Expected: 10
print(polishnotation(["4", "2", "/", "3", "-"]))       # Expected: -1
print(polishnotation(["7", "2", "/", "3", "/"]))       # Expected: 1
print(polishnotation(["3", "-4", "+"]))                # Expected: -1
print(polishnotation(["5", "6", "*"]))                 # Expected: 30

