# 1 - Bilan des outils testés — transcription

Synthèse des outils effectivement testés dans le cadre du POC.

## 1.1 - Adaptabilité (facilité de changer d'outil)

L'adaptabilité mesure : si on veut remplacer un outil par un autre, combien de code faut-il réécrire ?

### 1.1.1 - Groupe 1 — Très facile à substituer entre eux

Albert, Groq, OpenAI

Ces outils parlent tous le même "langage" (API compatible OpenAI). Passer de l'un à l'autre = modifier **2 lignes** dans le code : l'adresse du serveur et la clé API. Le reste du code ne change pas.

### 1.1.2 - Groupe 2 — Substituables entre eux, mais avec un peu plus de travail

AssemblyAI, Gladia, Rev.ai, Speechmatics

Ces outils fonctionnent en 3 étapes (envoyer le fichier → attendre le traitement → récupérer le résultat). Le concept est le même mais le code est différent selon les outils. Un changement implique une modification importante du code.

### 1.1.3 - Groupe 3 — Indépendant, effort moyen

Deepgram

Envoie le fichier et reçoit le résultat directement (pas d'attente asynchrone). Le code est spécifique à l'outil. Un changement implique une modification importante du code.

### 1.1.4 - Groupe 4 — Plus difficile à substituer

pyannote.ai

Processus plus complexe (stockage intermédiaire sur Amazon S3). Orienté principalement vers l'identification des locuteurs, pas la transcription seule. Difficile à remplacer et plus coûteux à maintenanir.

---

## 1.2 - Maintenance (facilité de faire fonctionner l'outil dans la durée)

### 1.2.1 - Groupe 1 — Simple

Albert, Groq, OpenAI, Gladia, AssemblyAI, Deepgram, Speechmatics, Rev.ai

Aucun problème structurel. Albert, Groq et OpenAI s'appuient sur le SDK OpenAI (pas de SDK dédié) ; Gladia, AssemblyAI, Deepgram, Speechmatics et Rev.ai fournissent leur propre SDK officiel.

### 1.2.2 - Groupe 2 — Lourd à maintenir

pyannote.ai

Pas de SDK officiel : tout changement d'API implique de trouver et corriger le code manuellement. Dépendance à Amazon S3 comme stockage intermédiaire : une infrastructure tierce supplémentaire à maintenir.

---

## 1.3 - Souveraineté des données (RGPD)

| Niveau | Outils |
|--------|--------|
| 🟢 Souverain France — sous contrôle de l'État | Albert (DINUM) |
| 🟡 Entreprise européenne privée | Gladia 🇫🇷, Speechmatics 🇬🇧 |
| 🔴 Entreprise US (CLOUD Act) | Groq, OpenAI, AssemblyAI, Deepgram, Rev.ai |

---

## 1.4 - Résumé

Tarif = coût mensuel estimé pour 50h/mois (usage intensif), hors free tier.

Nos fichiers de test : ETNA_46 = 18 MB, Reunion_Git_YAAL = 12 MB, video_0 = 8.6 MB.
Tous passent sous la limite d'Albert (20 MB) grâce au débit choisi (32 kbps).

| Outil | Taille max | Adaptabilité | Maintenance | Tarif | Souveraineté |
|-------|-----------|--------------|-------------|-------|--------------|
| Albert | 20 MB | groupe 1 | groupe 1 | 0 $ | 🟢 |
| Groq | 100 MB | groupe 1 | groupe 1 | ~6 $ | 🔴 |
| OpenAI | 25 MB | groupe 1 | groupe 1 | 18 $ | 🔴 |
| Gladia | 1 000 MB | groupe 2 | groupe 1 | 24,40 $ | 🟡 |
| AssemblyAI | 2.2 GB | groupe 2 | groupe 1 | 7,50 $ | 🔴 |
| Deepgram | 2 GB | groupe 3 | groupe 1 | 23 $ | 🔴 |
| pyannote.ai | 1 GB | groupe 4 | groupe 2 | ~5 € | 🔴 |
| Rev.ai | 2 GB | groupe 2 | groupe 1 | — | 🔴 |
| Speechmatics | 1 GB | groupe 2 | groupe 1 | 12 $ | 🟡 |

---

## 1.5 - Régularité des transcriptions

Mesure la similarité entre deux runs successifs du même outil sur le même fichier (100% = résultat identique).

- **Albert, Gladia, OpenAI** (video_0) : 100% déterministes — le même fichier donne exactement le même résultat
- **Deepgram, AssemblyAI et Speechmatics** : très stables (≥ 97%)
- **OpenAI** : déterministe sur les fichiers courts, variable sur les longs (91.9% sur Reunion_Git_YAAL) — non-déterminisme Whisper sur les fichiers longs
- **Groq** : stable sur les fichiers courts, variable sur les longs (87% sur ETNA_46) — non-déterminisme normal de Whisper, pas un bug
- **pyannote.ai** : régularité moyenne (89–96%)
- **Rev.ai** : ❌ bug systématique — transcription en anglais sur tous les fichiers français testés (35 et 91 mots en anglais, identiques entre runs) — le paramètre `language: "fr"` est ignoré

---

## 1.6 - Qualité des transcriptions sur les extraits

Comparaison outil par outil sur 3 extraits de nature différente.
Les outils testés : Albert, AssemblyAI, Groq, Deepgram, pyannote.ai, Speechmatics, Gladia (Rev.ai écarté — bug systématique).

### 1.6.1 - Albert
- **ETNA_46_extrait** (son moyen) : Très lisible, ponctuation correcte. Noms propres bien capturés. Erreurs : "DLE" au lieu de "DNE", "salons" au lieu de "jalons", "Técarat" au lieu de "T4".
- **ETNA_46_extrait2** (chiffres, voix superposées) : Chiffres bien capturés (221 000, 73 000, 11 instances). PeerTube et Framasoft reconnus. Erreurs : "Rancher de Créprod" pour pré-prod, "psychonomie des comptes" pour cycle de vie, "DRAP du Grand Est" (acronyme incertain), "podéduque d'intérieur d'Espace" pour Pod Education.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : Excellent. B3Desk, WebDAV, Nextcloud, Tchap, Renater, MTE tous corrects. "cinématique" bien rendu tout au long. Erreurs : "DGFIC" au lieu de "DGFIP", "CIP" au lieu de "SIP" à un endroit.

### 1.6.2 - AssemblyAI
- **ETNA_46_extrait** (son moyen) : Qualité similaire à Albert. Erreurs : "Olivier" au lieu de "Didier", "allants" au lieu de "agents/jalons", "testaments" au lieu de "prestataires", "Megzot" pour un outil non identifié.
- **ETNA_46_extrait2** (chiffres, voix superposées) : Bon niveau général. Erreurs notables : "Travissoft" au lieu de "Framasoft", "DRAM du Grand Est", "cyclonomie" pour cycle de vie, "ployer" pour "plugin". Chiffres bien capturés.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : Très bon. La cinématique technique (token, WebDAV, portail Apps) bien rendue. Erreurs : "DG FIQ" au lieu de "DGFIP", "Renata" au lieu de "Renater", "CNES West" pour un acronyme non identifié, "BetraDesk" à une reprise.

### 1.6.3 - Groq
- **ETNA_46_extrait** (son moyen) : Bon niveau, ponctuation correcte. Erreurs : "Mexico" pour un outil tiers (hallucination), "Plastas" pour "prestas", quelques coupures en milieu de phrase sur les passages difficiles.
- **ETNA_46_extrait2** (chiffres, voix superposées) : Capture les apartés ignorés par d'autres (discussion juillet, automatisation). Erreurs : "kertubes" pour instances PeerTube, "Tramasoft" pour Framasoft, "Crèpe-Rode" pour pré-prod. "psychonomie" identique à Albert — terme difficile pour tous les modèles Whisper.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : Meilleure capture des acronymes institutionnels : "DGFIP", "Renater", "MTE", "Tchap" tous corrects. Vocabulaire B3Desk bien maîtrisé. Erreur : "Rocket WebDAV" pour "requête WebDAV".

### 1.6.4 - Deepgram
- **ETNA_46_extrait** (son moyen) : Tout en minuscules, aucune ponctuation. Noms propres (Audran, DNE, Collabora) majoritairement absents ou déformés. Inutilisable directement pour un compte rendu.
- **ETNA_46_extrait2** (chiffres, voix superposées) : "youtube" pour PeerTube — erreur grave sur le nom central de l'extrait. "pramasoft" pour Framasoft. Nombreux trous sur les passages techniques. Les chiffres passent mieux que le reste.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : "next clave" pour Nextcloud, "web d'app"/"web d'av"/"web d'hab" pour WebDAV. Le projet SIP Media Gateway n'apparaît pas. L'audio plus clair n'améliore pas significativement le résultat.

### 1.6.5 - pyannote.ai
- **ETNA_46_extrait** (son moyen) : Mélange français/anglais envahissant — passages entiers rédigés en anglais ("There are many things that are changing functionality"). La qualité sonore moyenne met l'outil en échec. Inutilisable pour un compte rendu.
- **ETNA_46_extrait2** (chiffres, voix superposées) : Mélange français/anglais encore plus marqué. Capture les grandes thématiques mais les détails techniques sont perdus ou paraphrasés en anglais. PeerTube et Framasoft reconnus quand ils apparaissent en français.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : Nettement meilleur que sur les extraits ETNA — l'audio plus clair aide. Mélange français/anglais moins envahissant mais présent. "schématique" au lieu de "cinématique", "BGFI" pour "DGFIP". Utilisable partiellement, pas fiable.

### 1.6.6 - Speechmatics
- **ETNA_46_extrait** (son moyen) : Très bonne qualité. Noms propres bien capturés : Didier, Hugo, Benoît, Audran, Collabora, Nextcloud, régression v31. Échanges entre participants mieux restitués que les autres outils. Erreurs : "ADN" au lieu de "DNE", "Belvès" (nom de ville) au lieu de BBB/BVB, "placements" au lieu de "prestataires".
- **ETNA_46_extrait2** (chiffres, voix superposées) : Meilleure transcription de cet extrait parmi tous les outils. PeerTube correct partout, Framasoft correct, "raccourcisseur d'URL" correct, "Rancher de préprod" correct, DRAC du Grand Est correct, cycle de vie correctement rendu. Capture les apartés ignorés par les autres (discussion 14 juillet). Erreurs : "VOD" pour Pod Education, "portail ATS" pour portail Apps, "73 zéro zéro zéro" pour 73 000.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : Contenu très complet. WebDAV, cinématique, DGFIP, MTE corrects. B3Desk rendu de façon incohérente selon les passages ("B3, DESC", "B 3D", "bêtes froides"). "Reynaert" pour Renater, "chap" sans T initial pour Tchap.

### 1.6.7 - Gladia
- **ETNA_46_extrait** (son moyen) : Bonne lisibilité, ponctuation correcte. DNE bien rendu. "jalons" transcrit "salons" (même erreur qu'Albert). Collabora rendu de façon incohérente ("Colabora", "Collaborac", "Colaborat"). BBB transcrit tantôt "BBB", tantôt "B2B", "BNB" — inconstant.
- **ETNA_46_extrait2** (chiffres, voix superposées) : Chiffres corrects (221 000, 73 000). Framasoft correct. PeerTube très incohérent ("FairTube", "Pierre Tube", "tiers tubes"). "raccourcisseur d'URL" rendu "raccourci sort du rm" — erreur grave. "psychonomie" pour cycle de vie, identique aux autres modèles Whisper.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : B3Desk, WebDAV, Nextcloud, Tchap, Renater, cinématique, MTE bien rendus. "DGFIP" transcrit "DGFILM" — erreur. "SIP Media Gateway" correct.

### 1.6.8 - OpenAI (whisper-1)
- **ETNA_46_extrait** (son moyen) : Bonne lisibilité, ponctuation correcte. Audran correct. Collabora correct. "DLE" au lieu de "DNE". "jalons" bien rendu dans l'ensemble mais une fois transcrit en "agents". BBB rendu "BVB" à une reprise. Qualité similaire à Albert.
- **ETNA_46_extrait2** (chiffres, voix superposées) : Chiffres corrects (221 000, 73 000). Framasoft correct. PeerTube très incohérent ("l'tube", "tiers-tubes", "faire tube", "PierreTube"). "DRAM du Grand Est" au lieu de "DRAC". "cyclonomie" pour cycle de vie (Whisper). "Tradeprod" au lieu de "pré-prod".
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : B3Desk, WebDAV, Nextcloud, Tchap, cinématique, MTE corrects. "DGFIC" au lieu de "DGFIP". "Renataire" au lieu de "Renater". "SIP Media Gateway" correct. Transcription sans majuscules ni ponctuation en début de segment — moins lisible que les autres Whisper.

## 1.7 - Classement des meilleurs résultats (Transciption)

| Rang | Outil | Motif |
|------|-------|-------|
| 1 | Speechmatics | Meilleur sur l'audio difficile (chiffres, voix superposées) — PeerTube, Framasoft, "raccourcisseur d'URL", Rancher, DRAC tous corrects |
| 2 | Albert | Très lisible, ponctuation correcte, vocabulaire B3Desk maîtrisé — résultats constants sur les 3 extraits. Souverain et gratuit |
| 3 | Groq | Meilleure capture des acronymes institutionnels sur audio clair (DGFIP, Renater, MTE, Tchap tous corrects) — moins régulier sur fichiers longs |
| 4 | AssemblyAI | Niveau similaire à Albert, quelques erreurs sur les noms propres |

---
# 2 - Bilan des outils testés — comptes-rendus

## 2.1 - Évolution du prompt

**Prompt** :

Le prompt a été retravaillé à plusieurs reprises afin d'obtenir des résultats plus qualitatifs et homogènes avec des règles d'organisation en vue d'une génération sous contrainte.
Ces contraintes ont aussi permis de faciliter la comparaison des résultats.

```
Tu es un assistant spécialisé dans la rédaction de comptes rendus de réunion.

À partir de la transcription ci-dessous, rédige un compte rendu en markdown avec exactement ces sections (dans cet ordre, uniquement si le contenu est présent) :
- Participants
- Objet de la réunion
- Sujets abordés
- Décisions prises
- Questions en suspens
- Tâches à effectuer (responsable si mentionné)
- Prochaine rencontre

Règles strictes :
- N'inclus que des informations explicitement présentes dans la transcription.
- N'invente aucun chiffre, date, nom ou durée absent de la transcription.
- Si une information est incertaine ou mal audible, ne l'inclus pas.
- Réponds directement en markdown, sans encapsuler dans un bloc de code.

Transcription :
{transcription}

```

---

## 2.2 - LLMs testés

| LLM | Fournisseur | Payant/gratuit | Souveraineté |
|-----|-------------|----------------|--------------|
| `openai/gpt-oss-120b` | Albert (DINUM) | Gratuit | 🟢 |
| `mistralai/Mistral-Small-3.2-24B-Instruct-2506` | Albert (DINUM) | Gratuit | 🟢 |
| `mistralai/Ministral-3-8B-Instruct-2512` | Albert (DINUM) | Gratuit | 🟢 |
| `Qwen/Qwen3-Coder-30B-A3B-Instruct` | Albert (DINUM) | Gratuit | 🟢 |
| `gpt-4o-mini` | OpenAI | Payant | 🔴 |
| `gpt-4o` | OpenAI | Payant | 🔴 |
| `claude-haiku-4-5-20251001` | Anthropic | Payant | 🔴 |
| `claude-sonnet-4-6` | Anthropic | Payant | 🔴 |
| `mistral-small-latest` | Mistral AI | Payant | 🟡 |
| `mistral-large-latest` | Mistral AI | Payant | 🟡 |

---

## 2.3 - Comparaison des résumés

Analyse réalisée des 10 CR basés sur la même transcription source : `transcription_albert.txt`.

Critères : respect du format, couverture des sujets, erreurs factuelles, hallucinations, concision.

### 2.3.1 - Erreurs et hallucinations détectées

#### 2.3.1.1 - `openai/gpt-oss-120b` (Albert)

Aucune erreur claire détectée.

#### 2.3.1.2 - `mistralai/Mistral-Small-3.2-24B-Instruct-2506` (Albert)

Invente "Cine des Yéhouètes" (pour SIPMediaGW) comme projet mentionné dans la réunion.

#### 2.3.1.3 - `gpt-4o`

Invente "Sydney Gateway" (pour SIPMediaGW) comme nom d'un composant technique. Confond l'intégration de DBV dans Cap Education avec une "intégration de BBB" (BBB est l'outil de visioconférence, DBV est le module intégré). Liste "Benoît" deux fois dans les participants.

#### 2.3.1.4 - `mistral-small-latest` (API)

Invente "Sydney Gateway" (pour SIPMediaGW). Attribue au Portail Apps les 80 000 vidéos qui appartiennent à Tube (PeerTube) — deux projets distincts.

#### 2.3.1.5 - `gpt-4o-mini`

Indique que la campagne BNA a été décalée "d'un mois" — faux, le décalage est de 10 à 12 jours (du 16 au 27-28 juin).

#### 2.3.1.6 - `mistral-large-latest` (API)

Confond les acronymes : écrit "DNA" au lieu de "BNA" (Baromètre National d'Accompagnement) et "BGB" au lieu de "BBB" (BigBlueButton). Indique qu'aucune prochaine rencontre n'est mentionnée dans la transcription — faux, plusieurs réunions y sont planifiées.

#### 2.3.1.7 - `mistralai/Ministral-3-8B-Instruct-2512` (Albert)

Indique que le Rancher de pré-prod est "en attente de livraison" — faux, il a été livré mais n'est pas encore fonctionnel.

#### 2.3.1.8 - `Qwen/Qwen3-Coder-30B-A3B-Instruct` (Albert)

Indique que la prochaine réunion est prévue "le 10 juillet à 13h00" — cette heure n'est pas mentionnée dans la transcription (les autres CR évoquent une mise à jour du portail "le 10 juillet à midi", pas une réunion).

#### 2.3.1.9 - `claude-haiku-4-5-20251001`

Recopie du bruit de transcription sans le filtrer : "10 400 caminos envoyés" (mot incompréhensible issu d'une mauvaise transcription), "Côte-Saint-Francis" (déformation d'un nom de lieu), "Procat" (terme non identifiable).

#### 2.3.1.10 - `claude-sonnet-4-6`

Recopie "Côté Francis (antispam)" — "Francis" est une déformation issue de la transcription automatique.

### 2.3.2 - Respect de la consigne de format

Le prompt demandait explicitement de ne pas encapsuler la réponse dans un bloc de code. Trois modèles ont ignoré cette consigne : `mistralai/Mistral-Small-3.2-24B-Instruct-2506` (Albert), `mistralai/Ministral-3-8B-Instruct-2512` (Albert) et `mistral-large-latest` (API).

## 2.4 - Classement des meilleurs résultats (Compte-rendu)

Ce classement n'est qu'indicatif, car les outils testés permettent tous de générer un contenu de qualité suffisante pour un résumé clair et concis.

| Rang | LLM | Taille | Motif |
|------|-----|--------|-------|
| 1 | `openai/gpt-oss-120b` (Albert) | 4 459 car. | Meilleur équilibre couverture/concision, peu d'erreurs |
| 2 | `claude-sonnet-4-6` | 12 388 car. | Le plus exhaustif, table des tâches utile, mais trop verbeux |
| 3 | `mistral-small-latest` (API) | 4 570 car. | Bon format, couverture correcte, mais erreurs factuelles |
| 4 | `claude-haiku-4-5-20251001` | 7 392 car. | Bonne couverture, filtre insuffisant du bruit ASR |
