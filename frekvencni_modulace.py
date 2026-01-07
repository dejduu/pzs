import numpy as np
import matplotlib.pyplot as plt

def generate_fm_signal(carrier_freq=10, modulating_freq=5, modulation_index=5.0, duration=1.0, sampling_rate=1000):
    # Time axis
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    
    # Carrier signal
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    
    # Modulating signal (message signal)
    message = np.sin(2 * np.pi * modulating_freq * t)
    
    # Frequency modulated signal
    fm_signal = np.cos(2 * np.pi * carrier_freq * t + modulation_index * np.sin(2 * np.pi * modulating_freq * t))
    
    return t, fm_signal, carrier, message

# Signal parameters
carrier_freq = 5  # Carrier frequency
modulating_freq = 1  # Modulating frequency
modulation_index = 5.0  # Modulation index
duration = 4.0  # Duration of the signal in seconds

# Generate the FM signal
t, fm_signal, carrier, message = generate_fm_signal(carrier_freq, modulating_freq, modulation_index, duration)

# Plot the signals
plt.figure(figsize=(10, 8))

# Modulating signal
plt.subplot(3, 1, 1)
plt.plot(t, message)
plt.title('Modulating Signal (Message Signal)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Carrier signal
plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.title('Carrier Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Frequency modulated signal
plt.subplot(3, 1, 3)
plt.plot(t, fm_signal)
plt.title('Frequency Modulated Signal (FM Signal)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Adjust layout and save the plot
plt.tight_layout()
plt.show()
plt.savefig('fm_signal.png')  # Save the plot as an image
print("The plot has been saved as 'fm_signal.png'.")
