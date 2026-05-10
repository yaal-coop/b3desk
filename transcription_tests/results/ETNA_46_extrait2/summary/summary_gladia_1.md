# Compte rendu de réunion
**Date** : avant les vacances d’été 2024 (transcription réalisée fin juin)
**Durée estimée** : ~1 h 30 (pas indiqué explicitement, estimation basée sur le volume d’échanges)

---

## Participants
| Nom / Rôle | Fonction |
|------------|----------|
| **Hugo** | Chef de projet / coordinateur technique |
| **Manon** | Chargée de suivi fonctionnel (tubes) |
| **Nicolas** | Responsable infrastructure / déploiement |
| **Développeurs** (2) | Équipe de développement du portail Apps |
| **Équipe Dijon** | Développeurs rencontrés sur site |
| **Représentants Framasoft** | Partenaire externe pour les plugins |
| **DRAP Grand Est** | Responsable thématique des tubes |
| **Autres** (ex. exploitants, experts certificats) | Non nommés spécifiquement |

---

## Objet de la réunion
Faire le point d’avancement sur :

1. Le portail **Apps** (statistiques, version 6.4.1, Matomo).
2. Le **raccourcisseur d’URL / QR‑code** (développement, mise à jour).
3. L’architecture **micro‑applications** et le cycle de vie des comptes.
4. La plateforme **Rancher** (pré‑prod, certificats).
5. La refonte graphique **Thèmes des tubes**.
6. La **transcription vidéo** (déploiement, externalisation).
7. Priorités de sécurité (**Asset 1.1**) et répartition des développements avec **Framasoft**.

---

## Sujets abordés & décisions prises

| Sujet | Points clés | Décisions / orientations |
|-------|-------------|--------------------------|
| **Statistiques du portail Apps** | 81 k vidéos, 221 k comptes (hors comptes directs), 73 k ré‑activations depuis déc. | Continuer le suivi via Matomo (installé depuis 3 semaines). |
| **Version 6.4.1** | Mise en prod récente, petites améliorations (cycle de vie, raccourci URL). | Aucun changement majeur à prévoir. |
| **Raccourcisseur d’URL** | Deux devs travaillent, échange fructueux avec l’équipe de Dijon, démo attendue. | - Démo prévue **semaine prochaine**.<br>- Mise à jour prévue **juillet / mi‑juillet** (mise à jour des examens). |
| **Architecture micro‑applications** | Passage à un modèle où le portail appelle des micro‑apps sécurisées via token. | Poursuivre le développement ; la version « franchiseur » livrée il y a 2 semaines mais pas encore fonctionnelle. |
| **Rancher & certificats** | Demande de clarification sur l’usage en pré‑prod, problème de déploiement (logiciel libre vs exploitant). | - Recherche de solution de déploiement en cours.<br>- Suivi des clarifications sur les certificats. |
| **Thématiques / identité graphique des tubes** | 11 tubes, besoin d’une UI claire. Version 7.1.1 ne supporte plus l’ancien thème. | - Nouvelle approche « thèmes » (masquer les instances) validée.<br>- Implémentation prévue **rentrée prochaine** (3‑4 mois). |
| **Transcription vidéo** | Fonctionnelle en test sur la version 7, besoin de généraliser. | - Déploiement sur tous les serveurs tubes avec **Nicolas**.<br>- Prévoir un deuxième serveur dédié.<br>- Phase suivante : externaliser transcription + transcodage sur deux grosses machines. |
| **Sécurité (Asset 1.1)** | Priorité élevée à cause de failles. | - Déploiement prioritaire dès que possible. |
| **Plugins & partenariat Framasoft** | - Limiter la durée de vie d’une vidéo (ex. suppression automatique).<br>- Gestion des vidéos contenant des mineurs (spécifique ministère). | - **Framasoft** développe le plugin « durée vidéo ».<br>- Plugin « mineurs » sera développé en interne (plugin dédié). |
| **Gestion des devis & marché** | Nécessité de formaliser les achats pour les développements. | - Responsable de la rédaction des devis à désigner (non précisé). |

---

## Questions en suspens

1. **Déploiement complet sur Rancher** – quelles étapes restent ? (responsable non désigné).
2. **Clarification des exigences de certificats** – besoin d’un point avec l’expert sécurité.
3. **Date exacte de mise en production du raccourcisseur** – dépend de la démo de la semaine prochaine.
4. **Calendrier détaillé de la refonte des thèmes tubes** – confirmation du planning à la rentrée.
5. **Finalisation du devis pour les plugins** – qui pilote la procédure d’appel d’offres ?

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| **Démo du raccourcisseur d’URL** | Hugo | Semaine prochaine |
| **Finaliser le raccourcisseur** (intégration, tests) | Deux développeurs (équipe Dijon) | Fin juillet / début août |
| **Déployer la transcription sur tous les serveurs tubes** | Nicolas + équipe infra | Dès que le serveur secondaire sera prêt (prévu Q3) |
| **Mettre en place l’infrastructure de transcodage externalisée** | Nicolas (coordination) | Après déploiement transcription |
| **Livrer la version fonctionnelle du micro‑service « franchiseur »** | Équipe dev micro‑apps | Prochaine itération (début septembre) |
| **Clarifier l’usage de Rancher et résoudre le problème de déploiement** | Responsable infra (non nommé) | ASAP |
| **Finaliser le design des thèmes tubes** | Manon + DRAP Grand Est + Hugo | Rentrée (septembre) |
| **Développer le plugin durée vidéo** | Framasoft | Selon leur planning (début Q4) |
| **Développer le plugin gestion mineurs** | Équipe interne (développeurs) | Q4 2024 |
| **Rédiger et valider les devis pour les plugins** | (à désigner) | Avant fin août |
| **Suivi des certificats et mise à jour de la documentation** | (à désigner) | En cours |

---

## Prochaine rencontre

Aucun créneau fixé pendant la réunion.
**Proposition** : planifier une nouvelle réunion de suivi **le 15 septembre 2024** (ou à la rentrée) afin de :

* Valider la mise en production du raccourcisseur.
* Faire le point sur le déploiement Rancher et les certificats.
* Vérifier l’avancement des thèmes tubes et de la transcription.

---

*Rédigé par l’assistant spécialisé en comptes rendus.*
