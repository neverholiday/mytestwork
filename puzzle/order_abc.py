import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--input",required=True)

args = vars(ap.parse_args())


ball = [1,0,0]
order_abc = args["input"]

for alpha in order_abc:
    temp_ball = 0
    if(alpha == "A" or alpha == "a"):
        ball[0] , ball[1] = ball[1] , ball[0]
    elif(alpha == "B" or alpha == "b"):
        ball[1],ball[2] = ball[2] , ball[1]
    elif(alpha == "C" or alpha == "c"):
        ball[0] , ball[2] = ball[2],ball[0]

print ball
