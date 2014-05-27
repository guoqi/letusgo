-- phpMyAdmin SQL Dump
-- version 4.2.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2014-05-27 16:26:09
-- 服务器版本： 5.5.37-1
-- PHP Version: 5.5.12-2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `letusgo`
--

-- --------------------------------------------------------

--
-- 表的结构 `activity`
--

CREATE TABLE IF NOT EXISTS `activity` (
`aid` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `uid` int(11) NOT NULL,
  `intro` varchar(255) NOT NULL,
  `launch_t` datetime NOT NULL,
  `update_t` datetime NOT NULL,
  `start_t` datetime NOT NULL,
  `end_t` datetime NOT NULL,
  `status` smallint(6) NOT NULL,
  `limits` int(11) NOT NULL,
  `participants` int(11) NOT NULL,
  `voteups` int(11) NOT NULL,
  `longitude` float NOT NULL,
  `latitude` float NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `participant`
--

CREATE TABLE IF NOT EXISTS `participant` (
  `aid` int(11) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `review`
--

CREATE TABLE IF NOT EXISTS `review` (
`rid` int(11) NOT NULL,
  `content` mediumtext NOT NULL,
  `aid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `review_t` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE IF NOT EXISTS `user` (
`uid` int(11) NOT NULL,
  `tel` varchar(11) NOT NULL,
  `pwd` varchar(32) NOT NULL,
  `name` varchar(32) NOT NULL,
  `big_avatar` varchar(255) NOT NULL,
  `small_avatar` varchar(255) NOT NULL,
  `origin_avatar` varchar(255) NOT NULL,
  `sex` smallint(6) NOT NULL,
  `age` smallint(6) NOT NULL,
  `loc` varchar(255) NOT NULL,
  `reg_time` datetime NOT NULL,
  `last_login_t` datetime NOT NULL,
  `token` varchar(255) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`uid`, `tel`, `pwd`, `name`, `big_avatar`, `small_avatar`, `origin_avatar`, `sex`, `age`, `loc`, `reg_time`, `last_login_t`, `token`) VALUES
(1, '13260614509', '202cb962ac59075b964b07152d234b70', 'guoqi', '', '', '', 1, 20, '湖北武汉', '2014-05-27 00:00:00', '2014-05-27 16:19:13', 'pSp7adiPEE4Saw3c');

-- --------------------------------------------------------

--
-- 表的结构 `voteup`
--

CREATE TABLE IF NOT EXISTS `voteup` (
  `aid` int(11) NOT NULL,
  `uid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activity`
--
ALTER TABLE `activity`
 ADD PRIMARY KEY (`aid`), ADD KEY `uid` (`uid`);

--
-- Indexes for table `participant`
--
ALTER TABLE `participant`
 ADD KEY `aid` (`aid`), ADD KEY `uid` (`uid`);

--
-- Indexes for table `review`
--
ALTER TABLE `review`
 ADD PRIMARY KEY (`rid`), ADD KEY `aid` (`aid`), ADD KEY `uid` (`uid`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
 ADD PRIMARY KEY (`uid`), ADD UNIQUE KEY `tel` (`tel`);

--
-- Indexes for table `voteup`
--
ALTER TABLE `voteup`
 ADD KEY `aid` (`aid`), ADD KEY `uid` (`uid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activity`
--
ALTER TABLE `activity`
MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `review`
--
ALTER TABLE `review`
MODIFY `rid` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- 限制导出的表
--

--
-- 限制表 `activity`
--
ALTER TABLE `activity`
ADD CONSTRAINT `activity_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`);

--
-- 限制表 `participant`
--
ALTER TABLE `participant`
ADD CONSTRAINT `participant_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `activity` (`aid`),
ADD CONSTRAINT `participant_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`);

--
-- 限制表 `review`
--
ALTER TABLE `review`
ADD CONSTRAINT `review_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `activity` (`aid`),
ADD CONSTRAINT `review_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`);

--
-- 限制表 `voteup`
--
ALTER TABLE `voteup`
ADD CONSTRAINT `voteup_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `activity` (`aid`),
ADD CONSTRAINT `voteup_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
