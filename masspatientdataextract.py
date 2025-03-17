from sys import dont_write_bytecode
from unicodedata import name

import pydicom

# Get txt file with list of paths (each on newline)
# In folder with dicoms, call within bash: find . -wholename "*t1_mprage*/*.dcm" >> t1names.txt

# Open paths txt file
path_list = "/home/jovyan/data/JMR1/t1names.txt"
pathf = open(path_list, "r")

# Create MetaData txt file or clear an existing one (places in same directory as dicoms)
file_name = "/home/jovyan/data/JMR1/PatientMetaInfo.txt"
f = open(file_name, "w")
# WARNING!!!
# In the case that a txt file exists with this name, its contents will be erased and replaced with the new data
f.close()
f = open(file_name, "a")  #then reopen to begin appending data
f.write("Patient Id\tOperator\tAge\tSex\tHeight\tWeight\tStudy Date\tStart Time\n")  # Label the columns

for line in pathf:
    print(line)
    # Include path to dcm file below, with added starter as path is checked starting from home folder
    # The starter below directs to the external drive data folder
    dicom_file = "/home/jovyan/data/JMR1" + line[1:-1]
    
    # Load the DICOM file
    ds = pydicom.dcmread(dicom_file)
    
    # Extract basic metadata and check
    pName = f"{ds.PatientName}\t"
    sex = f"{ds.PatientSex}\t"
    age = f"{ds.PatientAge}\t"
    studyDate = f"{ds.StudyDate}\t"
    studyTime = f"{ds.StudyTime}\t"
    weight = f"{ds.PatientWeight}\t"
    height = f"{ds.PatientSize}\t"

    # Sometimes Operator is not available, so catch that and return a blank
    try:
        operator = f"{ds.OperatorsName}\t"
    except (AttributeError):
        operator = "--\t"
    
    
    # Add meta data to txt file in rows
    f.write(pName)
    f.write(operator)
    f.write(age)
    f.write(sex)
    f.write(height)
    f.write(weight)
    f.write(studyDate)
    f.write(studyTime)
    f.write("\n")


f.close() # close meta data file

pathf.close()  # close paths file
