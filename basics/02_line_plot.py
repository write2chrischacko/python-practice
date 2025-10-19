import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y, linestyle='-')       # OG sine wave
plt.plot(x, y*0.5, linestyle='--')  # Shifter sine wave
plt.plot(x, z, linestyle='-.')      # Cos wave

plt.legend(["Sine", "Sine (dashed)", "Cosine (dash-dot)"], loc="upper right")

plt.title("Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()
