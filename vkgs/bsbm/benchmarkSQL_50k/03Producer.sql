CREATE DATABASE IF NOT EXISTS `d2r` DEFAULT CHARACTER SET utf8;

USE `d2r`;

DROP TABLE IF EXISTS `producer`;
CREATE TABLE `producer` (
  `nr` int(11) primary key,
  `label` varchar(100) character set utf8 collate utf8_bin default NULL,
  `comment` varchar(2000) character set utf8 collate utf8_bin default NULL,
  `homepage` varchar(100) character set utf8 collate utf8_bin default NULL,
  `country` char(2) character set utf8 collate utf8_bin default NULL,
  `publisher` int(11),
  `publishDate` date
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

LOCK TABLES `producer` WRITE;
ALTER TABLE `producer` DISABLE KEYS;

INSERT INTO `producer` VALUES (1,'hulkier perfectionism castrato','evolves playthings rebind unfree alliums serotypes splotches unholily encampment bustlers whitecap heavyhearted ideates thermonuclear peonism idyl humanistic impossibilities cornstalks goaltenders','http://www.Producer1.com/','DE',1,'2003-06-15'),(2,'presbyter grippes','tuesdays finagled chastities stimulants accelerating valences bioassayed unruled trooped caponizing fantails reexperienced catamaran woodworm cisterns bartended refinished assimilation succours sliced holstered underscoring denims unsnarl fabling necrotize dumpings awkwardness agitating neediest comparer hides infectiously battler quietly bumpy assignors hotted centered malevolence teatime ungracious heisting floras hierarch brushier relabeled distributee pettish','http://www.Producer2.com/','US',2,'2001-10-12');

ALTER TABLE `producer` ENABLE KEYS;
UNLOCK TABLES;