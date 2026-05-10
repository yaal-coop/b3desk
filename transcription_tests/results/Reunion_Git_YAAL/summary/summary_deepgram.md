# Compte rendu de réunion

**Date** : 28 avril 2026
**Durée estimée** : *non précisée* (environ 1 h d’échanges)

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Michael** | Responsable du suivi du backlog et de la documentation |
| **Lohan** | Expert produit / processus (présence incertaine) |
| **Owen** | (Présent, rôle non détaillé) |
| **Benoît** | Auteur du tableau de suivi des tâches, responsable des releases |
| **Benjamin** | Responsable des migrations de base de données |
| **Sébastien** | Contributeur aux migrations (mentionné) |
| **Autres** | Participants non nommés explicitement (ex. « les collègues du bureau ») |

## Objet de la réunion
- Faire le point sur l’état du **backlog** et du tableau de suivi des tâches.
- Clarifier le **processus de release** (branches, tags, création de versions).
- Définir les **informations à inclure** dans les notes de release (tickets, migrations, changements de configuration).
- Identifier les actions à réaliser avant la prochaine mise en production.

## Sujets abordés
1. **État du tableau de suivi**
   - Colonne *Ready* remplie de façon incohérente.
   - Besoin de distinguer clairement les colonnes *Ready*, *In Progress* et créer une colonne *À trier*.

2. **Nettoyage du backlog**
   - Décision de vider la colonne *Ready* et de re‑classer les tickets dans les colonnes appropriées.

3. **Processus de release**
   - Branches : `main` (développement), `production` (release stable).
   - Création d’un **tag** (ex. `v1.3`) puis publication sur GitHub.
   - Vérification des conflits de version (ex. passage de `2.20` à `3.0`).

4. **Contenu des notes de release**
   - Lister les tickets résolus, les changements de configuration et les migrations.
   - Ajouter l’identifiant de chaque migration (hash généré par la librairie de migration).
   - Utiliser le titre du ticket comme description succincte.

5. **Migrations de base de données**
   - Explication du fonctionnement des hashes d’identifiant.
   - Nécessité d’indiquer l’ordre d’exécution et les IDs dans les notes de release.

6. **Gestion des erreurs**
   - Erreurs de connexion à BBB et au serveur d’identité : déjà résolues, à mentionner dans la release.

7. **Responsabilités**
   - Michael : nettoyage du tableau, mise à jour de la documentation, création du tag et publication de la release.
   - Benjamin : fournir les IDs de migration et vérifier leur présence dans les notes.
   - Benoît : valider le schéma du tableau et les colonnes, intervenir si besoin.

## Décisions prises
| Décision | Responsable | Délai |
|----------|-------------|-------|
| Vider la colonne **Ready** et re‑classer les tickets | Michael | Immédiat |
| Créer une colonne **À trier** pour les tickets anciens | Michael | Immédiat |
| Ajouter les IDs de migration dans les notes de release | Benjamin | Avant la prochaine release |
| Utiliser le titre du ticket comme description dans les notes | Michael | Immédiat |
| Publier la release avec le tag `v1.3` (ou version suivante) | Michael | Dès que le tableau est nettoyé |
| Mettre à jour le document de procédure de release (incl. exemples de commits) | Michael | Avant la prochaine réunion |

## Questions en suspens
- **Configuration** : faut‑il détailler chaque changement de configuration dans les notes ou se contenter du lien ticket ? (Consensus : lien ticket suffit, mais ajouter le titre).
- **Gestion des conflits** : procédure exacte à suivre lorsqu’un conflit apparaît lors du merge `main → production`.
- **Responsabilité du suivi des migrations** : formaliser qui doit vérifier que chaque migration a bien été appliquée en production.

## Tâches à effectuer
| Tâche | Responsable | Commentaire |
|-------|-------------|-------------|
| Nettoyer la colonne *Ready* et reclasser les tickets | Michael | Déplacer les tickets dans *In Progress* ou *À trier*. |
| Créer la colonne *À trier* dans le tableau | Michael | Utiliser pour les tickets anciens non triés. |
| Ajouter les IDs de migration aux notes de release | Benjamin | Récupérer les hashes depuis les scripts de migration. |
| Rédiger les notes de release (tickets, configs, migrations) | Michael | Inclure le titre du ticket et le lien. |
| Créer le tag de version (ex. `v1.3`) et pousser sur GitHub | Michael | Vérifier l’absence de conflits. |
| Publier la release sur la page GitHub | Michael | Sélectionner le tag et remplir le formulaire. |
| Mettre à jour la documentation de procédure de release | Michael | Ajouter les étapes détaillées et les captures d’écran. |
| Vérifier que les erreurs de connexion (BBB, serveur d’identité) sont bien documentées | Michael | S’assurer qu’elles figurent dans la release. |
| Planifier la prochaine réunion (dans 2 semaines) | Tous | Confirmation de la date/heure à définir. |

## Prochaine rencontre
- **Date prévue** : dans **deux semaines** (à confirmer).
- **Objectif** : Faire le point sur le nettoyage du backlog, valider la nouvelle version publiée et vérifier que les procédures de release sont bien appliquées.

---

*Fin du compte rendu.*
