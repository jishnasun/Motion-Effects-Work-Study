# Motion-Effects-Work-Study
All code created and used for the 2024-2025 work study at ToNI on motion effects. The aim of the study is to minimize motion and resulting artifacts from motion during MRI scans.

Overview
========

The code in this repository implements the following pipeline to estimate motion effects, represented by framewise displacement (FD), for a study with data in DICOM format. These are the steps in the pipeline

| Step | Used Script / Code                                      | Purpose                                                                                                    |
|------|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| 1.   | `patientdataextract.py`                                 | *Optional/Testing*: Retrieves demographic and system information from DICOM files of a single participant  |
| 2.   | ` find . -wholename "*t1_mprage*/*.dcm" >> t1names.txt` | Creates Text file with T1 dicom paths of all particiapnts to parse in next step                            |
| 3.   | `masspatientdataextract.py`                             | Takes all the subject paths (from a `.txt` file) and creates table of all participants' demographic data   |
