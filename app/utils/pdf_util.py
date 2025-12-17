from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from flask import current_app
import os

def export_receipt_pdf(receipt):
    folder = os.path.join(current_app.root_path, "static/invoices")
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, f"receipt_{receipt.id}.pdf")

    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()
    elements = []

    rf = receipt.repair_forms[0]
    reception = rf.reception_form

    # ===== TIÊU ĐỀ =====
    title = Paragraph(
        f"<b>HÓA ĐƠN SỬA CHỮA #{receipt.id}</b>",
        ParagraphStyle(
            name="Title",
            fontSize=16,
            alignment=1,  # center
            spaceAfter=20
        )
    )
    elements.append(title)

    # ===== THÔNG TIN CHUNG =====
    elements.append(Paragraph(f"<b>Phiếu #:</b> {receipt.id}", styles["Normal"]))
    elements.append(Paragraph(
        f"<b>Ngày:</b> {receipt.created_date.strftime('%d/%m/%Y')}",
        styles["Normal"]
    ))
    elements.append(Paragraph(
        f"<b>Khách hàng :</b> {reception.name}",
        styles["Normal"]
    ))
    elements.append(Paragraph(
        f"<b>Biển số :</b> {reception.carnumber}",
        styles["Normal"]
    ))
    elements.append(Paragraph(
        f"<b>Lỗi :</b> {reception.description}",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 12))

    # ===== BẢNG =====
    table_data = [[
        "Hạng mục", "Tiền công", "Linh kiện", "Đơn giá", "SL", "Thành tiền"
    ]]

    total = 0

    for rf in receipt.repair_forms:
        for comp in rf.components:
            thanh_tien = comp.component.price * comp.quantity
            total += thanh_tien + comp.cost

            table_data.append([
                comp.action,
                f"{comp.cost:,.0f}",
                comp.component.name,
                f"{comp.component.price:,.0f}",
                comp.quantity,
                f"{thanh_tien:,.0f}"
            ])

    table = Table(
        table_data,
        colWidths=[140, 60, 120, 60, 30, 80]
    )

    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 20))

    # ===== TỔNG TIỀN =====
    elements.append(
        Paragraph(
            f"<b>TỔNG THANH TOÁN: {total:,.0f} VND</b>",
            ParagraphStyle(
                name="Total",
                fontSize=13,
                alignment=2  # right
            )
        )
    )

    doc.build(elements)
    return file_path
