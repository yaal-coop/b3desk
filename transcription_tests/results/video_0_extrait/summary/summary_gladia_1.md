# Compte rendu de réunion

**Date** : 4 mai 2026
**Durée** : ~ 2 h 30 (prévue 1 h)

---

## Participants
- **Benjamin** (tests & captures de trafic)
- **Benoît** (tests navigateur)
- **Mickaël** (suivi projets & finances)
- **Autres membres de l’équipe B3Desk** (intervenants non nommés)
- **Renater** (développeur interne, mentionné)
- **MTE** – Ministère de la Transition écologique (mentionné)

---

## Objet de la réunion
1. **Investigations sur les performances de Nextcloud/Nuage** (connexion B3Desk ↔ Nuage, token, WebDAV).
2. **Suivi du projet d’API messagerie nationale** (devis, budget, support juridique).
3. **Mise à jour sur le projet SIP Media Gateway** (intégration SIP ↔ BBB, financement DGFILM, coordination avec Renater).

---

## Sujets abordés
| Thème | Points clés |
|-------|-------------|
| **Connexion B3Desk ↔ Nuage** | - Le token (validité 30 j) est obtenu une fois, puis les requêtes WebDAV passent directement sur Nuage.<br>- La cinématique est correcte, mais la connexion est parfois lente ou instable.<br>- Hypothèses : surcharge du serveur Nuage, bibliothèque Python WebDAV obsolète, version de Nextcloud. |
| **Tests & reproductions** | - Benjamin a réalisé des captures de trafic (visiotest) montrant les temps de réponse.<br>- Benoît rencontre des problèmes avec son navigateur (plugins).<br>- Nécessité de reproduire le dysfonctionnement en conditions réelles. |
| **Améliorations possibles** | - Vérifier/mettre à jour les librairies Python utilisées.<br>- Envisager d’allonger la durée du token applicatif (> 30 j) pour la mise en production.<br>- Si le protocole WebDAV reste problématique, envisager une alternative (API). |
| **Projet API messagerie nationale** | - Devis transféré à l’équipe messagerie, validation budgétaire confirmée.<br>- Besoin de finaliser le support juridique.<br>- Le « salon silencieux » peut être lancé dès que le support juridique est en place. |
| **Budget 2025 – BestProdesk** | - Un budget dédié a été alloué, il faut identifier le vecteur financier pour le commander. |
| **Projet SIP Media Gateway** | - Financement DGFILM confirmé.<br>- Nécessité d’intégrer un connecteur SIP à BBB et de générer les liens CIP.<br>- Renater développe les briques internes ; adaptation nécessaire car leurs technologies diffèrent.<br>- Discussion sur le périmètre fonctionnel à livrer avant d’envisager des développements supplémentaires. |
| **Organisation future** | - Une réunion technique dédiée avec Benjamin pour cadrer l’offre actuelle du SIP Media Gateway.<br>- Suivi des spécifications et des besoins exprimés par le MTE. |

---

## Décisions prises
1. **Poursuivre les tests** afin de reproduire le problème de connexion WebDAV.
2. **Mettre à jour** les librairies Python utilisées dans B3Desk (si besoin).
3. **Conserver l’action** de reproduction du problème comme priorité jusqu’à identification claire.
4. **Valider le devis** de l’API messagerie : le salon silencieux peut être lancé immédiatement (en attente du support juridique).
5. **Allouer le budget 2025** au développement BestProdesk ; recherche du vecteur financier à finaliser.
6. **Planifier une réunion** (voir section « Tâches à effectuer ») pour définir le périmètre fonctionnel du projet SIP Media Gateway.

---

## Questions en suspens
- Quelle est la cause exacte de l’instabilité WebDAV ? Surcharge du serveur Nuage ou bibliothèque Python obsolète ?
- Quelle version de Nextcloud offre la meilleure stabilité ?
- Faut‑il augmenter la durée de validité du token applicatif (au‑delà de 30 j) ?
- Quel sera le support juridique exact nécessaire pour le lancement du projet messagerie ?
- Quels sont les besoins fonctionnels détaillés du projet SIP Media Gateway et quelles adaptations Renater devra fournir ?

---

## Tâches à effectuer

| Action | Responsable | Échéance (provisoire) |
|--------|-------------|----------------------|
| Refaire les captures de trafic (tram) et reproduire le problème de connexion WebDAV. | **Benjamin** | 1 semaine |
| Effectuer des tests avec le navigateur de Benoît et remonter les échecs. | **Benoît** | 1 semaine |
| Vérifier et mettre à jour les librairies Python WebDAV utilisées dans B3Desk. | **Équipe technique B3Desk** | 2 semaines |
| Rechercher et sécuriser le support juridique pour le projet API messagerie. | **Mickaël** (ou référent juridique) | 2 semaines |
| Finaliser le vecteur financier pour le budget 2025 BestProdesk. | **Équipe finance** | 3 semaines |
| Organiser une réunion technique pour cadrer l’offre actuelle du SIP Media Gateway. | **Benjamin** | 10 jours |
| Recueillir les nouvelles spécifications du MTE et les besoins de Renater. | **Mickaël** | 2 semaines |

---

## Prochaine rencontre
**Date** : à définir (proposition : dans deux semaines, le même créneau).
**Objet** :
- Point sur les résultats des tests WebDAV et mise à jour des librairies.
- Avancement du support juridique et du financement messagerie.
- Définition du périmètre fonctionnel du projet SIP Media Gateway.

---

*Fin du compte rendu.*
