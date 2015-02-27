# Problem
We want to investigate on how to make Infinite Jukebox on student server.

# Question
1. How to make the website secured from other users for the student server?
2. How would the password be secured when get hacked?
3. What are limitations of those security options?
4. How to make the website run independently without the logistics that the original Infinite Jukebox has?

# Resources
1. [Website Security Introduction]
2. [Website Security]
3. [MP3 File Uploader]
4. [InfiniteJukebox]

### 1. Mini-abstract and relevance of [Website Security Introduction]
Infinite Jukebox has the option for other users to upload their own mp3 files to make it run through Infinite Jukebox. Therefore, in order to make it protected from other users from filling up and overloading the space on student server, content should only be seen by "authorized" eyes.
The .htpasswd file contains username/password pairs that the user would authorize the access of the website's contents to. The example of creating .htpasswd file is listed below. The user just need to change the path based on the appropriate directory that the user has, prompt a new username, and then list new password for that username respectively. 
The .htpasswod would store an encrypted password corresponding to the appropriate user that would prevent information leaking when the student server is hacked.
```python
htpasswd -c /usr/local/username/safedirectory/.htpasswd john
```
The .htaccess file is one of the possible ways to configure the details of your website without needed to alter the server config files. The period that starts the file name will keep the file hidden within the folder.
The example of .htaccess is listed below. The user just need to change the path of the Author User File that pointed to your .htpasswd:
```python
AuthUserFile /usr/local/username/safedirectory/.htpasswd
AuthGroupFile /dev/null
AuthName "Please Enter Password"
AuthType Basic
Require valid-user
```
The user would also need to change the permission of both files .htaccess and .htpasswd
```python
chmod +x .filename
```
This resource answers question 1 and 2: How to make the website secured from other users for the student server? and How would the password be secured when get hacked?

### 2. Mini-abstract and relevance of [MP3 File Uploader]
A few problems that users would encounter in term of using the .htaccess file are:

- One: Speed—the .htaccess page may slow down your server somewhat; for most servers this will probably be an imperceptible change. 
This is because of the location of the page: the .htaccess file affects the pages in its directory and all of the directories under it. 
Each time a page loads, the server scans its directory, and any above it until it reaches the highest directory or an .htaccess file.
- Two: Security—the .htaccess file is much more accessible than standard apache configuration and the changes are made live instantly (without the need to restart the server). 
Granting users permission to make alterations in the .htaccess file gives them a lot of control over the server itself. 

This resource answers question 3: What are limitations of those security options?

### 3. Mini-abstract and relevance of [InfiniteJukebox]
Looking at the code for the InfiniteJukebox at the moment, the option of uploading the song would puts the song in the amazon web services and then call Echonest for the analysis of the song. However, we need to change the storing option to the local folder on the student server. 
Moreover, we also need to update the API_Key to our instead of abusing their API_Key. 

This resource answers question 4: How to make the website run independently without the logistics that the original Infinite Jukebox has?

[Website Security Introduction]: http://weavervsworld.com/docs/other/passprotect.html
[Website Security]:https://www.digitalocean.com/community/tutorials/how-to-use-the-htaccess-file
[MP3 File Uploader]: http://bytes.com/topic/php/answers/953470-uploading-audio-mp3-file-php
[InfiniteJukebox]: http://labs.echonest.com/Uploader/index.html