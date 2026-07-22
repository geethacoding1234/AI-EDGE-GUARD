from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def generate_report(
    filename,
    health,
    status,
    confidence,
    engine,
    battery,
    rpm,
    speed,
    vibration,
    oil,
    coolant,
    current,
    tire,
    ambient,
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph("<b>EdgeGuard AI Vehicle Health Report</b>", styles["Title"])

    elements.append(title)

    elements.append(Paragraph("<br/>", styles["Normal"]))

    data = [
        ["Parameter", "Value"],
        ["Vehicle Health Score", f"{health:.2f}%"],
        ["Vehicle Status", status],
        ["Prediction Confidence", f"{confidence:.2f}%"],
        ["Engine Temperature", f"{engine} °C"],
        ["Battery Voltage", f"{battery} V"],
        ["RPM", rpm],
        ["Speed", f"{speed} km/h"],
        ["Engine Vibration", vibration],
        ["Oil Pressure", oil],
        ["Coolant Temperature", coolant],
        ["Battery Current", current],
        ["Tire Pressure", tire],
        ["Ambient Temperature", ambient],
    ]

    table = Table(data, colWidths=[3*inch, 3*inch])

    table.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),colors.darkblue),
        ('TEXTCOLOR',(0,0),(-1,0),colors.white),

        ('GRID',(0,0),(-1,-1),1,colors.black),

        ('BACKGROUND',(0,1),(-1,-1),colors.beige),

        ('ALIGN',(0,0),(-1,-1),'CENTER'),

        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),

        ('BOTTOMPADDING',(0,0),(-1,0),12),
    ]))

    elements.append(table)

    doc.build(elements)
