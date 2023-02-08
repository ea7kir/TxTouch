import pigpio
from time import sleep

from device_rf_switch import configure_rf_switches, shutdown_rf_switches
from device_rf_switch import switch_rf_switch_On, switch_rf_switch_Off
from device_relays import configure_relays, shutdown_relays
from device_relays import switch_mute_On, switch_mute_Off
from device_encoder import configure_encoder, shutdown_encoder
from device_encoder import setup_encoder
from device_pluto import configure_pluto, shutdown_pluto
from device_pluto import setup_pluto

_pi = None

def configure_devices():
    global _pi
    _pi = pigpio.pi()
    configure_rf_switches(_pi)
    configure_relays(_pi)
    configure_encoder()
    configure_pluto()

def shutdown_devices():
    shutdown_rf_switches()
    shutdown_relays()
    shutdown_encoder()
    shutdown_pluto()
    _pi.stop() # TypeError: pi.stop() missing 1 required positional argument: 'self'

def setup_encoder_and_pluto(encoder_args, pluto_args):
    setup_encoder(encoder_args)
    setup_pluto(pluto_args)

def activate_ptt():
    switch_rf_switch_On()
    switch_mute_On()
    
def deactivate_ptt():
    switch_rf_switch_Off()
    switch_mute_Off()
    
