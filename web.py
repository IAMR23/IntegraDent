from PIL import Image
import os

def convert_images_to_webp(folder_path):
    if not os.path.exists(folder_path):
        print("La carpeta no existe.")
        return
    
    output_folder = os.path.join(folder_path, "webp")
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
            try:
                img = Image.open(file_path)
                webp_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
                img.save(webp_path, "webp")
                print(f"Convertido: {filename} -> {webp_path}")
            except Exception as e:
                print(f"Error al convertir {filename}: {e}")

if __name__ == "__main__":
    carpeta = input("Ingrese la ruta de la carpeta con imágenes: ")
    convert_images_to_webp(carpeta)