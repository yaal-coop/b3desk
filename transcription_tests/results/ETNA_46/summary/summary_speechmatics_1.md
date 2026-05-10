# Compte‑rendu de la réunion du Comité de domaine
**Date** : 30 avril 2026
**Durée estimée** : ~ 2 h 30 (demi‑journée)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Didier** | Animateur du comité |
| **Hugo** | Responsable projets (Tribu, URL shortener) |
| **Benoît** | Responsable Nextcloud & suivi prestataires |
| **Audran** | Responsable fonctionnel, suivi des jalons |
| **Nicolas** | Infrastructure & bases de données |
| **Frédéric** | Pilotage volumétrie et profils |
| **Simon** | Coordination squash / expérience Tribu |
| **Maxime** (éditeur Nextcloud) | Support technique Nextcloud |
| **Valérie** | Validation des commandes de développement |
| **Autres** : François, Paul, Manon, etc. (intervenants ponctuels) |

---

## Objet de la réunion
- Faire le point sur l’avancement des projets du domaine (budget, jalons, livrables).
- Identifier les difficultés liées aux prestataires et aux versions logicielles (Nextcloud, Collabora).
- Définir les actions à mener pour améliorer la visibilité des dates de mise en production et la communication avec la direction.

---

## Sujets abordés

| # | Sujet | Points clés |
|---|-------|-------------|
| 1 | **Réduction du budget ADN** | - Baisse du budget confirmée, impact « indolore » sur les projets. <br>- Possibilité d’un « coup de rabot » ponctuel à prévoir. |
| 2 | **Suivi précis des jalons** | - Audran souhaite des dates plus fiables (septembre‑octobre). <br>- Nécessité d’améliorer la coordination avec les prestataires (Nextcloud, Collabora). |
| 3 | **Relation avec les prestataires** | - Manque de visibilité sur les road‑maps des éditeurs. <br>- Besoin d’engagements plus réalistes et de meilleures communications. |
| 4 | **Incident Nextcloud 31** | - Régression fonctionnelle (partage de fichiers) → version non déployable. <br>- Décision de reporter le déploiement jusqu’à validation du correctif (Maxime). |
| 5 | **Renouvellement licences Microsoft** | - Licences 30 000 agents et 50 000 postes renouvelées la semaine dernière. |
| 6 | **Squash & comité référent** | - Organisation d’un squash avec **Simon** (prévu dans ≈ 1 mois). <br>- Comité référent prévu **mardi prochain** (préparation de slides). |
| 7 | **Refonte graphique du projet Tribu (UX‑UI)** | - Chiffrage en cours → 3 lots (80 j, 60 j, 60 j ≈ 200 j). <br>- Objectif MEP fin 2025 (début novembre / début décembre). |
| 8 | **Portail App – statistiques & URL shortener** | - 82 k vidéos, 221 k comptes. <br>- Développement du raccourcisseur d’URL (2 dévs) – mise à jour prévue **1 juillet 12 h**. |
| 9 | **Architecture « micro‑applications »** | - Déploiement d’une couche d’orchestration pour la gestion du cycle de vie des comptes/vidéos. |
|10| **PeerTube – thème & transcription** | - Refonte des thèmes (DRAC Grand Est) – travaux à reprendre **dans 3‑4 mois**. <br>- Transcription vidéo opérationnelle en pré‑prod, généralisation prévue après validation. |
|11| **Wi‑Fi académies** | - Questionnaire envoyé, en attente de réponses. |
|12| **Intégration des « Bébés » (Visio Agent)** | - Validation fonctionnelle, mise en production prévue prochainement. |
|13| **Gateway (RTMP, charge)** | - POC fonctionnel, besoin d’extension de capacité (plus de VM). |
|14| **Divers** | - Mise à jour RAM serveur PostgreSQL (+4 Go) – stabilisation constatée. <br>- Suivi des incidents de pré‑prod (Orléans, Reims). |

---

## Décisions prises
| Décision | Responsable | Délai |
|----------|-------------|-------|
| **Appliquer la réduction budgétaire** | Didier | Immédiat |
| **Améliorer le suivi des jalons** (mise en place d’un tableau partagé) | Audran + Frédéric | 2 semaines |
| **Reporter le déploiement de Nextcloud 31** jusqu’à validation du correctif | Benoît + Maxime | Dès réception du correctif (prévu fin mai) |
| **Déplacer la campagne PNR** du 16 juin au **27‑28 juin** | Responsable communication | 27 juin |
| **Valider le chiffrage de la refonte Tribu** et lancer les développements | Valérie (validation) + Hugo (pilotage) | Fin mai |
| **Mettre en production le raccourcisseur d’URL** | Hugo + équipe dev | 1 juillet 12 h |
| **Planifier le squash Tribu** avec Simon | Simon | Dans ≈ 1 mois |
| **Lancer le comité référent** (préparation slides) | Tous les référents | Mardi prochain |
| **Finaliser l’augmentation RAM** et monitorer la stabilité | Nicolas | Fin mai |
| **Lancer la refonte des thèmes PeerTube** (phase 2) | Manon + Hugo | Q3 2026 |

---

## Questions en suspens
1. **Quand la version Nextcloud 31 sera‑t‑elle stable ?** (Attente du correctif de Maxime).
2. **Dates précises de mise à disposition des nouvelles fonctionnalités** (septembre‑octobre) – dépend du planning des éditeurs.
3. **Déploiement des plugins spécifiques** (ex. sélection aléatoire, gestion des mineurs) – besoin d’un cahier des charges détaillé.
4. **Retour du questionnaire Wi‑Fi** – aucune réponse à ce jour.
5. **Calendrier de la migration des comptes vers le nuage** (post‑migration Nextcloud).

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Créer le tableau de suivi des jalons (incl. dates prévisionnelles) | **Audran** | 2 semaines |
| Communiquer le correctif Nextcloud 31 et planifier le test | **Benoît** + **Maxime** | Fin mai |
| Préparer les slides du comité référent (statistiques, avancement) | **Tous les référents** | Mardi prochain |
| Lancer le développement du raccourcisseur d’URL | **Hugo** (pilotage) + devs | 1 juillet 12 h |
| Valider le chiffrage des 3 lots Tribu et déclencher les commandes | **Valérie** (validation) | Fin mai |
| Mettre à jour la RAM des serveurs PostgreSQL et monitorer | **Nicolas** | Fin mai |
| Organiser le squash Tribu avec Simon | **Simon** | Dans ≈ 1 mois |
| Finaliser le cahier des charges des plugins Bébés & PeerTube | **François** + **Paul** | Q3 2026 |
| Relancer les académies pour le questionnaire Wi‑Fi | **Responsable communication** | 1 semaine |
| Suivi de la migration des licences Microsoft (inventaire) | **Didier** | En cours |

---

## Prochaine rencontre
- **Comité référent** : **Mardi 7 mai 2026** (en présentiel/distanciel – lien à diffuser).
- **Squash Tribu** : prévu **dans 1 mois** (date précise à confirmer par Simon).

---

*Fin du compte‑rendu.*
