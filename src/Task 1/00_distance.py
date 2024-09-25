#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Tuple

def calculate_distance(city1: Tuple[int, int], city2: Tuple[int, int]):
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {x: {y: calculate_distance(sites[x], sites[y]) for y in sites if y != x} for x in sites}
print(distances)




