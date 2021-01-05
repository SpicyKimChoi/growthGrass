CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_name` varchar(255),
  `kakao_id` varchar(255)
);

CREATE TABLE `habbit` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `userid` int,
  `type` int,
  `color` varchar(255),
  `description` varchar(255)
);

CREATE TABLE `type` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

CREATE TABLE `log` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `habbit_id` int,
  `description` varchar(255),
  `date` varchar(255),
  `status` varchar(255)
);

CREATE TABLE `friendlist` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int,
  `friend_id` int
);

ALTER TABLE `habbit` ADD FOREIGN KEY (`userid`) REFERENCES `users` (`id`);

ALTER TABLE `log` ADD FOREIGN KEY (`habbit_id`) REFERENCES `habbit` (`id`);

ALTER TABLE `friendlist` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `friendlist` ADD FOREIGN KEY (`friend_id`) REFERENCES `users` (`id`);

ALTER TABLE `habbit` ADD FOREIGN KEY (`type`) REFERENCES `type` (`id`);
