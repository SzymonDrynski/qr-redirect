import pandas as pd
from datetime import datetime
from pathlib import Path

BASE_URL = "https://szymondrynski.github.io/qr-redirect/pages"
EXCEL_FILE = "data/schedule.xlsx"
OUTPUT_DIR = Path("pages")

# Lista nazw sal
sale = ["Van", "PC", "Poznań I", "Poznań II", "Bieszczady I", "Bieszczady II"]
sala_to_filename = {
    "Van": "van",
    "PC": "pc",
    "Poznań I": "poznan1",
    "Poznań II": "poznan2",
    "Bieszczady I": "bieszczady1",
    "Bieszczady II": "bieszczady2"
}

def main():
    today = pd.Timestamp.now().strftime("%Y-%m-%d")
    df = pd.read_excel(EXCEL_FILE)

    for sala in sale:
        row = df[(df["Data"] == today) & (df["Sala"] == sala)]
        url = row["Link"].values[0] if not row.empty else "https://szymondrynski.github.io/qr-redirect/pages/nolink.html"
        filename = sala_to_filename[sala]

        html = f"""<html><head>
        <meta http-equiv='refresh' content='0; url={url}'>
        </head><body>
        <p>Przekierowuję do <a href='{url}'>{url}</a></p>
        </body></html>"""

        OUTPUT_DIR.mkdir(exist_ok=True)
        with open(OUTPUT_DIR / f"{filename}.html", "w", encoding="utf-8") as f:
            f.write(html)

if __name__ == "__main__":
    main()
