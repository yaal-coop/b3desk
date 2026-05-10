# Compte rendu de réunion

**Date** : 4 mai 2026
**Durée estimée** : ~1 h 30

---

## Participants
| Nom | Rôle / Fonction |
|-----|-----------------|
| Johan | Animateur de la réunion |
| Bastien | Responsable de la présentation / PR |
| Benjamin | Développeur (B3Desk, migrations, tests) |
| Benoît | Responsable tests Nextcloud/Nuage, suivi budget |
| Mickaël | Responsable du backlog & chiffrage |
| (autres) | Participants ponctuels (ex. : interlocuteurs Arawa, Renater) |

---

## Objet de la réunion
1. Mettre en place un point de suivi bi‑hebdomadaire.
2. Faire le point sur les livrables récents (code unique, configuration BBB/ScaleLight, migration).
3. Traiter les incidents et tickets en cours (ticket 166, logs, instabilité Nextcloud/Nuage).
4. Valider le budget et le lancement du **salon silencieux** ainsi que le projet **SIP Media Gateway**.
5. Planifier la prochaine release (v1.3) et définir les estimations du backlog.

---

## Sujets abordés & décisions prises

| Sujet | Décision / Point clé |
|-------|----------------------|
| **Rythme de suivi** | Réunion toutes les 2 semaines, le **mercredi à 11 h 30**. Johan enverra l’invitation. |
| **Livraison du “code unique”** | Aucun développement supplémentaire côté Arawa ; il faut uniquement **modifier la configuration** (paramètre ScaleLight/BBB). Bastien ajoutera la précision dans la PR et la release notes. |
| **Scénario de test B3Desk** | Benjamin doit fournir un scénario de test détaillé (activation de la nouvelle option, vérification du PIN, etc.). |
| **BBB Dial Number** | Variable de configuration **`Dial Number`** à renseigner dans la config Métro‑Desk. Confirmation que l’affichage dépend de ce paramètre. |
| **Migrations** | L’ordre des migrations doit être respecté : **tri des salons → code unique**. Benjamin vérifiera que les fichiers de migration sont inclus dans la release et exécutés dans le bon ordre. |
| **Ticket 166 (erreur 500 salons)** | Résolu par Arawa (effacement d’un champ). La remontée de logs restera active dans la prochaine release. |
| **Instabilité Nextcloud/Nuage** | - Benjamin/Benoît poursuivent les captures de trafic et les tests de reproduction.<br>- Vérifier la version de la bibliothèque Python WebDAV et la mettre à jour si besoin.<br>- Envisager d’allonger la durée de validité du token (actuellement 30 j). |
| **Budget & lancement du salon silencieux** | Le devis est validé, le financement est disponible. Le salon silencieux peut être lancé immédiatement. |
| **Projet SIP Media Gateway** | Financement confirmé par la DGFIP. Développement côté B3Desk à prévoir (génération de liens SIP). |
| **Messagerie nationale & CIP** | Nécessité d’une réunion avec **Renater** pour cadrer les fonctionnalités possibles et les besoins de financement juridique. |
| **Plan de release** | - **Release 1.3** prévue **aujourd’hui à 14 h** (sans le numéro d’appel et le code unique).<br>- **Release 1.3.1** ultérieure pour intégrer ces deux éléments. |
| **Chiffrage du backlog** | Mickaël s’engage à fournir, d’ici la fin de journée, un tableau de correspondance **tags → estimation (heures/jours)**. |

---

## Questions en suspens
| Question | Responsable / Suivi |
|----------|---------------------|
| Nom exact du paramètre ScaleLight à modifier (pour la release). | Bastien (à préciser dans la PR). |
| Intégration du “code unique” dans la version 1.3 ou 1.3.1. | À confirmer avec Benoît. |
| Causes précises de l’instabilité Nextcloud/Nuage (charge serveur vs bibliothèque). | Benoît & Benjamin (tests complémentaires). |
| Support juridique pour le projet messagerie nationale. | À définir (contact à prendre avec l’équipe juridique). |
| Alignement des fonctionnalités CIP avec les développements Renater. | À planifier lors d’une réunion dédiée (à organiser). |

---

## Tâches à effectuer

| Action | Responsable | Échéance |
|--------|-------------|----------|
| Envoyer l’invitation du point bi‑hebdomadaire (mercredi 11 h 30). | **Johan** | Immédiate |
| Ajouter la description du paramètre de configuration ScaleLight/BBB dans la PR et les notes de release. | **Bastien** | Avant la release 1.3 |
| Fournir un scénario de test complet pour les changements B3Desk (activation, PIN, affichage). | **Benjamin** | Avant la fin de la semaine |
| Vérifier et garantir l’ordre des migrations dans la release. | **Benjamin** | Avant la release 1.3 |
| Conserver la remontée de logs du ticket 166 dans la prochaine release. | **Équipe dev** | Release 1.3 |
| Réaliser des captures de trafic et reproduire le problème Nextcloud/Nuage ; proposer mise à jour de la lib WebDAV. | **Benoît** (tests) & **Benjamin** (analyse) | 1 semaine |
| Prolonger la durée de validité du token applicatif (si besoin). | **Benjamin** | Après validation du besoin |
| Finaliser le tableau de correspondance **tags → estimation** (heures/jours). | **Mickaël** | Fin de journée |
| Organiser une réunion avec **Renater** pour le périmètre CIP. | **Johan** (coordination) | À planifier |
| Effectuer la release 1.3 à 14 h (pré‑release, tests). | **Équipe release** (Benjamin, Johan) | Aujourd’hui 14 h |
| Préparer la release 1.3.1 (code unique, numéro d’appel). | **Équipe dev** | Après validation du besoin |

---

## Prochaine rencontre
- **Date** : Mercredi 9 mai 2026
- **Heure** : 11 h 30
- **Objet** : Suivi des actions en cours, état des tests Nextcloud/Nuage, avancement du salon silencieux et du projet SIP Media Gateway, mise à jour du backlog.

---

*Fin du compte rendu.*
