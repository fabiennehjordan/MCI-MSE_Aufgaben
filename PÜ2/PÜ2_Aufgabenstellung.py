import numpy as np
import matplotlib.pyplot as plt
import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__)))
pathname = os.path.join(ROOT_DIR, "input_data")

for file in os.listdir(pathname):
    if file.endswith(".txt"):
       print(file)