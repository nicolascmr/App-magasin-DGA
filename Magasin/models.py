from .app import db

class Produit(db.Model):
    __tablename__ = 'Produit'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reference = db.Column(db.String(50), unique=True) 
    nom = db.Column(db.String(100))
    quantite = db.Column(db.Integer)
    fabricant = db.Column(db.String(100))

    def __init__(self, reference, nom, quantite, fabricant):
        self.reference = reference
        self.nom = nom
        self.quantite = quantite
        self.fabricant = fabricant

    def __repr__(self):
        return f"<Produit {self.reference} - {self.nom}>"
