-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: BloodDonationDB
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bloodbank`
--

DROP TABLE IF EXISTS `bloodbank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bloodbank` (
  `hospital_id` int NOT NULL,
  `A+` int DEFAULT NULL,
  `A-` int DEFAULT NULL,
  `B+` int DEFAULT NULL,
  `B-` int DEFAULT NULL,
  `AB+` int DEFAULT NULL,
  `AB-` int DEFAULT NULL,
  `O+` int DEFAULT NULL,
  `O-` int DEFAULT NULL,
  PRIMARY KEY (`hospital_id`),
  CONSTRAINT `bloodbank_ibfk_1` FOREIGN KEY (`hospital_id`) REFERENCES `hospital` (`hospital_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bloodbank`
--

LOCK TABLES `bloodbank` WRITE;
/*!40000 ALTER TABLE `bloodbank` DISABLE KEYS */;
INSERT INTO `bloodbank` VALUES (1,15,3,12,3,8,1,18,2),(2,10,3,11,3,7,1,19,1),(3,8,2,13,3,9,2,17,2),(4,18,4,15,2,10,1,20,2),(5,14,3,11,2,6,1,16,2),(6,4,3,12,2,6,1,18,1),(7,17,2,16,2,8,1,19,1),(8,12,2,13,3,6,1,16,1),(9,11,3,14,2,7,2,18,2),(10,16,3,12,2,9,1,17,2),(11,15,2,13,3,10,1,19,1),(12,14,3,11,2,6,1,18,2);
/*!40000 ALTER TABLE `bloodbank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bloodrequest`
--

DROP TABLE IF EXISTS `bloodrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bloodrequest` (
  `request_id` int NOT NULL AUTO_INCREMENT,
  `hospital_id` int DEFAULT NULL,
  `blood_group` varchar(5) NOT NULL,
  `units_required` int DEFAULT NULL,
  `request_date` date NOT NULL DEFAULT (curdate()),
  PRIMARY KEY (`request_id`),
  KEY `hospital_id` (`hospital_id`),
  CONSTRAINT `bloodrequest_ibfk_1` FOREIGN KEY (`hospital_id`) REFERENCES `hospital` (`hospital_id`) ON DELETE CASCADE,
  CONSTRAINT `bloodrequest_chk_1` CHECK ((`units_required` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bloodrequest`
--

LOCK TABLES `bloodrequest` WRITE;
/*!40000 ALTER TABLE `bloodrequest` DISABLE KEYS */;
INSERT INTO `bloodrequest` VALUES (1,1,'O+',2,'2025-03-05'),(2,2,'A-',3,'2025-03-05'),(3,1,'O+ ve',1,'2025-03-07'),(4,2,'O+ ve',3,'2025-03-11');
/*!40000 ALTER TABLE `bloodrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donor`
--

DROP TABLE IF EXISTS `donor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donor` (
  `donor_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `age` int DEFAULT NULL,
  `blood_group` varchar(5) NOT NULL,
  `contact` varchar(15) NOT NULL,
  `city` varchar(100) NOT NULL,
  `last_donation_date` date DEFAULT NULL,
  PRIMARY KEY (`donor_id`),
  CONSTRAINT `donor_chk_1` CHECK ((`age` >= 18))
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donor`
--

LOCK TABLES `donor` WRITE;
/*!40000 ALTER TABLE `donor` DISABLE KEYS */;
INSERT INTO `donor` VALUES (1,'Rahul Sharma',25,'O+','9876543210','Mumbai','2024-01-10'),(2,'Priya Verma',22,'A-','9876543211','Delhi','2023-12-15'),(3,'Arjun Singh',30,'B+','9876543212','Chennai','2023-11-05'),(4,'Navaneeth Krishna G',19,'A+','9562153025','Trivandrum',NULL),(5,'Narendra Modi',88,'AB-','4349939430','New delhi',NULL),(6,'valorant',821,'3','32','23',NULL),(7,'Navaneeth Krishna G',54,'54','54','54',NULL),(8,'Navaneeth Krishna G',32,'A+','9562153025','Ottapalam','2025-03-10'),(9,'Navaneeth Krishna G',32,'A+','9562153025','233232','2025-03-10'),(10,'text_manipulation_dataset',41,'A+','6458758573','fgbxcbf','2025-03-11'),(11,'valorant',54,'A+','4435785953','Trivandrum','2025-03-11'),(12,'valorant',54,'A+','4435785953','Trivandrum','2025-03-11'),(13,'valorant',54,'A+','4435785953','Trivandrum','2025-03-11'),(14,'valorant',54,'A+','4435785953','Trivandrum','2025-03-11'),(15,'valorant',54,'A+','4435785953','Trivandrum','2025-03-11'),(16,'valorant',54,'A+','4435785953','Trivandrum','2025-03-11'),(17,'valorant',54,'A+','4435785953','Trivandrum','2025-03-11'),(18,'valorant',54,'A+','4435785953','Trivandrum','2025-03-11'),(19,'valorant',54,'A+','4435785953','Trivandrum','2025-03-11'),(20,'valorant',54,'A+','4435785953','Trivandrum','2025-03-11'),(21,'valorant',54,'A+','4435785953','Trivandrum','2025-03-11'),(22,'valorant',54,'A+','4435785953','Trivandrum','2025-03-11'),(23,'hey',34,'A+','9562153025','fgbxcbf','2025-03-11'),(24,'hey',34,'A+','9562153025','fgbxcbf','2025-03-11'),(25,'NIrf bot',54,'B-','3443433434','2','2025-03-11'),(26,'skibidi',19,'A-','3243224634','vf','2025-03-12'),(27,'girish',49,'B+','9061153025','Muscat','2025-03-12'),(28,'Naveen',34,'O+','7476576756','tirivala','2025-03-20');
/*!40000 ALTER TABLE `donor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospital`
--

DROP TABLE IF EXISTS `hospital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospital` (
  `hospital_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `contact` varchar(15) NOT NULL,
  PRIMARY KEY (`hospital_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospital`
--

LOCK TABLES `hospital` WRITE;
/*!40000 ALTER TABLE `hospital` DISABLE KEYS */;
INSERT INTO `hospital` VALUES (1,'City Hospital','Mumbai','9123456789'),(2,'Apollo Hospital','Delhi','9234567890'),(3,'Fortis Hospital','Bangalore','9345678901'),(4,'AIIMS','Delhi','9456789012'),(5,'KIMS Hospital','Hyderabad','9567890123'),(6,'Sunshine Hospital','Chennai','9678901234'),(7,'Manipal Hospital','Pune','9789012345'),(8,'Max Super Specialty Hospital','Kolkata','9890123456'),(9,'Medanta Hospital','Gurgaon','9901234567'),(10,'Narayana Health','Bangalore','9012345678'),(11,'CMC Vellore','Vellore','9123456789'),(12,'Apollo Specialty Hospital','Mumbai','9234567890');
/*!40000 ALTER TABLE `hospital` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passwords`
--

DROP TABLE IF EXISTS `passwords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passwords` (
  `hospital_id` int NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`hospital_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passwords`
--

LOCK TABLES `passwords` WRITE;
/*!40000 ALTER TABLE `passwords` DISABLE KEYS */;
INSERT INTO `passwords` VALUES (1,'password123'),(2,'hospital234'),(3,'secure345'),(4,'health456'),(5,'bloodbank567'),(6,'trivandrum678'),(7,'medicare789'),(8,'healing890'),(9,'curefast901'),(10,'healthylife111'),(11,'redcross222'),(12,'savelife333');
/*!40000 ALTER TABLE `passwords` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `age` int DEFAULT NULL,
  `blood_group` enum('A+','A-','B+','B-','AB+','AB-','O+','O-') NOT NULL,
  `hospital_id` int NOT NULL,
  `units_needed` int DEFAULT NULL,
  `request_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Recieved` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`patient_id`),
  KEY `hospital_id` (`hospital_id`),
  CONSTRAINT `patients_ibfk_1` FOREIGN KEY (`hospital_id`) REFERENCES `hospital` (`hospital_id`) ON DELETE CASCADE,
  CONSTRAINT `patients_chk_1` CHECK ((`age` > 0)),
  CONSTRAINT `patients_chk_2` CHECK ((`units_needed` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES (4,'nekjr',43,'B+',1,43,'2025-03-11 06:52:41','NO'),(6,'asif ali',34,'B-',7,3,'2025-03-12 06:05:50','NO'),(7,'swqws',19,'O+',1,12,'2025-03-12 05:57:28',NULL),(25,'NIrf bot',34,'AB-',7,6,'2025-03-10 14:45:54',NULL),(26,'NIrf bot',23,'AB-',3,2,'2025-03-10 15:00:03',NULL),(27,'NIrf bot',23,'AB-',3,2,'2025-03-10 15:01:49',NULL),(28,'NIrf bot',23,'AB-',3,2,'2025-03-10 15:04:00',NULL),(29,'hey',21,'B+',2,1,'2025-03-10 15:04:30',NULL),(30,'NIrf bot',34,'B-',4,2,'2025-03-10 15:11:33',NULL),(31,'hey',23,'A+',1,1,'2025-03-10 15:21:29',NULL),(32,'hey',23,'A+',2,1,'2025-03-10 15:25:53',NULL),(33,'hey',23,'A+',2,65,'2025-03-10 15:26:02',NULL),(34,'hey',23,'A+',2,12,'2025-03-10 15:26:20',NULL),(35,'text_manipulation_dataset',43,'A+',1,3,'2025-03-11 05:51:21',NULL),(36,'mitu',23,'B-',1,1,'2025-03-11 06:29:27',NULL);
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-20 22:06:23
