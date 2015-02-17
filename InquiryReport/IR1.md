# Problem
We want to investigate on collaborative filtering as the method of how popular applications and website do filtering processes to recommend their products for the user. 

# Question
1. What are some popular applications on social web?
2. What is collaborative filtering method?
3. Why collaborative filtering is needed?
4. What are different types of collaborative filtering?
5. Which collaborative filtering is more preferable and why?
6. What are some other recommendation algorithms/systems?

# Resources
1. [Collaborative Filtering]
2. [Collaborative Filtering Recommender Systems]
3. [Amazon Recommendations]

### 1. Mini-abstract and relevance of [Collaborative Filtering]
Services such as Reddit, YouTube, Netflix, Amazon, Digg.com, and Last.fm are typical example of collaborative filtering based media.

This resource answers question 1: What are some popular applications on social web?

### 2. Mini-abstract and relevance of [Collaborative Filtering Recommender Systems]
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

[Amazon Recommendations]: http://www.cs.umd.edu/~samir/498/Amazon-Recommendations.pdf
[Collaborative Filtering Recommender Systems]: http://files.grouplens.org/papers/FnT%20CF%20Recsys%20Survey.pdf
[Collaborative Filtering]: http://en.wikipedia.org/wiki/Collaborative_filtering
