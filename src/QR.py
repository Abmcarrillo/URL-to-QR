import qrcode
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def generar_qr_con_logo(url, logo_path, output_path):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    logo = Image.open(logo_path)
    logo_size = img_qr.size[0] // 4
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
    pos = ((img_qr.size[0] - logo.size[0]) // 2, (img_qr.size[1] - logo.size[1]) // 2)
    img_qr.paste(logo, pos)
    img_qr.save(output_path)
    messagebox.showinfo("Éxito", f"QR generado y guardado en {output_path}")

def seleccionar_logo():
    logo_path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png *.jpg *.jpeg")])
    if logo_path:
        entry_logo.delete(0, tk.END)
        entry_logo.insert(0, logo_path)

def seleccionar_destino():
    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
    if output_path:
        entry_destino.delete(0, tk.END)
        entry_destino.insert(0, output_path)

def generar():
    url = entry_url.get()
    logo_path = entry_logo.get()
    output_path = entry_destino.get()
    if url and logo_path and output_path:
        generar_qr_con_logo(url, logo_path, output_path)
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

ventana = tk.Tk()
ventana.title("Generador de QR con Logo Personalizado by @abmcarrillo")

tk.Label(ventana, text="URL:").grid(row=0, column=0, padx=10, pady=10)
entry_url = tk.Entry(ventana, width=40)
entry_url.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Logo:").grid(row=1, column=0, padx=10, pady=10)
entry_logo = tk.Entry(ventana, width=40)
entry_logo.grid(row=1, column=1, padx=10, pady=10)
tk.Button(ventana, text="Examinar", command=seleccionar_logo).grid(row=1, column=2, padx=10, pady=10)

tk.Label(ventana, text="Guardar en:").grid(row=2, column=0, padx=10, pady=10)
entry_destino = tk.Entry(ventana, width=40)
entry_destino.grid(row=2, column=1, padx=10, pady=10)
tk.Button(ventana, text="Examinar", command=seleccionar_destino).grid(row=2, column=2, padx=10, pady=10)

tk.Button(ventana, text="Generar QR", command=generar).grid(row=3, column=1, padx=10, pady=20)

ventana.mainloop()
