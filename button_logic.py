#import

TUNED_MARKER = [
    # first Int16 represents 10490.500 MHz
    # last Int16 represents 10499.475 MHz
    # spectrum with = 10499.475 - 10490.500 = 8.975 Mhz
    # width between channels = 0.25 MHz
    103, # '10491.50 / 00' beacon
    230, # '10492.75 / 01'
    256, # '10493.00 / 02'
    281, # '10493.25 / 03'
    307, # '10493.50 / 04'
    332, # '10493.75 / 05'
    358, # '10494.00 / 06'
    383, # '10494.25 / 07'
    409, # '10494.50 / 08'
    434, # '10494.75 / 09'
    460, # '10495.00 / 10'
    485, # '10495.25 / 11'
    511, # '10495.50 / 12'
    536, # '10495.75 / 13'
    562, # '10496.00 / 14'
    588, # '10496.25 / 15'
    613, # '10496.50 / 16'
    639, # '10496.75 / 17'
    664, # '10497.00 / 18'
    690, # '10497.25 / 19'
    715, # '10497.50 / 20'
    741, # '10497.75 / 21'
    767, # '10490.00 / 22'
    792, # '10498.25 / 23'
    818, # '10498.50 / 24'
    843, # '10498.75 / 25'
    869, # '10499.00 / 26'
    894, # '10499.25 / 27'
]
BAND_LIST = [
    'Wide',
    'Narrow',
    'V.Narrow',
]
WIDE_FREQUENCY_LIST = [
    '2403.75 / 03',
    '2405.25 / 09',
    '2406.75 / 15',
]
NARROW_FREQUENCY_LIST = [
    '2403.25 / 01',
    '2403.75 / 03',
    '2404.25 / 05',
    '2404.75 / 07',
    '2405.25 / 09',
    '2405.75 / 11',
    '2406.25 / 13',
    '2406.75 / 15',
    '2407.25 / 17',
    '2407.75 / 19',
    '2408.25 / 21',
    '2408.75 / 23',
    '2409.25 / 25',
    '2409.75 / 27', # _f_index 13
]
V_NARROW_FREQUENCY_LIST = [
    '2403.25 / 01',
    '2403.50 / 02',
    '2403.75 / 03',
    '2404.00 / 04',
    '2404.25 / 05',
    '2404.50 / 06',
    '2404.75 / 07',
    '2405.00 / 08',
    '2405.25 / 09',
    '2405.50 / 10',
    '2405.75 / 11',
    '2406.00 / 12',
    '2406.25 / 13',
    '2406.50 / 14',
    '2406.75 / 15',
    '2407.00 / 16',
    '2407.25 / 17',
    '2407.50 / 18',
    '2407.75 / 19',
    '2408.00 / 20',
    '2408.25 / 21',
    '2408.50 / 22',
    '2408.75 / 23',
    '2409.00 / 24',
    '2409.25 / 25',
    '2409.50 / 26',
    '2409.75 / 27',
]
WIDE_SYMBOL_RATE_LIST = [
    '500',
    '1000',
    '1500',
]
NARROW_SYMBOL_RATE_LIST = [
    '125',
    '250',
    '333',
]
V_NARROW_SYMBOL_RATE_LIST = [
    '25',
    '33',
    '66',
]
MODE_LIST = [
    'DVB-S',
    'DVB-S2',
]
CODEC_LIST = [
    'H264 ACC',
    'H265 ACC',
]
CONSTELLATION_LIST = [
    'QPSK',
    '8PSK',
    '16PSK',
    '32PSK',
]
FEC_LIST = [
    '1/2',
    '2/3',
    '3/4',
    '4/5',
    '5/6',
    '6/7',
    '7/8',
    '8/9',
]
BITRATE_LIST = [
    '400','410','430',
]
PROVIDER_LIST = [
    'EA7KIR','G8WAA',
]
SERVICE_LIST = [
    'Malaga','Yorkshire'
]
GAIN_LIST = [
    '-10','-9','-8','-7','-6','-5','-4','-3','-2','-1','0',
]

WIDE_BAND_LIST_INDEX = 0
NARROW_BAND_LIST_INDEX = 1
V_NARROW_BAND_LIST_INDEX = 2

INITIAL_B           = 1 # narrow
INITIAL_WIDE_S      = 0 # 500
INITIAL_WIDE_F      = 2 # chan 15
INITIAL_NARROW_S    = 2 # 333
INITIAL_NARROW_F    = 13 # chan 27
INITIAL_V_NARROW_S  = 2 # 66
INITIAL_V_NARROW_F  = 0 # chan 01

class ButtonState:
    pass

class ButtonLogic:
    def __init__(self):
        self._b_index = INITIAL_B
        self._f_index = 0
        self._s_index = 0
        self._mode_index = 0
        self._codecs_index = 0
        self._constellation_index = 0
        self._fec_index = 0
        self._bitrate_index = 0
        self._provider_index = 0
        self._service_index = 0
        self._gain_index = 0
        self._prev_band = NARROW_BAND_LIST_INDEX
        self._prev_wide_f_index = 0
        self._prev_wide_s_index = 0
        self._prev_narrow_f_index = INITIAL_NARROW_F
        self._prev_narrow_s_index = 0
        self._prev_v_narrow_f_index = 0
        self._prev_v_narrow_s_index = 0
        self._change_band()
        self._update_variables()

    def _change_band(self):
        if self._b_index == WIDE_BAND_LIST_INDEX:
            self._curr_frequency_list = WIDE_FREQUENCY_LIST
            self._f_index = self._prev_wide_f_index
            self._curr_symbol_rate_list = WIDE_SYMBOL_RATE_LIST
            self._s_index = self._prev_wide_s_index
        elif self._b_index == NARROW_BAND_LIST_INDEX:
            self._curr_frequency_list = NARROW_FREQUENCY_LIST
            self._f_index = self._prev_narrow_f_index
            self._curr_symbol_rate_list = NARROW_SYMBOL_RATE_LIST
            self._s_index = self._prev_narrow_s_index
        elif self._b_index == V_NARROW_BAND_LIST_INDEX:
            self._curr_frequency_list = V_NARROW_FREQUENCY_LIST
            self._f_index = self._prev_v_narrow_f_index
            self._curr_symbol_rate_list = V_NARROW_SYMBOL_RATE_LIST
            self._s_index = self._prev_v_narrow_s_index

    def _update_variables(self):
        self.band = BAND_LIST[self._b_index]
        self.frequency = self._curr_frequency_list[self._f_index]
        self.symbol_rate = self._curr_symbol_rate_list[self._s_index]
        self.mode = MODE_LIST[self._mode_index]
        self.codecs = CODEC_LIST[self._codecs_index]
        self.constellation = CONSTELLATION_LIST[self._constellation_index]
        self.fec = FEC_LIST[self._fec_index]
        self.bitrate = BITRATE_LIST[self._bitrate_index]
        self.provider = PROVIDER_LIST[self._provider_index]
        self.service = SERVICE_LIST[self._service_index]
        self.gain = GAIN_LIST[self._gain_index]
        self.changed = True

    def dec_band(self):
        # TODO: there should be a check to see if the band is changed
        if self._b_index > 0:
            self._b_index -= 1
            self._change_band()
            self._update_variables()

    def inc_band(self):
        if self._b_index < len(BAND_LIST) - 1:
            self._b_index += 1
            self._change_band()
            self._update_variables()

    def dec_frequency(self):
        if self._f_index > 0:
            self._f_index -= 1
            self._update_variables()

    def inc_frequency(self):
        if self._f_index < len(self._curr_frequency_list) - 1:
            self._f_index += 1
            self._update_variables()

    def dec_symbol_rate(self):
        if self._s_index > 0:
            self._s_index -= 1
            self._update_variables()

    def inc_symbol_rate(self):
        if self._s_index < len(self._curr_symbol_rate_list) - 1:
            self._s_index += 1
            self._update_variables()

    def dec_mode(self):
        if self._mode_index > 0:
            self._mode_index -= 1
            self._update_variables()
            
    def inc_mode(self):
        if self._mode_index < len(MODE_LIST) - 1:
            self._mode_index += 1
            self._update_variables()
            
    def dec_codecs(self):
        if self._codecs_index > 0:
            self._codecs_index -= 1
            self._update_variables()
            
    def inc_codecs(self):
        if self._codecs_index < len(CODEC_LIST) - 1:
            self._codecs_index += 1
            self._update_variables()
            
    def dec_constellation(self):
        if self._constellation_index > 0:
            self._constellation_index -= 1
            self._update_variables()
            
    def inc_constellation(self):
        if self._constellation_index < len(CONSTELLATION_LIST) - 1:
            self._constellation_index += 1
            self._update_variables()
            
    def dec_fec(self):
        if self._fec_index > 0:
            self._fec_index -= 1
            self._update_variables()
            
    def inc_fec(self):
        if self._fec_index < len(FEC_LIST) - 1:
            self._fec_index += 1
            self._update_variables()

    def dec_bitrate(self):
        if self._bitrate_index > 0:
            self._bitrate_index -= 1
            self._update_variables()
            
    def inc_bitrate(self):
        if self._bitrate_index < len(BITRATE_LIST) - 1:
            self._bitrate_index += 1
            self._update_variables()

    def dec_provider(self):
        if self._provider_index > 0:
            self._provider_index -= 1
            self._update_variables()
            
    def inc_provider(self):
        if self._provider_index < len(PROVIDER_LIST) - 1:
            self._provider_index += 1
            self._update_variables()

    def dec_service(self):
        if self._service_index > 0:
            self._service_index -= 1
            self._update_variables()
            
    def inc_service(self):
        if self._service_index < len(SERVICE_LIST) - 1:
            self._service_index += 1
            self._update_variables()

    def dec_gain(self):
        if self._gain_index > 0:
            self._gain_index -= 1
            self._update_variables()
            
    def inc_gain(self):
        if self._gain_index < len(GAIN_LIST) - 1:
            self._gain_index += 1
            self._update_variables()

    def selected_frequency_marker(self):
        i = int(self.frequency[9:])
        return TUNED_MARKER[i]

button_logic = ButtonLogic()

