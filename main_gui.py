"""TxTouch"""

from multiprocessing import Process
from multiprocessing import Pipe

import threading
from time import sleep

import PySimpleGUI as sg
import control_status as cs

from process_spectrum import process_read_spectrum_data, SpectrumData
from process_server import process_read_server_data, ServerData

from device_manager import configure_devices, shutdown_devices

""" LAYOUT FUNCTIONS ------------------------------ """

sg.theme('Black')
SCREEN_COLOR = '#111111'
NORMAL_BUTTON_COLOR = ('#FFFFFF','#222222')
   
def text_data(name, key):
    return sg.Text(name, size=11), sg.Text(' ', size=9, key=key, text_color='orange')

def incdec_but(name, key):
    return sg.Button(name, key=key, size=4, border_width=0, button_color=NORMAL_BUTTON_COLOR, mouseover_colors=NORMAL_BUTTON_COLOR)

def button_selector(key_down, value, key_up, width):
    return  incdec_but('<', key_down), sg.Text(' ', size=width, justification='center', key=value, text_color='orange'), incdec_but('>', key_up) 

""" LAYOUTS --------------------------------------- """

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
        button_selector('-MODE_D-', '-MODE_V-', '-MODE_U-', 8),
        button_selector('-CODECS_D-', '-CODECS_V-', '-CODECS_U-', 8),
        button_selector('-CONSTELLATION_D-', '-CONSTELLATION_V-', '-CONSTELLATION_U-', 8),
        button_selector('-FEC_D-', '-FEC_V-', '-FEC_U-', 8),
    ]),
    sg.Column([
        button_selector('-VIDEO_BITRATE_D-', '-VIDEO_BITRATE_V-', '-VIDEO_BITRATE_U-', 8),
        button_selector('-SPARE1_D-', '-SPARE1_V-', '-SPARE1_U-', 8),
        button_selector('-SPARE2_D-', '-SPARE2_V-', '-SPARE2_U-', 8),
        button_selector('-GAIN_D-', '-GAIN_V-', '-GAIN_U-', 8),
    ]),
    sg.Column([
        text_data('Preamp Temp', '-PREAMP_TEMP-'),
        text_data('PA Current', '-PA_CURRENT-'),
        text_data('PA Temp', '-PA_TEMP-'),
        text_data('Fans Running', '-FANS-'),
    ]),
    sg.Column([
        [sg.Button(' TUNE ', key='-TUNE-', border_width=0, button_color=NORMAL_BUTTON_COLOR, mouseover_colors=NORMAL_BUTTON_COLOR)],
        [sg.Text(' ')],
        [sg.Button(' PTT ', key='-PTT-', border_width=0, button_color=NORMAL_BUTTON_COLOR, mouseover_colors=NORMAL_BUTTON_COLOR)],
    ]),
]

layout = [
    top_layout,
    spectrum_layout,
    tune_layout,
    status_layout,
]

""" THREADS -------------------------------------- """

def spectrum_thread(window, pipe):
    while True:
        while pipe.poll():
            _ = pipe.recv()
            sleep(0.166)
            #print('dump spectrum data', flush= True)
        spectrum_data = pipe.recv()
        window.write_event_value('-SPECTRUM_THREAD-', (threading.current_thread().name, spectrum_data))

def server_thread(window, pipe):
    while True:
        while pipe.poll():
            _ = pipe.recv()
            sleep(0.5)
            #print('dump server data', flush= True)
        server_data = pipe.recv()
        window.write_event_value('-SERVER_THREAD-', (threading.current_thread().name, server_data))
            
""" MAIN ------------------------------------------ """

def main_gui(spectrum_pipe, server_pipe):
    window = sg.Window('', layout, size=(800, 480), font=(None,11), background_color=SCREEN_COLOR, use_default_focus=False, finalize=True)
    window.set_cursor('none')
    graph = window['graph']
    window['-TUNE-'].update(button_color=cs.tune_button_color)
    window['-PTT-'].update(button_color=cs.ptt_button_color)
    window['-BV-'].update(cs.curr_value.band)
    window['-FV-'].update(cs.curr_value.frequency)
    window['-SV-'].update(cs.curr_value.symbol_rate)
    window['-MODE_V-'].update(cs.curr_value.mode)
    window['-CODECS_V-'].update(cs.curr_value.codecs)
    window['-CONSTELLATION_V-'].update(cs.curr_value.constellation)
    window['-FEC_V-'].update(cs.curr_value.fec)
    window['-VIDEO_BITRATE_V-'].update(cs.curr_value.video_bitrate)
    window['-SPARE1_V-'].update(cs.curr_value.spare1)
    window['-SPARE2_V-'].update(cs.curr_value.spare2)
    window['-GAIN_V-'].update(cs.curr_value.gain)
    window.refresh()

    threading.Thread(target=spectrum_thread, args=(window, spectrum_pipe), daemon=True).start()
    threading.Thread(target=server_thread, args=(window, server_pipe), daemon=True).start()

    while True:
        event, values = window.read()
        #print(event)
        match event:
            case '-TUNE-':
                cs.tune()
                window['-TUNE-'].update(button_color=cs.tune_button_color)
                window['-PTT-'].update(button_color=cs.ptt_button_color)
            case '-PTT-':
                cs.ptt()
                window['-TUNE-'].update(button_color=cs.tune_button_color)
                window['-PTT-'].update(button_color=cs.ptt_button_color)
            case '-BD-':
                if cs.dec_band():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-BV-'].update(cs.curr_value.band)
            case '-BU-':
                if cs.inc_band():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-BV-'].update(cs.curr_value.band)
            case '-FD-':
                if cs.dec_frequency():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-FV-'].update(cs.curr_value.frequency)
            case '-FU-':
                if cs.inc_frequency():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-FV-'].update(cs.curr_value.frequency)
            case '-SD-':
                if cs.dec_symbol_rate():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-SV-'].update(cs.curr_value.symbol_rate)
            case '-SU-':
                if cs.inc_symbol_rate():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-SV-'].update(cs.curr_value.symbol_rate)
            case '-MODE_D-':
                if cs.dec_mode():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-MODE_V-'].update(cs.curr_value.mode)
            case '-MODE_U-':
                if cs.inc_mode():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-MODE_V-'].update(cs.curr_value.mode)
            case '-CODECS_D-':
                if cs.dec_codecs():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-CODECS_V-'].update(cs.curr_value.codecs)
            case '-CODECS_U-':
                if cs.inc_codecs():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-CODECS_V-'].update(cs.curr_value.codecs)
            case '-CONSTELLATION_D-':
                if cs.dec_constellation():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-CONSTELLATION_V-'].update(cs.curr_value.constellation)
            case '-CONSTELLATION_U-':
                if cs.inc_constellation():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-CONSTELLATION_V-'].update(cs.curr_value.constellation)
            case '-FEC_D-':
                if cs.dec_fec():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-FEC_V-'].update(cs.curr_value.fec)
            case '-FEC_U-':
                if cs.inc_fec():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-FEC_V-'].update(cs.curr_value.fec)
            case '-VIDEO_BITRATE_D-':
                if cs.dec_video_bitrate():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-VIDEO_BITRATE_V-'].update(cs.curr_value.video_bitrate)
            case '-VIDEO_BITRATE_U-':
                if cs.inc_video_bitrate():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-VIDEO_BITRATE_V-'].update(cs.curr_value.video_bitrate)
            case '-SPARE1_D-':
                if cs.dec_spare1():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-SPARE1_V-'].update(cs.curr_value.spare1)
            case '-SPARE1_U-':
                if cs.inc_spare1():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-SPARE1_V-'].update(cs.curr_value.spare1)
            case '-SPARE2_D-':
                if cs.dec_spare2():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-SPARE2_V-'].update(cs.curr_value.spare2)
            case '-SPARE2_U-':
                if cs.inc_spare2():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-SPARE2_V-'].update(cs.curr_value.spare2)
            case '-GAIN_D-':
                if cs.dec_gain():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-GAIN_V-'].update(cs.curr_value.gain)
            case '-GAIN_U-':
                if cs.inc_gain():
                    cs.cancel_tune()
                    window['-TUNE-'].update(button_color=cs.tune_button_color)
                    window['-PTT-'].update(button_color=cs.ptt_button_color)
                    window['-GAIN_V-'].update(cs.curr_value.gain)
            case '-SHUTDOWN-':
                #if sg.popup_yes_no('Shutdown Now?', background_color='red', keep_on_top=True) == 'Yes':
                cs.cancel_tune()
                window['-TUNE-'].update(button_color=cs.tune_button_color)
                window['-PTT-'].update(button_color=cs.ptt_button_color)
                window['-STATUS_BAR-'].update('Shutting down...')
                window.refresh()
                sleep(5)
                break
            case '-SPECTRUM_THREAD-':
                spectrum_data = values['-SPECTRUM_THREAD-'][1]
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
            case '-SERVER_THREAD-':
                server_data = values['-SERVER_THREAD-'][1]
                #window['-PREAMP_TEMP-'].update(server_data.preamp_temp)
                #window['-PA_CURRENT-'].update(server_data.pa_current)
                #window['-PA_TEMP-'].update(server_data.pa_temp)
                #window['-FANS-'].update(server_data.fans)

                # TODO: show one line
                msg = 'Pre {}, PA {} {}, Ein {} Eout {} PAin {} PAout {}'.format(
                    server_data.preamp_temp,
                    server_data.pa_temp,
                    server_data.pa_current,
                    '9999', '9999', '9999', '9999')
                window['-STATUS_BAR-'].update(msg)

    window.close()
    del window

if __name__ == '__main__':

    configure_devices()

    # TODO: consider using duplex=False

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
    print('about to shut down', flush=True)
    #import subprocess
    #args = ['/usr/bin/sudo', 'poweroff']
    #subprocess.check_call(args)
