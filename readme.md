# Query
### Table Transcation
```commandline
CREATE TABLE `transaction` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`user_id` INT(11) DEFAULT NULL,
	`created_at` DATETIME DEFAULT CURRENT_TIMESTAMP(),
	`modified_at` DATETIME DEFAULT CURRENT_TIMESTAMP(),
	`status` INT(11) DEFAULT 10,
	`total` BIGINT(20) DEFAULT 0,
	PRIMARY KEY (`id`)
);
```

## Table Transaction Item
```commandline
CREATE TABLE `transaction_item` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`user_id` INT(11) DEFAULT NULL,
	`transaction_id` INT(11) DEFAULT	NULL,
	`created_at` DATETIME DEFAULT CURRENT_TIMESTAMP(),
	`modified_at` DATETIME DEFAULT CURRENT_TIMESTAMP(),
	`product_id` INT(11) DEFAULT	NULL,
	`product_name` VARCHAR(200) DEFAULT	NULL,
	`status` INT(11) DEFAULT 10,
	`price` BIGINT(20) DEFAULT 0,
	`qty` INT(11) DEFAULT 0,
	PRIMARY KEY (`id`)
);
```
### Table Product
```commandline
CREATE TABLE `product` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`barcode` VARCHAR(200) DEFAULT NULL,
	`name` VARCHAR(200) DEFAULT NULL,
	`price` BIGINT(20) DEFAULT NULL,
	`is_active` TINYINT(4) DEFAULT NULL,
	`created_at` DATETIME DEFAULT CURRENT_TIMESTAMP(),
	`modified_at` DATETIME DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`),
	KEY `product_barcode` (`barcode`)
);
```