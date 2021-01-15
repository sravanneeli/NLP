## Natural Language Processing
* An area of computer science and artificial intillegence concerned with the interactions between computers and human(natural) langauges, in particular how to program computers to process and analyze large amounts of natural langauge data.
* Often when performing analysis, lots of data is numerical, such as sales numbers, physical measurements, quantifiable categories.
* Computers are very good at handling direct numerical information.
* But what do we about <b>text data?</b>
   * Text data is highly unstructured data and can be in multiple languages.
   * NLP attempts to use a variety of techniques in order to create structure out of text data.


### What is Spacy?
1. For many NLP tasks, spacy only has one implemented method, choosing the most efficient algorithm currently available.
2. This means you often don't have the option to choose other algorithms.


### What is NLTK?
1. NLTK - Natural Language Toolkit is a very popular open source.
2. Initially released in 2001, it is much older than spacy.
3. It also provides many functionalities, but includes less efficient implementations.

### NLT vs Spacy
* For many common NLP tasks, spacy is much faster and more efficient, at the cost of the user not being able to choose algorithmic implementations.

### Spacy Tokens
|Tag|Description|
|:------|:------:|
|`.text`|The original word text<!-- .element: style="text-align:left;" -->|
|`.lemma_`|The base form of the word|
|`.pos_`|The simple part-of-speech tag|
|`.tag_`|The detailed part-of-speech tag|
|`.shape_`|The word shape – capitalization, punctuation, digits|
|`.is_alpha`|Is the token an alpha character?|
|`.is_stop`|Is the token part of a stop list, i.e. the most common words of the language?|

* For a full list of Syntactic Dependencies visit https://spacy.io/api/annotation#dependency-parsing
<br>A good explanation of typed dependencies can be found [here](https://nlp.stanford.edu/software/dependencies_manual.pdf)
