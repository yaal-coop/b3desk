# Compte rendu de réunion

**Date** : 28 avril 2026
**Durée** : prévue 1 h, réelle ≈ 2 h 30
**Objet** : Point d’avancement sur le projet BBB / Betfridesk (code unique, configuration, releases, budget, stabilité Nextcloud, messagerie nationale).

---

## Participants
- **Benjamin** (développeur)
- **Miguel** (analyseur)
- **Arwa** (configuration VisioTest)
- **Benoît** (tests)
- **Pierre** (support)
- **Michael** (planification)
- **Mickaël** (budget / juridique)
- **Sébastien** (procédure de release)

---

## Sujets abordés

| N° | Sujet | Points clés |
|----|-------|-------------|
| 1 | **Rythme des réunions** | Proposition d’un point toutes les 2 semaines, le mercredi à 11 h 30. |
| 2 | **Livraison du code unique** | - Questions sur la complétude du livrable.<br>- Nécessité d’ajouter un paramètre de configuration (PR). |
| 3 | **Scénario de test v3** | - Changer la configuration pour activer la nouvelle option.<br>- Vérifier l’affichage du PIN téléphonique et son édition. |
| 4 | **Migrations & releases** | - Ordre des migrations (tri → code unique).<br>- Toutes les migrations seront exécutées dans l’ordre dans la release. |
| 5 | **Ticket #666 – erreur de salon** | - Résolu par Arwa (suppression d’un champ).<br>- Conservation de la remontée de logs dans la prochaine release. |
| 6 | **Instabilité du token Nextcloud** | - Capture de trames réalisée.<br>- Hypothèses : surcharge du serveur, bibliothèque Python obsolète, durée du token (30 j). |
| 7 | **Budget & financement** | - 2 025 € alloués au développement Betfridesk.<br>- Projet de connecteur BBB financé par la DGFI. |
| 8 | **Messagerie nationale** | - Devis validé, besoin de support juridique.<br>- Salon en mode « silencieux » en attente de validation finale. |
| 9 | **Plan de release 1.3** | - Création prévue à 14 h le même jour.<br>- Exclusion du numéro d’appel et du code unique (prévu pour une release ultérieure). |
|10| **Estimation des tâches** | - Utilisation de tags (XS, S, M, L) pour chiffrer en jours/homme.<br>- Michael doit fournir le tableau de correspondance. |
|11| **Procédure de release** | - Sébastien a présenté la procédure ; Benjamin la reproduira cet après‑midi. |

---

## Décisions prises

- **Calendrier** : réunion bi‑hebdomadaire chaque mercredi à 11 h 30. Benjamin enverra l’invitation.
- **PR** : le paramètre de configuration manquant sera ajouté dans la PR et documenté.
- **Log** : la remontée de logs du ticket #666 sera conservée dans la prochaine release.
- **Release 1.3** : sera réalisée à 14 h le 28 / 04 / 2026 (sans le numéro d’appel ni le code unique).
- **Budget** : le montant de 2 025 € pour Betfridesk est approuvé ; le projet de connecteur BBB avance sous financement DGFI.
- **Salon silencieux** : maintenu en attente de validation du devis et du support juridique.
- **Tagging** : les tâches seront taguées (XS‑L) ; Michael enverra le tableau de correspondance d’ici la fin de journée.

---

## Questions en suspens

1. **Quand intégrer le code unique et le numéro unique** (release 1.4 ou ultérieure ?) – à confirmer avec Benoît / Pierre.
2. **Stabilité du token Nextcloud** – besoin de reproduire le problème de façon fiable et d’identifier si la bibliothèque Python doit être mise à jour.
3. **Durée du token** – envisager d’allonger la validité (> 30 j) pour réduire les appels au portail.
4. **Support juridique** pour la messagerie nationale – état d’avancement à préciser.
5. **Coordination avec Renater** pour les adaptations techniques du connecteur BBB.

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Envoyer l’invitation du point bi‑hebdomadaire | **Benjamin** | 30 / 04 / 2026 |
| Ajouter le paramètre manquant dans la PR et le documenter | **Benjamin** | Avant la release 1.3 |
| Fournir le scénario de test v3 (configuration + PIN) | **Benjamin** | Avant la release 1.3 |
| Vérifier l’ordre des migrations et les inclure dans la release | **Benjamin** | Avant la release 1.3 |
| Conserver la remontée de logs du ticket #666 dans la release | **Équipe dev** | Release 1.3 |
| Mettre à jour la configuration sur VisioTest (Arwa) | **Arwa** | Avant la release 1.3 |
| Réaliser des tests d’instabilité du token Nextcloud | **Benoît** | 05 / 05 / 2026 |
| Analyser les captures de trames et proposer des améliorations | **Miguel** | 07 / 05 / 2026 |
| Envoyer le tableau de correspondance tags ↔ estimation | **Michael** | 31 / 04 / 2026 |
| Suivre la procédure de création de release (Sébastien) | **Sébastien** (guidage) / **Benjamin** (exécution) | 28 / 04 / 2026, 14 h |
| Valider le support juridique pour la messagerie nationale | **Mickaël** | 10 / 05 / 2026 |
| Planifier la prochaine release (intégrant numéro d’appel & code unique) | **Équipe produit** | À définir (post‑release 1.3) |

---

## Prochaine rencontre

- **Date** : mercredi 5 mai 2026
- **Heure** : 11 h 30 (rappel du créneau bi‑hebdomadaire)
- **Ordre du jour prévisionnel** :
  1. Retour sur les tests du token Nextcloud.
  2. Avancement du support juridique messagerie nationale.
  3. Planification de la release incluant le code unique/numéro unique.
  4. Point sur le projet de connecteur BBB (DGFI).

---

*Fin du compte rendu.*
