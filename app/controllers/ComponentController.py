from flask import render_template, request
from app.dao import dao
from app.utils.component_util import get_components_data


class ComponentController:

    # [GET] /components
    def index(self):
        args = request.args.to_dict()
        comps, vehicles, brands, selected_vehicle_name, selected_brand_name = get_components_data(args)
        return render_template("components.html", page="Linh kiện",
                               comps=comps,vehicles=vehicles,brands=brands,current_args=args,
                               selected_vehicle_name=selected_vehicle_name,
                               selected_brand_name=selected_brand_name)


    # [GET] /components/:slug
    def show(self, slug):
        return render_template("componentDetail.html", slug=slug)
