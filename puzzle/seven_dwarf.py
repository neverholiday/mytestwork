import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--input",help = "each number are seperated by comma",required=True)
args = vars(ap.parse_args())

number_of_dwarfs = args["input"].split(",")
number_of_dwarfs = [int(n) for n in number_of_dwarfs]

print number_of_dwarfs

temp_sum = 0
confirm_dwarfs = []
first_group = number_of_dwarfs[0:len(number_of_dwarfs)-2]
second_group = [number_of_dwarfs[len(number_of_dwarfs)-2],number_of_dwarfs[len(number_of_dwarfs) - 1]]

for sec in second_group:
    for i in range(len(first_group)):
        temp_sum = sum(first_group) - first_group[i]
        temp_sum = temp_sum + sec
        if(temp_sum == 100):
            confirm_dwarfs = first_group
            confirm_dwarfs.pop(i)
            confirm_dwarfs.append(sec)
    temp_sum = 0
    
print confirm_dwarfs