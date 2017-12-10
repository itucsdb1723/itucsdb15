
    query = """INSERT INTO BRACKET (tr_id,br_type,br_stage,br_name,br_index)
    VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name = 'DreamLeague Season 8'),'1',0,'Grand Finals',0)"""
    cursor.execute(query)
    query = """INSERT INTO BRACKET (tr_id,br_type,br_stage,br_name,br_index)
    VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name = 'DreamLeague Season 8'),'1',1,'Winners'' Finals',0)"""
    cursor.execute(query)
    query = """INSERT INTO BRACKET (tr_id,br_type,br_stage,br_name,br_index)
    VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name = 'DreamLeague Season 8'),'1',1,'Losers'' Finals',1)"""
    cursor.execute(query)
    query = """INSERT INTO BRACKET (tr_id,br_type,br_stage,br_name,br_index)
    VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name = 'DreamLeague Season 8'),'1',2,'',0)"""
    cursor.execute(query)
    query = """INSERT INTO BRACKET (tr_id,br_type,br_stage,br_name,br_index)
    VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name = 'DreamLeague Season 8'),'1',2,'Losers'' Round 3',1)"""
    cursor.execute(query)
    query = """INSERT INTO BRACKET (tr_id,br_type,br_stage,br_name,br_index)
    VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name = 'DreamLeague Season 8'),'1',3,'Semifinals',0)"""
    cursor.execute(query)
    query = """INSERT INTO BRACKET (tr_id,br_type,br_stage,br_name,br_index)
    VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name = 'DreamLeague Season 8'),'1',3,'Losers'' Round 2',1)"""
    cursor.execute(query)
    query = """INSERT INTO BRACKET (tr_id,br_type,br_stage,br_name,br_index)
    VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name = 'DreamLeague Season 8'),'1',4,'Quarterfinals',0)"""
    cursor.execute(query)
    query = """INSERT INTO BRACKET (tr_id,br_type,br_stage,br_name,br_index)
    VALUES ((SELECT tr_id FROM TOURNAMENT WHERE tr_name = 'DreamLeague Season 8'),'1',4,'Losers'' Round 1',1)"""
    cursor.execute(query)



    query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
    VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Vici%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Immortals%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 0 ),3,2,0,2)"""
    cursor.execute(query)
    query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
    VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 0 ),3,1,2,0)"""
    cursor.execute(query)
    query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
    VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Immortals%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 0 ),3,2,0,2)"""
    cursor.execute(query)
    query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
    VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Vici%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 0 ),3,2,0,2)"""
    cursor.execute(query)
    query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
    VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Immortals%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 0 ),3,2,0,2)"""
    cursor.execute(query)
    query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
    VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Newbee%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%compLexity%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 1 ),3,2,0,2)"""
    cursor.execute(query)
    query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
    VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Vincere%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 1 ),3,2,1,2)"""
    cursor.execute(query)
    query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
    VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%compLexity%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Vincere%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 1 ),3,1,2,1)"""
    cursor.execute(query)
    query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
    VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Newbee%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 1 ),3,2,0,2)"""
    cursor.execute(query)
    query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
    VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Vincere%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '0' AND br_stage = 1 ),3,2,0,2)"""
    cursor.execute(query)


        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score,m_index)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%compLexity%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '1' AND br_stage = 1 AND br_index = 0),3,2,1,2,0)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score,m_index)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '1' AND br_stage = 1 AND br_index = 0),3,1,2,0,1)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score,m_index)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%Invitational Season 3%' ) AND br_type = '1' AND br_stage = 0 AND br_index = 0),5,2,1,3,0)"""
        cursor.execute(query)

        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Virtus%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Vincere%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 4 AND br_index = 0),3,2,1,1,0)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES (NULL,NULL,(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 4 AND br_index = 0),3,2,0,1,1)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES (NULL,NULL,(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 4 AND br_index = 0),3,2,0,1,2)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES (NULL,NULL,(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 4 AND br_index = 0),3,2,0,1,3)"""
        cursor.execute(query)

        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Vincere%'),NULL,(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 4 AND br_index = 1),3,2,1,2,0)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES (NULL,NULL,(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 4 AND br_index = 1),3,2,0,2,1)"""
        cursor.execute(query)

        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Virtus%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 3 AND br_index = 0),3,1,2,2,0)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES (NULL,NULL,(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 3 AND br_index = 0),3,2,0,2,1)"""
        cursor.execute(query)

        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Newbee%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Vincere%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 3 AND br_index = 1),3,1,2,1,0)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES (NULL,NULL,(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 3 AND br_index = 1),3,0,2,1,1)"""
        cursor.execute(query)


        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Vincere%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Evil G%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 2 AND br_index = 1),3,0,2,2,0)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 1 AND br_index = 0),3,1,2,1,0)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Evil G%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 1 AND br_index = 1),3,2,0,1,0)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,t_1_score,t_2_score,result,m_index)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT br_id FROM BRACKET WHERE tr_id IN (SELECT tr_id FROM TOURNAMENT WHERE  tr_name LIKE '%DreamLeague%' ) AND br_type = '1' AND br_stage = 0 AND br_index = 0),5,3,0,1,0)"""
        cursor.execute(query)
