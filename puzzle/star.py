import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--input",required=True)
args = vars(ap.parse_args())

def check_odd_even(num):
    if num%2 == 0:
        return True
    else:
        return False

def pattern_star(num):
    
    center = num/2
    result = [n for n in range(center)]
    if(check_odd_even(num)):
        for i in list(reversed(result)):
            result.append(i)
    else:
        result.append(result[-1]+1)
        for i in list(reversed(result)):
            if(not(i == result[-1])):
                result.append(i)
        
    return result


number = int(args["input"])
number_star = 0
if check_odd_even(number):
    print "Even"
    number_star = number - 1
else:
    print "Odd"
    number_star = number

char = ""
pattern = pattern_star(number)
center = number_star/2
print pattern
for i in pattern:
    if(i == 0):
        for j in range(number_star):
            if(j == (number_star)/2):
                char = char + "*"
            else:
                char = char + "-"
    else:
        for j in range(number_star):
            if(j == center - i or j == center + i):
                char = char + "*"
            else:
                char = char + "-"
        

    print char
    char = ""

