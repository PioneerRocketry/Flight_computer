# Flight_computer
Basically, we are simulating the flights in OpenRocket, exporting the altitude data to csv, then writing our program in python to read in the csv data and simulate the flight computer in air!

So far, it's very basic and handles noise with little consistency, but that should be fixable since it's just certain edge cases and should be better after we add something like a rolling average filter.

Next steps:
  - Make algorithm more resilient
  - write in arduino and feed simulation data to arduino to get better quality simulation
  - automate simulation testing
