def calc_labor_cost(repair_form):
    return sum(a.labor_cost for a in repair_form.actions)

def calc_component_cost(repair_form):
    total=0
    for a in repair_form.actions:
        for a_comp in a.components:
            total+= a_comp.quantity * a_comp.component.price
    return total

def calc_total_cost(repair_form):
    return calc_component_cost(repair_form) + calc_labor_cost(repair_form)