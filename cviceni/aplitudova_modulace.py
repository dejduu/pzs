import numpy as np
import matplotlib.pyplot as plt

def generate_am_signal(carrier_freq=100, modulating_freq=5, modulation_index=0.5, duration=1.0, sampling_rate=10000):
    # Časová osa
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    
    # Nosná vlna (carrier signal)
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    
    # Modulační signál (message signal)
    message = np.sin(2 * np.pi * modulating_freq * t)
    
    # Amplitudově modulovaný signál
    am_signal = (1 + modulation_index * message) * carrier
    
    return t, am_signal, carrier, message

# Parametry signálu
carrier_freq = 100  # Frekvence nosné vlny
modulating_freq = 5  # Frekvence modulačního signálu
modulation_index = 0.5  # Index modulace (0.5 znamená 50% modulace)
duration = 2.0  # Doba trvání signálu v sekundách

# Generování signálu
t, am_signal, carrier, message = generate_am_signal(carrier_freq, modulating_freq, modulation_index, duration)

# Vykreslení signálů
plt.figure(figsize=(10, 8))

# Modulační signál
plt.subplot(3, 1, 1)
plt.plot(t, message)
plt.title('Modulační signál (Message Signal)')
plt.xlabel('Čas [s]')
plt.ylabel('Amplituda')

# Nosná vlna
plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.title('Nosná vlna (Carrier Signal)')
plt.xlabel('Čas [s]')
plt.ylabel('Amplituda')
plt.grid(True)

# Amplitudově modulovaný signál
plt.subplot(3, 1, 3)
plt.plot(t, am_signal)
plt.title('Amplitudově modulovaný signál (AM Signal)')
plt.xlabel('Čas [s]')
plt.ylabel('Amplituda')
plt.grid(True)

# Nastavení rozložení a uložení grafu
plt.tight_layout()
plt.show()
plt.savefig('am_signal.png')  # Uložení grafu jako obrázek
print("Graf byl uložen jako 'am_signal.png'.")
