# Compte rendu de réunion

**Date** : 29 avril 2026
**Durée estimée** : ~1 heure

## Participants
- **Michael** (animateur)
- **Lohan** (expert produit) – absent (arrivée prévue)
- **Owen** (présent)
- **Benoît** (responsable du tableau de suivi)
- **Benjamin** (développeur, gestion des migrations)
- **Sébastien** (mentionné pour les migrations)
- Autres membres de l’équipe (non nommés)

## Objet de la réunion
Revoir et valider le processus de **déploiement / release** (gestion des branches, du tableau de suivi, des migrations et de la documentation) afin d’assurer une mise en production fiable et bien documentée.

## Sujets abordés

| Thème | Points clés |
|-------|-------------|
| **Tableau de suivi (backlog)** | - Colonne *Ready* remplie de tickets obsolètes.<br>- Besoin de nettoyer la colonne et de re‑classer les tickets dans *In Progress* ou *À trier*.<br>- Benoît était le créateur du tableau ; on évitera de le modifier sans son accord. |
| **Processus de passage des tickets** | - Décision de déplacer les tickets de *Ready* → *In Progress*.<br>- Si impossible, créer une colonne *À trier* pour libérer l’espace. |
| **Gestion des branches** | - `main` = branche de développement continu.<br>- `production` = branche de release stable (mise à jour à chaque merge).<br>- Chaque release part de `main`, crée une branche de release, puis merge dans `production`. |
| **Tagging & création de release** | - Création du tag `v1.3` sur `production`.<br>- Pousser le tag et créer la release sur GitHub.<br>- Utiliser le tag pour générer les notes de version. |
| **Notes de version / documentation** | - Inclure dans les notes : <br>  • Titres des tickets (ex. *Gérer les erreurs de connexion à BBB*).<br>  • Liens vers les tickets JIRA.<br>  • Modifications de configuration (s’il y en a).<br>  • Identifiant de migration (hash) lorsqu’il y a migration DB. |
| **Migrations de base de données** | - Les identifiants (hash) sont générés par la librairie de migration.<br>- Chaque migration possède son propre fichier et doit être exécutée dans l’ordre.<br>- Besoin d’ajouter ces identifiants dans les notes de release pour faciliter le suivi. |
| **Gestion des erreurs** | - Vérification que les erreurs de connexion (BBB, serveur d’identité) sont bien documentées et testées. |
| **Responsabilités & communication** | - Michael assure le nettoyage du tableau et la création du tag.<br>- Benjamin ajoute les identifiants de migration aux notes de version.<br>- L’équipe de dev (Benoît, etc.) continue de gérer les modifications de code et les petites corrections orthographiques directement dans le dépôt. |
| **Prochaine itération** | - Envoi d’un point de suivi dans deux semaines.<br>- Préparer la prochaine release (`v1.4‑dev`). |

## Décisions prises

1. **Nettoyage du tableau** : la colonne *Ready* sera vidée et les tickets seront re‑classés.
2. **Mise à jour du processus** : les tickets passent désormais de *Ready* → *In Progress* (ou *À trier*).
3. **Structure des branches** : `main` → branche de release → merge dans `production`.
4. **Tagging** : le tag `v1.3` sera créé et poussé ; la release correspondante sera publiée sur GitHub.
5. **Notes de version** : elles contiendront les titres des tickets, les liens, les changements de config et les IDs de migration.
6. **Documentation** : Michael mettra à jour le document de procédure avec les étapes validées.

## Questions en suspens

| Question | Responsable / Action |
|----------|----------------------|
| Y a‑t‑il des changements de configuration spécifiques à cette release ? | Michael vérifiera dans les tickets et confirmera. |
| Comment automatiser l’ajout des IDs de migration dans les notes de version ? | Benjamin proposera une solution (script ou template). |
| Qui assure le suivi des éventuels conflits lors du merge `main` → `production` ? | Michael (détecte, signale, résout avec l’équipe). |

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Nettoyer la colonne *Ready* et re‑classer les tickets | Michael | Avant la fin de la journée |
| Créer le tag `v1.3` et pousser sur le dépôt | Michael | Immédiat |
| Publier la release GitHub associée au tag | Michael | Immédiat après le push |
| Ajouter les IDs de migration aux notes de version | Benjamin | Avant la publication de la release |
| Mettre à jour la documentation du processus de release | Michael | Dans les 2 jours suivant |
| Vérifier l’absence de nouvelles configurations à déployer | Michael | Avant la création du tag |
| Envoyer le point de suivi et planifier la prochaine réunion | Michael | Dans 2 semaines |

## Prochaine rencontre

- **Date prévue** : dans deux semaines (date exacte à confirmer).
- **Objectif** : faire le point sur la release `v1.4‑dev`, valider les améliorations du processus et vérifier le suivi des tickets migrés.

---

*Fin du compte rendu.*
