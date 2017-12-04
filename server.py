import datetime
import os
import json
import re
import psycopg2 as dbapi2
from datetime import datetime
from datetime import date

from flask import Flask, jsonify
from flask import redirect
from flask import render_template
from flask import Response, request, session, abort
from flask.helpers import url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user 

countrieslist = """{"BD": "Bangladesh", "BE": "Belgium", "BF": "Burkina Faso", "BG": "Bulgaria", "BA": "Bosnia and Herzegovina", "BB": "Barbados", "WF": "Wallis and Futuna", "BL": "Saint Barthelemy", "BM": "Bermuda", "BN": "Brunei", "BO": "Bolivia", "BH": "Bahrain", "BI": "Burundi", "BJ": "Benin", "BT": "Bhutan", "JM": "Jamaica", "BV": "Bouvet Island", "BW": "Botswana", "WS": "Samoa", "BQ": "Bonaire, Saint Eustatius and Saba ", "BR": "Brazil", "BS": "Bahamas", "JE": "Jersey", "BY": "Belarus", "BZ": "Belize", "RU": "Russia", "RW": "Rwanda", "RS": "Serbia", "TL": "East Timor", "RE": "Reunion", "TM": "Turkmenistan", "TJ": "Tajikistan", "RO": "Romania", "TK": "Tokelau", "GW": "Guinea-Bissau", "GU": "Guam", "GT": "Guatemala", "GS": "South Georgia and the South Sandwich Islands", "GR": "Greece", "GQ": "Equatorial Guinea", "GP": "Guadeloupe", "JP": "Japan", "GY": "Guyana", "GG": "Guernsey", "GF": "French Guiana", "GE": "Georgia", "GD": "Grenada", "GB": "United Kingdom", "GA": "Gabon", "SV": "El Salvador", "GN": "Guinea", "GM": "Gambia", "GL": "Greenland", "GI": "Gibraltar", "GH": "Ghana", "OM": "Oman", "TN": "Tunisia", "JO": "Jordan", "HR": "Croatia", "HT": "Haiti", "HU": "Hungary", "HK": "Hong Kong", "HN": "Honduras", "HM": "Heard Island and McDonald Islands", "VE": "Venezuela", "PR": "Puerto Rico", "PS": "Palestinian Territory", "PW": "Palau", "PT": "Portugal", "SJ": "Svalbard and Jan Mayen", "PY": "Paraguay", "IQ": "Iraq", "PA": "Panama", "PF": "French Polynesia", "PG": "Papua New Guinea", "PE": "Peru", "PK": "Pakistan", "PH": "Philippines", "PN": "Pitcairn", "PL": "Poland", "PM": "Saint Pierre and Miquelon", "ZM": "Zambia", "EH": "Western Sahara", "EE": "Estonia", "EG": "Egypt", "ZA": "South Africa", "EC": "Ecuador", "IT": "Italy", "VN": "Vietnam", "SB": "Solomon Islands", "ET": "Ethiopia", "SO": "Somalia", "ZW": "Zimbabwe", "SA": "Saudi Arabia", "ES": "Spain", "ER": "Eritrea", "ME": "Montenegro", "MD": "Moldova", "MG": "Madagascar", "MF": "Saint Martin", "MA": "Morocco", "MC": "Monaco", "UZ": "Uzbekistan", "MM": "Myanmar", "ML": "Mali", "MO": "Macao", "MN": "Mongolia", "MH": "Marshall Islands", "MK": "Macedonia", "MU": "Mauritius", "MT": "Malta", "MW": "Malawi", "MV": "Maldives", "MQ": "Martinique", "MP": "Northern Mariana Islands", "MS": "Montserrat", "MR": "Mauritania", "IM": "Isle of Man", "UG": "Uganda", "TZ": "Tanzania", "MY": "Malaysia", "MX": "Mexico", "IL": "Israel", "FR": "France", "IO": "British Indian Ocean Territory", "SH": "Saint Helena", "FI": "Finland", "FJ": "Fiji", "FK": "Falkland Islands", "FM": "Micronesia", "FO": "Faroe Islands", "NI": "Nicaragua", "NL": "Netherlands", "NO": "Norway", "NA": "Namibia", "VU": "Vanuatu", "NC": "New Caledonia", "NE": "Niger", "NF": "Norfolk Island", "NG": "Nigeria", "NZ": "New Zealand", "NP": "Nepal", "NR": "Nauru", "NU": "Niue", "CK": "Cook Islands", "XK": "Kosovo", "CI": "Ivory Coast", "CH": "Switzerland", "CO": "Colombia", "CN": "China", "CM": "Cameroon", "CL": "Chile", "CC": "Cocos Islands", "CA": "Canada", "CG": "Republic of the Congo", "CF": "Central African Republic", "CD": "Democratic Republic of the Congo", "CZ": "Czech Republic", "CY": "Cyprus", "CX": "Christmas Island", "CR": "Costa Rica", "CW": "Curacao", "CV": "Cape Verde", "CU": "Cuba", "SZ": "Swaziland", "SY": "Syria", "SX": "Sint Maarten", "KG": "Kyrgyzstan", "KE": "Kenya", "SS": "South Sudan", "SR": "Suriname", "KI": "Kiribati", "KH": "Cambodia", "KN": "Saint Kitts and Nevis", "KM": "Comoros", "ST": "Sao Tome and Principe", "SK": "Slovakia", "KR": "South Korea", "SI": "Slovenia", "KP": "North Korea", "KW": "Kuwait", "SN": "Senegal", "SM": "San Marino", "SL": "Sierra Leone", "SC": "Seychelles", "KZ": "Kazakhstan", "KY": "Cayman Islands", "SG": "Singapore", "SE": "Sweden", "SD": "Sudan", "DO": "Dominican Republic", "DM": "Dominica", "DJ": "Djibouti", "DK": "Denmark", "VG": "British Virgin Islands", "DE": "Germany", "YE": "Yemen", "DZ": "Algeria", "US": "United States", "UY": "Uruguay", "YT": "Mayotte", "UM": "United States Minor Outlying Islands", "LB": "Lebanon", "LC": "Saint Lucia", "LA": "Laos", "TV": "Tuvalu", "TW": "Taiwan", "TT": "Trinidad and Tobago", "TR": "Turkey", "LK": "Sri Lanka", "LI": "Liechtenstein", "LV": "Latvia", "TO": "Tonga", "LT": "Lithuania", "LU": "Luxembourg", "LR": "Liberia", "LS": "Lesotho", "TH": "Thailand", "TF": "French Southern Territories", "TG": "Togo", "TD": "Chad", "TC": "Turks and Caicos Islands", "LY": "Libya", "VA": "Vatican", "VC": "Saint Vincent and the Grenadines", "AE": "United Arab Emirates", "AD": "Andorra", "AG": "Antigua and Barbuda", "AF": "Afghanistan", "AI": "Anguilla", "VI": "U.S. Virgin Islands", "IS": "Iceland", "IR": "Iran", "AM": "Armenia", "AL": "Albania", "AO": "Angola", "AQ": "Antarctica", "AS": "American Samoa", "AR": "Argentina", "AU": "Australia", "AT": "Austria", "AW": "Aruba", "IN": "India", "AX": "Aland Islands", "AZ": "Azerbaijan", "IE": "Ireland", "ID": "Indonesia", "UA": "Ukraine", "QA": "Qatar", "MZ": "Mozambique"}"""

countries = json.loads(countrieslist)

app = Flask(__name__)

#LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):

    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        
    def __repr__(self):
        return "%s/%s" % (self.name, self.password)

admin_user = User(1,"Mahmut","AOSCOPTUR")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']        
        if admin_user.name == username and admin_user.password == password:
            login_user(admin_user)
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')

# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')

@login_manager.user_loader
def load_user(userid):
    return admin_user

def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn

@app.route('/admin')
@login_required
def admin():
    return Response("Hello World!")

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
        query4 = """ SELECT *
                    FROM(
                        SELECT ROW_NUMBER() OVER() as team_rank, data.*
                        FROM (
                            SELECT t_id, sum(dpc_points) as dpc_points
                            FROM (
                                SELECT ROW_NUMBER() OVER (PARTITION BY t_id ORDER BY dpc_points DESC) AS rowNumber, result.*
                                FROM (
                                        SELECT p_id, max(t_id) as t_id, SUM(dpc_points) AS dpc_points
                                        FROM RESULT
                                        GROUP BY p_id
                                ) AS result
                            ) AS results
                            WHERE results.rowNumber<=3
                            GROUP BY t_id
                            ORDER BY dpc_points DESC
                        ) AS data
                    ) AS ranks
                    WHERE t_id=%s
                    """
        cursor.execute(query4,[player_info[7]])
        teamrank = cursor.fetchall()
        query5 = """ SELECT tr_name, tr_enddate, placement, dpc_points, prize
                    FROM RESULT LEFT JOIN TOURNAMENT ON RESULT.tr_id=TOURNAMENT.tr_id
                    WHERE p_id=%s
                    ORDER BY tr_enddate DESC
                """
        cursor.execute(query5,[player_info[0]])
        resultlist = cursor.fetchall()
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
    if len(teamrank)>0:
        teamrank=teamrank[0][0]
    else:
        teamrank=""
    stats = [('DPC Points',results[0]),
             ('Played',results[1]),
             ('Qualified',results[2]),
             ('Team Rank',teamrank)]
    resultTitles = ['Tournament Name','Date','Plc.','DPC','Prize']
    resultColArray = ['5','2','1','2','2']
    historyTitles= ['Team Name','Join Date','Leave Date','Position','Captain']
    historyColArray = ['3','3','2','2','2']
    return render_template('header.html', title="Dotabase", route="player") + \
           render_template('profile.html', name=player_info[2], info=info, ) + \
           render_template('stats.html', stats=stats) + \
           render_template('listcard.html', mainTitle='Results',items=resultlist,titles=resultTitles,colSizes=resultColArray) + \
           render_template('listcard.html', mainTitle='Team History',items=history,titles=historyTitles,colSizes=historyColArray) + \
           render_template('footer.html')

@app.route('/player')
def players_page():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT PLAYER.p_nick,dpc FROM (SELECT SUM(dpc_points) as dpc,p_id FROM RESULT GROUP BY p_id ORDER BY dpc DESC) as RESULT RIGHT JOIN PLAYER ON RESULT.p_id = PLAYER.p_id"""
        cursor.execute(query)
        players = cursor.fetchall()
        connection.commit()
    return render_template('header.html', title="Dotabase", route="player") + \
           render_template('list.html', title="All Players", route="player", items=players, badge="DPC Points") + \
           render_template('footer.html')

@app.route('/team/<tname>')
def team_profile(tname):
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT * FROM TEAM WHERE t_name=%s"""
        cursor.execute(query,[tname])
        team_info = cursor.fetchall()[0]
        query2 = """SELECT p_nick,join_date,leave_date,position,is_captain FROM ROSTER LEFT JOIN PLAYER ON ROSTER.p_id=PLAYER.p_id WHERE ROSTER.t_id = %s ORDER BY position ASC, leave_date DESC """
        cursor.execute(query2,[team_info[0]])
        rosterList = cursor.fetchall()
        query3 = """SELECT tr_name,tr_enddate,placement,dpc_points,prize FROM (SELECT tr_id,placement,sum(prize) as prize,SUM(dpc_points) as dpc_points FROM RESULT WHERE RESULT.t_id = %s GROUP BY tr_id,placement) AS RESULT LEFT JOIN TOURNAMENT ON RESULT.tr_id=TOURNAMENT.tr_id ORDER BY tr_enddate DESC """
        cursor.execute(query3,[team_info[0]])
        resultList = cursor.fetchall()
        connection.commit()
        info = []

        if team_info[1]!=None:
            info.append(('Team Name',team_info[1]))
        if team_info[2]!=None:
            info.append(('Team Tag',team_info[2]))
        if team_info[3]!=None:
            info.append(('Team Region',team_info[3]))
        if team_info[4]!=None:
            info.append(('Created',team_info[4]))
        rosterTitles= ['Player','Join Date','Leave Date','Position','Captain']
        rosterColArray = ['3','3','2','2','2']
        resultTitles = ['Tournament Name','Date','Plc.','DPC Pts.','Prize']
        resultColArray = ['5','2','1','2','2']
        return render_template('header.html', title="Dotabase", route="team") + \
               render_template('profile.html', name=team_info[1], info=info, ) + \
               render_template('listcard.html', mainTitle='Roster', items=rosterList, titles=rosterTitles, colSizes=rosterColArray) + \
               render_template('listcard.html', mainTitle='Result', items=resultList, titles=resultTitles, colSizes=resultColArray) + \
               render_template('footer.html')

@app.route('/team')
def teams_page():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT t_name,dpc_points
                    FROM(
                        SELECT t_id, sum(dpc_points) as dpc_points
                        FROM (
                            SELECT ROW_NUMBER() OVER (PARTITION BY t_id ORDER BY dpc_points DESC) AS rowNumber, result.*
                            FROM (
                                SELECT p_id, max(t_id) as t_id, SUM(dpc_points) AS dpc_points
                                FROM RESULT
                                GROUP BY p_id
                                ) AS result

                            ) AS RESULTS
                        WHERE results.rowNumber<=3
                        GROUP BY t_id
                        ) AS POINTS
                    RIGHT JOIN TEAM
                    ON POINTS.t_id = TEAM.t_id
                    ORDER BY (dpc_points IS NULL),dpc_points DESC
                """
        cursor.execute(query)
        teams = cursor.fetchall()
        connection.commit()
    colors = []
    for team in teams[:8]:
        if team[1]!=None:
            colors.append("success")
        else:
            colors.append("primary")
    return render_template('header.html', title="Dotabase", route="team") + \
           render_template('list.html', title="All Teams", route="team", items=teams, color=colors, badge="DPC Points") + \
           render_template('footer.html')

@app.route('/tournaments/<trname>')
def tournament_profile(trname):
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT * FROM TOURNAMENT WHERE tr_name=%s"""
        cursor.execute(query,[trname])
        tournament_info = cursor.fetchall()[0]
        query2 = """SELECT  teamScores.br_stage, TEAM.t_name as teamName , SUM(teamScores.team_score) as teamScore, SUM(teamScores.team_lose) as teamLose
                    FROM
                    (SELECT  t_id as team_ids , SUM(t_1_score) as team_win, SUM(t_2_score) as team_lose,br_stage FROM MATCH LEFT JOIN BRACKET WHERE MATCH.br_id IN (SELECT  br_id FROM BRACKET WHERE BRACKET.tr_id = %s )  AND BRACKET.br_type = '0'
                     UNION  ALL
                     SELECT  t_id_2 as team_ids,SUM(t_2_score) as team_score,SUM(t_1_score) as team_lose,br_stage FROM MATCH LEFT JOIN BRACKET WHERE MATCH.br_id IN (SELECT  br_id FROM BRACKET WHERE BRACKET.tr_id = %s )  AND BRACKET.br_type = '0'
                     ) as teamScores LEFT JOIN TEAM WHERE teamScores.team_ids = TEAM.t_id GROUP BY teamName ORDER BY teamLose ASC,teamScore DESC ,teamScores.br_stage ASC"""
        cursor.execute(query2,[tournament_info[0],tournament_info[0]])
        groupMatches = cursor.fetchall()

        query3 ="""SELECT t_id,t_id_2,m_type,result,t_1_score,t_2_score,br_stage,br_id FROM MATCH LEFT JOIN BRACKET WHERE MATCH.br_id IN (SELECT  br_id FROM BRACKET WHERE BRACKET.tr_id = %s )  AND BRACKET.br_type = 1 ORDER BY br_id,br_stage ASC"""
        cursor.execute(query3,[tournament_info[0]])
        playoffMatches = cursor.fetchall()
        groupMatchInfo = []
        if len(groupMatches) > 0:
            render_groups = 1
            curStage = groupMatches[0][0]
            for x in groupMatches:
                if curStage == groupMatches[x][0]:
                    groupMatchInfo[curStage].append(groupMatches[x])
                else:
                    curStage = groupMatches[x][0]
        else:
            render_groups = 0
        info = []
        if tournament_info[1]!=None:
            info.append(('Tournament Name',tournament_info[1]))
        if tournament_info[2]!=None:
            info.append(('Start Date',tournament_info[2]))
        if tournament_info[3]!=None:
            info.append(('End Date',tournament_info[3]))
        if tournament_info[4]!=None:
            query4 = """ SELECT t_name FROM TOURNAMENT WHERE t_id = %s"""
            cursor.execute(query4,[tournament_info[4]])
            parentTournamentName = cursor.fetchall()[0]
            info.append(('Parent Tournament',parentTournamentName))
        else:
            info.append(('Parent Tournament','None'))

        groupTitles= ['Team','Win-Lose']
        groupColArray = ['3','1']
        if len(playoffMatches) > 0:
            render_playoffs = 0
        else:
            render_playoffs = 1

        return render_template('header.html', title="Dotabase", route="tournaments") + \
               render_template('profile.html', name=tournament_info[1], info=info, )  + \
               render_template('groups.html', title="All Tournaments", route="tournaments", items=groupMatchesInfo, render=render_groups, titles=groupTitles) + \
               render_template('playoffs.html', title="All Tournaments", route="tournaments", items=playoffMatches, render=render_playoffs) + \
               render_template('footer.html')

        #TO DO: FIND BRACKET TYPES -> IF EXIST DRAW & DO PROPER THINGS FOR EACH BRACKET TYPE.
        #GROUPS -> DRAW TABLE ACCORDING TO WIN-LOSS NUMBERS
        #PLAYOFFS ->DRAW BRACKET GRAPH.(LAST 16, SEMI, FINAL ETC).
        #CREATE GROUP AND PLAYOFF TEMPLATE.
        #ALSO MATCH INFO CAN BE ADDED WHEN HOVERED OVER TEAM'S NAME.
        #ALSO MATCH PAGES CAN BE ADDED ACCORDING TO MATCH ID'S

@app.route('/tournaments')
def tournaments_page():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT tr_name,tr_date FROM TOURNAMENT ORDER BY tr_date DESC """
        cursor.execute(query)
        tournaments = cursor.fetchall()
        connection.commit()
    colors = []
    today = date.today()
    for tournament in tournaments:
        if tournament[1]>today:
            colors.append("primary")
        if tournament[1]<=today:
            colors.append("danger")
    return render_template('header.html', title="Dotabase", route="tournaments") + \
           render_template('list.html', title="All Tournaments", route="tournaments", items=tournaments, color=colors) + \
           render_template('footer.html')

@app.route('/sqltest')
def sqltest():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT *
                    FROM RESULT LEFT JOIN PLAYER ON PLAYER.p_id=RESULT.p_id
                    WHERE RESULT.t_id=%s
                """
        cursor.execute(query,[6])
        result = cursor.fetchall()
        connection.commit()
    return jsonify(result)

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
        query = """DROP TABLE IF EXISTS BRACKET CASCADE"""
        cursor.execute(query)
        query = """DROP TABLE IF EXISTS COMPETITOR CASCADE"""
        cursor.execute(query)
        query = """DROP TABLE IF EXISTS MATCH CASCADE"""
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
        tr_enddate DATE,
        parent_tr_id INTEGER,
        FOREIGN KEY(parent_tr_id) REFERENCES TOURNAMENT(tr_id) ON DELETE CASCADE
        )"""
        cursor.execute(query)
        #br_type = 0 group, 1 playoff
        #If br_stage = 0  means final ,1 means semi and  so on.
        query = """ CREATE TABLE BRACKET(
        br_id SERIAL PRIMARY KEY,
        team_count INTEGER,
        br_type BOOLEAN,
        br_stage SMALLINT,
        tr_id INTEGER,
        br_name VARCHAR(60) NOT NULL,
        FOREIGN KEY(tr_id) REFERENCES TOURNAMENT(tr_id) ON DELETE CASCADE
        )"""

        cursor.execute(query)
        #DO WE REALLY NEED THIS?
        #query = """ CREATE TABLE COMPETITOR(
        #br_id INTEGER,
        #t_id INTEGER,
        #FOREIGN KEY(br_id) REFERENCES BRACKET(br_id) ON DELETE CASCADE,
        #FOREIGN KEY(t_id) REFERENCES TEAM(t_id) ON DELETE CASCADE
        #)"""

        #cursor.execute(query)

        query = """ CREATE TABLE MATCH(
        m_id SERIAL PRIMARY KEY,
        t_id INTEGER,
        t_id_2 INTEGER,
        br_id INTEGER,
        m_type SMALLINT,
        result SMALLINT,
        t_1_score SMALLINT,
        t_2_score SMALLINT,
        FOREIGN KEY (t_id)  REFERENCES TEAM(t_id) ON DELETE CASCADE,
        FOREIGN KEY(t_id_2) REFERENCES TEAM(t_id) ON DELETE CASCADE,
        FOREIGN KEY(br_id) REFERENCES BRACKET(br_id) ON DELETE CASCADE
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
        query = """INSERT INTO TOURNAMENT (tr_name,tr_date,tr_enddate)
        VALUES ('AMD SAPPHIRE Dota PIT League','2017-11-02','2017-11-05')"""
        cursor.execute(query)


        query = """INSERT INTO BRACKET (team_count,br_type,br_stage,tr_id,br_name)
        VALUES (4,'0',0,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),'GROUP 1')"""
        cursor.execute(query)
        query = """INSERT INTO BRACKET (team_count,br_type,br_stage,tr_id,br_name)
        VALUES (4,'0',1,(SELECT tr_id FROM TOURNAMENT WHERE tr_name LIKE '%Invitational Season 3%'),'GROUP 2')"""
        cursor.execute(query)


        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Vici%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Immortals%'),(SELECT br_id FROM BRACKET WHERE br_name = 'GROUP 1'),3,1,0,2)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),(SELECT br_id FROM BRACKET WHERE br_name = 'GROUP 1'),3,0,2,0)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Immortals%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Liquid%'),(SELECT br_id FROM BRACKET WHERE br_name = 'GROUP 1'),3,1,0,2)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Vici%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),(SELECT br_id FROM BRACKET WHERE br_name = 'GROUP 1'),3,1,0,2)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Immortals%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Mineski%'),(SELECT br_id FROM BRACKET WHERE br_name = 'GROUP 1'),3,1,0,2)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Newbee%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%complexity%'),(SELECT br_id FROM BRACKET WHERE br_name = 'GROUP 2'),3,1,0,2)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Vincere%'),(SELECT br_id FROM BRACKET WHERE br_name = 'GROUP 2'),3,1,1,2)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%compLexity%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Vincere%'),(SELECT br_id FROM BRACKET WHERE br_name = 'GROUP 2'),3,0,2,1)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Newbee%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),(SELECT br_id FROM BRACKET WHERE br_name = 'GROUP 2'),3,1,0,2)"""
        cursor.execute(query)
        query = """INSERT INTO MATCH (t_id,t_id_2,br_id,m_type,result,t_1_score,t_2_score)
        VALUES ((SELECT t_id FROM TEAM WHERE t_name LIKE '%Vincere%'),(SELECT t_id FROM TEAM WHERE t_name LIKE '%Secret%'),(SELECT br_id FROM BRACKET WHERE br_name = 'GROUP 2'),3,1,0,2)"""
        cursor.execute(query)

        query = """INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
        VALUES ('Evil Geniuses','EG',1,'2011-10-24')"""
        cursor.execute(query)
        query = """INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
        VALUES ('compLexity Gaming','coL',1,'2012-02-16')"""
        cursor.execute(query)
        query = """INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
        VALUES ('Immortals','IMT',1,'2017-09-13')"""
        cursor.execute(query)
        query = """INSERT INTO TEAM (t_name,t_tag,t_region)
        VALUES ('Mineski','Mski',5)"""
        cursor.execute(query)
        query = """INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
        VALUES ('Team Liquid','Liquid',3,'2012-12-06')"""
        cursor.execute(query)
        query = """INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
        VALUES ('Virtus.pro','VP',2,'2003-01-01')"""
        cursor.execute(query)
        query = """INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
        VALUES ('Team Secret','Secret',3,'2014-08-27')"""
        cursor.execute(query)
        query = """INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
        VALUES ('Newbee','Newbee',4,'2014-02-13')"""
        cursor.execute(query)
        query = """INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
        VALUES ('Vici Gaming','VG',4,'2012-09-21')"""
        cursor.execute(query)
        query = """INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
        VALUES ('LGD Gaming','VG',4,'2009-01-01')"""
        cursor.execute(query)
        query = """INSERT INTO TEAM (t_name,t_tag,t_region,t_created)
        VALUES ('LGD Natus Vincere','NAVI',2,'2010-10-22')"""
        cursor.execute(query)

        query = """INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country,p_birth,p_mmr,t_id)
        VALUES ('SumaiL','Syed Sumail','Hassan','PK','1999-02-13','8140',(SELECT t_id FROM TEAM WHERE t_name='Evil Geniuses'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country,p_birth,p_mmr,t_id)
        VALUES ('MATUMBAMAN','Lasse Aukusti','Urpalainen','FI','1995-03-03','9421',(SELECT t_id FROM TEAM WHERE t_name LIKE 'Team Liquid'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,p_name,p_surname,p_country,p_birth,t_id)
        VALUES ('Miracle-','Amer','Al-Barqawi','JO','1997-06-20',(SELECT t_id FROM TEAM WHERE t_name='Team Liquid'))"""
        cursor.execute(query)

        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('RAMZES666',(SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('No[o]ne',(SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('9pasha',(SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('Lil',(SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('Solo',(SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('Ace',(SELECT t_id FROM TEAM WHERE t_name='Team Secret'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('MidOne',(SELECT t_id FROM TEAM WHERE t_name='Team Secret'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('Fata',(SELECT t_id FROM TEAM WHERE t_name='Team Secret'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('YapzOr',(SELECT t_id FROM TEAM WHERE t_name='Team Secret'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('Puppey',(SELECT t_id FROM TEAM WHERE t_name='Team Secret'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('MinD_ContRoL',(SELECT t_id FROM TEAM WHERE t_name='Team Liquid'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('GH',(SELECT t_id FROM TEAM WHERE t_name='Team Liquid'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('KuroKy',(SELECT t_id FROM TEAM WHERE t_name='Team Liquid'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('NaNa',(SELECT t_id FROM TEAM WHERE t_name='Mineski'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('Mushi',(SELECT t_id FROM TEAM WHERE t_name='Mineski'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('iceiceice',(SELECT t_id FROM TEAM WHERE t_name='Mineski'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('Jabz',(SELECT t_id FROM TEAM WHERE t_name='Mineski'))"""
        cursor.execute(query)
        query = """INSERT INTO PLAYER (p_nick,t_id) VALUES ('ninjaboogie',(SELECT t_id FROM TEAM WHERE t_name='Mineski'))"""
        cursor.execute(query)


        query = """CREATE TABLE RESULT (
        p_id INTEGER NOT NULL,
        t_id INTEGER NOT NULL,
        tr_id INTEGER NOT NULL,
        placement INTEGER,
        dpc_points REAL,
        prize INTEGER,
        FOREIGN KEY(p_id) REFERENCES PLAYER(p_id) ON DELETE CASCADE,
        FOREIGN KEY(t_id) REFERENCES TEAM(t_id) ON DELETE CASCADE,
        FOREIGN KEY(tr_id) REFERENCES TOURNAMENT(tr_id) ON DELETE CASCADE
        )"""
        cursor.execute(query)

        query = """INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
        VALUES ((SELECT p_id FROM PLAYER WHERE p_nick='RAMZES666'),
                (SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                1,650),
                ((SELECT p_id FROM PLAYER WHERE p_nick='No[o]ne'),
                (SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                1,750),
                ((SELECT p_id FROM PLAYER WHERE p_nick='9pasha'),
                (SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                1,750),
                ((SELECT p_id FROM PLAYER WHERE p_nick='Lil'),
                (SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                1,750),
                ((SELECT p_id FROM PLAYER WHERE p_nick='Solo'),
                (SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                1,750)
                """
        cursor.execute(query)

        query = """INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
        VALUES ((SELECT p_id FROM PLAYER WHERE p_nick='RAMZES666'),
                (SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='AMD SAPPHIRE Dota PIT League'),
                4,15),
                ((SELECT p_id FROM PLAYER WHERE p_nick='No[o]ne'),
                (SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='AMD SAPPHIRE Dota PIT League'),
                4,15),
                ((SELECT p_id FROM PLAYER WHERE p_nick='9pasha'),
                (SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='AMD SAPPHIRE Dota PIT League'),
                4,15),
                ((SELECT p_id FROM PLAYER WHERE p_nick='Lil'),
                (SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='AMD SAPPHIRE Dota PIT League'),
                4,15),
                ((SELECT p_id FROM PLAYER WHERE p_nick='Solo'),
                (SELECT t_id FROM TEAM WHERE t_name='Virtus.pro'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='AMD SAPPHIRE Dota PIT League'),
                4,15)
                """
        cursor.execute(query)

        query = """INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
        VALUES ((SELECT p_id FROM PLAYER WHERE p_nick='Ace'),
                (SELECT t_id FROM TEAM WHERE t_name='Team Secret'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                2,450),
                ((SELECT p_id FROM PLAYER WHERE p_nick='MidOne'),
                (SELECT t_id FROM TEAM WHERE t_name='Team Secret'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                2,450),
                ((SELECT p_id FROM PLAYER WHERE p_nick='Fata'),
                (SELECT t_id FROM TEAM WHERE t_name='Team Secret'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                2,450),
                ((SELECT p_id FROM PLAYER WHERE p_nick='YapzOr'),
                (SELECT t_id FROM TEAM WHERE t_name='Team Secret'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                2,450),
                ((SELECT p_id FROM PLAYER WHERE p_nick='Puppey'),
                (SELECT t_id FROM TEAM WHERE t_name='Team Secret'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                2,450)
                """
        cursor.execute(query)

        query = """INSERT INTO RESULT (p_id,t_id,tr_id,placement,dpc_points)
        VALUES ((SELECT p_id FROM PLAYER WHERE p_nick='MATUMBAMAN'),
                (SELECT t_id FROM TEAM WHERE t_name='Team Liquid'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                3,150),
                ((SELECT p_id FROM PLAYER WHERE p_nick='Miracle-'),
                (SELECT t_id FROM TEAM WHERE t_name='Team Liquid'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                3,150),
                ((SELECT p_id FROM PLAYER WHERE p_nick='MinD_ContRoL'),
                (SELECT t_id FROM TEAM WHERE t_name='Team Liquid'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                3,150),
                ((SELECT p_id FROM PLAYER WHERE p_nick='GH'),
                (SELECT t_id FROM TEAM WHERE t_name='Team Liquid'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                3,150),
                ((SELECT p_id FROM PLAYER WHERE p_nick='KuroKy'),
                (SELECT t_id FROM TEAM WHERE t_name='Team Liquid'),
                (SELECT tr_id FROM TOURNAMENT WHERE tr_name='ESL One Hamburg 2017'),
                3,150)
                """
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
    app.config["SECRET_KEY"] = 'super_secret_key'                               
    app.run(host='0.0.0.0', port=port, debug=debug)
