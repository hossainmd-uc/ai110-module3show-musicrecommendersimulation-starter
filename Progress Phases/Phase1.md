# Phase 1 Progress Summary

## What Has Been Decided

The recommender is being designed as a simple content-based system that compares a user's preferences to each song in the catalog and ranks songs by relevance.

## Core Design Decisions

- The system uses all available fields from `data/songs.csv`.
- The main comparison fields are `genre`, `mood`, `energy`, and `acousticness`.
- Secondary fields are `tempo_bpm`, `danceability`, and `valence`.
- The system uses weights so that more important fields influence the final score more than less important fields.
- A starting weight scheme was chosen as:
  - `genre = 0.25`
  - `mood = 0.20`
  - `energy = 0.20`
  - `acousticness = 0.15`
  - `tempo_bpm = 0.10`
  - `danceability = 0.07`
  - `valence = 0.03`
- Numerical features are scored by closeness to the user's preferred value using a Gaussian-style formula.
- The overall relevance score is the weighted sum of the individual feature scores and is used for ranking.

## User Profile Assumptions

- The user profile stores preference ratings or target values for the same fields used in scoring.
- The user can specify the most important preferences first and optionally tune the less important fields.
- The recommender is intended to reward similarity to the user's target values, not just higher numerical values.

## Documentation Updates Completed

- The README was updated to explain the weighted scoring system.
- The research prompt log was filled in with the key prompts, follow-up prompts, and answers used during the research process.

## Data Notes

- The starter catalog is very small, so the recommender relies on clear separations like genre, mood, energy, and acousticness.
- Songs in the catalog cluster naturally into calmer high-acousticness tracks and higher-energy low-acousticness tracks.

## Next Likely Steps

- Implement the scoring logic in `src/recommender.py`.
- Keep the scoring explanation aligned with the README and model card.
- Add or update tests once the scoring behavior is implemented.
