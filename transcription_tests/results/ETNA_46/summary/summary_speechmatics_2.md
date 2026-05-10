# Compte‑rendu de la réunion du Comité de suivi des projets
**Date** : 30 avril 2026
**Heure** : 09 h – 11 h (~ 2 h)

---

## Participants
| Nom | Fonction / Rôle |
|-----|-----------------|
| **Didier** | Responsable ADN / animation du comité |
| **Hugo** | Chef de projet Nextcloud / URL‑shortener |
| **Benoît** | Responsable technique Nextcloud & Collabora |
| **Audran** | Responsable budget et suivi domaine |
| **Antoine** | Intervenant ponctuel (support) |
| **Simon** | Animateur des retours d’expérience (squash) |
| **Frédéric** | Responsable dotation & liaison académies |
| **Nicolas** | Support / suivi infrastructure |
| **Maxime** | RSI – contact éditeur Nextcloud |
| **Johann** | Responsable déploiement production |
| **Valérie** | Pilotage des commandes de développement |
| **Michael / Benjamin** | Équipe gateway / démonstrateur |
| **François, Sophie, Valérie** | Portail intranet / refonte |
| **Autres** | Membres des équipes support, dev, pilotage académies |

---

## Objet de la réunion
- Faire le point sur l’avancement des projets du domaine ADN (budget, jalons, livrables).
- Identifier les blocages liés aux prestataires (Nextcloud, Collabora, éditeurs externes).
- Valider les priorités et les dates de mise en production des nouvelles fonctionnalités (Tribu, URL‑shortener, portail intranet, etc.).

---

## Durée estimée
**Environ 2 h** (début 09 h – fin 11 h).

---

## Sujets abordés

| Thème | Points clés |
|-------|-------------|
| **1. Budget ADN** | - Réduction du budget global (confirmation des montants en cours). <br>- Impact limité mais risque de « coup de rabot » sur certains projets. |
| **2. Précision des jalons** | - Besoin d’une visibilité claire (septembre / octobre) pour les nouvelles fonctionnalités. <br>- Actuellement les dates restent floues (« avant / après l’été »). |
| **3. Gestion des prestataires** | - Alignement sur les road‑maps de Nextcloud, Collabora, autres éditeurs. <br>- Nécessité d’obtenir des engagements plus réalistes. |
| **4. Incident Nextcloud 31** | - Régression fonctionnelle introduite unilatéralement. <br>- Impossible de livrer la version 31 → report du planning. |
| **5. Licences Microsoft** | - Renouvellement effectué la semaine précédente (30 000 agents). |
| **6. Retour d’expérience squash** | - Organisation d’un point avec Simon (date à fixer). |
| **7. Étude de dotation** | - En cours de volumétrie, suivi avec Frédéric. |
| **8. Refondre graphique du projet *Tribu* (Luxy)** | - Chiffrage en cours, 3 lots (accueil, tableaux de bord, administration). <br>- 200 jours estimés, mise en prod visée fin 2025 (début 2026). |
| **9. URL‑shortener** | - Développement en cours, démonstration prévue le **1 juillet 2026 à 12 h**. |
| **10. Cycle de vie micro‑applications & PeerTube** | - Architecture en cours (micro‑apps, token, transcription & transcodage). |
| **11. Portail agent / intranet** | - Version 6.4.1 en prod, travaux de refonte prévus, slides à préparer pour le comité référent. |
| **12. Wi‑Fi** | - Questionnaire envoyé aux académies Île‑de‑France, réponses en attente. |
| **13. Pilotes académiques** | - Déploiement en Corse (premier pilote complet). <br>- Suivi des déploiements à Nantes, Poitiers, Cannes, etc. |
| **14. Messagerie** | - Migration de Thunderbird → webmail, besoin d’accompagnement et de documentation. |

---

## Décisions prises

| Décision | Responsable / Commentaire |
|----------|---------------------------|
| **Réduction du budget ADN** validée, attend confirmation chiffrée d’Audran. | Audran |
| **Améliorer la précision des dates de livraison** : mise en place d’un tableau de suivi partagé (Jalons Sept‑Oct). | Didier + équipe projet |
| **Reporter le déploiement de Nextcloud 31** jusqu’à obtention d’un correctif stable. | Benoît + Maxime |
| **Déployer la refonte *Tribu* en 3 lots** avec un planning détaillé (lot 1 ≈ 80 j, lot 2 ≈ 60 j, lot 3 ≈ 60 j). | Valérie (validation) + équipe dev |
| **Planifier la démonstration du URL‑shortener** le 1 juillet 2026. | Hugo |
| **Augmenter la RAM des serveurs Postgres à 12 Go** (interim) et monitorer les incidents. | Équipe infra (déjà réalisé) |
| **Décaler le PNR** du 16 juin au **27/28 juin** pour éviter un blanc de sollicitations. | Responsable communication |
| **Préparer les slides** du comité référent (deadline : fin de semaine). | Frédéric |
| **Valider la commande de 35 jours de dev** pour la refonte *Tribu*. | Valérie |
| **Continuer le travail sur le gateway** et préparer le démonstrateur pour Audran. | Michael & Benjamin |
| **Conserver le plugin de partage** en attente de correctif (Nextcloud). | Benoît + Maxime |

---

## Questions en suspens

| Question | Responsable / Échéance |
|----------|------------------------|
| Quand la version 31 de Nextcloud sera‑t‑elle stable ? | Maxime (réponse attendue d’ici fin mai) |
| Quels sont les jalons précis (dates) pour les livraisons prévues en septembre/octobre ? | Didier (mise à jour du tableau de suivi) |
| Avancement du script de migration académique → central (Nextcloud) ? | Nicolas (en attente du retour de l’équipe Nantes) |
| Résultats du questionnaire Wi‑Fi des académies ? | Responsable questionnaire (date de clôture : 15 mai) |
| Validation finale du portail intranet (version 6.4.1) et plan de refonte ? | François / Sophie / Valérie (début juin) |
| Quand le plugin de partage sera‑t‑il corrigé ? | Benoît + Maxime |
| Date de la prochaine réunion squash (avec Simon) ? | Simon (à fixer) |
| Priorisation des développements plugins externes (ex : sélection aléatoire) ? | Équipe produit (définir Q2 2026) |

---

## Tâches à effectuer (avec responsable)

| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Confirmer les montants exacts de la réduction budgétaire ADN | Audran | 07 mai |
| Mettre à jour le tableau de suivi des jalons (Sept‑Oct) | Didier | 10 mai |
| Obtenir le correctif de la régression Nextcloud 31 et planifier le test en pré‑prod | Benoît + Maxime | 15 mai |
| Finaliser le chiffrage détaillé des 3 lots *Tribu* et valider le planning | Valérie | 12 mai |
| Préparer la démonstration du URL‑shortener (prototype fonctionnel) | Hugo | 01 juillet |
| Augmenter la RAM des serveurs Postgres à 12 Go (déjà fait) – monitorer les incidents | Équipe infra | En cours |
| Envoyer les slides du comité référent aux participants | Frédéric | 05 mai |
| Relancer l’équipe Nantes pour le script de migration Nextcloud | Nicolas | 08 mai |
| Analyser les réponses du questionnaire Wi‑Fi et préparer le compte‑rendu | Responsable questionnaire | 15 mai |
| Finaliser la refonte du portail intranet (UX, tests) | François / Sophie / Valérie | 30 mai |
| Organiser le point squash avec Simon | Simon | À définir (début juin) |
| Suivre le développement du gateway et préparer le démonstrateur | Michael & Benjamin | 20 mai |
| Documenter le processus de migration de la messagerie (Thunderbird → webmail) | Équipe support | 31 mai |

---

## Prochaine rencontre
- **Comité référent** : **du 7 au 9 mai 2026** (date précise à confirmer).
- **Comité de domaine** (suivi général) : **prévu dans un mois**, le **10 juin 2026**.

---

*Le présent compte‑rendu sera diffusé aux participants et archivé dans le répertoire partagé du comité.*
