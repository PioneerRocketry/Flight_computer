#!/usr/local/bin/python3
import pandas as pd
import time
import random
from progressbar import ProgressBar

# Event APOGEE occurred at t=8.8872 seconds

def noisy_sim(sim):
    noisy_sim = sim
    for index, row in noisy_sim.iterrows():
        if index <30:
            row["Altitude (m)"] = row["Altitude (m)"] + random.uniform(0,0.5)
        else:
            row["Altitude (m)"] = row["Altitude (m)"] + random.uniform(-0.5,0.5)
    return noisy_sim



class Flight_Computer():
    def __init__(self, path_to_csv_of_simulation, apogee_t, apogee_m):
        self.sim = pd.DataFrame(pd.read_csv(path_to_csv_of_simulation))
        self.correct_apogee_t = apogee_t#seconds; change this as needed between different openrocket simulations
        self.correct_apogee_m =apogee_m 


    @staticmethod
    def instant_velocity(time_now, time_previous, altitude_now, altitude_previous):
        return (altitude_now-altitude_previous)/(time_now-time_previous)
    
    @staticmethod
    def avg(lst):
        return sum(lst)/len(lst)

    def rolling_avg(self, velocities, block_size):
        rolled_vs = []
        for i in range(0,len(velocities)-1-block_size):
            rolled_vs.append(self.avg(velocities[i:i+block_size]))
        return rolled_vs

    def check_liftoff(self, velocities):
        count = 0
        for v in velocities:
            if v>4:
                count +=1
            else:
                pass
        if count >=7:
            return True
        else:
            return False

    #apogee detector needs to be changed to a counter system because the true-false approach doesn't work with noise
    def closetozero(self, velocity):
        if -2 <= velocity <= 2:
            return True
        else:
            return False

    def apogeeDetector(self,velocities):
        count = 0
        for i in range(1,7):
            if self.closetozero(velocities[-i]) == True:
                count+= 1
                continue
        if count >= 2:
            return True
        else:
            return False

    def calculate_accuracy(self,prediction, correct):
        accuracy = abs(prediction-correct) / correct
        return round(1-accuracy, 5)
    #hello
    def Fly(self, simulation_frame):
        velocities = []
        apogee = False
        liftoff = False
        for index, row in simulation_frame.iterrows():
            #print(index, row["Time (s)"], row["Altitude (m)"])

            if index == 0:
                continue
            else:
                #v is in m/s
                v = self.instant_velocity(simulation_frame["Time (s)"][index],simulation_frame["Time (s)"][index-1], simulation_frame["Altitude (m)"][index],simulation_frame["Altitude (m)"][index-1])
                velocities.append(v)
                if index > 5:
                    if liftoff == False:
                        liftoff = self.check_liftoff(self.rolling_avg(velocities,6))

            if liftoff== True:
                if index > 20:
                    apogee = self.apogeeDetector(velocities)
                    if apogee == True:
                        #print(self.rolling_avg(velocities, 3))
                        return [row["Time (s)"],row["Altitude (m)"], self.calculate_accuracy(row["Time (s)"], self.correct_apogee_t)]
                        break

apogee_m = 408.54
apogee_t = 8.8872
path_to_sim = "//PATH_TO//simulation1.csv"
#Eddie = Flight_Computer(path_to_sim, apogee_t,apogee_m)
#Eddie_for_noise = Flight_Computer(path_to_sim, apogee_t,apogee_m)
#print("Simulation no noise: ",Eddie.Fly(Eddie.sim))
#noise1 = noisy_sim(Eddie_for_noise.sim)
#print(noise1[20:40])

#print("Simulation with noise: ", Eddie_for_noise.Fly(noise1))


def gather_data(test_size):
    
    Eddie_test = Flight_Computer(path_to_sim, apogee_t,apogee_m)
    accuracies = []
    altitudes = []
    total_fails = 0
    pbar = ProgressBar()
    for i in pbar(range(test_size)):
        try:
            noised = noisy_sim(Eddie_test.sim)
            results = Eddie_test.Fly(noised)
            accuracies.append(results[2])
            altitudes.append(results[1])
        except Exception:
            total_fails += 1
            continue

    return accuracies, total_fails, test_size, altitudes
'''
results = super_tester(20)
accuracies = results[0]
failrate = results[1] / results[2]
altitudes = results[3]
avg = lambda lst: round(sum(lst)/len(lst),4)
print("Average accuracy: ",avg(accuracies))
<<<<<<< HEAD
print("Worst accuracy in set: ", min(accuracies))
print("Percentage total failure: ", failrate)
print("Average altitude: ", avg(altitudes))
'''
=======
print("Worst performance: ", min(accuracies))
>>>>>>> 02dfd53a5afcfd652b5eb08ad767a020cf9eb432
