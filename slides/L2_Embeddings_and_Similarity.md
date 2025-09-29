# L2 Embeddings and Similarity — Extended Lesson Notes

## Lesson Flow at a Glance
- **Concept ignition (10 min):** Use a word-web on the board to illustrate semantic neighborhoods.
- **Data craft (20 min):** Construct a co-occurrence matrix by hand for a tiny corpus, then mirror the process in the notebook.
- **Linear algebra adventure (25 min):** Walk through SVD intuition with paper folding and axis metaphors before running the code.
- **Exploration lab (25 min):** Students probe nearest neighbors, tweak hyperparameters, and journal discoveries.

## Warm-Up: Semantic Neighborhood Walk
1. Write "astronaut" in the center of a large sheet. Ask students to suggest related words; cluster them (spacecraft, NASA, gravity).
2. Discuss what makes a word feel "close"—shared stories? Same categories? Similar verbs?
3. Introduce embeddings as the computer's way to place words in a **vector space** so closeness can be measured numerically.
4. Vocabulary spotlight:
   - **Embedding:** A numeric vector representing a word's relationships.
   - **Co-occurrence window:** The number of neighboring words we care about on each side.
   - **Cosine similarity:** Measures how aligned two vectors are; 1.0 means pointing the same direction.

## Building Co-Occurrence Intuition (Pen & Paper)
Provide the mini corpus:
```
rockets launch fast
astronauts fly rockets
```
1. List the unique words (include `<PAD>` or `<UNK>` if you plan to in code).
2. Choose a window size of 1. Draw a table with center words as rows and neighbor words as columns.
3. Slide the window manually through each sentence. For "rockets launch fast" record that "rockets" sees "launch" once.
4. Sum counts and fill the table.
5. Ask students to circle which pairs got the highest counts. Predict which vectors will be similar.

## Transition to Notebook Implementation
- Highlight how the code generalizes the hand process: loops replace the sliding window you just simulated.
- Encourage learners to compare their manual table to the printed matrix from the notebook. Are the numbers aligned? If not, debug together—perhaps a boundary case was missed.

## SVD Without Fear
Before running `scipy.sparse.linalg.svds`, ground the idea:
- **Paper axis demo:** Hold two colored pencils as perpendicular axes. Place sticky notes representing words. Explain how SVD finds a new pair of axes that better align with the true themes (e.g., "space" vs. "speed").
- **Energy metaphor:** The first singular value captures the loudest pattern. Ask what pattern that might be in the rocket corpus (probably "space terms vs. action verbs").
- **Dimensionality choice:** Explain why we keep only the top *k* components—the rest contribute less meaning and add noise.

### Optional Mathematical Dig
For interested students:
- Show the equation `M ≈ U_k Σ_k V_kᵀ` and map each piece to code variables.
- Demonstrate how dividing by the square root of counts or applying Positive Pointwise Mutual Information (PPMI) changes the emphasis.

## Exploring Embedding Space
Use the notebook’s plotting and similarity helpers as jumping-off points.
1. **Nearest neighbors:** Pick a word like "rocket" and compute top-5 neighbors. Ask students to justify each neighbor using sentences from the corpus.
2. **Least similar words:** Identify vectors with cosine near zero or negative. Discuss what it means for meaning—do those words ever meet in the stories?
3. **Two-corpus comparison:** Train once on `space.txt` and once on `animals.txt`. Plot both embeddings on graph paper using two axes (Dimension 1 vs. Dimension 2) and label points by hand. Are the clusters different?

## Pen-and-Paper Challenge Stations
Set up stations with printed co-occurrence tables and partially completed embeddings.
- **Station A (Window sweep):** Students recalc counts with window size 2 and predict how "astronaut"’s vector changes.
- **Station B (Analogies):** Provide three word vectors (numbers small enough for mental math). Have students compute cosine similarity with calculators and decide which word completes an analogy like "planet is to orbit as fish is to ____".
- **Station C (Dimensional intuition):** Give a 2D scatter plot and ask students to annotate quadrants (e.g., top-right = "space nouns").

## Reflection and Discussion
- How does the choice of corpus shape what the embeddings "believe" about words?
- What might happen if we train on social media slang—would "lit" move closer to "exciting" or "illumination"?
- When could cosine similarity fail? Brainstorm cases where two words share neighbors but have opposite sentiment.

## Extension Ideas
- **Story blender:** Merge two themed corpora and observe whether SVD axes separate the themes. Encourage sketches of the axes with explanatory captions.
- **Time capsule:** Add new sentences to the corpus each day and plot how a word’s neighbors shift. Keep a logbook of the drift.
- **Explain to a friend:** Have students write a postcard explaining embeddings without using the word "vector." This reinforces conceptual clarity.
