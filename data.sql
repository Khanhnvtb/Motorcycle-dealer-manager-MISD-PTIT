-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: motorcycle_manager
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add delivery_ invoice',7,'add_delivery_invoice'),(26,'Can change delivery_ invoice',7,'change_delivery_invoice'),(27,'Can delete delivery_ invoice',7,'delete_delivery_invoice'),(28,'Can view delivery_ invoice',7,'view_delivery_invoice'),(29,'Can add import_ invoice',8,'add_import_invoice'),(30,'Can change import_ invoice',8,'change_import_invoice'),(31,'Can delete import_ invoice',8,'delete_import_invoice'),(32,'Can view import_ invoice',8,'view_import_invoice'),(33,'Can add motor',9,'add_motor'),(34,'Can change motor',9,'change_motor'),(35,'Can delete motor',9,'delete_motor'),(36,'Can view motor',9,'view_motor'),(37,'Can add store',10,'add_store'),(38,'Can change store',10,'change_store'),(39,'Can delete store',10,'delete_store'),(40,'Can view store',10,'view_store'),(41,'Can add supplier',11,'add_supplier'),(42,'Can change supplier',11,'change_supplier'),(43,'Can delete supplier',11,'delete_supplier'),(44,'Can view supplier',11,'view_supplier'),(45,'Can add import_ motor',12,'add_import_motor'),(46,'Can change import_ motor',12,'change_import_motor'),(47,'Can delete import_ motor',12,'delete_import_motor'),(48,'Can view import_ motor',12,'view_import_motor'),(49,'Can add delivery_ motor',13,'add_delivery_motor'),(50,'Can change delivery_ motor',13,'change_delivery_motor'),(51,'Can delete delivery_ motor',13,'delete_delivery_motor'),(52,'Can view delivery_ motor',13,'view_delivery_motor');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_myapp_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_myapp_user_id` FOREIGN KEY (`user_id`) REFERENCES `myapp_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-04-15 11:45:44.236189','1','khanhnvtb',2,'[{\"changed\": {\"fields\": [\"Name\", \"Avatar\", \"Dob\", \"Gender\", \"Address\", \"Phone\", \"Role\"]}}]',6,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(7,'myapp','delivery_invoice'),(13,'myapp','delivery_motor'),(8,'myapp','import_invoice'),(12,'myapp','import_motor'),(9,'myapp','motor'),(10,'myapp','store'),(11,'myapp','supplier'),(6,'myapp','user'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-04-15 11:43:36.071923'),(2,'contenttypes','0002_remove_content_type_name','2023-04-15 11:43:36.101669'),(3,'auth','0001_initial','2023-04-15 11:43:36.238580'),(4,'auth','0002_alter_permission_name_max_length','2023-04-15 11:43:36.275646'),(5,'auth','0003_alter_user_email_max_length','2023-04-15 11:43:36.281536'),(6,'auth','0004_alter_user_username_opts','2023-04-15 11:43:36.287383'),(7,'auth','0005_alter_user_last_login_null','2023-04-15 11:43:36.293108'),(8,'auth','0006_require_contenttypes_0002','2023-04-15 11:43:36.295727'),(9,'auth','0007_alter_validators_add_error_messages','2023-04-15 11:43:36.301749'),(10,'auth','0008_alter_user_username_max_length','2023-04-15 11:43:36.307922'),(11,'auth','0009_alter_user_last_name_max_length','2023-04-15 11:43:36.313060'),(12,'auth','0010_alter_group_name_max_length','2023-04-15 11:43:36.325426'),(13,'auth','0011_update_proxy_permissions','2023-04-15 11:43:36.332905'),(14,'auth','0012_alter_user_first_name_max_length','2023-04-15 11:43:36.337940'),(15,'myapp','0001_initial','2023-04-15 11:43:36.957768'),(16,'admin','0001_initial','2023-04-15 11:43:37.036605'),(17,'admin','0002_logentry_remove_auto_add','2023-04-15 11:43:37.045998'),(18,'admin','0003_logentry_add_action_flag_choices','2023-04-15 11:43:37.053471'),(19,'myapp','0002_remove_user_dob_alter_delivery_invoice_time_and_more','2023-04-15 11:43:37.087864'),(20,'myapp','0003_user_dob_alter_delivery_invoice_time_and_more','2023-04-15 11:43:37.120006'),(21,'myapp','0004_alter_delivery_invoice_time_and_more','2023-04-15 11:43:37.132327'),(22,'myapp','0005_alter_delivery_invoice_time_and_more','2023-04-15 11:43:37.145721'),(23,'myapp','0006_alter_delivery_invoice_time_and_more','2023-04-15 11:43:37.157727'),(24,'myapp','0007_alter_delivery_invoice_time_and_more','2023-04-15 11:43:37.174089'),(25,'myapp','0008_alter_delivery_invoice_time_and_more','2023-04-15 11:43:37.193120'),(26,'myapp','0009_rename_employee_id_delivery_invoice_employee_and_more','2023-04-15 11:43:37.621344'),(27,'myapp','0010_remove_employee_employee_id_employee_employee_and_more','2023-04-15 11:43:37.721477'),(28,'myapp','0011_alter_delivery_invoice_time_and_more','2023-04-15 11:43:37.734309'),(29,'myapp','0012_alter_delivery_invoice_time_and_more','2023-04-15 11:43:37.745329'),(30,'myapp','0013_alter_delivery_invoice_time_and_more','2023-04-15 11:43:37.757290'),(31,'myapp','0014_alter_delivery_invoice_time_and_more','2023-04-15 11:43:37.780524'),(32,'myapp','0015_remove_employee_employee_employee_user_id_and_more','2023-04-15 11:43:37.875021'),(33,'myapp','0016_user_salary_alter_delivery_invoice_employee_and_more','2023-04-15 11:43:38.077710'),(34,'sessions','0001_initial','2023-04-15 11:43:38.100409'),(35,'myapp','0017_alter_delivery_invoice_time_and_more','2023-04-16 02:33:02.427767'),(36,'myapp','0018_alter_delivery_invoice_time_and_more','2023-04-16 09:31:21.531975'),(37,'myapp','0019_alter_delivery_invoice_time_and_more','2023-04-16 14:34:17.458510');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('34z2b28fx7b85s5lk9suo8pzwbecsago','.eJxVjDsOwjAQBe_iGlmsvwklPWew1t41DiBbipMKcXcSKQW0M_PeWwRclxLWznOYSFwEiNMvi5ieXHdBD6z3JlOryzxFuSfysF3eGvHrerR_BwV72daesh0HzxjREWhtcDA-gSZrNhSVA8OZtMvIFs6KlMkADpInM0absvh8AfQ2OFQ:1po1ob:LWvICOvhC9mhdl0JgeN_XNdso5ZiNzCy5nWIRTU5fhw','2023-04-30 12:49:09.380641'),('54qw71fwa6e1rxg8hscwemu5wxgsg97x','.eJxVjMEOwiAQRP-FsyGBLt3i0bvfQIDdlaqhSWlPjf9um_Sgt8m8N7OpENelhLXxHEZSV2XU5bdLMb-4HoCesT4mnae6zGPSh6JP2vR9In7fTvfvoMRW9jWieCEPA1mRNABYJ1HEZBTHZLhHyyCdM6nzgL43mcVms0cEJO_V5wv8tzgM:1pnr6m:EDIIfNPJAhiR-KI7H4jxp4WAaggmbsUgKUUsUO1uqrc','2023-04-30 01:23:12.069484'),('xhg15qiyx6evro68qaxe1rwsjwnttyzy','.eJxVjEEOgjAURO_StWn6qZTi0j1naKa_vxY1kFBYGe-uJCx0O--9eamAbS1hq7KEMamLInX63SL4IdMO0h3TbdY8T-syRr0r-qBVD3OS5_Vw_w4KavnWncDG3sOJyWdnXdcyPMNZJiGAKDfeGkLfSvZkesrsLQRNm1MSk9T7A-6IOII:1ppLYK:SSOqj792iO6hmaTnqQAQTT1dnTS4JW-UZITX_4b24Og','2023-05-04 04:05:48.276934');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_delivery_invoice`
--

DROP TABLE IF EXISTS `myapp_delivery_invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_delivery_invoice` (
  `invoice_id` int NOT NULL AUTO_INCREMENT,
  `time` datetime(6) NOT NULL,
  `total` bigint NOT NULL,
  `employee_id` bigint NOT NULL,
  `store_id` int NOT NULL,
  PRIMARY KEY (`invoice_id`),
  KEY `myapp_delivery_invoice_store_id_bd55c319_fk_myapp_store_store_id` (`store_id`),
  KEY `myapp_delivery_invoice_employee_id_f7535221_fk_myapp_user_id` (`employee_id`),
  CONSTRAINT `myapp_delivery_invoice_employee_id_f7535221_fk_myapp_user_id` FOREIGN KEY (`employee_id`) REFERENCES `myapp_user` (`id`),
  CONSTRAINT `myapp_delivery_invoice_store_id_bd55c319_fk_myapp_store_store_id` FOREIGN KEY (`store_id`) REFERENCES `myapp_store` (`store_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_delivery_invoice`
--

LOCK TABLES `myapp_delivery_invoice` WRITE;
/*!40000 ALTER TABLE `myapp_delivery_invoice` DISABLE KEYS */;
INSERT INTO `myapp_delivery_invoice` VALUES (3,'2023-04-17 15:30:09.658998',220000000,1,5),(4,'2023-04-17 15:30:09.658998',88000000,1,5),(5,'2023-04-17 15:30:10.658998',44000000,1,5),(6,'2023-03-17 15:30:09.658998',44000000,2,5),(7,'2023-04-20 11:03:11.507057',272490000,1,5);
/*!40000 ALTER TABLE `myapp_delivery_invoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_delivery_motor`
--

DROP TABLE IF EXISTS `myapp_delivery_motor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_delivery_motor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `invoice_id` int NOT NULL,
  `motor_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_delivery_motor_invoice_id_f98311c2_fk_myapp_del` (`invoice_id`),
  KEY `myapp_delivery_motor_motor_id_f7459b65_fk_myapp_motor_motor_id` (`motor_id`),
  CONSTRAINT `myapp_delivery_motor_invoice_id_f98311c2_fk_myapp_del` FOREIGN KEY (`invoice_id`) REFERENCES `myapp_delivery_invoice` (`invoice_id`),
  CONSTRAINT `myapp_delivery_motor_motor_id_f7459b65_fk_myapp_motor_motor_id` FOREIGN KEY (`motor_id`) REFERENCES `myapp_motor` (`motor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_delivery_motor`
--

LOCK TABLES `myapp_delivery_motor` WRITE;
/*!40000 ALTER TABLE `myapp_delivery_motor` DISABLE KEYS */;
INSERT INTO `myapp_delivery_motor` VALUES (3,5,3,117),(4,2,4,120),(5,1,5,119),(6,1,6,119),(7,5,7,119),(8,1,7,135);
/*!40000 ALTER TABLE `myapp_delivery_motor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_import_invoice`
--

DROP TABLE IF EXISTS `myapp_import_invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_import_invoice` (
  `invoice_id` int NOT NULL AUTO_INCREMENT,
  `time` datetime(6) NOT NULL,
  `total` bigint NOT NULL,
  `employee_id` bigint NOT NULL,
  `supplier_id` int NOT NULL,
  PRIMARY KEY (`invoice_id`),
  KEY `myapp_import_invoice_supplier_id_c3ab866d_fk_myapp_sup` (`supplier_id`),
  KEY `myapp_import_invoice_employee_id_9a36e4ad_fk_myapp_user_id` (`employee_id`),
  CONSTRAINT `myapp_import_invoice_employee_id_9a36e4ad_fk_myapp_user_id` FOREIGN KEY (`employee_id`) REFERENCES `myapp_user` (`id`),
  CONSTRAINT `myapp_import_invoice_supplier_id_c3ab866d_fk_myapp_sup` FOREIGN KEY (`supplier_id`) REFERENCES `myapp_supplier` (`supplier_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_import_invoice`
--

LOCK TABLES `myapp_import_invoice` WRITE;
/*!40000 ALTER TABLE `myapp_import_invoice` DISABLE KEYS */;
INSERT INTO `myapp_import_invoice` VALUES (32,'2023-04-17 15:30:09.658000',362500000,1,4),(33,'2023-04-17 15:30:09.658000',181250000,1,4),(34,'2023-04-17 15:30:09.658000',72500000,1,4),(35,'2023-04-17 15:30:09.658000',362500000,1,4),(36,'2023-04-17 15:30:09.658000',181250000,1,4),(37,'2023-04-17 15:30:09.658000',72500000,1,4),(40,'2023-04-20 11:00:42.280736',545500000,1,6);
/*!40000 ALTER TABLE `myapp_import_invoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_import_motor`
--

DROP TABLE IF EXISTS `myapp_import_motor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_import_motor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `invoice_id` int NOT NULL,
  `motor_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_import_motor_invoice_id_fc7f8615_fk_myapp_imp` (`invoice_id`),
  KEY `myapp_import_motor_motor_id_13bab802_fk_myapp_motor_motor_id` (`motor_id`),
  CONSTRAINT `myapp_import_motor_invoice_id_fc7f8615_fk_myapp_imp` FOREIGN KEY (`invoice_id`) REFERENCES `myapp_import_invoice` (`invoice_id`),
  CONSTRAINT `myapp_import_motor_motor_id_13bab802_fk_myapp_motor_motor_id` FOREIGN KEY (`motor_id`) REFERENCES `myapp_motor` (`motor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_import_motor`
--

LOCK TABLES `myapp_import_motor` WRITE;
/*!40000 ALTER TABLE `myapp_import_motor` DISABLE KEYS */;
INSERT INTO `myapp_import_motor` VALUES (32,10,32,117),(33,5,33,120),(34,2,34,119),(35,10,35,117),(36,5,36,120),(37,2,37,119),(40,10,40,119),(41,4,40,135);
/*!40000 ALTER TABLE `myapp_import_motor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_motor`
--

DROP TABLE IF EXISTS `myapp_motor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_motor` (
  `motor_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `assurance` varchar(200) NOT NULL,
  `quantity` int NOT NULL,
  `import_price` int NOT NULL,
  `export_price` int NOT NULL,
  PRIMARY KEY (`motor_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=229 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_motor`
--

LOCK TABLES `myapp_motor` WRITE;
/*!40000 ALTER TABLE `myapp_motor` DISABLE KEYS */;
INSERT INTO `myapp_motor` VALUES (117,'Vario 125 đỏ','Honda','motor_image/motor1.jpg',' Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 124,8cc cho công suất 11,1 mã lực và momen xoắn 10,8Nm','Bảo dưỡng \n3/6/9 tháng',115,36250000,44000000),(118,'Vario 125 trắng','Honda','motor_image/motor2.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 124,8cc cho công suất 11,1 mã lực và momen xoắn 10,8Nm','Bảo dưỡng \n3/6/9 tháng',105,36250000,44000000),(119,'Vario 125 mâm vàng','Honda','motor_image/motor3.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 124,8cc cho công suất 11,1 mã lực và momen xoắn 10,8Nm','Bảo dưỡng \n3/6/9 tháng',108,36250000,44000000),(120,'Vario 1225 xanh nhám','Honda','motor_image/motor4.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 124,8cc cho công suất 11,1 mã lực và momen xoắn 10,8Nm','Bảo dưỡng \n3/6/9 tháng',108,36250000,44000000),(121,'Vario 125 vàng cát','Honda','motor_image/motor5.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 124,8cc cho công suất 11,1 mã lực và momen xoắn 10,8Nm','Bảo dưỡng \n3/6/9 tháng',100,36250000,44000000),(122,'Vario 125 hồng','Honda','motor_image/motor6.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 124,8cc cho công suất 11,1 mã lực và momen xoắn 10,8Nm','Bảo dưỡng \n3/6/9 tháng',100,36250000,44000000),(123,'Vario 125 xanh đen','Honda','motor_image/motor7.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 124,8cc cho công suất 11,1 mã lực và momen xoắn 10,8Nm','Bảo dưỡng \n3/6/9 tháng',100,36250000,44000000),(124,'Vario 125 đen nhám','Honda','motor_image/motor8.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 124,8cc cho công suất 11,1 mã lực và momen xoắn 10,8Nm','Bảo dưỡng \n3/6/9 tháng',100,36250000,44000000),(125,'Vario 125 trắng - đỏ','Honda','motor_image/motor9.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 124,8cc cho công suất 11,1 mã lực và momen xoắn 10,8Nm','Bảo dưỡng \n3/6/9 tháng',100,36250000,44000000),(126,'Vario 125 đỏ đen','Honda','motor_image/motor10.png','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 124,8cc cho công suất 11,1 mã lực và momen xoắn 10,8Nm','Bảo dưỡng \n3/6/9 tháng',100,36250000,44000000),(127,'Vario 150 bạc nhám','Honda','motor_image/motor11.jpg',' Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 149,3cc cho công suất 13,1 mã lực và momen xoắn 13,4Nm','Bảo dưỡng \n3/6/9 tháng',100,36250000,44000000),(128,'Vario 150 trắng tem đỏ','Honda','motor_image/motor12.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 149,3cc cho công suất 13,1 mã lực và momen xoắn 13,4Nm','Bảo dưỡng \n3/6/9 tháng',100,49250000,56500000),(129,'Vario 150 xanh ngọc','Honda','motor_image/motor13.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 149,3cc cho công suất 13,1 mã lực và momen xoắn 13,4Nm','Bảo dưỡng \n3/6/9 tháng',100,56250000,64000000),(130,'Vario 150 xanh nhám','Honda','motor_image/motor14.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 149,3cc cho công suất 13,1 mã lực và momen xoắn 13,4Nm','Bảo dưỡng \n3/6/9 tháng',100,54250000,62000000),(131,'Vario 150 đen mâm đồng','Honda','motor_image/motor15.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 149,3cc cho công suất 13,1 mã lực và momen xoắn 13,4Nm','Bảo dưỡng \n3/6/9 tháng',100,50250000,58200000),(132,'Vario 150 vàng cát','Honda','motor_image/motor16.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 149,3cc cho công suất 13,1 mã lực và momen xoắn 13,4Nm','Bảo dưỡng \n3/6/9 tháng',100,49250000,56000000),(133,'Vario 150 đỏ nhám','Honda','motor_image/motor18.jpg','Chiều dài x rộng x cao lần lượt là 1919mm x 679 mm x 1062mm, khoảng sáng gần 132 mm và chiều cao yên là 769mm.  Dung tích 149,3cc cho công suất 13,1 mã lực và momen xoắn 13,4Nm','Bảo dưỡng \n3/6/9 tháng',100,48250000,55500000),(134,'Vario 160 CBS tiêu chuẩn','Honda','motor_image/motor19.png','Chiều dài x rộng x cao của ABS là 1929 x 679 x 1088mm. Của CBS là 1929 x 695 x 1088mm, khoảng sáng gầm 138mm và chiều cao yên là 778mm. Dung tích 156,93cc','Bảo dưỡng \n3/6/9 tháng',100,45750000,51900000),(135,'Vario 160 CBS cao cấp','Honda','motor_image/motor20.png','Chiều dài x rộng x cao của ABS là 1929 x 679 x 1088mm. Của CBS là 1929 x 695 x 1088mm, khoảng sáng gầm 138mm và chiều cao yên là 778mm. Dung tích 156,93cc','Bảo dưỡng \n3/6/9 tháng',103,45750000,52490000),(136,'Vario 160 ABS đặc biệt','Honda','motor_image/motor21.jpg','Chiều dài x rộng x cao của ABS là 1929 x 679 x 1088mm. Của CBS là 1929 x 695 x 1088mm, khoảng sáng gầm 138mm và chiều cao yên là 778mm. Dung tích 156,93cc','Bảo dưỡng \n3/6/9 tháng',100,47250000,55900000),(137,'Vario 160 ABS thể thao','Honda','motor_image/motor22.jpg','Chiều dài x rộng x cao của ABS là 1929 x 679 x 1088mm. Của CBS là 1929 x 695 x 1088mm, khoảng sáng gầm 138mm và chiều cao yên là 778mm. Dung tích 156,93cc','Bảo dưỡng \n3/6/9 tháng',100,49250000,56490000),(138,'LEAD Tiêu chuẩn','Honda','motor_image/motor23.jpg','Chiều dài x rộng x cao là 1844 x 680 x 1130mm. Khoảng cách trục bánh xe là 1273mm, khoảng sáng gầm là 120mm, độ cao yên là 120mm. Dung tích 124,8cc','Bảo dưỡng \n3/6/9 tháng',100,39250000,46370000),(139,'LEAD Cao cấp','Honda','motor_image/motor24.jpg','Chiều dài x rộng x cao là 1844 x 680 x 1130mm. Khoảng cách trục bánh xe là 1273mm, khoảng sáng gầm là 120mm, độ cao yên là 120mm. Dung tích 124,8cc','Bảo dưỡng \n3/6/9 tháng',100,41250000,48680000),(140,'LEAD Đặc biệt','Honda','motor_image/motor25.jpg','Chiều dài x rộng x cao là 1844 x 680 x 1130mm. Khoảng cách trục bánh xe là 1273mm, khoảng sáng gầm là 120mm, độ cao yên là 120mm. Dung tích 124,8cc','Bảo dưỡng \n3/6/9 tháng',100,40250000,49835000),(141,'Vision bàn tiêu chuẩn','Honda','motor_image/motor26.jpg','Chiều dài x rộng x cao là 1871 x 686 x 1101mm. Khoảng cách trục bánh xe là 1255mm. Độ cao yên là 761mm, khoảng sáng gầm xe là 120mm. Dung tích 109,5cm3. Momen cực đại là 9,29Nm/6.000rpm. Loại đông cơ 4 kỳ, 1 xi lanh, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,26250000,33500000),(142,'Vision bàn tiêu chuẩn đen','Honda','motor_image/motor27.png','Chiều dài x rộng x cao là 1871 x 686 x 1101mm. Khoảng cách trục bánh xe là 1255mm. Độ cao yên là 761mm, khoảng sáng gầm xe là 120mm. Dung tích 109,5cm3. Momen cực đại là 9,29Nm/6.000rpm. Loại đông cơ 4 kỳ, 1 xi lanh, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,26250000,33500000),(143,'Vision cao cấp xanh yên nâu','Honda','motor_image/motor28.jpg','Chiều dài x rộng x cao là 1871 x 686 x 1101mm. Khoảng cách trục bánh xe là 1255mm. Độ cao yên là 761mm, khoảng sáng gầm xe là 120mm. Dung tích 109,5cm3. Momen cực đại là 9,29Nm/6.000rpm. Loại đông cơ 4 kỳ, 1 xi lanh, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,26250000,35800000),(144,'Vision cao cấp đỏ - trắng','Honda','motor_image/motor29.jpg','Chiều dài x rộng x cao là 1871 x 686 x 1101mm. Khoảng cách trục bánh xe là 1255mm. Độ cao yên là 761mm, khoảng sáng gầm xe là 120mm. Dung tích 109,5cm3. Momen cực đại là 9,29Nm/6.000rpm. Loại đông cơ 4 kỳ, 1 xi lanh, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,29250000,36000000),(145,'Vision đặc biệt xanh','Honda','motor_image/motor30.jpg','Chiều dài x rộng x cao là 1871 x 686 x 1101mm. Khoảng cách trục bánh xe là 1255mm. Độ cao yên là 761mm, khoảng sáng gầm xe là 120mm. Dung tích 109,5cm3. Momen cực đại là 9,29Nm/6.000rpm. Loại đông cơ 4 kỳ, 1 xi lanh, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,29250000,36500000),(146,'Vision thể thao xanh','Honda','motor_image/motor31.jpg','Chiều dài x rộng x cao là 1871 x 686 x 1101mm. Khoảng cách trục bánh xe là 1255mm. Độ cao yên là 761mm, khoảng sáng gầm xe là 120mm. Dung tích 109,5cm3. Momen cực đại là 9,29Nm/6.000rpm. Loại đông cơ 4 kỳ, 1 xi lanh, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,31250000,39500000),(147,'Vision thể thao đen nhám','Honda','motor_image/motor32.jpg','Chiều dài x rộng x cao là 1871 x 686 x 1101mm. Khoảng cách trục bánh xe là 1255mm. Độ cao yên là 761mm, khoảng sáng gầm xe là 120mm. Dung tích 109,5cm3. Momen cực đại là 9,29Nm/6.000rpm. Loại đông cơ 4 kỳ, 1 xi lanh, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,31250000,39000000),(148,'Air Blade 2007-2008','Honda','motor_image/motor33.jpg',' - Air Blade 125: Chiều dài x rộng x cao là 1887 x 687 x 1092mm, khoảng sáng gầm xe là 141mm. Dung tích 124,8cc - Air Blade 160: Chiều dài x rộng x cao là 1890 x 686 x 1116mm, khoảng sáng gầm xe là 142mm. Dung tích 156,9cc\n','Bảo dưỡng \n3/6/9 tháng',100,9250000,15800000),(149,'Air Blade 2009','Honda','motor_image/motor34.jpg','- Air Blade 125: Chiều dài x rộng x cao là 1887 x 687 x 1092mm, khoảng sáng gầm xe là 141mm. Dung tích 124,8cc - Air Blade 160: Chiều dài x rộng x cao là 1890 x 686 x 1116mm, khoảng sáng gầm xe là 142mm. Dung tích 156,9cc','Bảo dưỡng \n3/6/9 tháng',100,9750000,16500000),(150,'Air Blade 2010-2011','Honda','motor_image/motor35.jpg','- Air Blade 125: Chiều dài x rộng x cao là 1887 x 687 x 1092mm, khoảng sáng gầm xe là 141mm. Dung tích 124,8cc - Air Blade 160: Chiều dài x rộng x cao là 1890 x 686 x 1116mm, khoảng sáng gầm xe là 142mm. Dung tích 156,9cc','Bảo dưỡng \n3/6/9 tháng',100,11250000,17500000),(151,'Air Blade 2012','Honda','motor_image/motor36.jpg','- Air Blade 125: Chiều dài x rộng x cao là 1887 x 687 x 1092mm, khoảng sáng gầm xe là 141mm. Dung tích 124,8cc - Air Blade 160: Chiều dài x rộng x cao là 1890 x 686 x 1116mm, khoảng sáng gầm xe là 142mm. Dung tích 156,9cc','Bảo dưỡng \n3/6/9 tháng',100,11750000,17500000),(152,'Air Blade 2013','Honda','motor_image/motor37.jpg','- Air Blade 125: Chiều dài x rộng x cao là 1887 x 687 x 1092mm, khoảng sáng gầm xe là 141mm. Dung tích 124,8cc - Air Blade 160: Chiều dài x rộng x cao là 1890 x 686 x 1116mm, khoảng sáng gầm xe là 142mm. Dung tích 156,9cc','Bảo dưỡng \n3/6/9 tháng',100,12250000,18600000),(153,'Air Blade 2016','Honda','motor_image/motor38.jpg','- Air Blade 125: Chiều dài x rộng x cao là 1887 x 687 x 1092mm, khoảng sáng gầm xe là 141mm. Dung tích 124,8cc - Air Blade 160: Chiều dài x rộng x cao là 1890 x 686 x 1116mm, khoảng sáng gầm xe là 142mm. Dung tích 156,9cc','Bảo dưỡng \n3/6/9 tháng',100,19250000,26000000),(154,'Air Blade 2017','Honda','motor_image/motor39.jpg','- Air Blade 125: Chiều dài x rộng x cao là 1887 x 687 x 1092mm, khoảng sáng gầm xe là 141mm. Dung tích 124,8cc - Air Blade 160: Chiều dài x rộng x cao là 1890 x 686 x 1116mm, khoảng sáng gầm xe là 142mm. Dung tích 156,9cc','Bảo dưỡng \n3/6/9 tháng',100,24250000,31000000),(155,'Air Blade 2020','Honda','motor_image/motor40.jpg','- Air Blade 125: Chiều dài x rộng x cao là 1887 x 687 x 1092mm, khoảng sáng gầm xe là 141mm. Dung tích 124,8cc - Air Blade 160: Chiều dài x rộng x cao là 1890 x 686 x 1116mm, khoảng sáng gầm xe là 142mm. Dung tích 156,9cc','Bảo dưỡng \n3/6/9 tháng',100,25250000,32000000),(156,'Air Blade 2022','Honda','motor_image/motor41.jpg','- Air Blade 125: Chiều dài x rộng x cao là 1887 x 687 x 1092mm, khoảng sáng gầm xe là 141mm. Dung tích 124,8cc - Air Blade 160: Chiều dài x rộng x cao là 1890 x 686 x 1116mm, khoảng sáng gầm xe là 142mm. Dung tích 156,9cc','Bảo dưỡng \n3/6/9 tháng',100,29250000,37000000),(157,'Air Blade 150','Honda','motor_image/motor42.jpg','- Air Blade 125: Chiều dài x rộng x cao là 1887 x 687 x 1092mm, khoảng sáng gầm xe là 141mm. Dung tích 124,8cc - Air Blade 160: Chiều dài x rộng x cao là 1890 x 686 x 1116mm, khoảng sáng gầm xe là 142mm. Dung tích 156,9cc','Bảo dưỡng \n3/6/9 tháng',100,29250000,37500000),(158,'SH150i tiêu chuẩn CBS trắng','Honda','motor_image/motor43.png','Chiều dài x rộng x cao là 2026 x 740 x 1158mm. Khoảng cách trục bánh xe là 1340mm. Độ cao yên là 340mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xylanh, làm mát bằng dung dịch. Dung tích xylanh là 153 cm3','Bảo dưỡng \n3/6/9 tháng',100,81250000,88790000),(159,'SH150i tiêu chuẩn CBS đỏ','Honda','motor_image/motor44.jpg','Chiều dài x rộng x cao là 2026 x 740 x 1158mm. Khoảng cách trục bánh xe là 1340mm. Độ cao yên là 340mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xylanh, làm mát bằng dung dịch. Dung tích xylanh là 153 cm3','Bảo dưỡng \n3/6/9 tháng',100,81250000,88790000),(160,'SH150i tiêu chuẩn CBS đen','Honda','motor_image/motor45.png','Chiều dài x rộng x cao là 2026 x 740 x 1158mm. Khoảng cách trục bánh xe là 1340mm. Độ cao yên là 340mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xylanh, làm mát bằng dung dịch. Dung tích xylanh là 153 cm3','Bảo dưỡng \n3/6/9 tháng',100,81250000,88790000),(161,'SH150i thể thao ABS xám','Honda','motor_image/motor46.png','Chiều dài x rộng x cao là 2026 x 740 x 1158mm. Khoảng cách trục bánh xe là 1340mm. Độ cao yên là 340mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xylanh, làm mát bằng dung dịch. Dung tích xylanh là 153 cm3','Bảo dưỡng \n3/6/9 tháng',100,91750000,98490000),(162,'SH150i đặc biệt ABS đen','Honda','motor_image/motor47.png','Chiều dài x rộng x cao là 2026 x 740 x 1158mm. Khoảng cách trục bánh xe là 1340mm. Độ cao yên là 340mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xylanh, làm mát bằng dung dịch. Dung tích xylanh là 153 cm3','Bảo dưỡng \n3/6/9 tháng',100,91750000,97990000),(163,'SH150i đặc biệt ABS bạc','Honda','motor_image/motor48.png','Chiều dài x rộng x cao là 2026 x 740 x 1158mm. Khoảng cách trục bánh xe là 1340mm. Độ cao yên là 340mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xylanh, làm mát bằng dung dịch. Dung tích xylanh là 153 cm3','Bảo dưỡng \n3/6/9 tháng',100,91750000,97990000),(164,'SH150i cao cấp ABS trắng','Honda','motor_image/motor49.png','Chiều dài x rộng x cao là 2026 x 740 x 1158mm. Khoảng cách trục bánh xe là 1340mm. Độ cao yên là 340mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xylanh, làm mát bằng dung dịch. Dung tích xylanh là 153 cm3','Bảo dưỡng \n3/6/9 tháng',100,91750000,96790000),(165,'SH150i cao cấp ABS đen','Honda','motor_image/motor50.jpeg','Chiều dài x rộng x cao là 2026 x 740 x 1158mm. Khoảng cách trục bánh xe là 1340mm. Độ cao yên là 340mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xylanh, làm mát bằng dung dịch. Dung tích xylanh là 153 cm3','Bảo dưỡng \n3/6/9 tháng',100,89250000,96790000),(166,'SH150i cao cấp ABS đỏ','Honda','motor_image/motor51.png','Chiều dài x rộng x cao là 2026 x 740 x 1158mm. Khoảng cách trục bánh xe là 1340mm. Độ cao yên là 340mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xylanh, làm mát bằng dung dịch. Dung tích xylanh là 153 cm3','Bảo dưỡng \n3/6/9 tháng',100,89250000,96790000),(167,'SH125i tiêu chuẩn CBS trắng','Honda','motor_image/motor52.png','Chiều dài x rộng x cao là 2090 x 739 x 1129mm. Độ cao yên là 799mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xy lanh, làm mát bằng dung dịch. Dung tích xylanh  124,8cm3','Bảo dưỡng \n3/6/9 tháng',100,65150000,71790000),(168,'SH125i tiêu chuẩn CBS đỏ','Honda','motor_image/motor53.png','Chiều dài x rộng x cao là 2090 x 739 x 1129mm. Độ cao yên là 799mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xy lanh, làm mát bằng dung dịch. Dung tích xylanh  124,8cm3','Bảo dưỡng \n3/6/9 tháng',100,65150000,71790000),(169,'SH125i tiêu chuẩn CBS đen','Honda','motor_image/motor54.png','Chiều dài x rộng x cao là 2090 x 739 x 1129mm. Độ cao yên là 799mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xy lanh, làm mát bằng dung dịch. Dung tích xylanh  124,8cm3','Bảo dưỡng \n3/6/9 tháng',100,65150000,71790000),(170,'SH125i cao cấp ABS trắng','Honda','motor_image/motor55.png','Chiều dài x rộng x cao là 2090 x 739 x 1129mm. Độ cao yên là 799mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xy lanh, làm mát bằng dung dịch. Dung tích xylanh  124,8cm3','Bảo dưỡng \n3/6/9 tháng',100,71250000,79790000),(171,'SH125i cao cấp ABS đỏ','Honda','motor_image/motor56.png','Chiều dài x rộng x cao là 2090 x 739 x 1129mm. Độ cao yên là 799mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xy lanh, làm mát bằng dung dịch. Dung tích xylanh  124,8cm3','Bảo dưỡng \n3/6/9 tháng',100,71250000,79790000),(172,'Sh125i cao cấp ABS đen','Honda','motor_image/motor57.png','Chiều dài x rộng x cao là 2090 x 739 x 1129mm. Độ cao yên là 799mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xy lanh, làm mát bằng dung dịch. Dung tích xylanh  124,8cm3','Bảo dưỡng \n3/6/9 tháng',100,71250000,79790000),(173,'SH350i thể thao xám','Honda','motor_image/motor58.jpg','Chiều dài x rộng x cao là 2090 x 739 x 1129mm. Độ cao yên là 799mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xy lanh, làm mát bằng dung dịch. Dung tích xylanh  156,9cm3','Bảo dưỡng \n3/6/9 tháng',100,39250000,147490000),(174,'SH350i thể thao đen','Honda','motor_image/motor59.png','Chiều dài x rộng x cao là 2090 x 739 x 1129mm. Độ cao yên là 799mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xy lanh, làm mát bằng dung dịch. Dung tích xylanh  156,9cm3','Bảo dưỡng \n3/6/9 tháng',100,132000000,147490000),(175,'SH350i đặc biệt đen','Honda','motor_image/motor60.jpg','Chiều dài x rộng x cao là 2090 x 739 x 1129mm. Độ cao yên là 799mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xy lanh, làm mát bằng dung dịch. Dung tích xylanh  156,9cm3','Bảo dưỡng \n3/6/9 tháng',100,133000000,146990000),(176,'Sh350i cao cấp đỏ','Honda','motor_image/motor61.jpg','Chiều dài x rộng x cao là 2090 x 739 x 1129mm. Độ cao yên là 799mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xy lanh, làm mát bằng dung dịch. Dung tích xylanh  156,9cm3','Bảo dưỡng \n3/6/9 tháng',100,142500000,145990000),(177,'SH350i cao cấp trắng','Honda','motor_image/motor62.jpg','Chiều dài x rộng x cao là 2090 x 739 x 1129mm. Độ cao yên là 799mm, khoảng sáng gầm xe 146mm. Loại động cơ PGM-FI, xăng 4 kỳ, 1 xy lanh, làm mát bằng dung dịch. Dung tích xylanh  156,9cm3','Bảo dưỡng \n3/6/9 tháng',100,122500000,145990000),(178,'Wave Alpha 2023 đặc biệt','Honda','motor_image/motor63.jpg','Chiều dài x rộng x cao là 1914 x 688 x 1075mm. Khoảng cách trục bánh xe là 1224mm, độ cao yên là 769mm, khoảng sáng gầm xe là 138mm. Loại động cơ xăng, 4 kỳ, 1 xylanh làm mất bằng không khí. Dung tích xylanh là 109,1cm3','Bảo dưỡng \n3/6/9 tháng',100,11250000,18790000),(179,'Wave Alpha 2023 tiêu chuẩn','Honda','motor_image/motor64.png','Chiều dài x rộng x cao là 1914 x 688 x 1075mm. Khoảng cách trục bánh xe là 1224mm, độ cao yên là 769mm, khoảng sáng gầm xe là 138mm. Loại động cơ xăng, 4 kỳ, 1 xylanh làm mất bằng không khí. Dung tích xylanh là 109,1cm3','Bảo dưỡng \n3/6/9 tháng',100,11250000,18190000),(180,'Wave Alpha 110cc','Honda','motor_image/motor65.jpg','Chiều dài x rộng x cao là 1914 x 688 x 1075mm. Khoảng cách trục bánh xe là 1224mm, độ cao yên là 769mm, khoảng sáng gầm xe là 138mm. Loại động cơ xăng, 4 kỳ, 1 xylanh làm mất bằng không khí. Dung tích xylanh là 109,1cm3','Bảo dưỡng \n3/6/9 tháng',100,12550000,19600000),(181,'Wave Alpha 100cc','Honda','motor_image/motor66.jpg','Chiều dài x rộng x cao là 1914 x 688 x 1075mm. Khoảng cách trục bánh xe là 1224mm, độ cao yên là 769mm, khoảng sáng gầm xe là 138mm. Loại động cơ xăng, 4 kỳ, 1 xylanh làm mất bằng không khí. Dung tích xylanh là 109,1cm3','Bảo dưỡng \n3/6/9 tháng',100,11250000,18000000),(182,'Winner X đen vàng','Honda','motor_image/motor67.jpg','Chiều dai x rộng x cao là 2019 x 727 x 1104mm. Khoảng cách trục bánh xe là 1278mm, độ cao yên là 795mm, khoảng sáng gầm xe là 151mm. Loại động cơ PGM-FI, DOHC, xylanh đơn, côn 6 số, làm mát bằng dung dịch. Dung tích 149,1cm3','Bảo dưỡng \n3/6/9 tháng',100,36750000,43000000),(183,'Winner X bạc đen vàng','Honda','motor_image/motor68.png','Chiều dai x rộng x cao là 2019 x 727 x 1104mm. Khoảng cách trục bánh xe là 1278mm, độ cao yên là 795mm, khoảng sáng gầm xe là 151mm. Loại động cơ PGM-FI, DOHC, xylanh đơn, côn 6 số, làm mát bằng dung dịch. Dung tích 149,1cm3','Bảo dưỡng \n3/6/9 tháng',100,36750000,43000000),(184,'Winner đỏ đen xanh','Honda','motor_image/motor69.jpg','Chiều dai x rộng x cao là 2019 x 727 x 1104mm. Khoảng cách trục bánh xe là 1278mm, độ cao yên là 795mm, khoảng sáng gầm xe là 151mm. Loại động cơ PGM-FI, DOHC, xylanh đơn, côn 6 số, làm mát bằng dung dịch. Dung tích 149,1cm3','Bảo dưỡng \n3/6/9 tháng',100,36750000,42000000),(185,'Exciter 155 VVA cao cấp','Yamaha','motor_image/motor70.png','Chiều dài x rộng x cao là 1985 x 670 x 1100mm. Khoảng cách trục bánh xe 1290mm, độ cao yên là 795mm, độ cao gầm xe 155mm. Loại 4 thì, 4 van, SOHC, làm mát bằng dung dịch, xylanh đơn','Bảo dưỡng \n3/6/9 tháng',100,42250000,50800000),(186,'Exciter 155 VVA giới hạn màu','Yamaha','motor_image/motor71.png','Chiều dài x rộng x cao là 1985 x 670 x 1100mm. Khoảng cách trục bánh xe 1290mm, độ cao yên là 795mm, độ cao gầm xe 155mm. Loại 4 thì, 4 van, SOHC, làm mát bằng dung dịch, xylanh đơn','Bảo dưỡng \n3/6/9 tháng',100,44250000,52000000),(187,'Exciter 155 VVA master art of Street','Yamaha','motor_image/motor72.png','Chiều dài x rộng x cao là 1985 x 670 x 1100mm. Khoảng cách trục bánh xe 1290mm, độ cao yên là 795mm, độ cao gầm xe 155mm. Loại 4 thì, 4 van, SOHC, làm mát bằng dung dịch, xylanh đơn','Bảo dưỡng \n3/6/9 tháng',100,44250000,52000000),(188,'Exciter 155 VVA bản 60 năm','Yamaha','motor_image/motor73.png','Chiều dài x rộng x cao là 1985 x 670 x 1100mm. Khoảng cách trục bánh xe 1290mm, độ cao yên là 795mm, độ cao gầm xe 155mm. Loại 4 thì, 4 van, SOHC, làm mát bằng dung dịch, xylanh đơn','Bảo dưỡng \n3/6/9 tháng',100,44250000,52500000),(189,'Exciter 155 VVA monster energy motogp','Yamaha','motor_image/motor74.jpg','Chiều dài x rộng x cao là 1985 x 670 x 1100mm. Khoảng cách trục bánh xe 1290mm, độ cao yên là 795mm, độ cao gầm xe 155mm. Loại 4 thì, 4 van, SOHC, làm mát bằng dung dịch, xylanh đơn','Bảo dưỡng \n3/6/9 tháng',100,44250000,52000000),(190,'Exciter 155 VVA bản GP','Yamaha','motor_image/motor75.jpg','Chiều dài x rộng x cao là 1985 x 670 x 1100mm. Khoảng cách trục bánh xe 1290mm, độ cao yên là 795mm, độ cao gầm xe 155mm. Loại 4 thì, 4 van, SOHC, làm mát bằng dung dịch, xylanh đơn','Bảo dưỡng \n3/6/9 tháng',100,44250000,51100000),(191,'Exciter 155 VVA bản tiêu chuẩn','Yamaha','motor_image/motor76.png','Chiều dài x rộng x cao là 1985 x 670 x 1100mm. Khoảng cách trục bánh xe 1290mm, độ cao yên là 795mm, độ cao gầm xe 155mm. Loại 4 thì, 4 van, SOHC, làm mát bằng dung dịch, xylanh đơn','Bảo dưỡng \n3/6/9 tháng',100,41250000,47800000),(192,'Exciter 150 giới hạn màu','Yamaha','motor_image/motor77.png','Chiều dài x rộng x cao là 1985 x 670 x 1100mm. Khoảng cách trục bánh xe 1290mm, độ cao yên là 795mm, độ cao gầm xe 155mm. Loại 4 thì, 4 van, SOHC, làm mát bằng dung dịch, xylanh đơn','Bảo dưỡng \n3/6/9 tháng',100,38250000,45800000),(193,'Exciter 150 bản RC','Yamaha','motor_image/motor78.png','Chiều dài x rộng x cao là 1985 x 670 x 1100mm. Khoảng cách trục bánh xe 1290mm, độ cao yên là 795mm, độ cao gầm xe 155mm. Loại 4 thì, 4 van, SOHC, làm mát bằng dung dịch, xylanh đơn','Bảo dưỡng \n3/6/9 tháng',100,38250000,44800000),(194,'Sirius phanh cơ','Yamaha','motor_image/motor79.png','Chiều dài x rộng x cao là 1940 x 715 x 1075mm. Độ cao yên xe là 770mm, khoảng cách trục bánh xe 1200mm, độ cao gầm xe là 130mm. Loại 4 thì, 2 van SOHC, làm mát bằng không khí','Bảo dưỡng \n3/6/9 tháng',100,11250000,19100000),(195,'Sirius phanh đĩa màu mới','Yamaha','motor_image/motor80.png','Chiều dài x rộng x cao là 1940 x 715 x 1075mm. Độ cao yên xe là 770mm, khoảng cách trục bánh xe 1200mm, độ cao gầm xe là 130mm. Loại 4 thì, 2 van SOHC, làm mát bằng không khí','Bảo dưỡng \n3/6/9 tháng',100,13250000,20900000),(196,'Sirius phanh đĩa','Yamaha','motor_image/motor81.png','Chiều dài x rộng x cao là 1940 x 715 x 1075mm. Độ cao yên xe là 770mm, khoảng cách trục bánh xe 1200mm, độ cao gầm xe là 130mm. Loại 4 thì, 2 van SOHC, làm mát bằng không khí','Bảo dưỡng \n3/6/9 tháng',100,13250000,20900000),(197,'Sirius vành đúc màu mới','Yamaha','motor_image/motor82.png','Chiều dài x rộng x cao là 1940 x 715 x 1075mm. Độ cao yên xe là 770mm, khoảng cách trục bánh xe 1200mm, độ cao gầm xe là 130mm. Loại 4 thì, 2 van SOHC, làm mát bằng không khí','Bảo dưỡng \n3/6/9 tháng',100,14750000,22100000),(198,'Grande bản giới hạn hoàn toàn mới','Yamaha','motor_image/motor83.png','Chiều dài x rộng x cao là 1820 x 684 x 1155mm. Khoảng sáng gầm là 127mm. Loại Blue Core Hybrid, làm mát bằng không khí, 4 thì 2 van, xylanh đơn. Dung tích xylanh là 125cc','Bảo dưỡng \n3/6/9 tháng',100,43000000,51900000),(199,'Grande Blue Core Hybrid bản giới hạn','Yamaha','motor_image/motor84.png','Chiều dài x rộng x cao là 1820 x 684 x 1155mm. Khoảng sáng gầm là 127mm. Loại Blue Core Hybrid, làm mát bằng không khí, 4 thì 2 van, xylanh đơn. Dung tích xylanh là 125cc','Bảo dưỡng \n3/6/9 tháng',100,43250000,50500000),(200,'Grande bản đặc biệt hoàn toàn mới','Yamaha','motor_image/motor85.png','Chiều dài x rộng x cao là 1820 x 684 x 1155mm. Khoảng sáng gầm là 127mm. Loại Blue Core Hybrid, làm mát bằng không khí, 4 thì 2 van, xylanh đơn. Dung tích xylanh là 125cc','Bảo dưỡng \n3/6/9 tháng',100,42750000,51200000),(201,'Grande Blue Core Hybrid bản đặt biệt','Yamaha','motor_image/motor86.png','Chiều dài x rộng x cao là 1820 x 684 x 1155mm. Khoảng sáng gầm là 127mm. Loại Blue Core Hybrid, làm mát bằng không khí, 4 thì 2 van, xylanh đơn. Dung tích xylanh là 125cc','Bảo dưỡng \n3/6/9 tháng',100,43250000,50000000),(202,'Grande bẩn tiêu chuẩn hoàn toàn mới','Yamaha','motor_image/motor87.png','Chiều dài x rộng x cao là 1820 x 684 x 1155mm. Khoảng sáng gầm là 127mm. Loại Blue Core Hybrid, làm mát bằng không khí, 4 thì 2 van, xylanh đơn. Dung tích xylanh là 125cc','Bảo dưỡng \n3/6/9 tháng',100,39250000,46800000),(203,'Grande Blue Core Hybrid bản tiêu chuẩn','Yamaha','motor_image/motor88.png','Chiều dài x rộng x cao là 1820 x 684 x 1155mm. Khoảng sáng gầm là 127mm. Loại Blue Core Hybrid, làm mát bằng không khí, 4 thì 2 van, xylanh đơn. Dung tích xylanh là 125cc','Bảo dưỡng \n3/6/9 tháng',100,39250000,46000000),(204,'Jupiter FI GP','Yamaha','motor_image/motor89.jpg','Chiều dài x rộng x cao là 1935 x 680 x 1065mm. Độ cao yên xe 765mm, khoảng cách trục bánh xe 1240mm, độ cao gầm xe 125mm','Bảo dưỡng \n3/6/9 tháng',100,25750000,32751000),(205,'Jupiter FI RC','Yamaha','motor_image/motor90.png','Chiều dài x rộng x cao là 1935 x 680 x 1065mm. Độ cao yên xe 765mm, khoảng cách trục bánh xe 1240mm, độ cao gầm xe 125mm','Bảo dưỡng \n3/6/9 tháng',100,25750000,31753500),(206,'Vespa Sprint S 125CC','Piaggio','motor_image/motor91.png','Kích thước xe 1852 x 680mm, độ cao yên 790mm, khoảng cách trục bánh xe 1334mm. Động cơ 3 van, xăng, 1 xylanh 4 kỳ, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,72250000,81300000),(207,'Vespa Sprint S 150CC','Piaggio','motor_image/motor92.png','Kích thước xe 1852 x 680mm, độ cao yên 790mm, khoảng cách trục bánh xe 1334mm. Động cơ 3 van, xăng, 1 xylanh 4 kỳ, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,86750000,94300000),(208,'Vespa Sprint LED 125CC','Piaggio','motor_image/motor93.png','Kích thước xe 1852 x 680mm, độ cao yên 790mm, khoảng cách trục bánh xe 1334mm. Động cơ 3 van, xăng, 1 xylanh 4 kỳ, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,71250000,78900000),(209,'Vespa Primavera LED 2022','Piaggio','motor_image/motor94.png','Kích thước xe 1852 x 680mm, độ cao yên 790mm, khoảng cách trục bánh xe 1334mm. Động cơ 3 van, xăng, 1 xylanh 4 kỳ, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,69250000,76800000),(210,'Vespa Primavera S','Piaggio','motor_image/motor95.png','Kích thước xe 1852 x 680mm, độ cao yên 790mm, khoảng cách trục bánh xe 1334mm. Động cơ 3 van, xăng, 1 xylanh 4 kỳ, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,71250000,79400000),(211,'Vespa Primavera RED','Piaggio','motor_image/motor96.png','Kích thước xe 1852 x 680mm, độ cao yên 790mm, khoảng cách trục bánh xe 1334mm. Động cơ 3 van, xăng, 1 xylanh 4 kỳ, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,75250000,82800000),(212,'Vespa Sei Giorni II','Piaggio','motor_image/motor97.png','Kích thước xe 1852 x 680mm, độ cao yên 790mm, khoảng cách trục bánh xe 1334mm. Động cơ 3 van, xăng, 1 xylanh 4 kỳ, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,131250000,139400000),(213,'Vespa GTS 300 HPE','Piaggio','motor_image/motor98.png','Kích thước xe 1852 x 680mm, độ cao yên 790mm, khoảng cách trục bánh xe 1334mm. Động cơ 3 van, xăng, 1 xylanh 4 kỳ, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,146750000,155400000),(214,'Vespa GTS Super Sport','Piaggio','motor_image/motor99.png','Kích thước xe 1852 x 680mm, độ cao yên 790mm, khoảng cách trục bánh xe 1334mm. Động cơ 3 van, xăng, 1 xylanh 4 kỳ, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,106750000,115400000),(215,'Vespa 946 RED','Piaggio','motor_image/motor100.png','Kích thước xe 1852 x 680mm, độ cao yên 790mm, khoảng cách trục bánh xe 1334mm. Động cơ 3 van, xăng, 1 xylanh 4 kỳ, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,395750000,405000000),(216,'Vespa Super GTS 125','Piaggio','motor_image/motor101.jpg','Kích thước xe 1852 x 680mm, độ cao yên 790mm, khoảng cách trục bánh xe 1334mm. Động cơ 3 van, xăng, 1 xylanh 4 kỳ, làm mát bằng không khí.','Bảo dưỡng \n3/6/9 tháng',100,85250000,92600000),(217,'Liberty 50CC','Piaggio','motor_image/motor102.png','Xe dài 1945mm, chiều cao yên 790mm, có khung thép ống cường lực cao với cấu trúc đơn. Động cơ I-Get đơn xi lanh, 4 thì 3 value','Bảo dưỡng \n3/6/9 tháng',100,31250000,39900000),(218,'Liberty ABS S 125CC','Piaggio','motor_image/motor103.png','Xe dài 1945mm, chiều cao yên 790mm, có khung thép ống cường lực cao với cấu trúc đơn. Động cơ I-Get đơn xi lanh, 4 thì 3 value','Bảo dưỡng \n3/6/9 tháng',100,51250000,58800000),(219,'Liberty ONE','Piaggio','motor_image/motor104.jpg','Xe dài 1945mm, chiều cao yên 790mm, có khung thép ống cường lực cao với cấu trúc đơn. Động cơ I-Get đơn xi lanh, 4 thì 3 value','Bảo dưỡng \n3/6/9 tháng',100,41250000,49200000),(220,'Medley S 125','Piaggio','motor_image/motor105.png','chiều dài x rộng là 2020 x 205mm. Khoảng cách trục bánh xe 1390mm, chiều cao yên 799mm. Động cơ I-Get xylanh đơn 4 thì 4 van','Bảo dưỡng \n3/6/9 tháng',100,72250000,80500000),(221,'Medley S 150 2022','Piaggio','motor_image/motor106.png','chiều dài x rộng là 2020 x 205mm. Khoảng cách trục bánh xe 1390mm, chiều cao yên 799mm. Động cơ I-Get xylanh đơn 4 thì 4 van','Bảo dưỡng \n3/6/9 tháng',100,86250000,95300000),(222,'Satria F150','Suzuki','motor_image/motor107.png','Chiều dài x rộng x cao là 1960x675x980 mm. Độ cao yên là 764mm, khoảng cách gầm xe với mặt đất là 150mm, Động cơ DOHC, 4 thì, 4 values, FI, công suất 147,3cc','Bảo dưỡng \n3/6/9 tháng',100,47680000,54000000),(223,'Raider R150','Suzuki','motor_image/motor108.png','Chiều dài x rộng x cao là 1960x675x980 mm. Độ cao yên là 765mm, khoảng sáng gầm xe là 150mm. Động cơ D0HC, 4 van, con tay 6 số, công suất 150cc.','Bảo dưỡng \n3/6/9 tháng',100,43570000,51190000),(224,'Burgman Street','Suzuki','motor_image/motor109.jpg','Chiều dài x rộng x cao là 1880x715x1140 mm, chiều dài trục cơ sở là 1265mm. Độ cao yên là 780mm. Dung tích ngăn chúa đồ dưới yên là 21,5mm.','Bảo dưỡng \n3/6/9 tháng',100,41750000,49500000),(225,'Impulse 125 FI','Suzuki','motor_image/motor110.jpg','Động cơ 4 thì 125 phân khối mạnh mẽ, phun xăng điện tử FI. Chiều dài x rộng x cao là 1920 x 680 x 1065 mm. Độ cao yên là 770mm, khoảng cách giữa 2 trục bánh xe là 1285mm, khoảng sáng gầm là 135mm.','Bảo dưỡng \n3/6/9 tháng',100,22250000,29000000);
/*!40000 ALTER TABLE `myapp_motor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_store`
--

DROP TABLE IF EXISTS `myapp_store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_store` (
  `store_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `owner` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`store_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_store`
--

LOCK TABLES `myapp_store` WRITE;
/*!40000 ALTER TABLE `myapp_store` DISABLE KEYS */;
INSERT INTO `myapp_store` VALUES (4,'Duy Phong Xe Máy','Nguyễn Duy Phong','336 đường Láng, Đống Đa Hà Nội','924128686','duyphongxemay@gmail.com'),(5,'Siêu thị xe máy Hoàng Kiên','Hoàng Kiên','52 Chùa Hà, Cầu Giấy Hà Nội','986938662','hoangkien@gmail.com'),(6,'Siêu thị xe BD','Nguyễn Cao Nhật','165 Xuân Thuỷ Cầu Giấy HN','987435678','xebd@gmail.com'),(7,'Cửa hàng Đáo Ngời','Nguyễn Văn Đáo','Chợ Thứa Lương Tài Bắc Ninh','989632468','nguyenvdao@gmail.com'),(8,'Xe máy Việt Thanh Hà Đông','Trần Hoàng Việt','605 Nguyễn Trãi','339179686','xmvt@gmail.com'),(9,'HEAD Thương Mại 98','Nguyễn Quang Hưng','20/390 Tố Hữu, Trung Văn Nam Từ Liêm HN','2485874216','headthuongmai98@gmail.com'),(10,'HEAD Hồng Hạnh','Nguyễn Thị Hồng Hạnh','252 Phố Huế, Hai bà Trưng, HN','2439749797','headhonghanh@gmail.com'),(11,'HEAD T&H','Trần Anh Sơn','K1 Thành Công Láng hạ Ba Đình','2437724427','headhonghanh@gmail.com'),(12,'HEAD Hà Nội Motor','Hà Thế Tài','Tổ Bình Minh, Tt Trâu Quỳ Gia Lâm HN','2466729444','headhnmotor@gmail.com'),(13,'HEAD Vitan','Bùi Việt tân','Số 5 Nguyễn Khánh Toàn, Quan Hoa, Cầu Giấy','2438335311','headvitan@gmail.com'),(14,'HEAD Hoàng Hợp','Nguyễn Hoàng Hợp','119 Lạc Long Quân, P. Nghĩa Đô, cầu Giấy','2437531351','headhoanghop@gmail.com'),(15,'HEAD Phương Hà','Trương Phương Hà','508 Hà Huy Tập, Gia Lâm HN','2436981522','headphuongha@gmail.com'),(16,'Đống  Đa','Nguyễn Văn Hoàng Nam','123 ô chợ Dừa Đống Đa HN','2433668222','dongdayhm@gmail.com'),(17,'Việt Nhật 2','Trần Văn Thân','231 Tôn Đức Thắng Đống Đa HN','2435116532','vietnhat2yhm@gmail.com'),(18,'Xe máy 74','Nguyễn Văn Dũng','74 phố Khâm Thiên Đống Đa HN','2438510610','xemay74@gmail.com'),(19,'Anh Khánh','Bùi Bảo Anh','D1-22, KĐT Geleximco Lê Trọng Tấn Hà Đông HN','825157777','ankhanhyhm@gmail.com'),(20,'Cầu Giấy','Đỗ Anh Tài','98 Xuân Thuỷ Cầu Giấy HN','2437574999','caugiayyhm@gmail.com'),(21,'Việt Duy 2','Bùi Việt Duy','Ngọc Giả, Chúc Sơn, Chương Mỹ, HN','2433551919','vietduyyhm@gmail.com'),(22,'Lê Văn Lương','Phạm Diễm Quỳnh','68 đường Lê Văn Lương, Nhân Chính, Thanh Xuân','356426868','levanluongyhn@gmail.com'),(23,'Motor Minh Anh','Phạm Minh Anh','79 Phố Chùa Hà, Cầu Giấy, HN','911771996','motorminhanhvip@gmail.com'),(24,'Cửa hàng xe máy Anh Lộc','Nguyễn Bá Chí','275 Bạch Mai, Hai Bà Trưng, HN','923562889','anhlocmotor@gmail.com'),(25,'Đức Hùng','Dương Đức Hùng','921 Đường Giải Phóng, Giáp Bát, Hoàng Mai','2436645239','nguyenduchung@gmail.com'),(26,'Piaggio Đại Phát','Nguyễn Văn Dũng','118 Liễu Giai, Ba Đình, Hà Nội','376639181','Dugxpiaggio@gmail.com'),(27,'Xe Máy Piaggio Giáp','Bùi  Tiến Giáp','93 P. Giáp Nhị, Thịnh Liệt, Hoàng Mai, HN','373676868','ngtgiap.piagio@gmail.com'),(28,'Piaggio Đại Hoàng Gia','Nguyễn Trung Kiên','75 Thanh Xuân Trung, Thanh Xuân HN','976890801','Trugkientx@gmail.com'),(29,'Cửa hàng 2S Chín Hải','Nguyễn Văn Phùng','145 Ấp 4, Long Hòa, H. Cần Đước, Long An','2838979022','nvphung2S@gmail.com'),(30,'Cửa hàng 2S Công Tâm','Đỗ Ngọc Thu','497A Kha Vạn Cân, P. Linh Đông, Q.Thủ Đức, Hồ Chí Minh','907672737','congtam2S@gmail.com'),(31,'Cửa hàng 2S Dũng Suzuki','Trần QuangDũng','887 (số cũ: 127A) Lê Văn Lương, ấp 5, xã Phước Kiển, huyện Nhà Bè, TP. HCM','2439746462','Dung2S@gmail.com'),(32,'Cửa hàng 2S Hùng CLE','Nguyễn Đức Hùng','Số 1 Ngõ 424 Trần Khát Chân,Phường Phố Huế, Q. Hai Bà Trưng, Hà Nội','2973519666','duchung2S@gmail.com'),(33,'Cửa hàng 2S Kim Điệp','Trương Kim Điệp','Khu Vực 3, TT Thứ 3, Huyện An Biên, Tỉnh Kiên Giang','903510317','kimdiep2S@2gmail.com');
/*!40000 ALTER TABLE `myapp_store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_supplier`
--

DROP TABLE IF EXISTS `myapp_supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_supplier` (
  `supplier_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`supplier_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_supplier`
--

LOCK TABLES `myapp_supplier` WRITE;
/*!40000 ALTER TABLE `myapp_supplier` DISABLE KEYS */;
INSERT INTO `myapp_supplier` VALUES (4,'Honda Việt Nam','P. Phúc Thắng, TP Phúc yên, Vĩnh Phúc','18008001','cr@honda.com.vn'),(5,'Yamaha Motor VN','Thôn Bình An, Xã Trung Giã, Huyện Sóc Sơn, TP Hà nội','18001558','cskh@yamaha-motor.com.vn'),(6,'SYM','Lô 4, đường số 5C, KCN Nhơn Trạch 2, Đồng Nai','2513812080','cskh@sym.com.vn'),(7,'Việt Nam Suzuki','Đường số 2, KCN Long Bình, P.Long Bình, TP. Biên Hoà, Đồng Nai','18006950','cskh@vietnam-suzuki.com.vn'),(8,'Công ty TNHH Biên Vân Gỗ','Số 24, ngõ 67 ĐÌnh Thôn, Mỹ Đình, Nam Từ Liêm HN','024-665956648','bienvango@gmail.com'),(9,'Sơn Ô Tô Hợp Thuỷ','Số 3 Lê Quang Đạo, Q. Từ Liêm HN','024-378554490','Sonhopthuy@gmail.com'),(10,'Công Ty CP Thương Mại Hồng An','Số 29 Tổ 7 Yên Sở, Hoàng Mai HN','024-36453986','tmhongan@gmail.com'),(11,'Công Ty TNHH Motorlife Hoàng Phú','Biệt thự 28, OBT2, X1, KĐT Bắc Linh Đàm, Hoàng Mai HN','915572211','Hoangphumotor@gmail.com');
/*!40000 ALTER TABLE `myapp_supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_user`
--

DROP TABLE IF EXISTS `myapp_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `name` varchar(100) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `role` varchar(20) NOT NULL,
  `dob` date DEFAULT NULL,
  `salary` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_user`
--

LOCK TABLES `myapp_user` WRITE;
/*!40000 ALTER TABLE `myapp_user` DISABLE KEYS */;
INSERT INTO `myapp_user` VALUES (1,'pbkdf2_sha256$600000$L5TzufLiFGvUrO8G2uGXFH$lj1kVWkFcnzpUdXvKBvLjlVQSdOcywrTLCSzOSmk/5w=','2023-04-20 04:05:48.274169',1,'khanhnvtb','','',1,1,'2023-04-15 11:44:36.000000','Nguyễn Văn Khánh','user_image/Khanh_2IqkxTE.jpg','Nam','Đông Xá, Đông Hưng, Thái Bình','0857337586','khanhtb1012@gmail.com','admin','2001-12-10',0),(2,'pbkdf2_sha256$390000$wYREGQB1SE0w8VmLtGLFPB$CcwH1Z7V34BXmduRMNsYZMxqbSdXWRcPP6nNKbVM8iM=','2023-04-15 12:03:55.437605',0,'phuy2712','','',0,1,'2023-04-15 12:02:36.509843','Phan Quang Huy','user_image/user2_LsJB2jS.jpg','Nam','Thái Bình','0987687251','phuy2712@gmail.com','Nhân viên kho','2000-12-27',500000);
/*!40000 ALTER TABLE `myapp_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_user_groups`
--

DROP TABLE IF EXISTS `myapp_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_user_groups_user_id_group_id_1ef5feb7_uniq` (`user_id`,`group_id`),
  KEY `myapp_user_groups_group_id_488eb0fb_fk_auth_group_id` (`group_id`),
  CONSTRAINT `myapp_user_groups_group_id_488eb0fb_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `myapp_user_groups_user_id_925f87c5_fk_myapp_user_id` FOREIGN KEY (`user_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_user_groups`
--

LOCK TABLES `myapp_user_groups` WRITE;
/*!40000 ALTER TABLE `myapp_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `myapp_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_user_user_permissions`
--

DROP TABLE IF EXISTS `myapp_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_user_user_permissions_user_id_permission_id_13102f46_uniq` (`user_id`,`permission_id`),
  KEY `myapp_user_user_perm_permission_id_4657f93a_fk_auth_perm` (`permission_id`),
  CONSTRAINT `myapp_user_user_perm_permission_id_4657f93a_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `myapp_user_user_permissions_user_id_3f0ef5c3_fk_myapp_user_id` FOREIGN KEY (`user_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_user_user_permissions`
--

LOCK TABLES `myapp_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `myapp_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `myapp_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-20 16:06:16
