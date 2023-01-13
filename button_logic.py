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
    'Wide','Narrow','V.Narrow',
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
VERY_NARROW_FREQUENCY_LIST = [
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
    '500','1000','1500',
]
NARROW_SYMBOL_RATE_LIST = [
    '125','250','333',
]
VERY_NARROW_SYMBOL_RATE_LIST = [
    '25','33','66',
]
WIDE_MODE_LIST = [
    'DVB-S','DVB-S2',
]
NARROW_MODE_LIST = [
    'DVB-S','DVB-S2',
]
VERY_NARROW_MODE_LIST = [
    'DVB-S','DVB-S2',
]
WIDE_CODECS_LIST = [
    'H264 ACC','H265 ACC',
]
NARROW_CODECS_LIST = [
    'H264 ACC','H265 ACC',
]
VERY_NARROW_CODECS_LIST = [
    'H264 ACC','H265 ACC',
]
WIDE_CONSTELLATION_LIST = [
    'QPSK','8PSK','16PSK','32PSK',
]
NARROW_CONSTELLATION_LIST = [
    'QPSK','8PSK','16PSK','32PSK',
]
VERY_NARROW_CONSTELLATION_LIST = [
    'QPSK','8PSK','16PSK','32PSK',
]
WIDE_FEC_LIST = [
    '1/2','2/3','3/4','4/5','5/6','6/7','7/8','8/9',
]
NARROW_FEC_LIST = [
    '1/2','2/3','3/4','4/5','5/6','6/7','7/8','8/9',
]
VERY_NARROW_FEC_LIST = [
    '1/2','2/3','3/4','4/5','5/6','6/7','7/8','8/9',
]
WIDE_BITRATE_LIST = [
    '400','410','430',
]
NARROW_BITRATE_LIST = [
    '400','410','430',
]
VERY_NARROW_BITRATE_LIST = [
    '400','410','430',
]
WIDE_PROVIDER_LIST = [
    'EA7KIR','G8WAA',
]
NARROW_PROVIDER_LIST = [
    'EA7KIR','G8WAA',
]
VERY_NARROW_PROVIDER_LIST = [
    'EA7KIR','G8WAA',
]
WIDE_SERVICE_LIST = [
    'Malaga','Yorkshire'
]
NARROW_SERVICE_LIST = [
    'Malaga','Yorkshire'
]
VERY_NARROW_SERVICE_LIST = [
    'Malaga','Yorkshire'
]
WIDE_GAIN_LIST = [
    '-10','-9','-8','-7','-6','-5','-4','-3','-2','-1','0',
]
NARROW_GAIN_LIST = [
    '-10','-9','-8','-7','-6','-5','-4','-3','-2','-1','0',
]
VERY_NARROW_GAIN_LIST = [
    '-10','-9','-8','-7','-6','-5','-4','-3','-2','-1','0',
]

WIDE_BAND_LIST_INDEX = 0
NARROW_BAND_LIST_INDEX = 1
VERY_NARROW_BAND_LIST_INDEX = 2

INITIAL_BAND                        = 1 # narrow

INITIAL_WIDE_SYMBOL_RATE            = 0 # 500
INITIAL_WIDE_FREQUENCY              = 2 # chan 15
INITIAL_WIDE_MODE                   = 1 # DVB-S2
INITIAL_WIDE_CODEC                  = 1 # H265 ACC
INITIAL_WIDE_CONSTELLATION          = 0 # QPSK
INITIAL_WIDE_FEC                    = 2 # 3/4
INITIAL_WIDE_BITRATE                = 1 # 410
INITIAL_WIDE_PROVIDER               = 0 # EA7KIR
INITIAL_WIDE_SERVICE                = 0 # Malaga
INITIAL_WIDE_GAIN                   = 3 # -7

INITIAL_NARROW_SYMBOL_RATE          = 2 # 333
INITIAL_NARROW_FREQUENCY            = 13 # chan 27
INITIAL_NARROW_MODE                 = 1 # DVB-S2
INITIAL_NARROW_CODEC                = 1 # H265 ACC
INITIAL_NARROW_CONSTELLATION        = 0 # QPSK
INITIAL_NARROW_FEC                  = 2 # 3/4
INITIAL_NARROW_BITRATE              = 1 # 410
INITIAL_NARROW_PROVIDER             = 0 # EA7KIR
INITIAL_NARROW_SERVICE              = 0 # Malaga
INITIAL_NARROW_GAIN                 = 3 # -7

INITIAL_VERY_NARROW_SYMBOL_RATE     = 2 # 66
INITIAL_VERY_NARROW_FREQUENCY       = 0 # chan 01
INITIAL_VERY_NARROW_MODE            = 1 # DVB-S2
INITIAL_VERY_NARROW_CODEC           = 1 # H265 ACC
INITIAL_VERY_NARROW_CONSTELLATION   = 0 # QPSK
INITIAL_VERY_NARROW_FEC             = 2 # 3/4
INITIAL_VERY_NARROW_BITRATE         = 1 # 410
INITIAL_VERY_NARROW_PROVIDER        = 0 # EA7KIR
INITIAL_VERY_NARROW_SERVICE         = 0 # Malaga
INITIAL_VERY_NARROW_GAIN            = 3 # -7

class WideIndex:
    band = WIDE_BAND_LIST_INDEX
    frequency = INITIAL_WIDE_FREQUENCY
    symbol_rate = INITIAL_WIDE_SYMBOL_RATE
    mode = INITIAL_WIDE_MODE
    codecs = INITIAL_WIDE_CODEC
    constellation = INITIAL_WIDE_CONSTELLATION
    fec = INITIAL_WIDE_FEC
    bitrate = INITIAL_WIDE_BITRATE
    provider = INITIAL_WIDE_PROVIDER
    service = INITIAL_WIDE_SERVICE
    gain = INITIAL_WIDE_GAIN
    frequency_list = WIDE_FREQUENCY_LIST
    max_frequency_index = len(WIDE_FREQUENCY_LIST) - 1
    symbol_rate_list = WIDE_SYMBOL_RATE_LIST
    max_symbol_rate_list = len(WIDE_SYMBOL_RATE_LIST) - 1
    mode_list = WIDE_MODE_LIST
    max_mode_list = len(WIDE_MODE_LIST) - 1
    codecs_list = WIDE_CODECS_LIST
    max_codecs_list = len(WIDE_CODECS_LIST) - 1
    constellation_list = WIDE_CONSTELLATION_LIST
    max_constellation_list = len(WIDE_CONSTELLATION_LIST) - 1
    fec_list = WIDE_FEC_LIST
    max_fec_list = len(WIDE_FEC_LIST) - 1
    bitrate_list = WIDE_BITRATE_LIST
    max_bitrate_list = len(WIDE_BITRATE_LIST) - 1
    provider_list = WIDE_PROVIDER_LIST
    max_provider_list = len(WIDE_PROVIDER_LIST) - 1
    service_list = WIDE_SERVICE_LIST
    max_service_list = len(WIDE_SERVICE_LIST) - 1
    gain_list = WIDE_GAIN_LIST
    max_gain_list = len(WIDE_GAIN_LIST) - 1

class NarrowIndex:
    band = NARROW_BAND_LIST_INDEX
    frequency = INITIAL_NARROW_FREQUENCY
    symbol_rate = INITIAL_NARROW_SYMBOL_RATE
    mode = INITIAL_NARROW_MODE
    codecs = INITIAL_NARROW_CODEC
    constellation = INITIAL_NARROW_CONSTELLATION
    fec = INITIAL_NARROW_FEC
    bitrate = INITIAL_NARROW_BITRATE
    provider = INITIAL_NARROW_PROVIDER
    service = INITIAL_NARROW_SERVICE
    gain = INITIAL_NARROW_GAIN
    frequency_list = NARROW_FREQUENCY_LIST
    max_frequency_index = len(NARROW_FREQUENCY_LIST) - 1
    symbol_rate_list = NARROW_SYMBOL_RATE_LIST
    max_symbol_rate_list = len(NARROW_SYMBOL_RATE_LIST) - 1
    mode_list = NARROW_MODE_LIST
    max_mode_list = len(NARROW_MODE_LIST) - 1
    codecs_list = NARROW_CODECS_LIST
    max_codecs_list = len(NARROW_CODECS_LIST) - 1
    constellation_list = NARROW_CONSTELLATION_LIST
    max_constellation_list = len(NARROW_CONSTELLATION_LIST) - 1
    fec_list = NARROW_FEC_LIST
    max_fec_list = len(NARROW_FEC_LIST) - 1
    bitrate_list = NARROW_BITRATE_LIST
    max_bitrate_list = len(NARROW_BITRATE_LIST) - 1
    provider_list = NARROW_PROVIDER_LIST
    max_provider_list = len(NARROW_PROVIDER_LIST) - 1
    service_list = NARROW_SERVICE_LIST
    max_service_list = len(NARROW_SERVICE_LIST) - 1
    gain_list = NARROW_GAIN_LIST
    max_gain_list = len(NARROW_GAIN_LIST) - 1

class VeryNarrowIndex:
    band = VERY_NARROW_BAND_LIST_INDEX
    frequency = INITIAL_VERY_NARROW_FREQUENCY
    symbol_rate = INITIAL_VERY_NARROW_SYMBOL_RATE
    mode = INITIAL_VERY_NARROW_MODE
    codecs = INITIAL_VERY_NARROW_CODEC
    constellation = INITIAL_VERY_NARROW_CONSTELLATION
    fec = INITIAL_VERY_NARROW_FEC
    bitrate = INITIAL_VERY_NARROW_BITRATE
    provider = INITIAL_VERY_NARROW_PROVIDER
    service = INITIAL_VERY_NARROW_SERVICE
    gain = INITIAL_VERY_NARROW_GAIN
    frequency_list = VERY_NARROW_FREQUENCY_LIST
    max_frequency_index = len(VERY_NARROW_FREQUENCY_LIST) - 1
    symbol_rate_list = VERY_NARROW_SYMBOL_RATE_LIST
    max_symbol_rate_list = len(VERY_NARROW_SYMBOL_RATE_LIST) - 1
    mode_list = VERY_NARROW_MODE_LIST
    max_mode_list = len(VERY_NARROW_MODE_LIST) - 1
    codecs_list = VERY_NARROW_CODECS_LIST
    max_codecs_list = len(VERY_NARROW_CODECS_LIST) - 1
    constellation_list = VERY_NARROW_CONSTELLATION_LIST
    max_constellation_list = len(VERY_NARROW_CONSTELLATION_LIST) - 1
    fec_list = VERY_NARROW_FEC_LIST
    max_fec_list = len(VERY_NARROW_FEC_LIST) - 1
    bitrate_list = VERY_NARROW_BITRATE_LIST
    max_bitrate_list = len(VERY_NARROW_BITRATE_LIST) - 1
    provider_list = VERY_NARROW_PROVIDER_LIST
    max_provider_list = len(VERY_NARROW_PROVIDER_LIST) - 1
    service_list = VERY_NARROW_SERVICE_LIST
    max_service_list = len(VERY_NARROW_SERVICE_LIST) - 1
    gain_list = VERY_NARROW_GAIN_LIST
    max_gain_list = len(VERY_NARROW_GAIN_LIST) - 1


index = [ WideIndex, NarrowIndex, VeryNarrowIndex ]

class  WideValue:
    band = BAND_LIST[WideIndex.band]
    frequency = WIDE_FREQUENCY_LIST[WideIndex.frequency]
    symbol_rate = WIDE_SYMBOL_RATE_LIST[WideIndex.symbol_rate]
    mode = WIDE_MODE_LIST[WideIndex.mode]
    codecs = WIDE_CODECS_LIST[WideIndex.codecs]
    constellation = WIDE_CONSTELLATION_LIST[WideIndex.constellation]
    fec = WIDE_FEC_LIST[WideIndex.fec]
    bitrate = WIDE_BITRATE_LIST[WideIndex.bitrate]
    provider = WIDE_PROVIDER_LIST[WideIndex.provider]
    service = WIDE_SERVICE_LIST[WideIndex.service]
    gain = WIDE_GAIN_LIST[WideIndex.gain]

class NarrowValue:
    band = BAND_LIST[NarrowIndex.band]
    frequency = NARROW_FREQUENCY_LIST[NarrowIndex.frequency]
    symbol_rate = NARROW_SYMBOL_RATE_LIST[NarrowIndex.symbol_rate]
    mode = NARROW_MODE_LIST[NarrowIndex.mode]
    codecs = NARROW_CODECS_LIST[NarrowIndex.codecs]
    constellation = NARROW_CONSTELLATION_LIST[NarrowIndex.constellation]
    fec = NARROW_FEC_LIST[NarrowIndex.fec]
    bitrate = NARROW_BITRATE_LIST[NarrowIndex.bitrate]
    provider = NARROW_PROVIDER_LIST[NarrowIndex.provider]
    service = NARROW_SERVICE_LIST[NarrowIndex.service]
    gain = NARROW_GAIN_LIST[NarrowIndex.gain]

class VeryNarrowValue:
    band = BAND_LIST[VeryNarrowIndex.band]
    frequency = VERY_NARROW_FREQUENCY_LIST[VeryNarrowIndex.frequency]
    symbol_rate = VERY_NARROW_SYMBOL_RATE_LIST[VeryNarrowIndex.symbol_rate]
    mode = VERY_NARROW_MODE_LIST[VeryNarrowIndex.mode]
    codecs = VERY_NARROW_CODECS_LIST[VeryNarrowIndex.codecs]
    constellation = VERY_NARROW_CONSTELLATION_LIST[VeryNarrowIndex.constellation]
    fec = VERY_NARROW_FEC_LIST[VeryNarrowIndex.fec]
    bitrate = VERY_NARROW_BITRATE_LIST[VeryNarrowIndex.bitrate]
    provider = VERY_NARROW_PROVIDER_LIST[VeryNarrowIndex.provider]
    service = VERY_NARROW_SERVICE_LIST[VeryNarrowIndex.service]
    gain = VERY_NARROW_GAIN_LIST[VeryNarrowIndex.gain]

value = [ WideValue, NarrowValue, VeryNarrowValue ]

curr_band = INITIAL_BAND
curr_value = value[curr_band]
curr_index = index[curr_band]
max_band_list = len(BAND_LIST) - 1 # TODO: messy!  try integrating band into the Index classes

def inc_band():
    global curr_band, max_band_list, curr_value, curr_index
    if curr_band < max_band_list:
        curr_band += 1
        curr_value = value[curr_band]
        curr_index = index[curr_band]

def dec_band():
    global curr_band, curr_value, curr_index
    if curr_band > 0:
        curr_band -= 1
        curr_value = value[curr_band]
        curr_index = index[curr_band]
    
def inc_frequency():
    global curr_value, curr_index
    if curr_index.frequency < curr_index.max_frequency_index:
        curr_index.frequency += 1
        curr_value.frequency = curr_index.frequency_list[curr_index.frequency]

def dec_frequency():
    global curr_value, curr_index
    if curr_index.frequency > 0:
        curr_index.frequency -= 1
        curr_value.frequency = curr_index.frequency_list[curr_index.frequency]
    
def inc_symbol_rate():
    global curr_value, curr_index
    if curr_index.symbol_rate < curr_index.max_symbol_rate_list:
        curr_index.symbol_rate += 1
        curr_value.symbol_rate = curr_index.symbol_rate_list[curr_index.symbol_rate]

def dec_symbol_rate():
    global curr_value, curr_index
    if curr_index.symbol_rate > 0:
        curr_index.symbol_rate -= 1
        curr_value.symbol_rate = curr_index.symbol_rate_list[curr_index.symbol_rate]
    
def inc_mode():
    global curr_value, curr_index
    if curr_index.mode < curr_index.max_mode_list:
        curr_index.mode += 1
        curr_value.mode = curr_index.mode_list[curr_index.mode]

def dec_mode():
    global curr_value, curr_index
    if curr_index.mode > 0:
        curr_index.mode -= 1
        curr_value.mode = curr_index.mode_list[curr_index.mode]

def inc_codecs():
    global curr_value, curr_index
    if curr_index.codecs < curr_index.max_codecs_list:
        curr_index.codecs += 1
        curr_value.codecs = curr_index.codecs_list[curr_index.codecs]

def dec_codecs():
    global curr_value, curr_index
    if curr_index.codecs > 0:
        curr_index.codecs -= 1
        curr_value.codecs = curr_index.codecs_list[curr_index.codecs]
    
def inc_constellation():
    global curr_value, curr_index
    if curr_index.constellation < curr_index.max_constellation_list:
        curr_index.constellation += 1
        curr_value.constellation = curr_index.constellation_list[curr_index.constellation]

def dec_constellation():
    global curr_value, curr_index
    if curr_index.constellation > 0:
        curr_index.constellation -= 1
        curr_value.constellation = curr_index.constellation_list[curr_index.constellation]
    
def inc_fec():
    global curr_value, curr_index
    if curr_index.fec < curr_index.max_fec_list:
        curr_index.fec += 1
        curr_value.fec = curr_index.fec_list[curr_index.fec]

def dec_fec():
    global curr_value, curr_index
    if curr_index.fec > 0:
        curr_index.fec -= 1
        curr_value.fec = curr_index.fec_list[curr_index.fec]
    
def inc_bitrate():
    global curr_value, curr_index
    if curr_index.bitrate < curr_index.max_bitrate_list:
        curr_index.bitrate += 1
        curr_value.bitrate = curr_index.bitrate_list[curr_index.bitrate]

def dec_bitrate():
    global curr_value, curr_index
    if curr_index.bitrate > 0:
        curr_index.bitrate -= 1
        curr_value.bitrate = curr_index.bitrate_list[curr_index.bitrate]
    
def inc_provider():
    global curr_value, curr_index
    if curr_index.provider < curr_index.max_provider_list:
        curr_index.provider += 1
        curr_value.provider = curr_index.provider_list[curr_index.provider]

def dec_provider():
    global curr_value, curr_index
    if curr_index.provider > 0:
        curr_index.provider -= 1
        curr_value.provider = curr_index.provider_list[curr_index.provider]
   
def inc_service():
    global curr_value, curr_index
    if curr_index.service < curr_index.max_service_list:
        curr_index.service += 1
        curr_value.service = curr_index.service_list[curr_index.service]

def dec_service():
    global curr_value, curr_index
    if curr_index.service > 0:
        curr_index.service -= 1
        curr_value.service = curr_index.service_list[curr_index.service]
    
def inc_gain():
    global curr_value, curr_index
    if curr_index.gain < curr_index.max_gain_list:
        curr_index.gain += 1
        curr_value.gain = curr_index.gain_list[curr_index.gain]

def dec_gain():
    global curr_value, curr_index
    if curr_index.gain > 0:
        curr_index.gain -= 1
        curr_value.gain = curr_index.gain_list[curr_index.gain]

def selected_frequency_marker():
    i = int(curr_value.frequency[9:])
    return TUNED_MARKER[i]

class EncoderArgs:
    codecs = ''
    bitrate = ''

def encoder_args():
    global curr_value
    EncoderArgs.codecs = curr_value.codecs
    EncoderArgs.bitrate = curr_value.bitrate
    return EncoderArgs

class TuneArgs:
    frequency = ''
    symbol_rate = ''
    mode = ''
    constellation = ''
    fec = ''
    provider = ''
    service = ''
    gain = ''

def tune_args():
    global curr_value
    TuneArgs.frequency = curr_value.frequency[:7]
    TuneArgs.symbol_rate = curr_value.symbol_rate
    TuneArgs.mode = curr_value.mode
    TuneArgs.constellation = curr_value.constellation
    TuneArgs.fec = curr_value.fec
    TuneArgs.provider = curr_value.provider
    TuneArgs.service = curr_value.service
    TuneArgs.gain = curr_value.gain
    return TuneArgs 

    """
    # Eg: "rtmp://192.168.1.40:7272/,2409.75,DVBS2,QPSK,333,23,-2,nocalib,800,32,/,EA7KIR,"

    s =  f'rtmp://{IP},{PORT},{frequency},{mode},{constellation},{symbol_rate},{fec},{gain},nocalib,800,32,/,{provider},'

    IP = '192.168.1.40'
    PORT = '7277' or '8282'
    frequency = '2409.75'
    mode = 'DVBS2'
    constellation = 'QPSK'
    fec = '23'
    gain = '-2'
    provider = 'EA7KIR'
    """
