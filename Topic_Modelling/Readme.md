## Topic Modeling
* Topic Modeling allows for us to efficiently analyze large volumes of text by clustering documents into topics.
* A large amount of text data is unlabeled meaning we won't be able to apply our supervised learning approaches to create machine learning models for the data!
* If we have unlabeled data, then we can atempt to *discover* labels.
* In this case of text data, this means attempting to discover clusters of documents, grouped together by topic.
* A very important idea to keep in mind here is that we don't know the **correct** topic
* All we know is that the documents clustered together share similary topic ideas.
* It is up to user to identify what these topics represent.

## Latent Dirichlet Allocation(LDA)
* There is a probability distribution named after "Dirichlet Distribution".
* Latent Dirichlet Allocation is based off this probabiltiy distribution.
* In 2003 LDA was first published as a graphical model for topic discovery in a Journal.
* Assumptions of LDA for Topic Modeling:
    * Documents with similar topics similar groups of words.
    * Latent topics can then be found by searching for groups of words that frequently occur together in documents across the corpus
    * Documents are probability distributions over latent topics.
    * Topics themselves are probability distributions over words.

## Non-negative Matrix Factorization
* Non-negative Matrix Factrorization is an unsupervised algorithm that simultaneously performs dimensionality redcution and clustering.
* We can use it in conjuction with TF-IDF to model across documents.
* Given a non-negative matrix A, find k-dimension approximation in terms of non-negative factors W and H.
* Approximate each object (i.e. column of A) by a linear combination of k reduced dimensions or "basis vectors" in W.
    * A = (n, m) dimensions Data matrix (Rows = Features, Cols = Objects)
    * W = (n, k) dimensions Basis Vectors (Rows = Features)
    * H = (k, m) dimensions Coefficient Matrix (Cols = Objects) 
* Each basis vector can be interpreted as a cluster(Basis Vectors). The membership of objects in these cluster encoded by H(Coefficient matrix).
* Input: Non-negative data matrix(A), number of basis vectors(k), initial values for factors W and H(e.g. random matrices).
* Objective Function: Some measure of reconstruction error between A and the approximation WH.
    
