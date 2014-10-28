from __future__ import print_function
from __future__ import division
import requests

from riotwatcher import RiotWatcher

FEATURED_GAMES_REST_URL = 'http://spectator.na.lol.riotgames.com:8088/observer-mode/rest/featured'

w = RiotWatcher('3e5b7f1c-e67c-4a1b-b289-aed01afc2483')

def getSummonerIDsFromFeaturedGames():
    r = requests.get(FEATURED_GAMES_REST_URL)
    print(r.status_code)

    featuredGamesData = r.json()
    gameList = featuredGamesData['gameList']
    summonerNames = set()
    for game in gameList:
        participants = game['participants']
        for p in participants:
            summonerName = p['summonerName']
            summonerNames.add(summonerName);

    summoners = [];
    summonerNames = list(summonerNames);
    for i in range(0, len(summonerNames), 40):
        summoners.extend(w.get_summoners(names=summonerNames[i:i+40]).values())

    summonerIds = [x['id'] for x in summoners];
    return summonerIds;

if __name__ == "__main__":
    summonerIds = getSummonerIDsFromFeaturedGames()
    print(summonerIds)