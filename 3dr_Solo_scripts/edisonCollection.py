from rtlsdr import *
from pylab import *
import sys
import time
import json


spectrum = {}

sdr = RtlSdr()

sdr.sample_rate = 2.4e6
sdr.center_freq = sys.argv[1]
sdr.gain = 40
while True:
    samples = sdr.read_samples(256*4096)
    print(samples)

    spectrum[time.time()] = str(samples)

    psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
    xlabel('Frequency (MHz)')
    ylabel('Relative power (dB)')

    show()
    time.sleep(10)
with open('spectrumData', 'w') as f:
    json.dump(spectrum, f)
