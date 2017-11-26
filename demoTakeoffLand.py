"""
Demo taking off and landing
"""

from Mambo import Mambo
from constants import MAMBO_ADDR

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

print("landing")
mambo.safe_land()
mambo.smart_sleep(5)

print("disconnect")
mambo.disconnect()

