# I know panget yung program but cmon for fun lang to :D

import time

def ask_question():
    print(f"""
    Just type the number of the question you want to ask!
    For example, type '1' if you want my name.
    If you don't want to continue this conversation anymore, type 'None'.

        1: What's your name? 
        2: What's your course and year level?
        3: Any likes?
        4: Any dislikes?
        5: What are your interests and hobbies?
        6: Why did you apply for CSI?
    """)
    print(f"SAM: So... Which question do you want to ask me?\n")
    return input("YOU: ")

# Variables
q_1 = q_2 = q_3 = q_4 = q_5 = q_6 = q_idk = 0 # Counts how many times a question was asked

print(f"\nSAM: Yo! I'm Sam, an applicant for CSI!! Below are a few (required!) questions you can ask me! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧") # Initial greetings

while True:
    
    time.sleep(4)
    question = ask_question()
    print("")

    if question.lower() == "none":
        total_q = q_1 + q_2 + q_3 + q_4 + q_5 + q_6 + q_idk
        if total_q == 0:
            print("SAM: Bro... You didn't even ask me anything. Do you not want to get to know me? Ouch. (╥ω╥)")
        elif total_q <= 10:
            print("SAM: Done asking? Nice! I hope you got to know me better! Have a wonderful day!! ♡＼(￣▽￣)／♡")
        elif total_q <= 20:
            print("SAM: You're done? Wow, finally. You sure ask a lot of stuff. Anyways, I hope you have a nice day! (•‿•)")
        else:
            print("SAM: Done?!?! WOOOHOOO!!! I can finally rest! Talking to you was like talking to a five-year-old. GOSH. Anyways, good luck to you and whoever you have conversations with. (＾▽＾)")
        print("")
        exit()
    elif question == "1":
        if q_1 == 0:
            print("SAM: Well... I already introduced myself as 'Sam', but if you want a full name, then its Samantha Janell Siy!")
        elif q_1 == 1:
            print("SAM: Did you forget? My name is Samantha Janell Siy. Just call me Sam!")
        elif q_1 == 2:
            print("SAM: Why do you keep asking?! I said my name's Sam!! It's literally right next to my speech text!")
        elif q_1 == 3:
            print("SAM: Bro... You gotta be trolling me, right?")
        else:
            print("SAM: (ಠ_ಠ)")
        q_1 += 1
    elif question == "2":
        if q_2 == 0:
            print("SAM: I'm a BS Computer Science freshie, so please take it easy on me! I'm too young to die!")
        elif q_2 == 1:
            print("SAM: You already asked that, remember? I said I'm a first-year BS Computer Science student.")
        elif q_2 == 2:
            print("SAM: This is getting old real quick. I'm a BSCS first-year. Remember that please!")
        else:
            print("SAM: (ಠ_ಠ)")
        q_2 += 1
    elif question == "3":
        if q_3 == 0:
            print("SAM: I like a lot of things! Aside from food and sleep, I also like anime, traveling (or just wandering around in general), and video games!")
        elif q_3 == 1:
            print("SAM: Well, i also like some sports, such as table tennis and chess (even if I'm pretty bad at them).")
        elif q_3 == 2:
            print("SAM: Again? Uhhh... I guess I also like math, but I'm pretty sure that'll change eventually.")
        elif q_3 == 3:
            print("SAM: You know what? I'd like if you'd STOP asking me this question.")
        else:
            print("SAM: (ಠ_ಠ)")
        q_3 += 1
    elif question == "4":
        if q_4 == 0:
            print("SAM: I dislike vegetables.")
        elif q_4 == 1:
            print("SAM: Not enough? Well, I also dislike it when I have assessments back to back.")
        elif q_4 == 2:
            print("SAM: Look, there are a lot of things I dislike. It's kind of hard to list all of them down.")
        elif q_4 == 3:
            print("SAM: I dislike people who keep asking the same questions again and again.")
        else:
            print("SAM: (ಠ_ಠ)")
        q_4 += 1
    elif question == "5":
        if q_5 == 0:
            print("SAM: Well, my hobbies include reading or watching whatever I can find on the internet (mostly novels/anime tho). I also play the occasional Minecraft and Valorant.")
        elif q_5 == 1:
            print("SAM: I don't do this often, but sometimes I crochet. I also draw and paint, whenever I feel motivated at least.")
        elif q_5 == 2:
            print("SAM: Dude, I don't have as much hobbies as you think. School ain't exactly a walk in the park.")
        elif q_5 == 3:
            print("SAM: I already told you everything! What do you want from me?!?!")
        else:
            print("SAM: (ಠ_ಠ)")
        q_5 += 1
    elif question == "6":
        if q_6 == 0:
            print("SAM: I applied to CSI because it seemed cool! Do I need any other reason?")
        elif q_6 == 1:
            print("SAM: Okay, okay! I also think that CSI will allow me to practice and improve my programming skills. I don't want to learn only theory, after all.")
        elif q_6 == 2:
            print("SAM: More? Umm... Well I also want to make friends! It's kinda hard to do, after all, especially with everyone's differing schedules.")
        elif q_6 == 3:
            print("SAM: I dunno anymore. CSI is just cool! That's the only reason you need. Stop asking!!")
        else:
            print("SAM: (ಠ_ಠ)")
        q_6 += 1
    else:
        if q_idk == 0:
            print("SAM: Hey, bro... That ain't part of the choices. Please stick to the questions I gave.")
        elif q_idk == 1:
            print("SAM: Diba I said to stick to the choices?! Are you trolling me?")
        elif q_idk == 2:
            print("SAM: STOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
        else:
            print("SAM: (ಠ_ಠ)")
        q_idk += 1
    print("")