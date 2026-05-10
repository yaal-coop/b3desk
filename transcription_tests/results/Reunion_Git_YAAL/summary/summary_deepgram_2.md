# Compte rendu de réunion

**Date** : 30 avril 2026
**Durée** : environ 45 minutes (durée exacte non précisée)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Michael** | Responsable du suivi du tableau de tâches et de la documentation |
| **Lohan** | Expert produit / process (présence incertaine) |
| **Owen** | Présent (mentionné) |
| **Benoît** | Auteur du tableau de suivi des tâches, responsable du nettoyage des versions |
| **Benjamin** | Responsable des migrations et de la génération des identifiants de migration |
| **Sébastien** | Contributeur aux migrations (validation des champs) |
| *(autres participants non nommés)* | – |

---

## Objet de la réunion
Harmoniser le processus de **release** (fusion, création de tag, publication), nettoyer le tableau de suivi des tâches, et définir le format des notes de version (tickets, changements de configuration, identifiants de migration).

---

## Sujets abordés
1. **Présence de Lohan** – décision d’attendre ou de poursuivre sans lui.
2. **État du tableau de tâches**
   - Colonnes « Ready », « In Progress », colonnes obsolètes.
   - Nécessité de vider la colonne « Done » surchargée.
3. **Processus de release**
   - Branches : `main` (développement) → `production` (release).
   - Merge de `main` vers `production`, résolution des conflits, création d’un tag (`vX.Y.Z`).
   - Publication du tag sur GitHub → page *Releases*.
4. **Contenu des notes de version**
   - Titres des tickets, liens, description succincte.
   - Indication des **changements de configuration** et des **migrations** (identifiant de migration).
5. **Migrations**
   - Fonctionnement des identifiants (hash générés par la librairie de migration).
   - Gestion de plusieurs fichiers de migration distincts.
6. **Responsabilités**
   - Michael : nettoyage du tableau, mise à jour du document de release.
   - Benjamin & Sébastien : vérification et ajout des identifiants de migration dans les notes.
   - Benoît : suppression des versions mineures et maintien de la propreté du tableau.
7. **Prochaine mise à jour de la documentation** – ajout d’une section « Release checklist » et d’une vidéo de rappel.

---

## Décisions prises
- **Attente de Lohan** : si Lohan arrive tard, la réunion continue sans lui.
- **Nettoyage du tableau** : la colonne « Ready » sera vidée ; les tickets seront re‑classés dans les colonnes adéquates ou déplacés dans une nouvelle colonne « À trier ».
- **Processus de release** confirmé :
  1. Merge `main` → `production`.
  2. Résolution des conflits éventuels.
  3. Création du tag (`vX.Y.Z`).
  4. Publication du tag sur GitHub → création de la *Release*.
- **Notes de version** : chaque release contiendra
  - le titre du ticket + lien,
  - les changements de configuration (le cas échéant),
  - les identifiants de migration associés.
- **Documentation** : sera mise à jour avec le format ci‑dessus et une vidéo explicative.
- **Responsabilité du test** : Michael teste la livraison ; les développeurs restent responsables du code et du déploiement.

---

## Questions en suspens
| Question | Responsable | Commentaire |
|----------|-------------|--------------|
| Y a‑t‑il de nouvelles configurations à appliquer pour cette release ? | Michael / Benoît | Aucun changement identifié pour l’instant, à confirmer. |
| Qui assure la publication finale du *Release* après création du tag ? | À définir (probablement Michael ou Benoît) | Processus à préciser. |
| Gestion des conflits de merge : procédure détaillée à formaliser ? | Michael | Documenter les étapes de résolution. |
| Comment automatiser l’ajout des identifiants de migration dans les notes ? | Benjamin & Sébastien | À étudier (script ou template). |

---

## Tâches à effectuer
| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Nettoyer la colonne « Ready » et reclasser les tickets (ou créer « À trier ») | **Michael** | ASAP |
| Mettre à jour le tableau avec les colonnes correctes (In Progress, Done, …) | **Michael** | ASAP |
| Ajouter les titres + liens des tickets dans les notes de version | **Michael** | Avant la prochaine release |
| Insérer les changements de configuration dans les notes (si applicable) | **Benoît** | Avant la prochaine release |
| Ajouter les identifiants de migration (hash) dans les notes de version | **Benjamin** & **Sébastien** | Avant la prochaine release |
| Rédiger / mettre à jour le document de *Release checklist* | **Michael** | Dans les 2 semaines |
| Enregistrer une vidéo de démonstration du processus de release | **Michael** | Dans les 2 semaines |
| Formaliser la procédure de résolution de conflits de merge | **Michael** | Dans les 2 semaines |

---

## Prochaine rencontre
- **Date prévue** : dans **deux semaines** (date exacte à confirmer).
- **Objectif** : revue du tableau nettoyé, validation du nouveau format de notes de version et état d’avancement des tâches listées ci‑dessus.

---

*Fin du compte rendu.*
