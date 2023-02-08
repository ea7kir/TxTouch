from device_constants import ENCODER_ADDRESS

# TODO: network access to HEV-10

def configure_encoder():
    pass

def shutdown_encoder():
    pass

#class EncoderArgs:
#    audio_codec = None         # 'ACC'
#    audio_bitrate = None       # '64000'
#    video_codec = None         # 'H.265'
#    video_size = None          # '1280x720'
#    video_bitrate = None       # '330'
#    url = None                 # 'udp://192.168.3.10:8282' OR 'rtmp://192.168.3.10:7272 BUT this could require changing the encoder stream to pimary?

def setup_encoder(enc):
    print(f'ENCODER codec: {enc.codecs}, video_bitrate: {enc.video_bitrate}')
    pass

