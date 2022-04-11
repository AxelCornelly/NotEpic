-- Creating and using schema
DROP SCHEMA IF EXISTS epic_clone_project;
CREATE SCHEMA epic_clone_project;
USE epic_clone_project;

-- Creating Patient Table
CREATE TABLE patient (
	id INT NOT NULL,
    f_name VARCHAR(50),
    l_name VARCHAR(50),
    address VARCHAR(90),
    providerID INT,
    birthdate DATE,
    age INT,
    comments VARCHAR(1000),
    PRIMARY KEY (id));
    
-- Filling up table with data
INSERT INTO patient VALUES
(1, 'Jared', 'Keno', '1111 North Candy Rd, Everett, WA', 23, '1969-11-27', 53, 'Has severe headaches. Recommended Advil'),
(2, 'Johnny', 'Yi', '50501 56th Avenue E, Seattle, WA', 10, '2000-01-01', 22, 'Chronic knee pain. Has history playing Soccer, potential connection.'),
(3, 'Claire', 'Kim', '20211 North Rd APT-203, Bothell, WA', 5, '1999-10-13', 22, 'Has issues with lower back. Gymnast'),
(4, 'Eve', 'Daniels', '33333 2nd St, Lynnwood, WA', 11, '2003-04-11', 19, 'Poor vision in left eye. Needs to schedule with optomotry'),
(5, 'Chris', 'Turner', '54321 South St, Kent, WA', 1, '1998-12-05', 23, 'Requested a referal for physical therapy'),
(6, 'Jenny', 'Adams', '13505 59th Avenue W, Bellevue, WA', 55, '1980-05-05', 42, 'Bitten by a dog');
COMMIT;
