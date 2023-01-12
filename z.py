class Value():
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
        self.band = name
def func():
        wide.mode = 'QPSK'

wide = Value('Wide')
wide.symbol_rate = '333'
func()

print(wide.band, wide.symbol_rate, wide.mode)