# DEVOPS - TP3

# 🎯  Objectifs:

1. Deployer sur Azure Container Instance (ACI) using Github Actions
2. Mettre à disposition son image sur DockerHub
3. Mettre à disposition son code dans un repository Github

### Constitution du TP :

1. Workflow : Représente le flux des opérations effectuées sur le GIT
2. Dockerfile : Fichier texte qui contient les instructions nécessaires à la création d'une image de conteneur.
3. Le code en python

### Requirements du tp:

requests

datetime 

flask

### Commandes :

1. Création d’un nouveau repository.
    
    ![Untitled](DEVOPS%20-%20TP3%2055abcbdbb10e4070aa6062a89d5c1f7b/Untitled.png)
    

1. Création du workflow (modification selon ID Efrei)
    
    ![Untitled](DEVOPS%20-%20TP3%2055abcbdbb10e4070aa6062a89d5c1f7b/Untitled%201.png)
    
2. Création de repo secret pour cacher l’API KEY et l’ID Efrei
    
    ![Untitled](DEVOPS%20-%20TP3%2055abcbdbb10e4070aa6062a89d5c1f7b/Untitled%202.png)
    
    Les identifiants secrets pour Azure sont eux déjà prédéfinis dans un repo secrets (données sensibles)
    
    ![Untitled](DEVOPS%20-%20TP3%2055abcbdbb10e4070aa6062a89d5c1f7b/Untitled%203.png)
    
3. Exécution du workflow 
    
    ![Untitled](DEVOPS%20-%20TP3%2055abcbdbb10e4070aa6062a89d5c1f7b/Untitled%204.png)
    

1. Lorsque le Job du workflow est fini on lance la commande pour vérifier que ca marche correctement : 

> curl “http://devops-20190780.francecentral.azurecontainer.io/?lat=5.902785&lon=102.754175”
> 

![Untitled](DEVOPS%20-%20TP3%2055abcbdbb10e4070aa6062a89d5c1f7b/Untitled%205.png)

# Bonus : ****✅****

1. Add hadolint to Github workflow before build+push and failed on errors:

**On ajoute dans le work flow les lignes suivantes**

![Untitled](DEVOPS%20-%20TP3%2055abcbdbb10e4070aa6062a89d5c1f7b/Untitled%206.png)

1. Aucune données sensibles stockées dans l'image ou le code source (i.e: openweather API key, Docker hub credentials)

**Toutes les données que j’ai jugé personnelles/sensibles ont été caché et mis dans un repo secret dans le but afin de remédier aux soucis de données sensibles stockées.**

![Untitled](DEVOPS%20-%20TP3%2055abcbdbb10e4070aa6062a89d5c1f7b/Untitled%202.png)