# rename_gpx-filenames_inside-GPX

## GPX-Datei-Umbenennungsskript
Dieses Python-Skript ist dafür konzipiert, GPX-Dateien umzubenennen und sie basierend auf dem Erfolg des Umbenennungsprozesses in entsprechende Ordner zu verschieben.

## Beschreibung
Das Skript durchsucht den Ordner ./GPX/ nach GPX-Dateien und versucht, jede Datei umzubenennen. Der neue Name wird aus dem Dateinamen ohne Erweiterung generiert. Dies geschieht, indem der Inhalt zwischen den <name> und </name> Tags durch den Dateinamen ersetzt wird.

Nach dem Umbenennungsprozess wird die Datei in den Ordner ./done/ verschoben, wenn der Umbenennungsprozess erfolgreich war. Wenn beim Umbenennen ein Fehler auftritt, wird die Datei in den Ordner ./fail/ verschoben.

Die Ordner ./done/ und ./fail/ werden automatisch erstellt, wenn sie noch nicht existieren.
