# techsecure-web-app
# TechSecure Solutions - Portails Métiers Sécurisés

Ce projet déploie une application web Flask connectée à une base de données MySQL, le tout entièrement conteneurisé avec Docker. Aucune installation locale de Python ou dépendances n'est requise.

## Fonctionnalités Sécurité Intégrées
- **Sécurité applicative** : Requêtes SQL paramétrées (anti-injection).
- **Mots de passe** : Chiffrement/Vérification via hachage Bcrypt.
- **Sécurité Docker** : Réseau isolé, aucun port de base de données exposé publiquement.

---

## Instructions de Test (Pour correction ou déploiement tiers)

### Prérequis
Avoir installé **Docker Desktop** et lancé l'application sur sa machine.

### Étape 1 : Cloner le projet
```bash
git clone <URL_DU_DEPOT>
cd techsecure-web-app