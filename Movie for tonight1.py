#part 1

import random
print(("-"*34)+("Movie for tonight!!!")+("-"*34))

#part 1.2:    lists and dictionary

Anime = ["Hauru no ugoku shiro","Tsumiki no ie", "The End of Evangelion",
         "Kaze no tani no Naushika","One Piece Film Z",]

Comedi = ["The Big Lebowski","Monty Python and the Holy Grail",
          " As Good As It Gets","Young Adult","The Hangover"]

Documentare = ["8 Days: to the Moon and Back","Blue Planet","Art and Craft",
               "Real Scenes: London","Human Flow"]

Drama = ["Serenity","The Aftermath","Five Feet Apart","The Professor and the Madman"]

Sienfiction = ["Avatar","The Day The Earth Stood Still","Wall-E","Star Trek II: The Wrath Of Khan","Inception"]

Thriller = ["American Psycho","Winter’s Bone","The Girl With The Dragon Tattoo",
            "Nocturnal Animals","You Were Never Really Here"]

Romance = ["Casablanca","Before Sunrise","When Harry Met Sally","Cinema Paradiso","Titanic"]

History = ["Hamilton","Lincoln","Free State of Jones","A Night To Remember","Gettysburg"]

Other = ["The Holiday","Casino Royale","Memento","The Shining","Pride and Prejudice"]

Categories =[["Anime"],["Comedi"],["Documentare"],["Drama"],["Sienfiction"],
             ["Thiller"],["Romance"],["History"],["Other"]]

#part 2 informing the lists

old_movies=input(str("\nDo you want to tell me what movies have you already see? (y/n):\n")).lower()

while old_movies == "y" :

    a = input(str("Which is the title?:")).title()

    if Anime.count(a) or Comedi.count(a) or Documentare.count(a) or Drama.count(a) or\
    Sienfiction.count(a) or Thriller.count(a) or Romance.count(a) or History.count(a) or Other.count(a):
        print("I am in list")
        old_movies=input("Do you have any other move? (y/n):").lower()

    else:
        c = input(str("What type is it:\nAnime | Comedi | Documentare | Drama | Sienfiction | Thriller | Romance | History | Other :")).capitalize()

        if c == "Anime" :
            Anime.append(a)
            old_movies=input("Do you have any move? (y/n):").lower()
        elif c== "Comedi":
            old_movies=input("Do you have any move? (y/n):").lower()
        elif c == "Documentare":
            Documentare.append(a)
            old_movies=input("Do you have any move? (y/n):").lower()
        elif c == "Drama":
            Drama.append(a)
            old_movies=input("Do you have any move? (y/n):").lower()
        elif c == "Sienfiction":
            Sienfiction.append(a)
            old_movies=input("Do you have any move? (y/n):").lower()
        elif c == "Thriller":
            Thriller.append(a)
            old_movies=input("Do you have any move? (y/n):").lower()
        elif c == "Romance":
            Romance.append(a)
            old_movies=input("Do you have any move? (y/n):").lower()
        elif c == "History":
            History.append(a)
            old_movies=input("Do you have any move? (y/n):").lower()
        elif c == "Other":
            Other.append(a)
            old_movies=input("Do you have any move? (y/n):").lower()
        else:
            old_movies=input("This category does not exist.Do you want to try again ?(y/n):").lower()

 #part 3 suggestion

x = "y"

while x == "y":
    categori= input(str("What type of movie do you want to see:"
    "\nAnime | Comedi | Documentare | Drama | Sienfiction | Thriller | Romance | History | Other ?:")).capitalize()

    if categori == "Anime" :
        p=random.choice(list(Anime))
        print(p)
        x = input(str("Do you want another movie? (y/n):")).lower()
    elif categori == "Comedi" :
        p=random.choice(list(Comedi))
        print(p)
        x = input(str("Do you want another movie? (y/n):")).lower()
    elif categori == "Documentare" :
        p=random.choice(list(Documentare))
        print(p)
        x = input(str("Do you want another movie? (y/n):")).lower()
    elif categori == "Drama" :
        p=random.choice(list(Drama))
        print(p)
        x = input(str("Do you want another movie? (y/n):")).lower()
    elif categori == "Sienfiction" :
        p=random.choice(list(Sienfiction))
        print(p)
        x = input(str("Do you want another movie? (y/n):")).lower()
    elif categori == "Thriller" :
        p=random.choice(list(Thriller))
        print(p)
        x = input(str("Do you want another movie? (y/n):")).lower()
    elif categori == "Romance" :
        p=random.choice(list(Romance))
        print(p)
        x = input(str("Do you want another movie? (y/n):")).lower()
    elif categori == "History" :
        p=random.choice(list(History))
        print(p)
        x = input(str("Do you want another movie? (y/n):")).lower()
    elif categori == "Other" :
        p=random.choice(list(Other))
        print(p)
        x = input(str("Do you want another movie? (y/n):")).lower()
    else:
        x=input("This category does not exist.Do you want to try again (y/n):").lower()


#part 4  ending

print(str("Enjoy the film !!!"))
