# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define M = Character("Me", color="#000000") #TODO change colors
define m = Character("Molly", color="#1a4f14") 
define c = Character("Claudia", color="#e07aaf") 
define s = Character("Shelldon", color="#c46225")
define g = Character("Gaster", color="#5b1663")
define C = Character("Clawdia", color="#e07aaf") 
define narrator = Character(what_italic = True)
#TODO change color

transform midleft:
    xalign 0.0
    yalign 0.5

transform midright:
    xalign 1.0
    yalign 0.5

# The game starts here.

label start:
    $ with_claudia = True
    $ is_day2 = False
    $ claudia = False
    $ shelldon = False
    $ gaster = False
    $ molly = False
    $ day_2_breakup = False
    $ seeing_shelldon = False
    $ seeing_gaster = False
    $ claudia_good = False
    $ shelldon_good = False
    $ gaster_good = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg coffee #TODO make bg
    "Uuuuuuugggggggghhhhhhhh"
    "There's something about working in customer service that always makes time go by so slowly."
    "We've only just opened for the day and it already feels like I've been here for hours."

    M "Sigh..."

    show molly normal at midleft
    with moveinleft

    m "Something wrong?"

    M "Ack!"

    "I didn't realize I was thinking out loud."

    M "Nah it's fine. I'm just thinking."

    m "Dozing off on the job? That's unlike you."

    "Molly is my coworker. She's often off doing her own thing, but she's been a lifeline while working here."

    m "...Hello?"

    M "Oh. Yeah. Hi."

    m "Coffee?"

    M "Please."

    "Molly may not be great with the customers, but by the tides does she make a good cup of coffee."

    m "Didn't sleep well last night?"

    M "You could say that."

    "Truth is, I slept like shit."

    m "Is it Claudia?"

    M "Now hold on-"

    m "Come on, you and I both know she's a megabitch."

    M "That happens to be my girlfriend you're talking about."

    m "Yes. Your girlfriend is a megabitch. I hate to be the one to bring this to your attention."

    "Molly hands me the coffee and I take a big gulp of it."

    M "She can be a bit...snippy."

    m "I've been telling you this since high school!"

    "The door to the coffee shop rings."

    "It's Claudia."

    m "..."

    m "I'm gonna take a smoke break."

    hide molly
    with moveoutright

    M "Wait-"

    "..."

    "She abandoned me."

    show claudia normal at truecenter
    with moveinleft

    c "I can't believe you!"

    M "What? What did I do?"

    c "You forgot our anniversary!"

    M "Our- huh? Our anniversary's not for another 5 months!"

    c "I'm talking about our 7 month anniversary!"

    M "I don't think that's a thing."

    c "Oh, is that your excuse? Tides, you can be such a jerk sometimes."

    "Right back at you..."

    M "I'm sorry. I'll make it up to you somehow."

    c "You better. I'll see you later, I guess. Since you clearly don't have time for me."

    M "I'm at work..."

    hide claudia
    with moveoutleft

    show molly normal at midleft
    with moveinright

    m "Howdy!"

    M "How could you abandon me like that?"

    m "It's too early in the day to expose myself to that much bitchery. I'm watching my blood pressure."

    M "Is that also why you smell like weed at 7:30 in the morning?"

    m "Leave me alone."

    show shelldon normal at midright
    with moveinright

    M "Welcome!"

    s "Hi there!"
    
    M "What can I get started for ya?"

    s "I'll have a large black coffee."

    M "You got it."

    "At least it's something easy. I pour the coffee that Molly just brewed into a cup and hand it to him."

    s "Thank you."

    hide shelldon
    with moveoutright

    m "..."

    m "What a fine piece of ass."

    M "Molly!"

    m "What? I like 'em rugged."

    "She's got a point. He was definitely cute. And he looked strong too."

    m "He probably works for that one construction company. I saw they were working on something on my way here."

    M "Yeah, I saw them too. Looks like they're building something big."

    m "..."

    M "..."

    m "..."

    m "Sooooo...?"

    M "So what?"

    m "Don't play dumb! I saw how you were looking at him."

    menu:
        "Are you sure that's not the weed talking?":
            jump shellno
        "I suppose...but what about Claudia?":
            jump shellyes

label shellno:
    $ shelldon = False

    m "That's not how it works. But point taken."

    M "Good."

    m "You should still dump your girlfriend though."

    M "Oh, come on."

    m "I'm right!"

    M "Yeah, whatever."

    m "Just consider it."

    "The rest of my shift was uneventful."

    jump day_one_end_a

label shellyes:
    $ shelldon = True 
    
    m "You should've dumped that bitch ages ago!"

    M "Okay, you're right. After work I'm gonna invite her over and just rip off the bandage."

    m "Good."

    scene bg black with fade

    "The rest of my shift was uneventful. I was mostly thinking about how I'd break the news to Claudia. While I'm not entirely sure that she has a heart, if she did, it would be broken."

    jump breakup

label day_one_end_a:
    
    scene bg black with fade

    "I can't sleep."

    "I can't help but wonder if Molly was right."

    "Claudia has never treated me well. but she's kind of all I know."

    "I wish there was someone I could talk to about this."

    "..."

    menu:
        "I should call Molly.":
            "(beep)"
            "(riiinnnngggggggg...)"
            "(riiinnnngggggggg...)"
            "She probably smoked too much weed and fell asleep at 9pm again."
            "I really can't blame her for that."
            "I should ask her to share one of these days..."
            jump day2
        "I should call Claudia":
            "(beep)"
            "(riiinnnngggggggg...)"
            "(riiinnnngggggggg...)"      
            c "Hey babe."
            M "Hey..."
            c "Can't sleep?"
            M "No, not really."
            "She laughs. Then she hangs up."
            M "..."
            M "Bitch."
            jump day2
        "I should get some sleep.":
            "Sigh."
            jump day2

label breakup:
    $ with_claudia = False
    scene bg playerhouse
    "There's a knock."
    "Oh Tides. I don't know if I can do this."
    show claudia normal at truecenter
    with moveinright
    c "So you finally found time in your busy schedule for your girlfriend?"
    "...Never mind."

    M "Claudia, we need to talk."

    show claudia crying

    c "How could you do this to me?! I thought we had something special!"

    hide claudia
    with moveoutright

    "Huh. I didn't even say anything. She did all the work for me."
    "Cool?"
    scene bg black with fade
    if is_day2:
        jump day3
    else:
        jump day_one_end_b

label day_one_end_b:
    "I can't sleep."

    "I can't stop thinking about him..."

    "The way his hard-hat shines in the light..."

    "His beautiful blue eyes..."

    "His glistening abs..."

    "His shell."

    M "Ughhh..."

    "It's 4 am."

    "I have work in 2 hours."

    "Tides, today is gonna suck."

    jump day2

label day2:
    scene bg coffee with fade
    "I've only been here for two minutes and Molly's already staring at me expectantly."

    show molly normal at midleft
    with moveinleft
    m "...well?"

    if with_claudia:
        M "I haven't had the time."
        m "Yeah, sure. I totally believe that."
        M "Really!"
        m "Mhm..."
        "Molly mutters something under her breath that sounds suspiciously like \"Coward.\" I ignore it."
    else:
        M "We broke up."
        m "Really?!"
        M "Don't sound so surprised..."
        m "I didn't think you had it in you. Congrats!"

    if shelldon:
        "The door opens."
        show shelldon normal at midright
        with moveinright
        "He's back. Oh Tides."
        s "Hi there."
        M "Ah, you're back."
        s "What can I say? You guys make damn good coffee."
        "Molly gives me a cheeky look."
        m "I'm gonna go take a smoke break."
        hide molly
        with moveoutright
        M "So...large black coffee?"
        s "Please."
        "I start brewing the coffee, trying not to think about the inevitable awkward conversation with Molly that's soon to follow."
        M "How's your morning going?"
        s "Same as always. You?"
        M "Can't complain."
        "Shelldon smiles. He has a nice smile..."
        "The coffee is done. I pour a cup and hand it to him."
        s "Thanks, have a good day!"
        menu:
            "You Too!":
                hide shelldon
                with moveoutright
                "Shelldon leaves."
            "I'll see you tomorrow?":
                "Shelldon pauses at the door."
                s "Yeah, I'll see you tomorrow."
                hide shelldon
                with moveoutright
                "Shelldon leaves with a smile."
                $ seeing_shelldon = True
    hide molly
    with moveoutleft
    "The rest of the shift goes by quickly. Before I know it, we're about to close."
    "...And then the door rings."
    show gaster normal at midright
    with moveinright
    g "Are you guys still open?"
    "We close in 10 minutes."
    M "Yeah..."
    g "Pog. I need a quad-shot asap."
    "Did he just say pog?"
    "More importantly..."
    M "A quad? It's the middle of the night."
    g "Look, man, I'm going to be progging a raid in a half-hour and I need the energy."
    M "What?"
    "He rolls his eyes."
    g "Can you make it or not?"
    "I already cleaned the machines."
    M "Yeah, I'll do it."
    "My boss would be pissed at me otherwise."
    "I painfully start to work on his drink."
    M "So, what do you play?"
    g "Huh?"
    M "You're a gamer, right?"
    g "Yeah. Uh. Lotta stuff. MMOs, FPS, anything really."
    M "Mmm."
    g "What about you? Do you play anything?"
    menu:
        "Yeah, from time to time.":
            $ gaster = True
            g "Really? We should play something together!"
            M "That's a bit forward, don'tcha think?"
            g "Ah, you're right. Sorry..."
            "As weird as this guy is, I can't help but feel a bit sorry for him."
        "Not really.":
            g "Damn, kinda cringe."
            "Right back at you, buddy."
    "Soon enough, his horrible concoction is finished."
    M "Here you go."
    g "Mmm."
    hide gaster
    with moveoutright
    "He didn't even say thank you."
    $ is_day2 = True
    scene bg black with fade
    if with_claudia:
        "I've been thinking about what Molly told me."
        "I can't stay with Claudia any longer, so I invited her over to talk."
        "I'm nervous."
        $ day_2_breakup = True
        jump breakup
    else:
        jump day3

label day3:
    scene bg playerroom
    "I wake up feeling refreshed. I guess it's because I've broken up with Claudia."
    "It's strange to realize how much my relationship had been weighing on me."
    "But I feel like a whole new horseshoe crab now that I'm single."
    "And now I'm ready to find love."

    scene bg coffee with dissolve
    show molly normal at midleft
    with moveinleft
    "By the time I get to Clawbucks, Molly has already brewed the first round of coffee."
    m "You're awfully chipper this morning. What's up?"
    if day_2_breakup:
        M "I broke up with Claudia."
        m "Wooooooo!"
        "I can't help but smile."
        m "The megabitch is no more!"
    else:
        M "I'm just glad I listened to your advice the other day."
        m "Damn straight! The megabitch is no more!"
    M "No more megabitch!"
    m "Your options are endless now."
    M "Yeah..."
    m "Anybody in mind?"
    menu:
        "That weird dude from last night":
            $ gaster = True
            m "You mean that asshole that showed up right before closing and made us have to clean the espresso machine again?"
            M "Mhm. He was kind of annoying in an endearing way."
            m "I worry about your taste sometimes."
            m "I mean, between him and Claudia I don't think I can trust you to make good decisions regarding your love life."
            "I think I feel offended."
        "That construction worker.":
            $ shelldon = True
            m "With the nice ass?"
            M "I mean...you're not wrong."
            m "So you admit it!"
            M "Yes, fine, I admit it."
            m "I knew it."
            M "Not that it matters. I doubt he feels the same."
        "Not really":
            $ shelldon = False
            $ gaster = False
            m "Shame."
        "...":
            $ molly = True
    m "Well, I'm sure you'll find someone soon."
    if seeing_shelldon:
        show shelldon normal at midright
        with moveinright
        s "Hey."
        m "That's my cue!"
        hide molly
        with moveoutright
        s "Taking another smoke break?"
        M "She does that a lot. Your usual?"
        s "Yes please."
        "I pour his coffee and give it to him."
        s "Thank you."
        hide shelldon
        with moveoutright
        "He walks towards the door."
        "Instead of leaving, he turns back around."
        show shelldon normal at truecenter
        with moveinright
        s "I don't think I ever introduced myself. I'm Shelldon. I work for Clawdius Construction."
        "I've heard of that company. They make massive, state-of-the-art apartment complexes all over the country."
        M "Nice to meet you Shelldon. I'm..."
        s "Don't worry, I already read your name tag."
        M "Oh."
        s "Is that weird?"
        M "No."
        s "Okay."
        "..."
        if shelldon:
            "Tides, damn it. I can't disappoint Molly. The timing of this was too perfect."
            M "So, Shelldon..."
            s "My shift at the construction site ends at 6 tomorrow. You should drop by."
            "I smile. He's too perfect."
            M "I'd love that."
            s "I'll see you then"
            hide shelldon
            with moveoutright
            "He smiles his perfect smile and leaves."
        else:
            s "...Well, I better be going. Have a nice day."
            M "You too."
            hide shelldon
            with moveoutright
        show molly normal at midleft
        with moveinright
        m "So did you hit it off?"
        if shelldon:
            M "I'm visiting him at work after his shift tomorrow."
            m "Nice!"
        else:
            M "Nah, he's all yours."
            m "Well if I knew that, I wouldn't have left."
    hide molly
    with moveoutleft
    "The rest of my shift is pretty mellow. Molly left early, so I'm closing by myself."
    "There's only 20 minutes left and the shop is empty. Hopefully it'll be an easy night."
    show gaster big at truecenter
    with moveinleft
    "Fuck."
    g "Heyyyyyy..."
    show gaster normal at midright
    M "Hi."
    g "So I kinda need another drink."
    M "Pogging again?"
    g "Nah, and it's progging, by the by."
    "I couldn't care less."
    "But still, I couldn't say I wasn't the least bit curious..."
    M "So what are you up to tonight?"
    g "Well, for your information, I'm going to be competing in a tournament!"
    "He looks proud of himself. I suppose it is a bit impressive."
    M "In the middle of the night?"
    g "It's in a different timezone..."
    M "Huh."
    "After a grueling amount of time, Gaster's horrible sludge is complete. He takes it and turns to leave."
    M "Hey..."
    "He turns back to me."
    g "What's up?"
    if gaster:
        M "About your offer last night..."
        g "Uh?"
        M "To play something together?"
        g "Oh. Right."
        "He looks embarrassed."
        M "I'd like to take you up on it."
        g "What, really?! Like, for realsies?"
        "Pft. Kinda cute."
        M "For realsies."
        g "Sick! Let's set something up tomorrow."
        hide gaster
        with moveoutleft
        $ seeing_gaster = True
        if shelldon:
            "I should be done visiting Shelldon by then."
    else:
        M "Can you try showing up earlier? It's two minutes to close, you know."
        "He rolls his eyes at me."
        g "Whatever."
        hide gaster
        with moveoutleft
    "I sigh and start cleaning the espresso machine."
    scene bg black with fade
    jump day4

label day4:
    scene bg street
    "It's my day off."
    "With how crazy this week has been, it's nice to have a quiet day."
    "I decided to go on a walk when-"
    show claudia crying at truecenter
    with moveinright
    M "Claudia?!"
    "I see Claudia walking down the street. Her eyes are red like she's been crying."
    c "Huh?"
    show claudia normal
    "When she turns to see me, her eyes light up."
    c "Tides, it's so good to see you! It feels like forever since we last saw each other."
    M "It's only been a couple days..."
    "Looking closer, it's clear that our breakup hit her hard. Her hair is a mess and her bow is limp."
    M "Are you... doing alright?"
    show claudia crying
    "Claudia instantly bursts into tears."
    "Oh shit."
    c "Noooo... I miss you so muchhhh..."
    "She's bawling in the middle of the street. People are starting to stare."
    M "Um."
    c "I'm sorry (sniff) I know this is my fault (sniff) I wish I could make it up to you (sniff)"
    "I'm not sure how she's sniffing. We don't have noses."
    M "Listen, Claudia..."
    c "(sniff) ... Yeah?"
    menu:
        "... I have to go.":
            "She starts crying a bit harder. It's a shame I couldn't care less."
            c "Okay... (sniff) bye..."
            hide claudia
            with moveoutleft
        "Do you want to come over and talk this out?":
            c "... (sniff) Really?"
            M "Yeah, yeah. Let's just get away from here."
            jump claudia_talk
    "Awkward."
    
    if shelldon:
        jump shelldon_work
    elif gaster:
        jump gaster_date
    elif molly:
        jump molly_date
    else:
        jump badend

label claudia_talk:
    scene bg playerhouse with fade
    show claudia normal at truecenter with moveinright
    "I bring Claudia back to my house. It's better than doing this on the street."
    M "So..."
    "This is already incredibly awkward"
    c "..."
    M "..."
    c "I'm sorry I was such a jerk to you..."
    "I'm surprised she's this self aware."
    c "I just. I was angry, you know?"
    c "We were together for 7 months and we never so much as went on a date."
    c "I thought if I demanded for your attention, we'd actually do something together. Then you broke up with me and I realized I was acting like a bitch for nothing."
    M "Claudia..."
    c "That's another thing! It's not \"Claudia\", it's Clawdia."
    M "What? Really?"
    C "7 months. And you still couldn't spell my name."
    "Well this was certainly enlightening. Now I just need to figure out what to do with this information."
    menu:
        "I still don't think I can forgive you":
            "Clawdia's face drops."
            C "I see..."
            M "I understand where you're coming from, but you hurt me too much. I don't think we were right for each other."
            C "So this is it?"
            M "I think so, yeah."
            C "Oh...(sniff) Goodbye..."
            "She leaves."
            "Glad that's dealt with."
            "She seems to genuinely feel sorry, but I have to do what's best for me. Which isn't her."
            "I still have some more time today..."
            hide claudia

        "Do you think we could start over?":
            C '...!'
            "Clawdia's eyes start glistening with tears."
            C "I'd love to."
            $ claudia_good = True
            hide claudia

    if claudia_good:
        jump claudia_end
    elif shelldon:
        jump shelldon_work
    elif seeing_gaster:
        jump gaster_date
    else:
        jump badend

label shelldon_work:
    scene bg construction with fade
    "I decide to take Shelldon up on his offer and meet him at the end of his shift."
    show shelldon normal at midright
    with moveinright
    M "Hey!"
    s "Hi!"
    "He looks especially rugged after working outside all day. His shell is glistening with sweat. I can't help but admire him..."
    s "Are you ready?"
    M "Sure!"
    hide shelldon
    with moveoutleft
    scene bg bar with fade
    show shelldon normal at midright
    with moveinright
    "He ends up taking me to the bar. We make small talk while waiting for our drinks."
    M "So what's your team working on right now?"
    s "We're building a sustainable housing development. It should be able to hold thousands of horseshoe crabs by the time it's done."
    M "Wow, hard work, huh?"
    s "Yeah, but it's worth it. We get to help people, y'know?"
    menu:
        "Plus it's clearly a good workout...":
            "Shelldon blushes. Maybe I shouldn't have said that."
            M "I mean..."
            s "No, it's okay!"
            "He's awfully red."
            M "You're awfully red."
            "He laughs. That perfect laugh..."
            s "Wanna get out of here?"
            M "Please."
            hide shelldon
            with moveoutright
            scene bg black with fade
            $ shelldon_good = True
        "That sounds really cool.":
            "Shelldon smiles."
            s "After this drink I'm gonna head back to my place..."
            "He's definitely dropping a hint, but..."
            M "I'm flattered, but I had a pretty rough convo with my ex earlier. I think I need some more time."
            "Shelldon's smile weakens."
            s "Oh...I get it."
            M "I'll see you at Clawbucks though?"
            s "Absolutely. Best coffee in town."
            M "You can thank my coworker for that."
            "Molly...."
            "I hope she's not dissapointed with my decision."
            hide shelldon
            with moveoutright
            scene bg black with fade
            "I still have some more time today..."
    if shelldon_good:
        jump shelldon_end
    elif seeing_gaster:
        jump gaster_date
    else:
        jump badend

label gaster_date:
    scene bg arcade with fade
    "I end up meeting Gaster at an arcade that night."
    "I suppose it's fitting."
    show gaster normal at midright
    with moveinleft
    g "Hey!"
    M "Howdy."
    "It's not long before we're sucked into the arcade games."
    "He's really good."
    "Eventually we end up across from each other in a booth"
    g "So..."
    M "So?"
    g "Is this...fun?"
    "Not what I was expecting him to say."
    menu:
        "Yeah, I'm having fun":
            "It's true."
            "Gaster smiles at that."
            g "Pog."
            "I laugh."
            g "Huh? What is it?"
            M "You're a dork, you know that?"
            g "Hey!"
            M "No, no. It's...kinda cute."
            g "He blushes."
            $ gaster_good = True
            scene bg black with fade
            hide gaster
        "...":
            g "Ah."
            M "It's not that I'm having a BAD time, it's just..."
            g "No, no, I get it."
            "He looks a bit sad. Poor thing."
            g "I'm gonna go."
            hide gaster
            "..."
            "Like that, he's gone."
            "I'm getting tired..."
            scene bg black with fade
            hide gaster
    if gaster_good:
        jump gaster_end
    else:
        jump badend

label molly_date:
    scene bg street with fade
    "For some reason, I end up back at the Clawbucks."
    show molly normal at midleft
    with moveinleft
    "Unsurprisingly, Molly's on a smoke break when I get there."
    m "Yo."
    M "Yo."
    "I sit next to her on the curb. She's taking long drags of her joint."
    m "Want a hit?"
    M "I've never smoked before."
    m "No pressure."
    "I think about it for a second."
    M "Eh, life's short. Why not."
    m "Attaboy."
    "Molly passes me the joint. I take a hit and I cough...a lot."
    m "You're not supposed to hold it in, silly!"
    "I try to tell her to fuck off, but I'm coughing too much."
    m "Easy there..."
    "She hands me a water bottle. I take a sip. That seems to have done the trick."
    "We sit in silence for a while, passing the joint back and forth."
    m "So, what's up? I thought you were off today."
    M "I saw Clawdia."
    m "Oh. Shit."
    M "Yeah..."
    m "How'd it go?"
    M "She wasn't doing well."
    m "Karma's a bitch. A megabitch. Serves her right."
    "I smile weakly."
    M "Thanks for your advice, by the way. I don't know what would've happened if you didn't help me get my head out of my ass."
    m "Any time."
    M "No, really. You're a real friend."
    "She smiles, but I cant help but notice a hint of sadness."
    m "Do you know why Claudia bothered me so much?"
    M "Hm?"
    m "It's like she never saw you. She didn't care about getting to know you. You were just a toy to her."
    M "Oh."
    m "She would come visit just to bitch at you and it got on my nerves."
    M "What are you saying?"
    m "..."
    m "I think I could've done better than her."
    "Oh."
    M "Well...you don't know unless you try, right?"
    m "Are you saying what I think you're saying?"
    M "I don't know. could just be the weed talking."
    m "Hah."

    hide molly
    scene bg black with fade

    jump molly_end


label claudia_end:
    scene bg black with fade
    "The next day, we end up going on a second first date."
    "We go to a nice restaurant, and spend a lot of time talking."
    "I learned more about Clawdia in that date alone than I had in all the time I'd known her."
    "I feel like it's the start of something new..."
    "Now I just have to figure out how I'm going to explain this to Molly."
    "{b} Ending 1: Clawdia{/b}"
    jump end

label shelldon_end:
    "Shelldon and I end up staying up all night talking, among other things."
    "We fell asleep in his bed around 3am. When I wake up, I dont see him."
    "Oh shit."
    s "Good morning."
    "Thank the Tides."
    s "I made you some breakfast."
    "I smile. What a guy. And I never would've known if I didn't break up with Clawdia."
    "I should listen to Molly's advice more often."
    "{b} Ending 2: Shelldon{/b}"
    jump end

label gaster_end:
    "Gaster and I end up hanging out the next day too."
    "Instead of going back to the arcade, we stayed at my place."
    "I don't have a bunch of games, so we end up playing Mario Kart."
    "I even managed to beat him once or twice."
    "It felt like it was the start of something new."
    "{b} Ending 3: Gaster O. Pod"
    jump end

label molly_end:
    "The next day, neither of us had work, so we hung out at my place."
    "We sat on the couch, got high, and laughed at shitty movies."
    "To be honest, it was one of the best dates I'd ever been on."
    "With the way this week had been going, I can't say that I was expecting to go out with my coworker by the end of it."
    "But I'm not complaining."
    "{b} Ending 4: Molly Usque"
    jump end

label badend:
    scene bg playerroom with fade
    "I end up back in my room."
    "I don't know why I'm here..."
    "Probably because I have nothing better to do."
    "Huh."
    "I guess I have nothing to do now."
    "No one to hang out with."
    "Is this was the rest of my life is going to be like?"
    "I broke up with Clawdia, I met some people but we didn't click..."
    "Am I going to be lonely forever?"
    "I guess so..."
    scene bg black with fade
    "{b} Ending 5: Sad Crab"
    jump end

label end:
    return
