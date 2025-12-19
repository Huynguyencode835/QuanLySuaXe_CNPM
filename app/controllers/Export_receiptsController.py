from flask import render_template,send_file,request
import app.dao.dao as dao
from app.utils.pdf_util import export_receipt_pdf

class Export_receiptsController:
    def index(self):
        q = request.args.get("q")
        receipt=dao.get_receipt_success(q=q)
        vat=dao.get_VAT()
        return render_template("export_receipts.html",page="Xuất hóa đơn",receipt=receipt,vat=vat)

    def export(self,receipt_id):
        receipt=dao.get_receipt_by_id(receipt_id)
        pdf_path = export_receipt_pdf(receipt)
        return send_file(
            pdf_path,
            as_attachment=True,
            download_name=f"hoa_don_{receipt.id}.pdf"
        )
