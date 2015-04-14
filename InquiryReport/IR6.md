# Problem
How to improve the InfiniteJukebox Transition Detection Game?

# Question
1. What are some areas for improvements for the game?
2. How do the game start and end?
3. How to hide an object on the website without affecting negatively the functionality of the object?
4. How to change the image at the specific event?


# Resources
1. [Change IMG SRC]
2. [Hide Object]
3. [InfiniteJukebox]
4. [file]
5. [image]

### 1. Mini-abstract
The version of InfiniteJJ is the experiment still having the tile circle of beats from the original Infinite Jukebox to test if all the variables actual detections, detected transition, false positive transition, and false negative transition work. Therefore, user can easily see the transition makes and detect the transition. However, hiding the tile circle of beat along with the actual transitions row of the data table would greatly improve the level of difficulty because users have to solely depend on their ears then. A total score row can be added to keep track of all the points. It was set up previously is that if the transition was made and the user pressed down the plus button on the right key pad then the detected transitions value would increment until the fifth beat after making the transition. It is problematic because the user can score 50 points on detected transition at once while the user was only able to detect one transition. Therefore, there are possible updates so that within the four beats after the transition is made, the user can only score one time regardless of continuously pressing down but the earlier the user press the button the more point the user would get. 

This resource answers question 1: What are some areas for improvements for the game?


### 2. Mini-abstract and relevance of [InfiniteJukebox]
The game would start with the user pressing the space bar or clicking on the play button on the right corner below the title. The user would start up with 20 points in the beginning. The second the user's total score gets down to 0, the game stop and the user loses or the user can just play while enjoying their favorite song forever if the user is good enough.  

The code would check every time the user pressed the plus button on the right keypad to see if the totalS is 0 or below. If yes, the game and the music player stop. If not, the game continues. Moreover, there would be an image above the data table there to indicate game start or game end. 

This resource answers question 2: What are some methods to be used to retrieve the original song from the cover songs? and What are some impacts and aims of this research?  

### 3. Mini-abstract and relevance of [Change IMG SRC]

Before the data table, there would be an image [file] indicate the game start.
```python
<img id="myImg" src="http://oyster.ignimgs.com/wordpress/write.ign.com/19477/2013/07/Press-Start-600x375.jpg" width="300" height="300">
```
When the game ends, this [image] would show instead:		
```python
document.getElementById("myImg").src = "http://bbsimg.ngfiles.com/1/24409000/ngbbs50e4c67b0376b.jpg";
```
When the space bar is pressed to retry the game, the original image [file] would show 
```python
document.getElementById("myImg").src = "http://oyster.ignimgs.com/wordpress/write.ign.com/19477/2013/07/Press-Start-600x375.jpg";
```

### 4. Mini-abstract and relevance of [Hide Object]

```python
<div style = "display: none"> 
	<span id='tiles'> </span> 
</div>
```

[Change IMG SRC]: http://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_img_src2
[Hide Object]: http://www.w3schools.com/jsref/prop_style_display.asp
[InfiniteJukebox]: http://labs.echonest.com/Uploader/index.html
[file] : http://oyster.ignimgs.com/wordpress/write.ign.com/19477/2013/07/Press-Start-600x375.jpg
[image] : http://bbsimg.ngfiles.com/1/24409000/ngbbs50e4c67b0376b.jpg

