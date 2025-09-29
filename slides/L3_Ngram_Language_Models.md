# L3 N-gram Language Models — Extended Lesson Notes

## Lesson Flow at a Glance
- **Prediction warm-up (10 min):** Students play a cloze game guessing the next word in famous phrases.
- **Counting workshop (25 min):** Build unigram, bigram, and trigram tables on paper, then mirror the logic in code.
- **Probability playground (25 min):** Explore smoothing, sampling, and perplexity calculations from the notebook with guided prompts.
- **Evaluation reflection (15 min):** Discuss why models fail, compare perplexity scores, and plan improvements.

## Warm-Up Game: "Next Word?"
1. Present partial sentences like "The dragon breathed ___" or "In a galaxy far, far ___".
2. Have students write predictions on sticky notes; reveal actual endings.
3. Introduce the concept of **context length**—some endings are obvious with two previous words, others remain ambiguous.
4. Vocabulary spotlight:
   - **N-gram:** A chunk of `N` consecutive tokens.
   - **Conditional probability:** The likelihood of the next token given previous ones, written `P(next | context)`.
   - **Add-k smoothing:** Adding a small constant to every count to avoid zero probabilities.
   - **Cross-entropy:** A score summarizing surprise; lower means better predictions.

## Paper-Based Counting Workshop
Use the corpus:
```
the silver spaceship
the silver dragon
```
1. Tokenize into words (include `<BOS>` for beginning-of-sentence if using it later).
2. Build tables:
   - **Unigram:** Count each word independently.
   - **Bigram:** Record every pair `(context, next)`.
   - **Trigram:** Track triples using two-word contexts.
3. Practice computing probabilities:
   - `P(spaceship | the silver)` = trigram count / bigram count for `the silver`.
   - Apply add-1 smoothing: add 1 to each trigram count and adjust denominators accordingly.
4. Challenge: Ask students whether `P(dragon | the silver)` changes more for add-1 smoothing than `P(spaceship | the silver)`. Why?

## Connecting to the Notebook
When running the provided code:
- Encourage students to print sections of the count dictionaries to confirm they match the manual tables.
- Before sampling text, ask the class to predict the first three generated words using trigram probabilities.
- During perplexity computation, pause to interpret the formula. Use a whiteboard derivation to show that cross-entropy is the average negative log probability.

## Understanding Smoothing Deeply
Lead a short discussion:
- Without smoothing, what happens if the model never saw a sequence? (Probability becomes zero, and log probability is undefined.)
- Demonstrate with numbers: if `P = 0` for one token in a 10-token sentence, perplexity becomes infinite.
- Show how add-0.1 vs add-1 influences rare vs. common sequences using a simple table. Provide calculators so students can compute sample values by hand.

## Sampling Strategies (Hands-On)
1. **Temperature scaling worksheet:** Give students a list of probabilities for the next token (e.g., `fire:0.6, frost:0.2, friend:0.2`). Ask them to apply temperature 0.5 and 1.5 using the formula `p_i^(1/T) / Σ p_j^(1/T)`. Provide step-by-step hints.
2. **Dice simulation:** Use a 10-sided die to sample from a probability table rounded to tenths. Students physically roll to generate a sentence fragment.
3. Compare deterministic "pick the highest" decoding to sampling results. Discuss trade-offs (predictability vs creativity).

## Perplexity as Model Sense-Making
- Explain perplexity with a metaphor: it measures how many equally likely options the model juggles. A perplexity of 8 means the model feels there are about eight believable next words each time.
- Have students calculate perplexity for a tiny sentence using provided probabilities. Work through logs step-by-step (offer calculators or precomputed log tables).
- Ask: does a lower perplexity always mean better text? Discuss cases where the model might memorize and still get low scores.

## Reflection Questions
- When did the trigram model outperform the bigram model in your experiments? When did it struggle due to sparse data?
- How did smoothing change the generated stories? Cite specific examples.
- If you doubled the corpus size, which metric would you expect to improve most—perplexity, vocabulary coverage, or sample diversity?

## Extensions and Challenges
- **Context showdown:** Have teams build models with different N (2 vs 3 vs 4) and present evidence about which is best on a held-out paragraph.
- **Error forensics:** Provide a weird generated sentence. Students trace back which probability decisions likely produced it.
- **Backoff strategy design:** Sketch a pseudocode algorithm for Katz backoff or Kneser-Ney, even if not implemented. Identify when you’d drop from trigram to bigram counts.
- **Real-world connection:** Research how autocomplete on phones balances N-gram models with neural models. Share findings in a mini-poster.
