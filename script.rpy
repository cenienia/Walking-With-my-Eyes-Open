#show senku weak:
        #zoom 0.15 xalign 1.0 yalign 0.4 
        #pause 0.5


# s=senku
define s = Character("Senku")
# g=gen
define g = Character("Gen")
#N=narrator
define n = Character("")

image senku = "#38b373"
define bm = Character("senku", window_background=Frame("senku", 25, 25) )

# The game starts here.

label start:
scene bloody
pause 3.0

n "{i}When Senkuu was wrenched out of sleep in his newly minted observatory by a chest wracking cough and a handful of blood covered petals stuck to the floor, he had exactly four gut reactions and one conscious thought in specifically that order.{/i}"

pause 2.0

s "{b}This is going to be exhilarating.{/b}"

pause 3.0

scene forestday

pause 3.0

show gen happysmirk:
        zoom 0.15 xalign 1.0 yalign 0.4 

g "♫... ♪ Finally free!"

n "{i}A hand hooks around his collar.{/i}"

show gen smileyell

show senku normal:
        zoom 0.15 xalign 0.8 yalign 0.4 
s "Come help me over here, modern man. You must know at least a little more chemistry than the villagers."


scene hut
pause 2.0

show gen normal:
        zoom 0.15 xalign 1.0 yalign 0.4
show senku pondering:
        zoom 0.15 xalign 0.8 yalign 0.4
s "New experiment, I need you to be my research partner. Though, honestly, that’s probably overstating your role a bit."

g "Eeeh, I’m flattered that you’re finally appreciating my brilliance, Senkuu-chan, But, don’t you normally go to Chrome for the science things?"

show senku mid

s "Yeah and I’d definitely prefer Chrome for this, too; but, unfortunately, it looks like this one has to be you if I’m going to get any real work done."
s "Plus, I’d rather the village not find out about this one. At least, not until it’s done."

n "He seemed hesitant. Looks like today was the most interesting place Gen could be."

show gen happysmirk

g "Don’t worry, Senkuu-chan, I’m very, very good at being discreet. You can tell me aaaannnything, my lips are completely sealed."

n "Senku seemed to already be regretting this."

show gen smile

g "So, what’s this ultra big science-y secret that needs my help specially?"

n "{i}Senku rolled his eyes, taking a single breath.{/i}"

pause 3.0

s "I'm dying."

pause 1

show gen yell

g "excuse me?"          
g "You're.. you're what?" 
g "{i}this has to be some kind of sick joke.. or  he’s just being overdramatic. But he tends to only be dramatic about his should-be-insane science discovereries!{/i}"
g "How.. why?" 
 
show senku smirk
 
s "You can relax, mentalist. I said dying, not that I’m going to die. Quit lo oking like that. I already have a plan worked out. Trust me, I don’t have a millimetre's worth of interest in dying before we even get to the really exciting stuff."
        
show gen shocked

g "{i}wheww...{/i}" 
g "So.. how are you dying?"

show senku normal

s "hanahaki disease."

show gen yell

g "Eeeeeeeh?!"
g "{i}Did Senkuu just say….did Senkuu just..{/i}"

s "Hanahaki Disease, also known as the flower sickness, rare but most often originating in East Asian regions like–"

g "I know what it is! That’s supposed to be a {i}myth!{/i}"

pause 0.5       

show senku pondering

s "Hardly. Though I suppose that’s fair, it was more found in folklore in the past half a century--or, well, three thousand and six hundred centuries, now--but, the first medically documented case was in 2009."
pause 1
s "Admittedly, it’s still one of the rarest diseases documented. Even in our era, doctors didn’t know much about its causes or development. No one’s even found a full fledged cure yet or a treatment that didn’t involve invasive surgery."
 
show senku smirk

g "{i}did this guy just.. smirk?! He’s insane..{/i}"

s "Just think, mentalist, we’re going to use our stone world to make a groundbreaking medical discovery that even our experts couldn’t figure out."

show gen shocked

g "Hmmm, yes, I’m very excited for you, why get you the telescope when apparently we could have just given you a deadly disease for your birthday? Congratulations."

show senku normal

s "I liked the telescope, too,"

show gen smileyell

g "Fantastic. One teensy tiny question, what happens on the off chance we can’t figure it out and you die horrifically from something out of a fairytale!"

show gen shocked

show senku pondering

s "Fairytale or not, all fantasy has to have a scientific base. If we find out the underlying rules of this disease, we should be able to hypothesize a cure. It should even work out on our timeline."

s "Based on the reports, the average span of terminal Hanahaki Disease takes two to three months. We’ll have an answer one way or another by the time spring gets here and the village has to deal with Tsukasa."

show senku normal

s "We’ll figure this out, mentalist. I’m ten billion percent sure of it."

show gen pondering

g "{i}He’s right. We can do this. Compared from freeing the entire world from stone, this was even comparatively easy. He currently knew more about medicine than anyone in the world and I am an expert in psychology. If anyone could figure out a love disease, it’s us.{/i}"
g "{i}Oh yeah..{/i}"

show gen sleevesmirk

g "Oooh ho, and, now, I see why you just had to have me as your research partner. Hmmm, {i}Senkuu-chan ?{/i}"

s "Well, yeah, I figured it was obvious."

g "Oh, absolutely, who better to know about wooing someone than a mentalist! Don’t you worry, Senkuu-chan, whoever you’re pining over, I can get them falling over their feet in no time."

show senku mid 

show gen sleevehappy

g "Really, I’d be happy to. Even without the whole dying thing, this is the most interesting task I’ve had in weeks. Minus the whole preparing for war thing."

pause 0.8 

s "Mentalist–"

g "Now, first things first, tell me who the lucky lovebird-to-be is!"

s "..."

show gen sleevesmirk

g "Come on, Senkuu-chan, no need to be shy! I’m going to have to find out anyway if you want my help. Hmmm, or would it be easier if I guessed?"

pause 3.0

s "Sure, guess..."



default activity_set = set()



menu activity: 
        set activity_set

        "Kohaku":
                jump Choice_1
        "Chrome":
                jump Choice_2
        "Taiju":
                jump Choice_3
        "Tsukasa":
                jump Choice_4

show gen pondering

g "{i}Well there go all my worst scenario plans..{/i}"
g "Then who is it?"

pause 1.0

show gen yell

g "Wait, Do you even know who it is?"

show senku pondering

s "Yeah, it was absolutely clear when I saw the flower. Hanahaki Disease is reported to always be the flower the patient associates with the person they’re in love with. Though I have my doubts on whether that’s actually-"

show gen pondering

g "So, what’s the flower?"


show senku weak

n "{i}he huffed like he always did when he got derailed from science but obligingly reached for his belt and drew out a folded piece of cloth, handing it over to Gen.{/i}"

pause 1.0

show gen shocked

g "...!"

scene flowers with dissolve
        
hide gen 

hide senku

n "five black nightshades laid in his hand."

pause 1.0

g "Black nightshades… so, it’s me? You’re….you’re in love with me?"

scene hut

show gen pondering:
        zoom 0.15 xalign 1.0 yalign 0.4
show senku smirk:
        zoom 0.15 xalign 0.8 yalign 0.4


s "Enough to vomit flowers, apparently."

show senku normal

g "..."

show gen shocked

g "..!"

show gen yell

g "wait.. is this a {i}confession?!{/i}"

show senku pondering

s "A gesture to reveal feelings, specifically of a romantic nature.."

show senku smirk

s "Yeah, I suppose it is in a technical sense. I was more thinking of it as a research proposal."

show gen pondering

g "..."

show gen shocked

g "But, I don’t...I don’t feel the same way,"
g "{i}This is a problem. I never considered Senku to be the romantic type..{/i}"
g "{i}Had it been anyone else I would’ve been confident in my abilities, to, at the very least, make a very good effort at wooing them over to Senkuu’s side, maybe spark some interest.{/i}"

show gen pondering

show senku mid

g "{i}That doesn’t work if I’m trying to woo myself. He's made the ill-advised mistake of falling for me, who probably just broke is heart-{/i}"

show gen shocked

g "{i}Oh fuck. Have I just broken Senku’s heart? That’s possible?{/i}"
g "{i}I should’ve just lied, or-{/i}"

n "{i}cough{/i}"

show senku weak

s "Oi, mentalist, whatever you’re working yourself up about, stop."

show gen shocked 

pause 0.5

show senku normal 

s "I know. I’m perfectly aware that you’re not in love with me. I figured that out before I even decided to tell you. Wouldn’t be much of an experiment if you cured it right on the first day, would it?"

g "Then, why am I here?"

s "I told you, as a research partner, we’re basically working with a blank slate right now when it comes to what we know about the disease."
show senku pondering
s "Does it have to be love? What kind of love? How is that translated to brain activity? Where is the plant even growing and how? What kind of response slows the progression? Can it even be slowed significantly?"
s "There’s blood pressure monitoring, heart rate measure, proxemics, hormone release, biological susceptibility- a billion different variables and I can only study half of them without you here to show how your influence affects the results."

pause 0.5

show senku smirk

s "I told you, mentalist, we’re going to study this step by step until we find some answers. And the first step: Observation!”"

hide senku with dissolve
hide gen with dissolve

scene black with dissolve


return



# kohaku
label Choice_1:
        g "Weeeellll, I guess the most obvious choice would be Kohaku-"

        show senku yelling

        s "{i}Obvious?!{/i} Kohaku?"

        show gen pondering

        g "{i}Apparently not, okay and the rest get more tricky. He came to me first rather than them. Now, normally he’s a fairly straight forward person so I’d guess he’d go to them to start; but, here he wanted my advice first, so there must be some kind of problem. So, who is it…{/i}"
        show senku mid
        show gen pondering
jump activity


# Chrome and Ruri
label Choice_2:
        g "Oh, it’s Chrome, isn’t it? You’re worried because of his thing with Ruri."

        pause 3.0

        show senku weak

        s "What?"

        g "No worries, that childhood crush has years without results, so I think you still have a chance-"

        s "It's not Chrome."

        pause 0.8

        show gen sleevesmirk

        g "Then, is it Ruri? The ex-wife thing could-"

        show senku yelling 

        s "No!"

        show senku mid

        g "Chrome {i}and{/i} Ruri! Ambitious, Senkuu-chan, but-"

        s "I regret every second of this conversation."

        show gen pondering

        g "Okay, so not them.."

        show senku mid
        show gen pondering
jump activity

# Taiju/yuziriha
label Choice_3:
        show senku mid
        g "Taiju?"

        show senku weak

        s "Gross."

        
        show gen sleevesmirk

        g "-Yuziriha?"

        s "Seriously, mentalist."

        show senku mid
        show gen pondering
jump activity

# tsukasa
label Choice_4:
        g "Don’t tell me.. It’s tsukasa isn’t it!"

        scene tsukasa with dissolve
        
        show senku shocked:
                zoom 0.15 xalign 0.8 yalign 0.4
        show gen yell:
                zoom 0.15 xalign 1.0 yalign 0.4


        g "shit, it totally is."

        show gen

        show senku yelling

        s "No, but, you know what? I fucking wish it was Tsukasa now! At least, he has a brain." 

        g "{i}Well.. it was worth a try..{/i}"
        
        scene hut with dissolve

        show gen pondering:
                zoom 0.15 xalign 1.0 yalign 0.4
        show senku mid:
                zoom 0.15 xalign 0.8 yalign 0.4
        
jump activity   