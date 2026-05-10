# Compte rendu de réunion

**Date** : 5 mai 2026
**Durée estimée** : ~ 1 h 30 (la réunion était prévue 1 h mais a duré plus longtemps)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| Johan | Animateur de la réunion |
| Bastien | Développeur |
| Benjamin | Développeur / Responsable PR |
| Mickaël | Développeur (configuration) |
| Benoît | Responsable tests & suivi |
| Michael | Responsable architecture & estimation |
| Sébastien | Responsable release |
| Nathalie | (mentionnée pour suivi montée en charge) |
| Autres (ex. : participants de la messagerie nationale) |  |

---

## Objet de la réunion
- Mettre en place un point de suivi bi‑hebdomadaire.
- Faire le point sur les livraisons récentes (code unique, configuration, migrations).
- Traiter les incidents et tickets en cours (ticket 166, connexion Nuage/Nextcloud).
- Discuter du lancement du **salon silencieux** et du **devis** associé.
- Planifier la prochaine **release 1.3** et définir les priorités du backlog.
- Établir une méthode d’estimation des tâches (tags ↔ durée).

---

## Sujets abordés

| N° | Sujet | Principaux éléments discutés |
|----|-------|------------------------------|
| 1 | **Fréquence des réunions** | Proposition d’un point toutes les deux semaines, le mercredi à 11 h 30. |
| 2 | **Livraison du code unique** | - Besoin de préciser un paramètre de configuration (variable à préciser). <br>- Ajouter cette précision dans la PR et la release. |
| 3 | **Scénario de test B3 Desk / BVB ping** | Demande d’un scénario de test pour valider le nouveau ping et le PIN généré. |
| 4 | **Configuration du numéro de téléphone (Bebé Medianumber)** | - Le numéro doit être configuré côté Skyline puis répercuté dans la config Metro Desk. <br>- Variable identifiée : `BB_number` (ou `TheNumber`). |
| 5 | **Migrations & ordre de déploiement** | - La migration du tri doit précéder celle du code unique. <br>- Toutes les migrations seront exécutées dans l’ordre par la release. |
| 6 | **Ticket 166 – Erreur 500 salon** | Problème de cohérence de donnée résolu côté Arawa. Conservation de la remontée de logs dans la prochaine release. |
| 7 | **Instabilité connexion Nuage / Nextcloud** | - Analyse des captures de trames : problème possible de surcharge du serveur ou de la bibliothèque WebDAV. <br>- Nécessité de reproduire le dysfonctionnement et de vérifier les versions des librairies. |
| 8 | **Projet Media Gateway (SIP A/B)** | - Devis validé, financement prévu par la DGFIP. <br>- Besoin de définir le support juridique et le vecteur financier. |
| 9 | **Salon silencieux** | - Attente de validation du devis (déjà faite). <br>- Lancement dès que le support financier est confirmé. |
|10| **Backlog & estimation des tâches** | - Utilisation de tags (XS, S, M, L, XL) à associer à une durée (jours/heures). <br>- Demande d’un tableau de correspondance. |
|11| **Création de la release 1.3** | - Sébastien animera la procédure cet après‑midi à 14 h. <br>- La release contiendra les changements validés, sauf le numéro d’appel/code unique qui sera reporté. |

---

## Décisions prises

| Décision | Responsable / Commentaire |
|----------|----------------------------|
| Instaurer une réunion toutes les deux semaines, le **mercredi à 11 h 30**. | Johan (organisation du planning) |
| Ajouter la modification de configuration (paramètre du code unique) dans la **PR** et la **release**. | Benjamin (mise à jour PR) |
| Conserver la remontée de logs du ticket 166 dans la prochaine release. | Benjamin |
| Prioriser le **salon silencieux** dès que le devis est validé (déjà le cas). | Benoît (lancement) |
| La **release 1.3** sera créée cet après‑midi à **14 h**. | Sébastien |
| Reporter le **numéro d’appel / code unique** à une version ultérieure (post‑1.3). | Michael |
| Continuer l’investigation sur la connexion Nuage/Nextcloud : reproduire le problème, analyser les logs, vérifier les versions des librairies WebDAV. | Benoît & Michael |
| Fournir **dans la journée** un tableau de correspondance *tags ↔ estimation* (jours/heure). | Michael (ou Sébastien) |
| Vérifier que la migration du **tri** est bien appliquée avant celle du code unique. | Benjamin |
| Lancer les démarches de **support juridique et financier** pour le projet Media Gateway. | Michael |

---

## Questions en suspens

1. **Scénario de test exact** pour le nouveau ping BVB et le PIN : qui le rédige ?
2. **Nom exact du paramètre** à modifier dans la configuration du code unique (variable).
3. **Ordre définitif des migrations** dans la release : confirmation que le tri sera bien exécuté en premier.
4. **Intégration du code unique** : date précise (release 1.4 ? ).
5. **Validation du budget 2025** pour le développement 3D.
6. **Détails du support juridique** pour le projet Media Gateway.
7. **Impact éventuel d’une mise à jour de Nextcloud** sur la stabilité de la connexion.

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Envoyer le planning de la réunion bi‑hebdomadaire (mercredi 11 h 30). | Johan | Immédiat |
| Préciser le paramètre de configuration du code unique dans la PR. | Benjamin | Avant la release 1.3 |
| Mettre à jour la documentation de la PR avec le paramètre. | Benjamin | Avant la release 1.3 |
| Vérifier que la migration du tri est appliquée avant celle du code unique. | Benjamin | Avant la release 1.3 |
| Reproduire le problème de connexion Nuage/Nextcloud et fournir les logs. | Benoît | Au plus tard 12 mai 2026 |
| Vérifier et mettre à jour les librairies Python WebDAV si besoin. | Michael | Au plus tard 12 mai 2026 |
| Envoyer le tableau de correspondance *tags ↔ estimation* (jours/heure). | Michael (ou Sébastien) | Dans la journée |
| Créer la **release 1.3** (procédure, tags, builds). | Sébastien | 5 mai 2026, 14 h |
| Lancer le **salon silencieux** après validation du devis. | Benoît | Dès que le support financier est confirmé |
| Démarrer les démarches de support juridique et financier pour le projet Media Gateway. | Michael | Semaine prochaine |
| Suivi du budget 2025 pour le développement 3D. | Michael | À définir |

---

## Prochaine rencontre

- **Réunion de suivi** : **mercredi 12 mai 2026 à 11 h 30** (point bi‑hebdomadaire).
- **Session release 1.3** : **jeudi 5 mai 2026 à 14 h** (Sébastien animera).

---

*Fin du compte rendu.*
