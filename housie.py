import random

calling = (("1","Lone ranger","Buttered scone","Top of the house number 1","Son of a gun","At the beginning"),
("2","One little duck","Me and you","Kaala dhan","Doctor who"),
("3","Happy family","goodness me"),
("4","Murgi chor","Knock at the door","Hum 2 hamare 2"),
("5","Hum paanch","Symbol of congress","Punjab da puttar","Fingers in your hand"),
("6","Bottom heavy","Chopping sticks","Super sixer","In a fix"),
("7","Lucky no. Seven","One hockey stick","Gods in Heaven","days in a week","Colours of rainbow"),
("8","One fat major","Garden gate","Big fat lady number 8"),
("9","You are mine","Number of planets","Doctors time"),
("10","A big fat hen","Cock and hen","Uncle Ben"),
("11","Two heavenly legs","Two beautiful legs","Sexy legs"),
("12","One dozen","Monkeys cousin, one dozen"),
("13","Bakers dozen","Unlucky for some lucky for me no"),
("14","Valentines Day","Tender chick"),
("15","Yet to be kissed"),
("16","Sweet sixteen","never been kissed"),
("17","Dancing Queen","Not so sweet"),
("18","Voting age"),
("19","Last of the teens","End of teens","Goodbye teens"),
("20","One score","Blind 20"),
("21","Presidents salute","All womens age"),
("22","Two little ducks"),
("23","You and me"),
("24","Two dozen","Want somemore at 24"),
("25","Quarter","Silver Jublee Number","Wish to have a wife at 25","Duck dive 25"),
("26","Republic Day"),
("27","Gateway to heaven"),
("28","Duck and its mate","Overweight @ 28","In a state"),
("29","In your prime","Gin & Wine","Rise & shine"),
("30","Women get flirty at 30"),
("31","Time for fun","Flavours at baskin Robins","Get up and run"),
("32","Mouth Full","Buckle my shoe"),
("33","All the 3s","Two little bees"),
("34","Dil mange more","Ask for more","Lions roar"),
("35","Flirty wife","Jump and jive"),
("36","Popular size","Three dozens","Yardstick"),
("37","Mixed luck","More than eleven","Lime and leamon"),
("38","Oversize","Christmas cake"),
("39","Watch your waistline"),
("40","Naughty 40","Life begins at","Men get naughty"),
("41","Lifes begun at 41","Time for some fun @ 41","Kiss and run"),
("42","Quit India Movement","Winnie the pooh"),
("43","Pain in the knee","Down on your knees","Climb a tree"),
("44","All the fours","Chor chor, all the 4"),
("45","Halfway there"),
("46","Up to tricks"),
("47","Year of Independence","Four and seven"),
("48","Four dozen","You are not late"),
("49","Rise and shine","Your waist line"),
("50","Half a century","Golden Jublee"),
("51","Charity begins at 51","I love my mum"),
("52","Pack of cards","Weeks in a year"),
("53","Stuck in a tree"),
("54","Clean the floor","House of bamboo door"),
("55","All the fives","Bunch of 5s","Snakes alive @ 55"),
("56","Pick up sticks","Was she worth it?"),
("57","Mutiny Year"),
("58","Make them wait","Time to retire"),
("59","Just retired"),
("60","Five dozen"),
("61","Bakers bun"),
("62","Turn the screw","Click the two"),
("63","Tickle me","Click the three"),
("64","Hard core","Catch the chor"),
("65","Old age pension"),
("66","Chakke pe chakka","All the 6s"),
("67","Made in heaven"),
("68","Check your weight","Saving grace"),
("69","Your place or mine","Ulta Pulta"),
("70","Lucky blind"),
("71","Bang the drum","Lucky bachelor"),
("72","Lucky 2"),
("73","Under the tree","A crutch and a flea"),
("74","Still want more","Lucky chor","Candy store","Lucky 4"),
("75","Lucky Five","Diamond Jublee"),
("76","Lucky six"),
("77","Two hockey sticks","hum saat saat hai","Double hockey sticks"),
("78","Heavens gate","Lucky seth (hindi)"),
("79","One more time","lucky nine"),
("80","Gandhis breakfast"),
("81","Corner shot"),
("82","Last of the two","Fat lady with a duck"),
("83","India wins Cricket World Cup","Time for tea"),
("84","Last of the chors","Seven dozen"),
("85","Staying alive","Grandma"),
("86","Between the sticks","Last six"),
("87","Grandpa","Fat lady with a crutch"),
("88","Two fat ladies"),
("89","All but one","Nearly there"),
("90","Top of the house","End of the line","As far as we go"))
numbers = []

def unique(list1):

    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

random.seed()
while len(numbers) < 90:
    inp = raw_input("Press enter for next number")
    if inp != "next":
        continue
    random_number = random.randrange(90)
    chosen = random_number + 1
    while chosen in numbers:
        random_number = random.randrange(90)
        chosen = random_number + 1
    message = calling[random_number][1]
    if len(calling[random_number]) > 2 and bool(random.getrandbits(1)):
        message = calling[random_number][2]
    if len(calling[random_number]) > 3 and bool(random.getrandbits(1)):
        message = calling[random_number][3]
    print chosen, message
    numbers.append(chosen)
    numbers.sort()
    print numbers

