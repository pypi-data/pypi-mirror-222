import cytoplay
import numpy as np

"""
Here we showcase a simple cytosim simulation where an object can be controled by the keyboard.
Before running, copy or move the cytoplay module (cytoplay.---.so) to the current folder. 
"""

import time

parser = cytoplay.start("avoid.cym")
sim = parser.simul
time.sleep(0.1)
dt = sim.time_step()
frame = parser.frame()
speedos = {int(bad.id()) : dt*20.0*(np.random.rand(1,2)-0.5) for bad in frame["bad"]}
speed = np.zeros((1,2))
acc = np.zeros((1,2))

maxspeed = 20.0
decel = 10*dt
distSqr = np.square(frame["bad"][0].radius() + frame["good"][0].radius())

def runtime_all(s, speed, acc, parser):
    frame = s.frame()
    hero = frame["good"][0]
    bads = frame["bad"]
    pts =  np.array(hero.data(), copy=False)
    for bad in bads:
        id = bad.id()
        pt = np.array(bad.data(), copy=False) 
        pt += speedos[int(id)]
        if np.sum(np.square(pts-pt)) < distSqr:
            parser.execute_change("good","display = (color = red)")
    
    speed -= speed*decel
    speed += acc*dt
    ns = np.sqrt(np.sum(np.square(speed)))
    if ns>maxspeed:
        speed *= maxspeed/ns
    pts += speed*dt
    acc[:,:] = 0
    
runtime = lambda s:runtime_all(s, speed, acc, parser)

def key_cb(key, i, j):
    changed = 1
    mult = 5000
    if key==113:
        acc[:,0]-=mult
    elif key==100:
        acc[:,0]+=mult
    elif key==122:
        acc[:,1]+=mult
    elif key==115:
        acc[:,1]-=mult
    else:
        return key
    return 0
    
def mouseClick(i, j, v, k):
    vv = np.array(v, copy=True);
    frame = cytoplay.simul().frame()
    bads = frame["bad"]
    if len(bads):
        rad2 = np.square(frame["bad"][0].radius())
        for bad in bads:
            pt = np.array(bad.data(), copy=False) 
            if np.sum(np.square(pt[0,:]-vv[0:2]))<rad2:
                sim.beads.remove(bad)
    return k
    
cytoplay.setNormalKey(key_cb)
cytoplay.setRuntimeCheck(runtime)
cytoplay.setMouseClick(mouseClick)

try:
    cytoplay.play()
except:
    print("Simulation crashed or ended.")

    
