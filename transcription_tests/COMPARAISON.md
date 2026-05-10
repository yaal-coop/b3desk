# Comparaison des outils de transcription SaaS

## Tarifs et free tier

Coûts mensuels estimés pour 10h/mois (usage modéré) et 50h/mois (usage intensif), hors free tier.

| Outil | Free tier | $/heure | 10h/mois | 50h/mois | Notes |
|-------|-----------|---------|----------|----------|-------|
| Albert (DINUM) | Gratuit, 1 000 req/jour | 0 | **0 $** | **0 $** | Souverain 🇫🇷 |
| Groq | 7 200 s/heure, 28 800 s/jour | 0,11 | **0 $** | **~6 $** | 10h/mois dans les limites du free tier si étalé |
| Soniox | Non documenté | 0,10 | **1 $** | **5 $** | Peu connu |
| AssemblyAI | 50 $ de crédits offerts | 0,15 | **1,50 $** | **7,50 $** | Couverts par les crédits offerts |
| pyannote.ai | 150h/mois (1er mois seulement) | 0,11 € | **~1 €** | **~5 €** | Orienté diarisation |
| Speechmatics | 2h/mois | 0,24 | **2 $** | **12 $** | 2h gratuites déduites — 🇬🇧 |
| ElevenLabs | Free tier limité | 0,22 | **2,20 $** | **11 $** | Principalement TTS |
| OpenAI | Aucun | 0,36 | **3,60 $** | **18 $** | Pas de free tier |
| Azure Speech | 5h/mois | 0,36 (batch) / 1,00 (realtime) | **1,80 $** | **16,20 $** | Batch — diarisation +0,30 $/h |
| Deepgram | 200 $ de crédits offerts | 0,46 | **4,60 $** | **23 $** | Crédits sans expiration |
| Gladia | 10h/mois | 0,61 (ou 0,20 avec engagement) | **0 $** | **24,40 $** | 10h gratuites déduites — 🇫🇷 |
| Amazon Transcribe | 60 min/mois (12 mois) | 1,44 | **12,96 $** | **70,56 $** | Écosystème AWS |
| Google Cloud STT | 60 min/mois | 1,44 | **12,96 $** | **70,56 $** | Modèle Chirp = le plus récent |
| Rev.ai | 45 min/mois | 0,18 | — | — | ❌ Écarté (bug langue FR) |
| Cartesia | — | 0,13 | — | — | ⚠️ Principalement TTS |
| Gemini (Google) | Free tier API | Variable | — | — | ⚠️ IA généraliste, pas un ASR dédié |

---

## Taille de fichier maximale

| Outil | Limite | Notes |
|-------|--------|-------|
| Albert (DINUM) | 20 MB | Limite du reverse proxy, pas prévu de l'augmenter |
| OpenAI Whisper | 25 MB | |
| Groq | 100 MB | |
| Gladia | 1 000 MB / 135 min | Très permissif |
| AssemblyAI | à vérifier | |
| Deepgram | à vérifier | |
| pyannote.ai | non documenté | |
| Amazon Transcribe | 2 GB / 4 heures | |
| Google Cloud STT | 10 MB (direct), illimité via GCS | Passer par Google Cloud Storage pour les gros fichiers |
| Azure Speech | 1 GB (batch), 25 MB (Whisper) | |
| Rev.ai | 2 GB (API), 5 TB (dashboard) | |
| Speechmatics | 1 GB / 2 heures | |
| ElevenLabs | à vérifier | |
| Soniox | à vérifier | |
| Cartesia | à vérifier | |

Nos fichiers de test : ETNA_46 = 18 MB, Reunion_Git_YAAL = 12 MB, video_0 = 8.6 MB.
Tous passent sous la limite d'Albert (20 MB) grâce au débit choisi (32 kbps).

---

## Diarisation (identification des locuteurs) = pas encore de tests probants sur cette partie

La diarisation permet de savoir *qui parle quand* dans une réunion — utile pour les comptes rendus.

| Outil | Diarisation | Locuteurs max | Notes |
|-------|-------------|---------------|-------|
| Albert | ❌ | — | |
| Groq | ❌ | — | |
| OpenAI | ❌ | — | |
| Gladia | ✅ | — | |
| AssemblyAI | ✅ | — | |
| Deepgram | ✅ | — | |
| pyannote.ai | ✅ | — | Spécialité principale de l'outil |
| Amazon Transcribe | ✅ | 5 | |
| Google Cloud STT | ✅ | Configurable | |
| Azure Speech | ✅ | Configurable | Facturée en supplément |
| Rev.ai | ✅ | Inclus | Inclus par défaut |
| Speechmatics | ✅ | — | + identification du locuteur entre sessions |
| ElevenLabs | ✅ | — | |
| Soniox | ✅ | 15 | |
| Cartesia | ❌ | — | Optimisé pour la latence, pas la diarisation |
| Gemini | ❌ | — | IA généraliste |

---

## Adaptabilité (facilité de changer d'outil)

L'adaptabilité mesure : si on veut remplacer un outil par un autre, combien de code faut-il réécrire ?

### Groupe 1 — Très facile à substituer entre eux

Albert, Groq, OpenAI

Ces outils parlent tous le même "langage" (API compatible OpenAI). Passer de l'un à l'autre = modifier **2 lignes** dans le code : l'adresse du serveur et la clé API. Le reste du code ne change pas.

```
# Exemple : passer d'Albert à Groq
- base_url="https://albert.api.etalab.gouv.fr/v1"
+ base_url="https://api.groq.com/openai/v1"
```

### Groupe 2 — Substituables entre eux, mais avec un peu plus de travail

AssemblyAI, Gladia, Amazon Transcribe, Rev.ai, Speechmatics, Soniox

Ces outils fonctionnent en 3 étapes (envoyer le fichier → attendre le traitement → récupérer le résultat). Le concept est le même mais le code est différent selon les outils. Passer de l'un à l'autre = réécrire environ 50 lignes.

### Groupe 3 — Indépendant, effort moyen

Deepgram, Google Cloud STT, Azure Speech, ElevenLabs

Envoient le fichier et reçoivent le résultat directement (pas d'attente pour certains modes). Le code est spécifique à chaque outil. Changer = réécrire environ 30 lignes.

### Groupe 4 — Plus difficile à substituer

pyannote.ai

Processus plus complexe (stockage intermédiaire sur Amazon S3, problèmes de connexion rencontrés). Orienté principalement vers l'identification des locuteurs, pas la transcription seule. Code plus fragile.

---

## Maintenance (facilité de faire fonctionner l'outil dans la durée)

| Outil | Python SDK officiel | Problèmes rencontrés | Évaluation |
|-------|---------------------|----------------------|------------|
| Albert | Non (on utilise le SDK OpenAI) | Aucun | ✅ Simple |
| Groq | Non (on utilise le SDK OpenAI) | Rate limit sur le free tier | ✅ Simple |
| OpenAI | Non (SDK OpenAI = la référence) | Pas de free tier | ✅ Simple |
| Gladia | Oui | Free tier de 10h/mois épuisé rapidement lors des tests répétés (402 Payment Required) | ✅ Simple |
| AssemblyAI | Oui | Paramètre `speech_models` mal documenté | ✅ Simple |
| Deepgram | Oui | Problème d'authentification (clé invalide lors du test) | ⚠️ À confirmer |
| pyannote.ai | Non | Erreur SSL (Python 3.14 / Amazon S3), résultat vide au 1er essai | ❌ Fragile |
| Amazon Transcribe | Oui (boto3) | Dépendance à l'écosystème AWS | ✅ Simple |
| Google Cloud STT | Oui (google-cloud-speech) | Dépendance à GCP | ✅ Simple |
| Azure Speech | Oui (azure-cognitiveservices-speech) | Dépendance à Azure | ✅ Simple |
| Rev.ai | Oui (rev-ai) | Free tier épuisé après 2 fichiers (45 min/mois). **Bug systématique** : transcription en anglais malgré `language: "fr"` — confirmé sur ETNA_46 v1 et v2 (35 mots en anglais chacune) et Reunion_Git_YAAL (91 mots en anglais) | ❌ Inutilisable en FR |
| Speechmatics | Oui (speechmatics-python) | Quota 2h/mois (Standard et Enhanced) épuisé par ETNA_46 seul | ⚠️ Quota très limité |
| ElevenLabs | Oui | Non testé | 🔲 Non testé |
| Soniox | Oui (soniox) | Non testé | 🔲 Non testé |
| Cartesia | Oui | Principalement TTS | ⚠️ Hors sujet |
| Gemini | Oui (google-generativeai) | Pas un ASR dédié | ⚠️ Détour inutile |

**Python SDK officiel** : certains outils fournissent une librairie Python qu'on installe une fois (`pip install assemblyai` par exemple) et qui gère les détails techniques à notre place. Sans ça, on code tout manuellement — si l'API du service évolue, on doit trouver et corriger le code soi-même.

---

## Souveraineté des données (RGPD)

Critère important pour un service public français.

| Niveau | Outils |
|--------|--------|
| 🟢 Souverain France — sous contrôle de l'État | Albert (DINUM) |
| 🟡 Entreprise européenne privée | Gladia 🇫🇷, Speechmatics 🇬🇧 |
| 🔴 Entreprise US (CLOUD Act) | Groq, OpenAI, AssemblyAI, Deepgram, Amazon, Google, Azure, Rev.ai, ElevenLabs, Soniox, Cartesia |

Le CLOUD Act américain oblige les entreprises US à fournir des données aux autorités américaines sur demande, même si les serveurs sont en Europe.

---

## Pertinence pour B3Desk

Critères : service public français, réunions en français, RGPD, intégration simple, diarisation utile.

| Outil | Pertinence | Raison principale |
|-------|-----------|-------------------|
| Albert | ⭐⭐⭐⭐⭐ | Souverain, gratuit, déjà intégré |
| Groq | ⭐⭐⭐⭐ | Très rapide, API simple, bon free tier |
| Gladia | ⭐⭐⭐⭐ | Diarisation + qualité + free tier + 🇫🇷 |
| Speechmatics | ⭐⭐⭐⭐ | Diarisation, qualité reconnue en FR — quota Enhanced très limité |
| Rev.ai | ⭐ | Bug systématique : transcription en anglais sur fichiers français (malgré `language: "fr"`) |
| AssemblyAI | ⭐⭐⭐ | Crédits généreux, diarisation |
| Deepgram | ⭐⭐⭐ | Synchrone, rapide (clé à corriger) |
| Azure Speech | ⭐⭐⭐ | Qualité, mais cher et diarisation payante en plus |
| Google Cloud STT | ⭐⭐⭐ | Qualité, mais cher et dépendance GCP |
| OpenAI | ⭐⭐ | Pas de free tier |
| Amazon Transcribe | ⭐⭐ | AWS lock-in, plus cher que les alternatives |
| ElevenLabs | ⭐⭐ | ASR secondaire, principalement TTS |
| Soniox | ⭐⭐ | Peu de retours d'expérience en FR |
| pyannote.ai | ⭐⭐ | Intégration fragile, free tier limité à 1 mois |
| Gemini | ⭐ | Pas un ASR dédié |
| Cartesia | ⭐ | TTS, pas ASR |

---

## Tests réalisés

| Outil | ETNA_46 | Reunion_Git_YAAL | video_0 | Notes |
|-------|---------|-----------------|---------|-------|
| Albert | ✅ | ✅ | ✅ | |
| Groq | ✅ | ✅ | ✅ | |
| OpenAI | ✅ | ✅ | ✅ | |
| Gladia | ✅ | ✅ | ✅ | |
| AssemblyAI | ✅ | ✅ | ✅ | |
| Deepgram | ✅ | ✅ | ✅ | |
| pyannote.ai | ✅ | ✅ | ✅ | Problèmes SSL lors du test |
| Rev.ai | ✅ | ✅ | ❌ | Free tier épuisé sur video_0 — **bug systématique : transcription en anglais sur les 2 fichiers testés** |
| Speechmatics | ✅ | ✅ | ✅ | |
| Amazon Transcribe | 🔲 | 🔲 | 🔲 | Non testé (setup cloud AWS complexe) |
| Google Cloud STT | 🔲 | 🔲 | 🔲 | Non testé (setup cloud GCP complexe) |
| Azure Speech | 🔲 | 🔲 | 🔲 | Non testé (setup cloud Azure complexe) |
| ElevenLabs | 🔲 | 🔲 | 🔲 | Non testé (principalement TTS, ASR secondaire) |
| Soniox | 🔲 | 🔲 | 🔲 | Non testé (peu documenté, peu de retours sur le français) |
| Cartesia | 🔲 | 🔲 | 🔲 | Non testé (principalement TTS) |
| Gemini | 🔲 | 🔲 | 🔲 | Non testé (pas un ASR dédié) |

Le résumé de toutes les transcriptions réalisées a été généré via Albert (`openai/gpt-oss-120b`).

---

## Résumé

| Outil | Taille max | Diarisation | Adaptabilité | Maintenance | Free tier | Souveraineté |
|-------|-----------|-------------|--------------|-------------|-----------|--------------|
| Albert | 20 MB | ❌ | ⭐⭐⭐ (groupe 1) | ✅ | ✅ Gratuit | 🟢 |
| Groq | 100 MB | ❌ | ⭐⭐⭐ (groupe 1) | ✅ | ✅ Limité | 🔴 |
| OpenAI | 25 MB | ❌ | ⭐⭐⭐ (groupe 1) | ✅ | ❌ Aucun | 🔴 |
| Gladia | 1 000 MB | ✅ | ⭐⭐ (groupe 2) | ✅ | ✅ 10h/mois | 🟡 |
| AssemblyAI | à vérifier | ✅ | ⭐⭐ (groupe 2) | ✅ | ✅ 50$ crédits | 🔴 |
| Deepgram | à vérifier | ✅ | ⭐⭐ (groupe 3) | ⚠️ | ✅ 200$ crédits | 🔴 |
| pyannote.ai | non documenté | ✅ | ⭐ (groupe 4) | ❌ | ✅ 150h/mois (1 mois) | 🔴 |
| Amazon Transcribe | 2 GB | ✅ | ⭐⭐ (groupe 2) | ✅ | ✅ 60min/mois | 🔴 |
| Google Cloud STT | 10 MB / illimité GCS | ✅ | ⭐⭐ (groupe 3) | ✅ | ✅ 60min/mois | 🔴 |
| Azure Speech | 1 GB | ✅ | ⭐⭐ (groupe 3) | ✅ | ✅ 5h/mois | 🔴 |
| Rev.ai | 2 GB | ✅ | ⭐⭐ (groupe 2) | ❌ | ✅ 45min/mois | 🔴 |
| Speechmatics | 1 GB | ✅ | ⭐⭐ (groupe 2) | ⚠️ | ✅ 2h/mois | 🟡 |
| ElevenLabs | à vérifier | ✅ | ⭐⭐ (groupe 3) | 🔲 | ✅ Limité | 🔴 |
| Soniox | à vérifier | ✅ | ⭐⭐ (groupe 2) | 🔲 | ❌ | 🔴 |
| Cartesia | à vérifier | ❌ | — | ⚠️ | — | 🔴 |
| Gemini | — | ❌ | — | ⚠️ | ✅ Limité | 🔴 |

---

## Régularité des transcriptions

Mesure la similarité entre deux runs successifs du même outil sur le même fichier (100% = résultat identique).
Calculée mot à mot avec `compare_regularity.py`.

| Vidéo | Outil | Versions | Similarité | Mots v1 | Notes |
|-------|-------|----------|-----------|---------|-------|
| ETNA_46 | Albert | 2 | v1↔v2 : 100.0% | 12 803 | Déterministe |
| ETNA_46 | AssemblyAI | 2 | v1↔v2 : 98.4% | 11 240 | |
| ETNA_46 | Deepgram | 3 | v1↔v2 : 99.9% / v2↔v3 : 99.8% | 11 088 | |
| ETNA_46 | Gladia | 2 | v1↔v2 : 100.0% | 12 773 | Déterministe |
| ETNA_46 | Groq | 2 | v1↔v2 : 87.3% | 12 795 | ⚠️ Variabilité notable sur long fichier — non-déterminisme normal de Whisper (614 blocs de substitutions mineures) |
| ETNA_46 | pyannote.ai | 2 | v1↔v2 : 89.0% | 8 851 | ⚠️ |
| ETNA_46 | Rev.ai | 2 | v1↔v2 : 100.0% | 35 | ❌ Bug systématique : v1 et v2 identiques à 35 mots en anglais — `language: "fr"` ignoré |
| ETNA_46 | OpenAI | 2 | v1↔v2 : 98.7% | 11 916 | |
| ETNA_46 | Speechmatics | 2 | v1↔v2 : 76.8% | 13 418 | ⚠️ v1 = enhanced, v2 = standard — modèles différents |
| Reunion_Git_YAAL | Albert | 2 | v1↔v2 : 100.0% | 4 980 | Déterministe |
| Reunion_Git_YAAL | AssemblyAI | 2 | v1↔v2 : 98.9% | 4 518 | |
| Reunion_Git_YAAL | Deepgram | 3 | v1↔v2 : 99.9% / v2↔v3 : 99.9% | 5 196 | |
| Reunion_Git_YAAL | Gladia | 2 | v1↔v2 : 100.0% | 4 879 | Déterministe |
| Reunion_Git_YAAL | Groq | 2 | v1↔v2 : 98.1% | 4 978 | |
| Reunion_Git_YAAL | pyannote.ai | 2 | v1↔v2 : 96.0% | 4 341 | |
| Reunion_Git_YAAL | OpenAI | 2 | v1↔v2 : 91.9% | 4 950 | ⚠️ Variabilité notable — non-déterminisme Whisper |
| Reunion_Git_YAAL | Rev.ai | 2 | v1↔v2 : 100.0% | 91 | ❌ Bug systématique : 91 mots en anglais — `language: "fr"` ignoré |
| video_0 | Albert | 2 | v1↔v2 : 100.0% | 4 809 | Déterministe |
| video_0 | AssemblyAI | 2 | v1↔v2 : 99.6% | 4 394 | |
| video_0 | Deepgram | 3 | v1↔v2 : 99.8% / v2↔v3 : 99.9% | 5 284 | |
| video_0 | Groq | 2 | v1↔v2 : 99.9% | 4 802 | |
| video_0 | Gladia | 2 | v1↔v2 : 100.0% | 4 745 | Déterministe |
| video_0 | OpenAI | 2 | v1↔v2 : 100.0% | 4 526 | Déterministe |
| video_0 | pyannote.ai | 2 | v1↔v2 : 88.8% | 3 762 | ⚠️ |

**Conclusions :**
- **Albert, Gladia, OpenAI** (video_0) : 100% déterministes — le même fichier donne exactement le même résultat
- **Deepgram et AssemblyAI** : très stables (≥ 98%)
- **OpenAI** : déterministe sur les fichiers courts, variable sur les longs (91.9% sur Reunion_Git_YAAL) — non-déterminisme Whisper sur les fichiers longs
- **Groq** : stable sur les fichiers courts, variable sur les longs (87% sur ETNA_46) — non-déterminisme normal de Whisper, pas un bug
- **pyannote.ai** : régularité moyenne (89–96%)
- **Rev.ai** : ❌ bug systématique — transcription en anglais sur tous les fichiers français testés (35 et 91 mots en anglais, identiques entre runs) — le paramètre `language: "fr"` est ignoré
- **Speechmatics** : comparaison non valide (modèles différents entre v1 et v2)

---

## Qualité des transcriptions sur les extraits

Comparaison outil par outil sur 3 extraits de nature différente.
Les outils testés : Albert, AssemblyAI, Groq, Deepgram, pyannote.ai, Speechmatics, Gladia (Rev.ai écarté — bug systématique).

### Albert
- **ETNA_46_extrait** (son moyen) : Très lisible, ponctuation correcte. Noms propres bien capturés. Erreurs : "DLE" au lieu de "DNE", "salons" au lieu de "jalons", "Técarat" au lieu de "T4".
- **ETNA_46_extrait2** (chiffres, voix superposées) : Chiffres bien capturés (221 000, 73 000, 11 instances). PeerTube et Framasoft reconnus. Erreurs : "Rancher de Créprod" pour pré-prod, "psychonomie des comptes" pour cycle de vie, "DRAP du Grand Est" (acronyme incertain), "podéduque d'intérieur d'Espace" pour Pod Education.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : Excellent. B3Desk, WebDAV, Nextcloud, Tchap, Renater, MTE tous corrects. "cinématique" bien rendu tout au long. Erreurs : "DGFIC" au lieu de "DGFIP", "CIP" au lieu de "SIP" à un endroit.

### AssemblyAI
- **ETNA_46_extrait** (son moyen) : Qualité similaire à Albert. Erreurs : "Olivier" au lieu de "Didier", "allants" au lieu de "agents/jalons", "testaments" au lieu de "prestataires", "Megzot" pour un outil non identifié.
- **ETNA_46_extrait2** (chiffres, voix superposées) : Bon niveau général. Erreurs notables : "Travissoft" au lieu de "Framasoft", "DRAM du Grand Est", "cyclonomie" pour cycle de vie, "ployer" pour "plugin". Chiffres bien capturés.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : Très bon. La cinématique technique (token, WebDAV, portail Apps) bien rendue. Erreurs : "DG FIQ" au lieu de "DGFIP", "Renata" au lieu de "Renater", "CNES West" pour un acronyme non identifié, "BetraDesk" à une reprise.

### Groq
- **ETNA_46_extrait** (son moyen) : Bon niveau, ponctuation correcte. Erreurs : "Mexico" pour un outil tiers (hallucination), "Plastas" pour "prestas", quelques coupures en milieu de phrase sur les passages difficiles.
- **ETNA_46_extrait2** (chiffres, voix superposées) : Capture les apartés ignorés par d'autres (discussion juillet, automatisation). Erreurs : "kertubes" pour instances PeerTube, "Tramasoft" pour Framasoft, "Crèpe-Rode" pour pré-prod. "psychonomie" identique à Albert — terme difficile pour tous les modèles Whisper.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : Meilleure capture des acronymes institutionnels : "DGFIP", "Renater", "MTE", "Tchap" tous corrects. Vocabulaire B3Desk bien maîtrisé. Erreur : "Rocket WebDAV" pour "requête WebDAV".

### Deepgram
- **ETNA_46_extrait** (son moyen) : Tout en minuscules, aucune ponctuation. Noms propres (Audran, DNE, Collabora) majoritairement absents ou déformés. Inutilisable directement pour un compte rendu.
- **ETNA_46_extrait2** (chiffres, voix superposées) : "youtube" pour PeerTube — erreur grave sur le nom central de l'extrait. "pramasoft" pour Framasoft. Nombreux trous sur les passages techniques. Les chiffres passent mieux que le reste.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : "next clave" pour Nextcloud, "web d'app"/"web d'av"/"web d'hab" pour WebDAV. Le projet SIP Media Gateway n'apparaît pas. L'audio plus clair n'améliore pas significativement le résultat.

### pyannote.ai
- **ETNA_46_extrait** (son moyen) : Mélange français/anglais envahissant — passages entiers rédigés en anglais ("There are many things that are changing functionality"). La qualité sonore moyenne met l'outil en échec. Inutilisable pour un compte rendu.
- **ETNA_46_extrait2** (chiffres, voix superposées) : Mélange français/anglais encore plus marqué. Capture les grandes thématiques mais les détails techniques sont perdus ou paraphrasés en anglais. PeerTube et Framasoft reconnus quand ils apparaissent en français.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : Nettement meilleur que sur les extraits ETNA — l'audio plus clair aide. Mélange français/anglais moins envahissant mais présent. "schématique" au lieu de "cinématique", "BGFI" pour "DGFIP". Utilisable partiellement, pas fiable.

### Speechmatics
- **ETNA_46_extrait** (son moyen) : Très bonne qualité. Noms propres bien capturés : Didier, Hugo, Benoît, Audran, Collabora, Nextcloud, régression v31. Échanges entre participants mieux restitués que les autres outils. Erreurs : "ADN" au lieu de "DNE", "Belvès" (nom de ville) au lieu de BBB/BVB, "placements" au lieu de "prestataires".
- **ETNA_46_extrait2** (chiffres, voix superposées) : Meilleure transcription de cet extrait parmi tous les outils. PeerTube correct partout, Framasoft correct, "raccourcisseur d'URL" correct, "Rancher de préprod" correct, DRAC du Grand Est correct, cycle de vie correctement rendu. Capture les apartés ignorés par les autres (discussion 14 juillet). Erreurs : "VOD" pour Pod Education, "portail ATS" pour portail Apps, "73 zéro zéro zéro" pour 73 000.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : Contenu très complet. WebDAV, cinématique, DGFIP, MTE corrects. B3Desk rendu de façon incohérente selon les passages ("B3, DESC", "B 3D", "bêtes froides"). "Reynaert" pour Renater, "chap" sans T initial pour Tchap.

### Gladia
- **ETNA_46_extrait** (son moyen) : Bonne lisibilité, ponctuation correcte. DNE bien rendu. "jalons" transcrit "salons" (même erreur qu'Albert). Collabora rendu de façon incohérente ("Colabora", "Collaborac", "Colaborat"). BBB transcrit tantôt "BBB", tantôt "B2B", "BNB" — inconstant.
- **ETNA_46_extrait2** (chiffres, voix superposées) : Chiffres corrects (221 000, 73 000). Framasoft correct. PeerTube très incohérent ("FairTube", "Pierre Tube", "tiers tubes"). "raccourcisseur d'URL" rendu "raccourci sort du rm" — erreur grave. "psychonomie" pour cycle de vie, identique aux autres modèles Whisper.
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : B3Desk, WebDAV, Nextcloud, Tchap, Renater, cinématique, MTE bien rendus. "DGFIP" transcrit "DGFILM" — erreur. "SIP Media Gateway" correct.

### OpenAI (whisper-1)
- **ETNA_46_extrait** (son moyen) : Bonne lisibilité, ponctuation correcte. Audran correct. Collabora correct. "DLE" au lieu de "DNE". "jalons" bien rendu dans l'ensemble mais une fois transcrit en "agents". BBB rendu "BVB" à une reprise. Qualité similaire à Albert.
- **ETNA_46_extrait2** (chiffres, voix superposées) : Chiffres corrects (221 000, 73 000). Framasoft correct. PeerTube très incohérent ("l'tube", "tiers-tubes", "faire tube", "PierreTube"). "DRAM du Grand Est" au lieu de "DRAC". "cyclonomie" pour cycle de vie (Whisper). "Tradeprod" au lieu de "pré-prod".
- **video_0_extrait** (son clair, vocabulaire B3Desk/SIP) : B3Desk, WebDAV, Nextcloud, Tchap, cinématique, MTE corrects. "DGFIC" au lieu de "DGFIP". "Renataire" au lieu de "Renater". "SIP Media Gateway" correct. Transcription sans majuscules ni ponctuation en début de segment — moins lisible que les autres Whisper.

---

## Comptes-rendus automatiques

Actuellement : Albert API, modèle `openai/gpt-oss-120b`, temperature 0.3.

### LLMs candidats

| LLM | Fournisseur | Contexte | Coût | Souveraineté | Notes |
|-----|-------------|----------|------|--------------|-------|
| `openai/gpt-oss-120b` *(actuel)* | Albert (DINUM) | 128k | Gratuit | 🟢 | Meilleur modèle disponible sur Albert |
| `mistralai/Mistral-Small-3.2-24B` | Albert (DINUM) | 128k | Gratuit | 🟢 | |
| `mistralai/Ministral-3-8B` | Albert (DINUM) | 256k | Gratuit | 🟢 | Plus léger, plus rapide |
| `Qwen/Qwen3-Coder-30B` | Albert (DINUM) | 256k | Gratuit | 🟡 | Orienté code (Alibaba), souveraineté incertaine |
| Mistral API (direct) | Mistral AI | variable | Payant | 🟡 | Entreprise européenne privée |
| Groq LLM (Llama, Gemma…) | Groq | variable | Free tier | 🔴 | ❌ Free tier inutilisable : limite TPM trop basse (6k–12k selon modèle) pour une transcription longue (~20k tokens) |
| OpenAI GPT-4o-mini | OpenAI | 128k | Payant | 🔴 | ✅ Testé |
| OpenAI GPT-4o | OpenAI | 128k | Payant | 🔴 | ✅ Testé |
| Anthropic Claude Haiku | Anthropic | 200k | Payant | 🔴 | ✅ Testé (`claude-haiku-4-5-20251001`) |
| Anthropic Claude Sonnet | Anthropic | 200k | Payant | 🔴 | ✅ Testé (`claude-sonnet-4-6`) |
| Mistral API (direct) | Mistral AI | 128k | Payant | 🟡 | ✅ Testé (`mistral-small-latest`, `mistral-large-latest`) |
| Cohere Command R | Cohere | 128k | Free tier | 🔴 | Bon sur les résumés longs — clé à créer |
| Together AI | Together AI | variable | Free tier | 🔴 | Accès à Llama, Qwen, Mistral… — clé à créer |
| Google Gemini Flash | Google | 1M | Free tier | 🔴 | Free tier généreux — clé à créer |
| AssemblyAI LeMUR | AssemblyAI | variable | Payant | 🔴 | ❌ Réservé aux comptes avec facturation active — non disponible sur le free tier |
| Ollama (local) | — | selon modèle | Gratuit | 🟢 | 100 % souverain, qualité variable selon le modèle |

### Questions ouvertes

- Quelle transcription utiliser comme référence pour comparer les résumés ? video ETNA_46 transcription par Albert.
- Critères d'évaluation : pertinence, structure, fidélité aux faits, longueur, pertinence comparative de contenu ?


### LLMs testés

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

### Comparaison des résumés

Analyse réalisée des 10 CR basés sur la même transcription source : `transcription_albert.txt`.

Critères : respect du format, couverture des sujets, erreurs factuelles, hallucinations, concision.

#### Erreurs et hallucinations détectées

| LLM | Problème |
|-----|---------|
| `openai/gpt-oss-120b` (Albert) | Aucune erreur claire détectée. "portail RL" en prochaine rencontre est suspect (absent des autres CR) mais non confirmé |
| `mistralai/Mistral-Small-3.2-24B-Instruct-2506` (Albert) | "Cine des Yéhouètes" — hallucination répétée (v2 et v3) |
| `gpt-4o` | "Sydney Gateway" — hallucination (passerelle SIP Janus Gateway) ; "Intégration de BBB dans Cap Education" — devrait être DBV ; "Benoît" listé deux fois |
| `mistral-small-latest` (API) | "Sydney Gateway" — même hallucination que GPT-4o ; 80 000 vidéos (Tube) attribuées au Portail Apps |
| `gpt-4o-mini` | "Décalage d'un mois" pour BNA — faux (10-12 jours) |
| `mistral-large-latest` (API) | "DNA" au lieu de BNA ; "BGB" au lieu de BBB ; prochaine rencontre déclarée "non spécifiée" à tort |
| `mistralai/Ministral-3-8B-Instruct-2512` (Albert) | Rancher "livraison en attente" — faux (livré mais non fonctionnel) |
| `Qwen/Qwen3-Coder-30B-A3B-Instruct` (Albert) | "10 juillet à 13h00" pour prochaine réunion — non sourcé |
| `claude-haiku-4-5-20251001` | Inclut du bruit ASR sans filtrage ("10 400 caminos", "Côte-Saint-Francis", "Procat") |
| `claude-sonnet-4-6` | "Côté Francis (antispam)" — terme garbled non filtré |

#### Respect de la consigne de format

Trois modèles encapsulent leur réponse dans un bloc ` ```markdown ``` ` malgré l'instruction explicite du prompt :

- `mistralai/Mistral-Small-3.2-24B-Instruct-2506` (Albert)
- `mistralai/Ministral-3-8B-Instruct-2512` (Albert)
- `mistral-large-latest` (API)

#### Classement

| Rang | LLM | Motif |
|------|-----|-------|
| 1 | `openai/gpt-oss-120b` (Albert) | Meilleur équilibre couverture/concision, peu d'erreurs |
| 2 | `claude-sonnet-4-6` | Le plus exhaustif, table des tâches utile, mais trop verbeux |
| 3 | `mistral-small-latest` (API) | Bon format, couverture correcte, mais erreurs factuelles |
| 4 | `claude-haiku-4-5-20251001` | Bonne couverture, filtre insuffisant du bruit ASR |
| 5 | `gpt-4o` | Couverture incomplète, hallucination "Sydney Gateway" |
| 6 | `mistralai/Ministral-3-8B-Instruct-2512` (Albert) | Format incorrect, erreur sur Rancher, trop verbeux |
| 7 | `mistral-large-latest` (API) | Acronymes faux, format incorrect, prochaine rencontre absente |
| 8 | `gpt-4o-mini` | Trop court, erreur sur la durée du décalage BNA |
| 9 | `mistralai/Mistral-Small-3.2-24B-Instruct-2506` (Albert) | Hallucination répétée, format incorrect |
| 10 | `Qwen/Qwen3-Coder-30B-A3B-Instruct` (Albert) | Le plus incomplet, manque l'essentiel |

#### Conclusion

Le modèle `openai/gpt-oss-120b` via Albert produit le meilleur CR dans ce contexte : couverture solide, structure claire, concision sans lacunes majeures — et c'est le seul outil gratuit et souverain du classement.

`claude-sonnet-4-6` est le plus exhaustif mais produit un document trop long pour un usage pratique sans relecture. Les deux meilleurs modèles payants/non-souverains (Sonnet et Mistral Small direct) n'apportent pas un gain suffisant pour justifier leur coût et leur statut RGPD dans ce cas d'usage.
