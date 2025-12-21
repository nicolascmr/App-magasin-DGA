from flask import redirect, render_template, request, url_for
from Magasin.models import Produit
from .app import app,db

@app.route("/")
def home():
    data = Produit.query.all()

    page = request.args.get('page', 1, type=int)

    produits, page = _pagination(data, page)
    
    return render_template("home.html", produits=produits, page=page)

def _pagination(data, page, element_par_page: int = 5):
    if page < 1:
        page = 1
    elif page > (len(data) - 1) // element_par_page + 1:
        page = (len(data) - 1) // element_par_page + 1

    debut = (page - 1) * element_par_page
    fin = debut + element_par_page

    return data[debut:fin], page
