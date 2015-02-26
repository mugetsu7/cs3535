# Problem
We want to investigate on collaborative filtering as the method of how popular applications and website do filtering processes to recommend their products for the user. 

# Question
1. How to make the website secured from other users for the student?
2. How would the password be secured when get hacked?
3. How to make the website run independently without the logistics that the original InfiniteJukebox has?

# Resources
1. [Website Security]
2. [Website Security2]
3. [MP3 File Uploader]

### 1. Mini-abstract and relevance of [Website Security]
Services such as Reddit, YouTube, Netflix, Amazon, Digg.com, and Last.fm are typical example of collaborative filtering based media.

This resource answers question 1: What are some popular applications on social web?

### 2. Mini-abstract and relevance of [MP3 File Uploader]
Collaborative filtering is popular recommendation algorithm that bases its predictions and recommendations on the ratings, multiple users/agents, data resources, etc. 
There are two different types of collaborative filtering including User-User and Item-Item Collaborative Filtering
User-User Collaborative Filtering: "I like what you like"
- find other users whose have similar past rating behavior to the current user''s past rating behavior
- use their ratings on other items to predict what the current user will like
Item-Item Collaborative Filtering:
- use similarities between the rating patterns of items
- still deduced from user preference patterns rather than extracted from item data
It would be more scalable to use Item-Item CF for large user bases instead of User-User CF due to the big difference in the Big-O complexity of the searching for the neighbors of a user operations. 

This resource answers question 2 and 4: What is collaborative filtering method? and What are different types of collaborative filtering?

### 3. Mini-abstract and relevance of [Amazon Recommendations]
E-commerce recommendation algorithms often operate in a challenging environment with:
+ Large amounts of data, countless customers and millions of distinct catalog items
+ New customer have limited information 
+ Older customer have too much information

It would be more scalable to use Item-Item CF for large user bases instead of User-User CF due to the big difference in the Big-O complexity of the searching for the neighbors of a user operations. 
Unless the CF uses dimensionality reduction, sampling, or partitioning which would reduce the recommendation quality

The article mentioned search-based methods and cluster method as additional recommendation algorithms 
This resource answers question 3, 5, 6 : Why collaborative filtering is needed?, Which collaborative filtering is more preferable and why?, and What are some other recommendation algorithms/systems?

[Website Security]: http://weavervsworld.com/docs/other/passprotect.html
[Website Security2]:https://www.digitalocean.com/community/tutorials/how-to-use-the-htaccess-file
[MP3 File Uploader]: http://bytes.com/topic/php/answers/953470-uploading-audio-mp3-file-php
