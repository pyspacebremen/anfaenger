# Tupel
# Ein Tupel ist eine unveränderbare Sequenz.
# Ein Tupel kann aus Items mit beliebigen Datentypen zusammen gesetzt sein.
# Tupel werden in runden Klammern gesetzt und durch Komma getrent.


t = (1, 2, 3)
print(t)
print(type(t))

# Listen
# Eine Liste ist eine veränderbare Sequenz.
# Eine Liste kann aus Items mit beliebigen Datentypen zusammen gesetzt sein.
# Listen werden in eckigen Klammern gesetzt und durch Komma getrent.


l = [1,2,3]
print(l)
print(type(t))
# print(l[0])
l[1] = "Hallo"
print(l)


# Ein Dictionary ist eine veränderbare Sequenz aus Wertpaaren.
# Es ermöglicht einen Zugrif auf Werte(value) über einen Schlüssel(key).
# Ein Dictionary mit Wertpaaren wird in geschweiften Klammern gesetzt und durch Komma getrent.
# Ein Wertpaar besteht immer aus einen Schlüssel(key) und einen Wert(value)
# und diese werden durch einen Doppelpunkt getrennt.


d = {"eins":1,"zwei":2,"drei":3}
print(d)
print(d[0])
print(d["eins"])
d["zwei"] = "Hallo"
print(d)

