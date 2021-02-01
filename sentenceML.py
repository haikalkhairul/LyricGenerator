import random

#txt = "You know how the paigon chit-chat goes I like Rs and Vs and Os I don't really play no tic-tac-toe Been with Chubbs through highs and lows We seen man last night, they froze Wasn't no cameras, wasn't no pose Just like that one time at 'Chella Good thing man weren't pullin' out phones Staying in big six-six with woes Man start dissin' and doin' reposts They do anything except road Still can't see them after it snows I don't have time for the wasteman jokes Personal ting if I'm gettin' up close Loyal to O 'cause I've taken a oath Versace hotel and I'm takin' the robes Seen 'em in person, I'm seein' a ghost They told me relax 'cause they're takin' control Take all that shit up with P and his bro I wish you the best, let me know how it goes Wanna be free and I wanna let go We came around and you showed us the most I know so much shit that I cannot expose I keep it inside and I laugh on my own Got all the tea and I'm hottin' it up I need a shade mansion, a room's not enough You're droppin' some shit but that shit was a bust They got no direction, they're followin' us I come from a city that they never touch Your man is a goofy and he could get rushed I can't name a rapper or girl that I trust I dream about turnin' these yutes into dust You know how the paigon chit-chat goes I like Rs and Vs and Os I don't really play no tic-tac-toe Been with Roxx through highs and lows We seen man last night, they froze Wasn't no cameras, wasn't no pose Just like that one time at Nobu Good thing man weren't pullin' out phones Think you know me? That's not true We got ties in West End too She came over and she got slewed Throwin' up six like man had flu I got way too big off Views Back to the basics, I won't lose They wanna link when they got no chunes They too worried 'bout sellin' out shoes I don't give a fuck about jeans and crep Or goin' to Milan or goin' to the Met I just wanna make these songs for the set I just wanna load that and let that wet I got so much tings in the stash Fold up anyone, dun that clash Got no sense like Jizzle and shh Big and bad like leader and shh Can't do love 'cause they get too attached Phone get broke and whip get scratched I'ma just take my knots in cash They can never tie me down, that's facts All that bark but we know he's a cat I don't really like goin' tit for tat I'ma just come like tat-tat-tat I'ma just end that there, that's that"
#txt = "Gucci Gang, ooh, yeah, Lil Pump, yeah, Gucci Gang, ooh Gucci gang, Gucci gang, Gucci gang, Gucci gang Gucci gang, Gucci gang, Gucci gang (Gucci gang!) Spend ten racks on a new chain My bitch love do cocaine, ooh I f*ck a bitch, I forgot her name I can't buy a bitch no wedding ring Rather go and buy Balmains Gucci gang, Gucci gang, Gucci gang (Gucci gang!) Gucci gang, Gucci gang, Gucci gang, Gucci gang Gucci gang, Gucci gang, Gucci gang (Gucci gang!) Spend ten racks on a new chain My bitch love do cocaine, ooh I f*ck a bitch, I forgot her name, yeah I can't buy no bitch no wedding ring Rather go and buy Balmains, aye Gucci gang, Gucci gang, Gucci gang My lean cost more than your rent, ooh Your mama still live in a tent, yeah Still slanging dope in the jets, huh Me and my grandma take meds, ooh None of this shit be new to me F*cking my teacher, call it tutory Bought some red bottoms, cost hella Gs F*ck your airline, f*ck your company Bitch, your breath smell like some cigarettes I'd rather f*ck a bitch from the projects They kicked me out the plane off a Percocet Now Lil Pump fly a private jet Everybody screaming f*ck West Jet! Lil Pump still sell that meth Hunnid on my wrist sippin on Tech F*ck a lil bitch, make her pussy wet Gucci gang, Gucci gang, Gucci gang, Gucci gang Gucci gang, Gucci gang, Gucci gang (Gucci gang!) Spend ten racks on a new chain My bitch love do cocaine, ooh I f*ck a bitch, I forgot her name I can't buy a bitch no wedding ring Rather go and buy Balmains Gucci gang, Gucci gang, Gucci gang (Gucci gang!) Gucci gang, Gucci gang, Gucci gang, Gucci gang Gucci gang, Gucci gang, Gucci gang (Gucci gang!) Spend ten racks on a new chain My bitch love do cocaine, ooh I f*ck a bitch, I forgot her name I can't buy no bitch no wedding ring Rather go and buy Balmains, aye Gucci gang, Gucci gang, Gucci gang Lil Pump, yeah, Lil Pump, ooh"
#txt = "this is a more complex sentence sentence competence"
order = 5
ngrams = {}

file = open("lyrics.txt", "r")
lines = file.readlines()
songLyrics = "".join(lines)
while songLyrics.find("\n") != -1:
    songLyrics = songLyrics.replace("\n", " ")
txt = songLyrics

file.close()

def setup():
    count = 0
    for index, character in enumerate(txt):
        gram = txt[index:index+order]
        if not gram in ngrams:
            #count = 1
            #ngrams[gram] = count
            ngrams[gram] = []
        ngrams[gram].append(txt[index+order:index+order+1])
        
        #else:
            #ngrams[gram] = ngrams.get(gram) + 1
        
        if index == len(txt) - order:
            break

def markovIt():
    '''keys = str(ngrams.keys())
    keysFixed = keys[11:len(keys)-2]
    gramList = keysFixed.split("', '")
    currentGram = random.choice(gramList)
    print(currentGram)'''
    currentGram = txt[0:order]
    result = currentGram

    for idx in range(1000):
        possibilities = ngrams.get(currentGram)
        nextChar = random.choice(possibilities)
        result += nextChar
        currentGram = result[len(result)-order:len(result)]

    
    print(result)
    

setup()
markovIt()
'''flag = True
while flag:
    markovIt()
    user = input("continue? y, n")
    if user == "n":
        flag = False'''
