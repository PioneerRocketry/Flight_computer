import pandas as pd
import time
# Event APOGEE occurred at t=8.8872 seconds
sim = pd.read_csv("//Users//jeremi//Documents//RocketSimulation//simulation1.csv")
sim = pd.DataFrame(sim)


def instant_velocity(time_now, time_previous, altitude_now, altitude_previous):
    return (altitude_now-altitude_previous)/(time_now-time_previous)


velocities = []

lift_off_yet = False

def check_liftoff(velocities):
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
    
def closetozero(velocity):
    if -1 <= velocity <= 1:
        return True
    else:
        return False

def apogeeDetector(velocities):
    for i in range(1,5):
        #this is where we stopped in the club
        closetozero(velocities[-i])








apogee = False
liftoff = False
for index, row in sim.iterrows():
    print(index, row["Time (s)"], row["Altitude (m)"])

    if index == 0:
        continue
    else:
        #v is in m/s
        v = instant_velocity(sim["Time (s)"][index],sim["Time (s)"][index-1], sim["Altitude (m)"][index], sim["Altitude (m)"][index-1])
        velocities.append(v)
        if index > 5:
            if liftoff == False:
                liftoff = check_liftoff(velocities)
    
    
    if liftoff== True:
        apogee = apogeeDetector()




    if index <10:
        continue
    else:
        break

#we have to detect launch and we have to detect apogee

'''
to detect launch we could potentially do a rolling average and once the average
starts to trend convincingly upward the computer could say beep boop we have launched
'''
