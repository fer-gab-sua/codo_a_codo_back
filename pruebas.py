
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from models import Mochilas, Mochila

example_data = [
    (1, "Mochila de Aventuras", "Mochila espaciosa y resistente para aventuras al aire libre."),
    (2, "Mochila Escolar", "Mochila ligera y con muchos compartimentos para la escuela."),
    (3, "Mochila de Viaje", "Mochila cómoda y con espacio suficiente para viajes largos."),
    (4, "Mochila de Senderismo", "Mochila duradera con soporte para bastones de senderismo."),
    (5, "Mochila de Ciclismo", "Mochila aerodinámica y ligera para ciclistas."),
]


def create_pdf():
        doc = SimpleDocTemplate("example_reportlab.pdf", pagesize=letter)
        elements = []

        # Agregar una imagen al principio del documento
        logo = "src\static\img\logo.png"  # Cambia esto a la ruta de tu imagen
        img = Image(logo)  # Ajusta el tamaño de la imagen
        elements.append(img)

        # Recuperar datos de la tabla Mochilas
        mochilas = [1,2,3],

        # Datos de la tabla
        data = [["ID", "Nombre", "Descripción"]]

        for mochila in example_data:
            data.append([mochila.id, mochila.nombre, mochila.descripcion])

        # Crear una tabla
        table = Table(data)

        # Estilo de la tabla
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4F81BD')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#DCE6F1')),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ])

        table.setStyle(style)

        # Alternar colores de las filas
        for i in range(1, len(data)):
            bg_color = colors.whitesmoke if i % 2 == 0 else colors.beige
            table.setStyle(TableStyle([('BACKGROUND', (0, i), (-1, i), bg_color)]))

        elements.append(table)

        # Construir el PDF
        doc.build(elements)


create_pdf()