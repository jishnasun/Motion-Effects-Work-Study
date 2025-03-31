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

#Output will have the following form per row:
# Patient Id, Mean FD 1, Max FD 1, Mean FD 2, Max FD 2, Mean FD 3, Max FD 3, Mean FD 4, Max FD 4, Mean FD 5, Max FD 5, Mean FD 6, Max FD 6, Mean FD 7, Max FD 7
# If the subject has less than 7 runs it will simply leave the extra columns blank

# Using standard head radius
radius = 50

# Define directory with subject files
parent_dir = "/home/jovyan/data/derivatives"  # Parent directory; should containt NIFTI subject files in standard BIDSCOIN format

# Loop through each subject file in the parent directory
for subdir in sorted(os.listdir(parent_dir)):  # Sort for consistency
    subdir_path = os.path.join(parent_dir, subdir)
    
    # Check if it's a directory
    if os.path.isdir(subdir_path):
        subject_name = os.path.basename(subdir_path)
        print(f"\nProcessing directory: {subject_name}")
        f.write(f"{subject_name}\t")

        # Find all realignment txt files starting with "rp" in this subject file -- searches in 'func' directory within subject file
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

            # Annotate FD results for the run (only includes three decimal places)
            f.write(f"{mean_fd:.3f}\t{max_fd:.3f}\t")
            
        f.write("\n") # new row, new subject


f.close() # close FD data file
