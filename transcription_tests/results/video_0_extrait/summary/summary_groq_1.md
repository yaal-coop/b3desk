# Compte rendu de réunion

**Date** : 30 avril 2026
**Durée estimée** : ~ 2 h 30

---

## Participants
- **Benjamin** (tests & captures de trafic)
- **Benoît** (tests navigateur)
- **Mickael** (coordination projets)
- **Intervenants non nommés** (chef de projet, finance, juridique)
- **Renater** (développements internes CIME/ESOE) – mentionné comme partie prenante

---

## Objet de la réunion
1. Analyse des lenteurs / instabilités de la connexion **B3Desk ↔ Nextcloud (Nuage)** via WebDAV.
2. Suivi du **devis API messagerie nationale** et mise en place du « salon silencieux ».
3. Présentation du **budget 2025** pour le développement de **Best for Desk**.
4. Avancement du **projet SIP Media Gateway** (intégration SIP à BBB) et coordination avec **Renater**.

---

## Sujets abordés

| N° | Sujet | Points clés |
|---|-------|-------------|
| 1 | **Performance B3Desk‑Nuage** | - Le token (validité 30 j) est obtenu une fois, puis les requêtes passent uniquement sur le Nuage. <br>- La lenteur provient de la connexion B3Desk → Nuage (WebDAV). <br>- Hypothèses : surcharge du serveur Nuage, bibliothèque Python WebDAV obsolète, plugins navigateur, configuration réseau. |
| 2 | **Reproduction du problème** | - Benjamin a capturé le trafic (Viziotest) : montre les temps de réponse. <br>- Benoît doit refaire les tests avec un navigateur « clean ». <br>- Nécessité de reproduire le dysfonctionnement de façon fiable pour analyser la cinématique. |
| 3 | **Token applicatif** | - Validité actuelle : 30 jours. <br>- Discussion sur l’allongement de la durée pour réduire les appels au portail Apps. |
| 4 | **Devis API messagerie nationale** | - Devis validé, aucune objection. <br>- Attente du support juridique avant lancement officiel. <br>- Décision de créer un « salon silencieux » en attendant les retours. |
| 5 | **Budget 2025 – Best for Desk** | - Besoin de sécuriser le financement. <br>- Le budget sera attribué une fois le vecteur financier identifié. |
| 6 | **Projet SIP Media Gateway** | - Financement confirmé par la DGFIP. <br>- Nécessite des développements côté Renater (adaptation d’une brique existante). <br>- Possibilité de financer des développements supplémentaires via Renater. |
| 7 | **Coordination avec Renater** | - Renater réalise les développements internes CIME/ESOE. <br>- Il faut clarifier les spécifications fonctionnelles attendues par le ministère et Bercy. |
| 8 | **Organisation de réunions futures** | - Une réunion technique dédiée aux spécifications et aux capacités actuelles sera planifiée. |

---

## Décisions prises
1. **Conserver l’action de reproduction du problème** B3Desk ↔ Nuage et analyser la cinématique lors de chaque occurrence.
2. **Reporter l’évaluation du protocole WebDAV** (et éventuel changement) à la prochaine réunion.
3. Le **devis API messagerie nationale est validé** ; le salon silencieux peut être lancé dès que le volet juridique sera confirmé.
4. **Le financement du projet SIP Media Gateway** est assuré (DGFIP) ; une réunion avec Renater sera organisée pour définir les adaptations nécessaires.
5. **Planifier une réunion technique** (date à définir) pour : <br>‑ Faire le point sur les tests WebDAV, <br>‑ Valider les spécifications SIP, <br>‑ Déterminer les livrables et les besoins de financement.

---

## Questions en suspens
- Quelle est la cause exacte de l’instabilité ? (surcharge du serveur Nuage, bibliothèque Python obsolète, problème de token, etc.)
- Le token applicatif doit‑il être prolongé au‑delà de 30 jours ?
- Quels sont les besoins fonctionnels précis du ministère et de Bercy pour le connecteur SIP ?
- Quel type de support juridique est requis pour le lancement du salon silencieux ?
- Quels développements supplémentaires Renater doit‑il réaliser et qui les financera ?
- Quand le salon silencieux sera‑t‑il effectivement activé ?

---

## Tâches à effectuer

| Responsable | Action | Échéance (indicative) |
|-------------|--------|-----------------------|
| **Benjamin** | Réaliser de nouveaux tests de capture de trafic (Viziotest) pour reproduire le problème et identifier la cinématique exacte. | 1 semaine |
| **Benoît** | Effectuer des tests avec un navigateur « clean » (sans plugins) et communiquer les résultats. | 1 semaine |
| **Chef de projet / PO** | Analyser la pertinence d’allonger la durée de validité du token (ex. > 30 j). | 2 semaines |
| **Finance / Responsable budget** | Sécuriser le support financier pour le budget 2025 (Best for Desk) et le projet SIP Media Gateway. | 3 semaines |
| **Mickael** | Organiser une réunion avec Renater pour discuter des adaptations nécessaires et du financement des développements supplémentaires. | 2 semaines |
| **Coordinateur juridique** | Vérifier les exigences juridiques pour le lancement du salon silencieux et préparer les documents requis. | 1 semaine |
| **Équipe dev** | Vérifier et, si besoin, mettre à jour les librairies Python utilisées pour le WebDAV. | 2 semaines |
| **Tous** | Mettre à jour le tableau de suivi des incidents WebDAV avec les nouvelles captures et observations. | En continu |

---

## Prochaine rencontre
- **Objet** : Point technique sur les tests WebDAV, validation des spécifications SIP, état du financement.
- **Date / Heure** : À définir (proposition : dans 2 semaines).
- **Participants attendus** : Benjamin, Benoît, Mickael, représentant de Renater, chef de projet, finance, juridique.

---

*Fin du compte rendu.*
