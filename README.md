# getevent_to_sendevents
🚀 AVD Tool – Konvertiere AVD-Events in Shell-Skripte  

Das AVD Tool ist ein praktisches Werkzeug, das aufgezeichnete Events von Android Virtual Devices (AVD) in ausführbare Shell-Skripte konvertiert. Mit diesem Tool kannst du wiederkehrende Aktionen automatisieren, Tests beschleunigen und AVD-Interaktionen effizient reproduzieren.

# Warum das Skript?
- getevent gibt Hex-Werte aus → nicht direkt nutzbar für sendevent.
- sendevent benötigt Dezimalwerte → Umwandlung notwednig.
- Zusätzliche Anpassungen am Sendevent.sh notwendig, damit die Befehle direkt ausgeführt werden können
- Lösung: Umwandlung per Skript
