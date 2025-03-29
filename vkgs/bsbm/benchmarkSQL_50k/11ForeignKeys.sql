CREATE DATABASE IF NOT EXISTS `d2r` DEFAULT CHARACTER SET utf8;

USE `d2r`;
-- Foreign Key Constraints

-- 转换所有相关表为InnoDB引擎
ALTER TABLE offer ENGINE=InnoDB;
ALTER TABLE person ENGINE=InnoDB;
ALTER TABLE producer ENGINE=InnoDB;
ALTER TABLE product ENGINE=InnoDB;
ALTER TABLE productfeature ENGINE=InnoDB;
ALTER TABLE productfeatureproduct ENGINE=InnoDB;
ALTER TABLE producttype ENGINE=InnoDB;
ALTER TABLE producttypeproduct ENGINE=InnoDB;
ALTER TABLE review ENGINE=InnoDB;
ALTER TABLE vendor ENGINE=InnoDB;

-- offer table foreign keys
ALTER TABLE `offer` ADD CONSTRAINT `offer_producer_nr_fk` FOREIGN KEY (`producer`) REFERENCES `producer` (`nr`);
ALTER TABLE `offer` ADD CONSTRAINT `offer_product_nr_fk` FOREIGN KEY (`product`) REFERENCES `product` (`nr`);
ALTER TABLE `offer` ADD CONSTRAINT `offer_vendor_nr_fk` FOREIGN KEY (`vendor`) REFERENCES `vendor` (`nr`);

-- productfeatureproduct table foreign keys
ALTER TABLE `productfeatureproduct` ADD CONSTRAINT `productfeatureproduct_product_nr_fk` FOREIGN KEY (`product`) REFERENCES `product` (`nr`);
ALTER TABLE `productfeatureproduct` ADD CONSTRAINT `productfeatureproduct_productfeature_nr_fk` FOREIGN KEY (`productFeature`) REFERENCES `productfeature` (`nr`);

-- producttypeproduct table foreign keys
ALTER TABLE `producttypeproduct` ADD CONSTRAINT `producttypeproduct_product_nr_fk` FOREIGN KEY (`product`) REFERENCES `product` (`nr`);
ALTER TABLE `producttypeproduct` ADD CONSTRAINT `producttypeproduct_producttype_nr_fk` FOREIGN KEY (`productType`) REFERENCES `producttype` (`nr`);

-- review table foreign keys
ALTER TABLE `review` ADD CONSTRAINT `review_person_nr_fk` FOREIGN KEY (`person`) REFERENCES `person` (`nr`);
ALTER TABLE `review` ADD CONSTRAINT `review_producer_nr_fk` FOREIGN KEY (`producer`) REFERENCES `producer` (`nr`);
ALTER TABLE `review` ADD CONSTRAINT `review_product_nr_fk` FOREIGN KEY (`product`) REFERENCES `product` (`nr`);
