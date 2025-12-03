# Exercices Pratiques - Docker et Kubernetes
## Cours pour Ingénieurs en Électronique

---

## 📋 Table des matières

1. [Exercice 1 : Docker Basics](#exercice-1--docker-basics)
2. [Exercice 2 : Docker Compose - WordPress + MySQL](#exercice-2--docker-compose---wordpress--mysql)
3. [Exercice 3 : Dockerfile et Build d'images](#exercice-3--dockerfile-et-build-dimages)
4. [Exercice 4 : Kubernetes - Déploiement simple](#exercice-4--kubernetes---déploiement-simple)
5. [Exercices bonus](#exercices-bonus)

---

## Exercice 1 : Docker Basics

### 🎯 Objectifs
- Rechercher et télécharger des images Docker
- Lancer et gérer des conteneurs
- Explorer les commandes essentielles

### 📝 Prérequis
- Docker installé et fonctionnel
- Compte Docker Hub créé
- Terminal ouvert

### 🔨 Étapes

#### 1. Rechercher une image WordPress

**Dans un navigateur web :**
1. Aller sur https://hub.docker.com/
2. Taper `wordpress` dans la barre de recherche
3. Sélectionner l'image officielle (badge "OFFICIAL IMAGE")
4. Explorer :
   - Les versions disponibles (tags)
   - La documentation d'utilisation
   - Le nombre de téléchargements

**En ligne de commande :**
```bash
docker search wordpress
```

#### 2. Télécharger l'image

```bash
# Télécharger la dernière version
docker pull wordpress

# Vérifier que l'image est téléchargée
docker images
```

**Résultat attendu :**
```
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
wordpress     latest    4c9b15c9a8ae   4 weeks ago    697MB
```

#### 3. Lancer le conteneur WordPress

```bash
docker container run --name my-wordpress -p 8080:80 -d wordpress
```

**Explication des options :**
- `--name my-wordpress` : Nom du conteneur
- `-p 8080:80` : Mapper le port 80 du conteneur sur le port 8080 de l'hôte
- `-d` : Mode détaché (background)
- `wordpress` : Image à utiliser

#### 4. Vérifier que le conteneur fonctionne

```bash
# Lister les conteneurs en cours d'exécution
docker container ps

# Voir les logs
docker container logs my-wordpress

# Suivre les logs en temps réel
docker container logs -f my-wordpress
```

#### 5. Accéder à WordPress

Ouvrir un navigateur et aller sur :
- http://localhost:8080

Vous devriez voir la page d'installation de WordPress.

#### 6. Explorer le conteneur

```bash
# Entrer dans le conteneur
docker container exec -it my-wordpress bash

# Une fois dans le conteneur, explorer
ls -la
pwd
cat /etc/os-release

# Sortir du conteneur
exit
```

#### 7. Voir les statistiques

```bash
# Statistiques en temps réel
docker stats my-wordpress

# Appuyer sur Ctrl+C pour arrêter
```

#### 8. Arrêter et supprimer le conteneur

```bash
# Arrêter le conteneur
docker container stop my-wordpress

# Vérifier qu'il est arrêté
docker container ps -a

# Supprimer le conteneur
docker container rm my-wordpress

# Vérifier qu'il est supprimé
docker container ps -a
```

### ✅ Validation

Vous avez réussi si :
- [ ] Vous avez pu télécharger l'image WordPress
- [ ] Le conteneur s'est lancé sans erreur
- [ ] Vous avez accédé à WordPress dans le navigateur
- [ ] Vous avez pu entrer dans le conteneur avec `exec`
- [ ] Vous avez pu arrêter et supprimer le conteneur

---

## Exercice 2 : Docker Compose - WordPress + MySQL

### 🎯 Objectifs
- Utiliser Docker Compose pour gérer plusieurs conteneurs
- Configurer une application multi-conteneurs
- Gérer les volumes et les réseaux

### 📝 Prérequis
- Docker Compose installé
- Exercice 1 complété

### 🔨 Étapes

#### 1. Créer le répertoire du projet

```bash
mkdir wordpress-app
cd wordpress-app
```

#### 2. Créer le fichier docker-compose.yaml

Créer un fichier `docker-compose.yaml` avec le contenu suivant :

```yaml
version: '3.8'

services:
  db:
    image: mysql:8.0
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: somewordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    
  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    ports:
      - "8080:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress

volumes:
  db_data:
```

#### 3. Démarrer la topologie

```bash
# Démarrer en mode détaché
docker compose up -d

# Voir les logs
docker compose logs -f
```

#### 4. Vérifier les services

```bash
# Lister les conteneurs
docker compose ps

# Résultat attendu :
# NAME                        IMAGE              STATUS         PORTS
# wordpress-app-db-1          mysql:8.0          Up 2 minutes   3306/tcp
# wordpress-app-wordpress-1   wordpress:latest   Up 2 minutes   0.0.0.0:8080->80/tcp
```

#### 5. Accéder au site

Ouvrir http://localhost:8080 et suivre l'assistant d'installation WordPress.

#### 6. Explorer les logs

```bash
# Logs de tous les services
docker compose logs

# Logs d'un service spécifique
docker compose logs wordpress
docker compose logs db

# Suivre les logs en temps réel
docker compose logs -f wordpress
```

#### 7. Trouver le fichier wp-admin.php

```bash
# Entrer dans le conteneur WordPress
docker compose exec -ti wordpress bash

# Chercher le fichier
find / -name "wp-admin.php" 2>/dev/null

# Résultat : /var/www/html/wp-admin.php

# Sortir
exit
```

#### 8. Extraire le fichier

```bash
# Copier du conteneur vers l'hôte
docker compose cp wordpress:/var/www/html/wp-admin.php ./wp-admin.php

# Vérifier
ls -l wp-admin.php
```

#### 9. Voir les statistiques

```bash
docker stats
```

#### 10. Changer le port d'accès

Modifier le fichier `docker-compose.yaml` :

```yaml
wordpress:
  ports:
    - "9080:80"  # Changé de 8080 à 9080
```

Redémarrer :

```bash
docker compose down
docker compose up -d
```

Accéder à http://localhost:9080

#### 11. Nettoyer

```bash
# Arrêter et supprimer les conteneurs
docker compose down

# Arrêter et supprimer conteneurs + volumes
docker compose down -v
```

### ✅ Validation

Vous avez réussi si :
- [ ] Les deux conteneurs (WordPress et MySQL) démarrent correctement
- [ ] WordPress est accessible et fonctionnel
- [ ] Vous avez pu extraire le fichier wp-admin.php
- [ ] Vous avez changé le port avec succès
- [ ] Les données persistent entre les redémarrages (avant `down -v`)

---

## Exercice 3 : Dockerfile et Build d'images

### 🎯 Objectifs
- Créer un Dockerfile
- Construire une image personnalisée
- Publier l'image sur Docker Hub

### 📝 Prérequis
- Compte Docker Hub
- Connexion à Docker Hub (`docker login`)

### 🔨 Étapes

#### 1. Créer le répertoire du projet

```bash
mkdir nginx-custom
cd nginx-custom
```

#### 2. Créer un fichier HTML personnalisé

Créer un fichier `index.html` :

```html
<!doctype html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon Site Docker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        h1 {
            text-align: center;
            font-size: 3em;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        .info {
            margin: 20px 0;
            padding: 15px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐳 Hello from Docker!</h1>
        <div class="info">
            <h2>Informations</h2>
            <p><strong>Projet :</strong> Formation Docker & Kubernetes</p>
            <p><strong>École :</strong> Polytech</p>
            <p><strong>Spécialité :</strong> Électronique</p>
        </div>
        <div class="info">
            <h2>Technologies utilisées</h2>
            <ul>
                <li>Docker</li>
                <li>NGINX</li>
                <li>HTML/CSS</li>
            </ul>
        </div>
    </div>
</body>
</html>
```

#### 3. Tester avec un volume (optionnel)

```bash
# Lancer NGINX avec le volume
docker run -it --rm -d -p 8080:80 --name web \
  -v ./:/usr/share/nginx/html \
  nginx

# Tester dans le navigateur
# http://localhost:8080

# Arrêter
docker stop web
```

#### 4. Créer le Dockerfile

Créer un fichier nommé `Dockerfile` (sans extension) :

```dockerfile
FROM nginx:latest
COPY ./index.html /usr/share/nginx/html/index.html
```

#### 5. Construire l'image

```bash
# Construire l'image
docker build -t webserver .

# Vérifier l'image
docker images webserver
```

**Sortie attendue :**
```
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
webserver    latest    abc123def456   10 seconds ago   187MB
```

#### 6. Tester l'image

```bash
# Lancer le conteneur
docker run -it --rm -d -p 8080:80 --name web webserver

# Tester dans le navigateur
# http://localhost:8080

# Arrêter
docker stop web
```

#### 7. Publier sur Docker Hub

```bash
# Se connecter à Docker Hub
docker login

# Tagger l'image (remplacer <votre-username> par votre nom d'utilisateur)
docker tag webserver <votre-username>/mywebserver:v1.0

# Pousser l'image
docker push <votre-username>/mywebserver:v1.0
```

#### 8. Vérifier sur Docker Hub

Aller sur https://hub.docker.com/r/<votre-username>/mywebserver

#### 9. Tester l'image depuis Docker Hub

```bash
# Supprimer les images locales
docker rmi webserver
docker rmi <votre-username>/mywebserver:v1.0

# Télécharger et lancer depuis Docker Hub
docker run -d -p 8080:80 <votre-username>/mywebserver:v1.0

# Tester
# http://localhost:8080
```

#### 10. Bonus : Tester l'image d'un collègue

```bash
# Demander le nom d'utilisateur d'un collègue
docker pull <username-collegue>/mywebserver:v1.0

# Lancer
docker run -d -p 8081:80 <username-collegue>/mywebserver:v1.0

# Tester
# http://localhost:8081
```

### ✅ Validation

Vous avez réussi si :
- [ ] Votre Dockerfile construit sans erreur
- [ ] L'image fonctionne localement
- [ ] L'image est publiée sur Docker Hub
- [ ] Vous pouvez télécharger et exécuter votre image depuis Docker Hub
- [ ] Vous avez testé l'image d'un collègue

---

## Exercice 4 : Kubernetes - Déploiement simple

### 🎯 Objectifs
- Déployer une application sur Kubernetes
- Utiliser kubectl
- Scaler une application

### 📝 Prérequis
- Accès à un cluster Kubernetes (Minikube, Kind, ou Play with K8s)
- kubectl installé

### 🔨 Étapes

#### 1. Vérifier l'accès au cluster

```bash
# Vérifier kubectl
kubectl version --client

# Vérifier les nœuds
kubectl get nodes
```

#### 2. Créer un déploiement NGINX

Créer un fichier `nginx-deployment.yaml` :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
        ports:
        - containerPort: 80
        resources:
          limits:
            memory: "128Mi"
            cpu: "500m"
```

#### 3. Déployer l'application

```bash
# Appliquer le déploiement
kubectl apply -f nginx-deployment.yaml

# Vérifier les pods
kubectl get pods

# Voir les détails du déploiement
kubectl describe deployment nginx-deployment
```

#### 4. Créer un service

Créer un fichier `nginx-service.yaml` :

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
      nodePort: 30080
```

```bash
# Appliquer le service
kubectl apply -f nginx-service.yaml

# Vérifier le service
kubectl get services
```

#### 5. Accéder à l'application

```bash
# Obtenir l'URL (Minikube)
minikube service nginx-service --url

# Ou accéder directement
# http://<node-ip>:30080
```

#### 6. Scaler l'application

```bash
# Augmenter à 5 réplicas
kubectl scale deployment nginx-deployment --replicas=5

# Vérifier
kubectl get pods

# Réduire à 2 réplicas
kubectl scale deployment nginx-deployment --replicas=2

# Vérifier
kubectl get pods
```

#### 7. Voir les logs

```bash
# Lister les pods
kubectl get pods

# Voir les logs d'un pod (remplacer <pod-name>)
kubectl logs <pod-name>

# Suivre les logs
kubectl logs -f <pod-name>
```

#### 8. Mettre à jour l'application

```bash
# Mettre à jour l'image
kubectl set image deployment/nginx-deployment nginx=nginx:1.26

# Suivre le déploiement
kubectl rollout status deployment/nginx-deployment

# Voir l'historique
kubectl rollout history deployment/nginx-deployment
```

#### 9. Rollback

```bash
# Revenir à la version précédente
kubectl rollout undo deployment/nginx-deployment

# Vérifier
kubectl rollout status deployment/nginx-deployment
```

#### 10. Nettoyer

```bash
# Supprimer le service
kubectl delete service nginx-service

# Supprimer le déploiement
kubectl delete deployment nginx-deployment

# Vérifier
kubectl get all
```

### ✅ Validation

Vous avez réussi si :
- [ ] Le déploiement est créé avec 3 réplicas
- [ ] Le service expose l'application
- [ ] Vous pouvez accéder à NGINX
- [ ] Le scaling fonctionne
- [ ] La mise à jour et le rollback fonctionnent

---

## Exercices Bonus

### Bonus 1 : Application Python avec Docker

Créer une application Flask simple et la conteneuriser.

**app.py :**
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from Python Flask in Docker!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**requirements.txt :**
```
Flask==3.0.0
```

**Dockerfile :**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
```

### Bonus 2 : Docker Compose avec Redis

Ajouter un service Redis à votre application.

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - redis
  redis:
    image: redis:alpine
```

### Bonus 3 : Multi-stage Build

Optimiser une image Node.js avec multi-stage build.

```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY package*.json ./
RUN npm install --production
CMD ["node", "dist/server.js"]
```

### Bonus 4 : Kubernetes avec ConfigMap

Utiliser un ConfigMap pour la configuration.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  database_url: "mysql://db:3306"
  log_level: "info"
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 2
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:latest
        envFrom:
        - configMapRef:
            name: app-config
```

### Bonus 5 : Horizontal Pod Autoscaler

Configurer l'autoscaling basé sur le CPU.

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

---

## 🎓 Conseils pour réussir

1. **Lisez les messages d'erreur** : Ils contiennent souvent la solution
2. **Utilisez `--help`** : Chaque commande a une aide intégrée
3. **Consultez les logs** : `docker logs` et `kubectl logs` sont vos amis
4. **Testez étape par étape** : Ne passez pas à l'étape suivante si la précédente ne fonctionne pas
5. **Documentez vos commandes** : Créez un fichier avec les commandes qui fonctionnent
6. **Expérimentez** : N'ayez pas peur de casser, c'est comme ça qu'on apprend !

---

## 📚 Ressources supplémentaires

- [Documentation Docker](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Documentation Kubernetes](https://kubernetes.io/fr/docs/home/)
- [Play with Docker](https://labs.play-with-docker.com/)
- [Play with Kubernetes](https://labs.play-with-k8s.com/)
- [Katacoda (tutoriels interactifs)](https://www.katacoda.com/)

Bon courage ! 🚀