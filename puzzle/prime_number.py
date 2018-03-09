import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--input",help="input lenght of prime number",required=True)
args = vars(ap.parse_args())
input_number = int(args["input"])

def check_prime_number(number):
    count_prime = 0
    for num in range(1,number+1):
        if number%num == 0:
            count_prime = count_prime + 1
    if count_prime == 2:
        return True
    else:
        return False

list_number = range(1,input_number+1)
count_prime_number_total = 0

for num in list_number:
    status = check_prime_number(num)
    if(status):
        count_prime_number_total = count_prime_number_total + 1

print "Total of prime number is " + str(count_prime_number_total)

