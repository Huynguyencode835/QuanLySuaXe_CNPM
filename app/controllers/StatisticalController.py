import datetime
import math
from flask import render_template, request, current_app
from app.dao import dao, appointment_dao
from app.utils import repairform_util
from app.utils.component_util import get_components_data
from app._init_ import create_app

class StatisticalController:

    # [GET] /STATISTICAL
    def index(self):
        return render_template("statistical.html", page="Báo cáo thống kê",vehicleType = dao.load_vehicletype())

    def createStatistical(self):
        data = request.args.to_dict()
        if data.get('filter_type') == 'vehicle':
            res = appointment_dao.get_dataStatisticalByVehicle()
            type = 'vehicle'
        else:
            type = 'time'
            if data.get('date_month'):
                date_from = repairform_util.get_month_range(data.get('date_month'))[0]
                date_to = repairform_util.get_month_range(data.get('date_month'))[1]
            elif data.get('date_day'):
                date_from = data.get("date_day")
                date_to = datetime.date.today()
            else:
                date_to = data.get("date_to")
                date_from = data.get("date_from")
            res = appointment_dao.get_dataStatisticalByTime(date_from,date_to)
        total = 0
        for i in res:
            if type == 'time':
                total = total + i[1]
            else:
                total = total + i[0]
        return render_template("statistical.html", res = res, type= type, chart_type=data.get('chart_type'), total = total)

