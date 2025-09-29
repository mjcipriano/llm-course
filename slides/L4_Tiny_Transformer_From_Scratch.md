# L4 Tiny Transformer From Scratch — Extended Lesson Notes

## Lesson Flow at a Glance
- **Analogy opener (10 min):** Compare attention to spotlighting key lines in a play script.
- **Component teardown (25 min):** Walk through Queries, Keys, Values, masking, and positional encodings using manipulatives.
- **Notebook construction (30 min):** Students implement the attention head, block, and training loop, verifying each piece.
- **Insight circle (15 min):** Reflect on sample outputs, diagnose errors, and brainstorm architectural tweaks.

## Warm-Up: Spotlight Metaphor
1. Display a short dialogue. Ask students to highlight which earlier lines help predict the next line.
2. Introduce self-attention: every token shines a spotlight backward to decide which earlier tokens matter most.
3. Vocabulary spotlight:
   - **Self-attention:** Computes how much each token should attend to others.
   - **Masking:** Prevents peeking into the future.
   - **Residual connection:** Allows information to flow unchanged around a block.
   - **Layer normalization:** Stabilizes activations by normalizing features.
   - **Positional encoding:** Adds order clues.

## Hands-On Attention Mechanics
Use index cards and string to simulate an attention head.
1. Assign each student a token from a short sentence and give them three cards labeled Q, K, V with sample numeric values (e.g., small 2D vectors).
2. Have them compute dot products using calculators or dot-product grids; scale by `1/√d`.
3. Apply softmax using approximate values (provide a table for `exp(x)` of small numbers). Students convert scores into attention weights that sum to 1.
4. Each "Value" student multiplies their vector by the attention weight and adds results to produce the final representation for the querying token.
5. Discuss: Which token ended up contributing most? Does that match intuition?

## Masking Demonstration
- Use a paper matrix to show how future positions are set to `-∞` before softmax. Cover the upper-right triangle with sticky notes labeled "mask".
- Ask why this matters when generating text—connect to not cheating on a test.

## Positional Encoding Intuition
- Draw sine and cosine waves on graph paper. Mark how each position has a unique pair of sine/cos values.
- Explain that these signals let the model distinguish "dog bites man" from "man bites dog" even if the same words are present.
- Encourage students to compute the first two positional encoding values for positions 0–5 using a calculator to see the pattern.

## Notebook Guidance
As learners implement the code:
1. **Attention head:** Verify shapes at each step. Encourage print statements after matmul operations to confirm dimensions match expectations.
2. **Multi-head assembly:** Explain how concatenating heads increases the model’s ability to look at different relationship types simultaneously.
3. **Feedforward network:** Relate it to a tiny MLP applied to each position. Emphasize the role of non-linearity (e.g., GELU/ReLU).
4. **Training loop:** Connect cross-entropy loss back to Lesson 3’s perplexity. Remind students to monitor loss over epochs.
5. **Sampling:** Let them try different start prompts and share the funniest outputs.

## Pen-and-Paper Diagnostics
Provide scenarios and ask students to predict effects before coding:
- **What if layer norm is removed?** (Training may diverge.)
- **What if we forget to mask?** (Model sees future tokens and cheat-predicts.)
- **What if positional encodings are all zeros?** (Model can’t differentiate order.)
Have them justify answers referencing the attention pipeline.

## Error Debugging Checklist
- Check tensor shapes—draw a table of expected shapes after each operation.
- Inspect gradients for NaNs; explain how exploding values may require gradient clipping.
- Encourage logging sample predictions every few hundred steps to catch degenerate outputs early.

## Extension Activities
- **Architecture tweaks:** Increase number of heads or layers. Chart loss vs. parameter count on graph paper.
- **Dropout experiment:** Add dropout to attention weights and feedforward layers. Observe how it affects overfitting on small corpora.
- **Embedding sharing:** Compare performance when input and output embeddings are tied vs. separate. Discuss parameter efficiency.
- **Positional creativity:** Try learnable positional embeddings and debate pros/cons vs sinusoidal ones.

## Reflection Prompts
- Which component felt most magical once you saw it work? Why?
- How does self-attention generalize the N-gram idea from Lesson 3?
- If you doubled the block size, what new patterns could the model capture? What costs would that introduce?

## Exit Ticket Options
- Sketch the flow of data through one Transformer block in five labeled steps.
- Define "self-attention" in your own words plus an analogy.
- List two signs (quantitative or qualitative) that training is going well.
