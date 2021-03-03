import fileinput
import csv
import os.path
from os import path

valorantMaps = ["bind","ascent","haven","icebox","split"].sort()
characters = ["jett","reyna","raze","phoenix","yoru","omen","viper","brim","sova","breach","cypher","sage","killjoy"].sort()
header = ("map", "p1","p2","p3","p4","selected","balance")
filename = "valorant.csv"

def print_values(playermap):
    values = playermap.values().sort(reverse=True)
    for v in values: 
        print(playermap.index(v),v)

def characters_match_row(args,row_players):
    if len(args) == 2:
        return True
    for i in range(2,len(args)):
        if args[i] in row_players:
            return True
    return False

def process_character_selection(args):
    if not path.exists(filename):
        print("Ainda não há registro de jogadas")
        return
    playermap = { i : 0 for i in characters }
    with open(filename, newline='') as csvfile: 
        csvreader = csv.reader(csvfile)
        if len(args) == 1:
            for row in csvreader:
                playermap[row["selected"]] = playermap[row["selected"]] + row["balance"]
        elif len(args) >= 2:
            for row in csvreader:
                if playermap["map"] == args[1]:
                    row_players = {row["p1"],row["p2"],row["p3"],row["p4"]}
                    if characters_match_row(args,row_players):
                        playermap[row["selected"]] = playermap[row["selected"]] + row["balance"]
        print_values(playermap)    

def process_result(args):     
    # falta implementar
    pass

def import_file(args):
    # falta implementar
    pass



while True:
    print("escreva o comando:")
    line = fileinput.input()
    cmdline = line.rstrip().readline()
    args = cmdline.split( )
    if args[0] == 'select':
        process_character_selection(args)
    elif args[0] == 'result':
        process_result(args)
    elif args[0] == "import":
        import_file(args)   
    
