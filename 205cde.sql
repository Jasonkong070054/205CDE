-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 11, 2021 at 01:05 PM
-- Server version: 8.0.23-0ubuntu0.20.04.1
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `205cde`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `pdtid` int NOT NULL,
  `pdtname` varchar(255) NOT NULL,
  `pdtprice` smallint NOT NULL,
  `pdtimage` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `orderid` int NOT NULL,
  `pdtid` int NOT NULL,
  `pdtname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `pdtprice` smallint NOT NULL,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phoneNo` int NOT NULL,
  `address` varchar(255) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`orderid`, `pdtid`, `pdtname`, `pdtprice`, `username`, `phoneNo`, `address`, `date`) VALUES
(1, 4, 'Logitech G733 Lightspeed Wireless RGB Gaming Headset', 1099, 'user', 12345678, 'Tko', '2021-04-22 22:35:39'),
(2, 9, 'HyperX Cloud Revolver Gaming Headset', 1099, 'user', 12345678, 'Tko', '2021-04-23 18:41:25'),
(3, 1, 'Logitech Pro X Wireless Lightspeed Gaming Headset', 1799, 'user', 12345678, 'Tko', '2021-04-24 16:29:36');

-- --------------------------------------------------------

--
-- Table structure for table `orders2`
--

CREATE TABLE `orders2` (
  `orderid` int NOT NULL,
  `pdtsname` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pdtsprice` int NOT NULL,
  `username` varchar(20) NOT NULL,
  `phoneNo` int NOT NULL,
  `address` varchar(255) NOT NULL,
  `date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `pdtid` int NOT NULL,
  `pdtname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pdtprice` smallint NOT NULL,
  `pdtbrand` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pdtdetail` varchar(255) NOT NULL,
  `pdtimage` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`pdtid`, `pdtname`, `pdtprice`, `pdtbrand`, `pdtdetail`, `pdtimage`) VALUES
(1, 'Logitech Pro X Wireless Lightspeed Gaming Headset', 1799, 'logitech', 'DESIGNED WITH PROS. ENGINEERED TO WIN. Step up to the pro-grade communications and precision audio you need to win, all with the freedom and mobility of LIGHTSPEED wireless.', 'Logitech_ProX_Wireless.jpg'),
(2, 'Logitech Pro X Wired Gaming Headset with Blue VO!CE', 1199, 'logitech', 'PRO GRADE PERFORMANCE: Designed in collaboration with and for pros for advanced communications and precision audio.', 'Logitech_ProX_Wired.jpg'),
(3, 'Logitech G733 K/DA Lightspeed Wireless RGB Gaming Headset', 1199, 'logitech', 'G733 is wireless and designed for comfort. And it’s outfitted with all the surround sound, voice filters, and advanced lighting you need to look, sound, and play with more style than ever.', 'Logitech_G733KDA.jpg'),
(4, 'Logitech G733 Lightspeed Wireless RGB Gaming Headset', 1099, 'logitech', 'G733 is wireless and designed for comfort. And it’s outfitted with all the surround sound, voice filters, and advanced lighting you need to look, sound, and play with more style than ever.', 'Logitech_G733.jpg'),
(5, 'Razer Kraken V3 X Wired USB Gaming Headset', 549, 'razer', 'ULTRA-LIGHT COMFORT FOR GAMING IMMERSION Feel complete immersion without feeling the weight. Upgraded with patented Razer™ TriForce drivers for incredibly realistic sound, it’s time to lose yourself with an audio experience that’s always a win.', 'Razer_KrakenV3X.jpg'),
(6, 'Razer Kraken X USB Digital Surround Sound Gaming Headset', 499, 'razer', 'ULTRA-LIGHT COMFORT FOR NON-STOP GAMING Feel complete gaming immersion without feeling the weight. With its comfortable, lightweight design and superior audio, you’ll never want your gaming marathons to end.', 'Razer_KrakenXUSB.png'),
(7, 'Razer BlackShark V2 Multi-platform wired esports headset', 790, 'razer', 'THE SOUND OF ESPORTS If esports is everything, then give it your all with the Razer BlackShark V2. With an esports headset that’s a triple threat of amazing audio, superior mic clarity and supreme sound isolation, your time to turn pro is now.', 'Razer_BlackSharkV2.jpg'),
(8, 'Razer BlackShark V2 X Multi-platform wired esports headset', 479, 'razer', 'THE SOUND OF ESPORTS Face the competition head-on with a lightweight esports headset that thrives under pressure. Razer BlackShark V2 X—a triple threat of amazing audio, superior mic clarity and supreme sound isolation that’s approved by pros.', 'Razer_BlackSharkV2X.jpg'),
(9, 'HyperX Cloud Revolver Gaming Headset', 1099, 'hyperx', 'The HyperX Cloud Revolver™ line is premium-grade gear, meticulously designed to meet the demands of the elite PC or console gamer. Next-gen drivers separate the lows, mids, and highs to crank out precisely positioned, high-quality sound.', 'HyperX_Revolver.jpg'),
(10, 'HyperX Cloud Gaming Headset Cloud II Wireless ', 1299, 'hyperx', 'The HyperX Cloud was built to be an ultra-comfortable gaming headset with amazing sound.', 'HyperX_CloudII.jpg'),
(11, 'HyperX Cloud Stinger Wired Gaming Headset ', 399, 'hyperx', 'HyperX Cloud Stinger™ S immerses you in the game with virtual 7.1 surround1 sound via NGENUITY software. 50mm directional drivers pump out high-quality sound with pinpoint audio precision. ', 'HyperX_CloudStinger.png'),
(12, 'HyperX Cloud Stinger Wireless Gaming Headset', 699, 'hyperx', 'HyperX Cloud Stinger™ S immerses you in the game with virtual 7.1 surround1 sound via NGENUITY software. 50mm directional drivers pump out high-quality sound with pinpoint audio precision. ', 'HyperX_CloudStingerWireless.jpg'),
(13, 'HyperX Cloud Stinger S Gaming Headset', 499, 'hyperx', 'HyperX Cloud Stinger™ S immerses you in the game with virtual 7.1 surround1 sound via NGENUITY software. 50mm directional drivers pump out high-quality sound with pinpoint audio precision. ', 'HyperX_CloudStingerS.jpg'),
(14, 'SteelSeries ARCTIS 9 Wireless Gaming Headset for PC', 1599, 'steelseries', 'The Arctis 9 dual wireless headset combines high performance 2.4 GHz wireless for premium gaming audio on PC and PlayStation, with the convenience of simultaneous Bluetooth connectivity for everything else.', 'Steelseries_Arctis9Wireless.jpg'),
(15, 'SteelSeries ARCTIS 7 Wireless Gaming Headset for PC', 1399, 'steelseries', 'The most awarded wireless gaming headset ever', 'Steelseries_Arctis7.jpg'),
(16, 'SteelSeries ARCTIS 5 2019 Edition (Surround Sound RGB Gaming Headset)', 799, 'steelseries', 'Designed exclusively for PC gaming. Specifically designed for the PC Gamer, Arctis 5 combines independent game.', 'Steelseries_Arctis5.jpg'),
(17, 'SteelSeries ARCTIS 3 2019 Edition', 649, 'steelseries', 'The best headset for everywhere you game. Designed for everywhere you game, with superior sound, comfort and style on all gaming platforms, including PC, PlayStation, Xbox One, Nintendo Switch, VR and mobile via detachable 3.5mm cables.', 'Steelseries_Arctis3.jpg'),
(18, 'SteelSeries ARCTIS Pro Wireless', 2799, 'steelseries', 'High fidelity audio comes to gaming for the first time. Hi-res capable speaker drivers and a lossless and lag-free wireless solution make Arctis Pro Wireless the only true wireless high fidelity gaming audio system.', 'Steelseries_ArctisProWireless.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE `question` (
  `qid` int NOT NULL,
  `userid` int NOT NULL,
  `username` varchar(20) NOT NULL,
  `question` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`qid`, `userid`, `username`, `question`) VALUES
(1, 2, 'user', 'testing sending question');

-- --------------------------------------------------------

--
-- Table structure for table `reply`
--

CREATE TABLE `reply` (
  `rid` int NOT NULL,
  `qid` int NOT NULL,
  `userid` int NOT NULL,
  `reply` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `question` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `reply`
--

INSERT INTO `reply` (`rid`, `qid`, `userid`, `reply`, `question`) VALUES
(1, 1, 2, 'testing success', 'testing sending question'),
(2, 2, 2, 'hello i am admin', 'hello i am user');

-- --------------------------------------------------------

--
-- Table structure for table `testuser`
--

CREATE TABLE `testuser` (
  `username` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `testuser`
--

INSERT INTO `testuser` (`username`, `email`, `password`) VALUES
('testuser1', 'testuser1@gmail.com', '123'),
('testuser2', 'testuser2@gmail.com', '1234'),
('chunfungk', 'chunfungk@gmail.com', 'Jason070054'),
('testuser3', 'testuser3@gmail.com', '12345'),
('testuser4', 'testuser4@gmail.com', 'testuser4'),
('user1', 'user1@gmail.com', 'user1');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `userid` int NOT NULL,
  `username` varchar(20) NOT NULL,
  `useremail` varchar(100) NOT NULL,
  `userpassword` varchar(20) NOT NULL,
  `address` varchar(255) NOT NULL,
  `region` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `phoneNo` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`userid`, `username`, `useremail`, `userpassword`, `address`, `region`, `phoneNo`) VALUES
(1, 'admin', 'admin@gmail.com', 'admin', 'admin', 'Kowloon', 12345678),
(2, 'user', 'user@gmail.com', 'user', 'Tko', 'New Territories', 12345678),
(3, 'user1', 'user1@gmail.com', 'user1', 'user1', 'Hong Kong Island', 11111111);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`orderid`);

--
-- Indexes for table `orders2`
--
ALTER TABLE `orders2`
  ADD PRIMARY KEY (`orderid`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`pdtid`);

--
-- Indexes for table `question`
--
ALTER TABLE `question`
  ADD PRIMARY KEY (`qid`);

--
-- Indexes for table `reply`
--
ALTER TABLE `reply`
  ADD PRIMARY KEY (`rid`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `orderid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `orders2`
--
ALTER TABLE `orders2`
  MODIFY `orderid` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `pdtid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `question`
  MODIFY `qid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `reply`
--
ALTER TABLE `reply`
  MODIFY `rid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `userid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
