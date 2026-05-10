# Compte‑rendu de la réunion du 30 avril 2026
**Objet** : Point d’avancement des projets DNE (Domaines Numériques de l’État) – quinzaine

---

## Participants

| Nom | Fonction / Rôle |
|-----|-----------------|
| Didier | Responsable DNE |
| Hugo | Chef de projet – Portail Apps |
| Benoît | Responsable technique – Nextcloud / Tribu |
| Audran | Représentant du comité de domaine |
| Nicolas | Responsable support & infrastructure |
| Frédéric | Responsable des commandes & suivi budgétaire |
| Simon | Responsable Squash / Tribu |
| Maxime Leherici | Support éditeur Nextcloud |
| Paul Fouad | Responsable communication unifiée |
| … (autres intervenants ponctuels) |  |

---

## Durée estimée
Environ **2 h** (début ≈ 09 h – fin ≈ 11 h).

---

## Sujets abordés

| Thème | Points clés |
|-------|-------------|
| **Budget** | - Réduction du budget global de la DNE (attente de confirmation des montants).<br>- Risque de “coup de rabot” sur certains projets. |
| **Planification & jalons** | - Besoin urgent de dates de mise en production plus précises (ex. : septembre).<br>- Difficulté à obtenir des engagements fiables de la part des prestataires (Collaborat, Nextcloud, B2B, etc.). |
| **Nextcloud** | - Version 31 sortie avec régression fonctionnelle (liens de partage cassés).<br>- Déploiement en production bloqué ; besoin d’un correctif avant migration. |
| **Tribu – refonte graphique (UX/UI)** | - Chiffrage en cours ; 3 lots (accueil, recherche, admin) → ~200 j‑h.<br>- Objectif MEP fin 2025 (début novembre/décembre 2025).<br>- Environnements pré‑prod, dev et AQT préparés. |
| **Licences Microsoft** | - Renouvellement effectué la semaine dernière (50 licences). |
| **Squash & comité référents ATNA** | - Squash à organiser avec Simon (prochain comité).<br>- Comité référents ATNA prévu mardi prochain (distanciel). |
| **Adoption & formation** | - Étude de volumétries en cours, point à faire avec Frédéric.<br>- Montée en compétences des équipes support (C4). |
| **Campagne BNA** | - Report du lancement du 16 juin au 27/28 juin (conflit avec enquête DELCOM). |
| **Communication unifiée** | - Analyse des outils (Cisco, Webex, Tchap, solutions libres) et définition des usages. |
| **VisioAgent** | - Validation de l’intégration de DBV dans Cap Education.<br>- Développement d’un bouton “rejoindre la réunion” dans Tchap. |
| **Portail Apps** | - 80 000 vidéos, 221 000 comptes, 73 000 actifs depuis déc. 2022.<br>- Installation de Matomo, mise à jour 6.4.1 en prod.<br>- Raccourcisseur d’URL en cours (démo prévue la semaine prochaine). |
| **Infrastructure (Rancher, RAM, etc.)** | - +4 Go RAM sur serveurs BDD (passage de 8 → 12 Go).<br>- Tests Rancher en cours ; déploiement d’applications encore bloqué. |
| **Wi‑Fi académies** | - Questionnaire envoyé aux académies d’Île‑de‑France, en attente de réponses. |
| **Divers** | - Points rapides sur messagerie, plugins, migration de comptes, etc. |

---

## Décisions prises

| Décision | Responsable(s) | Délai |
|----------|----------------|-------|
| **Reporter la campagne BNA** du 16 juin au 27/28 juin. | Benoît / équipe BNA | 27 juin |
| **Planifier la mise en production de la version 31 de Nextcloud** uniquement après réception du correctif sur les liens de partage. | Benoît – Maxime Leherici (support éditeur) | Avant fin mai |
| **Valider le chiffrage de la refonte graphique de Tribu** et lancer les développements dès que le chiffrage sera acté. | Simon (Squash) / équipe dev Tribu | Juin 2026 |
| **Organiser le squash Tribu** avant le prochain comité référents. | Simon | Avant le comité du 6 mai |
| **Déployer le raccourcisseur d’URL** et le mettre à disposition via API. | Hugo | Démo la semaine prochaine (vers 10 juillet) |
| **Augmenter la RAM des serveurs PostgreSQL** à 12 Go (déjà effectué). | Nicolas / équipe infra | ✔︎ |
| **Planifier la réunion du comité référents ATNA** (distanciel). | Didier | Mardi 7 mai 2026 |
| **Faire le point avec Frédéric** sur la liste des profils à doter pour le projet d’adoption. | Frédéric | Avant le comité référents |

---

## Questions en suspens

| Question | Responsable(s) | Échéance envisagée |
|----------|----------------|--------------------|
| Quand les prestataires (Collaborat, B2B, etc.) pourront‑ils fournir des dates de livraison fiables ? | Audran / Didier | À définir (suivi continu) |
| Quel est le planning exact de la migration du script Nextcloud (Nantes → central) ? | Benoît / équipe Nextcloud | Correctif attendu d’ici fin mai |
| Validation du correctif de la version 31 (liens de partage) ? | Maxime Leherici | Avant fin mai |
| Déploiement du Rancher : quelles sont les étapes restantes ? | Nicolas | Juin 2026 |
| Retour du questionnaire Wi‑Fi académies ? | Paul Fouad | Fin mai |
| Définir les usages exacts et la gouvernance de la communication unifiée (outil privé vs libre). | Paul Fouad / Didier | Juin 2026 |

---

## Tâches à effectuer

| Tâche | Responsable | Date limite |
|-------|-------------|-------------|
| Envoyer les slides à remplir pour le comité référents ATNA. | Didier | 2 mai 2026 |
| Contacter Maxime Leherici pour obtenir le correctif Nextcloud 31. | Benoît | 31 mai 2026 |
| Finaliser le chiffrage des lots Tribu et valider le planning de dev. | Simon | 15 juin 2026 |
| Lancer le test du raccourcisseur d’URL et préparer la démonstration. | Hugo | 10 juillet 2026 |
| Mettre à jour la documentation Rancher et préparer le guide de déploiement. | Nicolas | 30 juin 2026 |
| Réaliser le point avec Frédéric sur les profils d’adoption et préparer le comité. | Frédéric | 5 mai 2026 |
| Suivre les réponses du questionnaire Wi‑Fi et préparer le compte‑rendu. | Paul Fouad | 30 mai 2026 |
| Préparer le livrable VisioAgent (intégration DBV) pour la prochaine version de Tchap. | Benoît / équipe VisioAgent | 15 juin 2026 |
| Vérifier la conformité des licences Microsoft et préparer le renouvellement Q3 2026. | Frédéric | 15 juillet 2026 |

---

## Prochaine rencontre

- **Comité référents ATNA** – mardi 7 mai 2026, en distanciel (heure à confirmer).
- **Suivi projet Tribu** – réunion de suivi prévue la semaine du **15 mai** (date précise à fixer).

---

*Fin du compte‑rendu.*
