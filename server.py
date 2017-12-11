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

teamRegionList = (("NA","North America"),("SA","South America"),("EU","Europe"),("CIS","CIS"),("CN","China"),("SEA","Southeast Asia"))

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

admin_user = User(1,"admin","alperencoptur")

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
        return Response(
               render_template('header.html', title="Admin Login") + \
               render_template('loginform.html') + \
               render_template('footer.html')
               )

# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response(render_template('error.html',title="Logged out",error="User logged out successfully!"))

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
    return Response(
           render_template('header.html', title="Admin Login") + \
           render_template('alert.html', color="success",text="Welcome to the admin page!") + \
           render_template('footer.html')
           )

@app.route("/add_player",methods=["GET", "POST"])
@login_required
def add_player():
    if request.method == 'POST':
        nick = (request.form['nick'],"p_nick")
        name = (request.form['name'],"p_name")
        surname = (request.form['surname'],"p_surname")
        country = (request.form['country'],"p_country")
        birth_date = (request.form['birth_date'],"p_birth")
        mmr = (request.form['mmr'],"p_mmr")
        image = (request.form['image'],"p_image")
        s = ""
        v = ""
        for var in (nick,name,surname,country,birth_date,mmr,image):
            if(var[0] != ""):
                if(s==""):
                    s = var[1]
                    v = "'"+var[0]+"'"
                else:
                    s += "," + var[1]
                    v += ","+"'"+var[0]+"'"


        query = """INSERT INTO PLAYER ({})
        VALUES ({})""".format(s,v)
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
            except dbapi2.Error as e:
                lcolor = "danger"
                ltext = e.pgerror
                pass
            else:
                lcolor = "success"
                ltext = "{} added to the dotabase".format(nick[0])
                pass
        return Response(
               render_template('header.html', title="Add Player") + \
               render_template('alert.html', color=lcolor,text=ltext) + \
               render_template('playerform.html', countries=countries) + \
               render_template('footer.html')
               )
    else:
        return Response(
               render_template('header.html', title="Add Player") + \
               render_template('playerform.html', countries=countries) + \
               render_template('footer.html')
               )

@app.route("/add_team", methods=["GET", "POST"])
@login_required
def add_team():
    if request.method == 'POST':
        team_name = (request.form['team_name'],"t_name")
        team_tag = (request.form['team_tag'],"t_tag")
        region = (request.form['region'],"t_region")
        date_created = (request.form['date_created'],"t_created")
        image = (request.form['image'],"t_image")
        s = ""
        v = ""
        for var in (team_name,team_tag,region,date_created,image):
            if(var[0] != ""):
                if(s==""):
                    s = var[1]
                    v = "'"+var[0]+"'"
                else:
                    s += "," + var[1]
                    v += ","+"'"+var[0]+"'"

        query = """INSERT INTO TEAM ({})
        VALUES ({})""".format(s,v)

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
            except dbapi2.Error as e:
                lcolor = "danger"
                ltext = e.pgerror
                pass
            else:
                lcolor = "success"
                ltext = "{} added to the dotabase".format(team_name[0])
                pass
        return Response(
               render_template('header.html', title="Add Team") + \
               render_template('alert.html', color=lcolor,text=ltext) + \
               render_template('teamform.html', regions=teamRegionList) + \
               render_template('footer.html')
               )
    else:
        return Response(
               render_template('header.html', title="Add Team") + \
               render_template('teamform.html', regions=teamRegionList) + \
               render_template('footer.html')
               )

@app.route("/add_tournament", methods=["GET", "POST"])
@login_required
def add_tournament():
    if request.method == 'POST':
        tournament_name = (request.form['tournament_name'],"tr_name")
        date_started = (request.form['date_started'],"tr_date")
        date_ended = (request.form['date_ended'],"tr_enddate")
        parent_id = (request.form['parent_id'],"parent_tr_id")

        s = ""
        v = ""
        for var in (tournament_name,date_started,date_ended,parent_id):
            if(var[0] != ""):
                if(s==""):
                    s = var[1]
                    v = "'"+var[0]+"'"
                else:
                    s += "," + var[1]
                    v += ","+"'"+var[0]+"'"

        query = """INSERT INTO TOURNAMENT ({})
        VALUES ({})""".format(s,v)
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
            except dbapi2.Error as e:
                lcolor = "danger"
                ltext = e.pgerror
                pass
            else:
                lcolor = "success"
                ltext = "{} added to the dotabase".format(tournament_name[0])
                pass
        return Response(
               render_template('header.html', title="Add Tournament") + \
               render_template('alert.html', color=lcolor,text=ltext) + \
               render_template('tournamentform.html') + \
               render_template('footer.html')
               )

    else:
        return Response(
               render_template('header.html', title="Add Tournament") + \
               render_template('tournamentform.html') + \
               render_template('footer.html')
               )

@app.route("/add_bracket", methods=["GET", "POST"])
@login_required
def add_bracket():
    if request.method == 'POST':
        team_count = (request.form['team_count'],"team_count")
        br_type = (request.form['br_type'],"br_type")
        br_stage = (request.form['br_stage'],"br_stage")
        tr_id = (request.form['tr_id'],"tr_id")
        br_name = (request.form['br_name'],"br_name")

        s = ""
        v = ""
        for var in (team_count,br_type,br_stage,tr_id,br_name):
            if(var[0] != ""):
                if(s==""):
                    s = var[1]
                    v = "'"+var[0]+"'"
                else:
                    s += "," + var[1]
                    v += ","+"'"+var[0]+"'"

        query = """INSERT INTO BRACKET ({})
        VALUES ({})""".format(s,v)
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
            except dbapi2.Error as e:
                lcolor = "danger"
                ltext = e.pgerror
                pass
            else:
                lcolor = "success"
                ltext = "{} added to the dotabase".format(br_name[0])
                pass
        return Response(
               render_template('header.html', title="Add Bracket") + \
               render_template('alert.html', color=lcolor,text=ltext) + \
               render_template('bracketform.html') + \
               render_template('footer.html')
               )

    else:
        return Response(
               render_template('header.html', title="Add Bracket") + \
               render_template('bracketform.html') + \
               render_template('footer.html')
               )

@app.route("/add_participant", methods=["GET", "POST"])
@login_required
def add_participant():
    if request.method == 'POST':
        tr_id = (request.form['tr_id'],"tr_id")
        t_id = (request.form['t_id'],"t_id")
        qualifier_id = (request.form['qualifier_id'],"qualifier_id")

        s = ""
        v = ""
        for var in (tr_id,t_id,qualifier_id):
            if(var[0] != ""):
                if(s==""):
                    s = var[1]
                    v = "'"+var[0]+"'"
                else:
                    s += "," + var[1]
                    v += ","+"'"+var[0]+"'"

        query = """INSERT INTO PARTICIPANT ({})
        VALUES ({})""".format(s,v)
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
            except dbapi2.Error as e:
                lcolor = "danger"
                ltext = e.pgerror
                pass
            else:
                lcolor = "success"
                ltext = "Participant is added to the dotabase"
                pass
        return Response(
               render_template('header.html', title="Add Participant") + \
               render_template('alert.html', color=lcolor,text=ltext) + \
               render_template('participantform.html') + \
               render_template('footer.html')
               )
    else:
        return Response(
               render_template('header.html', title="Add Participant") + \
               render_template('participantform.html') + \
               render_template('footer.html')
               )

@app.route("/add_match", methods=["GET", "POST"])
@login_required
def add_match():
    if request.method == 'POST':
        t_id = (request.form['t_id'],"t_id")
        t_id_2 = (request.form['t_id_2'],"t_id_2")
        br_id = (request.form['br_id'],"br_id")
        m_type = (request.form['m_type'],"m_type")
        result = (request.form['result'],"result")
        t_1_score = (request.form['t_1_score'],"t_1_score")
        t_2_score = (request.form['t_2_score'],"t_2_score")

        s = ""
        v = ""
        for var in (t_id, t_id_2, br_id, m_type, result, t_1_score, t_2_score):
            if(var[0] != ""):
                if(s==""):
                    s = var[1]
                    v = "'"+var[0]+"'"
                else:
                    s += "," + var[1]
                    v += ","+"'"+var[0]+"'"

        query = """INSERT INTO MATCH ({})
        VALUES ({})""".format(s,v)
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
            except dbapi2.Error as e:
                lcolor = "danger"
                ltext = e.pgerror
                pass
            else:
                lcolor = "success"
                ltext = "Match is added to the dotabase"
                pass
        return Response(
               render_template('header.html', title="Add Match") + \
               render_template('alert.html', color=lcolor,text=ltext) + \
               render_template('matchform.html') + \
               render_template('footer.html')
               )
    else:
        return Response(
               render_template('header.html', title="Add Match") + \
               render_template('matchform.html') + \
               render_template('footer.html')
               )

@app.route("/add_talent", methods=["GET", "POST"])
@login_required
def add_talent():
    if request.method == 'POST':
        p_id = (request.form['p_id'],"p_id")
        tr_id = (request.form['tr_id'],"tr_id")
        rl_id = (request.form['rl_id'],"rl_id")
        lang = (request.form['lang'],"lang")

        s = ""
        v = ""
        for var in (p_id, tr_id, rl_id, lang):
            if(var[0] != ""):
                if(s==""):
                    s = var[1]
                    v = "'"+var[0]+"'"
                else:
                    s += "," + var[1]
                    v += ","+"'"+var[0]+"'"

        query = """INSERT INTO TALENT ({})
        VALUES ({})""".format(s,v)
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
            except dbapi2.Error as e:
                lcolor = "danger"
                ltext = e.pgerror
                pass
            else:
                lcolor = "success"
                ltext = "Talent is added to the dotabase"
                pass
        return Response(
               render_template('header.html', title="Add Talent") + \
               render_template('alert.html', color=lcolor,text=ltext) + \
               render_template('talentform.html') + \
               render_template('footer.html')
               )
    else:
        return Response(
               render_template('header.html', title="Add Talent") + \
               render_template('talentform.html') + \
               render_template('footer.html')
               )

@app.route("/add_result", methods=["GET", "POST"])
@login_required
def add_result():
    if request.method == 'POST':
        p_id = (request.form['p_id'],"p_id")
        t_id = (request.form['t_id'],"t_id")
        tr_id = (request.form['tr_id'],"tr_id")
        placement = (request.form['placement'],"placement")
        dpc_points = (request.form['dpc_points'],"dpc_points")
        prize = (request.form['prize'],"prize")

        s = ""
        v = ""
        for var in (p_id, t_id, tr_id, placement, dpc_points, prize):
            if(var[0] != ""):
                if(s==""):
                    s = var[1]
                    v = "'"+var[0]+"'"
                else:
                    s += "," + var[1]
                    v += ","+"'"+var[0]+"'"

        query = """INSERT INTO RESULT ({})
        VALUES ({})""".format(s,v)
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
            except dbapi2.Error as e:
                lcolor = "danger"
                ltext = e.pgerror
                pass
            else:
                lcolor = "success"
                ltext = "Result is added to the dotabase"
                pass
        return Response(
               render_template('header.html', title="Add Result") + \
               render_template('alert.html', color=lcolor,text=ltext) + \
               render_template('resultform.html') + \
               render_template('footer.html')
               )
    else:
        return Response(
               render_template('header.html', title="Add Result") + \
               render_template('resultform.html') + \
               render_template('footer.html')
               )

@app.route("/add_roster", methods=["GET", "POST"])
@login_required
def add_roster():
    if request.method == 'POST':
        p_id = (request.form['p_id'],"p_id")
        t_id = (request.form['t_id'],"t_id")
        join_date = (request.form['join_date'],"join_date")
        leave_date = (request.form['leave_date'],"leave_date")
        position = (request.form['position'],"position")
        is_captain = (request.form['is_captain'],"is_captain")

        s = ""
        v = ""
        for var in (p_id, t_id, join_date, leave_date, position, is_captain):
            if(var[0] != ""):
                if(s==""):
                    s = var[1]
                    v = "'"+var[0]+"'"
                else:
                    s += "," + var[1]
                    v += ","+"'"+var[0]+"'"

        query = """INSERT INTO ROSTER ({})
        VALUES ({})""".format(s,v)
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
            except dbapi2.Error as e:
                lcolor = "danger"
                ltext = e.pgerror
                pass
            else:
                lcolor = "success"
                ltext = "Roster is added to the dotabase"
                pass
        return Response(
               render_template('header.html', title="Add Roster") + \
               render_template('alert.html', color=lcolor,text=ltext) + \
               render_template('rosterform.html') + \
               render_template('footer.html')
               )
    else:
        return Response(
               render_template('header.html', title="Add Roster") + \
               render_template('rosterform.html') + \
               render_template('footer.html')
               )



@app.route('/home')
@app.route('/')
def home_page():
    t_query = """ SELECT t_name,dpc_points
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
                LIMIT 8
            """
    tr_query = """ SELECT tr_name,tr_date FROM TOURNAMENT WHERE tr_date>=%s ORDER BY tr_date ASC LIMIT 8"""
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        cursor.execute(t_query)
        teams = cursor.fetchall()
        cursor.execute(tr_query,[date.today()])
        tournaments = cursor.fetchall()

    return render_template('header.html', title="Dotabase", route="home") + \
           render_template('home.html') + \
           render_template('dividepage.html', sizes = (5,7), content=(
           render_template('list.html', title="Top 8 Teams", route="team", items=teams, badge="DPC Points"),
           render_template('list.html', title="Upcoming Tournaments", route="tournaments", items=tournaments, badge="")
           )) + \
           render_template('footer.html')


@app.route('/player/<nick>')
def player_profile(nick):
    today=date.today()
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """SELECT * FROM (SELECT * FROM PLAYER WHERE p_nick=%s) AS PLAYER LEFT JOIN (SELECT ID.p_id,ID.t_id,TEAM.t_name FROM (SELECT p_id,t_id FROM ROSTER WHERE leave_date IS NULL) AS ID LEFT JOIN TEAM ON ID.t_id=TEAM.t_id) AS TEAM ON PLAYER.p_id = TEAM.p_id"""
        cursor.execute(query,[nick])
        player_info = cursor.fetchone()
        query2 = """ SELECT t_name,join_date,leave_date,position,is_captain FROM ROSTER JOIN TEAM ON ROSTER.t_id=TEAM.t_id WHERE p_id=%s ORDER BY leave_date IS NULL DESC, join_date DESC"""
        cursor.execute(query2,[player_info[0]])
        history = cursor.fetchall()
        query3 = """ SELECT SUM(dpc_points),COUNT(*) FROM RESULT WHERE p_id=%s """
        cursor.execute(query3,[player_info[0]])
        results = cursor.fetchone()
        query3b = """ SELECT COUNT(*) FROM PARTICIPANT WHERE t_id=%s """
        cursor.execute(query3b,[player_info[9]])
        participate = cursor.fetchone()
        query4 = """SELECT *
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
        cursor.execute(query4,[player_info[9]])
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
    if player_info[2]!=None or player_info[3]!=None:
        info.append(('Name',player_info[2]+" "+player_info[3]))
    if player_info[4]!=None:
        info.append(('Country',countries[player_info[4]]))
    if player_info[5]!=None:
        info.append(('Birth Date',player_info[5]))
    if player_info[5]!=None:
        info.append(('Age',today.year - player_info[5].year - ((today.month, today.day) < (player_info[5].month, player_info[5].day))))
    if player_info[9]!=None:
        info.append(('Team',player_info[10]))
    if player_info[6]!=None:
        info.append(('Solo MMR',player_info[6]))

    if len(teamrank)>0:
        teamrank=teamrank[0][0]
    else:
        teamrank=""

    stats = [('DPC Points',results[0]),
             ('Played',results[1]),
             ('Qualified',participate[0]),
             ('Team Rank',teamrank)]

    resultTitles = ['Tournament Name','Date','Plc.','DPC','Prize']
    resultColArray = ['5','2','1','2','2']
    historyTitles= ['Team Name','Join Date','Leave Date','Position','Captain']
    historyColArray = ['3','3','2','2','2']

    return render_template('header.html', title="Dotabase", route="player") + \
           render_template('profile.html', link=player_info[7], name=player_info[1], info=info) + \
           render_template('stats.html', stats=stats) + \
           render_template('listcard.html', mainTitle='Results',items=resultlist,titles=resultTitles,colSizes=resultColArray) + \
           render_template('listcard.html', mainTitle='Team History',items=history,titles=historyTitles,colSizes=historyColArray) + \
           render_template('footer.html', closetag=("div","div"))

@app.route('/player')
def players_page():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT PLAYER.p_nick,dpc
                    FROM (
                           SELECT SUM(dpc_points) as dpc,p_id
                           FROM RESULT
                           GROUP BY p_id
                           ORDER BY dpc DESC) as RESULT
                    RIGHT JOIN PLAYER
                    ON RESULT.p_id = PLAYER.p_id
                    ORDER BY dpc IS NULL, dpc DESC"""
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
        team_info = cursor.fetchone()
        query2 = """SELECT p_nick,join_date,leave_date,position,is_captain FROM ROSTER LEFT JOIN PLAYER ON ROSTER.p_id=PLAYER.p_id WHERE ROSTER.t_id = %s ORDER BY leave_date DESC,position ASC"""
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
            info.append(('Tag',team_info[2]))
        if team_info[3]!=None:
            info.append(('Region',teamRegionList[team_info[3]][1]))
        if team_info[4]!=None:
            info.append(('Created',team_info[4]))
        rosterTitles= ['Player','Join Date','Leave Date','Position','Captain']
        rosterColArray = ['3','3','2','2','2']
        resultTitles = ['Tournament Name','Date','Plc.','DPC Pts.','Prize']
        resultColArray = ['5','2','1','2','2']
        return render_template('header.html', title="Dotabase", route="team") + \
               render_template('profile.html', link=team_info[5],name=team_info[1], info=info) + \
               render_template('listcard.html', mainTitle='Roster', items=rosterList, titles=rosterTitles, colSizes=rosterColArray) + \
               render_template('listcard.html', mainTitle='Result', items=resultList, titles=resultTitles, colSizes=resultColArray) + \
               render_template('footer.html', closetag=("div","div"))

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
        tournament_info = cursor.fetchone()

        query2 ="""SELECT *
                    FROM (
                            SELECT TEAM.t_name,SUM(won_mathces) AS winScoreTotal,SUM(lose_mathces) AS loseScoreTotal,SUM(team_won) AS teamWonTotal ,SUM(team_lose) AS teamLoseTotal,br_stage
                            FROM(
                                    SELECT  t_id as team_ids ,SUM(CASE WHEN t_1_score > t_2_score THEN 1 ELSE 0 END) as won_mathces,SUM(CASE WHEN t_2_score > t_1_score THEN 1 ELSE 0 END) as lose_mathces,SUM(t_1_score) AS team_won, SUM(t_2_score) AS team_lose,br_stage
                                    FROM MATCH
                                    LEFT JOIN BRACKET
                                    ON MATCH.br_id = BRACKET.br_id
                                    WHERE MATCH.br_id
                                    IN (SELECT  br_id FROM BRACKET WHERE BRACKET.tr_id = %s )
                                    AND BRACKET.br_type = '0'
                                    GROUP BY team_ids,br_stage
                                    UNION All
                                    SELECT  t_id_2 as team_ids ,SUM(CASE WHEN t_2_score > t_1_score THEN 1 ELSE 0 END) as won_mathces,SUM(CASE WHEN t_1_score > t_2_score THEN 1 ELSE 0 END) as lose_mathces,SUM(t_2_score) AS team_won, SUM(t_1_score) AS team_lose,br_stage
                                    FROM MATCH
                                    LEFT JOIN BRACKET
                                    ON MATCH.br_id = BRACKET.br_id
                                    WHERE MATCH.br_id
                                    IN (SELECT  br_id FROM BRACKET WHERE BRACKET.tr_id = %s )
                                    AND BRACKET.br_type = '0'
                                    GROUP BY team_ids,br_stage
                                ) AS teamScores LEFT JOIN TEAM ON teamScores.team_ids = TEAM.t_id GROUP BY TEAM.t_name,br_stage
                          )as teamScores
                    ORDER BY  br_stage ASC, loseScoreTotal ASC,winScoreTotal DESC
                """
        cursor.execute(query2,[tournament_info[0],tournament_info[0]])
        groupMatches = cursor.fetchall()

        query3 =""" SELECT matches.t_id,team1name,t_id_2,TEAM.t_name as team2name,t_1_score,t_2_score,br_name,br_stage,br_index,COALESCE(m_index,0)
                    FROM (
                            SELECT  matches.t_id,TEAM.t_name as team1name,t_id_2,br_name,t_1_score,t_2_score,br_stage,br_index,m_index
                            FROM (
                                    SELECT t_id,t_id_2,br_name,t_1_score,t_2_score,br_stage,br_index,m_index
                                    FROM BRACKET
                                    LEFT JOIN MATCH
                                    ON BRACKET.br_id = MATCH.br_id
                                    WHERE BRACKET.tr_id = %s
                                    AND BRACKET.br_type = '1'
                                    ) as matches
                            LEFT JOIN TEAM
                            ON TEAM.t_id = matches.t_id
                        ) as matches
                    LEFT JOIN TEAM
                    ON TEAM.t_id = matches.t_id_2
                    ORDER BY br_stage DESC,m_index ASC,br_index ASC"""
        cursor.execute(query3,[tournament_info[0]])
        playoffMatches = cursor.fetchall()

        query4= """ SELECT teamTable.teamName,TOURNAMENT.tr_name
                    FROM(
                        SELECT qualifier_id,TEAM.t_name as teamName
                        FROM PARTICIPANT
                        LEFT JOIN TEAM
                        ON TEAM.t_id = PARTICIPANT.t_id
                        WHERE PARTICIPANT.tr_id = %s
                        ) as teamTable
                    LEFT JOIN TOURNAMENT
                    ON TOURNAMENT.tr_id = teamTable.qualifier_id
                    ORDER BY (TOURNAMENT.tr_name IS NULL) DESC """
        cursor.execute(query4,[tournament_info[0]])
        participants = cursor.fetchall()

        query5 = """SELECT role,p_nick,p_name,p_surname,lang,priority
                    FROM (
                            SELECT p_id,lang,role,priority
                            FROM TALENT
                            LEFT JOIN ROLE
                            ON ROLE.rl_id = TALENT.rl_id
                            WHERE TALENT.tr_id = %s
                          ) AS talents
                    LEFT JOIN PLAYER
                    ON PLAYER.p_id = talents.p_id
                    ORDER BY lang ASC, priority ASC"""
        cursor.execute(query5,[tournament_info[0]])
        talents = cursor.fetchall()

        talentsInfo = []
        if len(talents) > 0:
            langs = sorted({x[4] for x in talents})
            for y in langs:
                tempTalent = []
                roles = []
                for x in talents:
                    if x[0] not in roles:
                        roles.append(x[0])
                for z in roles:
                    tempTalent.append([x for x in talents if x[0] == z and x[4] == y])
                talentsInfo.append(tempTalent)

        groupMatchesInfo = []
        if len(groupMatches) > 0:
            groups = sorted({x[5] for x in groupMatches })
            for y in groups:
                groupMatchesInfo.append([x for x in groupMatches if x[5]==y])

        playoffMatchesInfo = []
        maxMatches = 0
        maxIndex = 0
        if len(playoffMatches) > 0:
            maxMatches = len(sorted({ x[9] for x in playoffMatches }))
            maxIndex = len(sorted({ x[8] for x in playoffMatches }))
            stages = sorted({ x[7] for x in playoffMatches }, reverse=True)
            for y in stages:
                tempStage = []
                indexes = sorted({ x[8] for x in playoffMatches if x[7] == y})
                for z in indexes:
                    tempStage.append([x[:7] for x in playoffMatches if x[8] == z and x[7] == y])
                playoffMatchesInfo.append(tempStage)

        info = []
        if tournament_info[2]!=None:
            info.append(('Start Date',tournament_info[2]))
        if tournament_info[3]!=None:
            info.append(('End Date',tournament_info[3]))
        if tournament_info[4]!=None:
            query4 = """ SELECT tr_name FROM TOURNAMENT WHERE tr_id = %s"""
            cursor.execute(query4,[tournament_info[4]])
            parentTournamentName = cursor.fetchone()
            info.append(('Parent Tournament',parentTournamentName[0]))

        return render_template('header.html', title="Dotabase", route="tournaments") + \
               render_template('tournamentprofile.html', name=tournament_info[1], info=info, )  + \
               render_template('teamlist.html', route="tournaments", items=participants) + \
               render_template('talents.html', route="tournaments", items=talentsInfo) + \
               render_template('groups.html', route="tournaments", items=groupMatchesInfo) + \
               render_template('playoffs.html', route="tournaments", height=120*maxMatches, indexes=maxIndex, items=playoffMatchesInfo) + \
               render_template('footer.html', closetag=("div"))


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

@app.route('/json/player/<nick>')
def jsonplayer(nick):
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT p_id,p_nick FROM PLAYER WHERE LOWER(p_nick) LIKE LOWER(%s)"""
        cursor.execute(query,['%'+nick+'%'])
        result = cursor.fetchall()
        connection.commit()
    resultList = []
    for i in result:
        resultList.append({"id":i[0],"name":i[1]})
    return jsonify(resultList)

@app.route('/json/tournament/<name>')
def jsontournament(name):
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT tr_id,tr_name FROM TOURNAMENT WHERE LOWER(tr_name) LIKE LOWER(%s)"""
        cursor.execute(query,['%'+name+'%'])
        result = cursor.fetchall()
        connection.commit()
    resultList = []
    for i in result:
        resultList.append({"id":i[0],"name":i[1]})
    return jsonify(resultList)

@app.route('/json/team/<name>')
def jsonteam(name):
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT t_id,t_name FROM TEAM WHERE LOWER(t_name) LIKE LOWER(%s)"""
        cursor.execute(query,['%'+name+'%'])
        result = cursor.fetchall()
        connection.commit()
    resultList = []
    for i in result:
        resultList.append({"id":i[0],"name":i[1]})
    return jsonify(resultList)

@app.route('/json/role/<name>')
def jsonrole(name):
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """ SELECT role FROM ROLE WHERE LOWER(role) LIKE LOWER(%s)"""
        cursor.execute(query,['%'+name+'%'])
        result = cursor.fetchall()
        connection.commit()
    return jsonify(result)

@app.route('/initdb')
def initialize_database():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        data1 = ""
        data2 = ""
        with open('structure.sql', 'r') as sql:
            data1=sql.read()
            cursor.execute(data1)
        with open('data.sql', 'r') as sql:
            data2=sql.read()
            cursor.execute(data2)
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
