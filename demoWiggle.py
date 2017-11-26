"""
Demo wiggle maneuver for capturing stereoscopic view
"""
"""
Demo taking off and landing
"""

from Mambo import Mambo
from settings import MAMBO_ADDR

mamboAddr = MAMBO_ADDR

# make my mambo object
mambo = Mambo(mamboAddr)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

# get the state information
print("sleeping")
mambo.smart_sleep(2)
mambo.ask_for_state_update()
mambo.smart_sleep(2)

print("taking off!")
mambo.safe_takeoff(5)


print('capturing shifts')
mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.1)
mambo.smart_sleep(1)
mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=0.2)
mambo.smart_sleep(1)
mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.1)

print("landing")
mambo.safe_land()
mambo.smart_sleep(5)

print("disconnect")
mambo.disconnect()

