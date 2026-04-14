# Phase 2: Designing the Simulation

## Data Flow Map (Input -> Process -> Output)

### 1. Input: User Preferences

- User provides baseline preferences: genre, mood, target_energy, and acousticness preference.
- User can optionally provide target_tempo_bpm, target_danceability, and target_valence.
- User profile also includes scoring settings:
	- feature_weights (importance per feature)
	- feature_sigmas (tolerance for numeric distance in Gaussian scoring)

### 2. Process: Score Every Song in the Catalog

For each song in the CSV:

1. Compare song categorical fields to the user profile:
	 - genre match score
	 - mood match score
2. Compare song numeric fields to user targets with Gaussian closeness scoring:

$$
s_f = e^{-\frac{(x_f - p_f)^2}{2\sigma_f^2}}
$$

Where:

- $x_f$ = song value for feature $f$
- $p_f$ = user target for feature $f$
- $\sigma_f$ = tolerance for feature $f$
- $s_f$ = feature match score in [0, 1]

3. Multiply each feature score by its feature weight.
4. Sum all weighted feature scores to get one song relevance value:

$$
R = \sum_i w_i s_i
$$

### 3. Output: Ranking and Top K Recommendations

- Sort all songs by relevance score $R$ from highest to lowest.
- Return the top $k$ songs as recommendations.
- Optionally attach short explanations based on strongest matching features.

## Phase 2 Implementation Sequence

1. Expanded `UserProfile` to support baseline and optional preferences.

- Baseline: genre, mood, energy, acousticness behavior.
- Optional: tempo, danceability, valence.
- Added validation and helper methods for targets/serialization.

2. Implemented CSV loading in `load_songs`.

- Parsed all fields from `data/songs.csv`.
- Cast numeric values to the correct types.
- Returned a clean list of song dictionaries for scoring.

3. Implemented `score_song`.

- Added weighted scoring for all active features.
- Added Gaussian numeric closeness scoring.
- Added normalization by active feature weight sum.

4. Implemented plain-language score reasons.

- Added per-feature contribution messages.
- Output now includes lines like:
	- Genre match: +X points
	- Energy closeness: +Y points

5. Implemented `recommend_songs` ranking loop.

- Scored every song in the catalog.
- Sorted by score in descending order.
- Returned Top-K results.

6. Improved terminal output in `main.py`.

- Added readable ranked layout with title, final score, and reason lines.
- Added import fallback so both module and direct execution work.

## Important Phase 2 Fixes

- Fixed a consistency bug where scoring defaults and profile defaults could diverge.
- Introduced shared module-level constants:
	- `DEFAULT_FEATURE_WEIGHTS`
	- `DEFAULT_FEATURE_SIGMAS`
- Both `UserProfile` defaults and `score_song` now use the same source of truth.

## Validation Performed

- Repeatedly ran the test suite (`pytest`) after major updates.
- Ran A/B weight comparisons (default vs energy-priority) and confirmed ranking shifts.
- Verified that explanation point contributions reflect active weight settings.

## Phase 2 Outcome

- The simulation now supports end-to-end recommendation flow with:
	- configurable preferences,
	- weighted + Gaussian scoring,
	- explainable output,
	- and Top-K ranking behavior.
