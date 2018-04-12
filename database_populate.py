def showName(a):
    print(a.name, ':', a.id)


categorySum = ['The action genre in anime depicts extremely high levels of intense action. More often than not, you’ll be witnessing thrilling battles and action-packed fight scenes in the shows from this genre. These series will make you jump off your seat or knock your socks off. Overall, the action genre usually possesses lots of battle scenes, fluid animation, and highly-engaging elements that will make your adrenaline rush!',
               'The adventure genre is about travelling and undertaking an adventure in a certain place or around the world (which may sometimes escalate to the whole universe or even to the other dimensions). In this genre, the main characters don’t usually stay in one place. They venture into several different places, usually with a goal in mind (e.g. searching for treasure, exploring some new place, defeating a heinous villain, or saving the world). Adventure anime are so broad and flexible that these shows can usually stretch to a huge number of episodes as well as overlap with multiple genres, usually with action.',
               'The main purpose of the comedy genre is…you got it…to make you laugh! If it fails to make you laugh or at least make you giggle, then it’s a failure. But then again, humor can depend on your personal sense of humor. The animation may not be as impressive as TV shows in the action and drama category, but that can be forgiven for the laughs. Funny moments, hilarious scenes, wacky dialogue, comical happenings—all of these are covered by the comedy genre in anime!',
               'Bringing us tears and a wave of emotions is basically what the drama genre does best! Drama anime tends to connect the viewers to the experiences of the characters. This results in viewers feeling what the characters are going through. Whether it\'s a tickle of emotion or a barrage of feelings, the goal of these series is to touch our hearts. In anime, one of the greatest signs that the drama effectively worked is if it was able to make you cry.',
               'When one says slice of life, that means the mundane good ol’ life. Stories depicted in this genre are realistically set in the domain of real life. Nothing out-of-the-blue happens, but that’s the point! Everyday life is portrayed in a realistic light, with nothing out of the extraordinary wrecking the premise.',
               'The fantasy genre in anime primarily deals with fantasy worlds and surreal events and locations. Most of the time, the setting is in a magical world where the characters start an adventure. Sometimes they get sent there from the real world. Magic is oftentimes a component of this genre, and various mystical elements serve as the building blocks of the story. You’ll often know it’s a fantasy anime if the environment and atmosphere seems so dazzling and dreamlike that it’ll make you feel captivated and allured.',
               'Magic, in all its essence, is about magical stuff like spells and incantations. It can also include magical sources, beings that grants wishes, and good ol’ sleeve tricks. One of the most famous themes in the magic genre is magical girls. It is so popular that it might just become a whole new genre on its own in the future.',
               'When one says supernatural, they’re referring to stuff or events that are odd and out-of-the-blue. For this category, supernatural might refer to something mythical, mystical, bizarre, or something outside the bounds of accepted reality. There’s a shadow of mystery often found in shows involved with this genre.',
               'It’s not difficult to spot the horror genre in anime. Usually, if there are ghosts, monsters, gore, and creeps, then you’re likely watching a horror series. Heavy gore and bloody violence is a common trait. The most important factor for a show to be considered horror is its ability to scare and creep you out.',
               'If there’s one thing that’s similar in all mystery anime shows, it is the existence of a central enigma. Whether it’s an event, a place, or an item, there’s some sort of mystery surrounding the narrative. In the history of anime, the most popular shows in the genre have featured detectives and gumshoes.',
               'Psychological anime are shows that delve into how the mind and psyche work. This genre tackles everything on a psychological level (sometimes even philosophical). You’ll often find mind games here as well as battles where the use of the wits is the primary focus. Series in this genre will play with your mind and make you think hard.',
               'Romance is all about love and sweet moments. Shows involved with this genre often have the skill to tug everyone’s heartstrings with their romantic scenes and tender moments. The focus of these shows is the romantic relationships between the characters as well as their blooming love with one another. You’ll often find romance anime tightly tied with the shoujo subgenre, but it also works pretty well with comedy, harem, and drama.',
               'Sci-fi (short for science fiction) is a genre that showcases scientific and technological elements in its story. Machines and various kinds of technologies are staples of this genre. Most of the time, its focus is on the advancement and development of science and technology. That is why you’ll often find sci-fi combined with subgenres such as mecha and space.']
categories = [
    'Action',
    'Adventure',
    'Comedy',
    'Drama',
    'Slice of Life',
    'Fantasy',
    'Magic',
    'Supernatural',
    'Horror',
    'Mystery',
    'Psychological',
    'Romance',
    'Sci-Fi'
]
anime = {
    'Action': [
        {'name': 'Gurren Lagann', 'summary': "Simon and many others live underground to escape the terror of Beastmen. Their dream of returning to the Earth's surface seems possible when a giant mecha suddenly crashes into their underground home."},
        {'name': 'Fullmetal Alchemist Brotherhood', 'summary': "Brothers Edward and Alphonse Elric search for the Philsopher's Stone, hoping to restore their bodies, which were lost when they attempted to use their alchemy skills to resurrect their deceased mother. Edward, who lost only limbs, joins the State Military, which gives him the freedom to continue the search as he tries to restore his brother, whose soul is tethered to earth by a suit of armor. However, Edward and Alphonse are not the only ones seeking the powerful stone. And as they search, they learn of a plot to transmute the entire country for reasons they cannot comprehend."}
    ],
    'Adventure': [
        {'name': 'One Piece',
            'summary': "The series focuses on Monkey D. Luffy, a young man who, inspired by his childhood idol and powerful pirate \"Red Haired\" Shanks, sets off on a journey from the East Blue Sea to find the famed treasure One Piece and proclaim himself the King of the Pirates. In an effort to organize his own crew, the Straw Hat Pirates (麦わら海賊団篇 Mugiwara Kaizoku-dan), Luffy rescues and befriends a swordsman named Roronoa Zoro, and they head off in search of the One Piece. They are joined in their journey by Nami, a navigator and thief; Usopp, a sniper and a liar; and Sanji, a womanizing chef. They acquire a ship named the Going Merry and engage in confrontations with notorious pirates of the East Blue. As Luffy and his crew set out on their adventures, others join the crew later in the series, including the doctor and anthropomorphized reindeer Tony Tony Chopper, an archaeologist and former assassin Nico Robin, a cyborg shipwright Franky, and skeletal musician Brook, and they also acquire a new ship named Thousand Sunny."},
        {'name': 'Hunter X Hunter',
            'summary': "Hunters (ハンター Hantā) are licensed, elite members of humanity who are capable of tracking down secret treasures, rare beasts, or even other individuals.[2] To obtain a license one must pass the rigorous annual Hunter Examination run by the Hunter Association, which has a success rate of less than one in a hundred-thousand.[3] A Hunter may be awarded up to three stars; a single star for making \"remarkable achievements in a particular field\"; they may then be upgraded to two stars for \"holding an official position\" and mentoring another Hunter up to single star level; and finally upgraded to three stars for \"remarkable achievements in multiple fields.\""}
    ],
    'Comedy': [
        {'name': 'Gintama',
            'summary': "The story is set in an alternate late-Edo period, where humanity is attacked by aliens called \"Amanto\" (天人, \"Sky People\"), and the samurai of Japan join the battle against the aliens, but when the shōgun realizes the power of aliens, he betrays the samurai and surrenders to the aliens. The shōgun writes an unequal contract with aliens which allows the aliens to enter the country and places a ban on carrying swords in public. The swords of samurai are taken away so they can no longer resist the aliens. After that, the shogunate becomes a puppet government."},
        {'name': 'The Melancholy of Haruhi Suzumiya',
            'summary': "Kyon is a cynical and incredulous student of North High School in Nishinomiya. He is dragged along by his classmate, the eponymous protagonist Haruhi Suzumiya, an eccentric girl who is seeking supernatural phenomena and figures such as aliens, time travelers, and espers. With Kyon's reluctant help, Haruhi establishes a club called the \"SOS Brigade\" (SOS団 Esu-Ō-Esu Dan), short for \"Spreading excitement all Over the world with Haruhi Suzumiya Brigade\" (世界を大いに盛り上げるための涼宮ハルヒの団 Sekai o Ōini Moriageru Tame no Suzumiya Haruhi no Dan) (In the school's official paperwork Kyon renamed it \"Support the Student Body by Overworking to Make the World a Better Place Student Service Brigade\") to investigate mysterious events. Haruhi later recruits three additional members: the laconic bibliophile Yuki Nagato, the shy and timid Mikuru Asahina, and the extremely friendly transfer student Itsuki Koizumi. These members soon reveal themselves (to Kyon) to be the types of extraordinary characters that Haruhi is seeking. They have been sent by their organizations to observe Haruhi — who is unaware that she possesses destructive reality warping powers — and to prevent these powers from being unleashed. Each of the three believe that it would be dangerous if Haruhi knew she had such powers. To all of these four the big mystery is why Kyon is in the brigade. Each of the three remarks that Haruhi chose Kyon. All of the four work to keep life interesting for Haruhi and keep her from getting bored and imagining up some new world, as doing this would destroy their world."}
    ],
    'Drama': [
        {'name': 'Clannad', 'summary': "Tomoya Okazaki is a delinquent who finds life dull and believes he'll never amount to anything. Along with his friend Youhei Sunohara, he skips school and plans to waste his high school days away."},
        {'name': 'Anohana: The Flower We Saw That Day', 'summary': "A group of six sixth-grade-age[1] childhood friends drift apart after one of them, Meiko \"Menma\" Honma, dies in an accident. Years[2] after the incident, the leader of the group, Jinta Yadomi, has withdrawn from society, does not attend high school,[3] and lives as a recluse. One summer day, the ghost of an older-looking Menma appears beside him and asks to have a wish granted, reasoning that she cannot pass on into the afterlife until it is fulfilled. At first, he only tries to help her minimally because he thinks he is hallucinating. But since Menma does not remember what her wish is, Jinta gathers his estranged friends together once again, believing that they are the key to resolving this problem. All of the group joins him, though most of them do so reluctantly. However, things grow increasingly complicated when his friends accuse him of not being able to get over the death of Menma, for Jinta is the only one who can see Menma's ghost and his friends think he is seeing things. But as matters progress, it is realized that Jinta is not the only person in the group who is having trouble letting go of the past. It is revealed that all of the group members blame themselves for Menma's death and long-hidden feelings are rekindled. The group struggles as they grow from trying to help Menma move on and help each other move on as well."}
    ],
    'Slice of Life': [
        {'name': 'Barakamon',
            'summary': "Seishū Handa is a pro calligrapher, despite his young age. When the elderly curator of an exhibition criticizes his calligraphy for being too unoriginal (\"like a textbook\"), Seishū gets angry and punches him. Because of this, his father sends him off for a retreat on Gotō Island, near Kyūshū. There, he meets the colorful villagers, interacts with them, and begins to find his own style."},
        {'name': 'Lucky Star',
            'summary': "Lucky☆Star follows the daily lives of four cute high school girls—Konata Izumi, the lazy otaku; the Hiiragi twins, Tsukasa and Kagami (sugar and spice, respectively); and the smart and well-mannered Miyuki Takara."}
    ],
    'Fantasy': [
        {'name': 'Nanatsu no Taizai', 'summary': "In a world similar to the European Middle Ages, the feared yet revered Holy Knights of Britannia use immensely powerful magic to protect the region of Britannia and its kingdoms. However, a small subset of the Knights supposedly betrayed their homeland and turned their blades against their comrades in an attempt to overthrow the ruler of Liones. They were defeated by the Holy Knights, but rumors continued to persist that these legendary knights, called the \"Seven Deadly Sins\" were still alive. Ten years later, the Holy Knights themselves staged a coup d’état, and thus became the new, tyrannical rulers of the Kingdom of Liones."},
        {'name': 'Inuyasha', 'summary': "Based on the Shogakukan award-winning manga of the same name, InuYasha follows Kagome Higurashi, a fifteen-year-old girl whose normal life ends when a demon drags her into a cursed well on the grounds of her family's Shinto shrine. Instead of hitting the bottom of the well, Kagome ends up 500 years in the past during Japan's violent Sengoku period with the demon's true target, a wish-granting jewel called the Shikon Jewel, reborn inside of her."}
    ],
    'Magic': [
        {'name': 'Little Witch Academia', 'summary': "\"A believing heart is your magic!\"—these were the words that Atsuko \"Akko\" Kagari's idol, the renowned witch Shiny Chariot, said to her during a magic performance years ago. Since then, Akko has lived by these words and aspired to be a witch just like Shiny Chariot, one that can make people smile. Hence, even her non-magical background does not stop her from enrolling in Luna Nova Magical Academy."},
        {'name': 'Magical Doremi', 'summary': "Harukaze Doremi considers herself to be the unluckiest girl in the world. Her parents are always fighting, her little sister makes fun of her, and her crush pines after another girl. If only Doremi could just wave a magic wand, she would have a much better life—or so she used to think."}
    ],
    'Supernatural': [
        {'name': 'Durarara!!', 'summary': "In Tokyo's downtown district of Ikebukuro, amidst many strange rumors and warnings of anonymous gangs and dangerous occupants, one urban legend stands out above the rest—the existence of a headless \"Black Rider\" who is said to be seen driving a jet-black motorcycle through the city streets."},
        {'name': 'Bakemonogatari', 'summary': "Koyomi Araragi, a third-year high school student, manages to survive a vampire attack with the help of Meme Oshino, a strange man residing in an abandoned building. Though being saved from vampirism and now a human again, several side effects such as superhuman healing abilities and enhanced vision still remain. Regardless, Araragi tries to live the life of a normal student, with the help of his friend and the class president, Tsubasa Hanekawa."}
    ],
    'Horror': [
        {'name': 'Parasyte -the maxim-', 'summary': "All of a sudden, they arrived: parasitic aliens that descended upon Earth and quickly infiltrated humanity by burrowing into the brains of vulnerable targets. These insatiable beings acquire full control of their host and are able to morph into a variety of forms in order to feed on unsuspecting prey."},
        {'name': 'Hell Girl', 'summary': "Have you heard of Hell Correspondence? Those with a powerful grudge may only access this mysterious website at midnight, allowing them to enter anyone's name and have that person be ferried straight to hell. Ai Enma, the Hell Girl, will not judge whether or not the chosen target deserves punishment; she will merely exact revenge on them for you. Not much is known about this young girl other than that she swiftly carries out her tasks with the help of three straw dolls. There is just one catch, however—as payment for carrying out such a request, the user must condemn themselves to an afterlife in hell."}
    ],
    'Mystery': [
        {'name': 'Detective Conan',
            'summary': "Shinichi Kudou, a great mystery expert at only seventeen, is already well known for having solved several challenging cases. One day, when Shinichi sees two suspicious men and decides to follow them, he inadvertently becomes witness to a disturbing illegal activity. When the men catch Shinichi, they dose him with an experimental drug formulated by their criminal organization and abandon him to die. However, to his own astonishment, Shinichi is still alive and soon wakes up, but now, he has the body of a seven-year-old, perfectly preserving his original intelligence. He hides his real identity from everyone, including his childhood friend Ran Mouri and her father, private detective Kogorou Mouri, and takes on the alias of Conan Edogawa (inspired by the mystery writers Arthur Conan Doyle and Ranpo Edogawa)."},
        {'name': 'Hyouka', 'summary': "Energy-conservative high school student Houtarou Oreki ends up with more than he bargained for when he signs up for the Classics Club at his sister's behest—especially when he realizes how deep-rooted the club's history really is. Begrudgingly, Oreki is dragged into an investigation concerning the 45-year-old mystery that surrounds the club room."}
    ],
    'Psychological': [
        {'name': 'Death Note', 'summary': "A shinigami, as a god of death, can kill any person—provided they see their victim's face and write their victim's name in a notebook called a Death Note. One day, Ryuk, bored by the shinigami lifestyle and interested in seeing how a human would use a Death Note, drops one into the human realm. \n High school student and prodigy Light Yagami stumbles upon the Death Note and—since he deplores the state of the world—tests the deadly notebook by writing a criminal's name in it. When the criminal dies immediately following his experiment with the Death Note, Light is greatly surprised and quickly recognizes how devastating the power that has fallen into his hands could be. "},
        {'name': 'Zetsuen no Tempest', 'summary': "Yoshino Takigawa, an ordinary teenager, is secretly dating his best friend Mahiro's younger sister. But when his girlfriend Aika mysteriously dies, Mahiro disappears, vowing to find the one responsible and make them pay for murdering his beloved sister. Yoshino continues his life as usual and has not heard from Mahiro in a month—until he is confronted by a strange girl who holds him at gunpoint, and his best friend arrives in the nick of time to save him."}
    ],
    'Romance': [
        {'name': 'Honey and Clover', 'summary': "Yuuta, Takumi, and Shinobu share a six-tatami room apartment with no bath. The rent is low and it's perfect for poor college students such as themselves. Shinobu is a mysterious, quirky person, who does things on a whim. Takumi is passionate both in work and love, and Yuuta is a simple person with simple dreams and desires. That is, until he meets Hagumi, a petite girl with enormous amount of talent. Hagumi is fondly called Hagu by Shuuji, who serves as Hagu's guardian. Hagu meets Ayumi, nicknamed Ayu, and they become close friends almost instantly. Meanwhile, Ayu falls for one of the boys..."},
        {'name': 'Toradora', 'summary': "Ryuuji Takasu is a gentle high school student with a love for housework; but in contrast to his kind nature, he has an intimidating face that often gets him labeled as a delinquent. On the other hand is Taiga Aisaka, a small, doll-like student, who is anything but a cute and fragile girl. Equipped with a wooden katana and feisty personality, Taiga is known throughout the school as the \"Palmtop Tiger.\""}
    ],
    'Sci-Fi': [
        {'name': 'Space Dandy', 'summary': "The universe is a mysterious and strange place, full of even stranger and more mysterious aliens. Dandy's job is to hunt down unclassified aliens and register them for a reward. It sounds easy enough, but something weird always seems to happen along the way, like chance meetings with zombies, mystical ramen chefs, and adorable orphans. Hunting down aliens may not be easy, but it's definitely never boring."},
        {'name': 'Cowboy Bebop', 'summary': "In the year 2071, humanity has colonized several of the planets and moons of the solar system leaving the now uninhabitable surface of planet Earth behind. The Inter Solar System Police attempts to keep peace in the galaxy, aided in part by outlaw bounty hunters, referred to as \"Cowboys.\" The ragtag team aboard the spaceship Bebop are two such individuals."}
    ]
}

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from database_setup import Base, Category, CatalogItem, User
    engine = create_engine('sqlite:///catalog.db')

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    User1 = User(name="Abhishek Chopra", email="phoenix.prog1796@gmail.com",
                 picture='https://avatars2.githubusercontent.com/u/9111802')
    session.add(User1)
    session.commit()
    for idx, category in enumerate(categories):
        myCategory = Category(user_id=1, name=category,
                              summary=categorySum[idx])
        session.add(myCategory)
        session.commit()
        for item in anime[category]:
            myItem = CatalogItem(
                user_id=1,
                name=item['name'],
                summary=item['summary'],
                category=myCategory)
            session.add(myItem)
            session.commit()

    print(list(map(showName, session.query(Category).all())))
    print(list(map(showName, session.query(CatalogItem).all())))

# Reference:
# https://reelrundown.com/animation/Anime-Genre-List
