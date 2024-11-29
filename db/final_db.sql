/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.5.8-log : Database - scms_pawcare
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`scms_pawcare` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `scms_pawcare`;

/*Table structure for table `acc_sale` */

DROP TABLE IF EXISTS `acc_sale`;

CREATE TABLE `acc_sale` (
  `acc_sale_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `accessorie_id` int(11) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`acc_sale_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `acc_sale` */

insert  into `acc_sale`(`acc_sale_id`,`user_id`,`accessorie_id`,`price`,`date`,`status`) values 
(1,1,2,'44','2023-12-16','cart'),
(2,1,2,'44','2023-12-16','cart'),
(3,1,2,'44','2023-12-16','cart'),
(4,1,2,'44','2023-12-26','cart'),
(5,1,2,'44','2023-12-26','cart'),
(6,1,2,'44','2023-12-26','cart'),
(7,1,2,'44','2023-12-26','cart'),
(8,1,2,'44','2023-12-26','cart'),
(9,1,2,'44','2024-01-01','cart'),
(10,3,2,'44','2024-01-11','cart'),
(11,3,3,'500','2024-02-18','cart'),
(12,3,3,'44','2024-02-18','cart'),
(13,3,0,'500','2024-02-18','cart'),
(14,3,0,'44','2024-02-18','cart'),
(15,3,0,'44','2024-02-18','cart'),
(16,3,2,'44','2024-02-18','cart'),
(17,3,2,'500','2024-02-18','cart');

/*Table structure for table `accessories` */

DROP TABLE IF EXISTS `accessories`;

CREATE TABLE `accessories` (
  `accessorie_id` int(11) NOT NULL AUTO_INCREMENT,
  `shop_id` int(11) DEFAULT NULL,
  `accessories` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`accessorie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `accessories` */

insert  into `accessories`(`accessorie_id`,`shop_id`,`accessories`,`price`,`quantity`,`image`) values 
(4,2,'pet travel Bag','20000','10','static/images/d4973e73-eee8-4f65-8c33-cdf09b91eb8facc5.jpg'),
(5,2,'brush','1000','18','static/images/67b6555d-90ca-46db-be56-9170e9743378acc4.jpg'),
(6,2,'lap','2000','30','static/images/88910a03-3826-4881-9432-ec277ec08299acc2.jpeg'),
(7,2,'harness','7000','20','static/images/99434a8f-9fa8-4045-b205-2becc711a9f8acc1.jpeg'),
(8,3,'belt','2000','20','static/images/3b2012c5-9194-4ea3-afab-70e3ee2f914cacc3.jpg');

/*Table structure for table `allocation_request` */

DROP TABLE IF EXISTS `allocation_request`;

CREATE TABLE `allocation_request` (
  `allocation_request_id` int(11) NOT NULL AUTO_INCREMENT,
  `day` varchar(100) DEFAULT NULL,
  `no_of_days` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`allocation_request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `allocation_request` */

insert  into `allocation_request`(`allocation_request_id`,`day`,`no_of_days`,`amount`,`date`,`status`,`user_id`,`staff_id`) values 
(1,'2024-06-01','10','6000','2024-05-24','paid',1,2),
(2,'2024-06-01','55','2000','2024-06-17','ok',2,2);

/*Table structure for table `appointment` */

DROP TABLE IF EXISTS `appointment`;

CREATE TABLE `appointment` (
  `appointment_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `pet_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `book_date` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`appointment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `appointment` */

insert  into `appointment`(`appointment_id`,`category_id`,`pet_id`,`user_id`,`status`,`book_date`,`date`,`amount`) values 
(1,4,26,1,'paid','2024-05-23','2024-05-23','2000'),
(2,4,24,1,'reject','2024-05-15','2024-05-23',NULL),
(3,4,19,2,'paid','2024-06-25','2024-06-17','6000');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category_name`) values 
(3,'walking'),
(4,'grooming');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `chat` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`sender_id`,`receiver_id`,`chat`,`date`) values 
(1,3,5,'hi','2024-05-25'),
(2,5,3,'hello','2024-05-25'),
(3,5,3,'hi','2024-06-08'),
(4,7,3,'hi','2024-06-17');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`login_id`,`complaint`,`reply`,`date`) values 
(1,10,'network problems ','ok','2023-12-18'),
(2,11,'not good','ok','2023-12-26'),
(3,15,'not good','ok','2024-01-11'),
(4,5,'not good','ok','2024-05-23'),
(5,5,'not good','pending','2024-05-23'),
(6,5,'not good','pending','2024-05-23');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`feedback`,`date`) values 
(1,3,'hhdj',NULL),
(2,3,'ghjhu','2024-02-18');

/*Table structure for table `hospitals` */

DROP TABLE IF EXISTS `hospitals`;

CREATE TABLE `hospitals` (
  `hospital_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `hospital_name` varchar(100) DEFAULT NULL,
  `h_place` varchar(100) DEFAULT NULL,
  `h_phone` varchar(100) DEFAULT NULL,
  `h_email` varchar(100) DEFAULT NULL,
  `h_pincode` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`hospital_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `hospitals` */

insert  into `hospitals`(`hospital_id`,`login_id`,`hospital_name`,`h_place`,`h_phone`,`h_email`,`h_pincode`) values 
(1,8,'The Cochin Pet Hospital','Kadavanthra','2345678908','CochinPet@gmail.com','232323'),
(2,9,'ad','Kadavanthra','2345678908','anna@gmail.com','333333');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(3,'anju','anju','staff'),
(5,'maya','1234','user'),
(7,'anju','anju22','user'),
(8,'vet1','vet1','veterinary'),
(9,'l','l','pending'),
(10,'shop1','shop1','shop');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment` int(11) NOT NULL AUTO_INCREMENT,
  `shop_id` int(11) DEFAULT NULL,
  `payment_for_id` int(11) DEFAULT NULL,
  `payment_type` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment`,`shop_id`,`payment_for_id`,`payment_type`,`amount`,`date`) values 
(1,15,20,'pets','200','2024-02-23'),
(2,1,1,'grooming','2000','2024-05-24'),
(3,1,1,'grooming','2000','2024-05-24'),
(4,2,1,'accessories','6000','2024-05-24'),
(5,2,1,'pets','4000','2024-05-24'),
(6,1,1,'Allocation','6000','2024-05-25'),
(7,1,1,'vet','6000','2024-05-29'),
(8,1,1,'vet','6000','2024-05-29'),
(9,4,2,'accessories','2000','2024-06-17'),
(10,5,2,'accessories','2000','2024-06-17'),
(11,5,2,'accessories','2000','2024-06-17'),
(12,3,2,'grooming','6000','2024-06-17');

/*Table structure for table `pet_image` */

DROP TABLE IF EXISTS `pet_image`;

CREATE TABLE `pet_image` (
  `pet_image_id` int(11) NOT NULL AUTO_INCREMENT,
  `pet_id` int(11) DEFAULT NULL,
  `file` varchar(2000) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pet_image_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `pet_image` */

insert  into `pet_image`(`pet_image_id`,`pet_id`,`file`,`type`) values 
(1,24,'static/images/e3836780-3021-4238-93fc-61de389b060dblog-1.jpg','image'),
(2,24,'static/images/e84c151d-d8ee-4c1d-be52-079966c07ee9user3.jpg','image'),
(5,24,'static/images/9c394c48-2a45-4099-b9ee-fb9e68e44100user2.jpeg','image'),
(7,24,'static/images/29577999-e416-48a4-872e-45da45ff3f17team-2.jpg','image'),
(8,24,'static/images/847739ee-ea7f-497a-b5f8-a79e24157098video1.mp4','video'),
(9,19,'static/images/b8dbde5b-683a-4243-9006-dbb3446e059eteam-3.jpg','image'),
(10,19,'static/images/4b66b90f-80bb-4911-81a3-2cfac2c31b12hero.jpg','image'),
(11,17,'static/images/4c697370-d869-443f-a4cd-5126b4a18b4cabout.jpg','image'),
(12,17,'static/images/303f39a6-ad63-40c4-8da3-91dfd4cfbf56blog-2.jpg','image'),
(13,28,'static/images/dbeba8fc-7023-4788-83a3-542190324a0ablog-2.jpg','image'),
(14,28,'static/images/9f6eeb39-7805-4bdd-b248-f1f525d671edoffer.jpg','image');

/*Table structure for table `pet_sale` */

DROP TABLE IF EXISTS `pet_sale`;

CREATE TABLE `pet_sale` (
  `pet_sale_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `pet_id` int(11) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pet_sale_id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=latin1;

/*Data for the table `pet_sale` */

insert  into `pet_sale`(`pet_sale_id`,`user_id`,`pet_id`,`price`,`date`,`status`) values 
(1,1,13,'10000','2023-12-15','cart'),
(2,1,13,'10000','2023-12-15','cart'),
(3,1,13,'10000','2023-12-15','cart'),
(4,1,13,'10000','2023-12-15','cart'),
(5,1,13,'10000','2023-12-15','cart'),
(6,1,13,'10000','2023-12-15','cart'),
(7,1,13,'10000','2023-12-15','cart'),
(8,1,0,'None','2023-12-15','cart'),
(9,1,0,'None','2023-12-15','cart'),
(10,1,2,'null','2023-12-15','cart'),
(11,1,2,'44','2023-12-16','cart'),
(12,1,2,'44','2023-12-16','cart'),
(13,1,2,'44','2023-12-16','cart'),
(14,1,16,'15000','2023-12-18','cart'),
(15,1,15,'350','2023-12-18','cart'),
(16,1,14,'10000','2023-12-18','cart'),
(17,1,17,'shop','2023-12-18','cart'),
(18,1,17,'shop','2023-12-18','cart'),
(19,1,15,'350','2023-12-20','cart'),
(20,1,14,'10000','2023-12-26','cart'),
(21,2,14,'10000','2023-12-26','cart'),
(22,2,15,'350','2023-12-26','cart'),
(23,1,14,'10000','2023-12-26','cart'),
(24,1,18,'600','2023-12-26','cart'),
(25,1,14,'10000','2024-01-01','cart'),
(26,3,0,'100000','2024-02-18','cart'),
(27,3,0,'500','2024-02-18','cart'),
(28,3,0,'600','2024-02-18','cart'),
(29,3,17,'500','2024-02-18','cart'),
(30,3,18,'600','2024-02-18','cart'),
(31,3,14,'10000','2024-02-18','cart'),
(32,3,18,'600','2024-02-18','cart'),
(33,3,18,'600','2024-02-18','cart'),
(34,3,18,'600','2024-02-18','cart'),
(35,3,18,'600','2024-02-18','cart'),
(36,3,19,'100000','2024-02-18','cart'),
(37,3,17,'500','2024-02-18','cart'),
(38,3,18,'600','2024-02-18','cart'),
(39,3,18,'600','2024-02-18','cart'),
(40,3,18,'600','2024-02-18','cart'),
(41,3,18,'600','2024-02-18','cart'),
(42,3,19,'100000','2024-02-18','cart'),
(43,3,18,'600','2024-02-18','cart'),
(44,3,19,'100000','2024-02-18','cart'),
(45,3,18,'600','2024-02-18','cart'),
(46,3,18,'600','2024-02-18','cart'),
(47,3,15,'350','2024-02-18','cart'),
(48,3,19,'100000','2024-02-18','cart'),
(49,3,18,'600','2024-02-18','cart'),
(50,3,18,'600','2024-02-18','cart'),
(51,3,19,'100000','2024-02-18','cart'),
(52,3,19,'100000','2024-02-18','cart'),
(53,3,19,'100000','2024-02-18','cart'),
(54,3,19,'100000','2024-02-18','cart'),
(55,3,13,'10000','2024-02-23','cart'),
(56,3,20,'200','2024-02-23','cart');

/*Table structure for table `pets` */

DROP TABLE IF EXISTS `pets`;

CREATE TABLE `pets` (
  `pet_id` int(11) NOT NULL AUTO_INCREMENT,
  `Pet_for_id` int(11) DEFAULT NULL,
  `pet_name` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `color` varchar(100) DEFAULT NULL,
  `breed` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `qty` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pet_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `pets` */

insert  into `pets`(`pet_id`,`Pet_for_id`,`pet_name`,`age`,`color`,`breed`,`gender`,`type`,`qty`,`price`) values 
(13,10,'pet1','2','white','abc',NULL,'user',NULL,NULL),
(14,10,'cat','2','white','long haired',NULL,'user',NULL,NULL),
(15,10,'birds','1','blue and yellow ','abcfh',NULL,'user',NULL,NULL),
(16,10,'rabbit ','2','white','Rex rabbit ',NULL,'user',NULL,NULL),
(17,6,'shop_pet','1','white','ggg',NULL,'600',NULL,NULL),
(18,12,'cat','2','gray','sss','male','shop','10','2000'),
(19,7,'dog','1','white','jkehj','female','shop','15','2000'),
(20,15,'dog1','2','white','bdndm',NULL,'user',NULL,NULL),
(24,5,'dog','2','black','sss',NULL,'user',NULL,NULL),
(26,5,'cat','2','white','sss','male','user',NULL,NULL),
(28,6,'cow','2','white','sdfr','male','shop','10','20000');

/*Table structure for table `predict` */

DROP TABLE IF EXISTS `predict`;

CREATE TABLE `predict` (
  `pre_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `pet` varchar(100) DEFAULT NULL,
  `Sleeping_Patterns` varchar(100) DEFAULT NULL,
  `Activity_Patterns` varchar(100) DEFAULT NULL,
  `Exercise` varchar(100) DEFAULT NULL,
  `Diet` varchar(100) DEFAULT NULL,
  `Health_Issues` varchar(100) DEFAULT NULL,
  `Behavioral_Pattern` varchar(100) DEFAULT NULL,
  `Obedience_Level` varchar(100) DEFAULT NULL,
  `out` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`pre_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `predict` */

insert  into `predict`(`pre_id`,`user_id`,`pet`,`Sleeping_Patterns`,`Activity_Patterns`,`Exercise`,`Diet`,`Health_Issues`,`Behavioral_Pattern`,`Obedience_Level`,`out`) values 
(1,2,'Cats','12 to 16 hours a day crepuscular','More active at dawn and dusk','Morning Playtime (Dawn)','Main Meal','Obesity','Litter Box Use','Moderate','0'),
(2,2,'Cats','12 to 16 hours a day crepuscular','More active at dawn and dusk','Morning Playtime (Dawn)','Main Meal','Obesity','Litter Box Use','Moderate','0'),
(3,2,'Cats','12 to 16 hours a day crepuscular','More active at dawn and dusk','Morning Playtime (Dawn)','Main Meal','Obesity','Litter Box Use','Moderate','0'),
(4,2,'Cats','12 to 16 hours a day crepuscular','More active at dawn and dusk','Morning Playtime (Dawn)','Main Meal','Obesity','Litter Box Use','Moderate','0'),
(5,2,'Cats','12 to 16 hours a day crepuscular','More active at dawn and dusk','Morning Playtime (Dawn)','Main Meal','Obesity','Litter Box Use','Moderate','0');

/*Table structure for table `purchase_child` */

DROP TABLE IF EXISTS `purchase_child`;

CREATE TABLE `purchase_child` (
  `purchase_child_id` int(11) NOT NULL AUTO_INCREMENT,
  `purchase_master_id` int(11) DEFAULT NULL,
  `accessorie_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `qty` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`purchase_child_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `purchase_child` */

insert  into `purchase_child`(`purchase_child_id`,`purchase_master_id`,`accessorie_id`,`amount`,`qty`) values 
(5,2,5,'2000','2'),
(6,2,8,'4000','2'),
(7,3,5,'4000','2'),
(8,3,4,'40000','2'),
(9,4,5,'2000','2'),
(10,5,5,'2000','2');

/*Table structure for table `purchase_master` */

DROP TABLE IF EXISTS `purchase_master`;

CREATE TABLE `purchase_master` (
  `purchase_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`purchase_master_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `purchase_master` */

insert  into `purchase_master`(`purchase_master_id`,`user_id`,`total`,`date`,`status`) values 
(2,1,'6000','2024-05-24','paid'),
(3,1,'44000','2024-05-24','pending'),
(4,2,'2000','2024-06-17','paid'),
(5,2,'2000','2024-06-17','paid');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rate_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `rate` varchar(100) DEFAULT NULL,
  `review` varchar(1000) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rate_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rate_id`,`user_id`,`rate`,`review`,`image`,`date`) values 
(1,1,'2','I had a terrible experience at this restaurant. The staff was rude and unhelpful, and the food was mediocre at best. I would not recommend this place to anyoneI had a terrible experience at this restaurant. The staff was rude and unhelpful, and the food was mediocre at best. I would not recommend this place to anyoneI had a terrible experience at this restaurant. The staff was rude and unhelpful, and the food was mediocre at best. I would not recommend this place to anyone','static/images/303f39a6-ad63-40c4-8da3-91dfd4cfbf56blog-2.jpg','2024-05-24'),
(2,1,'3','I had a terrible experience at this restaurant. The staff was rude and unhelpful, and the food was mediocre at best. I would not recommend this place to anyoneI had a terrible experience at this restaurant. The staff was rude and unhelpful, and the food was mediocre at best. I would not recommend this place to anyoneI had a terrible experience at this restaurant. The staff was rude and unhelpful, and the food was mediocre at best. I would not recommend this place to anyone','static/images/3e55662b-3299-4cbe-af49-7d2f0fab84b049c135c9-1346-4f6f-b404-e001ab4a2b4ccat1.jpeg','2024-06-10'),
(3,1,'5','I had a terrible experience at this restaurant. The staff was rude and unhelpful, and the food was mediocre at best. I would not recommend this place to anyoneI had a terrible experience at this restaurant. The staff was rude and unhelpful, and the food was mediocre at best. I would not recommend this place to anyoneI had a terrible experience at this restaurant. The staff was rude and unhelpful, and the food was mediocre at best. I would not recommend this place to anyone','static/images/4c697370-d869-443f-a4cd-5126b4a18b4cabout.jpg','2024-05-24');

/*Table structure for table `sales_child` */

DROP TABLE IF EXISTS `sales_child`;

CREATE TABLE `sales_child` (
  `sales_child_id` int(11) NOT NULL AUTO_INCREMENT,
  `sales_master_id` int(11) DEFAULT NULL,
  `pet_id` int(11) DEFAULT NULL,
  `s_amount` varchar(100) DEFAULT NULL,
  `s_qty` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sales_child_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `sales_child` */

insert  into `sales_child`(`sales_child_id`,`sales_master_id`,`pet_id`,`s_amount`,`s_qty`) values 
(3,2,19,'4000','2'),
(4,3,28,'20000','1');

/*Table structure for table `sales_master` */

DROP TABLE IF EXISTS `sales_master`;

CREATE TABLE `sales_master` (
  `sales_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sales_master_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `sales_master` */

insert  into `sales_master`(`sales_master_id`,`user_id`,`total`,`date`,`status`) values 
(2,1,'4000','2024-05-24','paid'),
(3,1,'20000','2024-06-08','pending');

/*Table structure for table `shops` */

DROP TABLE IF EXISTS `shops`;

CREATE TABLE `shops` (
  `shop_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `shop_name` varchar(100) DEFAULT NULL,
  `owner_name` varchar(100) DEFAULT NULL,
  `file_upload` varchar(100) DEFAULT NULL,
  `s_place` varchar(100) DEFAULT NULL,
  `s_email` varchar(100) DEFAULT NULL,
  `s_phone` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`shop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `shops` */

insert  into `shops`(`shop_id`,`login_id`,`shop_name`,`owner_name`,`file_upload`,`s_place`,`s_email`,`s_phone`) values 
(2,4,'Matha\'s Angel Pet Shop','kuriakose','static/images/be6edbc3-870d-443b-bc82-4f042e1aeaeelic.jpg','Puthiyakavu','MathaAngel@gmail.com','6757576767'),
(3,12,'The Complete Pet Store','Babu','static/images/be6edbc3-870d-443b-bc82-4f042e1aeaeelic.jpg','Udayamperoor','complete@gmail.com ','2222223444'),
(7,23,'PET HOST','Ashika Marjan','static/images/be6edbc3-870d-443b-bc82-4f042e1aeaeelic.jpg','Maradu','pethost@gmail.com','9345434567'),
(12,6,'shop1','raju','static/images/18908fcd-a044-4b40-aba7-518164b94461user.jpg','ernakulam','shop1@gmail.com','2345678908'),
(13,10,'shop1','raju','static/images/89b73c77-66b9-4e86-a3ee-f04bcfd17c51crm er.jpg','ernakulam','abi@gmail.com','2345678908');

/*Table structure for table `slot_booking` */

DROP TABLE IF EXISTS `slot_booking`;

CREATE TABLE `slot_booking` (
  `slot_booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `vaccine_id` int(11) DEFAULT NULL,
  `booking_date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`slot_booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `slot_booking` */

insert  into `slot_booking`(`slot_booking_id`,`user_id`,`vaccine_id`,`booking_date`,`status`) values 
(1,1,0,'2023-12-17','pending'),
(2,1,0,'2023-12-17','added'),
(3,1,0,'2023-12-17','added'),
(4,1,0,'2023-12-17','added'),
(5,1,0,'2023-12-17','added'),
(6,1,0,'2023-12-17','added'),
(7,1,0,'2023-12-17','added'),
(8,1,1,'2023-12-17','accept'),
(9,1,1,'2023-12-17','added'),
(10,1,1,'2023-12-17','accept'),
(11,3,1,'2024-01-11','added'),
(12,3,5,'2024-02-23','added');

/*Table structure for table `slots` */

DROP TABLE IF EXISTS `slots`;

CREATE TABLE `slots` (
  `slot_id` int(11) NOT NULL AUTO_INCREMENT,
  `hospital_id` int(11) DEFAULT NULL,
  `vaccine_id` int(11) DEFAULT NULL,
  `slot` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`slot_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `slots` */

insert  into `slots`(`slot_id`,`hospital_id`,`vaccine_id`,`slot`,`quantity`) values 
(1,1,1,'2','20'),
(2,2,1,'1','40'),
(3,2,1,'2','20');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `specialization` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`,`specialization`) values 
(2,3,'anju','m','paravoor','2345678908','anju@gmail.com','grooming ');

/*Table structure for table `staff_assign` */

DROP TABLE IF EXISTS `staff_assign`;

CREATE TABLE `staff_assign` (
  `staff_assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `appointment_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_assign_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `staff_assign` */

insert  into `staff_assign`(`staff_assign_id`,`appointment_id`,`staff_id`,`date`,`status`) values 
(1,1,2,'2024-05-23','pending'),
(2,1,2,'2024-05-23','pending'),
(3,1,2,'2024-05-23','pending'),
(4,1,2,'2024-05-23','pending'),
(5,3,2,'2024-06-17','pending'),
(6,3,2,'2024-06-17','pending');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`user_id`,`login_id`,`first_name`,`last_name`,`phone`,`place`,`email`,`pincode`,`address`) values 
(1,5,'maya','j','1111111111','ernakulam','maya@gmail.com','777777','dsiuhnsj'),
(2,7,'anju','m','2345678908','Kottayam','anj@gmail.com','333333','rrtrdjsnkjn');

/*Table structure for table `vaccine` */

DROP TABLE IF EXISTS `vaccine`;

CREATE TABLE `vaccine` (
  `vaccine_id` int(11) NOT NULL AUTO_INCREMENT,
  `vaccine_name` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `details` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`vaccine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `vaccine` */

insert  into `vaccine`(`vaccine_id`,`vaccine_name`,`amount`,`details`) values 
(2,'Rabies','200','Rabies is a serious disease that can be fatal to both dogs and humans.All dogs should be vaccinated against rabies, and booster shots should be given every one to three years depending on state law.'),
(3,'Parvovirus','350','Parvovirus is a deadly disease that can affect dogs of all ages, but puppies are especially vulnerable.The virus attacks the gastrointestinal system, causing severe vomiting and diarrhoea. Parvovirus can also cause heart problems and death. All dogs should be vaccinated against parvovirus, with booster shots given every one to two years.'),
(4,'Distemper','450','Distemper is a highly contagious disease that affects the respiratory, gastrointestinal, and nervous systems of dogs.It can cause severe coughing, vomiting, diarrhoea, seizures, and death. Puppies are especially vulnerable to the disease. All dogs should be vaccinated against distemper, with booster shots given every one to two years.'),
(5,'Leptospirosis','900','Leptospirosis is a bacterial disease that affects the kidneys and liver of dogs. It can be transmitted through contact with contaminated water or soil.The disease can cause severe kidney damage and death. All dogs should be vaccinated against leptospirosis, with booster shots given every one to two years.'),
(6,'Infectious Canine Hepatitis','1000','Hepatitis is a viral disease that affects the liver of dogs. The symptoms can range from loss of appetite and thirst, fever and bleeding.It is usually spread through contact with contaminated or infected urine, saliva or faeces.'),
(7,'Coronavirus','1500','The canine coronavirus (CCoV) is a virus that can cause intestinal infections and abdominal discomfort in dogs.It is most commonly spread through close contact with other infected dogs, therefore, if your dog socialises with other dogs regularly');

/*Table structure for table `vet_appointment` */

DROP TABLE IF EXISTS `vet_appointment`;

CREATE TABLE `vet_appointment` (
  `vet_appointment_id` int(11) NOT NULL AUTO_INCREMENT,
  `pet_id` int(11) DEFAULT NULL,
  `hospital_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `booking_date` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`vet_appointment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `vet_appointment` */

insert  into `vet_appointment`(`vet_appointment_id`,`pet_id`,`hospital_id`,`date`,`booking_date`,`amount`,`status`) values 
(1,24,1,'2024-05-24','2024-05-29','6000','paid'),
(2,28,1,'2024-06-27','2024-06-08','0','pending'),
(3,24,1,'2024-06-28','2024-06-08','0','pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
