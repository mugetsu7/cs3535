# Problem
We want to fix some limitations of InfiniteJukebox Transition Detection Game and alter how the website record the activities of the user!

# Question
1. What are some limitations of the game and the recording system of the activities of the user throughout the game?
2. How do we fix the limitations of the game?
3. How do we print out next line in the text file?
4. How do we record the current time?
5. How do we record the user's IP?
6. How do we record the beat where the transition starts and the beat which is the transition's destination of the transition?

# Resources
[InfiniteJukebox]: http://labs.echonest.com/Uploader/index.html
[Create Downloadable TextFile] : http://jsfiddle.net/UselessCode/qm5AG/
[New Line]: http://stackoverflow.com/questions/11058884/newlines-are-missing-after-downloading-txt-file-through-the-browser
[IP Address]: http://stackoverflow.com/questions/391979/get-client-ip-using-just-javascript


### 1. Mini-abstract
Currently, the game only ends when the user falsely detected transitions that resulted in total score less than or equal to 0. However, the game would not end even if the user misses a transition which results in less than or equal to 0. 
Moreover, the recording system at the moment is the hidden textarea that we keep adding more text in the javascript as events that let the user download them in the end. However, because we are writing in the textarea, the next line character is eliminated in the process of writing from javascript. For researching purposes, it would not be pleasant and professional to read through the file that is not organized. Moreover, there is no identification such as IP address included. It only records the beat without time(one beat < one second). For the transition, it only records the current beat instead of the beat where the transition starts and the beat which is the transition's destination (especially since the user have the 4 beats period to detect the transition).

### 2. Mini-abstract and relevance of [InfiniteJukebox]
I applied the same concept as when the user falsely detected a transition that results in the total score less than or equal to 0 with calling "driver.stop()". However, even when the driver is stop, the song is still playing in the background. I tried calling "player.stop()" as well but it also did not work. I finally tried "tile = null" after checking the value of total score variable.

For researching purposes, it is professional for the report to show not only the current beat but also the current time since value of one beat is less than value of one second. Therefore, I made a global variable called time where I took the current time subtract the starting time and put it into secondsToTime() to convert it into a string of organized hour, minute, and second as shown below:
```javascript
time =  secondsToTime((now() - startTime) / 1000.);
```
Currently, we have a global variable that keeps track of the beat in which is the transition's destination but not the transition's starting beat. In selectRandomNextTile() method, which takes in seed as the parameter or collection of tiles before it does all the transiting in the method, I let B_Tile variable keeps track of the transition starting beat. Moreover, since it is deciding the transition of the next beat, we need to subtract one to actually the transition starting beat as shown below:
```javascript
B_Tile = seed.q.which - 1;
```
While the transition's destination beat is still the same as shown below:
```javascript
var tile = next.dest.tile;
D_Tile = tile.which;
```

This resource answers question 2, 4, and 6: How do we fix the limitations of the game?, How do we record the current time?, and How do we record the beat where the transition starts and the beat which is the transition's destination of the transition?
### 3. Mini-abstract and relevance of [Create Downloadable TextFile]


### 4. Mini-abstract and relevance of [New Line]

Before the data table, there would be an image [File] indicate the game start.
```python
<img id="myImg" src="http://oyster.ignimgs.com/wordpress/write.ign.com/19477/2013/07/Press-Start-600x375.jpg" width="300" height="300">
```
When the game ends, this [Image] would show instead:		
```python
document.getElementById("myImg").src = "http://bbsimg.ngfiles.com/1/24409000/ngbbs50e4c67b0376b.jpg";
```
When the space bar is pressed to retry the game, the original image [File] would show 
```python
document.getElementById("myImg").src = "http://oyster.ignimgs.com/wordpress/write.ign.com/19477/2013/07/Press-Start-600x375.jpg";
```

### 5. Mini-abstract and relevance of [IP Address]
The original tag that contains the tile circle of beats for InfiniteJukebox is shown as below: 
```python
<div> 
	<span id='tiles'> </span> 
</div>
```
Yet, in order to truly test the users' ability to determine the transitions of beats within a song, the visualization would not be needed even when its functionality still matter. Therefore, in order to hide the object which is the tile circle of beats without affecting the functionality of it through the style aspect (style = "display: none") inside the div tag as shown below: 
```python
<div style = "display: none"> 
	<span id='tiles'> </span> 
</div>
```

[IP Address]: http://stackoverflow.com/questions/391979/get-client-ip-using-just-javascript
[New Line]: http://stackoverflow.com/questions/11058884/newlines-are-missing-after-downloading-txt-file-through-the-browser
[InfiniteJukebox]: http://labs.echonest.com/Uploader/index.html
[Create Downloadable TextFile] : http://jsfiddle.net/UselessCode/qm5AG/


