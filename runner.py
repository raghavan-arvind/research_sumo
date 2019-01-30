import os, sys
sys.path.append(os.path.join(os.environ['SUMO_HOME'], "share", "sumo", "tools"))
import traci

sumoBinary = os.path.join(os.environ['SUMO_HOME'], 'bin', 'sumo-gui')
sumoCmd = [sumoBinary, "-c", "square.sumocfg"]

traci.start(sumoCmd) 

step = 0

while step < 1000:
    print("Step: %d" % (step))
    traci.simulationStep()

    step += 1

traci.close(False)
