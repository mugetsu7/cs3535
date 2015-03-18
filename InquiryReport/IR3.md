# Problem
We want to investigate on how to judge the users on their ability to identify the occurrence of transitions of the song on Infinite Jukebox. 

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
This answers question 1: What are the visions and regulations of the InfiniteJukebox Transition Detection Game?

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
There are two crucial variables that InfiniteJukebox has including tile and branch. Tile is the array/list of tiles in which each tile representing one beat and together tiles compose the whole circle visualization representing the whole song. There are different kinds of branch such as last, long, reverse, or sequential branch. However, branch in general represent the possible jump or possible transition at that specific tile where the cursor is at to another arbitrary tile or beat in the circle or song that is considered or evaluated as the best transition.

Basically, for each possible transition location that the cursor lands on, it would randomly see if the cursor would take that transition and jump to the tile at the end of the branch or just continue to move to the next sequential tile. 

Technically, when the Driver function is called inside the javascript code block, it would pass in the tile to the selectRandomNextTile function to process the request and make the movement. selectRandomNextTile would pass in the current tile to shouldRandomBranch to decide yes or no to take the transition or the jump. shouldRandomBranch then responds the decision back to selectRandomNextTile to complete the process and movement of the cursor.  

Therefore, Driver would be the best option as far as location for inserting the extra integration to make InfiniteJukebox into InfiniteJukebox Transition Detection Game. We would be able to write most of the details in here. Especially, we want the user to have 4-8 beats time frame to hit the space bar so we would want to flag the program to make sure that it would not take any immediate transition until 4-8 beats have passed in Driver function. 

This resource answers question 3 and 4: How does InfiniteJukebox represent beats? and How does InfiniteJukebox do the transition?	

[Make Button]: http://www.w3schools.com/jsref/event_onclick.asp
[Space Bar Button]: http://stackoverflow.com/questions/2249203/check-if-the-spacebar-is-being-pressed-and-the-mouse-is-moving-at-the-same-time
[InfiniteJukebox]: http://labs.echonest.com/Uploader/index.html
