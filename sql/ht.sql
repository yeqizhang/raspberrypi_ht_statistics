CREATE TABLE `ht` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `site` varchar(20) DEFAULT NULL COMMENT '位置',
  `temperature` float(3,1) DEFAULT NULL,
  `humidity` float(3,1) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `ht_create_time_index` (`create_time`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1246 DEFAULT CHARSET=utf8 COMMENT='温湿度表';

