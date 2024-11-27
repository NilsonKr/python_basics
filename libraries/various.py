import os 
import math
import random

# Get cwd

cwd = os.getcwd()

# List current directory .py files

directory = [file for file in os.listdir() if file.endswith('.py')]