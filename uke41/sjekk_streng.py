def telle_tegn(streng,sjekk):
    teller = 0
    for tegn in streng:
        if tegn.lower() == sjekk:
            teller +=1
    return teller

dikt = """ (Tool - Lateralus)
Black then white are all I see in my infancy
Red and yellow then came to be, reaching out to me
Lets me see

As below so above and beyond, I imagine
Drawn beyond the lines of reason
Push the envelope, watch it bend

Over thinking, over analyzing separates the body from the mind
Withering my intuition, missing opportunities and I must
Feed my will to feel my moment, drawing way outside the lines

Black then white are all I see in my infancy
Red and yellow then came to be, reaching out to me
Lets me see
There is so much more
And beckons me to look through to these infinite possibilities

As below so above and beyond, I imagine
Drawn outside the lines of reason
Push the envelope, watch it bend

Over thinking, over analyzing separates the body from the mind
Withering my intuition leaving opportunities behind

Feed my will to feel this moment
Urging me to cross the line
Reaching out to embrace the random
Reaching out to embrace whatever may come

I embrace my desire to
I embrace my desire to
Feel the rhythm, to feel connected
Enough to step aside and weep like a widow
To feel inspired
To fathom the power
To witness the beauty
To bathe in the fountain
To swing on the spiral
To swing on the spiral to

Swing on the spiral
Of our divinity
And still be a human

With my feet upon the ground I lose myself
Between the sounds and open wide to suck it in
I feel it move across my skin
I'm reaching up and reaching out
I'm reaching for the random or whatever will bewilder me
Whatever will bewilder me
And following our will and wind we may just go where no one's been
We'll ride the spiral to the end and may just go where no one's been

Spiral out, keep going
Spiral out, keep going
Spiral out, keep going
Spiral out, keep going
"""


tegn = input("Hvilket tegn vil du telle i diktet To be or not...? ")
antall = telle_tegn(dikt,tegn)
print("Diktet inneholder",antall,"av tegnet",tegn)

