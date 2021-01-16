## Term Frequency - Inverse Term Frequency(TF-IDF)
* Term frequency tf(t,d): is the raw count of a term in a document, i.e the number of a times that term `t` occurs in a document `d`.
    * `tf(t,d) = count of t in d / number of words in d`
* However, Term Frequency alone isn't enough for a thorough feature analysis of the text!
* Let's imagine very commong terms, like "a", or "the".., because the term "the" is so common, term frequency will tend to incorrectly emphasize documents which happen to use the word "the" more frequently, without giving enough weight to the more meaningful terms "red" and "dogs".
* An inverse document frequency factor is incorporated which diminishes the weight of terms that occur very frequently in the document set and increases the weight of terms that occur rarely.
* It is logarithmically scaled inverse fraction of the documents that contain the word(obtained by dividing the total number of documents by the number of documents containing the term, and then taking the logarithm of that quotient)
    * `df(t) = occurrence of t in documents`
    * `idf(t) = N/df`
    * `idf(t) = log(N/(df + 1))`
* During the query time, when a word which is not in vocab occurs, the df will be 0. As we cannot divide by 0, we smoothen the value by adding 1 to the denominator.
* `tf-idf(t, d) = tf(t, d) * log(N/(df + 1))`