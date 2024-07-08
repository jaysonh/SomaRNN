import torch
import numpy as np

def strip_frame(filename, max_lines, feature_size):
        with open( filename, 'r' ) as file:
                lines = file.readlines()

        frameNum = 0
        num_lines = max_lines
        arr = np.zeros(shape=(2500,num_lines, feature_size),dtype=np.float32)
        for line in lines:
                line = line.strip()
                values = line.split("    ")
                arr[frameNum]=values
                frameNum += 1
                if frameNum % 100 == 0:
                        print(f"Loading frame {frameNum}")
                if frameNum >= max_lines:
                        break
        return arr
