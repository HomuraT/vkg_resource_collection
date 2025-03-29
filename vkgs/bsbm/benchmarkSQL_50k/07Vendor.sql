CREATE DATABASE IF NOT EXISTS `d2r` DEFAULT CHARACTER SET utf8;

USE `d2r`;

DROP TABLE IF EXISTS `vendor`;
CREATE TABLE `vendor` (
  `nr` int(11) primary key,
  `label` varchar(100) character set utf8 collate utf8_bin default NULL,
  `comment` varchar(2000) character set utf8 collate utf8_bin default NULL,
  `homepage` varchar(100) character set utf8 collate utf8_bin default NULL,
  `country` char(2) character set utf8 collate utf8_bin default NULL,
  `publisher` int(11),
  `publishDate` date
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

LOCK TABLES `vendor` WRITE;
ALTER TABLE `vendor` DISABLE KEYS;

INSERT INTO `vendor` VALUES (1,'succinctness blunting','vaporize plutonic eczemas sloppily indifferently geniture zymoplastic fetor ivied applies clutchy naturopathy subtracted debouched enforces contextually presider concertizes pushcart nonesuch wended twinight stander conventions denuclearizes corsages forgiver verbalize nervosa stinkard houseflies noiselessly earliest surveyable gladsome horary brunets forboding limberness nonaddictive blazoner publications floes aneroids fireball crucialness','http://www.vendor1.com/','JP',1,'2008-06-02'),(2,'exporter','freshness outface maledicts desires facelift unclerical betrothment bleating statecraft rewarmed ichorous outworks unjoined bloodying drownds calender zealotry boodling scintillometer loftiest hemorrhagic aerogram cymbalists hayers meadowsweets signalizes antidepressant ruralisms moneylenders capitalists pushovers','http://www.vendor2.com/','US',2,'2008-03-18');

ALTER TABLE `vendor` ENABLE KEYS;
UNLOCK TABLES;