# Wave Plotting in Python

This set of programs demonstrates the step-by-step evolution of plotting sine and cosine waves using matplotlib and numpy.
Each part builds on the previous one, gradually adding new features.

### Part 1: Basic Sine Wave Plot

np.linspace(0, 10, 100) – generates 100 evenly spaced points from 0 to 10.
np.sin(x) – calculates sine values for each point.
plt.plot(x, y) – plots sine wave (y) against time (x).
plt.title() – adds a title.
plt.show() – displays the graph.

Output: a simple sine wave.

### Part 2: Adding Grid Lines and Legend

Legend: plt.legend() labels each plotted line.
Axes labels: xlabel and ylabel name the axes.
Grid: plt.grid() makes reading values easier.

Output: two sine waves, one original and one scaled, are compared.

### Part 3: Adding Cosine Wave

A cosine wave is created using np.cos(x).
Added to the same graph with a dash-dot line style.

Output: three wave - sine, shifted sine, and cos, are plotted.

### Part 4: Efficient Loop Plotting, Filling, and Saving

Loop Plotting:
Uses zip() to iterate through multiple lists (wvs, lbls, stls) together — reducing repetitive code.

Shaded Area:
plt.fill_between(x, wave, alpha=0.1) lightly fills the area under each curve (adds visual emphasis).
alpha = transparency level (0 → fully transparent, 1 → solid).

Saving the Plot:

    plt.savefig("sine_cos_plot.png") stores the final figure as an image file.

To save the image in a specific folder, use:

    plt.savefig("/Users/xyz/Desktop/plots/sine_cos_plot.png")

### Final output: 

Three waves (Sine, Scaled Sine, Cosine)

Shaded area under each curve

Grid lines, labels, legend, and title

Saved image: sine_cos_plot.png
