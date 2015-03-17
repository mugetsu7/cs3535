# Problem
We want to investigate on how to judge the users on their ability to judge the transition of the song on Infinite Jukebox. 

# Question
1. What are the visions and regulations of the InfiniteJukebox Transition Detection Game?
2. How to make button that would link to the space bar button on the keyboard?
3. How does InfiniteJukebox represent beats?
4. How does InfiniteJukebox do the transition?	

# Resources
1. [Make Button]
2. [Space Bar Button]
3. [InfiniteJukebox]

### 1. Mini-abstract
Dr. Parry has helped guide me to think of making InfiniteJukebox as a Transition Detection game to study users on their ability to judge the transition of the song on Infinite Jukebox. The game would prompt the user to listen to a song on their choice. There would be transition occurred along the song and the user have 4-8 beats time frame to hit the space bar button to indicate that they heard the transition. 
The game will keep track of the actual transitions that occurs, the transitions that the user was able to detect, and the transitions that the user falsely detect.   
This resource answers question 1: What are the visions and regulations of the InfiniteJukebox Transition Detection Game?

### 2. Mini-abstract and relevance of [Make Button] and [Space Bar Button]
Button function is self-explanatory. However, we want something to happen as a function to run when the button is click so we need a button categorized as onclick Event button which is different from the normal button. The button shall calls a function in javascript code section as it is clicked to do the work of categozing the detected transition is true or false. 
```python
<button onclick="myFunction()">Click me</button>
```
Moreover, the user has two options with the button, they can click on it or they can click the space bar which is more convenient and it still activate the button as the same time. So in myFunction in javascript section we need to check if the space bar button is pressed before working on anything else. Looking at this code below, e.keyCode of 32 is the particular keyCode representing the assign number for space bar:
```python
$.keyup(function(e){
	if(e.keyCode == 32){
       // user has pressed space
       
	}
});
```
This resource answers question 2: How to make button that would link to the space bar button on the keyboard? 

### 3. Mini-abstract and relevance of [InfiniteJukebox]




This resource answers question 3 and 4: How does InfiniteJukebox represent beats? and How does InfiniteJukebox do the transition?	

[Make Button]: http://www.w3schools.com/jsref/event_onclick.asp
[Space Bar Button]: http://stackoverflow.com/questions/2249203/check-if-the-spacebar-is-being-pressed-and-the-mouse-is-moving-at-the-same-time
[InfiniteJukebox]: http://labs.echonest.com/Uploader/index.html
