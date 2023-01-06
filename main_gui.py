"""TxTouch"""

import PySimpleGUI as sg
import asyncio
from config_manager import config
from tx_bandplan import bandplan as bp

running = True

TEST_GRAPH = False

########################################################################### begin spectrum data

import websockets

# Each scan sends a block of 1844 bytes
# This is 922 16-bit samples in low-high format
# The last two 16-bit samples are zero
# Sample zero is at 10490.500MHz
# Each sample represents 10000 / 1024 = 9.765625kHz
# Sample 919 is at 10499.475MHz
# The noise floor value is around 10000
# The peak of the beacon is around 40000

from dataclasses import dataclass

@dataclass
class SpectrumData:
    points = [(int(0),int(0))] * 920 # to ensure the last point is (0,0)
    beacon_level:int = 0
    changed: bool = False

spectrum_data = SpectrumData()

async def read_spectrum_data():
    global running
    BATC_SPECTRUM_URI = 'wss://eshail.batc.org.uk/wb/fft/fft_ea7kirsatcontroller'
    websocket = await websockets.connect(BATC_SPECTRUM_URI)
    while running:
        recvd_data = await websocket.recv()
        if len(recvd_data) != 1844:
            print('rcvd_data != 1844')
            continue
        j = 1
        for i in range(0, 1836, 2):
            uint_16: int = int(recvd_data[i]) + (int(recvd_data[i+1] << 8))
            spectrum_data.points[j] = (j, uint_16)
            j += 1
        spectrum_data.points[919] = (919, 0)
        # calculate the average beacon peak level where beacon center is 103
        spectrum_data.beacon_level = 0
        for i in range(93, 113): # should be range(73, 133), but this works better
            spectrum_data.beacon_level += spectrum_data.points[i][1]
        spectrum_data.beacon_level //= 20.0
        spectrum_data.changed = True
        #await asyncio.sleep(0)
    await websocket.close()

########################################################################### end spectrum data

########################################################################### begin pluto data

#from dataclasses import dataclass

@dataclass
class PlutoData:
    # ...
    pluto_running: bool = False
    changed: bool = False

pluto_data = PlutoData()

async def read_pluto_data():
    global running
    while running:
        await asyncio.sleep(1.0)
        # ...
        pluto_data.changed = True
    stop_pluto()

def start_pluto():
    stop_pluto()
    # ...
    pluto_data.pluto_running = True

def stop_pluto():
    if not pluto_data.pluto_running:
        return
    # ...
    pluto_data.pluto_running = False

########################################################################### end pluto data

# LAYOUT ----------------------------------------

sg.theme('Black')

MYSCRCOLOR = '#111111'
MYBUTCOLORS = ('#FFFFFF','#222222')
MYDISABLEDBUTCOLORS = ('#444444',None)
PPTONBUTTON = ('#FFFFFF','#FF0000')
   
def text_data(name, key):
    return sg.Text(name, size=11), sg.Text(' ', size=9, key=key, text_color='orange')

def incdec_but(name, key):
    return sg.Button(name, key=key, size=4, border_width=0, button_color=MYBUTCOLORS, mouseover_colors=MYBUTCOLORS)

def button_selector(key_down, value, key_up, width):
    return  incdec_but('<', key_down), sg.Text(' ', size=width, justification='center', key=value, text_color='orange'), incdec_but('>', key_up) 

top_layout = [
    sg.Button('TxTouch', key='-SYSTEM-', border_width=0, button_color=MYBUTCOLORS, mouseover_colors=MYBUTCOLORS),
    sg.Text(' ', expand_x=True, key='-STATUS_BAR-', text_color='orange'),
    sg.Button('Shutdown', key='-SHUTDOWN-', border_width=0, button_color=MYBUTCOLORS, mouseover_colors=MYBUTCOLORS),    
]

spectrum_layout = [
    sg.Graph(canvas_size=(770, 250), graph_bottom_left=(0, 0x2000), graph_top_right=(918, 0xFFFF), background_color='black', float_values=False, key='graph'),
]

tune_layout = [
    sg.Column([
        button_selector('-BD-', '-BV-', '-BU-', 8),
    ]),
    sg.Column([
        button_selector('-SD-', '-SV-', '-SU-', 5),
    ]),
    sg.Column([
        button_selector('-FD-', '-FV-', '-FU-', 12),
    ]),
]

status_layout = [
    sg.Column([
        text_data('Mode', '-MODE_V-'),     # button_selector('-MODE_D-', '-MODE_V-', '-MODE_U-'),
        text_data('Codecs', '-CODECS_V-'), # button_selector('-CODECS_D-', '-CODECS_V-', '-CODECS_U-'),
        text_data('Constellation', '-CONSTELLATION_V-'), # button_selector('-CONSTELLATION_D-', '-CONSTELLATION_V-', '-CONSTELLATION_U-'),
        text_data('FEC', '-FEC_V-'),       # button_selector('-FEC_D-', '-FEC_V-', '-FEC_U-'),
    ]),
    sg.Column([
        text_data('Bit Rate', '-BITRATE_V-'),
        text_data('Provider', '-PROVIDER_V-'),
        text_data('Service', '-SERVICE_V-'),
        text_data('Gain', '-GAIN_V-'),
    ]),
    sg.Column([
        text_data('Preamp Temp', '-PREAMP_TEMP-'),
        text_data('PA Current', '-PA_CURRENT-'),
        text_data('PA Temp', '-PA_TEMP-'),
        text_data('Fans', '-FANS-'),
    ]),
    sg.Column([
        [sg.Button(' PTT ', key='-PTT-', border_width=0, button_color=MYBUTCOLORS, mouseover_colors=MYBUTCOLORS, disabled_button_color=MYDISABLEDBUTCOLORS, disabled=False)],
        [sg.Text(' ')],
        [sg.Button(' 28v ', key='-28V-', border_width=0, button_color=MYBUTCOLORS, mouseover_colors=MYBUTCOLORS, disabled_button_color=MYDISABLEDBUTCOLORS, disabled=False)],
    ]),
]

layout = [
    top_layout,
    spectrum_layout,
    tune_layout,
    status_layout,
]

# CALLBACK DISPATCH -----------------------------

def toggle_ptt():
    if pluto_data.pluto_running:
        stop_pluto()
    else:
        start_pluto(
            #frequency,
            #bp.mode,
            #bp.constellation,
            #rate,
            #bp.fec,
            #config.gain,
            #config.calibration_mode,
            #config.pcr_pts_delay,
            #config.audio_bit_rate,
            #config.provider,
            #config.service
        )

dispatch_dictionary = { 
    # Lookup dictionary that maps button to function to call
    '-BD-':bp.dec_band, '-BU-':bp.inc_band, 
    '-FD-':bp.dec_frequency, '-FU-':bp.inc_frequency, 
    '-SD-':bp.dec_symbol_rate, '-SU-':bp.inc_symbol_rate,
    #'-MODE_D-':bp.dec_mode, '-MODE_U-':bp.inc_mode,
    #'-CODECS_D-':bp.dec_codecs, '-CODECS_U-':bp.inc_codecs,
    #'-CONSTELLATION_D-':bp.dec_constellation, '-CONSTELLATION_U-':bp.inc_constellation,
    #'-FEC_D-':bp.dec_fec, '-FEC_U-':bp.inc_fec,
    '-PTT-':toggle_ptt,
}

# UPDATE FUNCTIONS ------------------------------

def update_control(window):
    window['-BV-'].update(bp.band)
    window['-FV-'].update(bp.frequency)
    window['-SV-'].update(bp.symbol_rate)

def update_pluto_status(window):
    window['-MODE_V-'].update(bp.mode)
    window['-CODECS_V-'].update(bp.codecs)
    window['-CONSTELLATION_V-'].update(bp.constellation)
    window['-FEC_V-'].update(bp.fec)
    if pluto_data.pluto_running: 
        window['-PTT-'].update(button_color=PPTONBUTTON)
    else:
        window['-PTT-'].update(button_color=MYBUTCOLORS)
    #window['-STATUS_BAR-'].update(pm.status_msg)
        
def update_graph(spectrum_graph):
    # TODO: try just deleting the polygon and beakcon_level with delete_figure(id)
    spectrum_graph.erase()
    # draw graticule
    c = 0
    for y in range(0x2697, 0xFFFF, 0xD2D): # 0x196A, 0xFFFF, 0xD2D
        if c == 5:
            spectrum_graph.draw_text('5dB', (13,y), color='#444444')
            spectrum_graph.draw_line((40, y), (918, y), color='#444444')
        elif c == 10:
            spectrum_graph.draw_text('10dB', (17,y), color='#444444')
            spectrum_graph.draw_line((40, y), (918, y), color='#444444')
        elif c == 15:
            spectrum_graph.draw_text('15dB', (17,y), color='#444444')
            spectrum_graph.draw_line((40, y), (918, y), color='#444444')
        else:
            spectrum_graph.draw_line((0, y), (918, y), color='#222222')
        c += 1
    # draw tuned marker
    x = bp.selected_frequency_marker()
    spectrum_graph.draw_line((x, 0x2000), (x, 0xFFFF), color='#880000')

    if TEST_GRAPH:
        spectrum_graph.draw_line((0, 0), (459, 0xFFFF), color='red', width=1)
        spectrum_graph.draw_line((459, 0xFFFF), (918, 0), color='red', width=1)
    else:
        # draw beacon level
        spectrum_graph.draw_line((0, spectrum_data.beacon_level), (918, spectrum_data.beacon_level), color='#880000', width=1)
        # draw spectrum
        spectrum_graph.draw_polygon(spectrum_data.points, fill_color='green')

# MAIN ------------------------------------------

async def main_ui():
    global running
    window = sg.Window('', layout, size=(800, 480), font=(None,11), background_color=MYSCRCOLOR, use_default_focus=False, finalize=True)
    window.set_cursor('none')
    graph = window['graph']
    while running:
        event, values = window.read(timeout=1)
        if event == '-SHUTDOWN-':
            #if sg.popup_yes_no('Shutdown Now?', background_color='red', keep_on_top=True) == 'Yes':
            running = False
        if event in dispatch_dictionary:
            func_to_call = dispatch_dictionary[event]
            func_to_call()
        if spectrum_data.changed:
            update_graph(graph)
            spectrum_data.changed = False
        if bp.changed:
            update_control(window)
            bp.changed = False
        if pluto_data.changed:
            update_pluto_status(window)
            pluto_data.changed = False
        await asyncio.sleep(0.2)
    window.close()
    del window

async def main(): 
    await asyncio.gather(
        main_ui(),
        read_spectrum_data(),
        read_pluto_data(),
    )

if __name__ == '__main__':
    asyncio.run(main())
    print('about to shut down')
    #import subprocess
    #subprocess.check_call(['sudo', 'poweroff'])
