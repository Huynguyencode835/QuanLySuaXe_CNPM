from flask_login import current_user

from app.dao import receptionform_dao
from app.models.model import Form_status


def get_receptionform(status):
    if (current_user.role.name == 'CUSTOMER'):
        data = receptionform_dao.receptionFormCustomer(current_user.id,status)
    else:
        data = receptionform_dao.load_receptionForm()
        if status:
            data = receptionform_dao.receptionFormUserState(status)
    return data

def parse_state():
    FORM_STATUS_VI = {
        Form_status.WAIT_APPROVAL: "Chờ duyệt",
        Form_status.REFUSE: "Từ chối",
        Form_status.WAIT_REPAIR: "Chờ sửa chữa",
        Form_status.UNDER_REPAIR: "Đang sửa chữa",
        Form_status.SUCCESS: "Hoàn thành"
    }
    return FORM_STATUS_VI


