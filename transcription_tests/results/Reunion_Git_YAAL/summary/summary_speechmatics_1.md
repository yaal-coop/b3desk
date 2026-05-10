# Compte rendu de réunion

**Date** : 4 mai 2026
**Heure** : non précisée (durée estimée ≈ 1 h)
**Objet** : Revue du processus de release, du tableau Kanban et de la documentation de déploiement

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Loane** | (absente, attendue) |
| **Michael** | Responsable du suivi Kanban |
| **Benoît** | Auteur du tableau Kanban, décisionnaire workflow |
| **Rudy** | Mentionné dans le Kanban |
| **Dan** | Mentionné dans le Kanban |
| **Sébastien** | Développeur (modifications DB) |
| **Benjamin** | Responsable des migrations |
| **Autres** (participants non nommés) | Observateurs / contributeurs |

---

## Sujets abordés

| Sujet | Points clés |
|-------|-------------|
| **1. État du tableau Kanban** | - Colonne **Done** surchargée, besoin de nettoyage.<br>- Colonne **Ready** mal positionnée / doublon avec **In Progress**.<br>- Proposition de créer une colonne **« À trier »** pour les tickets anciens. |
| **2. Documentation de déploiement** | - Traduction et clarification des commandes (Vite, Zsh, etc.).<br>- Ajout d’étapes supplémentaires (ex. : création de tag, push du tag). |
| **3. Processus de release** | - Branches : **main** (développement) → **production** (releases).<br>- Merge : création de pull‑request, validation par les testeurs, puis merge dans **main**.<br>- Tagging (ex. : `v1.3`, `v3.0`) et génération de release GitHub. |
| **4. Gestion des tickets** | - Lien entre tickets et releases : inclure le titre et le lien dans la note de release.<br>- Regrouper les changements de configuration/base dans un ticket dédié (ex. : version `3.0`). |
| **5. Migrations de base de données** | - Identifiants de migration (hash) générés par la librairie de migration.<br>- Nécessité d’ajouter ces IDs dans les notes de release pour faciliter le suivi. |
| **6. Points techniques divers** | - Utilisation de **zsh** avec le thème *Spaceship*.<br>- Problèmes de connexion (service de temps, serveur d’identité) et leur prise en compte dans les releases. |
| **7. Prochaine version** | - Prochaine release prévue : **v3.0‑dev** (ou `3.1` selon le contexte).<br>- Étapes de publication : création du tag, push, vérification des diff, mise à jour du tableau. |

---

## Décisions prises

| Décision | Responsable(s) |
|----------|----------------|
| Nettoyer la colonne **Done** et créer une colonne **« À trier »** pour les tickets anciens. | **Michael** |
| Conserver le workflow actuel du Kanban (colonne **Ready** → **In Progress**) mais en discuter avec **Benoît** pour d’éventuels ajustements. | **Benoît** (consulté) |
| Ajouter dans chaque release : <br>• le lien vers le(s) ticket(s) concerné(s) <br>• un titre descriptif <br>• l’identifiant de migration le cas échéant. | **Benjamin** (migration) + **Équipe dev** (release) |
| Mettre à jour la documentation de déploiement avec les nouvelles étapes (tag, push, vérif diff, etc.). | **Speaker** (ou équipe documentation) |
| Sébastien doit corriger les champs `updated_at` / `created_at` dans la table `Meeting`. | **Sébastien** |
| La responsabilité du test et de la validation de la livraison reste à l’équipe de test (speaker). | **Speaker** |

---

## Questions en suspens

| Question | État |
|----------|------|
| Pourquoi la colonne **Ready** apparaît‑elle dans le tableau alors qu’elle devrait être à côté de **In Progress** ? | À clarifier avec **Benoît**. |
| Gestion des conflits lors du merge de **main** → **production** (ex. : `Ignite`, `Pie Project`). | Processus déjà connu, mais besoin d’une procédure standardisée. |
| Comment automatiser l’ajout de l’ID de migration dans les notes de release ? | En cours d’étude par **Benjamin**. |
| Quels changements de configuration doivent être explicitement mentionnés dans les releases ? | À définir au fur et à mesure des tickets. |
| Validation finale du processus de création de tag et de push (ex. : options `--follow-tags`). | À tester lors de la prochaine release. |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Nettoyer la colonne **Done** et créer la colonne **« À trier »**. | **Michael** | Immédiate |
| Discuter du positionnement de la colonne **Ready** avec **Benoît**. | **Benoît** | Avant la prochaine réunion |
| Ajouter les IDs de migration dans les notes de chaque release. | **Benjamin** | Pour la prochaine release (v3.0) |
| Corriger les champs `updated_at` / `created_at` dans la table `Meeting`. | **Sébastien** | ASAP |
| Mettre à jour la documentation de déploiement (zsh, Spaceship, procédure de tag, etc.). | **Speaker** / équipe doc | Avant la prochaine release |
| Publier la release **v3.0‑dev** (création du tag, push, création de la release GitHub). | **Speaker** | Dès que les tickets sont prêts |
| Regrouper les changements de configuration/base dans un ticket dédié pour chaque version. | **Équipe dev** | Pour chaque version future |
| Envoyer le point de suivi des deux semaines (déjà envoyé). | **Speaker** | - |

---

## Prochaine rencontre
- **Date / heure** : à définir (prochaine réunion prévue dans deux semaines, selon le point envoyé).
- **Objectif** : Faire le point sur le nettoyage du Kanban, valider la nouvelle procédure de release et vérifier les migrations en cours.

---

*Fin du compte rendu.*
