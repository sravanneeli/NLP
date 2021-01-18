## [Word2Vec](https://www.analyticsvidhya.com/blog/2017/06/word-embeddings-count-word2veec/)
* Word2Vec is a two-layer nueral net that process text.
* Its input is a text corpus and its output is a set of vectors: feature vectors for words in that corpus.
* The purpose and usefulness of Word2Vec is to group the vectors of similar words together in vector space i.e.,it detects similarites mathematically.
* Word2Vec creates vectors that are distributed numerical representations of word features, features such as the context of individual words.
* It does so without human intervention.
* Word2Vec trains words against other words that neighbour them in the input corpus.
* It does so in one of the two ways, either using context to predict a target word(a method known as continous bag of words, or <b>CBOW</b>), or using a word to predict a target context, which is called <b>skip-gram</b>.
* This means we can use Cosine similarity to measure how similar word vectors are to each other.


### Continous Bag of Words(CBOW)
* CBOW generally takes a different words context (given window size ) it tries to predict a single context word.
* *Step1:* Find the mean input word vectors
* *Step2:* Get the output prediction.

### 