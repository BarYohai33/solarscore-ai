
print("=== SolarScore AI ===")

owner = input("Le client est-il propriétaire ? (oui/non) : ").strip().lower()

if owner == "oui":
    print("Statut : RDV valide")
elif owner == "non":
    print("Statut : RDV non valide")
else:
    print("Erreur : veuillez répondre par oui ou non.")
