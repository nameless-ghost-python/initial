# удалил таблицу.
DROP TABLE `city-world`.`area`
# создал таблицу.
USE `city-world`;
CREATE TABLE IF NOT EXISTS `area` (
`id` int NOT NULL AUTO_INCREMENT primary key,
`area` varchar(35) NOT NULL);
# добавил значения в таблицу.
INSERT INTO `area` (area) VALUES("lata");
INSERT INTO `area` (area) VALUES("Moscow");
# добавляю внешние ключи к основной таблице.
ALTER TABLE `main_table`
ADD FOREIGN KEY (`id_city`)
REFERENCES `city` (`id`)
ON UPDATE CASCADE
ON DELETE RESTRICT;

ALTER TABLE `main_table`
ADD FOREIGN KEY (`id_nation`)
REFERENCES `nation` (`id`)
ON UPDATE CASCADE
ON DELETE RESTRICT;

ALTER TABLE `main_table`
ADD FOREIGN KEY (`id_region`)
REFERENCES `region` (`id`)
ON UPDATE CASCADE
ON DELETE RESTRICT;

ALTER TABLE `main_table`
ADD FOREIGN KEY (`id_area`)
REFERENCES `area` (`id`)
ON UPDATE CASCADE
ON DELETE RESTRICT;
# посмотрел индексы в главной таблице
SHOW INDEX FROM `main_table`;
# создаю индексы в таблицах город и страна, для поиска по названию
CREATE INDEX `name_city` ON `city` (`city`);
CREATE INDEX `name_nation` ON `nation` (`nation`);

SELECT * FROM `city`;
# смотрю данные по городу (имя, страна, регион). Страна в таком запросе непонятна, присутствует только код.
SELECT `name`, `countryCode`, `district` FROM `city`
# добавляю читаемые названия столбцов и добавляю из таблицы country название страны.
SELECT `city`.`name` AS `Город`, `country`.`name`  AS `Страна`, `city`.`district` AS `Регион` FROM `city`
LEFT JOIN `country`
ON `country`.`code` = `city`.`countryCode`
GROUP BY `countryCode`;
# Выбираю все города в Нидерландах. БД немного иная, поэтому выборку делал не по Московской области.
SELECT `id`, `Name`, `CountryCode` FROM `city`
WHERE `countrycode` = 'NLD';
# мотрю данные из таблицы о Персонале.
SELECT `id`, `id_department` AS `Отдел`, CONCAT(`name`, ' ', `surname`) AS `ФИО`, `salary` AS `Зарплата` 
FROM `worker`
#Смотрю максимальную зарплату.
SELECT `id`, `id_department` AS `Отдел`, CONCAT(`name`, ' ', `surname`) AS `ФИО`, `salary` AS `Максимальная ЗП` 
FROM `worker`
WHERE `salary` = (SELECT MAX(`salary`) FROM `worker`);
# Удаляю самого зажиточного работника.
DELETE FROM `personal`.`worker` WHERE (`id` = '2');
# Смотрю сколько всего людей во всех отделах.
SELECT COUNT(`id_department`) 
FROM `worker`
WHERE `id_department` IS NOT NULL;
# Cмотрю среднюю ЗП.
SELECT AVG(`salary`) AS `Средняя ЗП` FROM `worker`;
# Смотрю ФОТ по каждому отделу.
SELECT SUM(`salary`) AS 'ФОТ отдела', `department`.`depart` AS 'Отдел' FROM `worker`
LEFT JOIN `department`
ON `department`.`id` = `worker`.`id_department`
GROUP BY `id_department`;
