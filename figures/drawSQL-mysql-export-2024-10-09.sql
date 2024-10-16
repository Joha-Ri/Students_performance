CREATE TABLE `Students`(
    `ID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Gender` BIGINT NOT NULL,
    `Age` INT NOT NULL,
    `Ethnicity` BIGINT NOT NULL
);
ALTER TABLE
    `Students` ADD INDEX `students_id_index`(`ID`);
CREATE TABLE `Parentalinfo`(
    `StudentID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `ParentalEducationLevel` INT NOT NULL,
    `ParentalSupport` BIGINT NOT NULL
);
CREATE TABLE `Extracurricularactivities`(
    `ExtracurricularactivitiesID` INT NOT NULL,
    `StudentID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Activitytype` VARCHAR(20) NOT NULL,
    `Participation` INT NOT NULL,
    PRIMARY KEY(`ExtracurricularactivitiesID`)
);
CREATE TABLE `Academicperformance`(
    `StudentID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Gradeclass` INT NOT NULL,
    `GPA` FLOAT(53) NOT NULL,
    `Year` INT NOT NULL,
    `Succes` INT NOT NULL
);
ALTER TABLE
    `Extracurricularactivities` ADD CONSTRAINT `extracurricularactivities_studentid_foreign` FOREIGN KEY(`StudentID`) REFERENCES `Students`(`ID`);
ALTER TABLE
    `Academicperformance` ADD CONSTRAINT `academicperformance_studentid_foreign` FOREIGN KEY(`StudentID`) REFERENCES `Students`(`ID`);
ALTER TABLE
    `Students` ADD CONSTRAINT `students_id_foreign` FOREIGN KEY(`ID`) REFERENCES `Parentalinfo`(`StudentID`);