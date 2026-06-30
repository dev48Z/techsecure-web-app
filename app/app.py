import os
import time  # <-- IL MANQUAIT CETTE LIGNE !
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
import mysql.connector

app = Flask(__name__)
app.secret_key = 'techsecure_ultra_secret_key'
bcrypt = Bcrypt(app)

# Configuration de la base de données via variables d'environnement
DB_HOST = os.environ.get('DB_HOST', 'db')
DB_USER = os.environ.get('DB_USER', 'techuser')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'techpass')
DB_NAME = os.environ.get('DB_NAME', 'techsecure_db')

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# Dictionnaire contenant le contenu textuel propre à chaque service exigé
SERVICES_DATA = {
    'infra': {
        'title': "Administration des Infrastructures",
        'desc': "Gestion de parcs, serveurs, supervision réseau et maintien opérationnel.",
        'image': "entreprise.jpg"  # Image pour l'infrastructure
    },
    'cyber': {
        'title': "Cybersécurité",
        'desc': "Audits de sécurité, tests d'intrusion, remédiation et gouvernance SSI.",
        'image': "cyber.jpg"       # Image pour la cyber
    },
    'cloud_pme': {
        'title': "Services Cloud PME",
        'desc': "Migration Cloud, architectures hybrides et sauvegardes externalisées.",
        'image': "cloud.jpg"       # Image pour le cloud PME
    },
    'collectivites': {
        'title': "Cloud Collectivités",
        'desc': "Hébergement souverain de données publiques et conformité RGPD.",
        'image': "lyon.jpg"       # Image pour les collectivités
    }
}

@app.route('/')
def index():
    return render_template('base.html', services=SERVICES_DATA)

@app.route('/login/<service_id>', methods=['GET', 'POST'])
def login(service_id):
    if service_id not in SERVICES_DATA:
        return "Service introuvable", 404
        
    service = SERVICES_DATA[service_id]
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            
            # SÉCURITÉ : Requête SQL paramétrée (évite les injections SQL)
            query = "SELECT * FROM users WHERE username = %s AND service_id = %s"
            cursor.execute(query, (username, service_id))
            user = cursor.fetchone()
            
            cursor.close()
            conn.close()
            
            # SÉCURITÉ : Vérification robuste du mot de passe haché avec Bcrypt
            if user and bcrypt.check_password_hash(user['password_hash'], password):
                return redirect(url_for('service_page', service_id=service_id))
            else:
                flash("Identifiants incorrects ou accès non autorisé pour ce service.", "danger")
        except Exception as e:
            flash("Erreur lors de la connexion à la base de données.", "danger")
            
    return render_template('login.html', service=service, service_id=service_id)

@app.route('/service/<service_id>')
def service_page(service_id):
    if service_id not in SERVICES_DATA:
        return "Accès interdit", 403
    return render_template('service.html', service=SERVICES_DATA[service_id])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
