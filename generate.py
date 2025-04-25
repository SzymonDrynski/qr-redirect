import pandas as pd
import os
import qrcode
from datetime import datetime

# Ścieżki
excel_file = 'schedule.xlsx'  # Ścieżka do pliku Excel
output_dir = 'pages'  # Folder, w którym będą generowane strony

# Załaduj dane z pliku Excel
df = pd.read_excel(excel_file)

# Dziś
today = datetime.today().strftime('%Y-%m-%d')

# Funkcja do generowania QR kodu
def generate_qr_code(link, sala):
    qr = qrcode.make(link)
    qr_path = os.path.join(output_dir, f'{sala}.png')
    qr.save(qr_path)
    return qr_path

# Funkcja do tworzenia pliku HTML
def create_html(sala, link=None):
    if link:
        html_content = f"""
        <html>
        <head><title>{sala}</title></head>
        <body>
            <h1>Przekierowanie do {sala}</h1>
            <meta http-equiv="refresh" content="0; url={link}">
        </body>
        </html>
        """
    else:
        html_content = """
        <html>
        <head><title>Brak strony</title></head>
        <body>
        <h1>Nie zaplanowano strony dla tej sali na dziś.</h1>
        </body>
        </html>
        """
    
    # Zapisz plik HTML
    html_file = os.path.join(output_dir, f'{sala}.html')
    with open(html_file, 'w') as f:
        f.write(html_content)

# Tworzenie stron i QR kodów
for _, row in df.iterrows():
    sala = row['Sala']
    link = row.get('Link', None)
    
    if pd.to_datetime(row['Data']).strftime('%Y-%m-%d') == today:
        # Tworzenie strony HTML i QR kodu
        create_html(sala, link)
        
        if link:
            generate_qr_code(link, sala)
        else:
            # Stwórz stronę bez linku (z komunikatem)
            create_html(sala)
