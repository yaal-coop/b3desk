# Compte rendu de réunion

**Date** : 28 avril 2026
**Heure** : non précisée (durée estimée : ~1 h)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Loan** | Développeur (présence incertaine) |
| **Mickaël** | Responsable du Kanban / suivi des tickets |
| **Benoît** | Responsable produit / gestion du tableau de bord |
| **Sébastien** | Développeur (migrations) |
| **Benjamin** | Développeur (migrations) |
| **Intervenant** (auteur du compte rendu) | Documentation & déploiement |
| Autres (non nommés) | Participants à la session de partage d’écran |

---

## Objet de la réunion
- Faire le point sur l’avancement de la documentation et du processus de release.
- Nettoyer et clarifier le tableau Kanban (colonnes *backlog*, *ready*, *in progress*, *done*).
- Valider la stratégie de branchement (*main* vs *production*) et le workflow de création de tags/releases.
- Définir le contenu des notes de release (tickets, changements de configuration, migrations).

---

## Sujets abordés

| Sujet | Points clés |
|-------|-------------|
| **Présence de Loan** | Loan devait être présent ; décision de commencer sans lui et de le faire rejoindre plus tard. |
| **Documentation** | Traduction et clarification de la doc pour les non‑experts ; création d’une vidéo de démonstration. |
| **Kanban B3desk** | - Colonne *ready* jugée superflue, à discuter avec Benoît.<br>- Colonne *done* (appelée « d’âne ») très encombrée ; proposition de la vider ou de créer une colonne « à trier ». |
| **Workflow Git** | - Branches : *main* (développement) → *production* (releases).<br>- Merge requests doivent être testées et validées avant d’être mergées dans *main*.<br>- Tags (`vX.Y.Z`) créés sur *production* puis poussés avec `--follow-tags`. |
| **Création de la release v1.3.0** | - Vérification des tickets associés.<br>- Aucun nouveau paramètre de configuration pour cette version (seulement un changement de base). |
| **Contenu des notes de release** | - Lister les tickets avec titre et lien.<br>- Indiquer les changements de base et de configuration.<br>- Ajouter l’identifiant de chaque migration. |
| **Migrations** | - Les identifiants (`hash`) sont générés par une librairie pour ordonner les scripts.<br>- Chaque fonctionnalité distincte possède son propre fichier de migration. |
| **Processus de suivi** | - Créer un ticket Kanban dédié à chaque release (ex. colonne *1.3.0*) regroupant infos config/base + migrations. |
| **Points techniques** | - Vérification de champs `updated_at`, `created_at`, `is_favorite` dans la table `meeting`.<br>- Gestion des conflits de merge (responsabilité de l’équipe dev). |

---

## Décisions prises
| Décision | Responsable(s) |
|----------|-----------------|
| Démarrer la session sans Loan et le faire rejoindre dès son arrivée. | Tous |
| Supprimer ou fusionner la colonne *ready* après discussion avec Benoît. | Benoît + Mickaël |
| Vider la colonne *done* (ou la renommer « à trier ») pour libérer le Kanban fonctionnel. | Mickaël |
| Utiliser *main* pour le développement et *production* pour les releases. | Tous |
| Créer les tags de version sur *production* et pousser avec `--follow-tags`. | Intervenant (déploiement) |
| Les notes de release contiendront : <br>• liens + titres des tickets <br>• changements de base/configuration <br>• identifiants de migration. | Intervenant (documentation) |
| Créer un ticket Kanban dédié à chaque release (ex. *1.3.0*) pour centraliser les infos. | Mickaël |
| Mettre à jour la documentation (procédure de release, migration IDs, etc.) et la vidéo de démonstration. | Intervenant |
| Vérifier les valeurs d’`updated_at`, `created_at` et `is_favorite` pour la migration des salons. | Sébastien |

---

## Questions en suspens
1. **Colonne *ready*** – doit‑elle être conservée ou supprimée ? (en attente de retour de Benoît).
2. **Nouvelle configuration** – confirmation qu’aucune modification de config n’est requise pour la version 1.3.0.
3. **Gestion des conflits de merge** – procédure exacte à suivre lorsqu’un conflit apparaît (qui intervient, comment).
4. **Synchronisation des identifiants de migration** avec les tickets de release – besoin d’un format standardisé ?

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Nettoyer la colonne *done* (ou la renommer « à trier ») | Mickaël | Prochaine réunion |
| Discuter du sort de la colonne *ready* avec Benoît | Benoît + Mickaël | ASAP |
| Mettre à jour la documentation du processus de release (incl. branches, tags, merges) | Intervenant | Avant la prochaine release |
| Ajouter les identifiants de migration et les titres de tickets dans les notes de release | Intervenant | Pour la release v1.3.0 |
| Créer le ticket Kanban « 1.3.0 » regroupant les infos de release | Mickaël | Avant la prochaine release |
| Vérifier les champs `updated_at`, `created_at`, `is_favorite` dans la migration des salons | Sébastien | Avant le déploiement |
| Produire / mettre à jour la vidéo de démonstration du workflow de release | Intervenant | Avant la prochaine release |
| Informer Loan de la prochaine session et vérifier sa disponibilité | Tous | Avant la prochaine réunion |

---

## Prochaine rencontre
- **Date / heure** : à définir (proposition de planifier dès que Loan confirme sa disponibilité).
- **Objectif** : Faire le point sur le nettoyage du Kanban, valider le processus de release finalisé et préparer la prochaine version.

---

*Fin du compte rendu.*
