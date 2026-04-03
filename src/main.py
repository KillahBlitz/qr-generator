


import qrcode
from pathlib import Path
from datetime import datetime

def qr_generator(url):
    output_dir = Path(__file__).parent / "qrs"
    output_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"qr_{timestamp}.png"
    file_path = output_dir / filename
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(str(file_path))
    
    return str(file_path)

if __name__ == "__main__":
    print("Programa para generar códigos QR")
    quantity = int(input("¿Cuántos códigos QR deseas generar? "))
    for i in range(quantity):
        print(f"\nGenerando código QR {i+1} de {quantity}")
        url = input("Ingresa la URL o texto para el código QR: ")
        route_save = qr_generator(url)
        print(f"Código QR guardado en: {route_save}")