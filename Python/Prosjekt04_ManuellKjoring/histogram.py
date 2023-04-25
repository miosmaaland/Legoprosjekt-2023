import matplotlib.pyplot as plt
import statistics

# Open the file for reading
with open('Data\Offline_P04_ManuellKjøring_Lisan.txt', 'r') as f:
    # Skip the first line (header)
    next(f)
    # Read the remaining contents of the file into a string
    data = f.read()

# Split the data into a list of lines
lines = data.split('\n')

# Extract the values of Lys into a list
Lys_L = []
for line in lines:
    # Skip any empty lines
    if line:
        # Split each line into a list of values
        values = line.split(',')
        # Check that the list of values has at least 9 elements (including Lys)
        if len(values) >= 9:
            # Extract the value of Lys from the list
            Lys = float(values[8])
            # Append the value of Lys to the list of Lys values
            Lys_L.append(Lys)

# Open the file for reading
with open('Data\Offline_P04_ManuellKjøring_Mio.txt', 'r') as f:
    # Skip the first line (header)
    next(f)
    # Read the remaining contents of the file into a string
    data = f.read()

# Split the data into a list of lines
lines = data.split('\n')

# Extract the values of Lys into a list
Lys_M = []
for line in lines:
    # Skip any empty lines
    if line:
        # Split each line into a list of values
        values = line.split(',')
        # Check that the list of values has at least 9 elements (including Lys)
        if len(values) >= 9:
            # Extract the value of Lys from the list
            Lys = float(values[8])
            # Append the value of Lys to the list of Lys values
            Lys_M.append(Lys)

with open('Data\Offline_P04_ManuellKjøring_Rich.txt', 'r') as f:
    # Skip the first line (header)
    next(f)
    # Read the remaining contents of the file into a string
    data = f.read()

# Split the data into a list of lines
lines = data.split('\n')

# Extract the values of Lys into a list
Lys_R = []
for line in lines:
    # Skip any empty lines
    if line:
        # Split each line into a list of values
        values = line.split(',')
        # Check that the list of values has at least 9 elements (including Lys)
        if len(values) >= 9:
            # Extract the value of Lys from the list
            Lys = float(values[8])
            # Append the value of Lys to the list of Lys values
            Lys_R.append(Lys)


# Create a histogram of the Lys values
import matplotlib.pyplot as plt

# Plot the histograms
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Lys_L histogram
axs[0, 0].hist(Lys_L, bins=50, color='blue', alpha=0.7)
axs[0, 0].set_title(f'Lisan, Mean={statistics.median(Lys_L)}, std={statistics.stdev(Lys_L): .2f}')
axs[0, 0].set_xlabel('Lysverdier')
axs[0, 0].set_ylabel('Antall målinger')

# Lys_M histogram
axs[0, 1].hist(Lys_M, bins=50, color='red', alpha=0.7)
axs[0, 1].set_title(f'Mio, Mean={statistics.median(Lys_M)}, std={statistics.stdev(Lys_M): .2f}')
axs[0, 1].set_xlabel('Lysverdier')
axs[0, 1].set_ylabel('Antall målinger')

# Lys_R histogram
axs[1, 0].hist(Lys_R, bins=50, color='green', alpha=0.7)
axs[1, 0].set_title(f'Rich, Mean={statistics.median(Lys_R)}, std={statistics.stdev(Lys_R): .2f}')
axs[1, 0].set_xlabel('Lysverdier')
axs[1, 0].set_ylabel('Antall målinger')

# Remove the unused subplot
axs[1, 1].axis('off')

plt.tight_layout()
plt.show()

