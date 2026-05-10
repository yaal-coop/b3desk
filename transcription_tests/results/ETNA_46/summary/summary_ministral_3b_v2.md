```markdown
# Compte rendu de réunion - Projets et suivi des jalons

## Participants
- Didier
- Hugo
- Benoît
- Simon
- Frédéric Cognès
- Nicolas
- Hugo (présent pour le point sur Tribu)
- Autres intervenants : Frédéric, Benoît, Johan, Sophie, François, Sophie, Paul Fouad, Mickaël, Benjamin, Aurélien, Nicolas (en formation), Frédéric, Johan, etc.

---

## Objet de la réunion
Retour d'expérience et suivi des projets en cours au sein de la DLE (Direction des Logiciels Éducatifs) et des comités associés.

---

## Durée estimée
Non précisée dans la transcription.

---

## Sujets abordés

### 1. Comité de domaine et réduction du budget
- **Réduction du budget** : Réduction budgétaire sur toute la DLE. Impact variable selon les projets, mais globalement indolore.
- **Suivi des jalons** : Audran insiste sur la nécessité d’améliorer la précision des dates de livraison des nouvelles fonctionnalités. Actuellement, les dates sont souvent des estimations ou des plages temporelles vagues (ex. "avant l'été").
- **Problématiques identifiées** :
  - Manque de visibilité sur les dates de livraison des fonctionnalités.
  - Dépendance aux éditeurs pour les versions majeures, avec des retards fréquents.
  - Nécessité d’améliorer la communication avec les prestataires pour obtenir des engagements plus réalistes.

### 2. Projets spécifiques
#### **Tribu**
- **Refonte graphique et UX** :
  - Chiffrage et planning en cours de validation. Trois lots identifiés :
    - Lot 1 : Accueil, tableaux de bord, dossiers (~80 jours).
    - Lot 2 : Outils et recherche.
    - Lot 3 : Administration.
  - Objectif : Mise en production prévue pour fin 2025, avec une version finalisée attendue pour fin d’année 2024.
  - Préparation des environnements de pré-production pour éviter les imprévus.

#### **Nuage (Nextcloud)**
- **Version 31** : Problème de régression fonctionnelle sur le partage de fichiers. Difficulté à déployer en production sans correction.
- **Migration académique** : Attente d’un correctif pour le script de migration. Nantes en pilote, mais migration académique reportée en attendant.
- **Optimisation des serveurs** : Ajout de 4 Go de RAM sur les serveurs de base de données, améliorant la stabilité. Planification d’une augmentation similaire sur les serveurs frontaux.

#### **BNA (Base Nationale des Agents)**
- **Décalage de la campagne** : Report du lancement de la campagne de juin au 27 juin pour éviter un chevauchement avec une autre enquête.

#### **Communication unifiée**
- **Problématique** : Choix des outils (Cisco, Webex, outils libres) et intégration avec CHAP pour une solution de téléphonie unifiée.
- **Démonstrateur** : Travail en cours pour intégrer BBB dans CHAP et les salles de vidéo.

#### **Vioja (BBB)**
- **Version 3.0** : Livrée depuis un mois, avec quelques fonctionnalités disparues (ex. sous-titrage manuel). Fonctionnalités comme la sélection aléatoire d’un participant sont désormais des plugins.
- **Demandes du CNET** : Intégration de fonctionnalités spécifiques comme la délégation de salles, en discussion pour priorisation et financement.

#### **Portail Apps**
- **Chiffres clés** :
  - 221 000 comptes ouverts (hors comptes directs).
  - 73 000 comptes actifs depuis décembre.
  - 80 000 vidéos sur le portail.
- **Améliorations** :
  - Installation de Matomo pour analyser les parcours utilisateurs.
  - Mise à jour 6.4.1 en production.
  - Travail sur le raccourcissement des URLs et l’architecture du cycle de vie des utilisateurs.

#### **Wi-Fi et bornes**
- **Questionnaire aux académies** : En attente des retours pour identifier les usages et problèmes liés aux bornes Wi-Fi.

#### **Messagerie (Aetna)**
- **Dépôt de la Corse** : Premier pilote complet en conditions réelles. Bilan :
  - Usages variés et parfois complexes après 20 ans d’utilisation de Convergence.
  - Nécessité d’accompagner le changement et d’adapter les processus.
  - Problèmes rencontrés (ex. boîtes aux lettres surchargées, 96 Go).
- **Migration académique** : Accélération prévue pour les pilotes (Nantes, Poitiers, Paca).

#### **Autres points**
- **Dotation et support** :
  - Étude des profils à doter en cours avec Frédéric.
  - Formation des équipes support en académies.
- **Comités et prochaines réunions** :
  - Comité des référents (mardi prochain, en distanciel).
  - Retour d’expérience Squash avec Tribu (à organiser avec Simon).
  - Réunion de lancement pour la migration de la messagerie en académie (fin juin).

---

## Décisions prises
1. **Précision des dates de livraison** :
   - Améliorer la communication avec les prestataires pour obtenir des engagements plus réalistes et des dates précises.
   - Établir une balance entre la communication avec la direction et le risque de ne pas livrer à temps.

2. **Tribu** :
   - Valider le chiffrage et le planning pour lancer les développements dès que possible.
   - Préparer les environnements de pré-production pour éviter les imprévus.

3. **Nuage** :
   - Attendre le correctif de Nextcloud pour la version 31 avant toute mise à jour majeure.
   - Surveiller attentivement les serveurs après l’ajout de RAM pour éviter les plantages.

4. **BNA** :
   - Décaler la campagne de juin au 27 juin pour éviter les chevauchements.

5. **Communication unifiée** :
   - Continuer les travaux d’intégration des outils (Cisco, BBB) avec CHAP.

6. **Vioja** :
   - Discuter en interne de la priorisation des demandes du CNET (ex. délégation de salles).
   - Explorer le développement de plugins pour des fonctionnalités spécifiques.

7. **Portail Apps** :
   - Finaliser le raccourcissement des URLs et l’architecture du cycle de vie des utilisateurs.

8. **Messagerie** :
   - Accélérer les déploiements pilotes (Nantes, Poitiers, Paca) et préparer l’accompagnement des académies.

---

## Questions en suspens
1. **Dates de livraison** :
   - Quand les prestataires pourront-ils fournir des dates précises pour les jalons en cours ?
   - Comment gérer les retards des éditeurs (ex. Nextcloud, Collaborat) ?

2. **Migration académique** :
   - Quand la migration académique de Nextcloud pourra-t-elle commencer après Nantes ?

3. **Délégation de salles dans Vioja** :
   - Comment prioriser et financer cette demande du CNET ?

4. **Wi-Fi** :
   - Quand les académies d’Île-de-France pourront-elles répondre au questionnaire sur les usages des bornes Wi-Fi ?

---

## Tâches à effectuer

| **Responsable**       | **Tâche**                                                                                     | **Échéance**          |
|-----------------------|-----------------------------------------------------------------------------------------------|-----------------------|
| Équipe Tribu         | Finaliser le chiffrage et lancer les développements pour la refonte graphique.               | Début juillet        |
| Frédéric (Nuage)      | Coordonner avec le support éditeur pour la correction de la version 31 de Nextcloud.         | Juin                  |
| Frédéric (Nuage)      | Surveiller les serveurs après l’ajout de RAM et préparer la montée en puissance.             | Fin juin              |
| Frédéric (BNA)        | Finaliser la communication et le traitement des données pour la campagne décalée.           | 27 juin               |
| Frédéric (Comms)      | Avancer sur l’intégration de BBB avec CHAP et les outils de téléphonie.                     | Juillet               |
| Frédéric (Vioja)      | Discuter avec Frédéric Cognès sur la priorisation des demandes du CNET.                      | Juin                  |
| Équipe Portail Apps  | Finaliser le raccourcissement des URLs et l’architecture du cycle de vie des utilisateurs.    | Juillet               |
| Frédéric (Messagerie) | Préparer l’accompagnement des académies pilotes (Nantes, Poitiers, Paca).                   | Juin                  |
| Frédéric (Wi-Fi)      | Relancer les académies d’Île-de-France pour obtenir leurs retours sur le questionnaire.       | Juin                  |
| Simon                | Organiser un retour d’expérience Squash avec Tribu.                                           | Prochain comité       |
| Frédéric (Comité)     | Préparer les slides pour le comité des référents (mardi prochain).                          | Avant mardi           |

---

## Prochaine rencontre
- **Comité des référents** : Mardi prochain (en distanciel).
- **Réunion de lancement de la migration de la messagerie** : Fin juin.
- **Réunion de suivi avec les académies pilotes** (Nantes, Poitiers, Paca) : Dates à confirmer.
```

Ce compte rendu est structuré pour refléter les points clés de la réunion tout en restant fidèle au contenu de la transcription. Les sections inutiles ou redondantes ont été supprimées pour garder une version concise et pertinente.
