from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = [255, 255, 255] #white
r = [255, 0, 0] #red
b = [0, 0, 255] #blue
g = [0, 255, 0] #green
y = [255, 255, 0] #yellow
n = [0, 0, 0] #nothing
p = [139, 15, 255] #perse purple
m = [255, 0, 255] #lurid pink
o = [255, 128, 0] #orange

play = [
n,n,g,n,n,n,n,n,
n,n,g,g,n,n,n,n,
n,n,g,g,g,n,n,n,
n,n,g,g,g,g,n,n,
n,n,g,g,g,g,n,n,
n,n,g,g,g,n,n,n,
n,n,g,g,n,n,n,n,
n,n,g,n,n,n,n,n
]

pause = [
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n
]


stop = [
n,n,n,n,n,n,n,n,
n,r,r,r,r,r,r,n,
n,r,r,r,r,r,r,n,
n,r,r,r,r,r,r,n,
n,r,r,r,r,r,r,n,
n,r,r,r,r,r,r,n,
n,r,r,r,r,r,r,n,
n,n,n,n,n,n,n,n
]


off = [
n,n,n,n,n,n,n,n,
n,n,n,r,r,n,n,n,
n,r,n,r,r,n,r,n,
r,n,n,r,r,n,n,r,
r,n,n,r,r,n,n,r,
r,n,n,r,r,n,n,r,
n,r,n,r,r,n,r,n,
n,n,r,r,r,r,n,n
]

charactermap = [
	[
	[n,b,n,n,],
	[b,n,b,n,],
	[b,n,b,n,],
	[b,n,b,n,],
	[b,n,b,n,],
	[b,n,b,n,],
	[b,n,b,n,],
	[n,b,n,n,],
	],
	[
	[n,b,n,n,],
	[b,b,n,n,],
	[n,b,n,n,],
	[n,b,n,n,],
	[n,b,n,n,],
	[n,b,n,n,],
	[n,b,n,n,],
	[b,b,b,n,],
	],
	[
	[n,b,n,n,],
	[b,n,b,n,],
	[n,n,b,n,],
	[n,b,n,n,],
	]
	]

load0 = [
b,g,y,o,r,m,p,b,	

sense.set_pixels(play)
sleep(1)
sense.set_pixels(pause)
sleep(1)
sense.set_pixels(stop)
sleep(1)
sense.set_pixels(off)
sleep(1)

while True:
	sense.set_pixels(load0)
	sleep(0.2)	
	sense.set_pixels(load1)
	sleep(0.2)
	sense.set_pixels(load2)
	sleep(0.2)
	sense.set_pixels(load3)
	sleep(0.2)
