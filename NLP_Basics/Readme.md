# Natural Language Processing
* An area of computer science and artificial intillegence concerned with the interactions between computers and human(natural) langauges, in particular how to program computers to process and analyze large amounts of natural langauge data.
* Often when performing analysis, lots of data is numerical, such as sales numbers, physical measurements, quantifiable categories.
* Computers are very good at handling direct numerical information.
* But what do we about <b>text data?</b>
   * Text data is highly unstructured data and can be in multiple languages.
   * NLP attempts to use a variety of techniques in order to create structure out of text data.


## What is Spacy?
1. For many NLP tasks, spacy only has one implemented method, choosing the most efficient algorithm currently available.
2. This means you often don't have the option to choose other algorithms.


## What is NLTK?
1. NLTK - Natural Language Toolkit is a very popular open source.
2. Initially released in 2001, it is much older than spacy.
3. It also provides many functionalities, but includes less efficient implementations.

## NLT vs Spacy
* For many common NLP tasks, spacy is much faster and more efficient, at the cost of the user not being able to choose algorithmic implementations.

## Spacy Tokens
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

___
## TOKENS
* Tokens are basic building blocks of a Doc Subject-everythin that helps us understanding the meaning of the text is derived from the tokens and their relationship to one another.
* <b>Prefix:</b> Character(s) at the beginning <b>(dollar sign, (, ")</b>
* <b>Suffix:</b> Character(s) at the end <b>(km, ),.!")</b>
* <b>Infix:</b> Character(s) in between <b>(-, --, /, ...)</b>
* <b>Exception:</b> Special-case rule to split a string into several tokens or prevent a token from being split when punctuation rules are applied<b>(let's, U.S.)</b>
___
## Stemming
* Often when searching text for a certain keyword, it helps if the search returns variations of the word.
* For instance, searching for "boat" might also return "boats" and "boating". Here, "boat" would be the stem for (boat, boater, boating, boats).
* Stemming is a somewhat crude method for cataloging related words; it essentially chops off letters from the end until the stem is reached.
* This works fairly well in most cases, but unfortunately English has many exceptions where a more sophisticated process is required.
* One of the most common - and effective - stemming tools is Porter's Algorithm developed by Martin Porter in 1980.
* The algorithm employs five phases of word reduction, each with its own set of mapping rules.
    * In first phase, simple sufix mapping rules are defined.
    * More sphosticated phases consider the length/complexity of the word before applying a rule.
___
## Lemmatization
* In contrast to stemming, lemmatization looks beyond word reduction, and considers a language's full vocabulary to apply a morphological analysis to words.
* The lemma of 'was' is 'be' and the lemma of 'mice' is 'mouse'. Further, the lemma of 'meeting' might be 'meet' or 'meeting' depending on its use in a sentence.
