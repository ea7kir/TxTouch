"""TxTouch"""

from multiprocessing import Process
from multiprocessing import Pipe

import PySimpleGUI as sg
import control_status as cs

from process_spectrum import process_read_spectrum_data, SpectrumData
from process_server import process_read_server_data, ServerData

from device_manager import configure_devices, shutdown_devices

# LAYOUT ----------------------------------------

sg.theme('Black')

SCREEN_COLOR = '#111111'
NORMAL_BUTTON_COLOR = ('#FFFFFF','#222222')
# DISABALED_BUTTON_COLOR = ('#444444',None)
# TUNE_ACTIVE_BUTTON_COLOR = ('#FFFFFF','#007700')
# PTT_ACTIVE_BUTTON_COLOR = ('#FFFFFF','#FF0000')
   
def text_data(name, key):
    return sg.Text(name, size=11), sg.Text(' ', size=9, key=key, text_color='orange')

def incdec_but(name, key):
    return sg.Button(name, key=key, size=4, border_width=0, button_color=NORMAL_BUTTON_COLOR, mouseover_colors=NORMAL_BUTTON_COLOR)

def button_selector(key_down, value, key_up, width):
    return  incdec_but('<', key_down), sg.Text(' ', size=width, justification='center', key=value, text_color='orange'), incdec_but('>', key_up) 

top_layout = [
    sg.Button('TxTouch', key='-SYSTEM-', border_width=0, button_color=NORMAL_BUTTON_COLOR, mouseover_colors=NORMAL_BUTTON_COLOR),
    sg.Text(' ', expand_x=True, key='-STATUS_BAR-', text_color='orange'),
    sg.Button('Shutdown', key='-SHUTDOWN-', border_width=0, button_color=NORMAL_BUTTON_COLOR, mouseover_colors=NORMAL_BUTTON_COLOR),    
]

spectrum_layout = [
    sg.Graph(canvas_size=(770, 240), graph_bottom_left=(0, 0x2000), graph_top_right=(918, 0xFFFF), background_color='black', float_values=False, key='graph'),
]

tune_layout = [
    sg.Column([
        # control data
        button_selector('-BD-', '-BV-', '-BU-', 8),  
    ]),
    sg.Column([
        # control data
        button_selector('-SD-', '-SV-', '-SU-', 5),
    ]),
    sg.Column([
        # control data
        button_selector('-FD-', '-FV-', '-FU-', 12),
    ]),
]

status_layout = [
    sg.Column([
        # control data   
        button_selector('-MODE_D-', '-MODE_V-', '-MODE_U-', 8),
        button_selector('-CODECS_D-', '-CODECS_V-', '-CODECS_U-', 8),
        button_selector('-CONSTELLATION_D-', '-CONSTELLATION_V-', '-CONSTELLATION_U-', 8),
        button_selector('-FEC_D-', '-FEC_V-', '-FEC_U-', 8),
    ]),
    sg.Column([
        # control data
        button_selector('-VIDEO_BITRATE_D-', '-VIDEO_BITRATE_V-', '-VIDEO_BITRATE_U-', 8),
        button_selector('-PROVIDER_D-', '-PROVIDER_V-', '-PROVIDER_U-', 8),
        button_selector('-SERVICE_D-', '-SERVICE_V-', '-SERVICE_U-', 8),
        button_selector('-GAIN_D-', '-GAIN_V-', '-GAIN_U-', 8),
    ]),
    sg.Column([
        # roof data
        text_data('Preamp Temp', '-PREAMP_TEMP-'),
        text_data('PA Current', '-PA_CURRENT-'),
        text_data('PA Temp', '-PA_TEMP-'),
        text_data('Fans Running', '-FANS-'),
    ]),
    sg.Column([
        # control data
        [sg.Button(' TUNE ', key='-TUNE-', border_width=0, button_color=NORMAL_BUTTON_COLOR, mouseover_colors=NORMAL_BUTTON_COLOR)],
        [sg.Text(' ')],
        # roof data
        [sg.Button(' PTT ', key='-PTT-', border_width=0, button_color=NORMAL_BUTTON_COLOR, mouseover_colors=NORMAL_BUTTON_COLOR)],
    ]),
]

layout = [
    top_layout,
    spectrum_layout,
    tune_layout,
    status_layout,
]

# CALLBACK DISPATCH -----------------------------

def display_initial_values():
    # fix to display initial controll values
    pass

dispatch_dictionary = { 
    # Lookup dictionary that maps button to function to call
    # NOTE: the order could affect responsiveness, but maybe a disctionary lookup is just too slow
    '-TUNE-':cs.tune,
    '-PTT-':cs.ptt,
    '-BD-':cs.dec_band, '-BU-':cs.inc_band, 
    '-FD-':cs.dec_frequency, '-FU-':cs.inc_frequency, 
    '-SD-':cs.dec_symbol_rate, '-SU-':cs.inc_symbol_rate,
    '-MODE_D-':cs.dec_mode, '-MODE_U-':cs.inc_mode,
    '-CODECS_D-':cs.dec_codecs, '-CODECS_U-':cs.inc_codecs,
    '-CONSTELLATION_D-':cs.dec_constellation, '-CONSTELLATION_U-':cs.inc_constellation,
    '-FEC_D-':cs.dec_fec, '-FEC_U-':cs.inc_fec,
    '-VIDEO_BITRATE_D-':cs.dec_video_bitrate, '-VIDEO_BITRATE_U-':cs.inc_video_bitrate,
    '-PROVIDER_D-':cs.dec_provider, '-PROVIDER_U-':cs.inc_provider,
    '-SERVICE_D-':cs.dec_service, '-SERVICE_U-':cs.inc_service,
    '-GAIN_D-':cs.dec_gain, '-GAIN_U-':cs.inc_gain,
    '-DISPLAY_INITIAL_VALUES-':display_initial_values,
}

# MAIN ------------------------------------------

def main_gui(spectrum_pipe, server_pipe):
    window = sg.Window('', layout, size=(800, 480), font=(None,11), background_color=SCREEN_COLOR, use_default_focus=False, finalize=True)
    window.set_cursor('none')
    graph = window['graph']
    window.write_event_value('-DISPLAY_INITIAL_VALUES-', None) # fix to display initial control values
    while True:
        event, values = window.read(timeout=100)
        if event == '__TIMEOUT__':
            if spectrum_pipe.poll():
                spectrum_data = spectrum_pipe.recv()
                while spectrum_pipe.poll():
                    _ = spectrum_pipe.recv()
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
                x = cs.selected_frequency_marker()
                graph.draw_line((x, 0x2000), (x, 0xFFFF), color='#880000')
                # draw beacon level
                graph.draw_line((0, spectrum_data.beacon_level), (918, spectrum_data.beacon_level), color='#880000', width=1)
                # draw spectrum
                graph.draw_polygon(spectrum_data.points, fill_color='green')
            if server_pipe.poll():
                server_data = server_pipe.recv()
                while server_pipe.poll():
                    _ = server_pipe.recv()
                window['-PREAMP_TEMP-'].update(server_data.preamp_temp)
                window['-PA_CURRENT-'].update(server_data.pa_current)
                window['-PA_TEMP-'].update(server_data.pa_temp)
                window['-FANS-'].update(server_data.fans)
        else: # don't bother searching for __TIMEOUT__ events
            if event == '-SHUTDOWN-':
                #if sg.popup_yes_no('Shutdown Now?', background_color='red', keep_on_top=True) == 'Yes':
                break
            if event in dispatch_dictionary:
                # NOTE: initial control values are displayed by window.write_event_value('-DISPLAY_INITIAL_VALUES-', None)
                func_to_call = dispatch_dictionary[event]
                func_to_call()
                window['-BV-'].update(cs.curr_value.band)
                window['-FV-'].update(cs.curr_value.frequency)
                window['-SV-'].update(cs.curr_value.symbol_rate)
                window['-MODE_V-'].update(cs.curr_value.mode)
                window['-CODECS_V-'].update(cs.curr_value.codecs)
                window['-CONSTELLATION_V-'].update(cs.curr_value.constellation)
                window['-FEC_V-'].update(cs.curr_value.fec)
                window['-VIDEO_BITRATE_V-'].update(cs.curr_value.video_bitrate)
                window['-PROVIDER_V-'].update(cs.curr_value.provider)
                window['-SERVICE_V-'].update(cs.curr_value.service)
                window['-GAIN_V-'].update(cs.curr_value.gain)
                window['-TUNE-'].update(button_color=cs.tune_button_color)
                window['-PTT-'].update(button_color=cs.ptt_button_color)
    window.close()
    del window

if __name__ == '__main__':

    configure_devices()

    parent_spectrum_pipe, child_spectrum_pipe = Pipe()
    parent_server_pipe, child_server_pipe = Pipe()
    # create the process
    p_read_spectrum_data = Process(target=process_read_spectrum_data, args=(child_spectrum_pipe,))
    p_read_server_data = Process(target=process_read_server_data, args=(child_server_pipe,))
    # start the process
    p_read_spectrum_data.start()
    p_read_server_data.start()
    # main ui
    main_gui(parent_spectrum_pipe, parent_server_pipe)
    # kill 
    p_read_spectrum_data.kill()
    p_read_server_data.kill()

    shutdown_devices()

    # shutdown
    print('about to shut down')
    #import subprocess
    #subprocess.check_call(['sudo', 'poweroff'])
