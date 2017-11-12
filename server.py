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

countrieslist = """{"BD": "Bangladesh", "BE": "Belgium", "BF": "Burkina Faso", "BG": "Bulgaria", "BA": "Bosnia and Herzegovina", "BB": "Barbados", "WF": "Wallis and Futuna", "BL": "Saint Barthelemy", "BM": "Bermuda", "BN": "Brunei", "BO": "Bolivia", "BH": "Bahrain", "BI": "Burundi", "BJ": "Benin", "BT": "Bhutan", "JM": "Jamaica", "BV": "Bouvet Island", "BW": "Botswana", "WS": "Samoa", "BQ": "Bonaire, Saint Eustatius and Saba ", "BR": "Brazil", "BS": "Bahamas", "JE": "Jersey", "BY": "Belarus", "BZ": "Belize", "RU": "Russia", "RW": "Rwanda", "RS": "Serbia", "TL": "East Timor", "RE": "Reunion", "TM": "Turkmenistan", "TJ": "Tajikistan", "RO": "Romania", "TK": "Tokelau", "GW": "Guinea-Bissau", "GU": "Guam", "GT": "Guatemala", "GS": "South Georgia and the South Sandwich Islands", "GR": "Greece", "GQ": "Equatorial Guinea", "GP": "Guadeloupe", "JP": "Japan", "GY": "Guyana", "GG": "Guernsey", "GF": "French Guiana", "GE": "Georgia", "GD": "Grenada", "GB": "United Kingdom", "GA": "Gabon", "SV": "El Salvador", "GN": "Guinea", "GM": "Gambia", "GL": "Greenland", "GI": "Gibraltar", "GH": "Ghana", "OM": "Oman", "TN": "Tunisia", "JO": "Jordan", "HR": "Croatia", "HT": "Haiti", "HU": "Hungary", "HK": "Hong Kong", "HN": "Honduras", "HM": "Heard Island and McDonald Islands", "VE": "Venezuela", "PR": "Puerto Rico", "PS": "Palestinian Territory", "PW": "Palau", "PT": "Portugal", "SJ": "Svalbard and Jan Mayen", "PY": "Paraguay", "IQ": "Iraq", "PA": "Panama", "PF": "French Polynesia", "PG": "Papua New Guinea", "PE": "Peru", "PK": "Pakistan", "PH": "Philippines", "PN": "Pitcairn", "PL": "Poland", "PM": "Saint Pierre and Miquelon", "ZM": "Zambia", "EH": "Western Sahara", "EE": "Estonia", "EG": "Egypt", "ZA": "South Africa", "EC": "Ecuador", "IT": "Italy", "VN": "Vietnam", "SB": "Solomon Islands", "ET": "Ethiopia", "SO": "Somalia", "ZW": "Zimbabwe", "SA": "Saudi Arabia", "ES": "Spain", "ER": "Eritrea", "ME": "Montenegro", "MD": "Moldova", "MG": "Madagascar", "MF": "Saint Martin", "MA": "Morocco", "MC": "Monaco", "UZ": "Uzbekistan", "MM": "Myanmar", "ML": "Mali", "MO": "Macao", "MN": "Mongolia", "MH": "Marshall Islands", "MK": "Macedonia", "MU": "Mauritius", "MT": "Malta", "MW": "Malawi", "MV": "Maldives", "MQ": "Martinique", "MP": "Northern Mariana Islands", "MS": "Montserrat", "MR": "Mauritania", "IM": "Isle of Man", "UG": "Uganda", "TZ": "Tanzania", "MY": "Malaysia", "MX": "Mexico", "IL": "Israel", "FR": "France", "IO": "British Indian Ocean Territory", "SH": "Saint Helena", "FI": "Finland", "FJ": "Fiji", "FK": "Falkland Islands", "FM": "Micronesia", "FO": "Faroe Islands", "NI": "Nicaragua", "NL": "Netherlands", "NO": "Norway", "NA": "Namibia", "VU": "Vanuatu", "NC": "New Caledonia", "NE": "Niger", "NF": "Norfolk Island", "NG": "Nigeria", "NZ": "New Zealand", "NP": "Nepal", "NR": "Nauru", "NU": "Niue", "CK": "Cook Islands", "XK": "Kosovo", "CI": "Ivory Coast", "CH": "Switzerland", "CO": "Colombia", "CN": "China", "CM": "Cameroon", "CL": "Chile", "CC": "Cocos Islands", "CA": "Canada", "CG": "Republic of the Congo", "CF": "Central African Republic", "CD": "Democratic Republic of the Congo", "CZ": "Czech Republic", "CY": "Cyprus", "CX": "Christmas Island", "CR": "Costa Rica", "CW": "Curacao", "CV": "Cape Verde", "CU": "Cuba", "SZ": "Swaziland", "SY": "Syria", "SX": "Sint Maarten", "KG": "Kyrgyzstan", "KE": "Kenya", "SS": "South Sudan", "SR": "Suriname", "KI": "Kiribati", "KH": "Cambodia", "KN": "Saint Kitts and Nevis", "KM": "Comoros", "ST": "Sao Tome and Principe", "SK": "Slovakia", "KR": "South Korea", "SI": "Slovenia", "KP": "North Korea", "KW": "Kuwait", "SN": "Senegal", "SM": "San Marino", "SL": "Sierra Leone", "SC": "Seychelles", "KZ": "Kazakhstan", "KY": "Cayman Islands", "SG": "Singapore", "SE": "Sweden", "SD": "Sudan", "DO": "Dominican Republic", "DM": "Dominica", "DJ": "Djibouti", "DK": "Denmark", "VG": "British Virgin Islands", "DE": "Germany", "YE": "Yemen", "DZ": "Algeria", "US": "United States", "UY": "Uruguay", "YT": "Mayotte", "UM": "United States Minor Outlying Islands", "LB": "Lebanon", "LC": "Saint Lucia", "LA": "Laos", "TV": "Tuvalu", "TW": "Taiwan", "TT": "Trinidad and Tobago", "TR": "Turkey", "LK": "Sri Lanka", "LI": "Liechtenstein", "LV": "Latvia", "TO": "Tonga", "LT": "Lithuania", "LU": "Luxembourg", "LR": "Liberia", "LS": "Lesotho", "TH": "Thailand", "TF": "French Southern Territories", "TG": "Togo", "TD": "Chad", "TC": "Turks and Caicos Islands", "LY": "Libya", "VA": "Vatican", "VC": "Saint Vincent and the Grenadines", "AE": "United Arab Emirates", "AD": "Andorra", "AG": "Antigua and Barbuda", "AF": "Afghanistan", "AI": "Anguilla", "VI": "U.S. Virgin Islands", "IS": "Iceland", "IR": "Iran", "AM": "Armenia", "AL": "Albania", "AO": "Angola", "AQ": "Antarctica", "AS": "American Samoa", "AR": "Argentina", "AU": "Australia", "AT": "Austria", "AW": "Aruba", "IN": "India", "AX": "Aland Islands", "AZ": "Azerbaijan", "IE": "Ireland", "ID": "Indonesia", "UA": "Ukraine", "QA": "Qatar", "MZ": "Mozambique"}"""

countries = json.loads(countrieslist)

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
    today=date.today()
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT * FROM PLAYER LEFT JOIN (SELECT t_id,t_name FROM TEAM) AS TEAM ON PLAYER.t_id=TEAM.t_id WHERE p_nick=%s """
        cursor.execute(query,[nick])
        player_info = cursor.fetchall()[0]
        query2 = """ SELECT t_name,join_date,leave_date,position,is_captain FROM ROSTER JOIN TEAM ON ROSTER.t_id=TEAM.t_id WHERE p_id=%s ORDER BY join_date ASC"""
        cursor.execute(query2,[player_info[0]])
        history = cursor.fetchall()
        query3 = """ SELECT SUM(dpc_points),COUNT(*),COUNT(CASE WHEN tr_date<%s THEN 1 END) FROM RESULT LEFT JOIN TOURNAMENT ON RESULT.tr_id=TOURNAMENT.tr_id WHERE p_id=%s """
        cursor.execute(query3,[today,player_info[0]])
        results = cursor.fetchall()[0]
        connection.commit()
    info =  []
    if player_info[3]!=None or player_info[4]!=None:
        info.append(('Name',player_info[3]+" "+player_info[4]))
    if player_info[5]!=None:
        info.append(('Country',countries[player_info[5]]))
    if player_info[6]!=None:
        info.append(('Birth Date',player_info[6]))
    if player_info[6]!=None:
        info.append(('Age',today.year - player_info[6].year - ((today.month, today.day) < (player_info[6].month, player_info[6].day))))
    if player_info[10]!=None:
        info.append(('Team',player_info[10]))
    if player_info[8]!=None:
        info.append(('Solo MMR',player_info[8]))

    stats = [('DPC Points',results[0]),
             ('Played',results[1]),
             ('Qualified',results[2]),
             ('Team Rank','')]
    return render_template('header.html', title="Dotabase", route="player") + \
           render_template('profile.html', name=player_info[2], info=info, stats=stats) + \
           render_template('teamhistory.html', history=history) + \
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

        query = """DROP TABLE IF EXISTS ROSTER CASCADE"""
        cursor.execute(query)
        query = """DROP TABLE IF EXISTS TEAM CASCADE"""
        cursor.execute(query)
        query = """DROP TABLE IF EXISTS PLAYER CASCADE"""
        cursor.execute(query)
        query = """DROP TABLE IF EXISTS TOURNAMENT CASCADE"""
        cursor.execute(query)
        query = """DROP TABLE IF EXISTS RESULT CASCADE"""
        cursor.execute(query)

        query = """ CREATE TABLE TEAM(
        t_id SERIAL PRIMARY KEY,
        t_name VARCHAR(60),
        t_tag VARCHAR(10),
        t_region INTEGER,
        t_created DATE
        )"""
        cursor.execute(query)

        query = """CREATE TABLE PLAYER (
        p_id SERIAL PRIMARY KEY,
        p_accountid INTEGER UNIQUE,
        p_nick VARCHAR(20) NOT NULL UNIQUE,
        p_name VARCHAR(60),
        p_surname VARCHAR(60),
        p_country VARCHAR(2),
        p_birth DATE,
        t_id INTEGER,
        p_mmr INTEGER,
        FOREIGN KEY(t_id) REFERENCES TEAM(t_id) ON DELETE CASCADE
        )"""
        cursor.execute(query)

        query = """CREATE TABLE TOURNAMENT (
        tr_id SERIAL PRIMARY KEY,
        tr_name VARCHAR(60) NOT NULL,
        tr_date DATE,
        tr_enddate DATE
        )"""
        cursor.execute(query)

        query = """INSERT INTO TOURNAMENT (tr_name,tr_date,tr_enddate)
        VALUES ('SL i-League Invitational Season 3','2017-10-12','2017-10-15')"""
        cursor.execute(query)
        query = """INSERT INTO TOURNAMENT (tr_name,tr_date,tr_enddate)
        VALUES ('PGL Open Bucharest','2017-10-19','2017-10-22')"""
        cursor.execute(query)
        query = """INSERT INTO TOURNAMENT (tr_name,tr_date,tr_enddate)
        VALUES ('ESL One Hamburg 2017','2017-10-26','2017-10-29')"""
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

        query = """INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country,p_birth,p_mmr,t_id)
        VALUES ('SumaiL','Syed Sumail','Hassan','PK','1999-02-13','8140',(SELECT t_id FROM TEAM WHERE t_name='Evil Geniuses'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country,p_birth,p_mmr,t_id)
        VALUES ('MATUMBAMAN','Lasse Aukusti','Urpalainen','FI','1995-03-03','9421',(SELECT t_id FROM TEAM WHERE t_name LIKE 'Team Liquid'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country,p_birth)
        VALUES ('Miracle-','Amer','Al-Barqawi','JO','1997-06-20')"""
        cursor.execute(query)

        query = """INSERT INTO PLAYER (p_nick) VALUES ('RAMZES666')"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick) VALUES ('MidOne')"""
        cursor.execute(query)

        query = """CREATE TABLE RESULT (
        p_id INTEGER NOT NULL,
        t_id INTEGER NOT NULL,
        tr_id INTEGER NOT NULL,
        placement INTEGER,
        dpc_points INTEGER,
        prize INTEGER,
        FOREIGN KEY(p_id) REFERENCES PLAYER(p_id) ON DELETE CASCADE,
        FOREIGN KEY(t_id) REFERENCES TEAM(t_id) ON DELETE CASCADE,
        FOREIGN KEY(tr_id) REFERENCES TOURNAMENT(tr_id) ON DELETE CASCADE
        )"""
        cursor.execute(query)

        query = """INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
        VALUES ((SELECT p_id FROM PLAYER WHERE p_nick='SumaiL'),
                (SELECT t_id FROM TEAM WHERE t_name='Evil Geniuses'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='PGL Open Bucharest'),
                3,30)"""
        cursor.execute(query)
        query = """INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
        VALUES ((SELECT p_id FROM PLAYER WHERE p_nick='SumaiL'),
                (SELECT t_id FROM TEAM WHERE t_name='Evil Geniuses'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                2,50)"""
        cursor.execute(query)

        query = """ CREATE TABLE ROSTER(
        p_id INTEGER NOT NULL,
        t_id INTEGER NOT NULL,
        join_date DATE,
        leave_date DATE,
        position INTEGER,
        is_captain BOOLEAN NOT NULL,
        FOREIGN KEY(p_id) REFERENCES PLAYER(p_id) ON DELETE CASCADE,
        FOREIGN KEY(t_id) REFERENCES TEAM(t_id) ON DELETE CASCADE
        )"""
        cursor.execute(query)
        query = """ INSERT INTO ROSTER (p_id, t_id , join_date, position,is_captain)
        VALUES ((SELECT p_id FROM PLAYER WHERE p_nick LIKE '%SumaiL%'),
                (SELECT t_id FROM TEAM WHERE t_name LIKE '%Evil%'),
                 '2015-01-05',
                 2,
                 False)"""
        cursor.execute(query)
        query = """ INSERT INTO ROSTER (p_id, t_id , join_date, leave_date, position,is_captain)
        VALUES ((SELECT p_id FROM PLAYER WHERE p_nick LIKE '%SumaiL%'),
                (SELECT t_id FROM TEAM WHERE t_name LIKE '%Evil%'),
                 '2014-01-11','2015-01-05',
                 2,
                 False)"""
        cursor.execute(query)
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
