# L1 Tokens and Tokenizers — Extended Lesson Notes

## Lesson Flow at a Glance
- **Spark curiosity (10 min):** Students manually tokenize a mini sentence with scissors and paper slips to feel what "breaking text into pieces" means.
- **Guided discovery (25 min):** Walk through the notebook sections on character vocabularies, pair counts, and merge rules, pausing for think-pair-share questions.
- **Hands-on build (30 min):** Learners implement and run the tiny BPE tokenizer, experimenting with different corpora from the `data/` folder.
- **Reflection + challenge (15 min):** Compare tokenizations from different corpora, journal observations, and plan extension experiments.

> **Reminder:** These notes expand on the notebook. Use them to enrich discussion, add unplugged activities, and surface connections the code doesn’t show explicitly.

## Warm-Up: Tokenizing by Hand
1. Write the sentence "Friendly robots help humans" on the board.
2. Hand each student index cards printed with single characters (including the space character and a `</w>` marker).
3. Challenge small groups to arrange the cards into words, then into frequent character pairs they notice. Ask:
   - Which pairs show up more than once?
   - Would combining those pairs make writing the sentence faster next time?
4. Introduce the vocabulary formally:
   - **Token:** A chunk of text the computer treats as a single unit.
   - **Corpus:** The training collection whose patterns decide which tokens are useful.
   - **Merge rule:** An instruction like "if you see `ro` followed by `bot`, glue them together." Write one merge on the board.

## Deep Dive: Why BPE Works
Connect the warm-up to the algorithm from the notebook.
- **Compression intuition:** Frequent pairs shrink the total number of symbols. Use a table showing how a 4-word corpus loses characters as merges happen.
- **Frequency spotting:** Show a short corpus and circle all occurrences of the pair `th`. Count them aloud to model the tallying step before the code does it.
- **Balancing act:** Explain that BPE keeps rare words in smaller pieces so the tokenizer can handle surprises. Relate to Lego sets: common bricks stay whole, custom shapes are built from standard pieces.

### Pen-and-Paper Practice
Give students a two-sentence corpus such as:
```
space ships sparkle
space suits sparkle
```
Have them:
1. Append `</w>` to each word.
2. Count pair frequencies manually (use tally marks in a table).
3. Decide the first two merges.
4. Apply the merges to the corpus and write the new tokenized form.
Discuss how the vocabulary shifts—"space" becomes a single token, while "sparkle" remains split after only two merges.

## Guided Notebook Walkthrough
As you move through the code cells, emphasize the conceptual checkpoints.
1. **Character split + `</w>` (Step 1):** Ask learners why we need an end-of-word marker. Highlight how it prevents merges across spaces.
2. **Pair counting (Step 2):** Encourage students to print the top 10 pairs. Prompt them to predict the next merge before revealing it.
3. **Merge application (Step 3):** Relate the iterative loop to building a dictionary. Each loop adds a new "shortcut" symbol.
4. **Tokenizing new sentences:** Demonstrate with both an in-corpus sentence and a novel one (e.g., "Robots explore space"). Compare token counts before/after merges.

## Stretch the Experiment
Suggest optional branching paths once the core notebook runs:
- **Corpus Remix:** Split the class—half edits `space.txt`, half edits `animals.txt`. After retraining, swap tokenizers and tokenize the same test sentence. Chart differences on the board.
- **Merge Budget Game:** Set merge counts (10, 50, 200) and have teams argue which number gives the best trade-off between vocabulary size and token length. Use evidence from their token counts.
- **Visual Timeline:** Ask students to plot merge number vs. token count reduction on graph paper. Discuss where the curve flattens.

## Reflection Prompts
Encourage individual or pair reflections:
- How did changing the corpus alter which merges were learned first? Why?
- Which merge surprised you the most? What does it reveal about the text’s patterns?
- If you wanted the tokenizer to understand fantasy spell names, what data would you add?

## Exit Ticket Ideas
- **Quick quiz:** Provide three candidate merges and ask which would appear next given a frequency table.
- **Analogy sketch:** Students draw a metaphor (puzzle pieces, cooking recipe, etc.) to explain BPE to a younger sibling.
- **Plan ahead:** Write one hypothesis about how a Minecraft-heavy corpus will tokenize "redstone" before running the experiment next lesson.
