-- phpMyAdmin SQL Dump
-- version 4.0.8
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 30, 2018 at 03:47 PM
-- Server version: 5.7.14-log
-- PHP Version: 5.4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `2712576789_afangaskraning`
--

-- --------------------------------------------------------

--
-- Table structure for table `namskeid`
--

CREATE TABLE IF NOT EXISTS `namskeid` (
  `namskeid_id` int(11) NOT NULL AUTO_INCREMENT,
  `afangaheiti` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`namskeid_id`),
  UNIQUE KEY `afangaheiti` (`afangaheiti`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `namskeid`
--

INSERT INTO `namskeid` (`namskeid_id`, `afangaheiti`) VALUES
(1, 'FORR1FG05AU'),
(2, 'FORR2FA05BU'),
(3, 'FORR2HF05CU'),
(9, 'GAGN1NG05AU'),
(4, 'KEST1TR05AU'),
(5, 'KEST1TR05BU'),
(6, 'KEST2TR05CU');

-- --------------------------------------------------------

--
-- Table structure for table `notendur`
--

CREATE TABLE IF NOT EXISTS `notendur` (
  `notandi_id` int(11) NOT NULL AUTO_INCREMENT,
  `nafn` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`notandi_id`),
  UNIQUE KEY `nafn` (`nafn`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=38 ;

--
-- Dumping data for table `notendur`
--

INSERT INTO `notendur` (`notandi_id`, `nafn`) VALUES
(1, 'Abdelaziz Ghazal'),
(5, 'Anna Sigurðardóttir'),
(7, 'Björn Jónsson'),
(6, 'Emil Gautur Emilsson'),
(28, 'Eyvindur Jónsson'),
(24, 'Finnur Jónsson'),
(10, 'Geir Sigursson'),
(36, 'Grettir Sterki'),
(11, 'Gunnar Þórunnarson'),
(4, 'Kári Konráðsson'),
(14, 'Karl Gunnarsson'),
(8, 'Kjartan Konráðsson'),
(12, 'Konráð Guðmundsson'),
(13, 'Ólafur Guðmundsson'),
(9, 'Ólafur Konráðsson'),
(3, 'Rósa Ólafsdóttir'),
(2, 'Sigríður Sturlaugsdóttir'),
(15, 'Sigurður Rögnvaldur Ragnarsson');

-- --------------------------------------------------------

--
-- Table structure for table `skradir`
--

CREATE TABLE IF NOT EXISTS `skradir` (
  `notandi_id` int(11) NOT NULL,
  `namskeid_id` int(11) NOT NULL,
  PRIMARY KEY (`notandi_id`,`namskeid_id`),
  KEY `namskeid_id` (`namskeid_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `skradir`
--

INSERT INTO `skradir` (`notandi_id`, `namskeid_id`) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 2),
(7, 2),
(8, 2),
(9, 2),
(11, 2),
(12, 2),
(10, 3),
(12, 3),
(13, 3),
(14, 3),
(15, 3),
(12, 4);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `skradir`
--
ALTER TABLE `skradir`
  ADD CONSTRAINT `namskeid_idfk_1` FOREIGN KEY (`notandi_id`) REFERENCES `notendur` (`notandi_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `notandi_idfk_2` FOREIGN KEY (`namskeid_id`) REFERENCES `namskeid` (`namskeid_id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
