# DEVOPS - TP1

## Objectifs:

1) Créer un wrapper qui retourne la météo d'un lieu donné avec sa latitude et sa longitude 
en utilisant openweather API en Python.
2) Packager son code dans une image Docker
3) Mettre à disposition son image sur DockerHub
4) Mettre à disposition son code dans un repository Github

### Commandes :

1) Création du Dockerfile depuis le terminal.

2) On accède au Dockerfile depuis le terminal.

3) On crée un environnement de travail et on défini la clé:
CMD : - pipenv shell 
      - export APIKEY=68e3a32a2b52669bdab1c00876332096

4) On teste l'API par la cmd :curl "http://api.openweathermap.org/data/2.5/weather?q=brescia&appid=$APIKEY"

Résultat :
((yaksouTk) ) bash-3.2$ curl "http://api.openweathermap.org/data/2.5/weather?q=brescia&appid=$APIKEY"
{"coord":{"lon":10.3,"lat":45.6333},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"base":"stations","main":{"temp":293.93,"feels_like":294.02,"temp_min":293.84,"temp_max":293.96,"pressure":1019,"humidity":75,"sea_level":1019,"grnd_level":900},"visibility":10000,"wind":{"speed":1.91,"deg":72,"gust":3.39},"clouds":{"all":32},"dt":1655235725,"sys":{"type":1,"id":6767,"country":"IT","sunrise":1655177342,"sunset":1655233750},"timezone":7200,"id":3181553,"name":"Provincia di Brescia","cod":200}((yaksouTk) ) bash-3.2$ 

5) Création du fichier python tp_devops.py



### Construction de l'image

On accède au DockerFile depuis le terminal pour créer l'image: CMD : docker build --tag tp_devops

MBP-de-Yakout:DockerFiles yaksouTk$ docker build --tag tp_devops . 
[+] Building 1.5s (13/13) FINISHED                                              
 => [internal] load build definition from Dockerfile                       0.0s
 => => transferring dockerfile: 467B                                       0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load metadata for docker.io/library/python:3.8              1.4s
 => [auth] library/python:pull token for registry-1.docker.io              0.0s
 => [internal] load build context                                          0.0s
 => => transferring context: 256B                                          0.0s
 => [1/7] FROM docker.io/library/python:3.8@sha256:1fbd81716d6d8d6081b11b  0.0s
 => CACHED [2/7] RUN apt update                                            0.0s
 => CACHED [3/7] RUN apt install python3                                   0.0s
 => CACHED [4/7] WORKDIR /Users/yaksouTk/Desktop/DockerFiles/Dockerfile    0.0s
 => CACHED [5/7] COPY tp_devops.py ./                                      0.0s
 => CACHED [6/7] COPY requirements.txt .                                   0.0s
 => CACHED [7/7] RUN pip install -r requirements.txt                       0.0s
 => exporting to image                                                     0.0s
 => => exporting layers                                                    0.0s
 => => writing image sha256:6618a332ba8e6a2d01a78285d21385dbb1b55213ae3e4  0.0s
 => => naming to docker.io/library/tp_devops                               0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
MBP-de-Yakout:DockerFiles yaksouTk$ 



## Envoi de l'image sur DockerHub

CMD :
docker images
docker login --username=yaksoutk
docker tag 6618a332ba8e yaksoutk/tp1_devops

docker run --env LAT="5.902785" --env LONG="102.754175" --env APIKEY=240aa650f4db4e154a07d0459c30a347 yaksoutk/tp1_devops



# DEVOPS - TP2

## Objectifs:


1) Configurer un workflow Github Action
2)Transformer un wrapper en API
3) Publier automatiquement a chaque push sur Docker Hub 
4) Mettre à disposition son image sur DockerHub 
5) Mettre à disposition son code dans un repository Github



### Commandes :

1) Création d’un nouveau Workflow depuis le repository du TP1

2) Connexion au docker (secret username/password depuis Github)

3) Modification du fichier python du TP1

4) On lance la commande : 
docker run --network host --env LAT="5.902785" --env LON="102.754175" --env API_KEY=240aa650f4db4e154a07d0459c30a347 
yaksoutk/tp2_devops_touhami_kadiri_yakout


Puis la commande : curl "http://localhost:8081/?lat=5.902785&lon=102.754175"
