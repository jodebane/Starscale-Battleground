CREATE TABLE `cards` (
  `id` int NOT NULL,
  `name` varchar(1000) NOT NULL,
  `tags` varchar(1000) NOT NULL,
  `resourcecost` int DEFAULT NULL,
  `ruletext` varchar(1000) DEFAULT NULL,
  `attackscore` int DEFAULT NULL,
  `hitpoints` int DEFAULT NULL,
  `removecost` int DEFAULT NULL,
  `conquercost` int DEFAULT NULL,
  `activationcondition` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
