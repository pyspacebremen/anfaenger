import random

def quiz():
    print("🎮 Willkommen zum Zahlenraten-Spiel!")
    print("Ich denke an eine Zahl zwischen 1 und 10. Rate sie!")

    zufallszahl = random.randint(1, 10)
    versuche = 0

    while True:
        versuche += 1
        rateversuch = input("Dein Tipp: ")

        # Eingabe prüfen
        if not rateversuch.isdigit():
            print("❌ Bitte eine Zahl eingeben!")
            continue

        rateversuch = int(rateversuch)

        if rateversuch < zufallszahl:
            print("Zu niedrig! 🔽")
        elif rateversuch > zufallszahl:
            print("Zu hoch! 🔼")
        else:
            print(f"🎉 Richtig! Du hast {versuche} Versuche gebraucht!")
            break

# Spiel starten
quiz()
