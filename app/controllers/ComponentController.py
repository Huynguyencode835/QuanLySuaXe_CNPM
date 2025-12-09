from flask import Flask, render_template, request
from app.models import dao


class ComponentController:

    # [GET] /components
    def index(self):
        args = request.args.to_dict()
        q=request.args.get('q')
        vehicle_id = request.args.get("vehicle_id")
        brand_id = request.args.get("brand_id")
        comps=dao.load_component(q=q,vehicle_id=vehicle_id,brand_id=brand_id)
        vehicles=dao.load_vehicletype()
        brands=dao.load_brandveghicle()
        selected_vehicle_name = "Loại linh kiện"
        if vehicle_id and vehicle_id.isdigit():
            selected_vehicle = next((c for c in vehicles if c.id == int(vehicle_id)), None)
            if selected_vehicle:
                selected_vehicle_name = selected_vehicle.name

        selected_brand_name = "Hãng linh kiện"
        if brand_id and brand_id.isdigit():
            selected_brand = next((b for b in brands if b.id == int(brand_id)), None)
            if selected_brand:
                selected_brand_name = selected_brand.name
        return render_template("components.html", page="Linh kiện",
                               comps=comps,vehicles=vehicles,brands=brands,current_args=args,
                               selected_vehicle_name=selected_vehicle_name,
                               selected_brand_name=selected_brand_name)


    # [GET] /components/:slug
    def show(self, slug):
        return render_template("componentDetail.html", slug=slug)
