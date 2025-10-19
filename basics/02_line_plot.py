import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, linestyle='-')       # OG sine wave
plt.plot(x, y*0.5, linestyle='--')  # Shifter sine wave
plt.legend(["Sine", "Sine (dashed)"], loc="upper right")

plt.title("Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()
