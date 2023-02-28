CREATE DATABASE trips_db;
use trips_db;

CREATE TABLE trips (
    `trip_id` int NOT NULL AUTO_INCREMENT,
    `region` VARCHAR(255),
    `origin_coord` POINT,
    `destination_coord` POINT,
    `datetime` DATETIME,
    `datasource` VARCHAR(255),
    PRIMARY KEY (`trip_id`)
);


INSERT INTO `trips` (`region`, `origin_coord`, `destination_coord`, `datetime`, `datasource`)
VALUES 
  ('Prague', POINT(14.4973794438195, 50.00136875782316), POINT(14.43109483523328, 50.04052930943246), '2018-05-28 09:03:40', 'funny_car'),
  ('Turin', POINT(7.672837913286881, 44.9957109242058), POINT(7.720368637535126, 45.06782385393849), '2018-05-21 02:54:04', 'baba_car'),
  ('Prague', POINT(14.32427345662177, 50.00002074358429), POINT(14.47767895969969, 50.09339790740321), '2018-05-13 08:52:25', 'cheap_mobile'),
  ('Turin', POINT(7.541509189114433, 45.09160503827746), POINT(7.74528653441973, 45.02628598341506), '2018-05-06 09:49:16', 'bad_diesel_vehicles'),
  ('Turin', POINT(7.614078119815749, 45.13433106465422), POINT(7.527497142312585, 45.03335051325654), '2018-05-23 12:45:54', 'pt_search_app');
