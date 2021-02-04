#import pandas as pd
import random
#sim = pd.read_csv("//Users//jeremi//Documents//Flight_computer//simulation1.csv")
#sim = pd.DataFrame(sim)

def add_noise(simulation_dataframe):
    for index, row in simulation_dataframe.iterrows():
        row["Altitude (m)"] = row["Altitude (m)"] + random.uniform(-1,1)
    return simulation_dataframe
