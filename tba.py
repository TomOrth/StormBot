import requests
import json
URL = 'http://www.thebluealliance.com/api/v2/'
HEADER_KEY = '?X-TBA-App-Id='
HEADER_VAL = 'frcTom:discord-bot:1'

class TBA(object):

	def teamRequest(self, endpoint : str):
	    resp = requests.get(URL + endpoint + HEADER_KEY + HEADER_VAL)
	    return resp.text

	def getTeamName(self, team : str):
		teamData = json.loads(self.teamRequest("team/frc" + team))
		return teamData["nickname"]

	def getTeamLocation(self, team : str):
		teamData = json.loads(self.teamRequest("team/frc" + team))
		return teamData["location"]

	def getRobot(self, team : str, year : str):
		try:
		    teamData = json.loads(self.teamRequest("team/frc" + team + "/history/robots"))
		    yearData = teamData[year]
		    return yearData["name"]
		except KeyError:
			return "No robot name for that year. Rip"

	def getAwards(self, team : str):
		teamData = json.loads(self.teamRequest("team/frc" + team + "/history/awards"))
		data = ""
		for i in range(len(teamData)):
			data += "Event Key: " + teamData[i]["event_key"] + ", Award Name: " + teamData[i]["name"] + "\n"
		return data
