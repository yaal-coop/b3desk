# Compte‑rendu de réunion
**Date** : 30 avril 2026
**Durée** : ~ 2 h 30 (prévu 1 h)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Benjamin** | Développeur (tests Nextcloud / Nuage) |
| **Benoît** | Utilisateur avancé (tests navigateur) |
| **Renata** | Développeuse interne CNES West (projets SIP) |
| **Michael** | Contact externe (mentionné) |
| **Speaker / Animateur** | Coordination projet B3DESK |
| **Équipe messager** | Validation du devis |
| **DG FIQ** | Financement du projet SIP Media Gateway |
| Autres (non nommés) | Participants aux discussions budgétaires et techniques |

---

## Objet de la réunion
1. **Analyse des lenteurs / instabilités** entre B3DESK et le service cloud **Nuage (Nextcloud)**.
2. **État d’avancement** du développement de l’API de messagerie nationale.
3. **Validation du devis** et mise en place du « salon silencieux » (commande).
4. **Plan budgétaire 2025** pour le développement de B3DESK.
5. **Projet SIP Media Gateway** (intégration d’un connecteur SIP à BBB) – aspects techniques et financement.

---

## Sujets abordés & décisions prises

| Sujet | Points clés | Décision |
|-------|-------------|----------|
| **1. Investigation Nuage / Nextcloud** | - Le token applicatif (validité 30 j) est obtenu une fois, puis les requêtes WebDAV passent directement par Nuage.<br>- La cinématique (B3DESK → Nuage) est correcte ; le problème semble venir de la connexion WebDAV (latence / instabilité).<br>- Hypothèses : surcharge du serveur Nuage, bibliothèque Python WebDAV obsolète, version de Nextcloud. | - **Action** : poursuivre les tests pour reproduire le dysfonctionnement.<br>- **Report** : la question du token (allonger la durée) sera revu lors d’une prochaine réunion. |
| **2. API messagerie nationale** | - Aucun nouveau retour, projet en stand‑by.<br>- Communication prévue via Tchap dès qu’une relance est nécessaire. | - Aucun changement immédiat ; le projet reste en attente. |
| **3. Devis & salon silencieux** | - Devis transféré à l’équipe messager, conforme aux exigences budgétaires.<br>- Le support juridique reste à identifier, mais le financement est validé. | - **Lancement du salon silencieux** autorisé immédiatement. |
| **4. Budget 2025 B3DESK** | - Un budget dédié pour 2025 doit être alloué au développement B3DESK. | - **Tâche** : sécuriser le vecteur financier (responsable : équipe finance). |
| **5. SIP Media Gateway** | - Projet financé par la DG FIQ.<br>- Nécessité d’adapter les briques existantes (développées par Renata) aux exigences SIP.<br>- Possibilité d’ajouter des fonctionnalités supplémentaires, sous réserve de financement. | - **Prochaine étape** : organiser une réunion technique (Benjamin + Renata) pour définir le périmètre fonctionnel réalisable avec les briques actuelles. |

---

## Questions en suspens
- Quelle est la cause exacte de l’instabilité WebDAV ? (surcharge du serveur Nuage vs bibliothèque Python obsolète).
- La version actuelle de Nextcloud résout‑elle les problèmes observés ?
- Faut‑il augmenter la durée de validité du token applicatif (au‑delà de 30 j) ?
- Quels sont les besoins exacts (spécifications) du client pour le connecteur SIP ?
- Quel sera le support juridique nécessaire pour le salon silencieux ?

---

## Tâches à effectuer

| Action | Responsable | Échéance |
|--------|-------------|----------|
| Reproduire le problème de connexion WebDAV (scénario de latence) | **Benjamin** | Prochaine réunion |
| Effectuer des tests sur le navigateur de Benoît (plugins, configuration) | **Benoît** | ASAP |
| Vérifier que les bibliothèques Python WebDAV utilisées par B3DESK sont à jour | Équipe technique B3DESK | Prochaine réunion |
| Informer le groupe via **Tchap** lorsqu’une relance du projet API messagerie est nécessaire | **Speaker** | Dès réception du besoin |
| Obtenir le support juridique pour le salon silencieux | Équipe juridique / finance | Avant le lancement complet |
| Sécuriser le financement du budget 2025 B3DESK | **Équipe finance** | Q3 2026 |
| Organiser une réunion technique (Benjamin, Renata, etc.) pour cadrer le projet SIP Media Gateway | **Speaker** (organisation) | Dans les 2 semaines |
| Collecter les nouvelles spécifications du client SIP (fonctionnalités attendues) | **Renata** / Contact client | Avant la réunion technique |

---

## Prochaine rencontre
- **Objet** : Suivi des tests Nuage / WebDAV et validation du token, point sur le budget 2025, cadrage du projet SIP Media Gateway.
- **Date proposée** : à définir (idéalement dans les 10 jours suivant la reproduction du problème).
- **Participants attendus** : Benjamin, Benoît, Renata, Speaker, équipe finance, éventuellement Michael.

---

*Fin du compte‑rendu.*
