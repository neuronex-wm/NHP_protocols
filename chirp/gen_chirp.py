import numpy as np
import pyabf
import scipy.signal
import matplotlib.pyplot as plt


def build_chirp(x, start=0, end=20):
    y = scipy.signal.chirp(x, f0=start, t1=x[-1], f1=end)
    return y

def build_testpulse(dt, length=10, mag=-25, totlength=500):
    x1 = np.arange(0, 1.540, dt)
    y1 = np.full(x1.shape[0], 0)
    x2 = np.arange(0, length/1000, dt)
    y2 = np.full(x2.shape[0], mag)
    x3 = np.arange(0, 450/1000, dt)
    y3 = np.full(x3.shape[0], 0)
    return np.hstack((x1,x2,x3)), np.hstack((y1,y2,y3))


def main():
    #Parameters
    dt = 1/20000 #in seconds
    strt_freq = 0.0
    end_freq = 20
    sweep_length = 40
    sweeps = 3
    scale_factor = 50
    # Build the X array
    x = np.arange(0, sweep_length+dt, step=dt)
    #get the chirp
    y = build_chirp(x, start=strt_freq, end=end_freq)  * scale_factor
    #get the testpulse
    xtp, tp = build_testpulse(dt)
    y = np.hstack((tp, y))
    x = np.linspace(0, x[-1]+xtp[-1], len(xtp)+len(x))
    #add the sweeps
    y = np.tile(y, (sweeps, 1))
    #output the chirp
    pyabf.abfWriter.writeABF1(y, f"chirp_{int(strt_freq)}_{int(end_freq)}_in_{int(sweep_length)}.abf", 1/dt)
    #plot the chirp
    plt.plot(x, y[0, :])
    plt.figure()
    plt.specgram(y[0, :], Fs=int(1/dt), NFFT=int(1/dt))
    plt.ylim(0, end_freq+10)
    plt.show()


main()