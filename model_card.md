# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

WaveMatch 1.0 

---

## 2. Intended Use  

This recommender suggests a Top-K list of songs from a small catalog based on a user taste profile.

It assumes the user can provide preferences like genre, mood, and numeric targets such as energy and acousticness.

This system is for classroom exploration, not for production use with real users.

---

## 3. How the Model Works  

Each song has features: genre, mood, energy, acousticness, tempo, danceability, and valence.

The user profile stores preferred values for those same fields.

The model gives each feature a weight, scores how close each song is to the profile, and then adds the weighted feature scores into one final relevance score from 0 to 1.

Compared to the starter version, I implemented CSV loading, weighted scoring, Gaussian-style numeric matching, readable reason output, and sorted Top-K recommendations.

---

## 4. Data  

The catalog contains 20 songs in `data/songs.csv`.

It includes genres like pop, lofi, rock, ambient, jazz, synthwave, hip hop, metal, house, folk, reggae, blues, cinematic, soul, and others.

I expanded the starter data by adding 10 additional songs with new genres and moods to improve variety.

Even with this expansion, the dataset is still small and cannot represent the full range of real-world musical taste.

---

## 5. Strengths  

The system works well when the user provides clear preferences (especially genre, mood, energy, and acousticness).

It captures intuitive patterns such as:

- high-energy profiles getting energetic tracks,
- low-energy and high-acousticness profiles getting calmer tracks,
- score shifts when feature weights are adjusted.

The reason breakdown is also a strength because users can see exactly why each song scored the way it did.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

There is some overconfidence in my system when the user provides very little information
for the scoring system to work, causing greater weights to be placed on potentially
unimportant features, subsequently leading to a non-optimal resulting top-K list.

The energy sigma (a calculation that thresholds the allowed tightness of the numrical deviation) is a bit tight, which may exclude nearby energy values and only prioritize
the values somewhat strictly within the range.

The categorical matches are quite strict, only awarding points on full match or none
which might not be ideal if we want to pursue a graded approach. For example,
chill vs relaxed are quite similar and it is logical that they would be regarded as such
and awared points accordingly based on the algorithm.

In terms of available data, there are some genres that appear more frequently than others
leading to potential narrowing of which genres appear even with fair scoring: the genres
that appear the most might have greater probability of appearance in the final top-K 
scoring. 

Finally, preferences are heavily based on the calculated score. Were it the case that 
the user favored novelty and variety, then the preference system would not be suited 
for that end.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

### My Evaluation Notes

I tested the recommender by comparing two versions of the same user taste profile.

1. Test A: Original settings

- This version gave more importance to genre.
- Top results were: Sunrise City, Rooftop Lights, Gym Hero, Night Drive Loop, and Neon Shuffle.

2. Test B: Energy-focused settings

- In this version, I lowered genre importance and raised energy importance.
- Top results were: Sunrise City, Rooftop Lights, Night Drive Loop, Neon Shuffle, and Starlit Heat.

3. What changed, and why it makes sense

- Sunrise City stayed #1 in both tests. This makes sense because it matches well across many fields, not just one.
- Gym Hero dropped while Starlit Heat moved into the top 5. This makes sense because the model was told to care more about energy than genre.
- Rooftop Lights got a much higher score in the energy-focused test because its energy value is close to the user target.
- Night Drive Loop and Neon Shuffle moved up even without genre or mood matches, because their numeric values (especially energy) were close to the target profile.

4. Reliability checks

- I ran the test suite after major changes to make sure I did not break the core project behavior.
- I also checked the explanation text to confirm it matched the actual score contributions.

Important bug found and fixed

- I found that one part of the code was using different default settings than another part.
- This made the printed explanation look inconsistent with what I expected.
- I fixed this by using one shared set of defaults for weights and tolerance values, so the scoring logic and explanations now stay in sync.

What surprised me

- Even after changing weights, the top song can stay the same when one track is a strong all-around match.
- The biggest differences often appear in positions 2 to 5, which still shows that the model is responding to preference changes.

---

## 8. Future Work  

Add graded similarity for categorical features (for example, treat chill and relaxed as partially similar).

Add a diversity step so top results are not overly concentrated in one genre or mood.

Allow users to set exploration level (safe recommendations vs discovery mode).

Support multi-profile or session-based preferences so users with changing tastes are modeled better.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that there are various facets to creating a recommender system, including
a behavioral system as well as a purely data driven system. My app uses the second
aspect as its algorithmic underpinning to produce Top-K recommendations based on a
user profile. Something interesting to keep in mind is the mathematical algorithm
that depends on sigma values for calculating thresholds and gradation of the numerical
values for a given feature score. This component is critical to quantifying the 
allowed deviation for specific feature values and calculating the final score. This 
project has allowed me to appreciate the complexity of music apps like Spotify much more
since they use much more complex algorithms that not only integrate the data-approach
but also the behavioral data in a hyrid manner!
