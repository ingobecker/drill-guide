#!/usr/bin/env python3

import argparse
import math

handle_edge_to_bolt = {'long': 94.5, 'short': 17}
top_bolt_to_hole = 38.747

ap = argparse.ArgumentParser(description='Helps to align the tool to drill a hole at a specified distance from the edge.')
ap.add_argument('-m', '--material', type=float, required=True, help='thickness of the material used in mm')
ap.add_argument('-d', '--distance', type=float, required=True, help='distance of the hole from the edge in mm')
ap.add_argument('-a', '--align', type=str, default='long', choices=['long', 'short'], help='handle to use for alignment')

args = ap.parse_args()

material_thickness = args.material
distance = args.distance
handle = args.align


tri_c = top_bolt_to_hole
tri_b = material_thickness / 2.0 + 6

tri_a = math.sqrt((tri_c ** 2) - (tri_b ** 2))

handle_alignment_dist = handle_edge_to_bolt[handle]
mark_distance = distance + abs(handle_alignment_dist - tri_a)
mark_distance = round(mark_distance, 1)

print("Material thickness: {} mm, Hole distance from edge: {} mm".format(material_thickness, distance))
print("Alignment mark ({} handle): {} mm".format(handle, mark_distance))
