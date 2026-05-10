# Compte‑rendu de la 46ᵉ réunion du Comité de Domaine
**Date** : 28 avril 2026
**Durée** : non précisée (environ 1 h)

---

## Participants
| Nom | Fonction / Rôle |
|-----|-----------------|
| **Audran** | Responsable suivi projets / jalons |
| **Benoît** | Animateur / suivi des incidents |
| **Simon** | Responsable du « squash » Tribu |
| **Frédéric** (et **Valérie**) | Pilotage intégration BVV & suivi volumétries |
| **Nicolas** | Support Nextcloud & portail apps |
| **Johan** | Supervision & coordination C4 |
| **Samir** | Support technique |
| **Joël** | Support incidents |
| **Maxime Le Hérissi** | Responsable support éditeur Nextcloud |
| **Irina** (pôle Paris) | Responsable équipe SOCle |
| **Mickaël** | Responsable BBB 3.0 |
| **Benjamin** | Formation / usage Office |
| **Hugo** | Développement URL raccourci & thème Tube |
| **Manon** | Suivi thème graphique Tube |
| **Christophe Sisko / Sœur Terreso** | Conformité poste de travail |
| **Bruno** | Point communication unifiée (invité) |
| **Autres** (participants ponctuels) | – |

> La liste n’est pas exhaustive ; les intervenants cités sont ceux qui ont pris la parole sur un sujet décisionnel.

---

## Objet de la réunion
Faire le point sur l’avancement des projets du domaine (budget, jalons, incidents, évolutions techniques) et définir les actions à mener avant la prochaine rencontre.

---

## Sujets abordés

| N° | Thème | Points clés |
|----|-------|-------------|
| 1 | **Réduction du budget DNE** | Décision prise, impact « indolore » sur les projets en cours. |
| 2 | **Visibilité des jalons / roadmap** | Besoin d’une planification plus précise (dates T4, été, etc.). |
| 3 | **Nextcloud – régression version 31** | Impossible de livrer la v31 ; besoin d’un correctif éditeur. |
| 4 | **Formation Microsoft Office & SBM** | Point d’attention sur l’usage généralisé. |
| 5 | **Squash Tribu** | Organisation d’un squash avec l’équipe Tribu (hors Simon). |
| 6 | **Comité référents ATNA** | Réunion prévue mardi prochain avec DRAZI/SGRA. |
| 7 | **Étude de volumétries – projet Optation** | Point à faire avec Frédéric pour réévaluer les profils. |
| 8 | **Superviseur / C4 – formation support** | Point à planifier avec l’ensemble des équipes. |
| 9 | **Campagne BNA** | Décalage du lancement du 16 juin au 27‑28 juin. |
|10| **Communication unifiée** | Aucun avancement ; invitation à Bruno pour un topo. |
|11| **Refonte graphique Tribu (UX/UI)** | 200 j‑h estimés, 3 lots, cible production fin 2025, pré‑prod déjà en place. |
|12| **Mise à jour Tribu – pas de coupure** | Déploiement transparent, mise à jour des tutos prévue. |
|13| **Incidents en cours** | – Regroupement de terminaux (pré‑prod) <br> – Déploiement d’application (postes) – ticket ouvert avec Onissa. |
|14| **Conformité poste de travail** | Rencontre avec Sœur Terreso & Christophe Sisko, suivi des prérequis. |
|15| **Dépendance aux éditeurs** | Manque de visibilité sur prérequis techniques (Kubernetes, Kafka, etc.). |
|16| **Intégration BVV dans CHAP** | Commande validée (35 j dev), démarrage imminent. |
|17| **VisioAgent / BBB** | Livraison du frontal, fonction « favoris », prochaine étape : plugin 1.3. |
|18| **Portail Apps – statistiques** | 82 k vidéos, 221 k comptes, Matomo installé. |
|19| **Raccourci URL** | Développement en cours (Hugo), livrable début juillet. |
|20| **Peertube / Tube** | Thématique graphique à revoir (prévu Q4 2026), transcription & transcodage en cours de test. |
|21| **Wi‑Fi – questionnaire** | Envoi aux académies d’Île‑de‑France, réponses attendues. |

---

## Décisions prises

| Décision | Responsable / Commentaire |
|----------|---------------------------|
| Réduction du budget DNE validée. | Comité |
| Augmenter la visibilité de la roadmap (dates précises). | Audran + chefs de projet |
| Reporter la campagne BNA au 27‑28 juin. | Responsable BNA (Benoît) |
| Lancer l’intégration BVV dans CHAP (35 j dev). | Frédéric Pomies / Valérie |
| Déployer la refonte Tribu sans interruption de service. | Johan (pilotage) |
| Augmenter la RAM des serveurs Postgres à 12 Go (optimus‑green). | CRTH / équipe infra |
| Ne pas mettre en production la version 31 de Nextcloud tant que le correctif n’est pas disponible. | Benoît + Maxime Le Hérissi |
| Faire intervenir Bruno pour le point communication unifiée. | Benoît (organisation) |
| Valider le chiffrage de la refonte Tribu avant lancement dev. | Équipe dev (Simon / Johan) |
| Mettre en place les trois environnements (pré‑prod, iso‑prod, AQT) pour Tribu. | Équipe technique |
| Reporter le déploiement du thème graphique Tube à la rentrée prochaine. | Hugo / Manon |

---

## Questions en suspens

| Question | Responsable / Suivi |
|----------|--------------------|
| Date de sortie de Collabora 3.1 (et impact sur nos développements). | Audran |
| Calendrier exact des prochains jalons (T4, été, etc.). | Audran |
| Obtention des prérequis d’installation auprès des éditeurs (K8s, Kafka, Terraform…). | Benoît |
| Confirmation du correctif Nextcloud 31 et plan de migration parallèle. | Benoît + Maxime Le Hérissi |
| Liste exhaustive des fonctionnalités disparues dans BBB 3.0. | Mickaël |
| Validation du budget et du planning pour le thème graphique Tube. | Hugo / Manon |
| Finalisation du plugin VisioAgent 1.3 (déploiement). | Yal |
| Retour du questionnaire Wi‑Fi des académies. | Frédéric |
| Définition précise des usages de la future solution de communication unifiée (Cisco vs libres). | Bruno |

---

## Tâches à effectuer

| Action | Responsable | Échéance |
|--------|-------------|----------|
| Faire le point avec **Frédéric** sur les volumétries du projet Optation et réévaluer les profils. | Benoît | 15 mai 2026 |
| Organiser le **squash Tribu** (hors Simon). | Simon | 22 mai 2026 |
| Préparer le **comité référents ATNA** (slides à remplir). | Benoît | 30 avril 2026 |
| Envoyer le questionnaire **Wi‑Fi** aux académies d’Île‑de‑France et relancer. | Frédéric | 10 mai 2026 |
| Contacter **Maxime Le Hérissi** pour obtenir le correctif Nextcloud 31 et planifier la migration. | Benoît | 05 mai 2026 |
| Suivre les tickets **regroupement** et **déploiement d’application** avec le support Onissa. | Johan | En cours |
| Mettre à jour la **conformité poste de travail** (pré‑requis, licences). | Christophe Sisko / Sœur Terreso | 31 mai 2026 |
| Valider le **chiffrage** de la refonte Tribu et confirmer le planning de développement. | Simon / équipe dev | 01 juin 2026 |
| Déployer les environnements **pré‑prod / iso‑prod / AQT** pour Tribu. | Équipe technique | 15 juin 2026 |
| Finaliser le **développement du raccourci URL** (Hugo). | Hugo | 01 juillet 2026 |
| Lancer le **développement du plugin VisioAgent 1.3**. | Yal | 15 juillet 2026 |
| Planifier l’**augmentation RAM** sur les serveurs frontaux Nextcloud (optimus‑green). | CRTH | 20 mai 2026 |
| Suivre le **déploiement du thème graphique Tube** et la mise en place de la transcription vidéo. | Manon / Hugo / Nicolas | Q4 2026 |
| Organiser le **point C4** (formation des équipes support). | Johan | 10 mai 2026 |
| Faire le suivi du **déploiement du plugin BBB 3.0** et récupérer la liste des fonctionnalités manquantes. | Mickaël | 30 mai 2026 |

---

## Prochaine rencontre

- **Date** : Mardi prochain (à confirmer, probable 5 mai 2026) – réunion du **Comité référents ATNA**.
- **Ordre du jour prévisionnel** : suivi des actions listées ci‑dessus, mise à jour de la roadmap, point sur Nextcloud 31 et sur la refonte Tribu.

---

*Ce compte‑rendu a été rédigé à partir de la transcription de la réunion du 28 avril 2026. Toute correction ou ajout doit être communiqué avant la prochaine réunion.*
