from sqlite3 import IntegrityError
from flask import flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

from Magasin.models import Produit
from .app import db

class ProduitForm(FlaskForm):
    reference = StringField('Référence', validators=[DataRequired(), Length(max=50)])
    nom = StringField('Nom', validators=[DataRequired(), Length(max=100)])
    fabricant = StringField('Fabricant', validators=[DataRequired(), Length(max=100)])
    quantite = IntegerField('Quantité', validators=[DataRequired(), NumberRange(min=0, message="La quantité ne peut pas être négative")])
    submit = SubmitField('Ajouter le produit')

    def creer_produit(self, filtre):
        """
        Crée le produit en vérifiant que le produit ayant la même référence n'existe pas déja
        
        @param filtre: Le filtre actif
        """
        produit = Produit.query.filter_by(reference=self.reference.data).first()
        print("produit", produit)
        if not produit:
            try:
                produit = Produit(
                    reference=self.reference.data,
                    nom=self.nom.data,
                    fabricant=self.fabricant.data,
                    quantite=self.quantite.data
                )
                db.session.add(produit)
                db.session.commit()
                # Affiche le message de validation de création du produit sur la page
                flash("Produit ajouté avec succès !")
            except IntegrityError as e:
                print(f"Erreur avec la base de donnée lors de la création du produit: {e}")
                # Affiche le message d'erreur sur la page
                flash("Erreur avec la base de donnée lors de la création du produit", "error")
        else:
            flash("Impossible de créer deux produits qui portent la même référence !", "error")
        return redirect(url_for('gestion_produits', filtre=filtre))
    
    def modifier_produit(self, produit_id):
        try:
            produit = Produit.query.filter_by(id=produit_id).first()
            produit.nom = self.nom.data
            produit.fabricant = self.fabricant.data
            produit.quantite = self.quantite.data
            db.session.commit()
            flash("Produit modifié avec succès !")
        except IntegrityError as e:
            print(f"Erreur avec la base de donnée lors de la création du produit: {e}")
            flash("Erreur avec la base de donnée lors de la création du produit", "error")
        return redirect(url_for('detail_produit', produit_id=produit_id))