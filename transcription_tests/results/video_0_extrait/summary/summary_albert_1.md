# Compte‑rendu de réunion

**Date** : 30 avril 2026
**Durée** : ~ 2 h 30 (prévue 1 h)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Benjamin** | Développeur B3Desk – tests WebDAV |
| **Benoît** | Utilisateur / testeur (navigateur chargé) |
| **Mickaël** | Responsable suivi projets / budget |
| **Autres membres de l’équipe** | (non nommés explicitement) |

---

## Objet de la réunion
1. **Analyse des lenteurs / instabilités** entre B3Desk et le service Nuage (Nextcloud) – token, WebDAV, bibliothèque Python.
2. **État d’avancement** de l’API de messagerie nationale (déploiement, budget, support juridique).
3. **Budget 2025** dédié au développement de Best 3 Desk.
4. **Projet SIP Media Gateway** (intégration d’un connecteur SIP à BBB) – financement, spécifications, dépendances avec Renater.

---

## Sujets abordés & décisions prises

| Sujet | Points clés | Décision |
|-------|-------------|----------|
| **1. Problème de connexion B3Desk ↔ Nuage** | - Les requêtes passent uniquement via Nuage après obtention du token (validité 30 j). <br>- Le problème ne survient pas systématiquement ; besoin de reproduire les échecs. <br>- Hypothèses : surcharge du serveur Nextcloud, bibliothèque Python WebDAV obsolète, instabilité du protocole WebDAV, version de Nextcloud. | - **Action** : poursuivre les tests pour reproduire le dysfonctionnement et capturer les traces (see *Tâches*). <br>- Garder l’action en cours jusqu’à preuve du problème. |
| **2. API messagerie nationale** | - Aucun nouveau besoin pour le moment, projet en **stand‑by**. <br>- Devis déjà validé et transmis à l’équipe messagerie. <br>- Nécessité de trouver un support juridique avant le lancement. | - Autoriser le **salon silencieux** (mise en attente) jusqu’à réception du support juridique. |
| **3. Budget 2025 – Best 3 Desk** | - Budget disponible pour le développement en 2025. <br>- Besoin de définir le vecteur financier (qui finance). | - Validation du budget ; il faut maintenant identifier le **support financier**. |
| **4. SIP Media Gateway** | - Projet porté par la DGFIC, implique un connecteur SIP pour BBB. <br>- Coordination nécessaire avec Renater (développements internes). <br>- Possibles extensions fonctionnelles demandées par la CIP/ Bercy. <br>- Risque de délai important si on attend le développement complet de Renater. | - Démarrer avec les **fonctionnalités existantes** et prévoir une évolution financée séparément. <br>- Organiser une réunion dédiée (voir *Prochaine rencontre*). |

---

## Questions en suspens
1. **Quelle est la cause exacte** de l’instabilité du WebDAV ? (surcharge serveur, bibliothèque Python, protocole, version Nextcloud…)
2. **Le token applicatif** doit‑il être prolongé au‑delà de 30 jours pour réduire les appels au portail Apps ?
3. **Quel support juridique** est requis pour lancer l’API messagerie ?
4. **Quel est le périmètre exact** des fonctionnalités SIP que nous pouvons livrer immédiatement vs celles nécessitant un financement supplémentaire auprès de Renater ?

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Reproduire le problème de connexion et capturer les traces (traces / timings). | **Benjamin** | ASAP |
| Effectuer les tests sur l’environnement de Benoît (navigateur chargé, plugins). | **Benoît** | ASAP |
| Vérifier que les bibliothèques Python utilisées pour le WebDAV sont à jour. | **Équipe dev** | 1 semaine |
| Proposer une éventuelle extension de la durée de validité du token (ex. > 30 j). | **Mickaël** + **Benjamin** | 2 semaines |
| Informer via Tchap le moment où le travail sur l’API messagerie pourra démarrer. | **Mickaël** | Dès que le support juridique est obtenu |
| Identifier le **support juridique** nécessaire et le mettre en place. | **Mickaël** (ou personne désignée) | 2 semaines |
| Définir le **vecteur financier** pour le budget 2025 Best 3 Desk. | **Mickaël** | 3 semaines |
| Préparer le cahier des charges initial du projet SIP Media Gateway (fonctionnalités livrables immédiatement). | **Benjamin** (co‑pilotage) | 1 mois |
| Organiser une réunion de cadrage SIP Media Gateway (participants : équipe B3Desk, Renater, représentants DGFIC). | **Mickaël** | Avant fin mai 2026 |

---

## Prochaine rencontre
- **Objet** : Cadrage du projet SIP Media Gateway & point d’avancement sur les tests WebDAV.
- **Date proposée** : à définir (idéalement la première semaine de mai 2026).
- **Participants attendus** : Benjamin, Benoît, Mickaël, représentants de Renater et DGFIC.

---

*Fin du compte‑rendu.*
