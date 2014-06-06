-- MySQL dump 10.13  Distrib 5.5.37, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: letusgo
-- ------------------------------------------------------
-- Server version	5.5.37-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `activity`
--

/* DROP TABLE IF EXISTS `activity`; */
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
/* CREATE TABLE `activity` ( */
/*   `aid` int(11) NOT NULL AUTO_INCREMENT, */
/*   `name` varchar(32) NOT NULL, */
/*   `uid` int(11) NOT NULL, */
/*   `intro` varchar(255) NOT NULL, */
/*   `launch_t` datetime NOT NULL, */
/*   `update_t` datetime NOT NULL, */
/*   `start_t` datetime NOT NULL, */
/*   `end_t` datetime NOT NULL, */
/*   `status` smallint(6) NOT NULL, */
/*   `limits` int(11) NOT NULL, */
/*   `participants` int(11) NOT NULL, */
/*   `voteups` int(11) NOT NULL, */
/*   `longitude` float NOT NULL, */
/*   `latitude` float NOT NULL, */
/*   `loc` varchar(255) NOT NULL, */
/*   `image` varchar(255) NOT NULL, */
/*   PRIMARY KEY (`aid`), */
/*   KEY `uid` (`uid`), */
/*   CONSTRAINT `activity_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) */
/* ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8; */
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activity`
--

/* LOCK TABLES `activity` WRITE; */
/*!40000 ALTER TABLE `activity` DISABLE KEYS */;
INSERT INTO `activity` VALUES (1,'hahaha',1,'我们一起去吃饭','2014-06-04 10:31:35','2014-06-04 10:37:50','2014-06-04 10:38:20','1974-06-30 20:16:40',2,10,0,0,22.5444,33.9,'武汉华中科技大学东九楼',''),(2,'test',1,'nihaoaaaaaaaaaaaaaaaaaaaa','2014-06-06 17:05:00','2014-06-06 17:05:00','2014-06-06 18:20:00','2014-06-06 21:06:40',0,5,0,0,22.3,44,'湖北武汉','');
/*!40000 ALTER TABLE `activity` ENABLE KEYS */;
/* UNLOCK TABLES; */

--
-- Table structure for table `participant`
--

/* DROP TABLE IF EXISTS `participant`; */
/* /*!40101 SET @saved_cs_client     = @@character_set_client *1/; */
/* /*!40101 SET character_set_client = utf8 *1/; */
/* CREATE TABLE `participant` ( */
/*   `aid` int(11) DEFAULT NULL, */
/*   `uid` int(11) DEFAULT NULL, */
/*   KEY `aid` (`aid`), */
/*   KEY `uid` (`uid`), */
/*   CONSTRAINT `participant_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `activity` (`aid`), */
/*   CONSTRAINT `participant_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) */
/* ) ENGINE=InnoDB DEFAULT CHARSET=utf8; */
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `participant`
--

/* LOCK TABLES `participant` WRITE; */
/*!40000 ALTER TABLE `participant` DISABLE KEYS */;
/*!40000 ALTER TABLE `participant` ENABLE KEYS */;
/* UNLOCK TABLES; */

--
-- Table structure for table `review`
--

/* DROP TABLE IF EXISTS `review`; */
/* /*!40101 SET @saved_cs_client     = @@character_set_client *1/; */
/* /*!40101 SET character_set_client = utf8 *1/; */
/* CREATE TABLE `review` ( */
/*   `rid` int(11) NOT NULL AUTO_INCREMENT, */
/*   `content` mediumtext NOT NULL, */
/*   `aid` int(11) NOT NULL, */
/*   `uid` int(11) NOT NULL, */
/*   `review_t` datetime NOT NULL, */
/*   PRIMARY KEY (`rid`), */
/*   KEY `aid` (`aid`), */
/*   KEY `uid` (`uid`), */
/*   CONSTRAINT `review_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `activity` (`aid`), */
/*   CONSTRAINT `review_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) */
/* ) ENGINE=InnoDB DEFAULT CHARSET=utf8; */
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

/* LOCK TABLES `review` WRITE; */
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
/* UNLOCK TABLES; */

--
-- Table structure for table `user`
--

/* DROP TABLE IF EXISTS `user`; */
/* /*!40101 SET @saved_cs_client     = @@character_set_client *1/; */
/* /*!40101 SET character_set_client = utf8 *1/; */
/* CREATE TABLE `user` ( */
/*   `uid` int(11) NOT NULL AUTO_INCREMENT, */
/*   `tel` varchar(11) NOT NULL, */
/*   `pwd` varchar(32) NOT NULL, */
/*   `name` varchar(32) NOT NULL, */
/*   `big_avatar` varchar(255) NOT NULL, */
/*   `small_avatar` varchar(255) NOT NULL, */
/*   `origin_avatar` varchar(255) NOT NULL, */
/*   `sex` smallint(6) NOT NULL, */
/*   `age` smallint(6) NOT NULL, */
/*   `loc` varchar(255) DEFAULT NULL, */
/*   `reg_time` datetime NOT NULL, */
/*   `last_login_t` datetime NOT NULL, */
/*   `token` varchar(16) NOT NULL, */
/*   PRIMARY KEY (`uid`), */
/*   UNIQUE KEY `tel` (`tel`) */
/* ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8; */
/* /*!40101 SET character_set_client = @saved_cs_client *1/; */

--
-- Dumping data for table `user`
--

/* LOCK TABLES `user` WRITE; */
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'13260614509','202cb962ac59075b964b07152d234b70','郭旗','/var/www/letusgo/letusgo/avatar/default/default64.png','/var/www/letusgo/letusgo/avatar/default/default32.png','/var/www/letusgo/letusgo/avatar/default/default.jpg',1,21,'湖北武汉','2014-06-04 10:22:32','2014-06-06 17:05:00','WSAxapxhjqHMjHU8');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
/* UNLOCK TABLES; */

--
-- Table structure for table `voteup`
--

/* DROP TABLE IF EXISTS `voteup`; */
/* /*!40101 SET @saved_cs_client     = @@character_set_client *1/; */
/* /*!40101 SET character_set_client = utf8 *1/; */
/* CREATE TABLE `voteup` ( */
/*   `aid` int(11) NOT NULL, */
/*   `uid` int(11) NOT NULL, */
/*   KEY `aid` (`aid`), */
/*   KEY `uid` (`uid`), */
/*   CONSTRAINT `voteup_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `activity` (`aid`), */
/*   CONSTRAINT `voteup_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) */
/* ) ENGINE=InnoDB DEFAULT CHARSET=utf8; */
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `voteup`
--

/* LOCK TABLES `voteup` WRITE; */
/*!40000 ALTER TABLE `voteup` DISABLE KEYS */;
/*!40000 ALTER TABLE `voteup` ENABLE KEYS */;
/* UNLOCK TABLES; */
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-06-06 21:36:09
