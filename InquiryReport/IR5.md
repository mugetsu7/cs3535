# Problem
How does Shazam or other software recognize and identify songs? 

# Question
1. What are the steps necessary of the recognizing and identifying process?
2. What are the usage from having song recognizer?
3. How do Shazam analyze and recognize a song?
4. What are some limitations of the algorithms?

# Resources
1. [Shazam It!]
2. [An Industrial-Strength Audio Search Algorithm]

### 1. Mini-abstract of [Shazam It!]
Often in the day, people hear a really good song or a familiar one in the public setting. They enjoyed that song a lot a long time ago and desperately wanted to heart it again, but can’t remember its name! However given they have a phone and data, they are saved with the mobile app such as Shazam.

Moreover, the app can be used in order to determine and identify plagiarism in music, or to find out who was the initial inspiration to some pioneers of blues, jazz, rock, pop or any other genre given the fact that we have a well-rounded and in-depth database of collection of music.

The steps including: capturing the song, conversion to appropriate frequency domain, analyzing and fingerprinting, hashing it, and then search for the marching song with the hashing data in the database.  

This resource answers question 1, and 2: What are the steps necessary of the recognizing and identifying process? and What are the usage from having song recognizer?

### 2. Mini-abstract and relevance of [An Industrial-Strength Audio Search Algorithm]

In the environment with the presence of highly significant noise and distortion, they experimented with a variety of candidate features that could survive GSM encoding in the presence of noise for sound analysis. Spectrogram peaks has been decided to be one of the means for that. due to their robustness in the presence of noise and approximate linear superposability. A time-frequency point is a candidate peak if it has a higher energy content than all its neighbors in a region centered around the point. 

Fingerprint hashing is the next step which they processed from the constellation map, in which pairs of time-frequency points are combinatorially associated. Anchor points are chosen, each anchor point having a target zone associated with it. 

The previous operation is carried out on each track in a database to generate a corresponding list of hashes and their associated offset times to receive a database index. Track IDs may also be appended to the small data structs, yielding anggregate 64-bit struct, 32 bits for the hash and 32 bits for the time offset and track ID. To facilitate fast processing, the 64-bit structs are sorted according to hash token value. 

The bins are scanned for matches after all sample hashes have been used to search in the database to form matching time pairs. Within each bin the set of time pairs represents a scatterplot of association between the sample and database sound files. The presence of a statistically significant cluster in a scatterplot of database time versus sample time for a track that does not match the sample indicates a match. This bin scanning process is repeated for each track in the database until a significant match is found. 

There are two limitations to the algorithm: 
- Firstly, the approach the algorithm took was search and recognize sound files that are already present in the database. It is not expected to generalize to live recordings, another version of the song, cover songs, or plagiarized songs. 
- Secondly, the recording will include a lot of noise that will introduce some error in the matches. Yet, Shazam would only do eliminate all but the correct song from our list of matches

This resource answers question 3 and 4: How do Shazam analyze and recognize a song? and What are some limitations of the algorithms?

[Shazam It!]: http://www.toptal.com/algorithms/shazam-it-music-processing-fingerprinting-and-recognition
[An Industrial-Strength Audio Search Algorithm]: https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf
