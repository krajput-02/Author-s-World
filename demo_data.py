# Fallback data used when the AI service is unavailable.
# These results are about the SAMPLE chapter below, not about the user's text.

DEMO_CHAPTER = (
    "The sea was loud that night. "
    "Notwithstanding the deteriorating condition of the structure, which had been neglected by "
    "successive municipal administrations that lacked either the funds or the inclination to "
    "maintain it, Maya ascended the staircase with a deliberateness born of apprehension. "
    "She held the lantern tight. "
    "The lamp's catadioptric lens, an assemblage of concentric prisms that refracts and magnifies "
    "illumination, had been calibrated by her grandfather according to principles she could "
    "scarcely comprehend. "
    "Having ascertained that the mechanism, whose rotation depended upon a clockwork apparatus "
    "requiring periodic winding, had ceased functioning, she surmised that someone had "
    "deliberately interfered with it. "
    "Her grandfather's notebook, replete with cryptic annotations concerning tidal patterns, "
    "maritime signals, and the unexplained absence of the previous keeper, suggested that the "
    "lighthouse concealed more than it revealed. "
    "Whether the locked door at the summit, secured by a rusted padlock of considerable antiquity, "
    "guarded something precious or something dangerous, she could not determine without "
    "relinquishing the safety of the stairwell."
)

DEMO_SENTENCES = [
    {
        "original": "Notwithstanding the deteriorating condition of the structure, which had been neglected by successive municipal administrations that lacked either the funds or the inclination to maintain it, Maya ascended the staircase with a deliberateness born of apprehension.",
        "why": "Very long, with a big interruption in the middle and heavy words like 'notwithstanding' and 'apprehension'.",
        "simpler": "The lighthouse was falling apart because the town had ignored it for years, but Maya climbed the stairs slowly and nervously.",
    },
    {
        "original": "The lamp's catadioptric lens, an assemblage of concentric prisms that refracts and magnifies illumination, had been calibrated by her grandfather according to principles she could scarcely comprehend.",
        "why": "Technical terms ('catadioptric', 'concentric prisms') and a long chain of ideas.",
        "simpler": "The lamp's lens was made of rings of glass that bend and boost the light. Her grandfather had set it up in ways she barely understood.",
    },
    {
        "original": "Having ascertained that the mechanism, whose rotation depended upon a clockwork apparatus requiring periodic winding, had ceased functioning, she surmised that someone had deliberately interfered with it.",
        "why": "Formal words ('ascertained', 'surmised') and three ideas packed into one sentence.",
        "simpler": "She saw that the clockwork that turned the lamp had stopped. Someone must have tampered with it.",
    },
    {
        "original": "Her grandfather's notebook, replete with cryptic annotations concerning tidal patterns, maritime signals, and the unexplained absence of the previous keeper, suggested that the lighthouse concealed more than it revealed.",
        "why": "A long list inside the sentence and abstract wording ('replete', 'cryptic annotations').",
        "simpler": "Her grandfather's notebook was full of strange notes about tides, ship signals, and the missing keeper. It hinted that the lighthouse hid secrets.",
    },
    {
        "original": "Whether the locked door at the summit, secured by a rusted padlock of considerable antiquity, guarded something precious or something dangerous, she could not determine without relinquishing the safety of the stairwell.",
        "why": "The main point comes at the very end, and rare words ('antiquity', 'relinquishing') slow the reader down.",
        "simpler": "Maya could not tell if the locked door at the top hid something precious or dangerous. To find out, she would have to leave the safe stairwell.",
    },
]

DEMO_BLOG = (
    "The lighthouse had stood on the cliff for two hundred years, and Maya had never been inside it. "
    "Until the night the light went out. In this chapter, Maya climbs the winding stairs with nothing "
    "but an old lantern and her grandfather's worn notebook. Each step brings a new question. Why did "
    "the keeper leave so suddenly? Who has been lighting the lamp all these years? And what is hidden "
    "behind the locked door at the top? Told in simple, vivid scenes, the chapter mixes quiet mystery "
    "with warm family memories. You will feel the cold sea wind, hear the creaking stairs, and wonder "
    "what Maya will find. Along the way, Maya learns that some secrets are kept out of love. If you "
    "enjoy gentle mysteries with heart, this story invites you to climb along. Step inside, turn the "
    "page, and see what waits in the dark."
)
