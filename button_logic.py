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

class Value:
    band:str = '-'
    frequency:str = '-'
    symbol_rate:str = '-'
    mode:str = '-'
    codecs:str = '-'
    constellation:str = '-'
    fec:str = '-'
    bitrate:str = '-'
    provider:str = '-'
    service:str = '-'
    gain:str = '-'
    def __init__(self, name):
        band = name

class Index:
    band = 0
    frequency = 0
    symbol_rate = 0
    mode = 0
    codecs = 0
    constellation = 0
    fec = 0
    bitrate = 0
    provider = 0
    service = 0
    gain = 0
    def __init__(self, number):
        band = number

value = [ Value(BAND_LIST[0]), Value(BAND_LIST[1]), Value(BAND_LIST[2]) ]
index = [ Index(0), Index(1), Index(2) ]

curr_band = 0
curr_value = value[curr_band]
curr_index = index[curr_band]

frequency_list = [ WIDE_FREQUENCY_LIST, NARROW_FREQUENCY_LIST, V_NARROW_FREQUENCY_LIST ]
synbol_rate_list = [ WIDE_SYMBOL_RATE_LIST, NARROW_SYMBOL_RATE_LIST, V_NARROW_SYMBOL_RATE_LIST ]
max_frequency_index = [ len(WIDE_FREQUENCY_LIST) - 1, len(NARROW_FREQUENCY_LIST) - 1, len(V_NARROW_FREQUENCY_LIST) - 1 ]
max_symbol_rate_index = [ len(WIDE_SYMBOL_RATE_LIST) - 1, len(NARROW_SYMBOL_RATE_LIST) - 1, len(V_NARROW_SYMBOL_RATE_LIST) - 1 ]

def inc_band():
    global curr_band, curr_value, curr_index
    if curr_band < len(BAND_LIST) - 1:
        curr_band += 1
        curr_value = value[curr_band]
        curr_index = index[curr_band]

def dec_band():
    global curr_band
    if curr_band > 0:
        curr_band -= 1
        curr_value = value[curr_band]
        curr_index = index[curr_band]
    
def inc_frequency():
    global curr_band
    if curr_index.frequency < max_frequency_index[curr_band]:
        curr_index.frequency += 1
        curr_value.frequency = frequency_list[curr_band][curr_index.frequency]

def dec_frequency():
    if curr_index.frequency > 0:
        curr_index.frequency -= 1
        curr_value.frequency = frequency_list[curr_band][curr_index.frequency]
    
def inc_symbol_rate():
    global curr_band
    if curr_index.symbol_rate < max_symbol_rate_index[curr_band]:
        curr_index.symbol_rate += 1
        curr_value.symbol_rate = synbol_rate_list[curr_band][curr_index.symbol_rate]

def dec_symbol_rate():
    global curr_band
    if curr_index.symbol_rate > 0:
        curr_index.symbol_rate -= 1
        curr_value.symbol_rate = synbol_rate_list[curr_band][curr_index.symbol_rate]
    
def inc_mode():
    if curr_index.mode < len(MODE_LIST) - 1:
        curr_index.mode += 1
        curr_value.mode = MODE_LIST[curr_index.mode]

def dec_mode():
    if curr_index.mode > 0:
        curr_index.mode -= 1
        curr_value.mode = MODE_LIST[curr_index.mode]
    
def inc_codecs():
    if curr_index.codecs < len(CODEC_LIST) - 1:
        curr_index.codecs += 1
        curr_value.codecs = CODEC_LIST[curr_index.codecs]

def dec_codecs():
    if curr_index.codecs > 0:
        curr_index.codecs -= 1
        curr_value.codecs = CODEC_LIST[curr_index.codecs]
    
def inc_constellation():
    if curr_index.constellation < len(CONSTELLATION_LIST) - 1:
        curr_index.constellation += 1
        curr_value.constellation = CONSTELLATION_LIST[curr_index.constellation]

def dec_constellation():
    if curr_index.constellation > 0:
        curr_index.constellation -= 1
        curr_value.constellation = CONSTELLATION_LIST[curr_index.constellation]
    
def inc_fec():
    if curr_index.fec < len(FEC_LIST) - 1:
        curr_index.fec += 1
        curr_value.fec = FEC_LIST[curr_index.fec]

def dec_fec():
    if curr_index.fec > 0:
        curr_index.fec -= 1
        curr_value.fec = FEC_LIST[curr_index.fec]
    
def inc_bitrate():
    if curr_index.bitrate < len(BITRATE_LIST) - 1:
        curr_index.bitrate += 1
        curr_value.bitrate = BITRATE_LIST[curr_index.bitrate]

def dec_bitrate():
    if curr_index.bitrate > 0:
        curr_index.bitrate -= 1
        curr_value.bitrate = BITRATE_LIST[curr_index.mode]
    
def inc_provider():
    if curr_index.provider < len(PROVIDER_LIST) - 1:
        curr_index.provider += 1
        curr_value.provider = PROVIDER_LIST[curr_index.provider]

def dec_provider():
     if curr_index.provider > 0:
        curr_index.provider -= 1
        curr_value.provider = PROVIDER_LIST[curr_index.provider]
   
def inc_service():
    if curr_index.service < len(SERVICE_LIST) - 1:
        curr_index.service += 1
        curr_value.service = SERVICE_LIST[curr_index.service]

def dec_service():
    if curr_index.service > 0:
        curr_index.service -= 1
        curr_value.service = SERVICE_LIST[curr_index.service]
    
def inc_gain():
    if curr_index.gain < len(GAIN_LIST) - 1:
        curr_index.gain += 1
        curr_value.gain = GAIN_LIST[curr_index.gain]

def dec_gain():
     if curr_index.gain > 0:
        curr_index.gain -= 1
        curr_value.gain = GAIN_LIST[curr_index.gain]

def selected_frequency_marker():
    #print(curr_value.frequency, curr_value.frequency[9:])
    i = 1 # int(curr_value.frequency[9:])
    return TUNED_MARKER[i]


########### OLD #############################################
"""
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
"""
