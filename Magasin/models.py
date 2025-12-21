from .app import db

class Produit(db.Model):
    __tablename__ = 'Produit'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reference = db.Column(db.String(50), unique=True) 
    nom = db.Column(db.String(100))
    fabricant = db.Column(db.String(100))
    quantite = db.Column(db.Integer)

    def __init__(self, reference, nom, fabricant, quantite):
        self.reference = reference
        self.nom = nom
        self.fabricant = fabricant
        self.quantite = quantite


    def __repr__(self):
        return f"<Produit {self.reference} - {self.nom}>"
