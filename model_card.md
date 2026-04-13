# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMatch Mini

---

## 2. Intended Use  

It suggests songs users will probably like from a small catalog. It compares their taste profile to each song. Then it ranks songs and shows the top matches. 

---

## 3. How the Model Works  

3.1. What parts of a song are we using?

- The style of music (genre), like pop or lofi.
- The vibe (mood), like happy, chill, or intense.
- A few “sound characteristics”:
- energy (calm vs high-powered),
- danceability (how groovy it feels),
- tempo (slow vs fast beat),
- acousticness (more natural instruments vs electronic),
- valence (more cheerful vs more serious feeling).

3.2. What do we use about the listener?

- What kind of genre they usually like.
- What mood they want right now.
- Their preferred sound profile:
- how energetic,
- how danceable,
- how fast,
- how acoustic,
- how cheerful.
- How important each of those is to them (for example, maybe genre matters a lot, tempo matters a little).

3.3. How do we turn that into one score?

- For each song, we ask: “How close is this song to what the person likes?”
- If genre matches, that gets good points.
- If mood matches, that gets good points.
- For things like energy or tempo, closer values get more points.
    - Example: if someone likes medium-high energy, a song near that gets a high score.
    - A song that is way too calm or way too intense gets fewer points.
- Then we combine all those points using importance weights, giving us one final score per song.
- Highest scores become the top recommendations.

3.4. What changed from the starter version?

- Before, it was basically a placeholder and did not truly “understand” taste.
- Now it actually compares each song to the listener’s preferences.
- Instead of just returning songs in simple order, it ranks them by match quality.
- It can also explain why a song was recommended (for example: same genre, similar energy, matching mood).


---

## 4. Data  

We used a small dataset with 18 songs. Each song has genre, mood, energy, tempo, valence, danceability, and acousticness. It is useful for learning, but too small for real-world quality. Some genre-mood combinations are missing, so certain users get fewer good matches.

---

## 5. Strengths  

- It works well for clear tastes like pop/happy or lofi/chill.
- It gives easy-to-understand reasons for each recommendation.
- It ranks songs consistently when preferences are similar.
- It responds clearly when we change weights, so behavior is transparent.
- It is simple to run and test in the CLI.
- It is good for learning how scoring and ranking work.

---

## 6. Limitations and Bias 

6.1. Features it does not consider

- Lyrics / Language: Only sound features considered; no content diversity
- Artist diversity: Same artist can dominate recommendations (e.g., LoRoom in lofi)
- Recency / Trends: All songs weighted equally; no time decay for discovery
- User context: No awareness of time-of-day, activity, or mood evolution
- Sub-genre nuance: "Indie pop" treated as atomic, not similar to "pop"

6.2. Genres or moods that are underrepresented  

Genre imbalance:

Lofi: 27.8% (oversaturated)
Jazz, Ambient, Synthwave: 11.1% each (starved)
Impact: Jazz/ambient users face artificial scarcity; limited alternatives

Mood imbalance:

Chill: 27.8% (dominates)
Intense, Relaxed, Moody, Focused: 11-16% each (sparse)
Critical gap: Zero songs matching "Ambient + Intense" or "Jazz + Happy"
Impact: Users with these combos get forced into numeric-only matching

6.3. Cases where the system overfits to one preference  

- "Pop Happy" users: Get 27+ recommendations ranked consistently; trapped in genre-mood bubble
- "Pop Intense" users: Only 1 exact match (Gym Hero); forced to depend on energy closeness
- Mid-range energy users (0.4–0.8): Consistently get better matches; extreme preferences (0.05 or 0.95) starved
- "Lofi Chill" users: 5 exact matches = maximum diversity; system feels "personalized"
- Opposite: "Ambient" or "Jazz" users: Average ~1–2 genre matches; minimal variation

6.4. Ways the scoring might unintentionally favor some users

- Lofi listeners: Huge, 27.8% of catalog matches
- Pop fans: Moderate,	3 exact songs + 2 indie-pop near-misses
- Jazz/Ambient lovers: Severe, Only 2 songs each; no mood matches
- Acoustic enthusiasts: Neglected, 0.5 weight on acousticness; feature is ignored
- Mid-energy seekers (0.5–0.7): Advantage, Catalog centered at 0.60 mean
- Extreme energy fans (0.05 or 0.95): Penalized, Energy gap formula rewards middle ground
- "Happy" mood users: Advantage, 22.2% of songs; 4 exact matches
- "Relaxed/Moody" users: Disadvantage, Only 2 songs each; no genre diversity within mood


---

## 7. Evaluation  

7.1. Which user profiles you tested  

- High-Energy Pop, Chill Lofi, Deep Intense Rock, Rock + Sad Contrast, Chill Lofi Fast Tempo, and Focused Lofi Detailed.

Any simple tests or comparisons you ran
Baseline run with current scoring, sensitivity checks by changing weights (energy up, genre down), a mood-off comparison, and side-by-side profile runs (including edge-case profiles) to see if results were more accurate or just different. We also did a quick catalog distribution check to spot likely bias and filter-bubble patterns.

7.2. What you looked for in the recommendations

- Whether top songs matched the profile’s intended vibe, whether explanations made sense feature-by-feature, and whether rank order changed in expected ways when we changed weights or disabled a feature.

7.3. What surprised you  

- How quickly rankings shift when one signal changes. Removing mood made intense pop tracks rise for happy-pop users, and genre/mood scarcity in the catalog made some profiles feel under-served even when the math was working correctly.

7.4. Any simple tests or comparisons you ran

- Baseline run with current scoring, sensitivity checks by changing weights (energy up, genre down), a mood-off comparison, and side-by-side profile runs (including edge-case profiles) to see if results were more accurate or just different. We also did a quick catalog distribution check to spot likely bias and filter-bubble patterns.

---

## 8. Future Work  

- Add more songs and more balanced genre-mood coverage. 
- Support partial similarity between related genres and moods instead of exact match only. 
- Let users set feature weights or learn weights from feedback over time.

---

## 9. Personal Reflection  

9.1. What was your biggest learning moment during this project?

- Small rule changes caused big ranking changes. Changing one weight or disabling mood shifted results a lot. That showed us how sensitive recommenders are.

9.2. How did using AI tools help you, and when did you need to double-check them?

- AI helped me move faster with coding, testing, and explanations. It helped generate profiles and edge-case experiments quickly. I still needed to double-check fairness claims, result quality, and naming/wording choices. I also needed to verify that changes matched my intent before keeping them.

9.3. What surprised you about how simple algorithms can still "feel" like recommendations?

- Even simple scoring can look very personalized. Matching a few features (genre, mood, energy) already feels smart. But it can still be biased or shallow underneath.

9.4. What would you try next if you extended this project?

- Add more songs and better genre-mood coverage. Add partial similarity for related genres and moods. Let users tune weights or learn them from feedback. Add a diversity rule so top results are not too repetitive.




