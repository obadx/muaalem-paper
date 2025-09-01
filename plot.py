import numpy as np
import matplotlib.pyplot as plt

# Data from the table (converted to JSON format)
data = {
    "phonemes": {"EXP1": 0.0069, "EXP2": 0.0069, "EXP3": 0.0063},
    "tikraar": {"EXP1": 0.006, "EXP2": 0.006, "EXP3": 0.0017},
    "tafkheem_or_tarqeeq": {"EXP1": 0.002599, "EXP2": 0.00279, "EXP3": 0.0065},
    "tafashie": {"EXP1": 0.001837, "EXP2": 0.0025, "EXP3": 0.0035},
    "Qalqala": {"EXP1": 0.001808, "EXP2": 0.008, "EXP3": 0.00174},
    "Safeer": {"EXP1": 0.00346, "EXP2": 0.00246, "EXP3": 0.00174},
    "Shidda_or_rakhawa": {"EXP1": 0.015276, "EXP2": 0.0053, "EXP3": 0.0031},
    "Istitala": {"EXP1": 0.00243, "EXP2": 0.00166, "EXP3": 0.001525},
    "Itbaaq": {"EXP1": 0.00176, "EXP2": 0.00217, "EXP3": 0.00168},
    "Ghonna": {"EXP1": 0.044, "EXP2": 0.02675, "EXP3": 0.00199},
    "hams_or_jahr": {"EXP1": 0.0024, "EXP2": 0.00256, "EXP3": 0.00234},
    "average_per": {"EXP1": 0.0080455, "EXP2": 0.006, "EXP3": 0.00293},
}

# Extract EXP data (excluding average_per)
attributes = [key for key in data.keys() if key != "average_per"]
exp_columns = ["EXP1", "EXP2", "EXP3"]

# Prepare data for standard deviation calculation
exp_data = {exp: [] for exp in exp_columns}
for attr in attributes:
    for exp in exp_columns:
        exp_data[exp].append(data[attr][exp])

# Calculate standard deviation for each EXP
std_values = [np.std(exp_data[exp]) for exp in exp_columns]

# Extract average values
average_values = [data["average_per"][exp] for exp in exp_columns]

# Create the plot with a larger figure size
plt.rcParams.update({"font.size": 12, "font.weight": "bold"})
fig, ax1 = plt.subplots(figsize=(12, 8))

# Bar plot for standard deviation
bars = ax1.bar(
    exp_columns, std_values, alpha=0.7, color="skyblue", label="Standard Deviation"
)
ax1.set_xlabel("EXP Columns", fontsize=14, fontweight="bold")
ax1.set_ylabel("Standard Deviation", color="skyblue", fontsize=14, fontweight="bold")
ax1.tick_params(axis="y", labelcolor="skyblue")

# Add values on top of bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width() / 2.0,
        height + 0.0001,
        f"{std_values[i]:.6f}",
        ha="center",
        va="bottom",
        fontweight="bold",
    )

# Create a second y-axis for average values
ax2 = ax1.twinx()
line = ax2.plot(
    exp_columns,
    average_values,
    color="red",
    marker="o",
    linewidth=3,
    markersize=8,
    label="Average",
)
ax2.set_ylabel("Average", color="red", fontsize=14, fontweight="bold")
ax2.tick_params(axis="y", labelcolor="red")

# Add values to the line plot
for i, exp in enumerate(exp_columns):
    ax2.text(
        i,
        average_values[i] + 0.0001,
        f"{average_values[i]:.6f}",
        ha="center",
        va="bottom",
        color="red",
        fontweight="bold",
    )

# Add title with increased font size and weight
plt.title(
    "Standard Deviation and Average Values for EXP Columns",
    fontsize=16,
    fontweight="bold",
    pad=20,
)

# Add grid for better readability
ax1.grid(True, alpha=0.3)
fig.tight_layout()

# Combine legends from both axes with bold text
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
legend = ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right")
for text in legend.get_texts():
    text.set_fontweight("bold")

plt.show()
plt.savefig("results_stats_v2.png")
