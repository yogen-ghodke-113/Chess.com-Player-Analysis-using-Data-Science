import methods as m
import json
import requests

username = "sudesh2911"

all_games_List = m.getGames(username)
#m.filterList(all_games_List, username)

print(json.dumps(all_games_List, indent=4))

# Import JSON openings file

f = open('openings2.json')
openings = json.load(f)
# print(json.dumps(openings, indent=4))


#WhiteTree = m.buildOpeningTree(openings)
#BlackTree = m.buildOpeningTree(openings)

#m.convertPGN(all_games_List, WhiteTree, BlackTree)



p = ["d2d4"]
q = WhiteTree.traverse(p, WhiteTree.root)
print(q.attributes)
