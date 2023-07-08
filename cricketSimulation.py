import random



# Player class tells us about player stats and probability of certain   
class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience



class Teams:
    def __init__(self, name, teamplayers):
        self.name = name
        self.teamplayers = teamplayers
        self.batsmen = []
        self.bowlers = []
        self.captain = None

    def captain_up(self, captain):
        self.captain = captain
    
    def next_batsman(self):
        if len(self.batsmen) >= 1:
            return self.batsmen.pop()
        else:
            return None
    def next_bowler(self):
        if len(self.bowlers) >= 1:
            return self.bowlers.pop()
        else:
            return None
    
    def batting_order(self, batsmen):
        return random.shuffle(batsmen)
    

class Field:
    def __init__(self, field_size, fan_ratio, pitch, home_advantage):
        self.field_size = field_size
        self.fan_ratio = fan_ratio
        self.pitch = pitch
        self.home_advantage = home_advantage

class Umpire:
    def __init__(self, stadium):
        self.stadium = stadium
        self.score = 0
        self.wickets = 0
        self.overs = 0
    
    def update_score(self, runs):
        self.score += runs

    def update_wickets(self):
        self.wickets += 1

    def update_overs(self):
        self.overs += 1

    def event_prediction(self, bowler, batsman):
        batting_prob = batsman.batting * self.stadium.pitch * random.random()
        bowling_prob = bowler.bowling * self.stadium.pitch * random.random()
        
        return bowling_prob > batting_prob

class Commentator:
    def __init__(self,umpire):
        self.umpire = umpire
    
    def toss_info(self, country_1, country_2):
        batting_team = bool(random.choice([country_1, country_2]))
        return batting_team

    def match_info(self, country_1, country_2, overs):
        print(f"\n{country_1.name} Versus {country_2.name}\nCaptain for {country_1.name}: {country_1.captain.name}\nCaptain for {country_2.name}: {country_2.captain.name}\nTotal Overs: {overs}\n\n\n")

    def ball_played(self, bowler, batsman):
        if self.umpire.event_prediction(bowler, batsman):
            return f"{batsman.name} is clean bowled!"
        else:
            return f"And like that {batsman.name} takes an amazing shot!"
    
    def fielding_prediction(self, fielder):
        if random.uniform(0,1) < fielder.fielding:
            return f"{fielder} caught the ball mid-air! That's an OUT!"
        else:
            return None

    def match_info_current(self, balls):
        return f"\nScore: {self.umpire.score}\nWickets: {self.umpire.wickets}\nOvers: {self.umpire.overs}\nTotal Balls: {balls}\n"

    def inning_end(self):
        print(f"\n-------------Final score: {self.umpire.score} | Wickets: {self.umpire.wickets} | Overs: {self.umpire.overs} -------------\n")

    def match_end(self, country, difference):
        if difference[1] == "all_out":
            print(f"{country} wins by {difference[0]} wickets!")
        else:
            print(f"{country} wins by {difference[0]} runs!")


class Match:
    def __init__(self, country_1, country_2, field, max_overs):
        self.country_1 = country_1
        self.country_2 = country_2
        self.field = field
        self.umpire = Umpire(stadium)
        
        #commentator derived from umpire object just created* - pesky mistake gotta keep this in mind
        self.commentator = Commentator(self.umpire)
        self.max_overs = max_overs

    def begin(self):
        self.country_1.captain_up(random.choice(self.country_1.teamplayers))
        self.country_2.captain_up(random.choice(self.country_2.teamplayers))
        
        self.country_1.batsmen = self.country_1.teamplayers.copy()
        self.country_2.batsmen = self.country_2.teamplayers.copy()
        self.country_1.bowlers = self.country_1.teamplayers.copy()
        self.country_2.bowlers = self.country_2.teamplayers.copy()
        self.commentator.match_info(self.country_1, self.country_2, self.max_overs)

        #for match start, let's go for toss
        team1 = self.commentator.toss_info(self.country_1, self.country_2)
        if team1:
            team2 = self.country_2
            team1 = self.country_1
        else:
            team2 = self.country_1
            team1 = self.country_2
        
        print(f"\n\n{team1.name} begins with batting first!\n")
        self.play_innings(team1,team2)
        self.commentator.inning_end()

        setScore = self.commentator.umpire.score

        self.commentator.umpire.score = 0
        self.commentator.umpire.wickets = 0
        self.commentator.umpire.overs = 0

        print(f"\n\nNow it's {team2.name}'s turn to show us some batting!\n")
        #roles reversed, team2 does the batting
        self.play_innings(team2, team1)
        self.commentator.inning_end()

        finalScore = self.commentator.umpire.score

        if setScore>finalScore:
            self.commentator.match_end(team1.name, [setScore-finalScore, "High score"])
            
        elif finalScore>setScore:
            self.commentator.match_end(team2.name, [finalScore-setScore, "High score"])
        else:
            print("\nIt's a DRAW.")

    #match happen here, runs and wickets updated through continuity of the program
    def play_innings(self,batsmen, bowlers):
        balls = 1
        over = 1
        bowler = bowlers.next_bowler()
        batsman = batsmen.next_batsman()

        while self.commentator.umpire.overs<self.max_overs:
            self.commentator.match_info_current(balls)
            event_ball = self.commentator.ball_played(bowler, batsman)
            print(event_ball)

            if event_ball.endswith("bowled!"):
                batsman = batsmen.next_batsman()
                if batsman is None:
                    break
                self.umpire.update_wickets()
                print(f"\nWickets: {self.umpire.wickets}\nBalls: {balls}\n")
                print(f"\nIncoming new batsman: {batsman.name}")
            else:
                runs = random.choice([1,2,3,4,6])
                fielder = random.choice(bowlers.teamplayers)
                fielding_prediction = self.commentator.fielding_prediction(fielder)
                if fielding_prediction is None:
                    self.umpire.update_score(runs)
                else:
                    print(f"{batsman.name} just got a wicket down")
                    batsman = batsmen.next_batsman()
                    if batsman is None:
                        break
                    self.umpire.update_wickets()
                    print(f"\nWickets: {self.umpire.wickets}\nBalls: {balls}\n")
                    print(f"\nIncoming new batsman: {batsman.name}\n")

            if balls == 6:
                over += 1
                self.umpire.update_overs()
                bowler = bowlers.next_bowler()
                balls = 0
                print(f"Starting over: {self.commentator.umpire.overs}")
            
            self.commentator.match_info_current(balls)
            balls += 1

            


# demo simmulation between India and Australia

teamIndia = []
for each in range(0,10):
    teamIndia.append(Player(
        "Ind_Player_"+str(each),
        random.uniform(0,0.9), #bowling
        random.uniform(0.6,0.9), #batting
        random.uniform(0,0.6), #fielding
        random.uniform(0,1.0), #running
        random.uniform(0,1.0) #experience
    ))


#for fairness the stats are generated using random library for the sake of fairness
teamAustralia = []
for each in range(0,10):
    teamAustralia.append(Player(
        "Aus_Player_"+str(each),
        random.uniform(0,0.8), #bowling
        random.uniform(0.40,1.0), #batting
        random.uniform(0,0.5), #fielding
        random.uniform(0,1.0), #running
        random.uniform(0,1.0) #experience
    ))


firstTeam = Teams("India",teamIndia)
secondTeam = Teams("Australia", teamAustralia)

stadium = Field(
    "Medium", #field size
    round(random.uniform(0.5,0.8),2), #fan ratio
    round(random.uniform(0.85,1),2), #pitch
    round(random.uniform(0,1),2) #home advantage
)

total_overs = 10
match = Match(firstTeam,secondTeam, stadium, 10 )
match.begin()