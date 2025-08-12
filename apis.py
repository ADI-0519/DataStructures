import requests

name = "UEFA Champions League"
year = 2011
competition = name
y = 2011
winner_url = f"https://jsonmock.hackerrank.com/api/football_competitions?name={name}&year={year}"
goals = 0


if requests.get(winner_url).status_code == 200:
    response = requests.get(winner_url).json()["data"]
    
winner_team = (response[0]["winner"])


team_url = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={y}&team1={winner_team}&page={1}"

response2 = requests.get(team_url).json()
pages = response2["total_pages"]

for i in range(1,pages + 1):
    team_url = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={y}&team1={winner_team}&page={i}"
    response2 = requests.get(team_url).json()
    print(response2["data"][i-1])
    goals += int(response2["data"][i-1]["team1goals"])
    # print(response2["data"])
    
team_url = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={y}&team2={winner_team}&page={1}"
response2 = requests.get(team_url).json()
pages = int(response2["total_pages"])

for i in range(1,pages + 1):
    team_url = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={y}&team1={winner_team}&page={i}"
    response2 = requests.get(team_url).json()
    goals += int(response2["data"][i-1]["team2goals"])


print(goals)