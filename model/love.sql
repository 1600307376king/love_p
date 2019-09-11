/*
Navicat MySQL Data Transfer

Source Server         : blog
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : love

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2019-09-11 17:18:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for analysis
-- ----------------------------
DROP TABLE IF EXISTS `analysis`;
CREATE TABLE `analysis` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of analysis
-- ----------------------------
