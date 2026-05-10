# Compte rendu de réunion

**Date** : 30 avril 2026
**Heure** : non précisée (durée estimée non indiquée)

---

## Participants
- **Benoît** (utilisateur avec navigateur très chargé)
- **Renate** (développeuse en stage sur la passerelle SIP)
- **Mickaël** (responsable produit SIP Media Gateway)
- **Benjamin** (coordinateur technique)
- **[Auteur du compte rendu]** (responsable de l’investigation WebDAV)
- Membres de l’équipe **messagerie** (support juridique & financement)

---

## Objet de la réunion
1. **Investigation** du problème de stabilité des connexions entre **B3desk** et le service **Nuage** (Nextcloud) via WebDAV et le token applicatif.
2. **Validation du devis** et du budget associés au projet, ainsi que le lancement du **salon silencieux**.
3. **État d’avancement** du projet **SIP Media Gateway** (intégration d’un connecteur SIP à BBB) et besoins de développement supplémentaires.

---

## Sujets abordés

| N° | Thème | Points clés |
|---|-------|-------------|
| 1 | **Cinématique du token** | - Le token (validité 30 jours) est obtenu une fois, puis toutes les requêtes passent directement sur Nuage, sans passer par le portail Apps.<br>- La connexion B3desk ↔︎ Nuage est parfois lente ou instable. |
| 2 | **Causes possibles d’instabilité** | - Surcharge du serveur Nuage lors des requêtes WebDAV.<br>- Bibliothèque Python WebDAV potentiellement obsolète.<br>- Versions de Nextcloud (montées de version récentes) qui pourraient impacter le comportement. |
| 3 | **Plan de tests** | - Reproduire le problème en conditions réelles (captures de trafic, mesure des temps de réponse).<br>- Tester avec différents navigateurs (notamment celui de Benoît, très chargé de plugins).<br>- Vérifier la bibliothèque Python et envisager une mise à jour. |
| 4 | **Validation du devis & budget** | - Le devis a été validé par l’équipe messagerie ; aucun obstacle juridique.<br>- Le budget 2025 est disponible.<br>- Le salon silencieux peut donc être lancé immédiatement. |
| 5 | **Projet SIP Media Gateway** | - Financement prévu par **BGFI**.<br>- Nécessité de développer des fonctions liées à la **CIP** (ex. gestion des flux SIP).<br>- Renate travaille sur le développement de la passerelle ; les exigences supplémentaires devront être discutées. |
| 6 | **Coordination & prochaines étapes** | - Besoin d’une réunion dédiée avec Mickaël et Benjamin pour cadrer l’offre actuelle et les évolutions possibles.<br>- Suivi des retours de Benoît avant de poursuivre les investigations. |

---

## Décisions prises
- **Début du salon silencieux** : le projet passe en phase de travail dès maintenant.
- **Reproduction du problème** : priorité à la capture de la cinématique exacte lorsqu’une défaillance survient.
- **Token** : on garde la durée de 30 jours pour le moment ; une éventuelle extension sera étudiée plus tard.
- **Financement** du projet SIP Media Gateway confirmé par BGFI.
- **Réunion de cadrage** à organiser (Mickaël + Benjamin) pour définir l’offre actuelle et les développements futurs.

---

## Questions en suspens
1. **Origine précise** de l’instabilité : surcharge serveur, bibliothèque Python, ou version de Nextcloud ?
2. **Retours de Benoît** sur les tests avec son navigateur ; quelles anomalies observe‑t‑il ?
3. **Besoin de financement** supplémentaire pour les fonctionnalités CIP non couvertes par la brique existante.
4. **Validation finale** du budget 2025 (date et modalités).
5. **Détails juridiques** du support à mettre en place (bien que le devis soit validé, le suivi juridique reste à confirmer).

---

## Tâches à effectuer

| Action | Responsable | Échéance (provisoire) |
|--------|-------------|----------------------|
| Reproduire le problème de connexion et capturer la cinématique (trafic, temps de réponse). | **[Auteur du compte rendu]** | 1 semaine |
| Effectuer des tests complémentaires sur différents navigateurs et versions de Nextcloud. | **[Auteur]** | 2 semaines |
| Vérifier l’état de la bibliothèque Python WebDAV et préparer une mise à jour si nécessaire. | **[Auteur]** | 2 semaines |
| Collecter les retours de Benoît et les intégrer aux analyses. | **[Auteur]** | Dès réception |
| Transmettre le devis validé au service juridique pour archivage et suivi. | **Équipe messagerie / Benoît** | 3 jours |
| Évaluer la possibilité d’allonger la durée du token (au‑delà de 30 jours) pour la mise en production. | **Équipe B3desk** | 1 mois |
| Organiser une réunion de cadrage avec Mickaël et Benjamin (définir l’offre SIP Media Gateway). | **Mickaël** | À planifier (dans les 10 jours) |
| Préparer le plan de financement des développements CIP supplémentaires (si besoin). | **Renate + Responsable produit** | À définir |
| Communiquer l’avancement global aux parties prenantes (rapport hebdomadaire). | **[Auteur]** | Hebdomadaire |

---

## Prochaine rencontre
- **Réunion de suivi** : à programmer dès que Benoît aura fourni ses retours, idéalement **dans la semaine suivante**.
- **Réunion de cadrage SIP Media Gateway** : à fixer avec Mickaël et Benjamin (proposition : **dans 10 jours**).

---

*Le présent compte rendu résume les points essentiels de la discussion et les actions à mener. Merci à tous pour votre participation.*
