#HotLemon
##Objectif du projet
L’application permettra à l'utilisateur de rédiger ou de partager un article, une annonce, un évènement dans sa zone géographique. Le système sera donc participatif, avec possibilité de voter de manière positive ou négative sur chaque news. Les articles mal notés disparaissent.
Le système comprendra également des filtres. Les utilisateurs pourront aussi sélectionner leurs centres d'intérêt et ainsi former des communautés.
##Technologie
Le projet sera basé sur django à l'aide du Framwork REST.
Voir le site de [Django](https://www.djangoproject.com/) et de [REST Framework](http://www.django-rest-framework.org/).
##Installation PyCharm (IDE)
1. Télécharger pycharm et créer un compte étudiant.
2. Télécharger git windows et installer le.
3. Paramètrer le répository dans pycharm.
4. Créer une branche personnel et faire un checkout sur cette branche.
##Démarrer le service django
dossier courant: hotlemon
1. create a virtual environment 
1. pip install -r requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py collectstatic
5. python manage.py createsuperuser
6. python manage.py runserver

## Tuto Git - Pour commit
1. git status
2. git commit -m "Insert message here"
3. git push

# Tuto Git - Pour update
1. git pull
