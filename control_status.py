from device_manager import activate_encoder, deactivate_encoder
from device_manager import activate_pluto, deactivate_pluto
from device_manager import activate_ptt, deactivate_ptt
from device_constants import PLUTO_ADDRESS, PROVIDER_NAME, SERVICE_NAME

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
    '1000','1500','2000',
]
NARROW_SYMBOL_RATE_LIST = [
    '250','333','500',
]
VERY_NARROW_SYMBOL_RATE_LIST = [
    '33','66','125',
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
    '290','300','310','330','340','350','360',
]
NARROW_BITRATE_LIST = [
    '290','300','310','330','340','350','360',
]
VERY_NARROW_BITRATE_LIST = [
    '290','300','310','330','340','350','360',
]
WIDE_SPARE1_LIST = [
    'sp1-a','sp1-b',
]
NARROW_SPARE1_LIST = [
    'sp1-a','sp1-b',
]
VERY_NARROW_SPARE1_LIST = [
    'sp1-a','sp1-b',
]
WIDE_SPARE2_LIST = [
    'sp2-a','sp2-b'
]
NARROW_SPARE2_LIST = [
    'sp2-a','sp2-b'
]
VERY_NARROW_SPARE2_LIST = [
    'sp2-a','sp2-b'
]
WIDE_GAIN_LIST = [
    '-20','-19','-18','-17','-16','-15','-14','-13','-12','-11','-10','-9','-8','-7','-6','-5','-4','-3','-2','-1','0',
]
NARROW_GAIN_LIST = [
    '-20','-19','-18','-17','-16','-15','-14','-13','-12','-11','-10','-9','-8','-7','-6','-5','-4','-3','-2','-1','0',
]
VERY_NARROW_GAIN_LIST = [
    '-20','-19','-18','-17','-16','-15','-14','-13','-12','-11','-10','-9','-8','-7','-6','-5','-4','-3','-2','-1','0',
]

WIDE_BAND_LIST_INDEX = 0
NARROW_BAND_LIST_INDEX = 1
VERY_NARROW_BAND_LIST_INDEX = 2

INITIAL_BAND                        = 1 # narrow

# See: https://www.f5uii.net/en/transmit-datv-over-qo100-with-sdr-adalm-pluto-f5oeo-plutodvb/11/

INITIAL_WIDE_SYMBOL_RATE            = 1 # 1500
INITIAL_WIDE_FREQUENCY              = 2 # chan 15
INITIAL_WIDE_MODE                   = 1 # DVB-S2
INITIAL_WIDE_CODEC                  = 1 # H265 ACC
INITIAL_WIDE_CONSTELLATION          = 0 # QPSK
INITIAL_WIDE_FEC                    = 2 # 3/4
INITIAL_WIDE_BITRATE                = 3 # 330
INITIAL_WIDE_SPARE1                 = 0 # sp1_a 
INITIAL_WIDE_SPARE2                 = 0 # sp2_a
INITIAL_WIDE_GAIN                   = 4 # -16

INITIAL_NARROW_SYMBOL_RATE          = 1 # 333
INITIAL_NARROW_FREQUENCY            = 13 # chan 27
INITIAL_NARROW_MODE                 = 1 # DVB-S2
INITIAL_NARROW_CODEC                = 1 # H265 ACC
INITIAL_NARROW_CONSTELLATION        = 0 # QPSK
INITIAL_NARROW_FEC                  = 2 # 3/4
INITIAL_NARROW_BITRATE              = 3 # 330
INITIAL_NARROW_SPARE1               = 0 # sp1_a
INITIAL_NARROW_SPARE2               = 0 # sp2_a
INITIAL_NARROW_GAIN                 = 4 # -16

INITIAL_VERY_NARROW_SYMBOL_RATE     = 1 # 66
INITIAL_VERY_NARROW_FREQUENCY       = 0 # chan 01
INITIAL_VERY_NARROW_MODE            = 1 # DVB-S2
INITIAL_VERY_NARROW_CODEC           = 1 # H265 ACC
INITIAL_VERY_NARROW_CONSTELLATION   = 0 # QPSK
INITIAL_VERY_NARROW_FEC             = 2 # 3/4
INITIAL_VERY_NARROW_BITRATE         = 3 # 330
INITIAL_VERY_NARROW_SPARE1          = 0 # sp1_a 
INITIAL_VERY_NARROW_SPARE2          = 0 # sp2_a 
INITIAL_VERY_NARROW_GAIN            = 4 # -16

class WideIndex:
    band = WIDE_BAND_LIST_INDEX
    frequency = INITIAL_WIDE_FREQUENCY
    symbol_rate = INITIAL_WIDE_SYMBOL_RATE
    mode = INITIAL_WIDE_MODE
    codecs = INITIAL_WIDE_CODEC
    constellation = INITIAL_WIDE_CONSTELLATION
    fec = INITIAL_WIDE_FEC
    video_bitrate = INITIAL_WIDE_BITRATE
    spare1 = INITIAL_WIDE_SPARE1
    spare2 = INITIAL_WIDE_SPARE2
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
    video_bitrate_list = WIDE_BITRATE_LIST
    max_video_bitrate_list = len(WIDE_BITRATE_LIST) - 1
    spare1_list = WIDE_SPARE1_LIST
    max_spare1_list = len(WIDE_SPARE1_LIST) - 1
    spare2_list = WIDE_SPARE2_LIST
    max_spare2_list = len(WIDE_SPARE2_LIST) - 1
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
    video_bitrate = INITIAL_NARROW_BITRATE
    spare1 = INITIAL_NARROW_SPARE1
    spare2 = INITIAL_NARROW_SPARE2
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
    video_bitrate_list = NARROW_BITRATE_LIST
    max_video_bitrate_list = len(NARROW_BITRATE_LIST) - 1
    spare1_list = NARROW_SPARE1_LIST
    max_spare1_list = len(NARROW_SPARE1_LIST) - 1
    spare2_list = NARROW_SPARE2_LIST
    max_spare2_list = len(NARROW_SPARE2_LIST) - 1
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
    video_bitrate = INITIAL_VERY_NARROW_BITRATE
    spare1 = INITIAL_VERY_NARROW_SPARE1
    spare2 = INITIAL_VERY_NARROW_SPARE2
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
    video_bitrate_list = VERY_NARROW_BITRATE_LIST
    max_video_bitrate_list = len(VERY_NARROW_BITRATE_LIST) - 1
    spare1_list = VERY_NARROW_SPARE1_LIST
    max_spare1_list = len(VERY_NARROW_SPARE1_LIST) - 1
    spare2_list = VERY_NARROW_SPARE2_LIST
    max_spare2_list = len(VERY_NARROW_SPARE2_LIST) - 1
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
    video_bitrate = WIDE_BITRATE_LIST[WideIndex.video_bitrate]
    spare1 = WIDE_SPARE1_LIST[WideIndex.spare1]
    spare2 = WIDE_SPARE2_LIST[WideIndex.spare2]
    gain = WIDE_GAIN_LIST[WideIndex.gain]

class NarrowValue:
    band = BAND_LIST[NarrowIndex.band]
    frequency = NARROW_FREQUENCY_LIST[NarrowIndex.frequency]
    symbol_rate = NARROW_SYMBOL_RATE_LIST[NarrowIndex.symbol_rate]
    mode = NARROW_MODE_LIST[NarrowIndex.mode]
    codecs = NARROW_CODECS_LIST[NarrowIndex.codecs]
    constellation = NARROW_CONSTELLATION_LIST[NarrowIndex.constellation]
    fec = NARROW_FEC_LIST[NarrowIndex.fec]
    video_bitrate = NARROW_BITRATE_LIST[NarrowIndex.video_bitrate]
    spare1 = NARROW_SPARE1_LIST[NarrowIndex.spare1]
    spare2 = NARROW_SPARE2_LIST[NarrowIndex.spare2]
    gain = NARROW_GAIN_LIST[NarrowIndex.gain]

class VeryNarrowValue:
    band = BAND_LIST[VeryNarrowIndex.band]
    frequency = VERY_NARROW_FREQUENCY_LIST[VeryNarrowIndex.frequency]
    symbol_rate = VERY_NARROW_SYMBOL_RATE_LIST[VeryNarrowIndex.symbol_rate]
    mode = VERY_NARROW_MODE_LIST[VeryNarrowIndex.mode]
    codecs = VERY_NARROW_CODECS_LIST[VeryNarrowIndex.codecs]
    constellation = VERY_NARROW_CONSTELLATION_LIST[VeryNarrowIndex.constellation]
    fec = VERY_NARROW_FEC_LIST[VeryNarrowIndex.fec]
    video_bitrate = VERY_NARROW_BITRATE_LIST[VeryNarrowIndex.video_bitrate]
    spare1 = VERY_NARROW_SPARE1_LIST[VeryNarrowIndex.spare1]
    spare2 = VERY_NARROW_SPARE2_LIST[VeryNarrowIndex.spare2]
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
        return True
    return False

def dec_band():
    global curr_band, curr_value, curr_index
    if curr_band > 0:
        curr_band -= 1
        curr_value = value[curr_band]
        curr_index = index[curr_band]
        return True
    return False
    
def inc_frequency():
    global curr_value, curr_index
    if curr_index.frequency < curr_index.max_frequency_index:
        curr_index.frequency += 1
        curr_value.frequency = curr_index.frequency_list[curr_index.frequency]
        return True
    return False

def dec_frequency():
    global curr_value, curr_index
    if curr_index.frequency > 0:
        curr_index.frequency -= 1
        curr_value.frequency = curr_index.frequency_list[curr_index.frequency]
        return True
    return False
    
def inc_symbol_rate():
    global curr_value, curr_index
    if curr_index.symbol_rate < curr_index.max_symbol_rate_list:
        curr_index.symbol_rate += 1
        curr_value.symbol_rate = curr_index.symbol_rate_list[curr_index.symbol_rate]
        return True
    return False

def dec_symbol_rate():
    global curr_value, curr_index
    if curr_index.symbol_rate > 0:
        curr_index.symbol_rate -= 1
        curr_value.symbol_rate = curr_index.symbol_rate_list[curr_index.symbol_rate]
        return True
    return False
    
def inc_mode():
    global curr_value, curr_index
    if curr_index.mode < curr_index.max_mode_list:
        curr_index.mode += 1
        curr_value.mode = curr_index.mode_list[curr_index.mode]
        return True
    return False

def dec_mode():
    global curr_value, curr_index
    if curr_index.mode > 0:
        curr_index.mode -= 1
        curr_value.mode = curr_index.mode_list[curr_index.mode]
        return True
    return False

def inc_codecs():
    global curr_value, curr_index
    if curr_index.codecs < curr_index.max_codecs_list:
        curr_index.codecs += 1
        curr_value.codecs = curr_index.codecs_list[curr_index.codecs]
        return True
    return False

def dec_codecs():
    global curr_value, curr_index
    if curr_index.codecs > 0:
        curr_index.codecs -= 1
        curr_value.codecs = curr_index.codecs_list[curr_index.codecs]
        return True
    return False
    
def inc_constellation():
    global curr_value, curr_index
    if curr_index.constellation < curr_index.max_constellation_list:
        curr_index.constellation += 1
        curr_value.constellation = curr_index.constellation_list[curr_index.constellation]
        return True
    return False

def dec_constellation():
    global curr_value, curr_index
    if curr_index.constellation > 0:
        curr_index.constellation -= 1
        curr_value.constellation = curr_index.constellation_list[curr_index.constellation]
        return True
    return False
    
def inc_fec():
    global curr_value, curr_index
    if curr_index.fec < curr_index.max_fec_list:
        curr_index.fec += 1
        curr_value.fec = curr_index.fec_list[curr_index.fec]
        return True
    return False

def dec_fec():
    global curr_value, curr_index
    if curr_index.fec > 0:
        curr_index.fec -= 1
        curr_value.fec = curr_index.fec_list[curr_index.fec]
        return True
    return False
    
def inc_video_bitrate():
    global curr_value, curr_index
    if curr_index.video_bitrate < curr_index.max_video_bitrate_list:
        curr_index.video_bitrate += 1
        curr_value.video_bitrate = curr_index.video_bitrate_list[curr_index.video_bitrate]
        return True
    return False

def dec_video_bitrate():
    global curr_value, curr_index
    if curr_index.video_bitrate > 0:
        curr_index.video_bitrate -= 1
        curr_value.video_bitrate = curr_index.video_bitrate_list[curr_index.video_bitrate]
        return True
    return False
    
def inc_spare1():
    global curr_value, curr_index
    if curr_index.spare1 < curr_index.max_spare1_list:
        curr_index.spare1 += 1
        curr_value.spare1 = curr_index.spare1_list[curr_index.spare1]
        return True
    return False

def dec_spare1():
    global curr_value, curr_index
    if curr_index.spare1 > 0:
        curr_index.spare1 -= 1
        curr_value.spare1 = curr_index.spare1_list[curr_index.spare1]
        return True
    return False
   
def inc_spare2():
    global curr_value, curr_index
    if curr_index.spare2 < curr_index.max_spare2_list:
        curr_index.spare2 += 1
        curr_value.spare2 = curr_index.spare2_list[curr_index.spare2]
        return True
    return False

def dec_spare2():
    global curr_value, curr_index
    if curr_index.spare2 > 0:
        curr_index.spare2 -= 1
        curr_value.spare2 = curr_index.spare2_list[curr_index.spare2]
        return True
    return False
    
def inc_gain():
    global curr_value, curr_index
    if curr_index.gain < curr_index.max_gain_list:
        curr_index.gain += 1
        curr_value.gain = curr_index.gain_list[curr_index.gain]
        return True
    return False

def dec_gain():
    global curr_value, curr_index
    if curr_index.gain > 0:
        curr_index.gain -= 1
        curr_value.gain = curr_index.gain_list[curr_index.gain]
        return True
    return False

def selected_frequency_marker():
    i = int(curr_value.frequency[9:])
    return TUNED_MARKER[i]

class EncoderArgs:
    audio_codec = None         # 'ACC'
    audio_bitrate = None       # '64000'
    video_codec = None         # 'H.265'
    video_size = None          # '1280x720'
    video_bitrate = None       # '330'
    url = None                 # 'udp://192.168.3.10:8282'

def encoder_args():
    global curr_value
    tup = curr_value.codecs.partition(" ")
    audio_codec = tup[2]
    if tup[0] == 'H264':
        video_codec = 'H.264'
        url = f'rtmp://{PLUTO_ADDRESS}:7272'
    else:
        video_codec = 'H.265'
        url = f'udp://{PLUTO_ADDRESS}:8282'
    args = EncoderArgs()
    args.audio_codec = audio_codec
    args.audio_bitrate = '64000'            # NOTE: not implemented
    args.video_codec = video_codec
    args.video_size = '1280x720'            # NOTE: not implemented
    args.video_bitrate = curr_value.video_bitrate
    args.url = url
    return args

class PlutoArgs:
    frequency = None                # '2409.75'
    mode = None                     # 'DBS2'
    constellation = None            # 'QPSK'
    symbol_rate = None              # '333'
    fec = None                      # '23'
    gain = None                     # '-10'
    calibration_mode = None         # 'nocalib'
    pcr_pts = None                  # '800'
    pat_period = None               # '200'
    roll_off = None                 # '0.25'
    pilots = None                   # 'off'
    frame = None                    # 'LongFrame'
    audio_bit_rate = None           # '32'
    provider = None                 # 'EA7KIR'
    service = None                  # 'Michael'
    url = None                      # 'udp://192.168.3.10:8282'

def pluto_args():
    global curr_value
    tup = curr_value.fec.partition("/")
    fec = tup[0] + tup[2]
    tup = curr_value.codecs.partition(" ")
    if tup[0] == 'H264':
        url = f'rtmp://{PLUTO_ADDRESS}:7272'
    else:
        url = f'udp://{PLUTO_ADDRESS}:8282'
    tup = curr_value.mode.partition("-")
    mode = tup[0] + tup[2]
    args = PlutoArgs()
    args.frequency = curr_value.frequency[:7]
    args.mode = mode
    args.constellation = curr_value.constellation
    args.symbol_rate = curr_value.symbol_rate
    args.fec = fec
    args.gain = curr_value.gain
    args.calibration_mode = 'nocalib'   # NOTE: not implemented
    args.pcr_pts = '800'                # NOTE: not implemented
    args.pat_period = '200'             # NOTE: not implemented
    args.roll_off = '0.25'              # NOTE: not implemented
    args.frame = 'LongFrame'            # NOTE: not implemented
    args.audio_bit_rate = '32'          # NOTE: not implemented
    args.provider = PROVIDER_NAME
    args.service = SERVICE_NAME
    args.url = url
    return args 

    """
    # Eg: "rtmp://192.168.1.40:7272/,2409.75,DVBS2,QPSK,333,23,-2,nocalib,800,32,/,EA7KIR,"

    s =  f'rtmp://{IP},{PORT},{frequency},{mode},{constellation},{symbol_rate},{fec},{gain},nocalib,800,32,/,{spare1},'

    IP = '192.168.2.1'
    PORT = '7277' or '8282'
    frequency = '2409.75'
    mode = 'DVBS2'
    constellation = 'QPSK'
    fec = '23'
    gain = '-2'
    provider = 'EA7KIR'
    """

NORMAL_BUTTON_COLOR = ('#FFFFFF','#222222')
DISABALED_BUTTON_COLOR = ('#444444',None)
TUNE_ACTIVE_BUTTON_COLOR = ('#FFFFFF','#007700')
PTT_ACTIVE_BUTTON_COLOR = ('#FFFFFF','#FF0000')
   
tune_is_active = False
ptt_is_active = False
tune_button_color = NORMAL_BUTTON_COLOR
ptt_button_color = NORMAL_BUTTON_COLOR

def tune():
    global tune_is_active, tune_button_color
    if ptt_is_active:
        return
    tune_is_active = not tune_is_active
    if tune_is_active:
        tune_button_color = TUNE_ACTIVE_BUTTON_COLOR
        enc_args = encoder_args()
        activate_encoder(enc_args)
        plu_args = pluto_args()
        activate_pluto(plu_args)
    else:
        tune_button_color = NORMAL_BUTTON_COLOR
        deactivate_pluto()
        deactivate_encoder()

def ptt():
    global ptt_is_active, ptt_button_color
    if not tune_is_active:
        return
    ptt_is_active = not ptt_is_active
    if ptt_is_active:
        ptt_button_color = PTT_ACTIVE_BUTTON_COLOR
        activate_ptt()
    else:
        ptt_button_color = NORMAL_BUTTON_COLOR
        deactivate_ptt()

def cancel_tune():
    global ptt_is_active, ptt_button_color, tune_is_active, tune_button_color
    if not tune_is_active:
        return False
    if ptt_is_active:
        ptt_is_active = False
        ptt_button_color = NORMAL_BUTTON_COLOR
        deactivate_ptt()
    tune_is_active = False
    tune_button_color = NORMAL_BUTTON_COLOR
    deactivate_pluto()
    deactivate_encoder()
    return True
   
    