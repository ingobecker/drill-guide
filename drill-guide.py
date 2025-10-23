#!/usr/bin/env python3

import argparse
import math

clamp_long_bolt_to_end = 94.5
top_bolt_to_hole = 38.747

ap = argparse.ArgumentParser(description='Helps to align the tool to drill a hole at a specified distance from the edge.')
ap.add_argument('-m', '--material', type=float, required=True, help='thinkness of the material used in mm')
ap.add_argument('-d', '--distance', type=float, required=True, help='distance of the hole from the edge in mm')

args = ap.parse_args()

material_thickness = args.material
distance = args.distance

tri_c = top_bolt_to_hole
tri_b = material_thickness / 2.0 + 6

tri_a = math.sqrt((tri_c ** 2) - (tri_b ** 2))

mark_distance = distance + (clamp_long_bolt_to_end - tri_a)
mark_distance = round(mark_distance, 1)

print("Material thickness: {}, Hole distance from edge: {}".format(material_thickness, distance))
print("Alignment mark: {} mm".format(mark_distance))
