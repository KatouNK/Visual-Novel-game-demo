# Define characters
define h = Character("Hitomi")
define m = Character("Makoto")

# The game starts here.
label start:
    scene club_room
    show hitomi_curious
    h "Hello there, welcome to our club. My name is Hitomi."
    show hitomi_default
    menu:
        "Nice to meet you too, I'm Kazuhito.":
            jump introduction
        "...":
            jump silent

label introduction:
    scene club_room
    show hitomi_curious
    h "Nice to meet you too, Kazuhito-san."
    
label silent:
    scene club_room
    show hitomi_default
    h "..."
    show hitomi_wondering
    h "Erhmm... haha, seems like you don't talk much."
    show hitomi_curious
    h "You must have some questions to ask. It might seem complicated about our club activities..."
    h "But don't worry, just ask me if you have a question."

    menu:
        "So what is this club all about again?":
            jump club_introduction
        "Can you tell me more about yourself?":
            jump hitomi_introduction
        "I wonder how big it is...":
            jump surprised

label club_introduction:
    scene club_room
    show hitomi_curious
    h "Our club is about..."
    jump main_story  

label hitomi_introduction:
    show hitomi_curious
    scene club_room
    h "Well, I am..."
    jump main_story  
label surprised:
    scene club_room
    show hitomi_concern 
    h "eh...?"
    "\"What am I thinking asking that?\""
    

label main_story:
    scene club_room
    show hitomi_default
    h "So, what would you like to do next?"
