# L6 Evaluation, Prompting, and Safety — Extended Lesson Notes

## Lesson Flow at a Glance
- **Metric mindset (10 min):** Review cross-entropy and introduce perplexity with tangible analogies.
- **Evaluation lab (25 min):** Run perplexity calculations on multiple models using the notebook and compare results.
- **Prompt engineering studio (20 min):** Craft and test prompt templates; analyze how structure changes responses.
- **Safety sprint (25 min):** Design simple guardrails, test edge cases, and discuss limitations.

## Warm-Up: Guessing Game for Perplexity
1. Present a jar with 6 equally likely mystery outcomes vs. a jar with 20 options. Ask: which jar is more "perplexing"?
2. Connect to perplexity—lower perplexity means fewer believable options.
3. Vocabulary spotlight:
   - **Perplexity:** `exp(cross_entropy)`, roughly the number of likely next tokens.
   - **Held-out set:** Data reserved strictly for evaluation.
   - **Prompt template:** A reusable structure guiding an LLM’s behavior.
   - **Guardrail:** Rules or classifiers that prevent unwanted content.

## Evaluation Lab
### Pen-and-Paper Prep
- Provide a short token sequence with predicted probabilities from two models (Model A and B).
- Have students compute cross-entropy manually (using provided `log` values) and then exponentiate to get perplexity.
- Discuss which model performs better and why small probability differences can impact the final metric.

### Notebook Application
1. Evaluate the trigram model from Lesson 3 and the tiny Transformer from Lesson 4 on the same held-out paragraph.
2. Plot or tabulate the perplexities side by side. Encourage students to hypothesize reasons for differences (context length, parameter count, training data).
3. Challenge: change the held-out text (e.g., swap themes) and observe how perplexity shifts. Does a space-themed model struggle with animal stories?

## Prompt Engineering Studio
1. Introduce the structured prompt formula: **Role → Task → Constraints → Examples → Check.**
2. Divide students into teams. Each team creates two prompts for the same task (e.g., "Explain orbital mechanics to a fifth grader").
3. Use the notebook (or an accessible LLM) to test both prompts. Students annotate responses for clarity, accuracy, and tone.
4. Pen-and-paper follow-up: Have teams map which prompt elements (examples, constraints) seemed most influential. Encourage them to draw arrows linking prompt components to observed behavior.

## Safety Sprint
### Designing Rule-Based Filters
- Brainstorm categories of unsafe or off-mission content relevant to the class (e.g., personal data requests, hate speech, spoilers).
- On paper, draft simple keyword or pattern rules. Discuss potential false positives/negatives.
- Implement chosen rules in the notebook’s safety filter and log which ones trigger during tests.

### Stress Testing
- Provide scripted test prompts, including borderline cases, for students to classify as "allow" or "block" before running through the filter.
- Compare human predictions with filter outcomes. Where did the filter miss? How might you improve it (add synonyms, use embeddings)?

## Reflection and Ethics Circle
- How do evaluation metrics and safety checks work together when deploying a model?
- Share stories of when a prompt tweak drastically improved an answer—what changed?
- Discuss the limits of rule-based safety: what nuanced cases require human judgment or more advanced classifiers?

## Extension Ideas
- **Metric mashup:** Combine perplexity with qualitative scoring (human ratings) and debate how to weigh them.
- **Prompt tournament:** Run brackets where prompts compete on effectiveness. Use a rubric for judging.
- **Safety roadmap:** Create a poster outlining a multi-layer defense (filters, classifiers, human review) for a hypothetical chatbot.

## Exit Ticket Options
- Compute perplexity for a two-token toy example given probabilities and explain what the number means.
- Outline one improvement you would make to the safety filter and why.
- Write a short paragraph comparing the goals of prompting vs. safety in responsible AI deployment.
