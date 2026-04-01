from playwright.sync_api import sync_playwright
from datetime import datetime
import os

URL = "https://itar.com.ar/producto/bs-cemento-x-25kg/"

def tomar_captura():
    fecha = datetime.now().strftime("%Y-%m-%d")
    nombre_archivo = f"captura_{fecha}.png"
    carpeta = "capturas"

    os.makedirs(carpeta, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 900})

        print(f"Abriendo {URL} ...")
        page.goto(URL, wait_until="networkidle", timeout=30000)

        # Espera extra por si hay contenido dinámico
        page.wait_for_timeout(3000)

        ruta = os.path.join(carpeta, nombre_archivo)
        page.screenshot(path=ruta, full_page=True)
        browser.close()

        print(f"Captura guardada: {ruta}")

if __name__ == "__main__":
    tomar_captura()
