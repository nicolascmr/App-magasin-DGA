from sqlite3 import IntegrityError
from flask import flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired

from Magasin.models import Produit
from .app import db,app

class ProduitForm(FlaskForm):
    reference = StringField('Référence', validators=[DataRequired()])
    nom = IntegerField('Nom', validators=[DataRequired()])
    fabricant = FloatField('Fabricant', validators=[DataRequired()])
    quantite = IntegerField('Quantité', validators=[DataRequired()])
    submit = SubmitField('Ajouter le produit')

    def create_produit(self, filtre):
        produit = Produit.query.filter_by(reference=self.reference.data).first()
        if not produit:
            try:
                produit = Produit(
                    reference=self.reference.data,
                    nom=self.nom.data,
                    fabricant=self.fabricant.data,
                    quantite=self.quantite.data
                )
                db.session.add(produit)
                print(produit)
                db.session.commit()
                flash("Plateforme créée avec succès !")
            except IntegrityError as e:
                print(f"Erreur avec la base de donnée lors de la création du produit: {e}")
                flash("Erreur avec la base de donnée lors de la création du produit", "error")
        else:
            flash("Impossible de créer deux produits qui portent le même nom !", "error")
        return redirect(url_for('home', filtre=filtre))