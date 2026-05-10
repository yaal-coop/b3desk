# Compte rendu de réunion

**Date** : 4 mai 2026
**Heure** : non précisée (réunion d’environ 1 h)
**Durée estimée** : non indiquée

---

## Participants
- **Johan** (animateur)
- **Bastien**
- **Benjamin**
- **Benoît**
- **Mickaël**
- **Autres** (participants non nommés explicitement mais présents dans les échanges)

---

## Objet de la réunion
- Mettre en place un point de suivi bi‑hebdomadaire.
- Faire le point sur les développements récents (code unique, configuration BBB/ScaleLight, migrations, tickets).
- Discuter des incidents et des investigations en cours (Nextcloud/Nuage, erreur 500).
- Valider les prochains livrables (release 1.3, salon silencieux, projet SIP Media Gateway).
- Organiser la planification et l’estimation du backlog.

---

## Sujets abordés & décisions prises

| # | Sujet | Décision / Action principale |
|---|-------|------------------------------|
| 1 | **Rythme des réunions** | Réunion toutes les 2 semaines, le **mercredi à 11 h 30**. Johan enverra les invitations. |
| 2 | **Livraison du « code unique »** | - Préciser dans la PR la modification de configuration (paramètre ScaleLight). <br> - Cette info sera ajoutée à l’APR et à la prochaine release. |
| 3 | **Scénario de test B3Desk / B3D** | Benjamin doit fournir un scénario de test détaillé. |
| 4 | **Configuration BBB Dial Number** | Le numéro de téléphone (Dial Number) sera ajouté à la configuration Métro‑Desk. |
| 5 | **Migrations** | Respecter l’ordre des migrations (tri des salons → migration du code unique). La release devra contenir toutes les migrations dans le bon ordre. |
| 6 | **Ticket 166 – erreur 500** | Problème résolu côté Arawa (suppression d’un champ). La remontée de log sera conservée dans la release. |
| 7 | **Instabilité Nextcloud/Nuage** | - Benjamin reproduira les problèmes de connexion WebDAV.<br> - Vérifier la version des bibliothèques Python utilisées.<br> - Eventuellement allonger la durée de validité du token (30 j → plus). |
| 8 | **Salon silencieux** | Le devis est validé ; le salon peut être lancé dès que les commandes seront passées. |
| 9 | **Budget 2025 & projet SIP Media Gateway** | Budget alloué confirmé. Le projet sera lancé (développement connecteur SIP côté B3Desk). |
|10| **Coordination avec Renater (CIP)** | Une réunion séparée sera organisée pour définir les fonctionnalités possibles et les besoins de financement. |
|11| **Estimation des tâches (tags)** | Mickaël/Benjamin fourniront, d’ici la fin de journée, un tableau de correspondance *tag → estimation (heures/jours)*. |
|12| **Release 1.3** | La release sera réalisée le **jour même à 14 h** (procédure décrite par Sébastien). Benjamin suivra la procédure et demandera de l’aide en cas de souci. |

---

## Questions en suspens
1. **Scénario de test complet** pour le nouveau paramètre B3Desk (BBB Dial Number).
2. **Nom exact de la variable** à modifier dans ScaleLight (confirmé par le développeur).
3. **Intégration du code unique** : sera‑t‑il dans la version 1.3 ou reporté en 1.3.1 ? (à valider avec Benoît).
4. **Cause précise** de l’instabilité WebDAV (surcharge du serveur vs bibliothèque obsolète).
5. **Support juridique** nécessaire pour le devis du salon silencieux (en cours de recherche).
6. **Alignement des développements Renater** avec les exigences de la CIP (réunion à planifier).

---

## Tâches à effectuer

| Action | Responsable | Échéance |
|--------|-------------|----------|
| Envoyer les invitations pour les réunions bi‑hebdomadaires | **Johan** | Immédiate |
| Ajouter la description de la configuration ScaleLight dans la PR | **Bastien** (ou l’auteur de la PR) | Avant la prochaine release |
| Fournir le scénario de test B3Desk (BBB Dial Number) | **Benjamin** | Avant la prochaine réunion |
| Vérifier et garantir l’ordre des migrations dans la release | **Benjamin** | Avant la release 1.3 |
| Conserver la remontée de log du ticket 166 dans la release | Équipe dev | Avant la release 1.3 |
| Reproduire les problèmes de connexion Nuage/Nextcloud et analyser | **Benjamin** | Au plus tard le 10 mai 2026 |
| Mettre à jour les librairies Python WebDAV si besoin | Équipe dev | Avant la prochaine release |
| Envoyer le tableau de correspondance tags → estimation | **Mickaël** (ou **Benjamin**) | Fin de journée (4 mai) |
| Réaliser la release 1.3 (procédure Sébastien) | **Benjamin** (avec l’aide de l’équipe) | 14 h, 4 mai 2026 |
| Lancer le salon silencieux après validation du devis | **Mickaël** / **Benoît** | Dès que les commandes sont passées |
| Préparer le budget 2025 et la commande du projet SIP Media Gateway | **Mickaël** | Avant fin juin 2026 |
| Organiser une réunion avec Renater pour la CIP | **Mickaël** | À planifier (prochaine quinzaine) |

---

## Prochaine rencontre
- **Réunion bi‑hebdomadaire** : mercredi prochain à **11 h 30** (date exacte à confirmer via l’invitation).
- Une réunion supplémentaire sera planifiée pour le **projet SIP Media Gateway** et la **coordination avec Renater** (date à définir).

---

*Fin du compte rendu.*
