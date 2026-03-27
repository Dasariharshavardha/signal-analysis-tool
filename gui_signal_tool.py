import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sg
import tkinter as tk

def generate_signal():
    freq = float(entry.get())

    t = np.linspace(0, 1, 500)
    sine = np.sin(2 * np.pi * freq * t)

    noise = np.random.normal(0, 0.3, len(t))
    noisy_signal = sine + noise

    filtered = sg.savgol_filter(noisy_signal, 21, 3)

    plt.figure()

    plt.subplot(3,1,1)
    plt.plot(t, sine)
    plt.title("Original Signal")

    plt.subplot(3,1,2)
    plt.plot(t, noisy_signal)
    plt.title("Noisy Signal")

    plt.subplot(3,1,3)
    plt.plot(t, filtered)
    plt.title("Filtered Signal")

    plt.tight_layout()
    plt.show()

    fft = np.fft.fft(sine)
    freqs = np.fft.fftfreq(len(t), t[1] - t[0])

    plt.figure()
    plt.plot(freqs, np.abs(fft))
    plt.title("Frequency Spectrum")
    plt.show()


# GUI
root = tk.Tk()
root.title("Signal Generator")

tk.Label(root, text="Enter Frequency:").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Generate Signal", command=generate_signal).pack()

root.mainloop()