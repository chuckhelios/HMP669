PRAGMA foreign_keys = ON;


DROP TABLE IF EXISTS Diagnosis;
CREATE TABLE Diagnosis (
	diagnosisNo INTEGER PRIMARY KEY autoincrement,
	diagnosis VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS Medication;
CREATE TABLE Medication (
	medicationNo INTEGER PRIMARY KEY autoincrement,
	medication VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS RecordMedicationtbl;
CREATE TABLE RecordMedicationtbl (
	rmid INTEGER NOT NULL PRIMARY KEY autoincrement,
	MRN INTEGER NOT NULL,
	medicationNo INTEGER NOT NULL,
	medStartDate DATE NOT NULL,
	medEndDate DATE NOT NULL,
	FOREIGN KEY(medicationNo) REFERENCES Medication(medicationNo),
	FOREIGN KEY(MRN) REFERENCES ResidentMedicalRecord(MRN)
);

DROP TABLE IF EXISTS RecordDiagnosistbl;
CREATE TABLE RecordDiagnosistbl (
	id INTEGER NOT NULL PRIMARY KEY autoincrement,
	MRN INTEGER NOT NULL,
	diagnosisNo INTEGER NOT NULL,
	daignosisDate DATE NOT NULL,
	FOREIGN KEY(diagnosisNo) REFERENCES Diagnosis(diagnosisNo),
	FOREIGN KEY(MRN) REFERENCES ResidentMedicalRecord(MRN)
);

DROP TABLE IF EXISTS ResidentMedicalRecord;
CREATE TABLE ResidentMedicalRecord (
	MRN INTEGER PRIMARY KEY autoincrement,
	nameFirst VARCHAR(20) NOT NULL,
	nameLast VARCHAR(20) NOT NULL,
	dob DATE NOT NULL,
	gender CHAR(1) NOT NULL CHECK (gender IN('M','F')),
	roomNo INTEGER,
	buildingCode CHAR(2),
	hospitalPreference VARCHAR(100),
	emergencyContacts VARCHAR(500) NOT NULL,
	emergencyPhoneNo VARCHAR(10) NOT NULL,
	phoneNo VARCHAR(10) NOT NULL,
	phoneType VARCHAR(20),
	-- diagnosisNo INTEGER,
	-- daignosisDesription VARCHAR(100) NOT NULL,
	-- medicationNo INTEGER,
	-- reasonForMedication VARCHAR(100) NOT NULL,
	-- FOREIGN KEY(medicationNo) REFERENCES RecordMedicationtbl(medicationNo),
	-- FOREIGN KEY(diagnosisNo) REFERENCES RecordDiagnosistbl(diagnosisNo),
	FOREIGN KEY(buildingCode) REFERENCES Building(buildingCode)
);

DROP TABLE IF EXISTS Building;
CREATE TABLE Building (
	buildingCode CHAR(2) PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS VitalSignsType;
CREATE TABLE VitalSignsType (
	typeCode CHAR(1) PRIMARY KEY,
	name VARCHAR(20) NOT NULL
);

DROP TABLE IF EXISTS VitalSigns;
CREATE TABLE VitalSigns (
	uniqueId INTEGER PRIMARY KEY autoincrement,
	eventId INTEGER NOT NULL,
	empId VARCHAR(10) NOT NULL,
	assesmDateTime DATETIME NOT NULL,
	vitalType CHAR(1) NOT NULL,
	results VARCHAR(100),
	comments VARCHAR(500),
	FOREIGN KEY(eventId) REFERENCES IncidentReport(eventId),
	FOREIGN KEY(empId) REFERENCES Employee(empId),
	FOREIGN KEY(vitalType) REFERENCES VitalSignsType(typeCode)
);

DROP TABLE IF EXISTS Hospital;
CREATE TABLE Hospital (
	hospitalId CHAR(3) PRIMARY KEY,
	name VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS IncidentReport;
CREATE TABLE IncidentReport (
	eventId INTEGER PRIMARY KEY autoincrement,
	empId INTEGER NOT NULL,
	MRN INTEGER NOT NULL,
	startDateTime DATETIME NOT NULL,
	endDateTime DATETIME NOT NULL,
	narrative VARCHAR(1500),
	hospitalId CHAR(3) NOT NULL,
	FOREIGN KEY(MRN) REFERENCES ResidentMedicalRecord(MRN),
	FOREIGN KEY(empId) REFERENCES Employee(empId),
	FOREIGN KEY(hospitalId) REFERENCES Hospital(hospitalId)
);

DROP TABLE IF EXISTS Employee;
CREATE TABLE Employee (
	empId VARCHAR(10) PRIMARY KEY,
	nameFirst VARCHAR(20) NOT NULL,
	nameLast VARCHAR(20) NOT NULL,
	userName VARCHAR(20) NOT NULL,
	password VARCHAR(20) NOT NULL,
	phoneNumber VARCHAR(10) NOT NULL,
	empType VARCHAR(3)
);


-- insert statements


INSERT INTO Diagnosis VALUES ('101','Lower Back Pain');
INSERT INTO Diagnosis VALUES ('102','Diabetes');
INSERT INTO Diagnosis VALUES ('103','Pancreatitis');
INSERT INTO Diagnosis VALUES ('104','Hypertension');

INSERT INTO RecordDiagnosistbl VALUES (1,'1000045','101','2013-11-21');
INSERT INTO RecordDiagnosistbl VALUES (2,'1000046','102','2014-02-12');
INSERT INTO RecordDiagnosistbl VALUES (3,'1000047','103','2015-04-04');
INSERT INTO RecordDiagnosistbl VALUES (4,'1000048','102','2012-09-09');
INSERT INTO RecordDiagnosistbl VALUES (5,'1000049','104','2013-11-21');
INSERT INTO RecordDiagnosistbl VALUES (6,'1000050','102','2014-02-12');
INSERT INTO RecordDiagnosistbl VALUES (7,'1000051','104','2015-04-04');
INSERT INTO RecordDiagnosistbl VALUES (8,'1000052','103','2012-09-09');
INSERT INTO RecordDiagnosistbl VALUES (9,'1000053','104','2013-11-21');
INSERT INTO RecordDiagnosistbl VALUES (10,'1000054','102','2014-02-12');
INSERT INTO RecordDiagnosistbl VALUES (11,'1000055','104','2015-04-04');
INSERT INTO RecordDiagnosistbl VALUES (12,'1000056','103','2012-09-09');

INSERT INTO Medication VALUES ('201','Propanol');
INSERT INTO Medication VALUES ('202','Insulin');
INSERT INTO Medication VALUES ('203','Aspirin');
INSERT INTO Medication VALUES ('204','Furosemide');

INSERT INTO RecordMedicationtbl VALUES (1,'1000045','201','2013-11-21','2016-12-08');
INSERT INTO RecordMedicationtbl VALUES (2,'1000046','202','2014-02-12','2015-12-08');
INSERT INTO RecordMedicationtbl VALUES (3,'1000047','203','2015-04-04','2017-12-08');
INSERT INTO RecordMedicationtbl VALUES (4,'1000048','202','2012-09-09','2017-12-08');
INSERT INTO RecordMedicationtbl VALUES (5,'1000049','204','2013-11-21','2016-12-08');
INSERT INTO RecordMedicationtbl VALUES (6,'1000050','202','2014-02-12','2015-12-08');
INSERT INTO RecordMedicationtbl VALUES (7,'1000051','204','2015-04-04','2017-12-08');
INSERT INTO RecordMedicationtbl VALUES (8,'1000052','203','2012-09-09','2017-12-08');
INSERT INTO RecordMedicationtbl VALUES (9,'1000053','204','2013-11-21','2016-12-08');
INSERT INTO RecordMedicationtbl VALUES (10,'1000054','202','2014-02-12','2015-12-08');
INSERT INTO RecordMedicationtbl VALUES (11,'1000055','204','2015-04-04','2017-12-08');
INSERT INTO RecordMedicationtbl VALUES (12,'1000056','203','2012-09-09','2017-12-08');

INSERT INTO ResidentMedicalRecord VALUES ('1000045','John','Locke','1936-11-01','M','333','FP','St. Joseph Mercy','Jack Locke - Son', '7341111111', '7341211111', 'cell phone');
INSERT INTO ResidentMedicalRecord VALUES ('1000046','Jill','Idersson','1946-12-11','F','105','HP','University of Michigan Hospital','Jacky - Daughter', '7346115111', '7341311111', 'cell phone');
INSERT INTO ResidentMedicalRecord VALUES ('1000047','Patty','Obo','1939-01-06','F','301','HG','St. Joseph Mercy','No Info', '7341711511', '7347219111', 'cell phone');
INSERT INTO ResidentMedicalRecord VALUES ('1000048','Kat','Pingel','1942-10-10','F','202','MG','Henry Ford Medical Center','Ms. Lo - Daughter','7341234567','7341235678','cell phone');
INSERT INTO ResidentMedicalRecord VALUES ('1000049','Micky','Mouse','1946-11-01','M','101','FP','University of Michigan Hospital','Mose Mouse - Son', '7340000000', '7346666666', 'cell phone');
INSERT INTO ResidentMedicalRecord VALUES ('1000050','Minnie','Mouse','1948-12-11','F','101','FP','University of Michigan Hospital','Mose Mouse - Son', '7340000000', '7346666661', 'cell phone');
INSERT INTO ResidentMedicalRecord VALUES ('1000051','Jenny','Ford','1938-01-06','F','201','CC','St. Joseph Mercy','No Info', '7342222222', '7343333333', 'cell phone');
INSERT INTO ResidentMedicalRecord VALUES ('1000052','Jimmy','Miller','1948-10-10','M','202','CC','Henry Ford Medical Center','Larry Miller- Son','7345555555','7347777777','cell phone');
INSERT INTO ResidentMedicalRecord VALUES ('1000053','Moon','Smith','1946-11-01','F','103','MS','Elisabeth Hospital','Betty Smith - Niece', '7340000001', '7346666665', 'cell phone');
INSERT INTO ResidentMedicalRecord VALUES ('1000054','Sun','Smith','1948-12-11','M','103','MS','Elisabeth Hospital','Betty Smith - Niece', '7340000001', '7346666668', 'cell phone');
INSERT INTO ResidentMedicalRecord VALUES ('1000055','Wendy','Green','1938-07-06','F','205','CC','St. Joseph Mercy','No Info','7349876543', '7349876542', 'cell phone');
INSERT INTO ResidentMedicalRecord VALUES ('1000056','William','Green','1939-10-24','M','205','CC','St. Joseph Mercy','No Info','7349876543','7349876545','cell phone');

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
INSERT INTO VitalSignsType VALUES ('T','Temperature');

INSERT INTO VitalSigns VALUES (1,'00001','EMT001','2014-11-21 10:30','S','120.1',NULL);
INSERT INTO VitalSigns VALUES (2,'00002','EMT001','2015-10-21 11:33','D','90',NULL);
INSERT INTO VitalSigns VALUES (3,'00003','EMT002','2015-10-23 10:35','W','120.7',NULL);
INSERT INTO VitalSigns VALUES (4,'00004','EMT003','2015-01-23 10:32','T','98.6',NULL);
INSERT INTO VitalSigns VALUES (5,'00005','EMT005','2014-10-12 10:10','R','14',NULL);
INSERT INTO VitalSigns VALUES (6,'00005','EMT005','2014-10-12 10:19','T','98.9',NULL);
INSERT INTO VitalSigns VALUES (7,'00005','EMT005','2014-10-12 10:21','P','88',NULL);
INSERT INTO VitalSigns VALUES (8,'00006','EMT004','2013-10-11 16:02','S','110.6',NULL);
INSERT INTO VitalSigns VALUES (9,'00006','EMT004','2013-10-11 16:02','D','70.6',NULL);
INSERT INTO VitalSigns VALUES (10,'00006','EMT004','2013-10-11 16:10','R','14',NULL);
INSERT INTO VitalSigns VALUES (11,'00006','EMT004','2013-10-11 16:19','T','98.9',NULL);
INSERT INTO VitalSigns VALUES (12,'00006','EMT004','2013-10-11 16:21','P','88',NULL);


INSERT INTO Hospital VALUES ('SJM','St. Jospeh Mercy');
INSERT INTO Hospital VALUES ('NOT','No Transport');
INSERT INTO Hospital VALUES ('UOM','University of Michigan');
INSERT INTO Hospital VALUES ('HFO','Henry Ford Medical Center');
INSERT INTO Hospital VALUES ('EBH','Elisabeth Hospital');


INSERT INTO IncidentReport VALUES ('00001','EMT001','1000045','2014-11-21 10:30','2014-11-21 11:30',NULL,'HFO');
INSERT INTO IncidentReport VALUES ('00002','EMT001','1000046','2015-10-21 11:00','2015-10-21 11:30',NULL,'NOT');
INSERT INTO IncidentReport VALUES ('00003','EMT002','1000047','2015-10-22 16:40','2015-10-22 16:55',NULL,'NOT');
INSERT INTO IncidentReport VALUES ('00004','EMT002','1000048','2015-01-22 16:40','2015-01-22 16:55',NULL,'NOT');
INSERT INTO IncidentReport VALUES ('00005','EMT005','1000046','2014-10-11 22:23','2014-10-11 23:00','Fell down, out of concious','UOM');
INSERT INTO IncidentReport VALUES ('00006','EMT004','1000052','2013-10-11 15:23','2013-10-11 16:00','Pain','HFO');



INSERT INTO Employee VALUES ('EMT001','DJ','Petrovic','djpetrov','hmp669','7340001000','EMT');
INSERT INTO Employee VALUES ('EMT002','Yang','Li','yanglixx','hmp669','7340002000','EMT');
INSERT INTO Employee VALUES ('EMT003','Ding','He','dinghe','hmp669','7340003000','PHY');
INSERT INTO Employee VALUES ('EMT004','Jianyu','Lai','jianyul','hmp669','7340004000','EMT');
INSERT INTO Employee VALUES ('EMT005','Ye','Zhang','zhangye','hmp669','7340005000','EMT');
INSERT INTO Employee VALUES ('admin','Yang','Li','yanglixx','hmp669','7340002000','EMT');
