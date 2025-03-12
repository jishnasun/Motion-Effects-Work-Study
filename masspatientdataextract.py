from sys import dont_write_bytecode
from unicodedata import name
import pydicom

# Get txt file with list of paths (each on newline)
# In dicom folder, call within bash: find . -wholename "*t1_mprage*/*.dcm" >> t1names.txt

# Open paths txt file
path_list = "t1names.txt"
pathf = open(path_list, "r")

# Create MetaData txt file or clear an existing one
file_name = "PatientMetaInfo.txt"
f = open(file_name, "w")
# WARNING!!!
# In the case that a txt file exists with this name, its contents will be erased and replaced with the new data
f.close()
f = open(file_name, "a")  #then reopen to begin appending data

# Loop through each line of txt file and extract metadata from path

#    pName = f"Patient Name: {ds.PatientName}\n"
#     # modality = f"Modality: {ds.Modality}\n"
#     # dob = f"Date of Birth: {ds.PatientBirthDate}\n"
#     sex = f"Patient Sex: {ds.PatientSex}\n"
#     age = f"Patient Age: {ds.PatientAge}\n"
#     studyDate = f"Study Date: {ds.StudyDate}\n"
#     studyTime = f"Study Start Time: {ds.StudyTime}\n"
#     weight = f"Weight: {ds.PatientWeight}\n"
#     height = f"Height: {ds.PatientSize}\n"
#     operator = f"Operator: {ds.OperatorsName}\n"
 

for line in pathf:
    print(line)
    # Include path to dcm file below, with added starter as path is checked starting from home folder
    dicom_file = "neurodesktop-storage/JMRI1/dicom" + line[1:-1]
    
    # Load the DICOM file
    ds = pydicom.dcmread(dicom_file)
    
    # Extract basic metadata and check
    pName = f"{ds.PatientName}\t"
    # modality = f"Modality: {ds.Modality}\n"
    # dob = f"Date of Birth: {ds.PatientBirthDate}\n"
    sex = f"{ds.PatientSex}\t"
    age = f"{ds.PatientAge}\t"
    studyDate = f"{ds.StudyDate}\t"
    studyTime = f"{ds.StudyTime}\t"
    weight = f"{ds.PatientWeight}\t"
    height = f"{ds.PatientSize}\t"
    operator = f"{ds.OperatorsName}\t"
    
    
    # Add meta data to txt file
    f.write(pName)
    f.write(operator)
   # f.write(modality)
    f.write(age)
    f.write(sex)
    f.write(height)
    f.write(weight)
    #f.write("Date format: YYYYMMDD\n")
    #f.write(dob)
    f.write(studyDate)
    f.write(studyTime)
    f.write("\n")
    
    # Access specific DICOM tags
    # print(f"Pixel Spacing: {ds[0x0028, 0x0030].value}")
    
    # Iterate through all data elements
    # for elem in ds:
    #     print(f"{elem.tag}: {elem.name} = {elem.value}")

f.close() # close meta data file

pathf.close()  # close paths file
