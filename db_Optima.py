-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sept 21, 2021 at 17:22 ABCMeta
-- Server version : 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT = @@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS = @@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_CHARACTER_COLLATION_CONNECTION = @@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: 'db_Optima'
--

-- --------------------------------------

--
-- Table structure for table 'cb'
--

CREATE TABLE 'cb'('nodin' varchar(100) NOT NULL, 'nocb' varchar(100) NOT NULL, 'perihal' varchar(100) NOT NULL, 'tanggal' varchar(100) NOT NULL)
ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- --------------------------------------

--
-- Table structure for table 'center'
--

CREATE TABLE 'center'('id_mitra' varchar(100) NOT NULL, 'nama_project' varchar(100) NOT NULL, 'nilai' varchar(100) NOT NULL, 'tanggal' varchar(100) NOT NULL)
ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- --------------------------------------

--
-- Table structure for table 'lpo'
--

CREATE TABLE 'lpo'('nama_project' varchar(100) NOT NULL, 'nocb' varchar(100) NOT NULL, 'witel' varchar(100) NOT NULL, 'paket' varchar(100) NOT NULL, 'sto' varchar(100) NOT NULL, 'nilai' int(11) NOT NULL)
ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- --------------------------------------

--
-- Table structure for table 'mitra'
--

CREATE TABLE 'mitra'('id_mitra' varchar(100) NOT NULL, 'nama_mitra' varchar(100) NOT NULL, 'nama_pic' varchar(100) NOT NULL, 'no_telp' varchar(100) NOT NULL, 'email' varchar(100) NOT NULL, 'pass' varchar(100) NOT NULL)
ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- --------------------------------------

--
-- Table structure for table 'permintaan'
--

CREATE TABLE 'permintaan'('nodin' varchar(100) NOT NULL, 'pemohon' varchar(100) NOT NULL, 'perihal' varchar(100) NOT NULL, 'tanggal' varchar(100) NOT NULL)
ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;
COMMIT;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT = @@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS = @@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_CHARACTER_COLLATION_CONNECTION = @@COLLATION_CONNECTION */;