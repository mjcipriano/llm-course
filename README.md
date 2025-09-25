# 3-Week LLM Course (6 Lessons) — Kids Edition (Advanced)
**Audience:** Ages ~12 & 15 (advanced).  
**Goal:** Learn *how LLMs work* by building core pieces yourself, then fine-tune a small pretrained model.

## Structure
- Week 1
  - **L1 Tokens & Tokenizers:** Build a mini BPE tokenizer and see merges.
  - **L2 Embeddings & Similarity:** Co-occurrence → SVD embeddings; plot neighbors.
- Week 2
  - **L3 N-gram Language Models:** Train 1/2/3-gram models; sampling; perplexity.
  - **L4 Tiny Transformer:** Implement a char-level Transformer and train it.
- Week 3
  - **L5 Fine-tune (Hugging Face):** Fine-tune a small GPT on your own text.
  - **L6 Evaluation/Prompting/Safety:** Perplexity, prompts, simple guardrails.

## Hands-on Flow
Every lesson is a Jupyter notebook under `notebooks/` with:
- Short lecture-style Markdown cells
- Code cells you can run and **edit**
- Challenges to extend learning

Editable corpora are under `data/`—add your own stories (space, animals/dogs, Minecraft)!

## Setup
Recommended Python 3.10+ with `pip`. Suggested installs in `environment.txt`:
```
pip install numpy matplotlib ipywidgets nbformat
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install transformers datasets accelerate  # for Lesson 5
```
> On GPU machines, install the appropriate PyTorch build.

## Running
```
jupyter lab
# or
jupyter notebook
```
Open any notebook in `notebooks/` and run cells top-to-bottom.

## For AI Agents (maintenance/upgrades)
- **Content Locations**
  - Notebooks: `notebooks/L#.ipynb`
  - Slides (markdown): `slides/L#.md`
  - Images: `images/*.png`
  - Data (editable corpora): `data/*.txt`
- **Dependency Hints**: See `environment.txt`
- **Upgrade Ideas**
  - Replace co-occurrence + SVD with skip-gram/CBOW (gensim).
  - Add multi-head attention, dropout, and better scheduler in Lesson 4.
  - Add PEFT/LoRA fine-tuning paths in Lesson 5 for low-VRAM devices.
  - Extend Lesson 6 with a real evaluation harness (perplexity for HF model).

## Purpose
Help advanced kids truly *understand* LLMs by building the key components from scratch:
tokenization, embeddings, language modeling, attention/Transformer, and fine-tuning—plus
practical evaluation and safety concepts.

— Generated on 2025-09-22T04:26:32.461787Z
