# Motion-Effects-Work-Study
All code created and used for the 2024-2025 work study at ToNI on motion effects. The aim of the study is to minimize motion and resulting artifacts from motion during MRI scans.

Overview
========

The code in this repository implements the following pipeline to estimate motion effects, represented by framewise displacement (FD), for a study with data in DICOM format. These are the steps in the pipeline

| Step | Used Script / Code                                       | Purpose                                                                                                                        |
|------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| 1.   | `patientdataextract.py`                                  | *Optional/Testing*: Retrieves demographic and system information from DICOM files of a single participant                      |
| 2.   | ` find . -wholename "*t1_mprage*/*.dcm" >> t1names.txt`  | Creates Text file with T1 dicom paths of all participants to parse in next step                                                |
| 3.   | `masspatientdataextract.py`                              | Takes all the subject paths (from a `.txt` file) and creates table of all participants' demographic data                       |
| 4.   | `bidsmapper /home/data /home/data/bidscoin_bids --subprefix 'PRE' --sesprefix 'First_Second' ` | Use in BIDSCoin terminal to create bidsmap (a `.yaml` file) for dicoms with provided subprefix and sesprefix in data directory   |
| 5.   | `bidscoiner /home/data /home/data/bidscoin_bids`         | Use in BIDSCoin terminal. Uses bidsmap from previous step to convert mapped dicoms to nifti according to the BIDSCoin format   |
| 6.   | `find . -name *.nii.gz -exec gunzip {} \; `              | Unzips all compressed nifi files of current directory when called in terminal in preparation for SPM realignment               |
| 7.   | `matlabbatch_realign_single_subject_all_runs_emptydir.m` | Runs SPM realignment for 7 sessions, each aligned to the first volume, for the inputted subject file                           |
| 8.   | `matlabbatch_runmultiplesub.m`                           | Automates SPM realignment above for multiple subjects, as inputted                                                             |
| 9.   | `fdcalculator.py`                                        | Cycles through all subject files in provided directory to calculate Mean and Max FD for each run. Creates table with this data |
