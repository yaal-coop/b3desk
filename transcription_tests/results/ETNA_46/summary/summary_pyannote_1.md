# Compte‑rendu de la réunion de suivi projet
*Date :* 30 avril 2026
*Durée estimée :* ~ 1 h 30 (pas indiqué explicitement, durée habituelle)

---

## Participants
- **Audran** (responsable suivi jalons)
- **Benoît** (animation, suivi Nextcloud)
- **Simon** (coordination Tribu)
- **Frédéric** (volumétries, BVV)
- **Nicolas** (portail apps, tests)
- **Johan**, **Samir**, **Joël** (incidents)
- **Aurélien**, **Mickaël**, **Benjamin**, **Valérie** (développements)
- **Hugo**, **Manon** (raccourcisseur d’URL)
- **Maxime Le Hérissi** (support Nextcloud) – absent, suivi par Benoît
- **Autres** : représentants des académies, équipes support, etc.

---

## Objet de la réunion
Faire le point sur l’avancement des projets du **DNE** sur les deux dernières semaines : budget, jalons, incidents techniques, évolutions fonctionnelles (Nextcloud, Tribu, BVV, communication unifiée, etc.) et préparer les actions à venir.

---

## Sujets abordés

| # | Sujet | Points clés |
|---|-------|-------------|
| 1 | **Réduction du budget DNE** | Décision déjà prise ; impact limité mais nécessite suivi des projets. |
| 2 | **Suivi précis des jalons** | Besoin de dates concrètes (semaine) plutôt que « T4 / avant‑été ». Audran chargé d’obtenir ces dates. |
| 3 | **Nextcloud 31 – régression fonctionnelle** | Version 31 introduit une régression du partage de fichiers ; impossible de livrer la V31 en production tant que le correctif n’est pas disponible. |
| 4 | **Formation Microsoft Office** | Rappel que la formation concerne tous les postes PC. |
| 5 | **Squash avec Tribu & comité référents ATNA** | Organisation d’un squash avec l’équipe Tribu (Simon) et d’un comité référents ATNA mardi prochain. |
| 6 | **Étude de volumétries** | Point à faire avec Frédéric pour re‑évaluer les profils nécessaires. |
| 7 | **Supervisor & formation support** | Prévoir une réunion C4 avec l’ensemble des équipes pour définir les besoins de formation. |
| 8 | **Campagne BNA** | Décalage du lancement du questionnaire du 16 juin au **27‑28 juin** pour éviter double sollicitation. |
| 9 | **Communication unifiée (Cisco vs solutions libres)** | Analyse des usages, choix d’outil à définir (Cisco WebX, solution libre, Teams, etc.). |
|10| **Projet Tribu – refonte UX/UI** | - Chiffrage en cours (3 lots : accueil / tableaux de bord, outils / recherche, administration). <br>- 200 j.h. estimés, 80 j.h. pour le lot 1. <br>- Planning visé : fin 2025 pour mise en prod, avec période de stabilisation en décembre. |
|11| **Incidents en cours** | • Regroupement (pré‑prod) – ticket ouvert, suivi avec le support Onissa. <br>• Déploiement d’application – problème de tâche planifiée, ticket créé. |
|12| **Conformité poste de travail** | Discussion sur les prérequis (Magenta, Intelligence, CTT) et planification des mises à jour (vacances d’été, fin décembre). |
|13| **Audit base de données – RAM** | Augmentation de 8 Go → 12 Go grâce aux ateliers Optimus Green ; plantage des services métrologie résolu. |
|14| **Intégration BVV dans CHAP** | Commande validée (35 j.h. de dev) ; démarrage imminent. |
|15| **BBB 3.0 – livrable** | Version livrée, recette validée, suivi des plugins et de la documentation. |
|16| **Portail Apps – statistiques** | 82 000 vidéos, 221 000 comptes, Matomo installé, suivi des usages. |
|17| **Raccourcisseur d’URL** | Développement en cours (Hugo & Manon) – livrable prévu début juin. |
|18| **Tube – thème graphique & transcription** | Thème graphique reporté à la rentrée prochaine. <br>Transcription vidéo opérationnelle en test, déploiement prévu avec Nicolas. |
|19| **Wi‑Fi – questionnaire académies** | Envoi du questionnaire, en attente de réponses. |

---

## Décisions prises

1. **Budget DNE** : réduction maintenue, aucun impact majeur prévu.
2. **Jalons** : Audran doit fournir des dates précises (semaine) d’ici la fin de la semaine.
3. **Nextcloud** : report de tout déploiement de la V31 jusqu’à réception du correctif de Maxime Le Hérissi.
4. **Campagne BNA** : nouvelle date de lancement **27‑28 juin**.
5. **Tribu** : validation du chiffrage (200 j.h.) et du découpage en 3 lots ; démarrage du développement dès validation du chiffrage.
6. **RAM BDD** : upgrade à 12 Go validé, suivi de la stabilité prévu jusqu’à fin mai.
7. **BVV** : commande de 35 j.h. validée, démarrage immédiat.

---

## Questions en suspens

| Question | Responsable / Suivi |
|----------|---------------------|
| Quand le correctif de la régression Nextcloud 31 sera‑t‑il disponible ? | Benoît (contact Maxime Le Hérissi) |
| Quels sont les prérequis techniques exacts (Kubernetes, Kafka, Terraform, …) pour les nouveaux développements ? | Audran / équipe technique – à clarifier avec les éditeurs. |
| Quel sera le périmètre exact de la refonte graphique Tribu (fonctionnalités à inclure) ? | Simon (validation avec les parties prenantes). |
| Quelle solution de communication unifiée sera retenue ? | Comité décisionnel – à définir après analyse des usages. |
| Quand les académies fourniront‑elles les réponses au questionnaire Wi‑Fi ? | Responsable questionnaire (non nommé) – relance prévue. |

---

## Tâches à effectuer

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Fournir dates précises des prochains jalons | **Audran** | Fin de semaine |
| Envoyer les slides à compléter pour le comité référents ATNA | **Frédéric** | D‑2 avant le comité (mardi) |
| Organiser le squash Tribu avec Simon | **Simon** | Avant le prochain comité (date à fixer) |
| Suivi du ticket Nextcloud avec Maxime Le Hérissi | **Benoît** | Dès réception du correctif |
| Réunion C4 pour la formation des équipes support | **Responsable formation** (non nommé) | Semaine prochaine |
| Relancer le support Onissa sur le ticket de tâche planifiée | **Johan / Samir** | 3 jours |
| Finaliser le chiffrage et valider le lancement du développement Tribu | **Simon** | Dès validation du chiffrage (début mai) |
| Mettre à jour la documentation (tutoriels, guides) pour la refonte Tribu | **Équipe documentation** | Avant mise en prod (début décembre) |
| Déployer l’augmentation RAM et monitorer la stabilité | **Equipe infra** | Fin mai |
| Préparer le rapport de volumétries avec Frédéric | **Frédéric** + **Audran** | Avant le comité référents (mardi) |
| Suivi du développement du raccourcisseur d’URL | **Hugo** & **Manon** | Livraison prévue début juin |
| Planifier la migration des académies (BNA) sur les nouvelles dates | **Responsable campagne BNA** | 27‑28 juin |
| Réunion de lancement pour l’Ile‑de‑France (Wi‑Fi) | **Responsable Wi‑Fi** | Octobre‑novembre (date à confirmer) |

---

## Prochaine rencontre

- **Comité référents ATNA** – **Mardi prochain** (date précise à confirmer).
- Un point d’avancement général sera prévu **la semaine suivante** pour faire le suivi des actions listées ci‑dessus.

---

*Fin du compte‑rendu.*
