# Compte rendu de réunion

**Date** : 30 avril 2026
**Heure** : non précisée (durée estimée ≈ 1 h)

---

## Participants
- **Lohan** (dev) – attendu au début de la réunion
- **Benoît** (product owner / responsable du Kanban)
- **Michael** (développeur, responsable du déploiement)
- **Benjamin** (développeur, migrations)
- **Sébastien** (développeur, base de données)
- **Speaker** (facilitateur, rédacteur de la documentation)

---

## Objet de la réunion
Revoir et harmoniser le processus de **déploiement / release** du projet B3desk :
- état du tableau Kanban,
- flux de travail entre les branches `main` et `production`,
- création des tags et des releases GitHub,
- contenu des notes de release (tickets, modifications de base/config, identifiants de migration),
- mise à jour de la documentation et des supports vidéo.

---

## Sujets abordés
| N° | Sujet |
|----|-------|
| 1 | Présence de Lohan et démarrage de la session. |
| 2 | Analyse du tableau Kanban : colonnes *Backlog*, *Ready*, *Done* et incohérences. |
| 3 | Workflow de merge : pull‑request, validation, résolution de conflits. |
| 4 | Structure des branches : `main` (développement) vs `production` (releases). |
| 5 | Processus de création de tags et de publications de releases sur GitHub. |
| 6 | Informations à inclure dans les notes de release : tickets, titres, liens, modifications de base et de configuration, identifiants de migration. |
| 7 | Gestion des migrations de base de données (identifiants, ordre d’exécution). |
| 8 | Mise à jour de la documentation OpenDocs et création d’une vidéo tutoriaire. |
| 9 | Répartition des responsabilités entre dev, test et déploiement. |
|10| Plan d’action pour la prochaine version (3.1 dev). |

---

## Décisions prises
1. **Attente de Lohan** – si absent, la réunion peut commencer, mais les points critiques seront revus avec lui dès son arrivée.
2. **Nettoyage du Kanban** – la colonne *Done* sera vidée ou déplacée dans une nouvelle colonne *À trier* afin de libérer le tableau fonctionnel.
3. **Clarification du workflow** – la colonne *Ready* sera supprimée ou re‑définie (actuellement redondante avec *Done*). Benoît sera consulté pour valider le nouveau schéma.
4. **Structure des releases** – les notes de release contiendront :
   - le titre et le lien de chaque ticket concerné,
   - les modifications de base et de configuration,
   - l’identifiant de chaque migration.
5. **Branches** – le développement continue sur `main`; `production` ne reçoit que les merges validés et sert de base aux releases.
6. **Gestion des conflits** – les conflits de merge seront résolus par le développeur concerné (ex. Michael).
7. **Documentation** – le speaker mettra à jour OpenDocs, ajoutera les nouvelles étapes et enregistrera une vidéo de démonstration.
8. **Responsabilités** :
   - **Développeurs** (Michael, Benjamin, Sébastien) : code, migrations, merges.
   - **Speaker** : tests de livraison, validation, documentation et communication.
   - **Benoît** : validation du Kanban et du processus de release.
9. **Suivi** – un point d’avancement sera envoyé dans deux semaines.

---

## Questions en suspens
- Pourquoi la colonne *Ready* a‑t‑elle été introduite ? Quelle valeur ajoute‑t‑elle réellement ?
- Niveau de détail souhaité dans les notes de release : titre uniquement ou courte description supplémentaire ?
- Méthode de suivi automatisé des migrations (ID ↔ release) – besoin d’un petit script ou d’une convention ?
- Qui sera le responsable final de la création du ticket « Release » dans le Kanban ?
- Validation finale du processus de merge/conflict resolution : besoin d’un guide partagé ?

---

## Tâches à effectuer
| Action | Responsable | Échéance |
|--------|-------------|----------|
| Nettoyer la colonne *Done* du tableau Kanban et créer la colonne *À trier* si besoin. | Speaker (avec l’aide de Michael) | Immédiate |
| Supprimer ou redéfinir la colonne *Ready* après validation avec Benoît. | Benoît | 1 semaine |
| Ajouter à chaque release : titre + lien du ticket, modifications base/config, ID de migration. | Michael (tickets) & Benjamin (ID migration) | Avant la prochaine release (v3.1 dev) |
| Mettre à jour la documentation OpenDocs avec le nouveau workflow et les étapes de release. | Speaker | Avant la fin de la semaine |
| Enregistrer et partager une vidéo de démonstration du processus de merge & release. | Speaker | 2 jours |
| Vérifier et corriger les configurations spécifiques (ex. paramètre `hisfavorite`). | Sébastien | Avant la release v3.1 |
| Préparer la prochaine version **3.1 dev** (mise à jour du `pyproject.toml`, tags, etc.). | Michael | Avant la fin du sprint |
| Envoyer le point d’avancement dans deux semaines. | Speaker | Dans 14 jours |
| Réunir les retours sur le format des notes de release et ajuster le template. | Benoît & Michael | Prochaine réunion |

---

## Prochaine rencontre
**Date prévue** : dans **deux semaines** (date exacte à confirmer).
Objectif : faire le point sur les actions ci‑dessus, valider le nouveau tableau Kanban et présenter la prochaine release 3.1 dev.
