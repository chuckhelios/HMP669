
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Diagnosis;
CREATE TABLE Diagnosis (
	diagnosisNo INTEGER PRIMARY KEY autoincrement NOT NULL,
	daignosisDate DATE NOT NULL,
	diagnosis VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS Medication;
CREATE TABLE Medication (
	medicationNo INTEGER PRIMARY KEY autoincrement,
	medStartDate DATE NOT NULL,
	medEndDate DATE NOT NULL,
	medication VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS MedicalRecord;
CREATE TABLE MedicalRecord (
	MRN INTEGER PRIMARY KEY autoincrement NOT NULL,
	diagnosisNo INTEGER,
	daignosisDesription VARCHAR(100) NOT NULL,
	medicationNo INTEGER,
	reasonForMedication VARCHAR(100) NOT NULL,
	FOREIGN KEY(medicationNo) REFERENCES Medication(med),
	FOREIGN KEY(diagnosisNo) REFERENCES Diagnosis(diagnosisNo)
);

DROP TABLE IF EXISTS Resident;
CREATE TABLE Resident (
	residentId VARCHAR(10) PRIMARY KEY NOT NULL,
	nameFirst VARCHAR(20) NOT NULL,
	nameLast VARCHAR(20) NOT NULL,
	dob DATE NOT NULL,
	gender CHAR(1) NOT NULL CHECK (gender IN('M','F')),
	MRN INTEGER,
	roomNo INTEGER,
	buildingCode CHAR(2),
	hospitalPreference VARCHAR(100),
	emergencyContacts VARCHAR(500) NOT NULL,
	emergencyPhoneNo VARCHAR(10) NOT NULL,
	phoneNo VARCHAR(10) NOT NULL,
	phoneType VARCHAR(20),
	FOREIGN KEY(MRN) REFERENCES MedicalRecord(MRN),
	FOREIGN KEY(buildingCode) REFERENCES Building(buildingCode)
);

DROP TABLE IF EXISTS Building;
CREATE TABLE Building (
	buildingCode CHAR(2) PRIMARY KEY NOT NULL,
	name VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS VitalSignsType;
CREATE TABLE VitalSignsType (
	typeCode CHAR(1) PRIMARY KEY NOT NULL,
	name VARCHAR(20) NOT NULL
);

DROP TABLE IF EXISTS VitalSigns;
CREATE TABLE VitalSigns (
	uniqueId INTEGER PRIMARY KEY autoincrement NOT NULL,
	eventId INTEGER NOT NULL,
	empId VARCHAR(10) NOT NULL,
	assesmDateTime DATE NOT NULL,
	vitalType CHAR(1) NOT NULL,
	results VARCHAR(100),
	comments VARCHAR(500),
	FOREIGN KEY(eventId) REFERENCES IncidentReport(eventId),
	FOREIGN KEY(empId) REFERENCES Employee(empId),
	FOREIGN KEY(vitalType) REFERENCES VitalSignsType(typeCode)
);

DROP TABLE IF EXISTS Hospital;
CREATE TABLE Hospital (
	hospitalId CHAR(3) PRIMARY KEY NOT NULL,
	name VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS IncidentReport;
CREATE TABLE IncidentReport (
	eventId INTEGER PRIMARY KEY autoincrement NOT NULL,
	empId INTEGER NOT NULL,
	residentId VARCHAR(10) NOT NULL,
	startDateTime DATE NOT NULL,
	endDateTime DATE NOT NULL,
	narrative VARCHAR(1500),
	hospitalId CHAR(3) NOT NULL,
	FOREIGN KEY(residentId) REFERENCES Resident(residentId),
	FOREIGN KEY(empId) REFERENCES Employee(empId),
	FOREIGN KEY(hospitalId) REFERENCES Hospital(hospitalId)
);

DROP TABLE IF EXISTS Employee;
CREATE TABLE Employee (
	empId VARCHAR(10) PRIMARY KEY NOT NULL,
	nameFirst VARCHAR(20) NOT NULL,
	nameLast VARCHAR(20) NOT NULL,
	userName VARCHAR(20) NOT NULL,
	password VARCHAR(20) NOT NULL,
	phoneNumber VARCHAR(10) NOT NULL,
	empType VARCHAR(3)
);


-- insert statements

INSERT INTO Diagnosis VALUES ('101','2013-11-21','Lower Back Pain');
INSERT INTO Diagnosis VALUES ('102','2014-02-12','Diabetes');
INSERT INTO Diagnosis VALUES ('103','2015-12-24','Pancreatitis');

INSERT INTO Medication VALUES ('201','2011-11-21','2016-12-08','Propanol');
INSERT INTO Medication VALUES ('202','2015-01-10','2015-12-08','Insulin');
INSERT INTO Medication VALUES ('203','2012-04-04','2017-12-08','Aspirin');

INSERT INTO MedicalRecord VALUES ('1000045','101','Sports Injury','201','For Pain');
INSERT INTO MedicalRecord VALUES ('1000046','102','Diabetes','202','For Blood Sugar');
INSERT INTO MedicalRecord VALUES ('1000047','103','Diabetes','203','For Pain');


INSERT INTO Resident (residentId, nameFirst, nameLast, dob, gender, MRN, roomNo, buildingCode, hospitalPreference, emergencyContacts, emergencyPhoneNo,phoneNo, phoneType)
VALUES ('123456789','John','Locke','1936-11-01','M','1000045','333','FP','St. Joseph Mercy','Jack Locke - Son', '7341111111', '7341211111', 'cell phone');
INSERT INTO Resident (residentId, nameFirst, nameLast, dob, gender, MRN, roomNo, buildingCode, hospitalPreference, emergencyContacts, emergencyPhoneNo,phoneNo, phoneType)
VALUES ('123456790','Jill','Idersson','1946-12-11','F','1000046','105','HP','University of Michigan Hospital','Jacky - Daughter', '7346115111', '7341311111', 'cell phone');
INSERT INTO Resident (residentId, nameFirst, nameLast, dob, gender, MRN, roomNo, buildingCode, hospitalPreference, emergencyContacts, emergencyPhoneNo,phoneNo, phoneType)
VALUES ('123456791','Patty','Obo','1939-01-06','F','1000047','301','HG','St. Joseph Mercy','No Info', '7341711511', '7347219111', 'cell phone');

INSERT INTO Building VALUES ('HG','Hickory Grove');
INSERT INTO Building VALUES ('HP','Hudson Park');
INSERT INTO Building VALUES ('FP','Fountain Point');
INSERT INTO Building VALUES ('MG','Medison Green');
INSERT INTO Building VALUES ('MS','Meadowbrook Square');
INSERT INTO Building VALUES ('CC','Chelsea Court');

INSERT INTO VitalSignsType VALUES ('S','Systolic BP');
INSERT INTO VitalSignsType VALUES ('D','Diastolic BP');
INSERT INTO VitalSignsType VALUES ('W','Weight');
INSERT INTO VitalSignsType VALUES ('H','Height');
INSERT INTO VitalSignsType VALUES ('P','Pulse');
INSERT INTO VitalSignsType VALUES ('R','Respiration');

INSERT INTO VitalSigns VALUES (NULL,'111','EMT001','2014-11-21 10:30','S','120.1',NULL);
INSERT INTO VitalSigns VALUES (NULL,'112','EMT001','2015-11-11 10:33','D','90',NULL);
INSERT INTO VitalSigns VALUES (NULL,'113','EMT002','2014-10-01 10:35','W','120.7',NULL);

INSERT INTO Hospital VALUES ('SJM','St. Jospeh Mercy');
INSERT INTO Hospital VALUES ('NOT','No Transport');
INSERT INTO Hospital VALUES ('UOM','University of Michigan');
INSERT INTO Hospital VALUES ('HFO','Henry Ford Medical Center');

INSERT INTO IncidentReport VALUES ('00001','EMT001','123456789','2014-11-21 10:30','2014-11-21 11:30',NULL,'HFO');
INSERT INTO IncidentReport VALUES ('00002','EMT001','123456790','2015-10-21 11:00','2015-10-21 11:30',NULL,'NOT');
INSERT INTO IncidentReport VALUES ('00003','EMT002','123456791','2015-10-22 16:40','2015-10-22 16:55',NULL,'NOT');

INSERT INTO Employee VALUES ('EMT001','DJ','Petrovic','djpetrov','hmp669','7340001000','EMT');
INSERT INTO Employee VALUES ('EMT002','Yang','Li','yanglixx','hmp669','7340002000','EMT');
INSERT INTO Employee VALUES ('EMT003','Ding','He','dinghe','hmp669','7340003000','PHY');

