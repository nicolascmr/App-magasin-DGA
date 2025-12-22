from flask import redirect, render_template, request, url_for
from Magasin.forms import ProduitForm
from Magasin.models import Produit
from .app import app,db
from sqlalchemy import or_


@app.route("/", methods=['GET','POST'])
def home():

    if request.method == 'POST':
        filtre = request.form.get('filtre')
    else:
        filtre = request.args.get('filtre')

    recherche = request.args.get('recherche')

    query = Produit.query

    print("FILTRE", filtre)
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
    
    form = ProduitForm()
    if form.validate_on_submit():
        form.creer_produit(filtre)

    if recherche:
        recherches = recherche.strip().split(" ")
        data = []
        for mot in recherches:
            motif = f'{mot}%'
            query = query.filter(
                or_(
                    Produit.reference.like(motif),
                    Produit.nom.like(motif),
                    Produit.fabricant.like(motif)
                )
            )
        

    data = query.all()

    page = request.args.get('page', 1, type=int)

    produits, page = _pagination(data, page)
    
    return render_template("home.html", form=form, produits=produits, page=page, filtre_actif=filtre)

@app.route('/supression/', methods=['POST'])
def supprimer_produit():

    id = request.form.get("id")
    produit = Produit.query.get(id)
    if produit:
        db.session.delete(produit)
        db.session.commit()

    filtre = request.values.get('filtre')
    return redirect(url_for('home', filtre=filtre))

@app.route('/recherche/', methods=['POST'])
def rechercher_produit():
    recherche = request.values.get('recherche')
    filtre = request.values.get('filtre')
    
    return redirect(url_for('home', filtre=filtre, recherche=recherche))


def _pagination(data, page, element_par_page: int = 5):
    if page < 1:
        page = 1
    elif page > (len(data) - 1) // element_par_page + 1:
        page = (len(data) - 1) // element_par_page + 1

    debut = (page - 1) * element_par_page
    fin = debut + element_par_page

    return data[debut:fin], page
