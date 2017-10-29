import datetime
import os
import json
import re
import psycopg2 as dbapi2
from datetime import date

from flask import Flask
from flask import redirect
from flask import render_template
from flask.helpers import url_for


app = Flask(__name__)

def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn


@app.route('/home')
@app.route('/')
def home_page():
    return render_template('header.html', title="Dotabase", route="home") + \
           render_template('home.html') + \
           render_template('footer.html')

@app.route('/player/<nick>')
def player_profile(nick):
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT * FROM PLAYER WHERE p_nick=%s """
        cursor.execute(query,[nick])
        player_info = cursor.fetchall()[0]
        connection.commit()
    today=date.today()
    info =  [('Name',player_info[3]+" "+player_info[4]),
             ('Country',player_info[5]),
             ('Birth Date',player_info[6]),
             ('Age',today.year - player_info[6].year - ((today.month, today.day) < (player_info[6].month, player_info[6].day))),
             ('Team','/Evil Geniuses'),
             ('Solo MMR','/8108'),
             ('Total Earnings','/$2,602,268')]
    stats = [('DPC Points','/150'),
             ('Played','/1'),
             ('Qualified','/3'),
             ('Team Rank','/2')]
    return render_template('header.html', title="Dotabase", route="player") + \
           render_template('profile.html', name=player_info[2], info=info, stats=stats) + \
           render_template('footer.html')

@app.route('/player')
def players_page():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT * FROM PLAYER """
        cursor.execute(query)
        players = cursor.fetchall()
        connection.commit()
    return render_template('header.html', title="Dotabase", route="player") + \
           render_template('list.html', title="All Players", route="player", items=players, index =2) + \
           render_template('footer.html')

@app.route('/team')
def teams_page():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT * FROM TEAM """
        cursor.execute(query)
        teams = cursor.fetchall()
        connection.commit()
    return render_template('header.html', title="Dotabase", route="team") + \
           render_template('list.html', title="All Teams", route="team", items=teams, index=1) + \
           render_template('footer.html')

@app.route('/initdb')
def initialize_database():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()

        query = """DROP TABLE IF EXISTS COUNTER"""
        cursor.execute(query)

        query = """DROP TABLE IF EXISTS PLAYER"""
        cursor.execute(query)

        query = """CREATE TABLE PLAYER (
        p_id SERIAL PRIMARY KEY,
        p_accountid INTEGER UNIQUE,
        p_nick VARCHAR(20) NOT NULL UNIQUE,
        p_name VARCHAR(60),
        p_surname VARCHAR(60),
        p_country VARCHAR(2),
        p_birth DATE,
        p_mmr INTEGER
        )"""
        cursor.execute(query)

        query = """INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country,p_birth)
        VALUES ('SumaiL','Syed Sumail','Hassan','PK','1999-02-13')"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country,p_birth)
        VALUES ('MATUMBAMAN','Lasse Aukusti','Urpalainen','FI','1995-03-03')"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country,p_birth)
        VALUES ('Miracle-','Amer','Al-Barqawi','JO','1997-06-20')"""
        cursor.execute(query)

        query = """ CREATE TABLE TEAM(
        t_id SERIAL PRIMARY KEY,
        t_name VARCHAR(60),
        t_tag VARCHAR(10),
        t_region INTEGER,
        t_created DATE
        )"""
        cursor.execute(query)

        query = """INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
        VALUES ('Evil Geniuses','EG',1,'2011-10-24')"""
        cursor.execute(query)
        query = """INSERT INTO TEAM (t_name,t_tag,t_region)
        VALUES ('Mineski','Mski',5)"""
        cursor.execute(query)
        query = """INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
        VALUES ('Team Liquid','Liquid ',3,'2012-12-06')"""
        cursor.execute(query)

        query = """ CREATE TABLE ROSTER(
        p_id INTEGER NOT NULL,
        t_id INTEGER NOT NULL,
        join_date DATE,
        leave_date DATE,
        position INTEGER,
        is_captain BIT NOT NULL,
        FOREIGN KEY(p_id) REFERENCES PLAYER(p_id),
        FOREIGN KEY(t_id) REFERENCES TEAM(t_id)
        )"""
        cursor.execute(query)
        query = """ INSERT INTO ROSTER (p_id, t_id , join_date, position,is_captain)
        VALUES ((SELECT p_id FROM PLAYER WHERE p_name LIKE '%Sumail%'),
                (SELECT t_id FROM TEAM WHERE t_name LIKE '%Evil%'),
                 '2015-01-05',
                 2,
                 0)"""

        connection.commit()

    return redirect(url_for('home_page'))


if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True

    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = """user='vagrant' password='vagrant'
                               host='localhost' port=5432 dbname='itucsdb'"""
    app.run(host='0.0.0.0', port=port, debug=debug)
