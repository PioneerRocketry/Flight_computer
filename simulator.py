import pandas as pd
import time
#import spreadsheet as ss
# Event APOGEE occurred at t=8.8872 seconds

class Flight_Computer():
    def __init__(self, path_to_csv_of_simulation):
        self.sim = pd.DataFrame(pd.read_csv(path_to_csv_of_simulation))
        self.correct_apogee_t = 8.8872#seconds; change this as needed between different openrocket simulations



    @staticmethod
    def instant_velocity(time_now, time_previous, altitude_now, altitude_previous):
        return (altitude_now-altitude_previous)/(time_now-time_previous)


    

    def check_liftoff(self, velocities):
        count = 0
        for v in velocities:
            if v>0:
                count +=1
            else:
                pass
        if count >=7:
            return True
        else:
            return False
        
    def closetozero(self, velocity):
        if -1 <= velocity <= 1:
            return True
        else:
            return False

    def apogeeDetector(self,velocities):
        good = False
        for i in range(1,5):
            #this is where we stopped in the club
            if self.closetozero(velocities[-i]) == True:
                good = True
                continue
            else:
                good = False
                break
        return good

    def calculate_accuracy(self,prediction, correct):
        accuracy = abs(prediction-correct) / correct
        return round(1 - accuracy, 5)
    #hello
    def Fly(self):
        velocities = []
        apogee = False
        liftoff = False
        for index, row in self.sim.iterrows():
            #print(index, row["Time (s)"], row["Altitude (m)"])

            if index == 0:
                continue
            else:
                #v is in m/s
                v = self.instant_velocity(self.sim["Time (s)"][index],self.sim["Time (s)"][index-1], self.sim["Altitude (m)"][index],self. sim["Altitude (m)"][index-1])
                velocities.append(v)
                if index > 5:
                    if liftoff == False:
                        liftoff = self.check_liftoff(velocities)
            

            if liftoff== True:
                if index > 20:
                    apogee = self.apogeeDetector(velocities)
                    if apogee == True:
                        print("APOGEE!!! ")
                        break



Eddie_the_Computer = Flight_Computer("//Users//jeremi//Documents//Flight_computer//simulation1.csv")
Eddie_the_Computer.Fly()