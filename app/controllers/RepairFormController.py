from flask import render_template, request

from app.dao import dao
from app.utils.component_util import get_components_data


class RepairFormController:
    def index(self):
        args = request.args.to_dict()
        comps, vehicles, brands, selected_vehicle_name, selected_brand_name = get_components_data(args)
        comps_data = []
        for comp in comps:
            comps_data.append({
                'id': comp.id,
                'name': comp.name,
                'price': float(comp.price) if comp.price else 0,
                'brand_id': comp.brand_id,
                'vehicle_id': comp.vehicle_id
            })

            vehicles_data = []
            for vehicle in vehicles:
                vehicles_data.append({
                    'id': vehicle.id,
                    'name': vehicle.name
                })

            brands_data = []
            for brand in brands:
                brands_data.append({
                    'id': brand.id,
                    'name': brand.name
                })
        return render_template("repairform.html", page="Phiếu sửa xe",
                               comps=comps_data, vehicles=vehicles_data, brands=brands_data, current_args=args,
                               selected_vehicle_name=selected_vehicle_name,
                               selected_brand_name=selected_brand_name)