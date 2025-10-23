student = {
    "jmeno": "Lucie",
    "prijmeni": "Svododová",
    "znamky": [1, 2, 3, 1, 1, 1, 3, 1, 1, 1, 2, 1, 1]
}

prumer = sum(student["znamky"]) / len(student["znamky"])

if not (5 in student["znamky"]):
    if prumer <= 1.5:
        print("Výborný prospěch.")
    elif prumer <= 2:
        print("Není to zlé.")
    else:
        print("Je to zlé.")
else:
    print("Průser. Neprospěl/a")
