import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--radius",required=True)
args = vars(ap.parse_args())

def area_of_circle(radius):
    area = np.pi * radius * radius
    return area

def area_of_taxi(radius):
    area = (radius + radius)*radius
    return area

radius = int(args["radius"])
area_circle = area_of_circle(radius)
area_taxi = area_of_taxi(radius)

print area_circle
print area_taxi
