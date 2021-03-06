-- TALENT ROLES
INSERT INTO ROLE (role,priority) VALUES ('Host',1);
INSERT INTO ROLE (role,priority) VALUES ('Co-Host',2);
INSERT INTO ROLE (role,priority) VALUES ('Analyst',3);
INSERT INTO ROLE (role,priority) VALUES ('Commentator',3);
INSERT INTO ROLE (role,priority) VALUES ('Observer',4);
INSERT INTO ROLE (role,priority) VALUES ('Interviewer',4);
INSERT INTO ROLE (role,priority) VALUES ('Content Creator',5);
INSERT INTO ROLE (role,priority) VALUES ('Newbie Stream',5);
INSERT INTO ROLE (role,priority) VALUES ('Interpreter',5);
INSERT INTO ROLE (role,priority) VALUES ('Statistician',5);

-- TALENTS IN PLAYERS
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('Sheever','Jorien','van der Heijden','NL');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('Fogged','Ioannis','Loucas','US');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('Capitalist','Austin','Walsh','US');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('ODPixel','Owen','Davies','GB');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('Blitz','William','Lee','US');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('GoDz','David','Parker','AU');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('Lyrical','Gabriel','Cruz','US');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('WinteR','Chan Litt','Binn','MY');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('Starsky','Boris','Staroselsky','RU');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('Mag~','Andrey','Chipenko','QA');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('Iceberg','Bogdan','Vasylenko','QA');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('TpoH','Maxim','Vernikov','RU');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('DkPhobos','Alexander','Kucheria','QA');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('CaspeRRR','Roman','Lepokhin','QA');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('Bafikk','Aleksey','Bafadarov','QA');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('Droog','Dmitry','Chumachenko','QA');
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country)
VALUES ('Feaver','Oleg','Skarzhinsky','QA');

-- TOURNAMENTS
INSERT INTO TOURNAMENT (tr_name,tr_date,tr_enddate)
VALUES ('SL i-League Invitational Season 3','2017-10-12','2017-10-15');
INSERT INTO TOURNAMENT (tr_name,tr_date,tr_enddate)
VALUES ('PGL Open Bucharest','2017-10-19','2017-10-22');
INSERT INTO TOURNAMENT (tr_name,tr_date,tr_enddate)
VALUES ('ESL One Hamburg 2017','2017-10-26','2017-10-29');
INSERT INTO TOURNAMENT (tr_name,tr_date,tr_enddate)
VALUES ('AMD SAPPHIRE Dota PIT League','2017-11-02','2017-11-05');
INSERT INTO TOURNAMENT (tr_name,tr_date,tr_enddate)
VALUES ('Perfect World Masters','2017-11-19','2017-11-26');
INSERT INTO TOURNAMENT (tr_name,tr_date,tr_enddate)
VALUES ('ROG DreamLeague Season 8','2017-12-01','2017-12-03');
INSERT INTO TOURNAMENT (tr_name,tr_date,tr_enddate)
VALUES ('MDL Macau','2017-12-08','2017-12-10');
INSERT INTO TOURNAMENT (tr_name,tr_date,tr_enddate)
VALUES ('DOTA Summit 8','2017-12-13','2017-12-17');
INSERT INTO TOURNAMENT (tr_name,tr_date,tr_enddate)
VALUES ('Captains Draft 4.0','2018-01-04','2018-01-07');

-- TALENTS
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'Sheever'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Host'),
       'EN');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'Fogged'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Commentator'),
       'EN');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'Capitalist'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Commentator'),
       'EN');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'ODPixel'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Commentator'),
       'EN');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'Blitz'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Commentator'),
       'EN');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'GoDz'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Analyst'),
       'EN');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'Lyrical'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Analyst'),
       'EN');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'WinteR'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Analyst'),
       'EN');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'Starsky'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Host'),
       'RU');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'CaspeRRR'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Commentator'),
       'RU');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'Bafikk'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Commentator'),
       'RU');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'Droog'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Commentator'),
       'RU');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'Feaver'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Commentator'),
       'RU');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'Mag~'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Analyst'),
       'RU');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'Iceberg'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Analyst'),
       'RU');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'TpoH'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Analyst'),
       'RU');
INSERT INTO TALENT(p_id ,tr_id,rl_id,lang)
VALUES((SELECT p_id from PLAYER WHERE p_nick = 'DkPhobos'),
       (SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
       (SELECT rl_id FROM ROLE WHERE role = 'Analyst'),
       'RU');

-- TEAMS
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('Evil Geniuses','EG',0,'2011-10-24');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('compLexity Gaming','coL',0,'2012-02-16');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('Immortals','IMT',0,'2017-09-13');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('Digital Chaos','DC',0,'2015-08-24');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('OpTic Gaming','OpTic',0,'2017-09-26');
INSERT INTO TEAM (t_name,t_tag,t_region)
    VALUES ('Team Leviathan','LvT',0);
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('VGJ.Storm','VGJ.Storm',0,'2017-09-06');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('SG e-sports','SG',1,'2016-11-13');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('Wheel Whreck While Whistling','Wheel',0,'2014-01-01');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('Team Liquid','Liquid',2,'2012-12-06');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('Team Secret','Secret',2,'2014-08-27');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('OG','OG',2,'2015-10-31');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('mousesports ','mouz',2,'2011-12-05');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('Alliance','[A]',2,'2013-04-12');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('HellRaisers','HR',2,'2014-08-29');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('Team Kinguin','Kinguin',2,'2015-05-05');
INSERT INTO TEAM (t_name,t_tag,t_region)
    VALUES ('Mineski','Mski',5);
INSERT INTO TEAM (t_name,t_tag,t_region)
    VALUES ('Fnatic','Fnatic',5);
INSERT INTO TEAM (t_name,t_tag,t_region)
    VALUES ('TNC Pro Team','TNC',5);
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('Virtus.pro','VP',3,'2003-01-01');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('Newbee','Newbee',4,'2014-02-13');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('Vici Gaming','VG',4,'2012-09-21');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('LGD Gaming','LGD',4,'2009-01-01');
INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
    VALUES ('Natus Vincere','NAVI',3,'2010-10-22');

-- PARTICIPANT
INSERT INTO PARTICIPANT (tr_id,t_id)
VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
        (SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'));
INSERT INTO PARTICIPANT (tr_id,t_id)
VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
        (SELECT t_id FROM TEAM WHERE t_name LIKE '%Newbee%'));
INSERT INTO PARTICIPANT (tr_id,t_id)
VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
        (SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'));
INSERT INTO PARTICIPANT (tr_id,t_id)
VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
        (SELECT t_id FROM TEAM WHERE t_name LIKE '%Natus%'));
INSERT INTO PARTICIPANT (tr_id,t_id)
VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
        (SELECT t_id FROM TEAM WHERE t_name LIKE '%compLexity%'));
INSERT INTO PARTICIPANT (tr_id,t_id)
VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
        (SELECT t_id FROM TEAM WHERE t_name LIKE '%SG e-sports%'));
INSERT INTO PARTICIPANT (tr_id,t_id)
VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
        (SELECT t_id FROM TEAM WHERE t_name LIKE '%Vici%'));
INSERT INTO PARTICIPANT (tr_id,t_id)
VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),
        (SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'));

-- PLAYERS
INSERT INTO PLAYER (p_nick) VALUES ('Ace');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Ace'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),
            '2017-09-05',1,False);
INSERT INTO PLAYER (p_nick) VALUES ('MidOne');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'MidOne'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),
            '2016-08-27',2,False);
INSERT INTO PLAYER (p_nick) VALUES ('Fata');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Fata'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),
            '2017-09-05',3,False);
INSERT INTO PLAYER (p_nick) VALUES ('YapzOr');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'YapzOr'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),
            '2017-05-04',4,False);
INSERT INTO PLAYER (p_nick) VALUES ('Puppey');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Puppey'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),
            '2014-08-27',5,True);

INSERT INTO PLAYER (p_nick) VALUES ('MATUMBAMAN');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'MATUMBAMAN'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),
            '2015-10-09',1,False);
INSERT INTO PLAYER (p_nick) VALUES ('Miracle-');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Miracle-'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),
            '2016-09-16',2,False);
INSERT INTO PLAYER (p_nick) VALUES ('MinD_ContRoL');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'MinD_ContRoL'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),
            '2015-10-09',3,False);
INSERT INTO PLAYER (p_nick) VALUES ('GH');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'GH'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),
            '2017-01-02',4,False);
INSERT INTO PLAYER (p_nick) VALUES ('KuroKy');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'KuroKy'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),
            '2015-10-09',5,True);

INSERT INTO PLAYER (p_nick) VALUES ('RAMZES666');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'RAMZES666'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Virtus%'),
            '2016-08-04',1,False);
INSERT INTO PLAYER (p_nick) VALUES ('No[o]ne');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'No[o]ne'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Virtus%'),
            '2016-08-04',2,False);
INSERT INTO PLAYER (p_nick) VALUES ('9pasha');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = '9pasha'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Virtus%'),
            '2016-08-04',3,False);
INSERT INTO PLAYER (p_nick) VALUES ('Lil');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Lil'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Virtus%'),
            '2016-08-04',4,False);
INSERT INTO PLAYER (p_nick) VALUES ('Solo');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Solo'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Virtus%'),
            '2016-08-04',5,True);

INSERT INTO PLAYER (p_nick) VALUES ('Moogy');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Moogy'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Newbee%'),
            '2016-09-17',1,False);
INSERT INTO PLAYER (p_nick) VALUES ('Sccc');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Sccc'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Newbee%'),
            '2016-09-17',2,False);
INSERT INTO PLAYER (p_nick) VALUES ('kpii');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'kpii'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Newbee%'),
            '2016-03-25',3,False);
INSERT INTO PLAYER (p_nick) VALUES ('Kaka');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Kaka'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Newbee%'),
            '2016-03-25',4,False);
INSERT INTO PLAYER (p_nick) VALUES ('Faith');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Faith'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Newbee%'),
            '2016-09-17',5,True);

INSERT INTO PLAYER (p_nick) VALUES ('Arteezy');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Arteezy'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Evil%'),
            '2016-09-15',1,False);
INSERT INTO PLAYER (p_nick) VALUES ('SumaiL');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'SumaiL'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Evil%'),
            '2016-09-15',2,False);
INSERT INTO PLAYER (p_nick) VALUES ('UNiVeRsE');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'UNiVeRsE'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Evil%'),
            '2016-06-09',3,False);
INSERT INTO PLAYER (p_nick) VALUES ('Cr1t-');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Cr1t-'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Evil%'),
            '2016-09-15',4,False);
INSERT INTO PLAYER (p_nick) VALUES ('Fear');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Fear'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Evil%'),
            '2017-09-01',5,True);

INSERT INTO PLAYER (p_nick) VALUES ('NaNa');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'NaNa'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),
            '2017-08-16',1,False);
INSERT INTO PLAYER (p_nick) VALUES ('Mushi');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Mushi'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),
            '2017-03-20',2,True);
INSERT INTO PLAYER (p_nick) VALUES ('iceiceice');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'iceiceice'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),
            '2017-08-16',3,False);
INSERT INTO PLAYER (p_nick) VALUES ('Jabz');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Jabz'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),
            '2017-08-16',4,False);
INSERT INTO PLAYER (p_nick) VALUES ('ninjaboogie');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'ninjaboogie'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),
            '2016-07-13',5,False);

INSERT INTO PLAYER (p_nick) VALUES ('Paparazi');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Paparazi'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Vici%'),
            '2017-09-06',1,False);
INSERT INTO PLAYER (p_nick) VALUES ('Ori');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Ori'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Vici%'),
            '2017-01-09',2,False);
INSERT INTO PLAYER (p_nick) VALUES ('eLeVeN');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'eLeVeN'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Vici%'),
            '2017-09-06',3,False);
INSERT INTO PLAYER (p_nick) VALUES ('LaNm');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'LaNm'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Vici%'),
            '2017-09-06',4,False);
INSERT INTO PLAYER (p_nick) VALUES ('Fenrir');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Fenrir'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Vici%'),
            '2017-09-06',5,False);

INSERT INTO PLAYER (p_nick) VALUES ('N0tail');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'N0tail'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%OG%'),
            '2015-10-31',1,False);
INSERT INTO PLAYER (p_nick) VALUES ('Resolut1on');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Resolut1on'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%OG%'),
            '2017-09-01',2,False);
INSERT INTO PLAYER (p_nick) VALUES ('s4');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 's4'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%OG%'),
            '2016-08-31',3,False);
INSERT INTO PLAYER (p_nick) VALUES ('JerAx');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'JerAx'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%OG%'),
            '2016-08-31',4,False);
INSERT INTO PLAYER (p_nick) VALUES ('Fly');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Fly'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%OG%'),
            '2015-10-31',5,True);

INSERT INTO PLAYER (p_nick) VALUES ('Crystallize');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Crystallize'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Natus%'),
            '2017-09-04',1,False);
INSERT INTO PLAYER (p_nick,p_name,p_surname,p_image,p_country,p_birth) VALUES ('Dendi','Danil','Ishutin','https://cybbet-static.s3.eu-central-1.amazonaws.com/images/news/d0953c700dd10eeb55045ba69d8a08a7.jpg','UA','1989-12-30');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Dendi'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Natus%'),
            '2015-10-20',2,False);
INSERT INTO PLAYER (p_nick) VALUES ('GeneRaL');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'GeneRaL'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Natus%'),
            '2016-02-23',3,False);
INSERT INTO PLAYER (p_nick) VALUES ('RodjER');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'RodjER'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Natus%'),
            '2017-09-04',4,False);
INSERT INTO PLAYER (p_nick) VALUES ('SoNNeikO');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'SoNNeikO'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%Natus%'),
            '2017-04-20',5,True);

INSERT INTO PLAYER (p_nick) VALUES ('Raven');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Raven'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%TNC%'),
            '2016-11-29',1,False);
INSERT INTO PLAYER (p_nick) VALUES ('Kuku');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Kuku'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%TNC%'),
            '2016-08-31',2,False);
INSERT INTO PLAYER (p_nick) VALUES ('Sam_H');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Sam_H'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%TNC%'),
            '2016-08-30',3,False);
INSERT INTO PLAYER (p_nick) VALUES ('Tims');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = 'Tims'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%TNC%'),
            '2016-12-15',4,False);
INSERT INTO PLAYER (p_nick) VALUES ('1437');
INSERT INTO ROSTER (p_id, t_id , join_date, position, is_captain)
    VALUES ((SELECT p_id FROM PLAYER WHERE p_nick = '1437'),
            (SELECT t_id FROM TEAM WHERE t_name LIKE '%TNC%'),
            '2017-05-16',5,True);


-- RESULTS
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),3,30
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Team Secret') AND leave_date IS NULL LIMIT 5;
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%ESL One Hamburg%'),2,450
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Team Secret') AND leave_date IS NULL LIMIT 5;
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%DreamLeague%'),1,750
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Team Secret') AND leave_date IS NULL LIMIT 5;

INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),2,90
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Mineski') AND leave_date IS NULL LIMIT 5;
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Bucharest%'),1,150
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Mineski') AND leave_date IS NULL LIMIT 5;

INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%DreamLeague%'),3,225
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Evil Geniuses') AND leave_date IS NULL LIMIT 5;
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Bucharest%'),3,30
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Evil Geniuses') AND leave_date IS NULL LIMIT 5;

INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),1,150
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Team Liquid') AND leave_date IS NULL LIMIT 5;
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%ESL One Hamburg%'),3,150
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Team Liquid') AND leave_date IS NULL LIMIT 5;
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Dota PIT%'),1,150
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Team Liquid') AND leave_date IS NULL LIMIT 5;
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%DreamLeague%'),2,450
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Team Liquid') AND leave_date IS NULL LIMIT 5;

INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%MDL Macau%'),4,22.5
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Virtus.pro') AND leave_date IS NULL LIMIT 4;
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%ESL One Hamburg%'),1,750
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Virtus.pro') AND leave_date IS NULL LIMIT 5;
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Dota PIT%'),4,15
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Virtus.pro') AND leave_date IS NULL LIMIT 5;

INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Perfect World Masters%'),1,150
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Newbee') AND leave_date IS NULL LIMIT 5;
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%ESL One Hamburg%'),3,150
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Newbee') AND leave_date IS NULL LIMIT 5;
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Dota PIT%'),3,45
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Newbee') AND leave_date IS NULL LIMIT 5;

INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Perfect World Masters%'),1,150
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Vici Gaming') AND leave_date IS NULL LIMIT 5;
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Dota PIT%'),2,150
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Vici Gaming') AND leave_date IS NULL LIMIT 5;

INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%MDL%'),1,150
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'OG') AND leave_date IS NULL LIMIT 5;

INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%MDL%'),3,30
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Natus Vincere') AND leave_date IS NULL LIMIT 5;
INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
SELECT p_id,t_id,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%DreamLeague%'),4,75
FROM ROSTER WHERE t_id = (SELECT t_id FROM TEAM WHERE t_name = 'Natus Vincere') AND leave_date IS NULL LIMIT 5;

-- BRACKETS
INSERT INTO BRACKET (br_type,br_stage,tr_id,br_name,br_index)
VALUES ('0',0,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),'GROUP 1',0);
INSERT INTO BRACKET (br_type,br_stage,tr_id,br_name,br_index)
VALUES ('0',1,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),'GROUP 2',0);
INSERT INTO BRACKET (br_type,br_stage,tr_id,br_name,br_index)
VALUES ('1',1,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),'Semifinals',0);
INSERT INTO BRACKET (br_type,br_stage,tr_id,br_name,br_index)
VALUES ('1',0,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),'Finals',0);

-- MATCHES
INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score)
VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Vici%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Immortals%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 0 ),3,0,2);
INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score)
VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 0 ),3,2,0);
INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score)
VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Immortals%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 0 ),3,0,2);
INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score)
VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Vici%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 0 ),3,0,2);
INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score)
VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Immortals%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 0 ),3,0,2);
INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score)
VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Newbee%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%compLexity%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 1 ),3,0,2);
INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score)
VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Vincere%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 1 ),3,1,2);
INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score)
VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%compLexity%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Vincere%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 1 ),3,2,1);
INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score)
VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Newbee%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 1 ),3,0,2);
INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score)
VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Vincere%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 1 ),3,0,2);

INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,m_index)
VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%compLexity%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '1' AND br_stage = 1 AND br_index = 0),3,1,2,0);
INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,m_index)
VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '1' AND br_stage = 1 AND br_index = 0),3,2,0,1);
INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,m_index)
VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '1' AND br_stage = 0 AND br_index = 0),5,1,3,0);
