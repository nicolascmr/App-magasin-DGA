from flask import redirect, render_template, request, url_for
from Magasin.forms import ProduitForm
from Magasin.models import Produit
from .app import app,db
from sqlalchemy import or_

@app.route("/")
def home():
    """
    Affiche la page d'acceuil du site web
    """
    return render_template("home.html")

@app.route("/gestion_produits/", methods=['GET','POST'])
def gestion_produits():
    """
    Affiche la page de gestion de produits et gère l'utilisation des fonctionnalités de la page
    """
    # Création du formulaire pour la création du produit
    form = ProduitForm()
    # Si il y a une validation du formulaire de création d'un produit il est créé et la page est rafraichie en gardant le filtre actif
    if form.validate_on_submit():
        return form.creer_produit(request.form.get('filtre'))
    # Si il y a nouvel changement de filtre la page est actualisée
    if request.method == 'POST' and 'submit' not in request.form:
        filtre = request.form.get('filtre')
        return redirect(url_for('gestion_produits', filtre=filtre))
    
    filtre = request.args.get('filtre')
    recherche = request.args.get('recherche')

    query = Produit.query

    # Filtre selon le filtre choisi et si rien est sélection on filtre par référence
    match filtre:
        case 'reference':
            query = query.order_by(Produit.reference)
        case 'nom':
            query = query.order_by(Produit.nom)
        case 'fabricant':
            query = query.order_by(Produit.fabricant)
        case 'quantite':
            query = query.order_by(Produit.quantite)
        case default:
            query = query.order_by(Produit.reference)
    # Si il y a une recherche l'ensemble des mots sont mis dans la liste data
    if recherche:
        recherches = recherche.strip().split(" ")
        data = []
        #Pour chaque mot de la recherche les données sont affinés pour chaque élement existant 
        for mot in recherches:
            motif = f'{mot}%'
            query = query.filter(
                or_(
                    Produit.reference.like(motif),
                    Produit.nom.like(motif),
                    Produit.fabricant.like(motif)
                )
            )
        
    # Toutes les données sont récupérées selon les élements choisis auparavant
    data = query.all()

    page = request.args.get('page', 1, type=int)

    # La fonction pagination affiche les données à afficher selon la page
    produits, page = _pagination(data, page)
    
    return render_template("gestion_produits.html", form=form, produits=produits, page=page, filtre_actif=filtre)

@app.route("/gestion_produits/<string:produit_id>/", methods=["GET", "POST"])
def detail_produit(produit_id):
    """
    Affiche la page de détail produit et permet la modification du produit
    
    @param produit_id: L'id du produit sélectionné
    """
    # Le produit est récupéré par son id
    produit = Produit.query.filter_by(id=produit_id).first()
    # Création du formulaire avec les données pour pré-remplir les champs
    form = ProduitForm(obj=produit)
    # Si il y a une validation du formulaire le produit est modifié
    if form.validate_on_submit():
        form.modifier_produit(produit_id)

    return render_template("detail_produit.html", produit=produit, form=form)

@app.route('/supression/', methods=['POST'])
def supprimer_produit():
    """
    S'occupe de supprimer le produit sélectionner
    """

    id = request.form.get("id")
    produit = Produit.query.get(id)
    # Si le produit exite il est supprimé
    if produit:
        db.session.delete(produit)
        db.session.commit()

    filtre = request.values.get('filtre')
    return redirect(url_for('gestion_produits', filtre=filtre))

@app.route('/recherche/', methods=['POST'])
def rechercher_produit():
    """
    S'occupe de la recherche
    """
    recherche = request.values.get('recherche')
    filtre = request.values.get('filtre')
    
    return redirect(url_for('gestion_produits', filtre=filtre, recherche=recherche))


def _pagination(data, page, element_par_page: int = 5):
    """
    Récupère les produits à afficher selon la page et l'ensemble des données
    
    @param data: L'ensemble des données
    @param page: La page actuelle
    @param element_par_page: Le nombre d'éléement que l'on souhaite afficher
    @type element_par_page: int
    """
    # Empeche d'aller à une page où il n'y a pas de données
    if page < 1:
        page = 1
    elif page > (len(data) - 1) // element_par_page + 1:
        page = (len(data) - 1) // element_par_page + 1

    debut = (page - 1) * element_par_page
    fin = debut + element_par_page

    return data[debut:fin], page
