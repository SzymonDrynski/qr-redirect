# QR Redirect System

System przekierowań dla sal szkoleniowych oparty o GitHub Pages i harmonogram z pliku Excel.

## Jak działa

- Codziennie o 7:00 (czasu PL) uruchamia się GitHub Action.
- Wczytuje harmonogram z `data/schedule.xlsx`.
- Tworzy strony przekierowujące w `pages/salaX.html`.
- QR prowadzi na stałą stronę (`sala1.html`), która dynamicznie przekierowuje.

## Harmonogram

Plik Excel (`schedule.xlsx`) powinien mieć kolumny:

| Data       | Sala     | Link                    |
|------------|----------|-------------------------|
| 2025-04-25 | Sala 1   | https://example.com/1   |
