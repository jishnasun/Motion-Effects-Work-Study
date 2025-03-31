from sys import dont_write_bytecode
from unicodedata import name

import os
import glob
import numpy as np


# Create FD txt file or clear an existing one (places in same directory as subject files)
file_name = "/home/jovyan/data/derivatives/FDvalues.txt"
f = open(file_name, "w")
# WARNING!!!
# In the case that a txt file exists with this name, its contents will be erased and replaced with the new data
f.close()
f = open(file_name, "a")  #then reopen to begin appending data
#f.write("Patient Id\tMean FD 1\tMax FD 1\tMean FD 2\tMax FD 2\tMean FD 3\tMax FD 3\tMean FD 4\tMax FD 4\tMean FD 5\tMax FD 5\tMean FD 6\tMax FD 6\tMean FD 7\tMax FD 7\n")  # Label the columns

# Using standard head radius
radius = 50

# Define directory with subject files
parent_dir = "/home/jovyan/data/derivatives/ya"  # Change last directory for each section

# Loop through each subdirectory in the parent directory
for subdir in sorted(os.listdir(parent_dir)):  # Sort for consistency
    subdir_path = os.path.join(parent_dir, subdir)
    
    # Check if it's a directory
    if os.path.isdir(subdir_path):
        subject_name = os.path.basename(subdir_path)
        print(f"\nProcessing directory: {subject_name}")
        f.write(f"{subject_name}\t")

        # Find all realignment txt files starting with "rp" in this subject file
        txt_files = glob.glob(os.path.join(subdir_path, "func", "rp*.txt"))

        if not txt_files:
            print("No files found.")
            f.write("\n")
        
        # Loop through each run's realignment parameters in the subject file
        for file_path in txt_files:
           
            # Load motion parameters (Assumes 6 columns: x, y, z, pitch, roll, yaw)
            motion_params = np.loadtxt(file_path)

            # Compute framewise displacement
            diffs = np.abs(np.diff(motion_params, axis=0))  # Frame-to-frame difference
            diffs[:, 3:6] *= radius  # Convert rotations from radians to mm
            fd = np.sum(diffs, axis=1)  # Sum absolute values per frame

            # Compute mean and max FD
            mean_fd = np.mean(fd)
            max_fd = np.max(fd)

            # Annotate FD results for the run
            f.write(f"{mean_fd:.3f}\t{max_fd:.3f}\t")
            
        f.write("\n")


f.close() # close FD data file
