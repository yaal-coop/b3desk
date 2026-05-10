# Compte‑rendu de la réunion du 46ᵉ comité DNE
*Date :* 28 avril 2026 – *Durée estimée :* ≈ 2 h

---

## 1️⃣ Participants

| Nom | Fonction / Rôle (si connu) |
|-----|-----------------------------|
| **Didier** | Animateur de la réunion |
| **Hugo** | Responsable projets (Tribu, Wi‑Fi, etc.) |
| **Benoît** | Responsable technique / suivi des prestataires |
| **Audran** | Responsable du comité de domaine |
| **Frédéric** | Responsable intégration DBV / CapEducation |
| **Nicolas** | Responsable nuage & licences Microsoft |
| **Simon** | Responsable du comité Squash |
| **Johan** | Responsable support & coordination |
| **Samir** | Responsable support technique |
| **Aurélien** | Responsable déploiement terminaux |
| **Valérie** | Validation des commandes de développement |
| **Maxime Leherici** | Contact éditeur Nextcloud |
| **Autres** (participants ponctuels) : Jean‑Claude, François, Sophie, etc.

---

## 2️⃣ Objet de la réunion

- Faire le point sur l’avancement des projets DNE (budget, planning, livrables).
- Identifier les blocages liés aux prestataires (Nextcloud, Collaborat, etc.).
- Définir les actions à mettre en place pour améliorer la visibilité des jalons et la maîtrise des livraisons.
- Préparer les prochains comités (Squash, référents ATNA) et les livrables associés.

---

## 3️⃣ Sujets abordés

| Thème | Points clés |
|-------|-------------|
| **Budget DNE** | - Réduction globale du budget annoncée par la DNE. <br> - En attente de confirmation des montants impactés sur les projets. |
| **Planification & visibilité** | - Besoin d’une meilleure précision sur les dates de mise en production (ex. : version 3.1, version 31 de Nextcloud). <br> - Risque de « date‑promesse » non tenue → perte de confiance. |
| **Prestataires / éditeurs** | - **Nextcloud** : régression fonctionnelle dans la version 31, mise à jour reportée. <br> - **Collaborat** : livraisons irrégulières, besoin d’un engagement plus réaliste. <br> - **BBB**, **Bitesize Network**, **Renater** : suivi des évolutions et des correctifs. |
| **Renouvellement licences Microsoft** | - Licences IES renouvelées l’an passé pour 30 k agents / 50 k postes. |
| **Comité Squash** | - Organisation d’un atelier avec **Simon** (date à fixer). |
| **Comité des référents ATNA** | - Réunion prévue **mardi prochain** ; slides à préparer (envoi imminent). |
| **Projet Tribu – refonte UX/UI** | - Chiffrage en cours (3 lots, ≈ 200 j‑h). <br> - Objectif MEP fin novembre / début décembre 2025. |
| **Campagne BNA** | - Décalage du lancement du 16 juin au **27‑28 juin** (conflit avec enquête DELCOM). |
| **Communication unifiée** | - Étude d’outils (Cisco, Webex, solutions libres). <br> - Besoin d’une décision sur l’outil « privé » vs « libre ». |
| **Nuage / Nextcloud** | - Version 30 en prod, version 31 disponible mais non testée. <br> - Problème de liens internes → impact sur le déploiement de *Global Scale*. |
| **RAM serveur PostgreSQL** | - +4 Go obtenus via l’atelier Optimus Green (passage de 8 Go à 12 Go). |
| **Portail Apps** | - 221 k comptes, 73 k actifs sur 5 mois. <br> - Installation de Matomo pour analytics. |
| **Wi‑Fi académies** | - Questionnaire envoyé aux académies d’Île‑de‑France, en attente de réponses. |
| **Messagerie (Thunderbird / Webmail)** | - Analyse des usages, besoin d’accompagnement au changement. |
| **Autres projets** | - Intégration DBV dans CapEducation (validée). <br> - VidéoAgent 1.3 (tri des salons, favoris). <br> - Plugin « sélection aléatoire » pour VNB. |

---

## 4️⃣ Décisions prises

| Décision | Responsable | Délai |
|----------|-------------|-------|
| **Reporter la campagne BNA** du 16 juin au **27‑28 juin**. | Benoît / équipe communication | 28 juin |
| **Valider l’intégration DBV** dans CapEducation et lancer le développement. | Frédéric & Benoît | Début mai |
| **Préparer les slides** pour le comité des référents ATNA (infos à partager). | Nicolas (en charge de la diffusion) | Avant le comité (mardi prochain) |
| **Planifier le workshop Squash** avec Simon. | Simon | À fixer (prochaine semaine) |
| **Mettre à jour la RAM PostgreSQL** à 12 Go (déjà effectué). | Équipe infra / Optimus Green | Effectué |
| **Déclencher le chiffrage final** de la refonte Tribu dès validation du budget. | Hugo / équipe dev | Avant fin mai |
| **Reporter la mise à jour Nextcloud 31** jusqu’à obtention du correctif de partage. | Benoît (coordination avec Maxime Leherici) | Juin 2026 (date précise à confirmer) |

---

## 5️⃣ Questions en suspens

| Question | Responsable(s) | Commentaire |
|----------|----------------|-------------|
| **Montants exacts de la réduction budgétaire** et impact sur chaque projet. | Didier / Audran | En attente de confirmation officielle. |
| **Date de livraison précise** de la version 3.1 (BBB) et de la version 31 (Nextcloud). | Benoît / Maxime Leherici | Nécessite validation du prestataire. |
| **Road‑map détaillée** des éditeurs (Collaborat, Nextcloud, BBB). | Audran / équipe projets | À obtenir pour améliorer la visibilité. |
| **Choix final de l’outil de communication unifiée** (Cisco, Webex, solution libre). | Hugo / comité décision | Décision attendue avant le prochain trimestre. |
| **Statut du script de migration** Nextcloud académique → centralisé (Nantes). | Benoît / Irina (Pôle Paris) | Correctif attendu « ce week‑end ». |
| **Déploiement du plugin Thunderbird** (compatibilité, authentification). | Nicolas / pôle identité | Étude en cours, décision avant le déploiement de la prochaine version. |
| **Réponse des académies** au questionnaire Wi‑Fi. | Hugo | Suivi à faire dès réception des réponses. |

---

## 6️⃣ Tâches à effectuer

| Action | Responsable | Échéance |
|--------|-------------|----------|
| Obtenir la confirmation des montants de la réduction budgétaire. | **Didier** (avec Audran) | 15 mai 2026 |
| Produire et diffuser les **slides du comité référents ATNA**. | **Nicolas** | Avant le mardi prochain |
| **Planifier** le workshop Squash avec Simon (date, agenda). | **Simon** | 5 mai 2026 |
| **Finaliser le chiffrage** de la refonte Tribu et valider le planning de développement. | **Hugo** + **Équipe dev** | 31 mai 2026 |
| **Suivre** le correctif du partage de fichiers sur Nextcloud 31 et valider le test en pré‑prod. | **Benoît** (avec Maxime Leherici) | Fin mai 2026 |
| **Mettre à jour** la RAM des serveurs frontaux Nextcloud (+4 Go) et monitorer la stabilité. | **Équipe infra** | 1 juin 2026 |
| **Envoyer** le questionnaire Wi‑Fi aux académies d’Île‑de‑France et compiler les réponses. | **Hugo** | 10 mai 2026 |
| **Valider** la feuille de route des plugins VNB (sélection aléatoire, etc.) et lancer les développements. | **Nicolas** + **Équipe VNB** | 30 mai 2026 |
| **Préparer** le plan de communication pour la migration BNA (27‑28 juin). | **Benoît** / **Équipe com** | 20 juin 2026 |
| **Faire le point** sur le statut du projet *Portail Apps* (analytics, nouvelles fonctionnalités). | **Aurélien** | 15 mai 2026 |

---

## 7️⃣ Prochaine rencontre

- **Réunion du comité des référents ATNA** – **Mardi 2 mai 2026** (en distanciel).
- **Workshop Squash** – date à confirmer (prévu la semaine suivante).
- **Suivi général** – prochaine réunion de suivi DNE prévue **fin mai 2026** (date exacte à définir).

---

*Le présent compte‑rendu sera diffusé à l’ensemble des participants et archivé dans le répertoire partagé du comité DNE.*
