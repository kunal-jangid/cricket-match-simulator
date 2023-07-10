# Cricket Match Simulator - Assignment

The goal of this assignment is to develop a Python program that simulates a cricket tournament involving various teams with an advanced level of detail. The application has tp be designed to mimic real-world cricket matches and statistics.

---

## Program Requirements:
The program should consist of the following key classes :

### Player
This class should contain information on player stats, such as:

name (e.g., "MS Dhoni")
bowling: 0.2
batting: 0.8
fielding: 0.99
running: 0.8
experience: 0.9
<etc>
These player stats should be used when running the simulation and should affect the probabilities of various events occurring like a boundary, getting out, etc.

### Teams
A team will consist of players. It should have methods like selecting the captain, sending the next player to the field, choosing a bowler for an over, deciding batting order, etc.

### Field
This class will contain factors like field size, fan ratio, pitch conditions, home advantage, etc., which can impact the probabilities of the simulation.

### Umpire
This class will be responsible for chunking probabilities of all the players on the field and predicting the outcome of a ball. The Umpire class will also keep track of scores, wickets, and overs. It can also make decisions on LBWs, catches, no-balls, wide-balls, etc.

###CommentatorThis class will provide commentary for each ball and over. It can use the match stats to give a description of the ongoing game events.

### Match
This class will simulate an individual cricket match. It will use objects of the Teams, Field, and Umpire classes and should have methods to start the match, change innings, and end the match.

---
![screenshot_cricketMatchSimulator](https://github.com/kunal-jangid/cricket-match-simulator/assets/38829114/8089be6f-e146-412a-9b5d-74ccace82a3a)

## How to run the program?
Well I got you covered, just follow these simply steps and the program will display the result in no time at all!
1. Go the `<> Code` and click on `Download ZIP` or simmply clone the github repo using Git Bash : `git clone https://github.com/kunal-jangid/cricket-match-simulator``<br>
![image](https://github.com/kunal-jangid/cricket-match-simulator/assets/38829114/d2d40d79-26d2-4222-8456-db0f5dab5a07)

2. Open `cricketSimulation.py` using your favorite code editor. I will be using VS Code for implementation on my end.
   
3. Run the Python file using `Run and Debug` option and you shall have what you seek. <br>
![image](https://github.com/kunal-jangid/cricket-match-simulator/assets/38829114/d831304e-188f-4d23-a2d9-194cbb1c423e)

---

Demo Link - https://youtu.be/OMMSAoOSf4E
