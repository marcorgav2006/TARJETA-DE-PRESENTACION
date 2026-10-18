# Tarjeta Digital Ejecutiva - Ing. Bella Gavilanes

Tarjeta de presentación digital corporativa para **Ing. Bella Gavilanes**, Gerente de Cadena de Abastecimiento en **Grupo Alessa &bull; Alessa S.A.**

Sitio en producción: **[https://marcorgav2006.github.io/TARJETA-DE-PRESENTACION/](https://marcorgav2006.github.io/TARJETA-DE-PRESENTACION/)**

---

## Características Principales

* **Diseño Mobile-First:** Optimizado para visualización fluida en cualquier smartphone y centrado en pantallas de escritorio.
* **Identidad Corporativa Grupo Alessa:** Paleta de azules institucionales (`#074574`, `#0A5386`, `#0085CA`), tipografía de alta legibilidad y logotipo corporativo oficial en alta resolución.
* **Efecto de Iluminación de Contornos (NameDrop feedback):** Resplandor perimetral estático en los bordes de la pantalla al guardar contacto con respuesta háptica y notificación superior.
* **Descarga vCard 3.0:** Genera y descarga el archivo estándar `Bella_Gavilanes_Alessa.vcf` compatible con la agenda de contactos de iOS (iPhone) y Android.
* **Enlaces de Contacto Rápido:**
  * Teléfono: `+593 99 746 0811` (llamada directa y WhatsApp)
  * Correo corporativo: `bella.gavilanes@alessa.com.ec`
* **Código QR Estático de Alta Fidelidad:**
  * Generado con `generar_qr.py` en 2000 × 2000 px (300 DPI) para imprenta y 800 × 800 px para pantalla web.
  * Ojos de localización personalizados y logotipo de Grupo Alessa integrado con corrección de error `ERROR_CORRECT_H` (30%).

---

## Archivos del Proyecto

* `index.html`: Archivo autocontenido de producción (HTML5, CSS3 nativo, JavaScript vanilla sin dependencias externas).
* `generar_qr.py`: Script en Python con `qrcode` y `Pillow` para generar el código QR.
* `foto.jpg`: Fotografía de perfil oficial.
* `logo_alessa.png` / `logo_alessa_azul.png`: Logotipos oficiales en alta definición.
* `qr_tarjeta.png`: Versión web del código QR para visualización directa en la tarjeta.
* `qr_tarjeta_alta_resolucion.png`: Código QR en alta resolución (300 DPI) para imprenta física o tarjetas de PVC.

---

## Despliegue en GitHub Pages

1. Ve a **Settings** > **Pages** en el repositorio.
2. En **Build and deployment** > **Source**, selecciona `Deploy from a branch`.
3. Selecciona la rama `main` y la carpeta `/ (root)`.
4. Haz clic en **Save**. En 1 o 2 minutos tu tarjeta estará activa en:
   `https://marcorgav2006.github.io/TARJETA-DE-PRESENTACION/`
