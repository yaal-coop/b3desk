# Compte rendu de réunion

**Date** : 30 avril 2026
**Durée** : ~ 2 h 30 (prévue 1 h)

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| **Benjamin** | Développeur / coordinateur |
| **Miguel** | Développeur |
| **Arwa** | Responsable configuration BBB |
| **Benoît** | Testeur / support |
| **Pierre** | Responsable produit |
| **Michael** | Chef de projet |
| **Mickaël** | Responsable estimation |
| **Sébastien** | Responsable release |
| **Autres** | Participants occasionnels (ex. : Michel) |

---

## Objet de la réunion
1. Mettre en place un point d’avancement récurrent.
2. Faire le point sur la livraison du **code unique** et les évolutions BBB.
3. Traiter le ticket **#666** (erreur de salon) et la remontée de logs.
4. Analyser les problèmes de stabilité de la connexion **Nextcloud** (token).
5. Valider le budget et le lancement du **salon silencieux** (messagerie nationale).
6. Planifier les prochaines releases (1.3, 1.3.1) et la gestion des migrations.
7. Définir une méthode d’estimation des tâches (tags).

---

## Décisions prises
| Décision | Détails |
|----------|---------|
| **Point bi‑hebdomadaire** | Tous les mercredis à **11 h 30**. Benjamin envoie l’invitation. |
| **Paramètre BBB** | Le paramètre à modifier sera indiqué dans la PR et ajouté à la release. |
| **Log remontée** | Conserver la remontée de logs introduite par Arwa. |
| **Ordre des migrations** | Respecter l’ordre : migration *tri des salons* → migration *code unique*. La release contiendra toutes les migrations, exécutées séquentiellement. |
| **Release 1.3** | Création prévue **aujourd’hui à 14 h** (Sébastien guide Benjamin). |
| **Release 1.3.1** | Intégrera le **code unique** et le **numéro d’appel** après validation de la 1.3. |
| **Salon silencieux** | Lancement dès que le devis est validé (budget 2025 jours de développement). |
| **Estimation des tâches** | Michael envoie un tableau de correspondance *tags ↔ estimation* (jours/h). |
| **Investigation Nextcloud** | Benoît poursuit les tests de stabilité ; les résultats seront présentés à la prochaine réunion. |

---

## Sujets abordés & points clés
| Sujet | Points discutés |
|-------|-----------------|
| **Bi‑hebdomadaire** | Fréquence choisie pour limiter la charge tout en suivant l’avancement. |
| **Livraison du code unique** | - Deux questions sur la configuration restante.<br>- Nécessité d’un scénario de test pour la version 3.<br>- Variable à modifier identifiée mais nom à préciser. |
| **Paramètres BBB** | - Deux nouvelles variables (affichage du PIN, numéro de téléphone).<br>- Le numéro de téléphone est fourni par Arwa et doit être injecté dans la config. |
| **Ticket #666** | - Problème d’état incohérent d’un salon résolu par Arwa (suppression d’un champ).<br>- Conservation de la remontée de logs souhaitée. |
| **Instabilité Nextcloud** | - Token applicatif valable 30 jours.<br>- Problèmes possibles : surcharge du serveur, bibliothèque Python obsolète, version de Nextcloud.<br>- Besoin de reproduire le bug et de mesurer les temps de réponse. |
| **Budget & salon silencieux** | - Budget de 2025 jours alloué au développement de Betfridesk.<br>- Le devis est validé, lancement du salon silencieux en attente de support juridique. |
| **Road‑map releases** | - 1.3 (déploiement immédiat) → 1.3.1 (code unique + numéro d’appel).<br>- Priorité au classement alphabétique/favori des salles (forte demande utilisateur). |
| **Estimation des tâches** | - Utilisation de tags (XS, S, M, L, XL) pour donner une fourchette d’effort (ex. : M ≈ 3 jours).<br>- Michael doit fournir le tableau de correspondance. |
| **Coordination avec Renater** | - Renater développe les briques internes ; nous restons fournisseur de services.<br>- Nécessité de clarifier les fonctionnalités possibles sans développements supplémentaires. |

---

## Questions en suspens
| Question | Responsable / Action |
|----------|----------------------|
| Nom exact de la variable BBB à modifier (pour le PIN) | Benjamin → préciser dans la PR. |
| Scénario de test complet pour la version 3 (v3) | Miguel → fournir un cas d’usage. |
| Confirmation que la migration *tri des salons* sera incluse avant la migration *code unique* dans la release | Benjamin → valider avec l’équipe release. |
| Durée optimale du token applicatif (30 jours vs plus long) | Benoît → tester l’impact d’une durée plus longue. |
| Support juridique pour le lancement du salon silencieux | Michael → identifier le contact juridique. |
| État des librairies Python utilisées par Betfridesk (mise à jour) | Sébastien → audit des dépendances. |
| Date précise du prochain point d’avancement (bi‑hebdomadaire) | Benjamin → envoi de l’invitation. |

---

## Tâches à effectuer
| Tâche | Responsable | Échéance |
|-------|-------------|----------|
| Envoyer l’invitation du point bi‑hebdomadaire (mercredi 11 h 30) | **Benjamin** | Avant le prochain mercredi |
| Ajouter le paramètre BBB dans la PR et la release | **Benjamin** | Avant la release 1.3 |
| Fournir le scénario de test v3 | **Miguel** | Avant la prochaine réunion |
| Vérifier l’ordre des migrations dans la release | **Benjamin** | Avant la release 1.3 |
| Réaliser les tests de stabilité Nextcloud (reproduire le bug) | **Benoît** | Au plus tard 7 jours |
| Envoyer le tableau de correspondance *tags ↔ estimation* | **Michael** | Dans la journée |
| Guidage de Benjamin pour la création de la release 1.3 (14 h) | **Sébastien** | Aujourd’hui 14 h |
| Identifier le support juridique pour le salon silencieux | **Michael** | Avant la prochaine réunion |
| Auditer les dépendances Python de Betfridesk | **Sébastien** | Avant la release 1.3.1 |
| Communiquer les résultats des tests Nextcloud à l’équipe | **Benoît** | Lors du prochain point bi‑hebdomadaire |

---

## Prochaine rencontre
- **Date** : Mercredi 5 mai 2026
- **Heure** : 11 h 30 (point bi‑hebdomadaire)
- **Ordre du jour prévisionnel** :
  1. Retour sur les tests Nextcloud.
  2. Validation de la release 1.3.1 (code unique & numéro d’appel).
  3. Suivi du lancement du salon silencieux.
  4. Mise à jour du tableau d’estimation des tâches.

---

*Document rédigé par l’assistant IA, validé par les participants.*
