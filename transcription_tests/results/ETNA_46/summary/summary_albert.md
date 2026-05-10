# Compte‑rendu de la 46ᵉ réunion d’équipe
*Date :* 28 avril 2026
*Heure :* 09 h – 12 h (environ 3 h)
*Lieu :* Distanciel (Teams)

---

## Participants
| Nom | Fonction / Rôle |
|-----|-----------------|
| **Didier** | Responsable de programme |
| **Hugo** | Chef de projet – Portail Apps |
| **Benoît** | Responsable technique – Tribu & Nuage |
| **Audran** | Responsable domaine (comité de domaine) |
| **Simon** | Animateur du comité Squash |
| **Frédéric** | Responsable référents régionaux |
| **Nicolas** | Responsable support & formation |
| **Maxime Leherici** | Responsable support éditeur Nextcloud |
| **Johan** | Responsable suivi licences IES Microsoft |
| **Valérie** | Gestion des commandes de développement |
| **Autres** (participants ponctuels) : Frédéric Cognès, Paul Fouad, etc.

---

## Objet de la réunion
Faire le point sur l’avancement des projets du **programme DLE** (budget, planning, livrables) et sur les actions opérationnelles en cours :
- Suivi des jalons et amélioration de la visibilité des dates de mise en production.
- Points d’avancement des projets **Tribu**, **Nuage**, **BGB**, **DBV**, **VisioAgent**, **Portail Apps**, **Tube**, etc.
- Gestion des incidents et des dépendances avec les prestataires/éditeurs.

---

## Durée estimée
Environ **3 h** (début 09 h, fin 12 h).

---

## Sujets abordés

| Thème | Points clés |
|-------|-------------|
| **1️⃣ Réduction du budget DLE** | - Décision du comité de domaine (avec Audran) de réduire le budget global. <br>- Confirmation des montants en attente, impact « indolore » sur la plupart des projets, mais vigilance sur les éventuels « coup de rabot ». |
| **2️⃣ Besoin de dates de livraison précises** | - Audran souhaite des jalons plus fiables (ex. : septembre/octobre). <br>- Actuellement, on ne peut fournir que des fourchettes (« avant l’été », « après l’été »). <br>- Nécessité d’améliorer la gouvernance avec les prestataires (Collabora, Nextcloud, BVB, etc.). |
| **3️⃣ Problème de version Nextcloud 31** | - Régression fonctionnelle (partage de fichiers) non‑communicée. <br>- Impossible de livrer la version 31 en production tant que le correctif n’est pas disponible. <br>- Action : contacter Maxime Leherici pour obtenir une version parallèle ou un correctif urgent. |
| **4️⃣ Licences IES Microsoft** | - Renouvellement effectué la semaine précédente pour 30 000 agents. |
| **5️⃣ Comité des référents** | - Réunion prévue **mardi prochain** (distanciel). <br>- Slides à préparer et diffuser d’ici la fin de semaine. |
| **6️⃣ BNA – campagne d’enquête** | - Décalage d’un mois : nouvelle date de lancement **27‑28 juin** (au lieu du 16 juin) pour éviter le chevauchement avec la DELCOM. |
| **7️⃣ Communication unifiée** | - Étude des outils (Cisco, Webex, solutions libres). <br>- Décision à prendre sur l’outil « privé » vs « libre ». |
| **8️⃣ Projet Tribu – Refonte graphique (UX8)** | - Chiffrage en cours, 3 lots (accueil / tableaux de bord / dossiers – ~80 j, outils / recherche, administration). <br>- Objectif MEP **fin novembre / début décembre** (date précise à confirmer). <br>- Environ **200 j** de travail au total. |
| **9️⃣ Intégration DBV dans Cap Education** | - Validation du développement, démarrage imminent avec l’éditeur. |
| **🔟 VisioAgent** | - Validation du frontal, ajout d’un bandeau d’information, gestion des favoris. <br>- Développement de plugins (ex. : sélection aléatoire d’un participant). |
| **1️⃣1️⃣ Portail Apps** | - 221 000 comptes créés, 80 000 vidéos hébergées. <br>- Installation de **Matomo** pour le suivi analytique. <br>- Raccourcisseur d’URL en cours de développement (démo attendue la semaine prochaine). |
| **1️⃣2️⃣ Rancher (pré‑prod)** | - Livré mais non fonctionnel à ce jour. <br>- Besoin d’une documentation claire et d’un support pour le déploiement d’applications. |
| **1️⃣3️⃣ Tube (vidéothèque)** | - Thématisation des instances (travaux avec la DRAME du Grand Est). <br>- Transcription vidéo opérationnelle en test, déploiement prévu sur tous les serveurs. <br>- Plugin de gestion de durée de vie des vidéos (développement chez Pramasoft). |
| **1️⃣4️⃣ Wi‑Fi académies** | - Questionnaire envoyé aux académies d’Île‑de‑France, en attente de réponses. |
| **1️⃣5️⃣ Accompagnement terrain** | - Nécessité d’améliorer le support de proximité (VIP, académies, déploiements). |
| **Divers** | - Point rapide sur les incidents en cours (pré‑prod, déploiement d’applications, etc.). |

---

## Décisions prises

| Décision | Responsable | Délai |
|----------|--------------|-------|
| **Réduction du budget DLE** validée par le comité de domaine. | – | Immédiat |
| **Améliorer la précision des dates de livraison** – mettre en place un tableau de suivi partagé avec les prestataires. | **Audran** (pilotage) + **Benoît** (technique) | 1 semaine |
| **Reporter la campagne BNA** du 16 juin au **27‑28 juin**. | **Benoît** (coordination) | 27 juin |
| **Ne pas interrompre le service Tribu** lors de la mise à jour ; déploiement transparent. | **Benoît** | Avant la MEP (nov‑déc) |
| **Valider l’intégration DBV** dans Cap Education et lancer le développement. | **Frédéric Cognès** + **Valérie** (commande) | Début mai |
| **Organiser le Squash Tribu** avec Simon. | **Simon** | Avant le prochain comité (date à fixer) |
| **Préparer les slides du comité référent** et les diffuser. | **Frédéric** | Fin de semaine |
| **Contacter Maxime Leherici** pour obtenir une version parallèle de Nextcloud 31 ou le correctif de partage. | **Benoît** | ASAP (avant fin mai) |
| **Déployer le raccourcisseur d’URL** du Portail Apps et préparer une démo. | **Hugo** | Semaine prochaine |
| **Finaliser le thème des instances Tube** (travail avec la DRAME du Grand Est). | **Hugo** + **Manon** | Rentrée prochaine (septembre) |
| **Mettre en place la transcription vidéo** sur tous les serveurs Tube. | **Nicolas** | Juin 2026 |

---

## Questions en suspens

| Question | Responsable(s) | Commentaire |
|----------|----------------|-------------|
| **Quand pourra‑t‑on communiquer une date précise pour la version 3.1 de DBV ?** | **Benoît**, **Maxime Leherici** | Dépend du correctif Nextcloud. |
| **Quel outil de communication unifiée choisir (Cisco, Webex, solution libre) ?** | **Paul Fouad**, **Direction IT** | Décision attendue après étude de besoins. |
| **Comment structurer les contrats avec les éditeurs : paiement direct → exigences de dates ?** | **Didier**, **Direction financière** | À définir dans la prochaine revue budgétaire. |
| **Quel est le périmètre exact du plugin de délégation de salles (VisioAgent) ?** | **Benoît**, **YAL** | En cours d’analyse, décision à la prochaine réunion. |
| **Quand le Rancher sera‑t‑il opérationnel en pré‑prod ?** | **Equipe infra** | Besoin d’une documentation et d’un support éditeur. |
| **Résolution du problème de latence sur les bornes Wi‑Fi** | **Équipe réseau** | En attente des retours du questionnaire. |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Mettre à jour le tableau de suivi des jalons (dates, livrables). | **Audran** + **Benoît** | 05 mai 2026 |
| Contacter Maxime Leherici pour le correctif Nextcloud 31. | **Benoît** | 02 mai 2026 |
| Préparer et envoyer les slides du comité référent. | **Frédéric** | 31 mai 2026 |
| Organiser le Squash Tribu (date, agenda). | **Simon** | 10 mai 2026 |
| Finaliser le chiffrage de la refonte Tribu et valider le planning de développement. | **Benoît** | 15 mai 2026 |
| Déployer le raccourcisseur d’URL et préparer la démonstration. | **Hugo** | 07 mai 2026 |
| Lancer la migration BNA (nouvelle date). | **Benoît** | 27 juin 2026 |
| Mettre en place la transcription vidéo sur les serveurs Tube. | **Nicolas** | 30 juin 2026 |
| Récolter les réponses du questionnaire Wi‑Fi et analyser les résultats. | **Équipe réseau** | 15 mai 2026 |
| Suivi des incidents en pré‑prod (tickets Omniface, etc.). | **Nicolas** | En continu |

---

## Prochaine rencontre

| Date | Objet | Lieu |
|------|-------|------|
| **Mardi 9 mai 2026** | Réunion du **comité des référents** (préparation du déploiement, suivi des jalons) | Distanciel (Teams) |
| **À définir** | Point d’avancement **Tribu** (début du développement) | Distanciel / présentiel selon disponibilité |

---

*Le présent compte‑rendu a été rédigé par l’assistant de réunion et diffusé à tous les participants.*
