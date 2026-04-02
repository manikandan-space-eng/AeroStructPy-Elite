
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate(data, img=None):
    doc=SimpleDocTemplate("AeroStruct_Report.pdf")
    st=getSampleStyleSheet(); c=[]
    c.append(Paragraph("AeroStructPy Elite Report",st['Title']))
    c.append(Spacer(1,12))
    for k,v in data.items():
        c.append(Paragraph(f"{k}: {v}",st['Normal']))
    if img:
        c.append(Image(img, width=400, height=250))
    doc.build(c)
