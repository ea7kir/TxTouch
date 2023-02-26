import pigpio
from device_constants import RF_SWITCH_HIGH, RF_SWITCH_LOW
from device_constants import RF_SWITCH_EN_GPIO, RF_SWITCH_CTRL_GPIO

_rf_pi = None

# HMC349 using RFC as the input, RF2 as the output

def _switch_HMC349(gpio, state):
    _rf_pi.write(gpio, state)

def _config_HMC349(en_gpio, ctrl_gpio):
    _rf_pi.set_mode(ctrl_gpio, pigpio.OUTPUT)
    _rf_pi.write(ctrl_gpio, RF_SWITCH_HIGH)
    _rf_pi.set_mode(en_gpio, pigpio.OUTPUT)
    _rf_pi.write(en_gpio, RF_SWITCH_LOW)

def configure_rf_switches(pi):
    global _rf_pi
    _rf_pi = pi
    _config_HMC349(RF_SWITCH_EN_GPIO, RF_SWITCH_CTRL_GPIO)

def shutdown_rf_switches():
    _switch_HMC349(RF_SWITCH_CTRL_GPIO, RF_SWITCH_HIGH)
    _switch_HMC349(RF_SWITCH_EN_GPIO, RF_SWITCH_HIGH)

def switch_rf_switch_On():
    print("SWITCHING ON RF SWITCH")
    _switch_HMC349(RF_SWITCH_CTRL_GPIO, RF_SWITCH_LOW)

def switch_rf_switch_Off():
    print("SWITCHING OFF RF SWITCH")
    _switch_HMC349(RF_SWITCH_CTRL_GPIO, RF_SWITCH_HIGH)

