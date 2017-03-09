Kerry McConnaughay and Anika Payano
Project 4 - Interactive Programming

**Project Overview**

The goal of our project was to use visual input from the webcam to control music playing from the computer. The part of the project that controls the webcam allows the user to interact by pressing down keys on the keyboard to take pictures for three different commands: play, stop, and change (shuffles music). This, in turn, would allow us to control the music playback by determining if these images exist. If they did, the user could then move forward and manipulate the music playback. 

**Results**

We were able to write fully functional code for the webcam that initializes the webcam and takes snapshots of the screen created in the program when prompted by keys on the keyboard. After capturing the images, another part of the code saves these images under specific file names. The keys the user can press are 'p', 's', and 'c'. The image that plays the music is saved by pressing 'p', the image saved by 's' would stop the music, and the image saved by 'c' change to the next song. 

The image below shows what the terminal says while the music is playing on the computer. There are directions for which keys to press while the music is playing. With a few more functions, we were able to write code that allows the user to shuffle songs without having to stop the music before changing the song. This library is saved on the computer and could be expanded easily.


![terminal]
(terminal.jpeg)

Look at these videos by clicking on the links below.  
[Functional Example](https://goo.gl/photos/sJZFpJsXKpvtFuUNA)  
[Disfunctional Example](https://goo.gl/photos/BtXQyyNE8zBDnFfC9)  

The first video gives step-by-step directions on how to use the program and also shows what happens when there are no images saved from the webcam. If the user does not capture any snapshots from the webcam, then the music will not play, stop, or shuffle because of the conditions we included. This is shown in the second video. Files with the names we specified must exist (the statement is true) in order for the user to listen to any music.

**Implementation**

At a system architecture level, there are multiple steps the data goes through before the music stops. First, the user poses in front of the camera while the webcam is on. The user then presses one of the defined keys in the events method to save the pictures, which are evaluated in another class. The presence of these images allows the user to control the playing, stopping, and shuffling of the music. When the images are not saved, there is no way to control the music player and no music will play.
A major part of the program is the events that allow the user to capture images from the webcam. By pressing different keys, the user saves the necessary images in the directory. There are many small parts to the Camera class, including the construction of the surface and the events method that provides the framework for the keys to work. The program moves to another major component of the code, the music player. The most important parts of that code are the methods and functions that play and stop the music when given input. There is also a necessary part that chooses songs randomly from the library where the songs are saved in the directory.

In the webcam part of the project, there were multiple different ways to process the images the user saves. We could have used thresholds, different surface arrays, found blobs in the images, or even taken the average color of a certain area of the screen and returned that value. Ultimately, we chose the existence of certain files in the directory. Originally, we had planned on using hand gestures, but opencv never worked, so we had to move away from that path. It was hard to pick how to process the images because we knew nothing about processing images in these different ways, so we chose the most straightforward path we thought of: using the existence of the images as a condition.

![MVC]
(MVC.jpeg)

**Reflection**

Overall, we would say the research and implementation of new concepts went well. Neither of us had any experience with pygame or code relating to the webcam and music. Through lots of reading and many documentations, we were able to build a solid base of knowledge about the subject and implement our program. In terms of improvements, it would be better if next time, we started off writing our code using classes, methods, and attributes. Initially, we wrote plain functions and then switched to classes later, which led to more debugging and wasted time. It would have also been more helpful to start out by writing on paper what our program needed to do. Before writing, we spoke about the different components we thought we would need, but that was not as useful as written diagrams. We did not have completely solid plans for unit testing, but ran small tests while writing the code. After writing one part of the code, we would test it to make sure there were no errors before moving on. There are a few subjects that we wished we could have known about before beginning this project including how to integrate two separate programs with each other, multiprocessing and threading, and how classes apply to programs that do more than print results, such as the webcam and music programs.

We planned on dividing the work into the two main components of the project: the webcam and music. When we were together, we each worked on our part and asked questions when we needed help. There were times when each of us worked alone on the project, but it was usually after we had been together and we knew what we needed to debug and research to move forward in the project. A lot of the time ended up being devoted to researching and reading documentation because of the obstacles we encountered. Once we realized that opencv would not work, we decided to take on a different project because we had already spent a lot of time trying use that library. After the check-in, we were hopeful and chose to go back to our original project. In the future, we would both continue to do the new project even though we were mostly successful by the end of the project because of how much frustration it caused us. The biggest takeaway from switching back and forth is how important it is to chose one topic and stick with it. We did not have any problems working together besides the frustration caused by the failures of our programming.

