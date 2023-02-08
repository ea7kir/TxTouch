# constants

# HVC349 RF Switch
# using RFC as the input, RF2 as the output
RF_SWITCH_EN_GPIO               = 23 # pin 16 GPIO_23 (GND pin 14, pin 17 3.3v)
RF_SWITCH_CTRL_GPIO             = 24 # pin 18 GPIO_24
RF_SWITCH_HIGH                  = 1
RF_SWITCH_LOW                   = 0

# Mute Relay
RELAY_MUTE_GPIO                 = 16 # pin 36 GPIO_16 (GND pin 34, pin 17 3.3v)
# NOTE: the opto coupleers need reverse logic
RELAY_ON                        = 0  # TODO: int or bool?
RELAY_OFF                       = 1

PLUTO_ADDRESS                   = '192.168.2.1'
ENCODER_ADDRESS                 = '192.168.3.1'
