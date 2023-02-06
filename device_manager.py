import pigpio
from time import sleep

from device_rf_switch import configure_rf_switches, shutdown_rf_switches
from device_rf_switch import switch_rf_switch_On, switch_mute_Off
from device_relays import configure_relays, shutdown_relays
from device_relays import switch_mute_On, switch_mute_Off

_pi = None

def configure_devices():
    global _pi
    _pi = pigpio.pi()
    configure_rf_switches(_pi)
    configure_relays(_pi)

def shutdown_devices():
    shutdown_rf_switches()
    shutdown_relays()
    _pi.stop() # TypeError: pi.stop() missing 1 required positional argument: 'self'

def activate_ptt():
    switch_rf_switch_On
    
def deactivate_ptt():
    switch_rf_switch_Off
    
def mute_audio():
    # sleep(5) # TODO: this may not be the best place - 0r use a thread !
    switch_mute_On()

def unmute_audio():
    switch_mute_Off()
