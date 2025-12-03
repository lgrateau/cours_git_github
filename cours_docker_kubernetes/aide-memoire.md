# Aide-Mémoire Docker et Kubernetes
## Commandes essentielles

---

## 🐳 Docker - Commandes de base

### Images

```bash
# Rechercher une image
docker search <nom>

# Télécharger une image
docker pull <image>:<tag>

# Lister les images locales
docker images
docker images -a  # Inclure les images intermédiaires

# Supprimer une image
docker rmi <image>
docker rmi -f <image>  # Forcer la suppression

# Construire une image
docker build -t <nom>:<tag> .
docker build -t <nom>:<tag> -f <Dockerfile> .

# Sauvegarder/Restaurer une image
docker save -o <fichier.tar> <image>
docker load -i <fichier.tar>

# Inspecter une image
docker inspect <image>

# Voir l'historique d'une image
docker history <image>
```

### Conteneurs

```bash
# Lancer un conteneur
docker run <image>
docker run -d <image>                    # Mode détaché
docker run -it <image>                   # Mode interactif
docker run --name <nom> <image>          # Nommer le conteneur
docker run -p <host>:<container> <image> # Mapper les ports
docker run -v <host>:<container> <image> # Monter un volume
docker run -e <VAR>=<value> <image>      # Variable d'environnement
docker run --rm <image>                  # Supprimer après arrêt

# Lister les conteneurs
docker ps                # Conteneurs en cours
docker ps -a             # Tous les conteneurs
docker ps -q             # IDs seulement

# Arrêter/Démarrer/Redémarrer
docker stop <container>
docker start <container>
docker restart <container>
docker kill <container>  # Arrêt forcé

# Supprimer un conteneur
docker rm <container>
docker rm -f <container>  # Forcer la suppression

# Exécuter une commande dans un conteneur
docker exec <container> <commande>
docker exec -it <container> bash
docker exec -it <container> sh

# Voir les logs
docker logs <container>
docker logs -f <container>           # Suivre les logs
docker logs --tail 50 <container>    # 50 dernières lignes
docker logs --since 10m <container>  # Depuis 10 minutes

# Copier des fichiers
docker cp <container>:<chemin> <destination>
docker cp <source> <container>:<chemin>

# Inspecter un conteneur
docker inspect <container>

# Voir les statistiques
docker stats
docker stats <container>

# Voir les processus
docker top <container>

# Mettre en pause/reprendre
docker pause <container>
docker unpause <container>
```

### Nettoyage

```bash
# Supprimer les conteneurs arrêtés
docker container prune

# Supprimer les images non utilisées
docker image prune
docker image prune -a  # Toutes les images non utilisées

# Supprimer les volumes non utilisés
docker volume prune

# Supprimer les réseaux non utilisés
docker network prune

# Nettoyage complet
docker system prune
docker system prune -a --volumes  # Tout supprimer

# Voir l'espace disque utilisé
docker system df
```

### Volumes

```bash
# Créer un volume
docker volume create <nom>

# Lister les volumes
docker volume ls

# Inspecter un volume
docker volume inspect <nom>

# Supprimer un volume
docker volume rm <nom>

# Utiliser un volume
docker run -v <volume>:<chemin> <image>
docker run -v <chemin-host>:<chemin-container> <image>
```

### Réseaux

```bash
# Lister les réseaux
docker network ls

# Créer un réseau
docker network create <nom>

# Inspecter un réseau
docker network inspect <nom>

# Connecter un conteneur à un réseau
docker network connect <réseau> <container>

# Déconnecter
docker network disconnect <réseau> <container>

# Supprimer un réseau
docker network rm <nom>
```

---

## 📝 Dockerfile - Instructions

```dockerfile
# Image de base
FROM <image>:<tag>

# Métadonnées
LABEL maintainer="email@example.com"
LABEL version="1.0"

# Répertoire de travail
WORKDIR /app

# Copier des fichiers
COPY <source> <destination>
ADD <source> <destination>  # Peut extraire des archives

# Exécuter des commandes (build time)
RUN <commande>
RUN apt-get update && apt-get install -y package

# Variables d'environnement
ENV <KEY>=<value>
ENV NODE_ENV=production

# Arguments de build
ARG <name>=<default>

# Exposer un port (documentation)
EXPOSE <port>

# Volumes
VOLUME ["/data"]

# Utilisateur
USER <user>

# Commande par défaut (runtime)
CMD ["executable", "param1", "param2"]

# Point d'entrée
ENTRYPOINT ["executable"]

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost/ || exit 1
```

### Exemple complet

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY . .
EXPOSE 3000
USER node
CMD ["node", "server.js"]
```

---

## 🎼 Docker Compose

### Commandes

```bash
# Démarrer les services
docker compose up
docker compose up -d              # Mode détaché
docker compose up --build         # Reconstruire les images

# Arrêter les services
docker compose stop
docker compose down               # Arrêter et supprimer
docker compose down -v            # Supprimer aussi les volumes

# Voir les services
docker compose ps
docker compose ps -a

# Voir les logs
docker compose logs
docker compose logs -f            # Suivre les logs
docker compose logs <service>     # Logs d'un service

# Exécuter une commande
docker compose exec <service> <commande>
docker compose exec -ti <service> bash

# Construire les images
docker compose build
docker compose build --no-cache

# Redémarrer les services
docker compose restart
docker compose restart <service>

# Scaler un service
docker compose up -d --scale <service>=<nombre>

# Voir la configuration
docker compose config

# Copier des fichiers
docker compose cp <service>:<source> <destination>
```

### Fichier docker-compose.yaml

```yaml
version: '3.8'

services:
  web:
    build: .
    # ou
    image: nginx:latest
    container_name: mon-web
    ports:
      - "8080:80"
    volumes:
      - ./app:/usr/share/nginx/html
      - data:/data
    environment:
      - NODE_ENV=production
      - API_KEY=${API_KEY}
    env_file:
      - .env
    depends_on:
      - db
    networks:
      - frontend
    restart: always
    
  db:
    image: mysql:8.0
    volumes:
      - db_data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: mydb
    networks:
      - backend

volumes:
  data:
  db_data:

networks:
  frontend:
  backend:
```

---

## ☸️ Kubernetes - kubectl

### Contexte et configuration

```bash
# Voir la configuration
kubectl config view

# Voir les contextes
kubectl config get-contexts

# Changer de contexte
kubectl config use-context <context>

# Voir le contexte actuel
kubectl config current-context
```

### Ressources de base

```bash
# Obtenir des ressources
kubectl get <resource>
kubectl get pods
kubectl get deployments
kubectl get services
kubectl get nodes
kubectl get all

# Options utiles
kubectl get pods -o wide           # Plus d'informations
kubectl get pods -o yaml           # Format YAML
kubectl get pods -o json           # Format JSON
kubectl get pods --watch           # Suivre les changements
kubectl get pods -n <namespace>    # Dans un namespace
kubectl get pods --all-namespaces  # Tous les namespaces

# Décrire une ressource
kubectl describe <resource> <nom>
kubectl describe pod <pod-name>
kubectl describe deployment <deployment-name>

# Créer des ressources
kubectl create -f <fichier.yaml>
kubectl apply -f <fichier.yaml>    # Créer ou mettre à jour
kubectl apply -f <dossier>/        # Tous les fichiers du dossier

# Supprimer des ressources
kubectl delete <resource> <nom>
kubectl delete -f <fichier.yaml>
kubectl delete pod <pod-name>
kubectl delete deployment <deployment-name>
```

### Pods

```bash
# Lister les pods
kubectl get pods

# Voir les logs
kubectl logs <pod-name>
kubectl logs -f <pod-name>                    # Suivre les logs
kubectl logs <pod-name> -c <container-name>   # Conteneur spécifique
kubectl logs --previous <pod-name>            # Logs du conteneur précédent

# Exécuter une commande
kubectl exec <pod-name> -- <commande>
kubectl exec -it <pod-name> -- bash
kubectl exec -it <pod-name> -- sh

# Copier des fichiers
kubectl cp <pod-name>:<chemin> <destination>
kubectl cp <source> <pod-name>:<chemin>

# Port forwarding
kubectl port-forward <pod-name> <local-port>:<pod-port>
kubectl port-forward pod/nginx 8080:80
```

### Deployments

```bash
# Créer un deployment
kubectl create deployment <nom> --image=<image>
kubectl create deployment nginx --image=nginx:latest

# Scaler un deployment
kubectl scale deployment <nom> --replicas=<nombre>
kubectl scale deployment nginx --replicas=5

# Mettre à jour l'image
kubectl set image deployment/<nom> <container>=<nouvelle-image>
kubectl set image deployment/nginx nginx=nginx:1.26

# Voir le statut du rollout
kubectl rollout status deployment/<nom>

# Voir l'historique
kubectl rollout history deployment/<nom>

# Rollback
kubectl rollout undo deployment/<nom>
kubectl rollout undo deployment/<nom> --to-revision=<numéro>

# Pause/Resume
kubectl rollout pause deployment/<nom>
kubectl rollout resume deployment/<nom>

# Autoscaling
kubectl autoscale deployment <nom> --min=<min> --max=<max> --cpu-percent=<pourcent>
```

### Services

```bash
# Créer un service
kubectl expose deployment <nom> --port=<port> --type=<type>
kubectl expose deployment nginx --port=80 --type=NodePort

# Types de services
# - ClusterIP (défaut)
# - NodePort
# - LoadBalancer
# - ExternalName

# Obtenir l'URL d'un service (Minikube)
minikube service <service-name> --url
```

### Namespaces

```bash
# Lister les namespaces
kubectl get namespaces

# Créer un namespace
kubectl create namespace <nom>

# Utiliser un namespace
kubectl config set-context --current --namespace=<nom>

# Supprimer un namespace
kubectl delete namespace <nom>
```

### ConfigMaps et Secrets

```bash
# Créer un ConfigMap
kubectl create configmap <nom> --from-file=<fichier>
kubectl create configmap <nom> --from-literal=<key>=<value>

# Créer un Secret
kubectl create secret generic <nom> --from-file=<fichier>
kubectl create secret generic <nom> --from-literal=<key>=<value>

# Voir les ConfigMaps/Secrets
kubectl get configmaps
kubectl get secrets

# Décrire
kubectl describe configmap <nom>
kubectl describe secret <nom>
```

### Débogage

```bash
# Événements du cluster
kubectl get events
kubectl get events --sort-by=.metadata.creationTimestamp

# Ressources du cluster
kubectl top nodes
kubectl top pods

# Informations du cluster
kubectl cluster-info

# Version
kubectl version
```

---

## 📊 Fichiers YAML Kubernetes

### Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  labels:
    app: myapp
spec:
  replicas: 3
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
        image: myapp:1.0
        ports:
        - containerPort: 8080
        env:
        - name: ENV_VAR
          value: "value"
        resources:
          limits:
            memory: "256Mi"
            cpu: "500m"
          requests:
            memory: "128Mi"
            cpu: "250m"
```

### Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  type: LoadBalancer
  selector:
    app: myapp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
```

### ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  database_url: "mysql://db:3306"
  log_level: "info"
```

### Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
data:
  password: cGFzc3dvcmQxMjM=  # base64 encodé
```

---

## 🔧 Astuces et bonnes pratiques

### Docker

- Utilisez des images de base légères (alpine)
- Spécifiez toujours des versions précises
- Utilisez .dockerignore
- Minimisez le nombre de layers
- Ne stockez jamais de secrets dans les images
- Utilisez multi-stage builds pour optimiser
- Scannez vos images pour les vulnérabilités

### Kubernetes

- Utilisez des namespaces pour organiser
- Définissez toujours des limites de ressources
- Utilisez des labels pour organiser les ressources
- Utilisez des ConfigMaps et Secrets pour la configuration
- Définissez des health checks (liveness et readiness probes)
- Utilisez des PodDisruptionBudgets pour la haute disponibilité
- Versionnez vos fichiers YAML dans Git

---

## 📚 Ressources

- [Documentation Docker](https://docs.docker.com/)
- [Documentation Kubernetes](https://kubernetes.io/fr/docs/home/)
- [Docker Hub](https://hub.docker.com/)
- [Kubernetes Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)