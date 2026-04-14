# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

My version uses a weighted, content-based scoring system. The recommender compares a user profile against each song in the catalog, gives the most important fields the largest weights, and then ranks songs by their overall relevance score.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

### Song Features

Each song is represented using the available fields in `data/songs.csv`:

- `genre`
- `mood`
- `energy`
- `tempo_bpm`
- `valence`
- `danceability`
- `acousticness`

### User Profile

The `UserProfile` stores the user's preference ratings for each field. In this system, the most important preferences are the baseline comparison fields:

- `genre`
- `mood`
- `energy`
- `acousticness`

Users can also provide optional preferences for:

- `tempo_bpm`
- `danceability`
- `valence`

### Weighting Strategy

The recommender uses a weighted system so that the most important fields influence the final score more strongly than the less important fields. A reasonable starting set of weights is:

- `genre = 0.25`
- `mood = 0.20`
- `energy = 0.20`
- `acousticness = 0.15`
- `tempo_bpm = 0.10`
- `danceability = 0.07`
- `valence = 0.03`

These weights can be adjusted, but the idea is that genre, mood, and energy matter most, while the remaining fields fine-tune the ranking.

### Scoring Rule

For numerical features, the recommender rewards songs that are close to the user's preference rather than simply larger or smaller. The score for one feature is based on the distance between the song value and the user target:

$$
s_f = e^{-\frac{(x_f - p_f)^2}{2\sigma_f^2}}
$$

Where:

- $s_f$ = score for one feature
- $x_f$ = the song's value for that feature
- $p_f$ = the user's preferred value for that feature
- $\sigma_f$ = how quickly the score drops as the song moves away from the user's preference

This formula gives a score close to $1$ when the song matches the user's preference and a smaller score as the song gets farther away.

For categorical features like `genre` and `mood`, the recommender can assign a high score when the song matches the user's preference and a lower score when it does not.

### Overall Relevance Score

The final score is a weighted sum of all feature scores:

$$
R = \sum_i w_i s_i
$$

Where:

- $R$ = overall relevance score
- $w_i$ = importance weight for feature $i$
- $s_i$ = score for feature $i$

The result is normalized to a value from $0$ to $1$, where higher values mean the song is a better match for the user.

### Recommendation Flow

1. Compare each song against the user profile.
2. Compute a score for each field.
3. Multiply each field score by its weight.
4. Add the weighted scores together to get the final relevance score.
5. Sort songs from highest score to lowest score and return the top results.

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

Phase 2 A/B output screenshots:

- Test 1 (decreased genre importance, increased energy importance): [Screenshots/image1.png](Screenshots/image1.png)
- Test 2 (complementary setup: higher genre importance, lower energy importance): [Screenshots/image2.png](Screenshots/image2.png)

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

