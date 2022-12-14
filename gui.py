# gui.py

"""TxTouch"""

import PySimpleGUI as sg
from tx_bandplan import tx_bandplan as bp
from pluto_manager import pluto_manager as pm

# LAYOUT ----------------------------------------

sg.theme('Black')

MYBUTCOLORS = ('#FFFFFF','#222222')
PPTONBUTTON = ('#ffffff','#FF0000')
MYDISABLEDBTCOLORS = ('#444444',None)
    
def text_data(name, key):
    return [ sg.Text(' '), sg.Text(name, size=(15,1)), sg.Text('', key=key, text_color='orange', font=(None,11)) ]

def incdec_but(name, key):
    return sg.Button(name, key=key, size=(4,1), font=(None,13), border_width=0, button_color=MYBUTCOLORS, mouseover_colors=MYBUTCOLORS)

def button_selector(key_down, value, key_up):
    return [ incdec_but('<', key_down), sg.Push(), sg.Text('', key=value, text_color='orange', font=(None,13)), sg.Push(), incdec_but('>', key_up) ]

encoding_layout = [
    [sg.Push(), sg.Text('Codecs', text_color='green'), sg.Push()],
    button_selector('-CODECS_D-', '-CODECS_V-', '-CODECS_U-'),
    [sg.Push(), sg.Text('Constellation', text_color='green'), sg.Push()],
    button_selector('-CONSTELLATION_D-', '-CONSTELLATION_V-', '-CONSTELLATION_U-'),
    [sg.Push(), sg.Text('FEC', text_color='green'), sg.Push()],
    button_selector('-FEC_D-', '-FEC_V-', '-FEC_U-'),
    [sg.Text('Bit Rate [integer]')],
    [sg.Text('Provider [text]')],
    [sg.Text('Servicee [text]')],
]

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

layout = [
    [sg.Frame(' Encoding Controls ',
        encoding_layout, title_color='green', size=(340,340), pad=(15,15) ),  
        sg.Frame(' Transmitter Controls ',
        control_layout, title_color='green', size=(340,340), pad=(15,15) ),
    ],
    [sg.Push(), sg.Button('Shutdown', key='-SHUTDOWN-', border_width=0, button_color=MYBUTCOLORS, mouseover_colors=MYBUTCOLORS)],
    [sg.Text('', key='-STATUS_BAR-', text_color='green')],
]

# CALLBACK DISPATCH -----------------------------

def toggle_ptt():
    # call out to Pluto
    if pm.ptt_is_on:
        pm.stop_ptt()
    else:
        pm.start_ptt(bp.frequency, bp.symbol_rate)

dispatch_dictionary = { 
    # Lookup dictionary that maps button to function to call
    '-BD-':bp.dec_band, '-BU-':bp.inc_band, 
    '-FD-':bp.dec_frequency, '-FU-':bp.inc_frequency, 
    '-SD-':bp.dec_symbol_rate, '-SU-':bp.inc_symbol_rate,
    '-CODECS_D-':bp.dec_codecs, '-CODECS_U-':bp.inc_codecs,
    '-CONSTELLATION_D-':bp.dec_constellation, '-CONSTELLATION_U-':bp.inc_constellation,
    '-FEC_D-':bp.dec_fec, '-FEC_U-':bp.inc_fec,
    '-PTT-':toggle_ptt,
}

# UPDATE FUNCTIONS ------------------------------

#def update_more():
#    pass
 
def update_control():
    window['-BV-'].update(bp.band)
    window['-FV-'].update(bp.frequency)
    window['-SV-'].update(bp.symbol_rate)
    window['-CODECS_V-'].update(bp.codecs)
    window['-CONSTELLATION_V-'].update(bp.constellation)
    window['-FEC_V-'].update(bp.fec)
    if pm.ptt_is_on: 
        window['-PTT-'].update(button_color=PPTONBUTTON)
        print('ON')
    else:
        window['-PTT-'].update(button_color=MYBUTCOLORS)
        print('OFF')
        
# MAIN ------------------------------------------

window = sg.Window('', layout, size=(800, 480), font=(None,11), use_default_focus=False, finalize=True)
window.set_cursor('none')

while True:
    event, values = window.read(timeout=10)
    if event == '-SHUTDOWN-':
        if sg.popup_yes_no('Shutdown Now?', font=(None,11), background_color='red', keep_on_top=True) == 'Yes':
            pm.stop_ptt()
            break
    if event in dispatch_dictionary:
        func_to_call = dispatch_dictionary[event]
        func_to_call()
    elif bp.changed:
        update_control()
        bp.changed = False
    elif pm.status_changed:
        window['-STATUS_BAR-'].update(pm.status_msg)
        update_control()
        pm.status_changed = False
        
window.close()
del window

############ for long operations, see: https://www.pysimplegui.org/en/latest/cookbook/#threaded-long-operation
#    if lm.status_available:
#    window.perform_long_operation(lm.read_status(), '-FUNCTION COMPLETED-')
#    
#    if event == '-FUNCTION COMPLETED-':)

print('Shutting down...')
#import subprocess
#subprocess.check_call(['sudo', 'poweroff'])
    