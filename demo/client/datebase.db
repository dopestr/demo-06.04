CREATE TABLE IF NOT EXISTS Patients (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255),
    l_name VARCHAR(255),
    middle_name VARCHAR(255),
    passport_number VARCHAR(255),
    date_of_birth DATE,
    gender ('male', 'female'),
    address VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    medical_card_number VARCHAR(255)ast,
    date_of_issue_of_medical_card DATE,
    date_of_last_visit DATE,
    date_of_next_visit DATE,
    insurance_policy_number VARCHAR(255),
    insurance_policy_end_date DATE
);

CREATE TABLE IF NOT EXISTS Doctors (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    specialization VARCHAR(255),
    work_experience INT,
    salary DECIMAL(10, 2),
    work_schedule VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Departments (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    head_of_department VARCHAR(255),
    number_of_beds INT,
    address VARCHAR(255),
    phone VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Appointment_Schedule (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    doctor_id INT,
    day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(id)
);

CREATE TABLE IF NOT EXISTS Medications (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    form VARCHAR(255),
    dosage VARCHAR(255),
    manufacturer VARCHAR(255),
    price DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS Diagnoses (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    description TEXT
);

INSERT INTO Patients (first_name,  last_name,  middle_name,passport_number, date_of_birth, gender, address, phone, email, date_of_issue_of_medical_card,  date_of_last_visit, date_of_next_visit, insurance_policy_number, insurance_policy_end_date)
VALUES
    ('John', 'Doe', 'Edward', 'AB1234567', '1985-06-15', 'male', '123 Main St', '555-1234', 'john.doe@example.com', 'MC123456789', '2010-05-01', '2023-03-12', '2023-05-16', 'IP789101112', '2024-06-30'),
    ('Jane', 'Smith', 'Ann', 'CD8901234', '1990-09-24', 'female', '456 Broad Ave', '555-5678', 'jane.smith@example.com', 'MC987654321', '2015-07-21', '2023-04-10', '2023-06-21', 'IP213141516', '2025-07-20');


INSERT INTO Doctors (first_name, last_name, specialization, work_experience, salary, work_schedule)
VALUES
    ('John', 'Doe', 'Cardiologist', 10, 120000.00, 'Mon-Fri 09:00-17:00'),
    ('Jane', 'Smith', 'Neurologist', 8, 115000.00, 'Mon-Fri 10:00-18:00');

INSERT INTO Departments (name, head_of_department, number_of_beds, address, phone)
VALUES
    ('Cardiology', 'John Doe', 20, '123 Heartbeat Blvd, Health City', '555-1234'),
    ('Neurology', 'Jane Smith', 15, '456 Brainwave St, Health City', '555-5678');

INSERT INTO Appointment_Schedule (doctor_id, day_of_week, start_time, end_time)
VALUES
    (1, 'Monday', '09:00', '12:00'),
    (2, 'Wednesday', '12:00', '15:00');


INSERT INTO Medications (name, form, dosage, manufacturer, price)
VALUES
    ('Aspirin', 'Tablet', '100mg', 'Global Pharma', 5.99),
    ('Tylenol', 'Capsule', '500mg', 'HealthCorp', 7.99);

INSERT INTO Diagnoses (name, description)
VALUES
    ('Hypertension', 'A condition in which the blood pressure in the arteries is persistently elevated.'),
    ('Migraine', 'A primary headache disorder characterized by recurrent headaches that are moderate to severe.');
