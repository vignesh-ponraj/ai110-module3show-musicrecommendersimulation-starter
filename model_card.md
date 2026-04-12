# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

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
- - Example: if someone likes medium-high energy, a song near that gets a high score.
- - A song that is way too calm or way too intense gets fewer points.
- Then we combine all those points using importance weights, giving us one final score per song.
- Highest scores become the top recommendations.

3.4. What changed from the starter version?
- Before, it was basically a placeholder and did not truly “understand” taste.
- Now it actually compares each song to the listener’s preferences.
- Instead of just returning songs in simple order, it ranks them by match quality.
- It can also explain why a song was recommended (for example: same genre, similar energy, matching mood).


---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
