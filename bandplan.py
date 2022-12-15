# bandplan.py

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

WIDE_BAND_LIST_INDEX = 0
NARROW_BAND_LIST_INDEX = 1
V_NARROW_BAND_LIST_INDEX = 2

class BandPlan():
    def __init__(self):
        self._b_index = 0
        self._f_index = 0
        self._s_index = 0
        self._mode_index = 0
        self._codecs_index = 0
        self._constellation_index = 0
        self._fec_index = 0
        self._prev_band = 0
        self._prev_wide_f_index = 0
        self._prev_wide_s_index = 0
        self._prev_narrow_f_index = 0
        self._prev_narrow_s_index = 0
        self._prev_v_narrow_f_index = 0
        self._prev_v_narrow_s_index = 0
        #self._prev_codecs
        self._change_band()
        self._update_variables()

    def _update_variables(self):
        self.band = BAND_LIST[self._b_index]
        self.frequency = self._curr_frequency_list[self._f_index]
        self.symbol_rate = self._curr_symbol_rate_list[self._s_index]
        self.mode = MODE_LIST[self._mode_index]
        self.codecs = CODEC_LIST[self._codecs_index]
        self.constellation = CONSTELLATION_LIST[self._constellation_index]
        self.fec = FEC_LIST[self._fec_index]
        self.changed = True

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
            
    def dec_mode(self):
        #self._prev_codecs_index = self._codecs_index
        if self._mode_index > 0:
            self._mode_index -= 1
            self._update_variables()
            
    def inc_mode(self):
        if self._mode_index < len(MODE_LIST) - 1:
            self._mode_index += 1
            #self._change_band()
            self._update_variables()
            
    def dec_codecs(self):
        #self._prev_codecs_index = self._codecs_index
        if self._codecs_index > 0:
            self._codecs_index -= 1
            self._update_variables()
            
    def inc_codecs(self):
        if self._codecs_index < len(CODEC_LIST) - 1:
            self._codecs_index += 1
            #self._change_band()
            self._update_variables()
            
    def dec_constellation(self):
        if self._constellation_index > 0:
            self._constellation_index -= 1
            self._update_variables()
            
    def inc_constellation(self):
        if self._constellation_index < len(CONSTELLATION_LIST) - 1:
            self._constellation_index += 1
            #self._change_band()
            self._update_variables()
            
    def dec_fec(self):
        if self._fec_index > 0:
            self._fec_index -= 1
            self._update_variables()
            
    def inc_fec(self):
        if self._fec_index < len(FEC_LIST) - 1:
            self._fec_index += 1
            #self._change_band()
            self._update_variables()

    # ----------------------------------

    def dec_band(self):
        self._prev_b_index = self._b_index
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

    def frequency_and_rate(self):
        #rate_list:str = []
        #if self.symbol_rate == 'AUTO':
        #    for i in range(1, len(self._curr_symbol_rate_list)):
        #        rate_list.append(self._curr_symbol_rate_list[i])
        #else:
        #    rate_list = [self.symbol_rate]
        return self.frequency[:7], self.symbol_rate



bandplan = BandPlan()

