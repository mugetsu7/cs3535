# Problem
How to identify and retrieve audio-based cover song

# Question
1. How do we want to maximize retrieval results of the original song from the cover songs?
2. What are the usage from having cover song detection?
3. What are some methods to be used to retrieve the original song from the cover songs?
4. What are some impacts and aims of this research?  
5. What are other methods have been used to approach this problem?	

# Resources
1. [Approximate Chord Sequences]
2. [Information Theoretic Measures of Similarity]

### 1. Mini-abstract of [Approximate Chord Sequences]
Renditions are often quite different from the original in one or many attributes including instrumentation, key or genre. One has to consider not only the key or tempo differences between cover song sequences, but also the ways in which these chord sequences approximate (or not) the songs they represent

In order to represent and model music signals for cover song detection, a variety of methods have been proposed involving cross-correlation, alignment techniques, cross-recurrence analysis, and time series prediction.

From having cover song detection, potential applications includes automated music recommendation, copyright infringement detection, and musicological research

This resource answers question 1, 2, and 5: How do we want to maximize retrieval results of the original song from the cover songs? and What are the usage from having cover song detection? and What are other methods have been used to approach this problem?	



### 2. Mini-abstract and relevance of [Information Theoretic Measures of Similarity]

This research based on a variation on the theme of using string alignment for Music Information Retrieval in the context of cover song identification in audio collections. Here, the strings are derived from audio by means of Hidden Markov Model -based chord estimation. The characteristics of the cover-song ID problem and the nature of common chord estimation errors are carefully considered. There are three areas needed to be considered including estimating chord sequences and sequence alignment.

- Firstly, on the topic of Estimating Chord Sequence, the approach is used as the front end to our cover song identification system. First, 36-dimensional chroma vectors, or pitch-class profiles, are calculated from the audio signal. These vectors are tuned and, optionally, averaged within beats, before being quantized into 12-bits vectors representing the spectral energy distribution across notes of the chromatic scale. These features are used as observations on a 24-state hidden Markov model, where each state corresponds to one of the major and minor triads. The parameters of the model, initialized using simple musical knowledge, are trained in an unsupervised fashion using the Expectation-Maximization (EM) algorithm. The final sequence of triads is obtained by decoding the model using the Viterbi algorithm.

- Secondly, on the topic of Sequence Alignment, finding the globally-optimal alignment between strings is an extensively researched topic. The works involve with substitution matrix and key-invariant alignment. The idea is to find the best possible path between the strings by allowing inexact character matches (i.e. substitutions or swaps) and the introduction of gaps in either of the sequences. In this context, the best path is the one that maximizes a score function, usually the sum of individual scores for aligned pairs of characters, under the consideration that both gap insertions and substitutions imply a penalty. 

The experiment is done through 4 testings including testing shifts, testing gaps, testing beats, and testing swaps.
The research measures the impact of actions including key-shifting; varying the gap penalty used by the scoring algorithm, changing the distribution of positive and negative values on the substitution matrix by varying the offset value; and using beat synchronous instead of frame-based chroma features for the sequence estimation 

This resource answers question 3 and 4: What are some methods to be used to retrieve the original song from the cover songs? and What are some impacts and aims of this research?  

[Approximate Chord Sequences]: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.205.8766&rep=rep1&type=pdf
[Information Theoretic Measures of Similarity]: http://www.eecs.qmul.ac.uk/~peterf/foster_icassp2013.pdf
