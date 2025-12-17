from app._init_ import db
from app.dao import repairform_dao

def createRepairform(data):
    try:
        receptionform_id = data.get('receptionform_id')
        items = data.get('items', [])
        repair_form = repairform_dao.create_repair_form(receptionform_id)
        for item in items:
            repairform_dao.create_repair_component(
                id_repair_form=repair_form.id,
                id_component=item['component_id'],
                quantity=item['quantity'],
                action=item['action'],
                cost=item['cost']
            )
        db.session.commit()
        return True

    except Exception as e:
        print(f"Error: {e}")
        db.session.rollback()
        return False
