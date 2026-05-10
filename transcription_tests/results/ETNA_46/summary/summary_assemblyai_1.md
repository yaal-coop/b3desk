# Compte rendu de la 46ᵉ réunion du Comité – 30 avril 2026

---

## Participants
| Nom | Fonction / Rôle |
|-----|-----------------|
| **Olivier** | Animateur du comité |
| **Hugo** | Responsable projets |
| **Benoît** | Responsable technique / support |
| **Audran** | Responsable suivi des jalons (DNE) |
| **Simon** | Responsable référents régionaux |
| **Frédéric** | Responsable intégration PGV & BVB |
| **Nicolas** | Responsable Nuage (Nextcloud) |
| **Maxime** (RSI) | Responsable support éditeur Nextcloud |
| **Johan** | Responsable mise en production Tribu |
| **Vincent** | (mentionné – non présent) |
| **Autres** | Participants ponctuels (ex. : Paul Fouad, Irina, etc.) |

---

## Objet de la réunion
Faire le point sur l’avancement des projets du **Domaine Numérique de l’Éducation (DNE)**, identifier les blocages (budget, planning, livrables) et définir les actions à mener pour les semaines à venir.

---

## Durée estimée
≈ 1 h 30 min (début ≈ 09 h 00 – fin ≈ 10 h 30).

---

## Sujets abordés

| Thème | Points clés |
|-------|-------------|
| **1. Budget DNE** | - Réduction globale du budget confirmée (montants en attente).<br>- Impact limité mais risque de « coup de rabot » sur certains projets. |
| **2. Suivi des jalons / visibilité** | - Besoin urgent de dates précises (septembre / octobre) pour les nouvelles fonctionnalités.<br>- Difficulté à garantir les dates auprès des prestataires (Collabora, Nextcloud, Megzot). |
| **3. Relation avec les prestataires** | - Manque de fiabilité des plannings (ex. : BVB, Nextcloud 31).<br>- Nécessité d’un meilleur cadre contractuel (exigences sur les livrables financés). |
| **4. Nextcloud (Nuage)** | - Version 31 introduit une régression fonctionnelle (partage de fichiers).<br>- Migration reportée, besoin d’un environnement parallèle pour tester.<br>- Correctif attendu de Maxime / l’équipe éditeur. |
| **5. BMA (enquête)** | - Lancement décalé du 16 juin au 27‑28 juin (conflit avec enquête BELCOM). |
| **6. Comité des référents ATHNA** | - Réunion prévue **mardi prochain** ; slides à préparer (envoi imminent). |
| **7. Tribu – refonte graphique UX8** | - Chiffrage en cours (3 lots ≈ 200 jv).<br>- Livraison visée fin 2025, mise en prod prévue fin novembre / début décembre 2025.<br>- Environnements pré‑prod, prod et AQT créés. |
| **8. PGV & VisioAgent** | - Intégration PGV validée avec Frédéric Pommiès.<br>- VisioAgent (BBB) validé, déploiement en cours. |
| **9. Apple Quad / VNV** | - Travail sur les Gateways, montée en charge et démonstrateur Cisco ↔ BBB. |
| **10. Portail Apps** | - 221 000 comptes créés, 73 000 actifs depuis déc. 2023.<br>- Statistiques détaillées disponibles (parcours utilisateurs). |
| **11. Raccourcisseur d’URL** | - Développement en cours (2 devs), démonstration attendue la semaine prochaine. |
| **12. Architecture micro‑applications (cycle de vie)** | - Mise en place d’une couche micro‑app pour le portail (gestion des comptes, vidéos, etc.). |
| **13. Peertube / Tube** | - Refondation graphique (thèmes vs instances).<br>- Plugin de suppression automatique des vidéos (délais légaux). |
| **14. Rancher** | - Livraison récente, mais déploiement d’applications encore bloqué (documentation). |
| **15. Wi‑Fi académies** | - Questionnaire envoyé aux académies d’Île‑de‑France, réponses en attente. |
| **16. Etna (messagerie)** | - Nécessité de clarifier le périmètre du projet auprès du GSR. |

---

## Décisions prises

| Décision | Responsable(s) |
|----------|----------------|
| **Réduction du budget DNE** – validation du principe, chiffrage des impacts à finaliser. | Olivier |
| **Report du lancement BMA** du 16 juin au 27‑28 juin. | Hugo |
| **Validation de l’intégration PGV** et du lancement de VisioAgent. | Frédéric |
| **Augmentation de la RAM PostgreSQL** de 8 Go à 12 Go (via ateliers Optimus Green). | Nicolas |
| **Déploiement de la version 31 de Nextcloud** différé jusqu’à réception du correctif sur les partages. | Maxime + Nicolas |
| **Chiffrage final de la refonte Tribu** à acter avant le lancement du développement (prévu en mai). | Johan + équipe dev |
| **Mise à jour du portail Apps** – publication de la version 6.4.1 en prod. | Hugo |
| **Création des slides pour le comité référent** – envoi d’ici fin de semaine. | Frédéric |
| **Planification du prochain comité des référents ATHNA** – réunion mardi prochain (distanciel). | Simon |

---

## Questions en suspens

1. **Dates précises** (septembre / octobre) pour les livraisons fonctionnelles attendues par Audran.
2. **Quand la version 3.1 de BBB sera‑t‑elle disponible** ? (dépend du fournisseur).
3. **Calendrier exact de la migration Nextcloud 31** – besoin d’un environnement parallèle validé.
4. **État du correctif du script de migration académique → centralisé** (attente du retour de Nantes).
5. **Définition du périmètre fonctionnel du plugin “délégation de salles”** (CNET).
6. **Choix de la stratégie de diffusion du plugin Thunderbird** (webmail uniquement ou déploiement large).

---

## Tâches à effectuer

| Action | Responsable | Échéance |
|--------|-------------|----------|
| Fournir les montants définitifs du nouveau budget DNE. | Olivier | 10 mai 2026 |
| Finaliser le chiffrage des 3 lots Tribu et valider le planning de développement. | Johan / équipe dev | 15 mai 2026 |
| Envoyer les slides du comité référent (contenu à remplir). | Frédéric | 5 mai 2026 |
| Tester et valider le correctif de la version 31 (partage de fichiers). | Maxime + Nicolas | 12 mai 2026 |
| Relancer le support MISA pour le ticket de regroupement de terminaux. | Benoît | 8 mai 2026 |
| Préparer le correctif du script de migration Nextcloud (Nantes). | Benoît | 14 mai 2026 |
| Déployer le raccourcisseur d’URL et préparer la démonstration. | Hugo (dev) | 19 mai 2026 |
| Mettre à jour la documentation et les tutoriels suite à la refonte Tribu. | Johan | 30 novembre 2025 (pré‑prod) |
| Réaliser le suivi de la RAM PostgreSQL (monitoring) et préparer le rollback éventuel. | Nicolas | 31 mai 2026 |
| Consolider les réponses du questionnaire Wi‑Fi académies. | Simon | 15 mai 2026 |
| Décider du mode de diffusion du plugin Thunderbird (webmail‑only ou général). | Frédéric + équipe identité | 20 mai 2026 |

---

## Prochaine rencontre

- **Réunion du comité des référents ATHNA** – **mardi 7 mai 2026**, en distanciel (invitation et slides à diffuser d’ici le 5 mai).

---

*Fin du compte rendu.*
