# Research Prompt Log

## 1. Streaming recommender systems

**Prompt**

Research and summarize how major streaming platforms like Spotify or YouTube predict what users will love next.

What is the difference between collaborative filtering and content-based filtering?

How are these used by these major platforms respectively?

**Follow-up prompt**

Can you give a shorter explanation focused on the practical difference between the two approaches?

**Answer used**

Collaborative filtering learns from behavior patterns across users. If many people who liked one item also liked another, the system uses that pattern to recommend the second item. Content-based filtering learns from item attributes. If a user liked a song with certain features, it recommends songs with similar features.

**Takeaway**

Streaming systems are usually hybrid. Spotify uses strong content-based signals such as audio features and seed tracks, but also benefits from behavioral signals like plays and skips. YouTube leans heavily on collaborative and behavior-driven ranking, especially watch and click history.

---

## 2. Feature selection for a content-based recommender

**Prompt**

Analyze the available data and suggest which features would be most effective for a simple content-based recommender.

**Follow-up prompt**

What does valence entail in this context and how relevant is it?

What is acousticness?

What is energy tied to?

**Answer used**

The strongest features in the catalog are genre, mood, energy, acousticness, tempo, and danceability. Valence is useful for fine-tuning mood, but it is less decisive than energy or acousticness. Acousticness describes how acoustic or organic a track sounds. Energy reflects perceived intensity and activity.

**Takeaway**

For a small dataset, the best content-based features are the ones that clearly separate song clusters: genre and mood for broad categories, then energy, acousticness, and tempo for closer matching.

---

## 3. Scoring and ranking logic

**Prompt**

Let's create an algorithmic blueprint for the specific variables you mentioned and assign importance values.

Specifically, let's make a math-based scoring rule for the recommender. How can I calculate a score for a numerical feature like energy that rewards songs that are closer to the user's preference rather than just having higher or lower values?

**Follow-up prompt**

Is this a scoring rule or a ranking rule? Would I need both? What does either entail?

I am trying to conceptualize the scoring you mentioned. You mentioned the weights which make sense because it's the backbone of the system and how it considers how much importance to give to a field.

But when scoring, if a song is relevant, how does that come into play exactly, is there data that the user has regarding their preference initially, and that is used against the song to calculate the differences which are summed? What is the exact process?

**Answer used**

Numerical features can be scored by closeness to a target value using a Gaussian-style rule. A weighted sum then combines all feature scores into one overall relevance score. The user profile stores preference values, and each song is compared against those preferences field by field.

**Takeaway**

The recommender has two stages: scoring calculates how well a song matches the user profile, and ranking sorts all songs by that score.

---

## 4. README explanation

**Prompt**

I want you to fill in the readme with this information:

My system will use a weighted system considering all the available fields. The higher fields such as genre mood and energy will be given greater importance and subsequent ones will be given lower importance based on my relevance preference.

[...]

I want you to include this information in the read me under the appropriate headings. Use equations where needed.

**Answer used**

The README should explain the song features, the user profile fields, the weight ordering, the Gaussian scoring rule, and the overall relevance equation. It should also describe the recommendation flow from feature comparison to ranking.

**Takeaway**

Use plain language for the explanation, but include the math in the system design section so the scoring logic is explicit and easy to justify.
