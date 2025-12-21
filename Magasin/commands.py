from .app import app, db
from .models import Produit

@app.cli.command()
def init_db():
    """Initialiser la base de données."""
    db.drop_all()
    db.create_all()
    db.session.add(Produit("REF-001", "Bois", "Point P", 1))
    db.session.add(Produit("REF-002", "Verre", "Point P", 1))
    db.session.add(Produit("REF-003", "Sable", "Point P", 1))
    db.session.add(Produit("REF-004", "Ciment", "Point P", 1))
    db.session.add(Produit("REF-005", "Terre", "Point P", 1))
    db.session.add(Produit("REF-006", "Plastique", "Point P", 1))
    db.session.add(Produit("REF-007", "PVC", "Point P", 1))
    db.session.add(Produit("REF-008", "Beton", "Point P", 1))
    db.session.add(Produit("REF-009", "Fer", "Point P", 1))
    db.session.add(Produit("REF-010", "Aluminium", "Point P", 1))
    db.session.commit()
    print("Base de données initialisée !")