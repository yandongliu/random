from math import sqrt
from random import random

MAX = 100000


def is_in_quadrant(x, y, radius):
    return sqrt(x * x + y * y) <= radius

def compute_pi(radius=1):
    count = 0
    in_count = 0
    while count < MAX:
        x, y = sample_one_point(radius)
        if is_in_quadrant(x, y, radius):
            in_count += 1
        count += 1
    return float(in_count)/count * 4.0

def sample_one_point(radius=1):
    return (random() * radius, random() * radius)


print compute_pi()
