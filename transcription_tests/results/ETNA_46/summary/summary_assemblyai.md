# Compte‑rendu du 46ᵉ Comité de suivi projets DNE
**Date** : 28 avril 2026
**Durée estimée** : ~ 2 h 30 (déroulement continu du pointage des projets)

---

## Participants
| Nom | Fonction / Rôle |
|-----|-----------------|
| **Olivier** | Responsable de domaine |
| **Hugo** | Chef de projet |
| **Benoît** | Responsable technique |
| **Audran** | Responsable du suivi fonctionnel |
| **Simon** | Animateur du comité référent |
| **Frédéric** | Responsable intégration PGV / VisioAgent |
| **Nicolas** | Responsable infrastructure / support Nextcloud |
| **Maxime** | Responsable éditeur Nextcloud |
| **Johan** | Responsable déploiement & mise en prod |
| **Samir** | Responsable BV (terminaux) |
| **Aurélien** | Support pré‑production |
| **Valérie** | Validation des commandes de développement |
| **Autres** | Participants ponctuels (ex. : Renater, Apple Quad, etc.) |

---

## Objet de la réunion
Faire le point sur l’avancement des projets DNE, identifier les blocages (budget, planning, fournisseurs) et définir les actions correctives à mettre en œuvre avant les prochains jalons (septembre / octobre 2026).

---

## Sujets abordés

| Thème | Points clés |
|-------|-------------|
| **1. Budget DNE** | - Réduction globale du budget confirmée (montants en attente). <br>- Impact limité sur les projets en cours, mais vigilance requise. |
| **2. Visibilité des livraisons** | - Nécessité d’établir des dates précises (sep/oct) pour les nouvelles fonctionnalités. <br>- Difficulté à obtenir des engagements fermes de la part des prestataires (Collabora, Nextcloud, Megzot). |
| **3. Relations avec les prestataires** | - Collabora : livraisons irrégulières, manque de planning fiable. <br>- Nextcloud : version 31 sortie avec régression fonctionnelle (partage de fichiers). <br>- Megzot : même problème de visibilité. |
| **4. Nextcloud – version 31** | - Régression partagée non résolue, mise en production impossible sans correctif. <br>- Décision de reporter le déploiement au **mois prochain** après validation du correctif. |
| **5. BMA (enquête)** | - Décalage du lancement du **16 juin** au **27‑28 juin** pour éviter chevauchement avec enquête BELCOM. |
| **6. Support adaptateur** | - Mise à jour en cours, besoin d’un plan de montée en compétences des équipes académiques. |
| **7. Conformité poste de travail** | - Audit BDD : +4 Go de RAM sur chaque serveur (passage de 8 → 12 Go). <br>- Suivi de la stabilité post‑augmentation. |
| **8. Intégration PGV & VisioAgent** | - Validation de la commande PGV (déploiement imminent). <br>- VisioAgent intégré à Tchap/BVB, fonctionnel. |
| **9. Tribu – refonte graphique (UX8)** | - Chiffrage finalisé (≈ 200 jv). <br>- Découpage en 3 lots (accueil, recherche, admin). <br>- Début du développement prévu **mai** après validation du chiffrage. <br>- Environnements pré‑prod, prod et AQT créés. |
| **10. Portail Apps** | - 221 000 comptes créés, 73 000 actifs depuis déc. <br>- Statistiques détaillées disponibles (parcours, terminaux). |
| **11. Raccourcisseur d’URL** | - Développement en cours (API, QR‑code). <br>- Démo attendue la semaine prochaine. |
| **12. Architecture micro‑services (cycle de vie)** | - Implémentation d’une micro‑application par tube pour gestion des comptes, vidéos, etc. |
| **13. Rancher** | - Livraison du composant, mais déploiement d’applications toujours bloqué (documentation). |
| **14. Tube – thématisation & conformité** | - Refonte graphique retardée (support 7.1.1). <br>- Travail sur thématiques plutôt que “instances”. <br>- Transcription vidéo opérationnelle en test, déploiement prévu. |
| **15. Déploiements académiques** | - Pilotes (Nantes, Poitiers, Tacan) en cours, plan d’accélération pour Île‑de‑France (oct‑nov). <br>- Retour d’expérience sur la messagerie (migration, accompagnement). |
| **16. Divers** | - Point sur les bornes Wi‑Fi (questionnaire en cours). <br>- Mise à jour CPT prévue pendant les vacances d’été. <br>- Suivi des incidents BV (regroupement, déploiement d’applications). |

---

## Décisions prises

| Décision | Responsable | Échéance |
|----------|-------------|----------|
| **Valider la réduction budgétaire** | Olivier | Immédiate (montants à confirmer) |
| **Élaborer un planning détaillé (sep/oct) pour les livraisons** | Audran + équipe planning | 15 mai 2026 |
| **Reporter le déploiement de Nextcloud 31** | Nicolas + Maxime | Déploiement différé au **mois prochain** (post‑correctif) |
| **Décaler la campagne BMA** | Benoît | 27‑28 juin 2026 |
| **Lancer le chiffrage définitif de la refonte Tribu** | Hugo + prestataires | Fin mai 2026 |
| **Valider la commande PGV et le lancement VisioAgent** | Frédéric | Dès réception du bon de commande (déjà validé) |
| **Augmenter la RAM des serveurs BDD** | équipe infra (Nicolas) | Déjà effectué, suivi continu |
| **Préparer les slides du comité référent** | Simon | Envoi d’ici **5 mai 2026** |
| **Plan de formation support adaptateur** | Benoît | Élaboration d’ici **15 mai 2026** |
| **Déployer le raccourcisseur d’URL** | Hugo (développeurs) | Démo prévue **semaine prochaine** |
| **Finaliser la migration des académies pilotes** | Johan + équipes locales | Fin 2026 (plan détaillé à valider) |

---

## Questions en suspens

| Question | Responsable(s) | Suivi |
|----------|----------------|-------|
| Quels sont les montants exacts de la réduction budgétaire ? | Olivier | Attente des confirmations financières |
| Quand le correctif de partage de fichiers de Nextcloud 31 sera‑t‑il disponible ? | Nicolas / Maxime | Ticket ouvert, mise à jour attendue d’ici fin mai |
| Quels développements sont financés vs non financés chez les éditeurs ? | Audran | Nécessité d’un tableau de suivi des financements |
| Comment garantir la stabilité de la RAM après l’augmentation ? | Nicolas | Monitoring continu, alerte en cas de plantage |
| Validation du plugin “délégation de salles” (BBB) – priorisation ? | Yann + Frédéric | Décision à prendre lors du prochain comité de pilotage |
| Déploiement du Rancher – quelles sont les dépendances manquantes ? | équipe infra | Analyse en cours, plan d’action à définir |

---

## Tâches à effectuer (avec responsable)

| Action | Responsable | Date limite |
|--------|-------------|-------------|
| Transmettre les montants définitifs de la réduction budgétaire | **Olivier** | 10 mai 2026 |
| Produire le planning détaillé (sep/oct) des livraisons fonctionnelles | **Audran** + **Chef de projet** | 15 mai 2026 |
| Envoyer les slides du comité référent aux participants | **Simon** | 5 mai 2026 |
| Tester le correctif de partage de fichiers de Nextcloud 31 et valider le déploiement | **Nicolas** (avec **Maxime**) | Fin mai 2026 |
| Lancer le développement de la refonte Tribu (lot 1) | **Hugo** + prestataires | Début juin 2026 |
| Mettre en place le plan de formation “support adaptateur” | **Benoît** | 15 mai 2026 |
| Suivre la consommation RAM et préparer un rollback si nécessaire | **Nicolas** | Surveillance continue, alerte dès dépassement |
| Organiser la démonstration du raccourcisseur d’URL | **Hugo** | Semaine prochaine |
| Finaliser le script de migration Nextcloud académique → centralisé | **Benoît** | Avant fin mai 2026 |
| Préparer le questionnaire de retour d’expérience Wi‑Fi et le diffuser | **Équipe Wi‑Fi** | 30 mai 2026 |
| Planifier la mise à jour CPT (minimiser les interruptions) | **Johan** | Avant les vacances d’été (début juillet) |

---

## Prochaine rencontre

- **Date** : **Mardi 9 mai 2026** (Comité référent) – en distanciel.
- **Ordre du jour prévisionnel** :
  1. Validation du planning de livraisons (sep/oct).
  2. Point sur le correctif Nextcloud 31.
  3. Avancement de la refonte Tribu.
  4. Suivi des actions de formation support adaptateur.
  5. Retour sur le questionnaire Wi‑Fi.

---

*Fin du compte‑rendu.*
