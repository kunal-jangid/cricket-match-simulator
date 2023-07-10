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

---

Demo Link - https://youtu.be/OMMSAoOSf4E
