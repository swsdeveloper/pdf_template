import pandas
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
# orientation: P(ortrait) or L(andscape)
# unit = dimensions for drawing lines and shapes: mm (millimeters)
# format: Paper size (A4: 200 mm from left-to-right border)

csvfile = 'topics.csv'
df = pandas.read_csv(csvfile)
for index, row in df.iterrows():
    topic = row['Topic']
    pages = int(row['Pages'])
    # print(pages, topic)

    pdf.add_page()

    # Header:
    pdf.set_font(family="Times", style="B", size=24)
    # style="B" -- bold (for normal, omit this argument)
    # size=12 -- 12 points

    pdf.set_text_color(0, 0, 0)  # black (rgb)
    # pdf.set_text_color(255, 0, 0)  # red
    # pdf.set_text_color(0, 255, 0)  # green
    # pdf.set_text_color(0, 0, 255)  # blue

    pdf.cell(w=0, h=12, txt=topic, align="L", ln=1)
    # w/h = width and height:
    #   w=0 defaults to printable width (pertains to border)
    #   h=12 -- should match font size
    # align="L" (left); can also be "R" (right) or "C" (center)
    # ln=1 -- advance 1 line down (like a breakline)
    # border=1 -- thickness of border (for no border, omit this arg)

    # Draw a line:
    pdf.line(x1=10, y1=21, x2=200, y2=21)
    # x1, y1: starting coordinates (in mm -- see unit=mm above)
    # x2, y2: ending coordinates

    # Footer:
    # pdf.footer()
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(100, 100, 100)  # light grey
    pdf.cell(w=0, h=12, txt=topic, align="R", ln=1, border=0)

    for i in range(pages - 1):
        pdf.add_page()
        # pdf.footer()
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(100, 100, 100)  # light grey
        pdf.cell(w=0, h=12, txt=topic, align="R", ln=1, border=0)

pdf.output("pdf_template.pdf", )
