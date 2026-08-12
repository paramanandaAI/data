# Nepali WordNet Expansion

The core idea of this project was to utilize pre-trained models combined with Jaccard similarity or FastText-based similarity. For example, if "cow" is semantically near "buffalo", and "buffalo" is an "animal", the model should recognize that semantic relationship as a success.

## Important Papers & Tools We Read
- Bal K. Bal SentiWordNet
- IndoWordNet
- Word2Word
- VecMap
- FastText Vectors
- Pragya Pratisthan Dictionary
- Various GitHub repositories (around 5–6)
- Inception NLP annotation and Doccano
- npvec1

## Repository Files
- `translation.csv`: Compiled automatically from various GitHub sources. We are currently unable to track the exact script that generated it, but hope to recover it later.
- `category.csv`: Created for the hierarchical evaluation of the WordNet.
- `graphml`: We created a GraphML file to visualize relationships. As it was our first time generating one, its usefulness may vary.