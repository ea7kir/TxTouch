# gui.py

import PySimpleGUI as sg
from bandplan import band_plan as bp
from pluto_manager import pluto_manager as pm

"""
Frequency
-
encoder settings
-
Symbol Rate
Mode
Constellation
FEC
Drive
-
PTT
"""

# The callback functions

def ptt():
    pm.start_ptt(bp.frequency, bp.symbol_rate)

# Lookup dictionary that maps button to function to call
dispatch_dictionary = { 
    '-BD-':bp.dec_band, '-BU-':bp.inc_band, 
    '-FD-':bp.dec_frequency, '-FU-':bp.inc_frequency, 
    '-SD-':bp.dec_symbol_rate, '-SU-':bp.inc_symbol_rate,
    '-PTT-':ptt,
}

# ------------------------------------------------

MYBUTCOLORS = ('#FFFFFF','#222222')
MYDISABLEDBTCOLORS = ('#444444',None)

def text_data(name, key):
    return [ sg.Text(' '), sg.Text(name, size=(15,1)), sg.Text('', key=key, text_color='orange', font=(None,11)) ]

def incdec_but(name, key):
    return sg.Button(name, key=key, size=(4,1), font=(None,13), border_width=0, button_color=MYBUTCOLORS, mouseover_colors=MYBUTCOLORS)

def button_selector(key_down, value, key_up):
    return [ incdec_but('<', key_down), sg.Push(), sg.Text('', key=value, text_color='orange', font=(None,13)), sg.Push(), incdec_but('>', key_up) ]

# ------------------------------------------------

sg.theme('Black')

# layouts

# ------------------------------------------------

control_layout = [
    [sg.Push(), sg.Text('Band', text_color='green'), sg.Push()],
    button_selector('-BD-', '-BV-', '-BU-'),
    [sg.Push(), sg.Text('Frequency / Channel', text_color='green'), sg.Push()],
    button_selector('-FD-', '-FV-', '-FU-'),
    [sg.Push(), sg.Text('Symbol Rate', text_color='green'), sg.Push()],
    button_selector('-SD-', '-SV-', '-SU-'),
    [sg.Text('')],
    [sg.Push(), sg.Button('PTT', key='-PTT-', border_width=0, button_color=MYBUTCOLORS, mouseover_colors=MYBUTCOLORS, disabled_button_color=MYDISABLEDBTCOLORS, disabled=False), sg.Push()],
]

more_layout = [
    [sg.Text('more...')]
]

# ------------------------------------------------

def update_control():
    window['-BV-'].update(bp.band)
    window['-FV-'].update(bp.frequency)
    window['-SV-'].update(bp.symbol_rate)

def update_more():
    pass

layout = [
    [sg.Frame('Transmiter Controls',
        control_layout, title_color='green', size=(340,340), pad=(15,15) ),
        
        sg.Frame('More Controls',
        more_layout, title_color='green', size=(340,340), pad=(15,15) ),
    ],
    [sg.Push(), sg.Button('Shutdown', key='-SHUTDOWN-', border_width=0, button_color=MYBUTCOLORS, mouseover_colors=MYBUTCOLORS)],
    [sg.Text('', key='-STATUS_BAR-', text_color='green')],
]

window = sg.Window('', layout, size=(800, 480), font=(None,11), use_default_focus=False, finalize=True)
window.set_cursor('none')

while True:
    event, values = window.read(timeout=10)
    if event == '-SHUTDOWN-':
        if sg.popup_ok_cancel('Shutdown Now?', font=(None,15), background_color='red',
                    #no_titlebar=True, keep_on_top=True) == 'OK':
                    keep_on_top=True) == 'OK':
            pm.stop_ptt()
            break

    if event in dispatch_dictionary:
        func_to_call = dispatch_dictionary[event]
        func_to_call()
    elif bp.changed:
        update_control()
        bp.changed = False
    else:
        update_more()

############ for long operations, see: https://www.pysimplegui.org/en/latest/cookbook/#threaded-long-operation
#    if lm.status_available:
#    window.perform_long_operation(lm.read_status(), '-FUNCTION COMPLETED-')
#    
#    if event == '-FUNCTION COMPLETED-':)

window.close()
del window

print('about to shutdown')
#import subprocess
#subprocess.check_call(['sudo', 'poweroff'])
    