from flask import Blueprint, render_template, request, jsonify
from model.first_constellation import FirstConstellation
from model.buyiju import BuYiJu
from app import db


route_index = Blueprint("main_page", __name__)


@route_index.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        surname_m = request.form.get('surname_m')
        person_name_m = request.form.get('person_name_m')
        zodiac_m = request.form.get('zodiac_m')
        month_m = request.form.get('month_m')
        day_m = request.form.get('day_m')
        constellation_m = request.form.get('constellation_m')

        surname_f = request.form.get('surname_f')
        person_name_f = request.form.get('surname_f')
        zodiac_f = request.form.get('zodiac_f')
        month_f = request.form.get('month_f')
        day_f = request.form.get('day_f')
        constellation_f = request.form.get('constellation_f')

        obj = constellation_m + ' VS ' + constellation_f
        obj2 = constellation_m[:-1] + '男' + constellation_f[:-1] + '女' + '配对'

        byj_msg = BuYiJu.query.filter(BuYiJu.obj == obj).first()
        score = byj_msg.score
        fir_msg = FirstConstellation.query.filter(FirstConstellation.obj == obj2).first()
        love = fir_msg.love
        family = fir_msg.family
        friendly = fir_msg.friendly

        data = {
            'obj': constellation_m[:-1] + '男 VS ' + constellation_f[:-1] + '女',
            'friendly_score': '★★★★',
            'love_score': '★★',
            'marriage_score': '★★',
            'family_score': '★★',
            'about_love': love,
            'about_family': family,
            'about_friendly': friendly
        }
        print(data)
        return render_template('middle.html', js=jsonify(data))
    else:
        return render_template('middle.html')
