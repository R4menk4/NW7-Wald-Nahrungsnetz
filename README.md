# Wer frisst wen? – eigenständiges Lernprogramm

Die fertige Lernanwendung liegt in dist. dist/index.html kann direkt im Browser geöffnet werden; alle Bilder liegen lokal unter dist/assets. Es werden keine Schülerdaten versendet oder dauerhaft gespeichert. Antworten bleiben beim Wechsel zwischen Lernschritten erhalten, solange die Seite geöffnet bleibt; Neuladen setzt sie zurück.

Für GitHub Pages liegt zusätzlich eine `index.html` im Hauptordner. Sie öffnet automatisch das Lernprogramm unter `dist/`. In den GitHub-Einstellungen muss Pages aus dem gewünschten Branch und dem Ordner `/ (root)` veröffentlicht werden.

Enthalten ist ausschließlich die selbstständig zu bearbeitende Unterrichtseinheit „Wer frisst wen?“ für die Klasse 7.

Prüfung: node verify.cjs. Statische Vorschau: node preview.cjs.

## Unterrichtsersatz: Wer frisst wen?

Geführter Lernweg zum Arbeitsblatt „3.2 Wer frisst wen?“ mit sechs Schritten: Pfeilregel wiederholen, acht Organismenkarten per Drag-and-drop frei in die Ebenen Produzenten, Erstkonsumenten und Zweitkonsumenten einordnen, das individuelle Nahrungsnetz verbinden und auswerten, den Vorteil eines Nahrungsnetzes erklären und Folgen seltener Waldmäuse vorhersagen. Das Arbeitsblatt liegt als Begleitmaterial unter `dist/assets/arbeitsblatt-wer-frisst-wen.pdf`.

Die Netzaufgabe verwendet die Organismenkarten aus `3 Wer frisst wen/M1_Organismenkarten_einzeln`. Verbindungen werden durch Anklicken von Nahrung und Fresser gesetzt, können einzeln entfernt und geprüft werden. Mehrere fachlich passende Antworten bei den Aufgaben 2 und 3 werden akzeptiert. Alle Daten bleiben im Browser und gehen beim Neuladen verloren.

WebMCP: Das optionale Werkzeug `set_foodweb_connections` wird bei API-Verfügbarkeit registriert.
