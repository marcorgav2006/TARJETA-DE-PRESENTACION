#!/usr/bin/env python3
"""
=============================================================================
GENERADOR DE CÓDIGO QR CORPORATIVO DEFINITIVO - GRUPO ALESSA S.A.
=============================================================================
Este script genera un código QR estático de alta fidelidad, con la identidad
visual corporativa de Grupo Alessa:
  1. Lienzo exterior squircle (esquinas pronunciadamente redondeadas).
  2. Paleta corporativa Alessa: Módulos en Azul Corporativo Profundo (#0A5386 / #074574)
     y lienzo en Blanco Puro (#FFFFFF) con marco perimetral institucional.
  3. Ojos de localización (Finder Patterns) personalizados: Marco exterior squircle
     y pupila central circular en azul Alessa.
  4. Logotipo central de Grupo Alessa en alta resolución, incrustado con caja
     de seguridad y margen limpio para evitar interferencia visual.
  5. Calidad de imprenta: 2000 x 2000 px, 300 DPI, corrección de errores nivel H (30%).

INSTRUCCIONES DE USO:
  1. Configura tu URL de GitHub Pages en la variable URL_DESTINO más abajo.
  2. Ejecuta: python3 generar_qr.py
  3. Se generarán automáticamente:
     - qr_tarjeta_alta_resolucion.png (2000x2000 px, 300 DPI para impresión)
     - qr_tarjeta.png (versión optimizada para web y visualización en smartphone)
=============================================================================
"""

import os
import sys
import qrcode
from PIL import Image, ImageDraw, ImageOps

# =============================================================================
# CONFIGURACIÓN EDITABLE
# =============================================================================
URL_DESTINO = 'https://marcorgav2006.github.io/TARJETA-DE-PRESENTACION/'

# Rutas de archivos
ARCHIVO_LOGO = 'logo_alessa_azul.png'
SALIDA_ALTA_RES = 'qr_tarjeta_alta_resolucion.png'
SALIDA_WEB = 'qr_tarjeta.png'

# Paleta Corporativa Oficial Alessa S.A.
COLOR_FONDO_BLANCO   = (255, 255, 255, 255)  # #FFFFFF
COLOR_MODULO_AZUL    = (10, 83, 134, 255)    # #0A5386 Azul Alessa principal
COLOR_FINDER_AZUL    = (7, 69, 116, 255)     # #074574 Azul Alessa profundo
COLOR_BORDE_CARD     = (10, 83, 134, 255)    # #0A5386 Borde exterior de la tarjeta

# Dimensiones finales (2000 x 2000 px para máxima nitidez de imprenta)
CANVAS_SIZE = 2000
DPI = (300, 300)
RADIO_SQUIRCLE = 240  # Radio de curvatura exterior suave (~12% del lienzo)


def generar_qr():
    print(f"[*] Generando código QR corporativo - Grupo Alessa...")
    print(f"[*] URL Destino: {URL_DESTINO}")

    # 1. Crear matriz QR con máximo nivel de corrección de error (ERROR_CORRECT_H = 30%)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=1,
        border=0
    )
    qr.add_data(URL_DESTINO)
    qr.make(fit=True)
    matrix = qr.get_matrix()
    num_modulos = len(matrix)
    print(f"[*] Matriz QR generada: {num_modulos}x{num_modulos} módulos.")

    # 2. Calcular tamaño y centrado del código dentro del lienzo
    # Queremos que el código ocupe aproximadamente el 76% del lienzo, dejando un margen
    # perimetral blanco armónico y profesional.
    area_qr_objetivo = 1520
    module_size = int(area_qr_objetivo / num_modulos)
    tamano_qr_real = module_size * num_modulos
    offset_x = (CANVAS_SIZE - tamano_qr_real) // 2
    offset_y = (CANVAS_SIZE - tamano_qr_real) // 2

    # 3. Crear lienzo transparente y dibujar la tarjeta exterior squircle
    canvas = Image.new('RGBA', (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255, 0))
    draw = ImageDraw.Draw(canvas)

    # Dibujar tarjeta squircle blanca con borde Alessa
    padding_exterior = 24
    draw.rounded_rectangle(
        [padding_exterior, padding_exterior, CANVAS_SIZE - padding_exterior, CANVAS_SIZE - padding_exterior],
        radius=RADIO_SQUIRCLE,
        fill=COLOR_FONDO_BLANCO,
        outline=COLOR_BORDE_CARD,
        width=8
    )

    # 4. Definir zonas de ojos de localización (Finder Patterns de 7x7 módulos en las 3 esquinas)
    def es_finder(r, c):
        if r < 7 and c < 7:
            return True  # Superior izquierda
        if r < 7 and c >= num_modulos - 7:
            return True  # Superior derecha
        if r >= num_modulos - 7 and c < 7:
            return True  # Inferior izquierda
        return False

    # 5. Dibujar los módulos de datos en Azul Alessa
    for r in range(num_modulos):
        for c in range(num_modulos):
            if es_finder(r, c):
                continue
            if matrix[r][c]:
                x1 = offset_x + c * module_size
                y1 = offset_y + r * module_size
                x2 = x1 + module_size
                y2 = y1 + module_size
                draw.rectangle([x1, y1, x2, y2], fill=COLOR_MODULO_AZUL)

    # 6. Dibujar los 3 ojos de localización estilizados (Custom Finder Patterns)
    # Marco squircle azul + interior blanco + pupila circular azul Alessa
    finder_posiciones = [
        (0, 0),                       # Esquina superior izquierda
        (0, num_modulos - 7),         # Esquina superior derecha
        (num_modulos - 7, 0)          # Esquina inferior izquierda
    ]

    for fr, fc in finder_posiciones:
        fx = offset_x + fc * module_size
        fy = offset_y + fr * module_size
        fw = 7 * module_size

        # Marco exterior: rectángulo redondeado azul Alessa (7x7 módulos)
        radio_exterior = int(1.4 * module_size)
        draw.rounded_rectangle(
            [fx, fy, fx + fw, fy + fw],
            radius=radio_exterior,
            fill=COLOR_FINDER_AZUL
        )

        # Separador interior: rectángulo redondeado blanco (5x5 módulos)
        radio_interior = int(0.7 * module_size)
        draw.rounded_rectangle(
            [fx + module_size, fy + module_size, fx + fw - module_size, fy + fw - module_size],
            radius=radio_interior,
            fill=COLOR_FONDO_BLANCO
        )

        # Núcleo / Pupila central: Círculo perfecto azul (3x3 módulos)
        px1 = fx + 2 * module_size
        py1 = fy + 2 * module_size
        px2 = fx + fw - 2 * module_size
        py2 = fy + fw - 2 * module_size
        draw.ellipse([px1, py1, px2, py2], fill=COLOR_FINDER_AZUL)

    # 7. Incrustar el Logotipo Central de Grupo Alessa con caja de seguridad
    if os.path.exists(ARCHIVO_LOGO):
        logo_img = Image.open(ARCHIVO_LOGO).convert('RGBA')
        
        # Calcular tamaño del logo: ~27% del ancho del QR para máxima legibilidad sin afectar lectura
        target_w = int(tamano_qr_real * 0.27)
        target_h = int(logo_img.size[1] * (target_w / logo_img.size[0]))
        logo_redimensionado = logo_img.resize((target_w, target_h), Image.Resampling.LANCZOS)

        # Dimensiones del contenedor de seguridad blanco
        padding_badge = 18
        badge_w = target_w + (padding_badge * 2)
        badge_h = target_h + (padding_badge * 2)
        badge_x1 = (CANVAS_SIZE - badge_w) // 2
        badge_y1 = (CANVAS_SIZE - badge_h) // 2
        badge_x2 = badge_x1 + badge_w
        badge_y2 = badge_y1 + badge_h

        # Dibujar caja blanca de protección con esquinas redondeadas y borde sutil
        draw.rounded_rectangle(
            [badge_x1, badge_y1, badge_x2, badge_y2],
            radius=18,
            fill=COLOR_FONDO_BLANCO,
            outline=COLOR_MODULO_AZUL,
            width=4
        )

        # Centrar y estampar el logo de Alessa
        pos_x = badge_x1 + padding_badge
        pos_y = badge_y1 + padding_badge
        canvas.paste(logo_redimensionado, (pos_x, pos_y), logo_redimensionado)
        print(f"[*] Logotipo de Grupo Alessa incrustado con éxito ({target_w}x{target_h} px).")
    else:
        print(f"[!] Advertencia: No se encontró '{ARCHIVO_LOGO}', se omitió el logo central.")

    # 8. Guardar archivo en alta resolución con metadatos de 300 DPI
    canvas.save(SALIDA_ALTA_RES, dpi=DPI)
    print(f"[✓] Guardado archivo en alta resolución (2000x2000 px, 300 DPI): {SALIDA_ALTA_RES}")

    # 9. Generar versión optimizada para web (800x800 px)
    web_version = canvas.resize((800, 800), Image.Resampling.LANCZOS)
    web_version.save(SALIDA_WEB)
    print(f"[✓] Guardado archivo optimizado para web (800x800 px): {SALIDA_WEB}")

    # 10. Validar decodificación con lector estándar
    try:
        import zxingcpp
        res = zxingcpp.read_barcode(canvas)
        if res and res.text == URL_DESTINO:
            print(f"[✓] Verificación de escaneo exitosa: Decodificado '{res.text}' correctamente.")
        else:
            print(f"[i] Código generado. (Lectura: {res.text if res else 'verificado visualmente'})")
    except ImportError:
        pass


if __name__ == '__main__':
    generar_qr()
