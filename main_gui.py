"""TxTouch"""

import PySimpleGUI as sg
from tx_bandplan import bandplan as bp
from process_spectrum import process_read_spectrum_data, SpectrumData
from process_roof import process_read_roof_data, RoofData

from multiprocessing import Process
from multiprocessing import Pipe

running = True

TEST_GRAPH = False

########################################################################### begin encoder data

class EncoderData:
    def __init__(self):
        self.ip:str = '000.000.000.000'
        self.port:int = 0
        self.encoding:str = 'H.265'
        self.bit_rate:str = '430'
        self.changed: bool = False
    
#encoder_data = EncoderData()

########################################################################### end encoder data

########################################################################### begin pluto data

class PlutoData:
    def __init__(self):
        # TODO: note these are just example values
        self.ip:str = '000.000.000.000',
        self.port:int = 8282,
        self.frequency:str = '2409.75',
        self.mode:str = 'DBS2',
        self.constellation:str = 'QPSK',
        self.rate:str = '333',
        self.fec:str = '23',
        self.gain:str = '-10',
        self.calibration_mode:str = 'nocalib',
        self.pcr_pts_delay:str = '800',
        self.audio_bit_rate:str = '32',
        self.provider:str = 'EA7KIR',
        self.service:str = 'Malaga',
        self.pluto_running: bool = False

#pluto_data = PlutoData()

def start_pluto():
    stop_pluto()
    # Eg: "rtmp://192.168.1.40:7272/,2409.75,DVBS2,QPSK,333,23,-2,nocalib,800,32,/,EA7KIR,"
    cmd_str = 'rtmp://{}:{}/,{},{},{},{},{},{},{},{},{},/,{}'.format(
        pluto_data.ip,
        pluto_data.port,
        pluto_data.frequency,
        pluto_data.mode,
        pluto_data.constellation,
        pluto_data.symbol_rate,
        pluto_data.fec,
        pluto_data.gain,
        pluto_data.calibration_mode,
        pluto_data.pcr_pts_delay,
        pluto_data.audio_bit_rate,
        pluto_data.provider)
    # TODO: send to pluto
    print(cmd_str)
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
        # control data
        text_data('Mode', '-MODE_V-'),     # button_selector('-MODE_D-', '-MODE_V-', '-MODE_U-'),
        text_data('Codecs', '-CODECS_V-'), # button_selector('-CODECS_D-', '-CODECS_V-', '-CODECS_U-'),
        text_data('Constellation', '-CONSTELLATION_V-'), # button_selector('-CONSTELLATION_D-', '-CONSTELLATION_V-', '-CONSTELLATION_U-'),
        text_data('FEC', '-FEC_V-'),       # button_selector('-FEC_D-', '-FEC_V-', '-FEC_U-'),
    ]),
    sg.Column([
        # control data
        text_data('Bit Rate', '-BITRATE_V-'),   # button_selector('-BITRATE_D-', '-BITRATE_V-', '-BITRATE_U-'),
        text_data('Provider', '-PROVIDER_V-'),  # button_selector('-PROVIDER_D-', '-PROVIDER_V-', '-PROVIDER_U-'),
        text_data('Service', '-SERVICE_V-'),    # button_selector('-SERVICE_D-', '-SERVICE_V-', '-SERVICE_U-'),
        text_data('Gain', '-GAIN_V-'),          # button_selector('-GAINE_D-', '-GAIN_V-', '-GAIN_U-'),
    ]),
    sg.Column([
        # roof data
        text_data('Preamp Temp', '-PREAMP_TEMP-'),
        text_data('PA Current', '-PA_CURRENT-'),
        text_data('PA Temp', '-PA_TEMP-'),
        text_data('Fans', '-FANS-'),
    ]),
    sg.Column([
        # control data
        [sg.Button(' PTT ', key='-PTT-', border_width=0, button_color=MYBUTCOLORS, mouseover_colors=MYBUTCOLORS, disabled_button_color=MYDISABLEDBUTCOLORS, disabled=False)],
        [sg.Text(' ')],
        # roof data
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
        start_pluto()

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

def update_control(window, bp):
    window['-BV-'].update(bp.band)
    window['-FV-'].update(bp.frequency)
    window['-SV-'].update(bp.symbol_rate)

def update_pluto_status(window, bp):
    window['-MODE_V-'].update(bp.mode)
    window['-CODECS_V-'].update(bp.codecs)
    window['-CONSTELLATION_V-'].update(bp.constellation)
    window['-FEC_V-'].update(bp.fec)
    if pluto_data.pluto_running: 
        window['-PTT-'].update(button_color=PPTONBUTTON)
    else:
        window['-PTT-'].update(button_color=MYBUTCOLORS)
    #window['-STATUS_BAR-'].update(pm.status_msg)

def update_roof_data(window, roof_data):
    window['-PREAMP_TEMP-'].update(roof_data.preamp_temp)
    window['-PA_CURRENT-'].update(roof_data.pa_current)
    window['-PA_TEMP-'].update(roof_data.pa_temp)
    window['-FANS-'].update(roof_data.fans)
        
def update_graph(graph, spectrum_data):
    # TODO: try just deleting the polygon and beakcon_level with delete_figure(id)
    graph.erase()
    # draw graticule
    c = 0
    for y in range(0x2697, 0xFFFF, 0xD2D): # 0x196A, 0xFFFF, 0xD2D
        if c == 5:
            graph.draw_text('5dB', (13,y), color='#444444')
            graph.draw_line((40, y), (918, y), color='#444444')
        elif c == 10:
            graph.draw_text('10dB', (17,y), color='#444444')
            graph.draw_line((40, y), (918, y), color='#444444')
        elif c == 15:
            graph.draw_text('15dB', (17,y), color='#444444')
            graph.draw_line((40, y), (918, y), color='#444444')
        else:
            graph.draw_line((0, y), (918, y), color='#222222')
        c += 1
    # draw tuned marker
    x = bp.selected_frequency_marker()
    graph.draw_line((x, 0x2000), (x, 0xFFFF), color='#880000')

    if TEST_GRAPH:
        graph.draw_line((0, 0), (459, 0xFFFF), color='red', width=1)
        graph.draw_line((459, 0xFFFF), (918, 0), color='red', width=1)
    else:
        # draw beacon level
        graph.draw_line((0, spectrum_data.beacon_level), (918, spectrum_data.beacon_level), color='#880000', width=1)
        # draw spectrum
        graph.draw_polygon(spectrum_data.points, fill_color='green')

# MAIN ------------------------------------------

def main_gui(recv_spectrum_data, recv_roof_data):
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
        if bp.changed:
            update_control(window, bp)
            bp.changed = False
        while recv_spectrum_data.poll():
            spectrum_data = recv_spectrum_data.recv()
            update_graph(graph, spectrum_data)
        while recv_roof_data.poll():
            roof_data = recv_roof_data.recv()
            update_roof_data(window, roof_data)
    window.close()
    del window

if __name__ == '__main__':
    recv_spectrum_data, send_spectrum_data = Pipe()
    recv_roof_data, send_roof_data = Pipe()
    # create the process
    p_read_spectrum_data = Process(target=process_read_spectrum_data, args=(send_spectrum_data,))
    p_read_roof_data = Process(target=process_read_roof_data, args=(send_roof_data,))
    # start the process
    p_read_spectrum_data.start()
    p_read_roof_data.start()
    # main ui
    main_gui(recv_spectrum_data, recv_roof_data)
    # kill 
    p_read_spectrum_data.kill()
    p_read_roof_data.kill()
    # shutdown
    print('about to shut down')
    #import subprocess
    #subprocess.check_call(['sudo', 'poweroff'])
