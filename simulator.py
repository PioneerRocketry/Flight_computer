import pandas as pd
import time
# Event APOGEE occurred at t=8.8872 seconds
sim = pd.read_csv("//Users//jeremi//Documents//RocketSimulation//simulation1.csv")
sim = pd.DataFrame(sim)


def instant_velocity(time_now, time_previous, altitude_now, altitude_previous):
    return (altitude_now-altitude_previous)/(time_now-time_previous)


velocities = []
rolling_vs = []


for index, row in sim.iterrows():
    print(row["Time (s)"], row["Altitude (m)"])

    if index == 0:
        continue
    else:
        #v is in m/s
        v = instant_velocity(sim["Time (s)"][index],sim["Time (s)"][index-1], sim["Altitude (m)"][index], sim["Altitude (m)"][index-1])
        velocities.append(v)
        try:
            to_calc = []
            for i in range(5):
                to_calc.append(velocities[-i])
            to_calc = to_calc.reverse()
            for i in range(1,len(to_calc)-1):
                if to_calc[i] - to_calc[i-1] > 0:
                    continue
                    still_good = True
                else:
                    still_good = False
                    break
                if still_good == True:
                    print("Liftoff!!!")
                else:
                    print("Boring")
        except Exception:
            print("Oh fuckaroonie doo, it didn't work yet")
            continue
        print(v)


    if index <10:
        continue
    else:
        break

#we have to detect launch and we have to detect apogee

'''
to detect launch we could potentially do a rolling average and once the average
starts to trend convincingly upward the computer could say beep boop we have launched
'''