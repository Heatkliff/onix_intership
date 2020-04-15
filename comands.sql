CREATE DATABASE db_books;
use db_books;
CREATE TABLE tbl_topics (
    topic_id TINYINT PRIMARY KEY AUTO_INCREMENT,
    topic_name VARCHAR(100));
CREATE TABLE tbl_books (
    b_id VARCHAR(17) COMMENT 'ISBN код книги',
    b_name VARCHAR(255) NOT NULL COMMENT 'Название книги',
    b_author VARCHAR(255) COMMENT 'Автор',
    b_topic TINYINT COMMENT 'Код категории, к которой относится книга',
    b_price FLOAT(10,2) COMMENT 'Стоимость');
INSERT INTO `db_books`.`tbl_topics` (`topic_name`) VALUES ('классика');
INSERT INTO `db_books`.`tbl_topics` (`topic_name`) VALUES ('лирика');
INSERT INTO `db_books`.`tbl_topics` (`topic_name`) VALUES ('мемуары');
INSERT INTO `db_books`.`tbl_topics` (`topic_name`) VALUES ('психология');
INSERT INTO `db_books`.`tbl_topics` (`topic_name`) VALUES ('философия');
INSERT INTO `db_books`.`tbl_books` (`b_id`, `b_name`, `b_author`, `b_topic`, `b_price`) VALUES ('978-617-7559-71-8', 'Нож: лирика', 'Линдеманн Т.',(SELECT `topic_id` FROM `tbl_topics` WHERE `topic_name`='лирика'), '465.00');
INSERT INTO `db_books`.`tbl_books` (`b_id`, `b_name`, `b_author`, `b_topic`, `b_price`) VALUES ('ИБА12120', 'Масонство (Pietra Scura)', 'Мак-Налти У. Кирк',(SELECT `topic_id` FROM `tbl_topics` WHERE `topic_name`='психология'), '18400.00');
INSERT INTO `db_books`.`tbl_books` (`b_id`, `b_name`, `b_author`, `b_topic`, `b_price`) VALUES ('978-966-03-8307-4', 'В оточенні ідіотів, або Як зрозуміти тих, кого неможливо зрозуміти', 'Томас Эриксон',(SELECT `topic_id` FROM `tbl_topics` WHERE `topic_name`='философия'), '225.00');
INSERT INTO `db_books`.`tbl_books` (`b_id`, `b_name`, `b_author`, `b_topic`, `b_price`) VALUES ('978-5-17-088390-5', 'Мемуары гейши', 'Артур Голден',(SELECT `topic_id` FROM `tbl_topics` WHERE `topic_name`='мемуары'), '212.00');
INSERT INTO `db_books`.`tbl_books` (`b_id`, `b_name`, `b_author`, `b_topic`, `b_price`) VALUES ('ИБА12120', 'Масонство (Pietra Scura)', 'Мак-Налти У. Кирк',(SELECT `topic_id` FROM `tbl_topics` WHERE `topic_name`='классика'), '18400.00');
UPDATE tbl_books SET b_price = b_price * 0.10 + b_price WHERE b_price > 0;
DELETE FROM tbl_books WHERE b_price is NULL;