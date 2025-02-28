from sys import dont_write_bytecode
from unicodedata import name
import pydicom


# Include path to dcm file below
dicom_file = "neurodesktop-storage/JMRI1/dicom/BAY795_20221017/6_t1_mprage_sag_p2_iso/JMR1_BAY795_202.MR.Barense_Jackson.6.1.2022.10.17.14.59.55.508.19428856.dcm"
 # "neurodesktop-storage/JMRI1/dicom/YA99108_20230428/6_t1_mprage_sag_p2_iso/JMR1_YA99108_20.MR.Barense_Natalia.6.1.2023.04.28.14.47.16.132.27777384.dcm"

# Load the DICOM file
ds = pydicom.dcmread(dicom_file)

# Uncomment below to check meta data avialable for patient (JMRI1 dicoms do NOT have coil data)
# for element in ds:
#     print(element)


# Extract basic metadata and check
pName = f"Patient Name: {ds.PatientName}\n"
modality = f"Modality: {ds.Modality}\n"
dob = f"Date of Birth: {ds.PatientBirthDate}\n"
sex = f"Patient Sex: {ds.PatientSex}\n"
age = f"Patient Age: {ds.PatientAge}\n"
studyDate = f"Study Date: {ds.StudyDate}\n"
studyTime = f"Study Start Time: {ds.StudyTime}\n"
weight = f"Weight: {ds.PatientWeight}\n"
height = f"Height: {ds.PatientSize}\n"
operator = f"Operator: {ds.OperatorsName}\n"


# Create and add to txt file
file_name = f"{ds.PatientName}_MetaInfo.txt"
f = open(file_name, "w")
f.close()
f = open(file_name, "a")
f.write(pName)
f.write(operator)
f.write(modality)
f.write(age)
f.write(sex)
f.write(height)
f.write(weight)
f.write("Date format: YYYYMMDD\n")
f.write(dob)
f.write(studyDate)
f.write(studyTime)
f.close()

# Access specific DICOM tags
print(f"Pixel Spacing: {ds[0x0028, 0x0030].value}")

# Iterate through all data elements
for elem in ds:
    print(f"{elem.tag}: {elem.name} = {elem.value}")
