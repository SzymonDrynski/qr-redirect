import pandas as pd
from datetime import datetime
from pathlib import Path

BASE_URL = "https://szymondrynski.github.io/qr-redirect/pages"
EXCEL_FILE = "data/schedule.xlsx"
OUTPUT_DIR = Path("pages")

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    df = pd.read_excel(EXCEL_FILE)

    for sala in range(1, 7):
        sala_id = f"Sala {sala}"
        row = df[(df["Data"] == today) & (df["Sala"] == sala_id)]
        url = row["Link"].values[0] if not row.empty else "https://szymondrynski.github.io/qr-redirect/pages/nolink.html"

        html = f"""<html><head>
        <meta http-equiv='refresh' content='0; url={url}'>
        </head><body>
        <p>Przekierowuję do <a href='{url}'>{url}</a></p>
        </body></html>"""

        OUTPUT_DIR.mkdir(exist_ok=True)
        with open(OUTPUT_DIR / f"sala{sala}.html", "w") as f:
            f.write(html)

if __name__ == "__main__":
    main()
