# L5 Fine-tune with Hugging Face — Extended Lesson Notes

## Lesson Flow at a Glance
- **Bridge from scratch builds (10 min):** Review how Lessons 1–4 prepared us to understand pretrained models.
- **Workflow storyboard (20 min):** Map the fine-tuning pipeline on a whiteboard before touching code.
- **Trainer deep dive (30 min):** Execute the notebook while pausing to inspect datasets, tokenization, and training arguments.
- **Quality checks + ethics (20 min):** Evaluate generated samples, discuss overfitting, and consider responsible deployment.

## Warm-Up Discussion: Why Pretrain?
1. Ask: "If our tiny Transformer already writes stories, why use Hugging Face models?" Collect hypotheses.
2. Introduce key terms with quick definitions:
   - **Pretrained checkpoint:** A model already trained on massive text corpora.
   - **Fine-tuning:** Nudging weights so outputs match a new domain.
   - **Overfitting:** When the model memorizes training examples and stops generalizing.
   - **Learning rate:** Step size for weight updates.
3. Compare this process to transferring a skilled musician to a new song—lessons 1–4 built the instrument, now we learn a new tune.

## Workflow Storyboard (Pen & Paper)
Have students sketch a flowchart with boxes for:
1. **Load tokenizer** → 2. **Prepare dataset** → 3. **Initialize model** → 4. **Set training arguments** → 5. **Run Trainer** → 6. **Evaluate & save**.
Encourage them to annotate each box with what could go wrong (e.g., dataset too small, learning rate too high). This paper artifact acts as a checklist while coding.

## Notebook Guidance
As you guide the class through the notebook:
1. **Tokenizer choices:** Show how to reuse the pretrained tokenizer vs. plugging in a custom BPE vocabulary. Discuss trade-offs (compatibility vs specialization).
2. **Dataset construction:** Examine a single batch to ensure `input_ids` and `attention_mask` look correct. Have students compute the average sequence length and consider truncation effects.
3. **Training arguments:** Explain each key hyperparameter. Provide a table for students to note default vs. chosen values and predicted impacts.
4. **Launching training:** Encourage monitoring the loss curve printed by the Trainer. Ask learners to annotate their storyboard with the observed trend.
5. **Generation comparison:** After fine-tuning, generate text from the base model and the fine-tuned model. Students highlight stylistic differences using color coding.

## Pen-and-Paper Hyperparameter Lab
Set up scenario cards describing different goals:
- "I have only 10 minutes—what should my batch size and epochs be?"
- "My model overfits quickly—what adjustments help?"
- "Outputs are bland—how might temperature or top-k sampling change that?"
Students discuss in small groups and write recommendations referencing the hyperparameters table.

## Monitoring for Overfitting
- Teach students to compare training loss vs. evaluation loss curves. Provide graph paper for sketching the trends they observe.
- Introduce simple heuristics: if validation loss plateaus or rises while training loss keeps dropping, consider early stopping.
- Encourage maintaining a sample journal—after each epoch, paste generated text and note improvements or regressions.

## Responsible Deployment Checkpoints
1. **Content review:** Reuse Lesson 6 safety ideas to filter outputs for disallowed content.
2. **Data privacy:** Discuss whether any personal data in the corpus needs anonymization.
3. **Attribution:** If using fan fiction or internet text, clarify permission and citation expectations.
4. **Bias audit:** Brainstorm prompts to test for stereotypes. Record findings and mitigation strategies.

## Offline / No-Internet Fallback
- Revisit the Lesson 4 Transformer. Have students experiment with continuing training on fresh text and compare to the pretrained model’s behavior once they regain connectivity.
- Encourage saving checkpoints locally and documenting training settings so experiments are reproducible.

## Reflection Prompts
- Which part of the fine-tuning pipeline felt most sensitive to your choices? Why?
- How would you explain the benefit of starting from a pretrained model to someone who has only seen Lesson 4’s scratch model?
- What ethical guardrails would you put in place before sharing your fine-tuned model online?

## Extension Ideas
- **Hyperparameter sweep journal:** Vary one setting at a time (learning rate, batch size) and capture results in a table.
- **Dataset curation project:** Design a themed corpus (e.g., eco-fiction) and document cleaning steps.
- **Model card draft:** Have students write a short model card summarizing intended use, training data, evaluation, and limitations.
