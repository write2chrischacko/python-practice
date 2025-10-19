import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)       # Original sine wave
y_shift = y * 0.5   # Shifted sine wave
z = np.cos(x)       # Cosine wave

# Store waves, labels, and line styles in *lists* for loop plotting
wvs = [y, y_shift, z]
lbls = ["Sine", "Sine (dashed)", "Cosine (dash-dot)"]
stls = ['-', '--', '-.']

# Plot all waves using a loop (Programming Efficiency)
# Creates *tuples* of lists created earlier
for wave, label, style in zip(wvs, lbls, stls):
    plt.plot(x, wave, linestyle=style, label=label)
    
    # Fill under each curve (Area Plot)
    plt.fill_between(x, wave, alpha=0.1)  # light shaded area under curve


plt.legend(loc="upper right")
plt.title("Sine & Cosine Waves")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.savefig("sine_cos_plot.png")  # saves the current figure as a PNG file

plt.show()
