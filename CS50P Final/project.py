import random
import sys

for_zep_fans = [
    "Out on the Tiles - The Rolling Stones",
    "Highway Star - Deep Purple",
    "All Right Now - Free",
    "The Rover - Interpol",
    "Space Truckin' - Deep Purple",
    "No One Knows - Queens of the Stone Age",
    "Stranglehold - Ted Nugent",
    "Fortunate Son - Creedence Clearwater Revival",
    "Black Magic Woman - Santana",
    "Crossroads - Cream",
    "Whole Lotta Rosie - AC/DC",
    "Since You've Been Gone - Rainbow",
    "Fire - Jimi Hendrix",
    "The Chain - Fleetwood Mac",
    "Sultans of Swing - Dire Straits",
    "Barracuda - Heart",
    "Money - Pink Floyd",
    "Born on the Bayou - Creedence Clearwater Revival",
    "Don't Fear the Reaper - Blue Öyster Cult",
    "Sharp Dressed Man - ZZ Top",
    "You Shook Me All Night Long - AC/DC",
    "Smoke on the Water - Deep Purple",
    "Jessica - The Allman Brothers Band",
    "I'm Eighteen - Alice Cooper",
    "Tush - ZZ Top",
    "Ramblin' Man - The Allman Brothers Band",
    "Kashmir - Puscifer",
    "Rock and Roll - Greta Van Fleet",
    "Runnin' with the Devil - Van Halen"
]

classic_rock = [
    "Hotel California - Eagles",
    "Bohemian Rhapsody - Queen",
    "Stairway to Heaven - Led Zeppelin",
    "Dream On - Aerosmith",
    "Born to Run - Bruce Springsteen",
    "Layla - Derek and the Dominos",
    "Free Bird - Lynyrd Skynyrd",
    "Sultans of Swing - Dire Straits",
    "More Than a Feeling - Boston",
    "You Really Got Me - The Kinks",
    "Carry on Wayward Son - Kansas",
    "Paint It Black - The Rolling Stones",
    "The Joker - Steve Miller Band",
    "All Along the Watchtower - Jimi Hendrix",
    "Comfortably Numb - Pink Floyd",
    "Sweet Home Alabama - Lynyrd Skynyrd",
    "Wheel in the Sky - Journey",
    "Barracuda - Heart",
    "Black Dog - Led Zeppelin",
    "Come Sail Away - Styx",
    "Fortunate Son - Creedence Clearwater Revival",
    "Crazy on You - Heart",
    "Highway to Hell - AC/DC",
    "Bad Moon Rising - Creedence Clearwater Revival",
    "We Will Rock You - Queen",
    "Rock and Roll All Nite - Kiss",
    "American Girl - Tom Petty and the Heartbreakers",
    "Time - Pink Floyd",
    "Rockin' in the Free World - Neil Young",
    "Magic Carpet Ride - Steppenwolf"
]

prog_rock = [
    "Close to the Edge - Yes",
    "2112 - Rush",
    "Supper's Ready - Genesis",
    "Starless - King Crimson",
    "The Gates of Delirium - Yes",
    "Echoes - Pink Floyd",
    "Thick as a Brick - Jethro Tull",
    "Karn Evil 9 - Emerson, Lake & Palmer",
    "Tarkus - Emerson, Lake & Palmer",
    "Heart of the Sunrise - Yes",
    "The Musical Box - Genesis",
    "Larks' Tongues in Aspic Part I - King Crimson",
    "Xanadu - Rush",
    "Roundabout - Yes",
    "In the Court of the Crimson King - King Crimson",
    "A Plague of Lighthouse Keepers - Van der Graaf Generator",
    "Aqualung - Jethro Tull",
    "Cygnus X-1 - Rush",
    "Firth of Fifth - Genesis",
    "Red - King Crimson",
    "Astronomy Domine - Pink Floyd",
    "The Knife - Genesis",
    "Lucky Man - Emerson, Lake & Palmer",
    "Time and a Word - Yes",
    "Atom Heart Mother - Pink Floyd",
    "The Gates of Babylon - Rainbow",
    "Epitaph - King Crimson",
    "Dogs - Pink Floyd",
    "Fly From Here - Yes",
    "The Cinema Show - Genesis"
]

indie_rock = [
    "Fluorescent Adolescent - Arctic Monkeys",
    "Mr. Brightside - The Killers",
    "Take Me Out - Franz Ferdinand",
    "Electric Feel - MGMT",
    "Somebody Told Me - The Killers",
    "Do I Wanna Know? - Arctic Monkeys",
    "1901 - Phoenix",
    "Pumped Up Kicks - Foster the People",
    "Time to Pretend - MGMT",
    "Feel Good Inc. - Gorillaz",
    "Someday - The Strokes",
    "Lazy Eye - Silversun Pickups",
    "Float On - Modest Mouse",
    "Reptilia - The Strokes",
    "Tongue Tied - Grouplove",
    "Riptide - Vance Joy",
    "You Only Live Once - The Strokes",
    "The Less I Know The Better - Tame Impala",
    "Cough Syrup - Young the Giant",
    "Fitzpleasure - alt-J",
    "All These Things That I've Done - The Killers",
    "Do You - Spoon",
    "Elephant - Tame Impala",
    "Pork and Beans - Weezer",
    "Feel It Still - Portugal. The Man",
    "Pumped Up Kicks - Foster the People",
    "My Number - Foals",
    "Crystalised - The xx",
    "Little Lion Man - Mumford & Sons",
    "Hannah Hunt - Vampire Weekend"
]

dad_rock = [
    "Don't Stop Believin' - Journey",
    "Hotel California - Eagles",
    "More Than a Feeling - Boston",
    "Sweet Home Alabama - Lynyrd Skynyrd",
    "Livin' on a Prayer - Bon Jovi",
    "Take It Easy - Eagles",
    "Summer of '69 - Bryan Adams",
    "You Give Love a Bad Name - Bon Jovi",
    "Renegade - Styx",
    "Jessie's Girl - Rick Springfield",
    "Any Way You Want It - Journey",
    "Old Time Rock and Roll - Bob Seger",
    "Runnin' Down a Dream - Tom Petty",
    "The Boys Are Back in Town - Thin Lizzy",
    "Rock and Roll All Nite - Kiss",
    "Sister Christian - Night Ranger",
    "We're Not Gonna Take It - Twisted Sister",
    "Saturday Night's Alright for Fighting - Elton John",
    "Here I Go Again - Whitesnake",
    "Sharp Dressed Man - ZZ Top",
    "Walk This Way - Aerosmith",
    "Crazy Train - Ozzy Osbourne",
    "Rebel Yell - Billy Idol",
    "Pour Some Sugar On Me - Def Leppard",
    "Don't Fear The Reaper - Blue Öyster Cult",
    "Jack & Diane - John Mellencamp",
    "Peaceful Easy Feeling - Eagles",
    "Keep On Loving You - REO Speedwagon",
    "Bad to the Bone - George Thorogood & The Destroyers",
    "Start Me Up - The Rolling Stones"
]

alt_rock = [
    "Smells Like Teen Spirit - Nirvana",
    "Creep - Radiohead",
    "Bitter Sweet Symphony - The Verve",
    "Everlong - Foo Fighters",
    "Champagne Supernova - Oasis",
    "Wonderwall - Oasis",
    "Under the Bridge - Red Hot Chili Peppers",
    "I Will Follow You into the Dark - Death Cab for Cutie",
    "Fake Plastic Trees - Radiohead",
    "Black Hole Sun - Soundgarden",
    "1979 - The Smashing Pumpkins",
    "Karma Police - Radiohead",
    "My Hero - Foo Fighters",
    "Mr. Jones - Counting Crows",
    "Scar Tissue - Red Hot Chili Peppers",
    "Losing My Religion - R.E.M.",
    "The Man Who Sold the World - Nirvana",
    "Drive - Incubus",
    "Slide - Goo Goo Dolls",
    "In the Meantime - Spacehog",
    "The Middle - Jimmy Eat World",
    "Alive - Pearl Jam",
    "Sex and Candy - Marcy Playground",
    "Stupid Girl - Garbage",
    "No Rain - Blind Melon",
    "Violet - Hole",
    "The Freshmen - The Verve Pipe",
    "Plush - Stone Temple Pilots",
    "Low - Cracker",
    "Basket Case - Green Day"
]

woodstock_songs = [
    "With a Little Help from My Friends - Joe Cocker",
    "Purple Haze - Jimi Hendrix",
    "Soul Sacrifice - Santana",
    "White Rabbit - Jefferson Airplane",
    "Piece of My Heart - Janis Joplin",
    "Woodstock - Crosby, Stills, Nash & Young",
    "The Weight - The Band",
    "Going Up the Country - Canned Heat",
    "Suite: Judy Blue Eyes - Crosby, Stills, Nash & Young",
    "Freedom - Richie Havens",
    "I'm Going Home - Ten Years After",
    "We're Not Gonna Take It - The Who",
    "Summertime Blues - The Who",
    "Spinning Wheel - Blood, Sweat & Tears",
    "I Want to Take You Higher - Sly & the Family Stone",
    "Green River - Creedence Clearwater Revival",
    "Born on the Bayou - Creedence Clearwater Revival",
    "Love March - Paul Butterfield Blues Band",
    "Wooden Ships - Crosby, Stills, Nash & Young",
    "Goin' Up the Country - Canned Heat",
    "Dark Star - Grateful Dead",
    "Fire - The Jimi Hendrix Experience",
    "Hoochie Coochie Man - The Paul Butterfield Blues Band",
    "My Generation - The Who",
    "Badge - Cream",
    "The Star-Spangled Banner - Jimi Hendrix",
    "Try (Just a Little Bit Harder) - Janis Joplin",
    "Good Times Bad Times - Joe Cocker",
]

chart_toppers = [
    "Eye of the Tiger - Survivor",
    "Another Brick in the Wall, Part II - Pink Floyd",
    "Every Breath You Take - The Police",
    "Livin' on a Prayer - Bon Jovi",
    "Sweet Child o' Mine - Guns N' Roses",
    "Walk Like an Egyptian - The Bangles",
    "We Will Rock You - Queen",
    "Start Me Up - The Rolling Stones",
    "You Give Love a Bad Name - Bon Jovi",
    "Jump - Van Halen",
    "Black or White - Michael Jackson",
    "Billie Jean - Michael Jackson",
    "Every Rose Has Its Thorn - Poison",
    "Love Bites - Def Leppard",
    "Africa - Toto",
    "Owner of a Lonely Heart - Yes",
    "I Love Rock 'n Roll - Joan Jett & the Blackhearts",
    "Rock You Like a Hurricane - Scorpions",
    "Don't Stop Believin' - Journey",
    "Carry on Wayward Son - Kansas",
    "Don't You (Forget About Me) - Simple Minds",
    "Rock the Casbah - The Clash",
    "Jumpin' Jack Flash - The Rolling Stones",
    "You Really Got Me - The Kinks",
    "Smells Like Teen Spirit - Nirvana",
    "Enter Sandman - Metallica",
    "I Was Made for Lovin' You - Kiss",
    "Money for Nothing - Dire Straits",
    "Sweet Home Alabama - Lynyrd Skynyrd",
    "Bohemian Rhapsody - Queen"
]

for_doors_fans = [
    "Light My Fire - The Doors",
    "Break on Through (To the Other Side) - The Doors",
    "Riders on the Storm - The Doors",
    "L.A. Woman - The Doors",
    "Love Her Madly - The Doors",
    "People Are Strange - The Doors",
    "The End - The Doors",
    "Touch Me - The Doors",
    "Roadhouse Blues - The Doors",
    "Hello, I Love You - The Doors",
    "Sympathy for the Devil - The Rolling Stones",
    "White Rabbit - Jefferson Airplane",
    "Somebody to Love - Jefferson Airplane",
    "All Along the Watchtower - Jimi Hendrix",
    "House of the Rising Sun - The Animals",
    "Paint It Black - The Rolling Stones",
    "Come Together - The Beatles",
    "Stairway to Heaven - Led Zeppelin",
    "Purple Haze - Jimi Hendrix",
    "Gimme Shelter - The Rolling Stones",
    "Strawberry Fields Forever - The Beatles",
    "Piece of My Heart - Janis Joplin",
    "Lucy in the Sky with Diamonds - The Beatles",
    "Hey Joe - Jimi Hendrix",
    "My Generation - The Who",
    "Time of the Season - The Zombies",
    "California Dreamin' - The Mamas & The Papas",
    "A Whiter Shade of Pale - Procol Harum",
    "Like a Rolling Stone - Bob Dylan",
    "Space Oddity - David Bowie"
]

for_nirvana_fans = [
    "Smells Like Teen Spirit - Nirvana",
    "Come As You Are - Nirvana",
    "Lithium - Nirvana",
    "Heart-Shaped Box - Nirvana",
    "In Bloom - Nirvana",
    "All Apologies - Nirvana",
    "About a Girl - Nirvana",
    "The Man Who Sold the World - Nirvana",
    "Rape Me - Nirvana",
    "Polly - Nirvana",
    "Pearl Jam - Alive",
    "Black Hole Sun - Soundgarden",
    "Man in the Box - Alice In Chains",
    "Plush - Stone Temple Pilots",
    "1979 - Smashing Pumpkins",
    "Where Is My Mind? - Pixies",
    "Teen Age Riot - Sonic Youth",
    "Feel the Pain - Dinosaur Jr.",
    "Touch Me I'm Sick - Mudhoney",
    "Celebrity Skin - Hole",
    "Basket Case - Green Day",
    "Creep - Radiohead",
    "Under the Bridge - Red Hot Chili Peppers",
    "Loser - Beck",
    "Song 2 - Blur",
    "Glycerine - Bush",
    "Say It Ain't So - Weezer",
    "Everlong - Foo Fighters",
    "Self Esteem  - The Offspring",
    "Only Happy When It Rains - Garbage"
]

for_white_stripes_fans = [
    "Seven Nation Army - The White Stripes",
    "Fell in Love with a Girl - The White Stripes",
    "The Hardest Button to Button - The White Stripes",
    "Icky Thump - The White Stripes",
    "Dead Leaves and the Dirty Ground - The White Stripes",
    "My Doorbell - The White Stripes",
    "Blue Orchid - The White Stripes",
    "Ball and Biscuit - The White Stripes",
    "Black Math - The White Stripes",
    "Hotel Yorba - The White Stripes",
    "Steady, As She Goes - The Raconteurs",
    "Lonely Boy - The Black Keys",
    "Do I Wanna Know? - Arctic Monkeys",
    "Cheap and Cheerful - The Kills",
    "Reptilia - The Strokes",
    "Maps - Yeah Yeah Yeahs",
    "Take Me Out - Franz Ferdinand",
    "Hate to Say I Told You So - The Hives",
    "The Underdog - Spoon",
    "No One Knows - Queens of the Stone Age",
    "Romantic Rights - Death From Above 1979",
    "A-Punk - Vampire Weekend",
    "Float On - Modest Mouse",
    "Slow Hands - Interpol",
    "Sex on Fire - Kings of Leon",
    "Banquet - Bloc Party",
    "Spread Your Love - Black Rebel Motorcycle Club",
    "Woman - Wolfmother",
    "Get Free - The Vines",
    "I Know What I Am - Band of Skulls"
]


# All of these lists were generated by chatGPT. For most, I asked it to list 30 songs for fans of certain bands, or simply in specific genres.
# The chart_toppers list is just chart topping rock songs, and the woodstock list is just 30 songs played at woodstock.

master = [for_zep_fans, classic_rock, prog_rock, indie_rock, dad_rock, alt_rock, woodstock_songs, chart_toppers, for_doors_fans, for_nirvana_fans, for_white_stripes_fans]
active_songs = []
active_lists = []
my_list = []

def main():
    active_lists = scan_for_artist(master, "The Rolling Stones")
    active_songs = random_from_active(active_lists)
    print("Select a song to add: ")
    my_list.append(choices(active_songs))
    print_list(my_list)
    print("")
    while True:
        print("1. Review playlist")
        print("2. Add songs")
        print("3. Finalize")
        try:
            c = input("Choice: ")
        except EOFError:
            sys.exit(0)
        if c == "1":
            print("\nYour current playlist is: ")
            print_list(my_list)
            print("")
        elif c == "3":
            print("\nYour final playlist is: ")
            print_list(my_list)
            print("")
            break
        else:
            print("\nSelect a song on your playlist to add more similar songs: ")
            target_artist = song_to_artist(choices(my_list))
            print("Select one of these suggested songs based on " + target_artist)
            my_list.append(choices(random_from_active(scan_for_artist(master, target_artist))))


def song_to_artist(song):
    t, a = song.split(" - ")
    return a

def choices(choices):
    i = 1
    for song in choices:
        print(str(i) + ": " + song)
        i = i + 1
    return choices[int(input("Choose a number: "))-1]

def scan_for_artist(m, artist):
    active_lists = []
    for thatlist in m:
        for song in thatlist:
            t, a = song.split(" - ")
            if a == artist:
                active_lists.append(thatlist)
                break
    return active_lists

def random_from_active(lists):
    active_songs = []
    while len(active_songs) < 5:
        for l in lists:
            randy = random.choice(l)
            active_songs.append(randy)
    active_songs = list(dict.fromkeys(active_songs))
    return active_songs

def print_list(list_to_print):
    for x in list_to_print:
        print(x)

def no_input_choices(choices, fake_input): #Identical function to choices that takes pre-added choice, rather than asking for one from user
    i = 1
    for song in choices:
        print(str(i) + ": " + song)
        i = i + 1
    return choices[int(fake_input)-1]

if __name__ == "__main__":
    main()