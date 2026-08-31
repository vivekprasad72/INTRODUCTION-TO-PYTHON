# Hospital Management System

# 1. Patient Registration - Dictionary

patient = {
    "id": 101,
    "name": "Rohul",
    "age": 21,
    "disease": "Fever"
}

print("Patient Details")
print("ID:", patient["id"])
print("Name:", patient["name"])
print("Age:", patient["age"])
print("Disease:", patient["disease"])


# 2. Appointment Scheduling - List

appointments = []

appointments.append("10:00 AM - Dr. Vivek")
appointments.append("11:00 AM - Dr. Janvi")

print("\nAppointments:")
for appointment in appointments:
    print(appointment)


# 3. Medical Records - File Handling

file = open("medical_record.txt", "w")

file.write("Patient Name: " + patient["name"] + "\n")
file.write("Disease: " + patient["disease"] + "\n")
file.write("Medicine: Paracetamol\n")

file.close()

print("\nMedical record saved.")


# 4. Doctor Information - Tuple

doctor = ("Dr. Janvi", "Cardiologist", "10:00 AM")

print("\nDoctor Information")
print("Name:", doctor[0])
print("Specialization:", doctor[1])
print("Available Time:", doctor[2])


# 5. Billing System - Class and Object

class Bill:

    def __init__(self, consultation, medicine):
        self.consultation = consultation
        self.medicine = medicine

    def total(self):
        return self.consultation + self.medicine


bill1 = Bill(500, 300)

print("\nBilling")
print("Consultation:", bill1.consultation)
print("Medicine:", bill1.medicine)
print("Total Bill:", bill1.total())


# 6. Report Generation - Python Library

import datetime

print("\nHospital Report")
print("Report Generated On:", datetime.datetime.now())
print("Patient:", patient["name"])
print("Total Bill:", bill1.total())