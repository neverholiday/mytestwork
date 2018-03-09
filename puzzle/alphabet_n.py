import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--input",help = "Width_and_Height",required = True)
args = vars(ap.parse_args())

rows = int(args["input"])
columns = int(args["input"])


for row in range(rows):
    n_alplabet = ""
    for col in range(columns):
        if col == 0 or col == columns-1:
            n_alplabet = n_alplabet + "x"
        
        elif col == row:
            n_alplabet = n_alplabet + "x"

        else:
            n_alplabet = n_alplabet + " "
    print n_alplabet
        
