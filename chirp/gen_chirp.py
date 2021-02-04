import numpy as np
import pyabf
import scipy.signal
import matplotlib.pyplot as plt


def build_chirp(x, start=0, end=20):
    y = scipy.signal.chirp(x, f0=start, t1=x[-1], f1=end)
    return y



def main():
    #Parameters
    dt = 1/20000 #in seconds
    strt_freq = 0.0
    end_freq = 50
    sweep_length = 50
    sweeps = 3
    scale_factor = 10
    # Build the X array
    x = np.arange(0, sweep_length+dt, step=dt)
    #get the chirp
    y = build_chirp(x, start=strt_freq, end=end_freq)
    #add the sweeps
    y = np.tile(y, (sweeps, 1)) * scale_factor
    #output the chirp
    pyabf.abfWriter.writeABF1(y, f"chirp_{int(strt_freq)}_{int(end_freq)}_in_{int(sweep_length)}.abf", 1/dt)
    #plot the chirp
    plt.plot(x, y[0, :])
    plt.figure()
    plt.specgram(y[0, :], Fs=int(1/dt), NFFT=int(1/dt))
    plt.ylim(0, end_freq+10)
    plt.show()


main()