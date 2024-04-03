from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Crear un documento PDF
doc = SimpleDocTemplate("reportlab_ejemplo.pdf", pagesize=letter)

# Obtener estilos de muestra
styles = getSampleStyleSheet()

# Definir un estilo de párrafo para el título
title_style = ParagraphStyle(
    "Title",
    parent=styles["Title"],
    fontName="Calibri",
    fontSize=12,
    leading=14,  # Espacio entre líneas
    spaceAfter=12  # Espacio después del párrafo
)

# Definir un estilo de párrafo para el subtítulo
subtitle_style = ParagraphStyle(
    "Subtitle",
    parent=styles["Heading2"],
    fontName="Calibri",
    fontSize=12,
    leading=14,  # Espacio entre líneas
    spaceAfter=12  # Espacio después del párrafo
)

# Crear contenido para el documento
title_text = "Título del Documento"
subtitle_text = "Subtítulo del Documento"
body_text = "Este es el contenido del documento."

# Crear párrafos con los estilos definidos
title_paragraph = Paragraph(title_text, title_style)
subtitle_paragraph = Paragraph(subtitle_text, subtitle_style)
body_paragraph = Paragraph(body_text, styles["Normal"])

# Construir el documento
doc.build([title_paragraph, subtitle_paragraph, body_paragraph])
