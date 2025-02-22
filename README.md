# getevent_to_sendevents
🚀 AVD Tool – Konvertiere AVD-Events in Shell-Skript

Das getevent_to_sendevents.py Skript ist ein praktisches Werkzeug, das aufgezeichnete Events von Android Virtual Devices (AVD) in ausführbare Shell-Skripte konvertiert. Mit diesem Tool kannst du wiederkehrende Aktionen automatisieren, Tests beschleunigen und AVD-Interaktionen effizient reproduzieren.

# Warum das Skript?
- getevent gibt Hex-Werte aus → nicht direkt nutzbar für sendevent.
- sendevent benötigt Dezimalwerte → Umwandlung notwednig.
- Zusätzliche Anpassungen am Sendevent.sh notwendig, damit die Befehle direkt ausgeführt werden können
- Lösung: Umwandlung per Skript

# Anwendung
1) Verbindung per ADB zur Shell auf dem Gerät
2) ADB Shell> getevent
3) Aktionen auf dem Display (AVD) durchführen
4) getevent mit STRG+C beenden
5) Copy&Paste der Aufzeichung in die Datei getevent_input.txt
6) Ausführen des Skripts getevent_to_sendevents.py
7) ADB push sendevent.sh /sdcard/sendevent.sh
8) ADB Shell /sdcard/sendevent.sh

#FAQ
- Das Skript und die Datei getevent_input.txt müssen im gleichen Verzeichnis liegen.
