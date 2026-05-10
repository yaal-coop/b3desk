# Compte rendu de réunion

**Date** : 28 avril 2026
**Heure** : non précisée (durée estimée ≈ 1 h)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Lohan** | (prévu, présence incertaine) |
| **Loan** | Maîtrise du produit et du process |
| **Benoît** | Responsable du Kanban/backlog |
| **Mickaël** | Responsable du déploiement & tests |
| **Michael** | (intervenant sur les migrations) |
| **Benjamin** | (connaissance des scripts de migration) |
| **Sébastien** | (intervention sur la base de données) |
| **Autres** | Participants non nommés (ex. : “toi”, “vous”) |

---

## Objet de la réunion
Revue et amélioration du **processus de déploiement** : documentation, gestion du Kanban, workflow Git (branches *main* et *production*), création de releases et suivi des migrations.

---

## Sujets abordés

| N° | Sujet | Points clés |
|----|-------|-------------|
| 1 | **Présence de Lohan** | Décision de commencer sans lui, mais possibilité d’attendre s’il est indispensable. |
| 2 | **Documentation OpenDocs** | Mise à jour simultanée pendant la réunion ; ajout de nouvelles commandes et étapes. |
| 3 | **Kanban B3desk** | - Colonnes actuelles : *Backlog*, *Ready*, *In Progress*, *Done*. <br> - Confusion sur la fonction de *Ready* (doublon avec *Done*). <br> - Proposition de nettoyer la colonne *Done* et, si besoin, créer une colonne « À trier ». |
| 4 | **Workflow Git** | - *main* = branche de développement. <br> - *production* = branche de release. <br> - Processus : merge de *main* → *production*, gestion des conflits (ex. : `init`, `pyproject`). |
| 5 | **Création de tags & releases** | - Tagger chaque version (ex. : `v1.3`). <br> - Publier la release sur GitHub. <br> - Contenu des notes : tickets concernés (lien + titre), modifications de base, modifications de configuration, identifiants de migration. |
| 6 | **Migrations de base de données** | - Chaque migration possède un ID généré par une librairie. <br> - Les IDs doivent être mentionnés dans les notes de release. <br> - Deux migrations distinctes pour la même version (ex. : classement des salons, code unique). |
| 7 | **Responsabilités & communication** | - Mickaël : tests de livraison, validation, retour. <br> - Benoît : gestion du Kanban et des revues. <br> - Benjamin : explication du système d’IDs de migration. <br> - Sébastien : mise à jour des champs `updated_at`, `created_at`, `hisfavorite` dans la table `meeting`. |
| 8 | **Améliorations futures** | - Créer un ticket dédié à chaque version dans le Kanban (colonne `1.3.0`). <br> - Formaliser le format des notes de release. <br> - Documenter le processus de merge et de résolution de conflits. |

---

## Décisions prises
| Décision | Responsable(s) | Commentaire |
|----------|----------------|-------------|
| Démarrer la réunion sans Lohan (attente possible) | – | Lohan pourra rejoindre plus tard si besoin. |
| Conserver les colonnes actuelles du Kanban mais clarifier la fonction de **Ready** | Benoît (avec l’équipe) | Discussion à planifier pour éventuellement supprimer ou renommer la colonne. |
| Utiliser *main* pour le développement et *production* pour les releases | Toute l’équipe | Merge de *main* → *production* systématique avant chaque release. |
| Taguer chaque release et publier sur GitHub | Mickaël (avec l’aide de l’équipe dev) | Tags créés automatiquement lors du push (`--follow-tags`). |
| Les notes de release doivent contenir : <br>• lien + titre du ticket <br>• modifications de base <br>• modifications de config <br>• ID de migration | Mickaël (rédaction) <br>Benjamin (ID) | Format validé lors de la réunion. |
| Créer un ticket Kanban dédié à chaque version (ex. : `1.3.0`) | Benoît | Permet de centraliser les infos de release. |
| Sébastien met à jour les champs `updated_at`, `created_at`, `hisfavorite` dans la table `meeting` | Sébastien | Valeur d’initialisation = date de migration, `hisfavorite` = `false`. |

---

## Questions en suspens
| Question | Responsable(s) | État |
|----------|----------------|------|
| Quelle est la finalité exacte de la colonne **Ready** ? | Benoît | À clarifier dans le prochain point Kanban. |
| Comment gérer les conflits récurrents lors du merge *main* → *production* (ex. `init`, `pyproject`) ? | Équipe dev | Procédure à formaliser. |
| Niveau de détail souhaité dans les notes de release ? (titre seulement vs description) | Mickaël / Benoît | Décision partielle : lien + titre suffisent, mais possibilité d’ajouter une courte description. |
| Faut‑il créer un ticket Kanban **pour chaque release** ou seulement pour les majeures ? | Benoît | Décidé de créer un ticket pour chaque version, à confirmer. |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|--------------|----------|
| Nettoyer la colonne **Done** du Kanban et créer la colonne **À trier** si besoin | Benoît | Prochaine réunion |
| Rédiger le modèle de notes de release (incluant tickets, configs, migrations) | Mickaël | Avant la prochaine release |
| Ajouter les IDs de migration aux notes de release | Benjamin | Immédiat |
| Mettre à jour les champs `updated_at`, `created_at`, `hisfavorite` dans la table `meeting` | Sébastien | Dès que possible |
| Enregistrer une vidéo tutorielle du processus de merge & release | Mickaël | Avant la prochaine release |
| Créer un ticket Kanban `1.3.0` (ou version courante) regroupant toutes les infos de release | Benoît | Avant la prochaine release |
| Documenter la procédure de résolution de conflits de merge | Équipe dev | À planifier |

---

## Prochaine rencontre
**Date prévue** : dans **2 semaines** (mentionnée à la fin de la réunion).
Objet : suivi des actions ci‑dessus, validation du nouveau format de release notes et mise à jour du Kanban.

---

*Compte rendu rédigé par l’assistant IA, basé sur la transcription fournie.*
