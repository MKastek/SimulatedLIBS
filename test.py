from SimulatedLIBS import simulation
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    simulation.SimulatedLIBS.create_dataset(input_csv_file=r"C:\Users\marci\Desktop\Python\SimulatedLIBS\data.csv", output_csv_file='output.csv', size=100, Te_min=1.0, Te_max=2.0, Ne_min=10**17, Ne_max=10**18)
