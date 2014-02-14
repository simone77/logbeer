-- MySQL dump 10.13  Distrib 5.5.35, for debian-linux-gnu (i686)
--

CREATE DATABASE `logger`;

USE `logger`;

--
-- Table structure for table `Logtemp`
--

DROP TABLE IF EXISTS `Logtemp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Logtemp` (
  `Data` datetime DEFAULT NULL,
  `Temp` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Settings`
--

DROP TABLE IF EXISTS `Settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Settings` (
  `ID` tinyint(4) NOT NULL,
  `Polling` smallint(6) DEFAULT NULL,
  `Correction` float DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Settings`
--

LOCK TABLES `Settings` WRITE;
/*!40000 ALTER TABLE `Settings` DISABLE KEYS */;
INSERT INTO `Settings` VALUES (0,20,-0.5);
