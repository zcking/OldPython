from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import *
import tkinter.ttk as ttk
import pickle

newT_books = ("Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
              "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel", "1 Kings",
              "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah",
              "Esther", "Job", "Psalms", "Proverbs", "Ecclesiastes",
              "Song of Solomon", "Isaiah", "Jeremiah", "Lamentations",
              "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah",
              "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai",
              "Zechariah", "Malachi")

oldT_books = ("Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians",
              "2 Corinthians", "Galatians", "Ephesians", "Philippians",
              "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy",
              "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter",
              "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation")

all_books = newT_books + oldT_books
bookmarks = []
screen = "read"

Genesis = [50, [31,
                "In the beginning God created the heaven and the earth.",
                "And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.",
                "And God said, Let there be light: and there was light.",
                "And God saw the light, that it was good: and God divided the light from the darkness.",
                "And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.",
                "And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters",
                "And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so.",
                "And God called the firmament Heaven. And the evening and the morning were the second day.",
                "And God said, Let the waters under the heaven be gathered together unto one place, and let the dry land apear: and it was so.",
                "And God called the dry land Earth; and the gathering together of the waters called he Seas: and God saw that it was good.",
                "And God said, Let the earth bring forth grass, the herb yielding seed, and the fruit tree yielding fruit after his kind, whose seed is in itself, upon the earth: and it was so.",
                "And the earth brought forth grass, and herb yielding seed after his kind, and the tree yielding fruit, whose seed was in itself, after his kind: and God saw that it was good.",
                "And the evening and the morning were the third day.",
                "And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years:",
                "And let them be for lights in the firmament of the heaven to give light upon the earth: and it was so.",
                "And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also.",
                "And God set them in the firmament of the heaven to give light upon the earth, ",
                "And to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good.",
                "And the evening and the morning were the forth day.",
                "And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.",
                "And God created great whales, and every living creature that moveth, which the waters brought forth abundantly, after their kind, and every winged fowl after his kind: and God saw that it was good.",
                "And God blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let fowl multiply in the earth.",
                "And the evening and the morning were the fifth day.",
                "And God said, Let the earth bring forth the living creature after his kind, cattle, and creeping thing, and beast of the earth after his kind: and it was so.",
                "And God made the beast of the earth after his kind, and cattle after their kind, and every thing that creepeth upon the earth after his kind: and God saw that it was good.",
                "And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth.",
                "So God created man in his own image, in the image of God created he him; male and female created he them.",
                "And God blessed them, and God said to unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth.",
                "And God said, Behold, I have given you every herb bearing seed, which is upon the face of all the earth, and every tree, in the which is the fruit of a tree yielding seed; to you it shall be for meat.",
                "And to every beast of the earth, and to every fowl of the air, and to every thing that creepeth upon the earth, wherein there is life, I have given every green herb for meat: and it was so.",
                "And God saw every thing that he had made, and, behold, it was very good. And the evening and the morning were the sixth day."],
           [25,
            "Thus the heavens and the earth were finished, and all the host of them.",
            "And on the seventh day God ended his work which he had made; and he rested on the seventh day from all his work which he had made.",
            "And God blessed the seventh day, and sanctified it: because that in it he had rested from all his work which God created and made.",
            "These are the generations of the heavens and of the earth when they were created, in the day that the LORD God made the earth and the heavens.",
            "And every plant of the field before it was in the earth, and every herb of the field before it grew: for the LORD God had not caused it to rain upon the earth, and there was not a man to till the ground.",
            "But there went up a mist from the earth, and watered the whole face of the ground.",
            "And the LORD God formed man of the dust of the ground, and breathed into his nostrils the breath of life; and man became a living soul.",
            "And the LORD God planted a garden eastward in Eden; and there he put the man whom he had formed.",
            "And out of the ground made the LORD God to grow every tree that is pleasant to the sight, and good for food; the tree of life also in the midst of the garden, and the tree of knowledge of good and evil.",
            "And a river went out of Eden to water the garden; and from thence it was parted, and became into four heads.",
            "The name of the first is Pison: that is it which compasseth the whole land of Havilah, where there is gold;",
            "And the gold of that land is good: there is bdellium and the onyx stone.",
            "And the name of the second river is Gihon: the same is it that compasseth the whole land of Ethiopia.",
            "And the name of the third river is Hiddekel: that is it which goeth toward the east of Assyria. And the fourth river is Euphrates.",
            "And the LORD God took the man, and put him into the garden of Eden to dress it and to keep it.",
            "And the LORD God commanded the man, saying, Of every tree of the garden thou mayest freely eat:",
            "But of the tree of the knowledge of good and evil, thou shalt not eat of it: for in the day that thou eatest thereof thou shalt surely die.",
            "And the LORD God said, It is not good that the man should be alone; I will make for him a helper suitable.",
            "And out of the ground the LORD God formed every beast of the field, and every fowl of the air; and brought them unto Adam to see what he would call them: and whatsoever Adam called every living creature, that was the name thereof.",
            "And Adam gave names to all cattle, and to the fowl of the air, and to every beast of the field; but for Adam there was not found an help meet for him.",
            "And the LORD God caused a deep sleep to fall upon Adam, and he slept: and he took one of his ribs, and closed up the flesh instead thereof;",
            "And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.",
            "And Adam said, This is now bone of my bones, and flesh of my flesh: she shall be called Woman, because she was taken out of Man.",
            "Therefore shall a man leave his father and his mother, and shall cleave unto his wife: and they shall be one flesh.",
            "And they were both naked, the man and his wife, and were not ashamed."],
           [24,
            "Now the serpent was more subtil than any beast of the field which the LORD God had made. And he said unto the woman, Yea, hath God said, Ye shall not eat of every tree of the garden?",
            "And the woman said unto the serpent, We may eat of the fruit of the trees of the garden:",
            "But of the fruit of the tree which is in the midst of the garden, God hath said, Ye shall not eat of it, neither shall ye touch it, lest ye die.",
            "And the serpent said unto the woman, Ye shall not surely die.",
            "For God doth know that in the day ye eat thereof, then your eyes shall be opened, and ye shall be as gods, knowing good and evil.",
            "And when the woman saw that the tree was good for food, and that it was pleasant to the eyes, and a tree to be desired to make one wise, she took of the fruit thereof, and did eat, and gave also unto her husband with her; and he did eat.",
            "And the eyes of them both were opened, and they knew that they were naked; and they sewed fig leaves together, and made themselves aprons.",
            "And they heard the voice of the LORD God walking in the garden in the cool of the day: and Adam and his wife hid themselves from the presence of the LORD God amongst the trees of the garden.",
            "And the LORD God called unto Adam, and said unto him, Where art thou?",
            "And he said, I heard thy voice in the garden, and I was afraid, because I was naked; and I hid myself.",
            "And he said, Who told thee that thou wast naked? Hast thou eaten of the tree, whereof I commanded thee that thou shouldest not eat?",
            "And the man said, The woman whom thou gavest to be with me, she gave me of the tree, and I did eat.",
            "And the LORD God said unto the woman, What is this that thou hast done? And the woman said, The serpent beguiled me, and I did eat.",
            "And the LORD God said unto the serpent, Because thou hast done this, thou art cursed above all cattle, and above every beast of the field; upon thy belly shalt thou go, and dust shalt thou eat all the days of thy life:",
            "And I will put enmity between thee and the woman, and between thy seed and her seed; it shall bruise thy head, and thou shalt bruise his heel.",
            "Unto the woman he said, I will greatly multiply thy sorrow and thy conception; in sorrow thou shalt bring forth children; and thy desire shall be to thy husband, and he shall rule over thee.",
            "And unto Adam he said, Because thou hast hearkened unto the voice of thy wife, and hast eaten of the tree, of which I commanded thee, saying, Thou shalt not eat of it: cursed is the ground for thy sake; in sorrow shalt thou eat of it all the days of thy life;",
            "Thorns also and thistles shall it bring forth to thee; and thou shalt eat the herb of the field;",
            "In the sweat of thy face shalt thou eat bread, till thou return unto the ground; for out of it wast thou taken: for dust thou art, and unto dust shalt thou return.",
            "And Adam called his wifes name Eve; because she was the mother of all living.",
            "Unto Adam also and to his wife did the LORD God make coats of skins, and clothed them.",
            "And the LORD God said, Behold, the man is become as one of us, to know good and evil: and now, lest he put forth his hand, and take also of the tree of life, and eat, and live for ever:",
            "Therefore the LORD God sent him forth from the garden of Eden, to till the ground from whence he was taken.",
            "So he drove out the man; and he placed at the east of the garden of Eden Cherubims, and a flaming sword which turned every way, to keep the way of the tree of life.",],
           [26,
            "And Adam knew Eve his wife; and she conceived, and bare Cain, and said, I have gotten a man from the LORD.",
            "And she again bare his brother Abel. And Abel was a keeper of sheep, but Cain was a tiller of the ground.",
            "And in process of time it came to pass, that Cain brought of the fruit of the ground an offering unto the LORD.",
            "And Abel, he also brought of the firstlings of his flock and of the fat thereof. And the LORD had respect unto Abel and to his offering:",
            "But unto Cain and to his offering he had not respect. And Cain was very wroth, and his countenance fell.",
            "And the LORD said unto Cain, Why art thou wroth? And why is thy countenance fallen?",
            "If thou doest well, shalt thou not be accepted? And if thou doest not well, sin lieth at the door. And unto thee shall be his desire, and thou shalt rule over him.",
            "And Cain talked with Abel his brother: and it came to pass, when they were in the field, that Cain rose up against Abel his brother, and slew him.",
            "And the LORD said unto Cain, Where is Abel thy brother? And he said, I know not: Am I my brothers keeper?",
            "And he said, What hast thou done? The voice of thy brothers blood crieth unto me from the ground.",
            "And now art thou cursed from the earth, which hath opened her mouth to receive thy brothers blood from thy hand;",
            "When thou tillest the ground, it shall not henceforth yield unto thee her strength; a fugitive and a vagabond shalt thou be in the earth.",
            "And Cain said unto the LORD, My punishment is greater than I can bear.",
            "Behold, thou hast driven me out this day from the face of the earth; and from thy face shall I be hid; and I shall be a fugitive and a vagabond in the earth; and it shall come to pass, that every on ethat findeth me shall slay me.",
            "And the LORD said unto him, Therefore whosoever slayeth Cain, vengeance shall be taken on him sevenfold. And the LORD set a mark upon Cain, lest any finding him should kill him.",
            "And Cain went out from the presence of the LORD, and dwelt in the land of Nod, on the east of Eden.",
            "And Cain knew his wife; and she conceived, and bare Enoch: and he builded a city, and called the name of the city, after the name of his son, Enoch.",
            "And unto Enoch was born Irad: and Irad begat Mehujael: and Mehujael begat Methusael: and Methusael begat Lamech.",
            "And Lamech took unto him two wives: the name of the one was Adah , and the name of the other Zillah.",
            "And Adah bare Jabal: he was the father of such as dwell in tents, and of such as have cattle.",
            "And his brothers name was Jubal: he was the father of all such as handle the harp and organ.",
            "And Zillah, she also bare Tubalcain, an instructer of every artificer in brass and iron: and the sister of Tubalcain was Naamah.",
            "And Lamech said unto his wives, Adah and Zillah, Hear my voice: ye wives of Lamech, hearken unto my speech: for I have slain a man to my wounding, and a young man to my hurt.",
            "If Cain shall be avenged sevenfold, truly Lamech seventy and sevenfold.",
            "And Adam knew his wife again; and she bare a son, and called his name Seth: For God, said she, hath appointed me another seed instead of Abel, whom Cain slew.",
            "And to Seth, to him also there was born a son; and he called his name Enos: then began men to call upon the name of the LORD."],
           [32,
            "This [is] the book of the generations of Adam. In the day that God created man, in the likeness of God made he him;",
            "Male and female created he them; and blessed them, and called their name Adam, in the day when they were created.",
            "And Adam lived an hundred and thirty years, and begat [a son] in his own likeness, after his image; and called his name Seth:",
            "And the days of Adam after he had begotten Seth were eight hundred years: and he begat sons and daughters:",
            "And all the days that Adam lived were nine hundred and thirty years: and he died.",
            "And Seth lived an hundred and five years, and begat Enos:",
            "And Seth lived after he begat Enos eight hundred and seven years, and begat sons and daughters:",
            "And all the days of Seth were nine hundred and twelve years: and he died.",
            "And Enos lived ninety years, and begat Cainan:",
            "And Enos lived after he begat Cainan eight hundred and fifteen years, and begat sons and daughters:",
            "And all the days of Enos were nine hundred and five years: and he died.",
            "And Cainan lived seventy years, and begat Mahalaleel:",
            "And Cainan lived after he begat Mahalaleel eight hundred and forty years, and begat sons and daughters:",
            "And all the days of Cainan were nine hundred and ten years: and he died.",
            "And Mahalaleel lived sixty and five years, and begat Jared:",
            "And Mahalaleel lived after he begat Jared eight hundred and thirty years, and begat sons and daughters:",
            "And all the days of Mahalaleel were eight hundred ninety and five years: and he died.",
            "And Jared lived an hundred sixty and two years, and he begat Enoch:",
            "And Jared lived after he begat Enoch eight hundred years, and begat sons and daughters:",
            "And all the days of Jared were nine hundred sixty and two years: and he died.",
            "And Enoch lived sixty and five years, and begat Methuselah:",
            "And Enoch walked with God after he begat Methuselah three hundred years, and begat sons and daughters:",
            "And all the days of Enoch were three hundred sixty and five years:",
            "And Enoch walked with God: and he [was] not; for God took him.",
            "And Methuselah lived an hundred eighty and seven years, and begat Lamech:",
            "And Methuselah lived after he begat Lamech seven hundred eighty and two years, and begat sons and daughters:",
            "And all the days of Methuselah were nine hundred sixty and nine years: and he died.",
            "And Lamech lived an hundred eighty and two years, and begat a son:",
            "And he called his name Noah, saying, This [same] shall comfort us concerning our work and toil of our hands, because of the ground which the LORD hath cursed.",
            "And Lamech lived after he begat Noah five hundred ninety and five years, and begat sons and daughters:",
            "And all the days of Lamech were seven hundred seventy and seven years: and he died.",
            "And Noah was five hundred years old: and Noah begat Shem, Ham, and Japheth."],
           [22,
            "And it came to pass, when men began to multiply on the face of the earth, and daughters were born unto them,",
            "That the sons of God saw the daughters of men that they [were] fair; and they took them wives of all which they chose.",
            "And the LORD said, My spirit shall not always strive with man, for that he also [is] flesh: yet his days shall be an hundred and twenty years.",
            "There were giants in the earth in those days; and also after that, when the sons of God came in unto the daughters of men, and they bare [children] to them, the same [became] mighty men which [were] of old, men of renown.",
            "And GOD saw that the wickedness of man [was] great in the earth, and [that] every imagination of the thoughts of his heart [was] only evil continually.",
            "And it repented the LORD that he had made man on the earth, and it grieved him at his heart.",
            "And the LORD said, I will destroy man whom I have created from the face of the earth; both man, and beast, and the creeping thing, and the fowls of the air; for it repenteth me that I have made them.",
            "But Noah found grace in the eyes of the LORD.",
            "These [are] the generations of Noah: Noah was a just man [and] perfect in his generations, [and] Noah walked with God.",
            "And Noah begat three sons, Shem, Ham, and Japheth.",
            "The earth also was corrupt before God, and the earth was filled with violence.",
            "And God looked upon the earth, and, behold, it was corrupt; for all flesh had corrupted his way upon the earth.",
            "And God said unto Noah, The end of all flesh is come before me; for the earth is filled with violence through them; and, behold, I will destroy them with the earth.",
            "Make thee an ark of gopher wood; rooms shalt thou make in the ark, and shalt pitch it within and without with pitch.",
            "And this [is the fashion] which thou shalt make it [of]: The length of the ark [shall be] three hundred cubits, the breadth of it fifty cubits, and the height of it thirty cubits.",
            "A window shalt thou make to the ark, and in a cubit shalt thou finish it above; and the door of the ark shalt thou set in the side thereof; [with] lower, second, and third [stories] shalt thou make it.",
            "And, behold, I, even I, do bring a flood of waters upon the earth, to destroy all flesh, wherein [is] the breath of life, from under heaven; [and] every thing that [is] in the earth shall die.",
            "But with thee will I establish my covenant; and thou shalt come into the ark, thou, and thy sons, and thy wife, and thy sons' wives with thee.",
            "And of every living thing of all flesh, two of every [sort] shalt thou bring into the ark, to keep [them] alive with thee; they shall be male and female.",
            "Of fowls after their kind, and of cattle after their kind, of every creeping thing of the earth after his kind, two of every [sort] shall come unto thee, to keep [them] alive.",
            "And take thou unto thee of all food that is eaten, and thou shalt gather [it] to thee; and it shall be for food for thee, and for them.",
            "Thus did Noah; according to all that God commanded him, so did he."],
           [24,
            "And the LORD said unto Noah, Come thou and all thy house into the ark; for thee have I seen righteous before me in this generation.",
            "Of every clean beast thou shalt take to thee by sevens, the male and his female: and of beasts that [are] not clean by two, the male and his female.",
            "Of fowls also of the air by sevens, the male and the female; to keep seed alive upon the face of all the earth.",
            "For yet seven days, and I will cause it to rain upon the earth forty days and forty nights; and every living substance that I have made will I destroy from off the face of the earth.",
            "And Noah did according unto all that the LORD commanded him.",
            "And Noah [was] six hundred years old when the flood of waters was upon the earth.",
            "And Noah went in, and his sons, and his wife, and his sons' wives with him, into the ark, because of the waters of the flood.",
            "Of clean beasts, and of beasts that [are] not clean, and of fowls, and of every thing that creepeth upon the earth,",
            "There went in two and two unto Noah into the ark, the male and the female, as God had commanded Noah.",
            "And it came to pass after seven days, that the waters of the flood were upon the earth.",
            "In the six hundredth year of Noah's life, in the second month, the seventeenth day of the month, the same day were all the fountains of the great deep broken up, and the windows of heaven were opened.",
            "And the rain was upon the earth forty days and forty nights.",
            "In the selfsame day entered Noah, and Shem, and Ham, and Japheth, the sons of Noah, and Noah's wife, and the three wives of his sons with them, into the ark;",
            "They, and every beast after his kind, and all the cattle after their kind, and every creeping thing that creepeth upon the earth after his kind, and every fowl after his kind, every bird of every sort.",
            "And they went in unto Noah into the ark, two and two of all flesh, wherein [is] the breath of life",
            "And they that went in, went in male and female of all flesh, as God had commanded him: and the LORD shut him in.",
            "And the flood was forty days upon the earth; and the waters increased, and bare up the ark, and it was lift up above the earth.",
            "And the waters prevailed, and were increased greatly upon the earth; and the ark went upon the face of the waters.",
            "And the waters prevailed exceedingly upon the earth; and all the high hills, that [were] under the whole heaven, were covered.",
            "Fifteen cubits upward did the waters prevail; and the mountains were covered.",
            "And all flesh died that moved upon the earth, both of fowl, and of cattle, and of beast, and of every creeping thing that creepeth upon the earth, and every man:",
            "All in whose nostrils [was] the breath of life, of all that [was] in the dry [land], died.",
            "And every living substance was destroyed which was upon the face of the ground, both man, and cattle, and the creeping things, and the fowl of the heaven; and they were destroyed from the earth: and Noah only remained [alive], and they that [were] with him in the ark.",
            "And the waters prevailed upon the earth an hundred and fifty days."],
           [22,
            "And God remembered Noah, and every living thing, and all the cattle that [was] with him in the ark: and God made a wind to pass over the earth, and the waters asswaged;",
            "The fountains also of the deep and the windows of heaven were stopped, and the rain from heaven was restrained;",
            "And the waters returned from off the earth continually: and after the end of the hundred and fifty days the waters were abated.",
            "And the ark rested in the seventh month, on the seventeenth day of the month, upon the mountains of Ararat.",
            "And the waters decreased continually until the tenth month: in the tenth [month], on the first [day] of the month, were the tops of the mountains seen.",
            "And it came to pass at the end of forty days, that Noah opened the window of the ark which he had made:",
            "And he sent forth a raven, which went forth to and fro, until the waters were dried up from off the earth.",
            "Also he sent forth a dove from him, to see if the waters were abated from off the face of the ground;",
            "But the dove found no rest for the sole of her foot, and she returned unto him into the ark, for the waters [were] on the face of the whole earth: then he put forth his hand, and took her, and pulled her in unto him into the ark.",
            "And he stayed yet other seven days; and again he sent forth the dove out of the ark;",
            "And the dove came in to him in the evening; and, lo, in her mouth [was] an olive leaf pluckt off: so Noah knew that the waters were abated from off the earth.",
            "And he stayed yet other seven days; and sent forth the dove; which returned not again unto him any more.",
            "And it came to pass in the six hundredth and first year, in the first [month], the first [day] of the month, the waters were dried up from off the earth: and Noah removed the covering of the ark, and looked, and, behold, the face of the ground was dry.",
            "And in the second month, on the seven and twentieth day of the month, was the earth dried.",
            "And God spake unto Noah, saying,",
            "Go forth of the ark, thou, and thy wife, and thy sons, and thy sons' wives with thee.",
            "Bring forth with thee every living thing that [is] with thee, of all flesh, [both] of fowl, and of cattle, and of every creeping thing that creepeth upon the earth; that they may breed abundantly in the earth, and be fruitful, and multiply upon the earth.",
            "And Noah went forth, and his sons, and his wife, and his sons' wives with him:",
            "Every beast, every creeping thing, and every fowl, [and] whatsoever creepeth upon the earth, after their kinds, went forth out of the ark.",
            "And Noah builded an altar unto the LORD; and took of every clean beast, and of every clean fowl, and offered burnt offerings on the altar.",
            "And the LORD smelled a sweet savour; and the LORD said in his heart, I will not again curse the ground any more for man's sake; for the imagination of man's heart [is] evil from his youth; neither will I again smite any more every thing living, as I have done.",
            "While the earth remaineth, seedtime and harvest, and cold and heat, and summer and winter, and day and night shall not cease."],
           [29,
            "And God blessed Noah and his sons, and said unto them, Be fruitful, and multiply, and replenish the earth.",
            "And the fear of you and the dread of you shall be upon every beast of the earth, and upon every fowl of the air, upon all that moveth [upon] the earth, and upon all the fishes of the sea; into your hand are they delivered.",
            "Every moving thing that liveth shall be meat for you; even as the green herb have I given you all things.",
            "But flesh with the life thereof, [which is] the blood thereof, shall ye not eat.",
            "And surely your blood of your lives will I require; at the hand of every beast will I require it, and at the hand of man; at the hand of every man's brother will I require the life of man.",
            "Whoso sheddeth man's blood, by man shall his blood be shed: for in the image of God made he man.",
            "And you, be ye fruitful, and multiply; bring forth abundantly in the earth, and multiply therein.",
            "And God spake unto Noah, and to his sons with him, saying,",
            "And I, behold, I establish my covenant with you, and with your seed after you;",
            "And with every living creature that [is] with you, of the fowl, of the cattle, and of every beast of the earth with you; from all that go out of the ark, to every beast of the earth.",
            "And I will establish my covenant with you; neither shall all flesh be cut off any more by the waters of a flood; neither shall there any more be a flood to destroy the earth.",
            "And God said, This [is] the token of the covenant which I make between me and you and every living creature that [is] with you, for perpetual generations:",
            "I do set my bow in the cloud, and it shall be for a token of a covenant between me and the earth.",
            "And it shall come to pass, when I bring a cloud over the earth, that the bow shall be seen in the cloud:",
            "And I will remember my covenant, which [is] between me and you and every living creature of all flesh; and the waters shall no more become a flood to destroy all flesh.",
            "And the bow shall be in the cloud; and I will look upon it, that I may remember the everlasting covenant between God and every living creature of all flesh that [is] upon the earth.",
            "And God said unto Noah, This [is] the token of the covenant, which I have established between me and all flesh that [is] upon the earth.",
            "And the sons of Noah, that went forth of the ark, were Shem, and Ham, and Japheth: and Ham [is] the father of Canaan.",
            "These [are] the three sons of Noah: and of them was the whole earth overspread.",
            "And Noah began [to be] an husbandman, and he planted a vineyard:",
            "And he drank of the wine, and was drunken; and he was uncovered within his tent.",
            "And Ham, the father of Canaan, saw the nakedness of his father, and told his two brethren without.",
            "And Shem and Japheth took a garment, and laid [it] upon both their shoulders, and went backward, and covered the nakedness of their father; and their faces [were] backward, and they saw not their father's nakedness.",
            "And Noah awoke from his wine, and knew what his younger son had done unto him.",
            "And he said, Cursed [be] Canaan; a servant of servants shall he be unto his brethren.",
            "And he said, Blessed [be] the LORD God of Shem; and Canaan shall be his servant.",
            "God shall enlarge Japheth, and he shall dwell in the tents of Shem; and Canaan shall be his servant.",
            "And Noah lived after the flood three hundred and fifty years.",
            "And all the days of Noah were nine hundred and fifty years: and he died."],
           [32,
            "Now these [are] the generations of the sons of Noah, Shem, Ham, and Japheth: and unto them were sons born after the flood.",
            "The sons of Japheth; Gomer, and Magog, and Madai, and Javan, and Tubal, and Meshech, and Tiras.",
            "And the sons of Gomer; Ashkenaz, and Riphath, and Togarmah.",
            "And the sons of Javan; Elishah, and Tarshish, Kittim, and Dodanim.",
            "By these were the isles of the Gentiles divided in their lands; every one after his tongue, after their families, in their nations.",
            "And the sons of Ham; Cush, and Mizraim, and Phut, and Canaan.",
            "And the sons of Cush; Seba, and Havilah, and Sabtah, and Raamah, and Sabtecha: and the sons of Raamah; Sheba, and Dedan.",
            "And Cush begat Nimrod: he began to be a mighty one in the earth.",
            "He was a mighty hunter before the LORD: wherefore it is said, Even as Nimrod the mighty hunter before the LORD.",
            "And the beginning of his kingdom was Babel, and Erech, and Accad, and Calneh, in the land of Shinar.",
            "Out of that land went forth Asshur, and builded Nineveh, and the city Rehoboth, and Calah,",
            "And Resen between Nineveh and Calah: the same [is] a great city.",
            "And Mizraim begat Ludim, and Anamim, and Lehabim, and Naphtuhim,",
            "And Pathrusim, and Casluhim, (out of whom came Philistim,) and Caphtorim.",
            "And Canaan begat Sidon his firstborn, and Heth,",
            "And the Jebusite, and the Amorite, and the Girgasite,",
            "And the Hivite, and the Arkite, and the Sinite,",
            "And the Arvadite, and the Zemarite, and the Hamathite: and afterward were the families of the Canaanites spread abroad.",
            "And the border of the Canaanites was from Sidon, as thou comest to Gerar, unto Gaza; as thou goest, unto Sodom, and Gomorrah, and Admah, and Zeboim, even unto Lasha.",
            "These [are] the sons of Ham, after their families, after their tongues, in their countries, [and] in their nations.",
            "Unto Shem also, the father of all the children of Eber, the brother of Japheth the elder, even to him were [children] born.",
            "The children of Shem; Elam, and Asshur, and Arphaxad, and Lud, and Aram.",
            "And the children of Aram; Uz, and Hul, and Gether, and Mash.",
            "And Arphaxad begat Salah; and Salah begat Eber.",
            "And unto Eber were born two sons: the name of one [was] Peleg; for in his days was the earth divided; and his brother's name [was] Joktan.",
            "And Joktan begat Almodad, and Sheleph, and Hazarmaveth, and Jerah,",
            "And Hadoram, and Uzal, and Diklah,",
            "And Obal, and Abimael, and Sheba,",
            "And Ophir, and Havilah, and Jobab: all these [were] the sons of Joktan.",
            "And their dwelling was from Mesha, as thou goest unto Sephar a mount of the east.",
            "These [are] the sons of Shem, after their families, after their tongues, in their lands, after their nations.",
            "These [are] the families of the sons of Noah, after their generations, in their nations: and by these were the nations divided in the earth after the flood."],
           [32,
            "And the whole earth was of one language, and of one speech.",
            "And it came to pass, as they journeyed from the east, that they found a plain in the land of Shinar; and they dwelt there.",
            "And they said one to another, Go to, let us make brick, and burn them throughly. And they had brick for stone, and slime had they for morter.",
            "And they said, Go to, let us build us a city and a tower, whose top [may reach] unto heaven; and let us make us a name, lest we be scattered abroad upon the face of the whole earth.",
            "And the LORD came down to see the city and the tower, which the children of men builded.",
            "And the LORD said, Behold, the people [is] one, and they have all one language; and this they begin to do: and now nothing will be restrained from them, which they have imagined to do.",
            "Go to, let us go down, and there confound their language, that they may not understand one another's speech.",
            "So the LORD scattered them abroad from thence upon the face of all the earth: and they left off to build the city.",
            "Therefore is the name of it called Babel; because the LORD did there confound the language of all the earth: and from thence did the LORD scatter them abroad upon the face of all the earth.",
            "These [are] the generations of Shem: Shem [was] an hundred years old, and begat Arphaxad two years after the flood:",
            "And Shem lived after he begat Arphaxad five hundred years, and begat sons and daughters.",
            "And Arphaxad lived five and thirty years, and begat Salah:",
            "And Arphaxad lived after he begat Salah four hundred and three years, and begat sons and daughters.",
            "And Salah lived thirty years, and begat Eber:",
            "And Salah lived after he begat Eber four hundred and three years, and begat sons and daughters.",
            "And Eber lived four and thirty years, and begat Peleg:",
            "And Eber lived after he begat Peleg four hundred and thirty years, and begat sons and daughters.",
            "And Peleg lived thirty years, and begat Reu:",
            "And Peleg lived after he begat Reu two hundred and nine years, and begat sons and daughters.",
            "And Reu lived two and thirty years, and begat Serug:",
            "And Reu lived after he begat Serug two hundred and seven years, and begat sons and daughters.",
            "And Serug lived thirty years, and begat Nahor:",
            "And Serug lived after he begat Nahor two hundred years, and begat sons and daughters.",
            "And Nahor lived nine and twenty years, and begat Terah:",
            "And Nahor lived after he begat Terah an hundred and nineteen years, and begat sons and daughters.",
            "And Terah lived seventy years, and begat Abram, Nahor, and Haran.",
            "Now these [are] the generations of Terah: Terah begat Abram, Nahor, and Haran; and Haran begat Lot.",
            "And Haran died before his father Terah in the land of his nativity, in Ur of the Chaldees.",
            "And Abram and Nahor took them wives: the name of Abram's wife [was] Sarai; and the name of Nahor's wife, Milcah, the daughter of Haran, the father of Milcah, and the father of Iscah.",
            "But Sarai was barren; she [had] no child.",
            "And Terah took Abram his son, and Lot the son of Haran his son's son, and Sarai his daughter in law, his son Abram's wife; and they went forth with them from Ur of the Chaldees, to go into the land of Canaan; and they came unto Haran, and dwelt there.",
            "And the days of Terah were two hundred and five years: and Terah died in Haran."],
           [20],
           [18],
           [24],
           [21],
           [16],
           [27],
           [33],
           [38],
           [18],
           [34],
           [24],
           [20],
           [67],
           [34],
           [35],
           [46],
           [22],
           [35],
           [43],
           [55],
           [32],
           [20],
           [31],
           [29],
           [43],
           [36],
           [30],
           [23],
           [23],
           [57],
           [38],
           [34],
           [34],
           [28],
           [34],
           [31],
           [22],
           [33],
           [26]]
Exodus = [40]
Leviticus = [27]
Numbers = [36]
Deuteronomy = [34]
Joshua = [24]
Judges = [21]
Ruth = [4]
fSamuel = [31]
sSamuel = [24]
fKings = [22]
sKings = [25]
fChronicles = [29]
sChronicles = [36]
Ezra = [10]
Nehemiah = [13]
Esther = [10]
Job = [42]
Psalms = [150]
Proverbs = [31]
Ecclesiastes = [12]
Song_of_Solomon = [8]
Isaiah = [66]
Jeremiah = [52]
Lamentations = [5]
Ezekiel = [48]
Daniel = [12]
Hosea = [14]
Joel = [3]
Amos = [9]
Obadiah = [1, [21,
               "The vision of Obadiah. Thus saith the LORD God concerning Edom; We have heard a rumor from the LORD, and an ambassador is sent among the heathen, Arise ye, and let us rise up against her in battle.",
               "Behold, I have made thee small among the heathen: thou art greatly despised.",
               "The pride of thine heart hath deceived thee, thou that dwellest in the clefts of the rock, whose habitation is high; that saith in his heart, Who shall bring me down to the ground?",
               "Though thou exalt thyself as the eagle, and though thou set thy nest among the stars, thence will I bring thee down, saith the LORD.",
               "If thieves came to thee, if robbers by night, (how art thou cut off!) would they not have stolen till they had enough? If the grapegatherers came to thee, would they not leave some grapes?",
               "How are the things of Esau searched out! How are his hidden things sought up!",
               "All the men of thy confederacy have brought thee even to the border: the men that were at peace with thee have deceived thee, and prevailed against thee; they that eat thy bread have laid a wound under thee: there is none understanding in him.",
               "Shall I not in that day, saith the LORD, even destroy the wise men out of Edom, and understanding out of the mount of Esau?",
               "And thy mighty men, O Teman, shall be dismayed, to the end that every one of the mount of Esau may be cut off by slaughter.",
               "For thy violence against thy brother Jacob shame shall cover thee, and thou shalt be cut off forever.",
               "In the day that thou stoodest on the other side, in the day that the strangers carried away captive his forces, and foreigners entered into his gates, and cast lots upon Jerusalem, even thou wast as one of them.",
               "But thou shouldest not have looked on the day of thy brother in the day that he became a stranger; neither shouldest thou have rejoiced over the children of Judah in the day of their destruction; neither shouldest thou have spoken proudly in the day of distress.",
               "Thou shouldest not have entered into the gate of my people in the day of their calamity; yea, thou shouldest not have looked on their affliction in the day of their calamity, nor have laid hands on their substance in the day of their calamity;",
               "Neither shouldest thou have stood in the crossway, to cut off those of his that did escape; neither shouldest thou have delivered up those of his that did remain in the day of distress.",
               "For the day of the LORD is near upon all the heathen: as thou hast done, it shall be done unto thee: thy reward shall return upon thine own head.",
               "For as ye have drunk upon my holy mountain, so shall all the heathen drink continually, yea, they shall drink, and they shall be as though they had not been.",
               "But upon mount Zion shall be deliverance, and there shall be holiness; and the house of Jacob shall possess their possessions.",
               "And the house of Jacob shall be a fire, and the house of Joseph a flame, and the house of Esau for stubble, and they shall kindle in them, and devour them; and there shall not be any remaining of the house of Esau; for the LORD hath spoken it.",
               "And they of the south shall possess the mount of Esau; and they of the plain the Philistines: and they shall possess the fields of Ephraim, and the fields of Samaria: and Benjamin shall possess Gilead.",
               "And the captivity of this host of the children of Israel shall possess that of the Canaanites, even unto Zarephath; and the captivity of Jerusalem, which is in Sepharad, shall possess the cities of the south.",
               "And saviors shall come up on mount Zion to judge the mount of Esau; and the kingdom shall be the LORDs."]]
Jonah = [4]
Micah = [7]
Nahum = [3]
Habakkuk = [3]
Zephaniah = [3]
Haggai = [2]
Zechariah = [14]
Malachi = [4]
Matthew = [28]
Mark = [16]
Luke = [24]
John = [21]
Acts = [28]
Romans = [16]
fCorinthians = [16]
sCorinthians = [13]
Galatians = [6]
Ephesians = [6]
Philippians = [4, [30,
                   "Paul and Timothy, the servants of Jesus Christ, To all the saints in Christ Jesus which are at Philippi, with the bishops and deacons:",
                   "Grace be unto you, and peace, from God our Father, and from the Lord Jesus Christ.",
                   "I thank my God upon every remembrance of you,",
                   "Always in every prayer of mine for you all making request with joy,",
                   "For your fellowship in the gospel from the first day until now;",
                   "Being confident of this very thing, that he which hath begun a good work in you will perform it until the day of Jesus Christ:",
                   "Even as it is meet for me to think this of you all, because I have you in my heart; inasmuch as both in my bonds, and in the defense and confirmation of the gospel, ye all are partakers of my grace.",
                   "For God is my record, how greatly I long after you all in the bowels of Jesus Christ.",
                   "And this I pray, that your love may abound yet more and more in knowledge and in all judgment;",
                   "That ye may approve things that are excellent; that ye may be sincere and without offence till the day of Christ;",
                   "Being filled with the fruits of righteousness, which are by Jesus Christ, unto the glory and praise of God.",
                   "But I would ye should understand, brethren, that the things which happened unto me have fallen out rather unto the furtherance of the gospel;",
                   "So that my bonds in Christ are manifest in all the palace, and in all other places;",
                   "And many of the brethren in the Lord, waxing confident by my bonds, are much more bold to speak the word without fear.",
                   "Some indeed preach Christ even of envy and strife; and some also of good will.",
                   "The one preach Christ of contention, not sincerely, supposing to add affliction to my bonds:",
                   "But the other of love, knowing that I am set for the defense of the gospel.",
                   "What then? Notwithstanding, every way, whether in pretense, or in truth, Christ is preached; and I therein do rejoice, yea, and will rejoice.",
                   "For I know that this shall turn to my salvation through your prayer, and the supply of the Spirit of Jesus Christ,",
                   "According to my earnest expectation and my hope, that in nothing I shall be ashamed, but that with all boldness, as always, so now also Christ shall be magnified in my body, whether it be by life, or by death.",
                   "For to me to live is Christ, and to die is gain.",
                   "But if I live in the flesh, this is the fruit of my labor: yet what I shall choose I will not.",
                   "For I am in a strait betwixt two, having a desire to depart, and to be with Christ; which is far better:",
                   "Nevertheless to abide in the flesh is more needful for you.",
                   "And having this confidence, I know that I shall abide and continue with you all for your furtherance and joy of faith;",
                   "That your rejoicing may be more abundant in Jesus Christ for me by coming to you again.",
                   "Only let your conversation be as it becometh the gospel of Christ: that whether I come and see you, or else be absent, I may hear of your affairs, that ye stand fast in one spirit, with one mind striving together for the faith of the gospel;",
                   "And in nothing terrified by your adversaries: which is to them an evident token of perdition, but to you of salvation, and that of God.",
                   "For unto you it is given in the behalf of Christ, not only to believe on him, but also to suffer for his sake;",
                   "Having the same conflict which ye saw in me, and now hear to be in me."],
               [30,
                "If there be therefore any consolation in Christ, if any comfort of love, if any fellowship of the Spirit, if any bowels and mercies,",
                "Fulfill ye my joy, that ye be likeminded, having the same love, being of one accord, of one mind.",
                "Let nothing be done through strife or vainglory; but in lowliness of mind let each esteem other better than themselves.",
                "Look not every man on his own things, but every man also on the things of others.",
                "Let this mind be in you, which was also in Christ Jesus:",
                "Who, being in the form of God, thought it not robbery to be equal with God:",
                "But made himself of no reputation, and took upon him the form of a servant, and was made in the likeness of men:",
                "And being found in fashion as a man, he humbled himself, and became obedient unto death, even the death of the cross.",
                "Wherefore God also hath highly exalted him, and given him a name which is above every name:",
                "That at the name of Jesus every knee should bow, of things in heaven, and things in earth, and things under the earth;",
                "And that every tongue should confess that Jesus Christ is Lord, to the glory of God the Father.",
                "Wherefore, my beloved, as ye have always obeyed, not as in my presence only but now much more in my absence, work out your own salvation with fear and trembling.",
                "For it is God which worketh in you both to will and to do of his good pleasure.",
                "Do all things without murmurings and disputings:",
                "That ye may be blameless and harmless, the sons of God, without rebuke, in the midst of a crooked and perverse nation, among whom ye shine as lights in the world;",
                "Holding forth the word of life; that I may rejoice in the day of Christ, that I have not run in vain, neither labored in vain.",
                "Yea, and if I be offered upon the sacrifice and service of your faith, I joy, and rejoice with you all.",
                "For the same cause also do ye joy, and rejoice with me.",
                "But I trust in the Lord Jesus to send Timothy shortly unto you, that I may be of good comfort, when I know your state.",
                "For I have no man likeminded, who will naturally care for your state.",
                "For all seek their own, not the things which are Jesus Christs.",
                "But ye know the proof of him, that, as a son with the father, he hath served with me in the gospel.",
                "Him therefore I hope to send presently, so soon as I shall see how it will go with me.",
                "But I trust in the Lord that I also myself shall come shortly.",
                "Yet I supposed it necessary to send to you Epaphroditus, my brother, and companion in labor, and fellow soldier, but your messenger, and he that ministered to my wants.",
                "For he longed after you all, and was full of heaviness, because that ye had heard that he been sick.",
                "For indeed he was sick nigh unto death: but God had mercy on him; and not on him only, but on me also, lest I should have sorrow upon sorrow.",
                "I sent him therefore the more carefully, that, when ye see him again, ye may rejoice, and that I may be the less sorrowful.",
                "Receive him therefore in the Lord with all gladness; and hold such in reputation:",
                "Because for the work of Christ he was nigh unto death, not regarding his life, to supply your lack of service toward me."],
               [21,
                "Finally, my brethren, rejoice in the Lord. To write the same things to you, to me indeed is not grievous, but for you it is safe.",
                "Beware of dogs, beware of evil workers, beware of the concision.",
                "For we are the circumcision, which worship God in the spirit, and rejoice in Christ Jesus, and have no confidence in the flesh.",
                "Though I might also have confidence in the flesh. If any other man thinketh that he hath whereof he might trust in the flesh, I more:",
                "Circumcised the eighth day, of the stock of Israel, of the tribe of Benjamin, and Hebrew of the Hebrews; as touching as the law, a Pharisee;",
                "Concerning zeal, persecuting the church; touching the righteousness which is in the law, blameless.",
                "But what things were gain to me, those I counted loss for Christ.",
                "Yea doubtless, and I count all things but loss for the excellency of the knowledge of Christ Jesus my Lord: for whom I have suffered the loss of all things, and do count them but dung, that I may win Christ,",
                "And be found in him, not having mine own righteousness, which is of the law, but that which is through the faith of Christ, the righteousness which is of God by faith:",
                "That I may know him, and the power of his resurrection, and the fellowship of his sufferings, being made conformable unto his death;",
                "If by any means I might attain unto the resurrection of the dead.",
                "Not as though I had already attained, either were already perfect: but I follow after, if that I may apprehend that for which also I am apprehended of Christ Jesus.",
                "Brethren, I count not myself to have apprehended: but this one thing I do, forgetting those things which are behind, and reaching forth unto those things which are before,",
                "I press toward the mark for the prize of the high calling of God in Christ Jesus.",
                "Let us therefore, as many as be perfect, be thus minded: and if in anything ye be otherwise minded, God shall reveal even this unto you.",
                "Nevertheless, whereto we have already attained, let us walk by the same rule, let us mind the same thing.",
                "Brethren, be followers together of me, and mark them which walk so as ye have us for an ensample.",
                "(For many walk, of whom I have told you often, and now tell you even weeping, that they are the enemies of the cross of Christ:",
                "Whose end is destruction, whose God is their belly, and whose glory is in their shame, who mind earthly things.)",
                "For our conversation is in heaven; from whence also we look for the Savior, the Lord Jesus Christ:",
                "Who shall change our vile body, that it may be fashioned like unto his glorious body, according to the working whereby he is able even to subdue all things unto himself."],
               [23,
                "Therefore, my brethren dearly beloved and longed for, my joy and crown, so stand fast in the Lord, my dearly beloved.",
                "I beseech Euodias, and beseech Syntyche, that they be of the same mind in the Lord.",
                "And I intreat thee also, true yokefellow, help those women which labored with me in the gospel, with Clement also, and with other my fellowlaborers, whose names are in the book of life.",
                "Rejoice in the Lord always: and again I say, Rejoice.",
                "Let your moderation be known unto all men. The Lord is at hand.",
                "Be careful for nothing; but in every thing by prayer and supplication with thanksgiving let your requests be made known unto God.",
                "And the peace of God, which passeth all understanding, shall keep your hearts and minds through Christ Jesus.",
                "Finally, brethren, whatsoever things are true, whatsoever things are honest, whatsoever things are just, whatsoever things are pure, whatsoever things are lovely, whatsoever things are of good report; if there be any virtue, and if there be any praise, think on these things.",
                "Those things, which ye have both learned, and received, and heard, and seen in me, do: and the God of peace shall be with you.",
                "But I rejoiced in the Lord greatly, that now at the last your care of me hath flourished again; wherein ye were also careful, but ye lacked opportunity.",
                "Not that I speak in respect of want: for I have learned, in whatsoever state I am, therewith to be content.",
                "I know both how to be abased, and I know how to abound: everywhere and in all things I am instructed both to be full and to be hungry, both to abound and to suffer need.",
                "I can do all things through Christ which strengthens me.",
                "Notwithstanding ye have well done, that ye did communicate with my affliction.",
                "Now ye Philippians know also, that in the beginning of the gospel, when I departed from Macedonia, no church communicated with me as concerning giving and receiving, but ye only.",
                "For even in Thessalonica ye sent once and again unto my necessity.",
                "Not because I desire a gift: but I desire fruit that may abound to your account.",
                "But I have all, and abound: I am full, having received of Epaphroditus the things which were sent from you, an odor of a sweet smell, a sacrifice acceptable, wellpleasing to God.",
                "But my God shall supply all your need according to his riches in glory by Christ Jesus.",
                "Now unto God and our Father be glory forever and ever. Amen.",
                "Salute every saint in Christ Jesus. The brethren which are with me greet you.",
                "All the saints salute you, chiefly they that are of Caesars household.",
                "The grace of our Lord Jesus Christ be with you all. Amen."]]
Colossians = [4]
fThessalonians = [5]
sThessalonians = [3]
fTimothy = [6]
sTimothy = [4]
Titus = [3]
Philemon = [1]
Hebrews = [13]
James = [5]
fPeter = [5]
sPeter = [3]
fJohn = [5]
sJohn = [1, [13,
             "The elder unto the elect lady and her children, whom I love in the truth; and not I only, but also all they that have known the truth;",
             "For the truths sake, which dwelleth in us, and shall be with us forever.",
             "Grace be with you, mercy, and peace, from God the Father, and from the Lord Jesus Christ, the Son of the Father, in truth and love.",
             "I rejoiced greatly that I found of thy children walking in truth, as we have received a commandment from the Father.",
             "And now I beseech thee, lady, not as though I wrote a new commandment unto thee, but that which we had from the beginning, that we love one another.",
             "And this is love, that we walk after his commandments. This is the commandment, That, as ye have heard from the beginning, ye should walk in it.",
             "For many deceivers are entered into the world, who confess not that Jesus Christ is come in the flesh. This is a deceiver and an antichrist.",
             "Look to yourselves, that we lost not those things which we have wrought, but that we receive a full reward.",
             "Whosoever transgretheth, and abideth not in the doctrine of Christ, hath not God. He that abideth in the doctrine of Christ, he hath both the Father and the Son.",
             "If there come any unto you, and bring not this doctrine, receive him not into your house, neither bid him God speed:",
             "For he that biddeth him God speed is partaker of his evil deeds.",
             "Having many things to write unto you, I would not write with paper and ink: but I trust to come unto you, and speak face to face, that our joy may be full.",
             "The children of thy elect sister greet thee. Amen."]]
tJohn = [1, [14,
             "The elder unto the wellbeloved Gaius, whom I love in the truth.",
             "Beloved, I wish above all things that thou mayest prosper and be in health, even as thy soul prospereth.",
             "For I rejoiced greatly, when the brethren came and testified of the truth that is in thee, even as thou walkest in the truth.",
             "I have no greater joy than to hear that my children walk in truth.",
             "Beloved, thou doest faithfully whatsoever thou doest to the brethren, and to strangers;",
             "Which have born witness of thy charity before the church: whom if thou bring forward on their journey after a godly sort, thou shalt do well:",
             "Because that for his names sake they went forth, taking nothing of the Gentiles.",
             "We therefore ought to receive such, that we might be fellowhelpers to the truth.",
             "I wrote unto the church: but Diotrephes, who loveth to have the preeminence among them, receiveth us not.",
             "Whenceforth, if I come, I will remember his deeds which he doeth, prating against us with malicious words: and not content therewith, neither doth he himself receive the brethren, and forbiddeth them that would, and casteth them out of the church.",
             "Beloved, follow not that which is evil, but that which is good. He that doeth good is of God: but he that doeth evil hath not seen God.",
             "Demetrius hath good report of all men, and of the truth itself: yea, and we also bear record; and ye know that our record is true.",
             "I had many things to write, but I will not with ink and pen write unto thee:",
             "But I trust I shall shortly see thee, and we shall speak face to face. Peace be to thee. Our friends salute thee. Greet the friends by name."]]
Jude = [1, [25,
            "Jude, the servant of Jesus Christ, and brother of James, to them that are sanctified by God the Father, and preserved in Jesus Christ, and called:",
            "Mercy unto you, and peace, and love, be multiplied.",
            "Beloved, when I gave all diligence to write unto you of the common salvation, it was needful for me to write unto you, and exhort you that ye should earnestly contend for the faith which was once delivered unto the saints.",
            "For there are certain men crept in unawares, who were before of old ordained to this condemnation, ungodly men, turning the grace of our God into lasciviousness, and denying the only Lord God, and our Lord Jesus Christ.",
            "I will therefore put you in remembrance, though ye once knew this, how that the Lord, having saved the people out of the land of Egypt, afterward destroyed them that believed not.",
            "And the angels which kept not their first estate, but left their own habitation, he hath reserved in everlasting chains under darkness unto the judgment of the great day.",
            "Even as Sodom and Gomorrha, and the cities about them in like manner, giving themselves over to fornication, and going after strange flesh, are set forth for an example, suffering the vengeance of eternal fire.",
            "Likewise also these filthy dreamers defile the flesh, despise dominion, and speak evil of dignities.",
            "Yet Michael the archangel, when contending with the devil he disputed about the body of Moses, durst not bring against him a railing accusation, but said, The Lord rebuke thee.",
            "But these speak evil of those things which they know not: but what they know naturally, as brute beasts, in those things they corrupt themselves.",
            "Woe unto them! For they have gone in the way of Cain, and ran greedily after the error of Balaam for reward, and perished in the gainsaying of Core.",
            "These are spots in your feasts of charity, when they feast with you, feeding themselves without fear: clouds they are without water, carried about of winds; trees whose fruit withereth, without fruit, twice dead, plucked up by the roots;",
            "Raging waves of the sea, foaming out their own shame; wandering stars, to whom is reserved the blackness of darkness forever.",
            "And Enoch also, the seventh from Adam, prophesied of these, saying, Behold, the Lord cometh with ten thousands of his saints,",
            "To execute judgment upon all, and to convince all that are ungodly among them of all their ungodly deeds which they have ungodly committed, and of all their hard speeches which ungodly sinners have spoken against him.",
            "These are murmurers, complainers, walking after their own lusts; and their mouth speaketh great swelling words, having mens persons in admiration because of advantage.",
            "But, beloved, remember ye the words which were spoken of our Lord Jesus Christ;",
            "How that they told you there should be mockers in the last time, who should walk after their own ungodly lusts.",
            "These be they who separate themselves, sensual, having not the Spirit.",
            "But ye, beloved, building up yourselves on your most holy faith, praying in the Holy Ghost,",
            "Keep yourselves in the love of God, looking for the mercy of our Lord Jesus Christ unto eternal life.",
            "And of some have compassion, making a difference:",
            "And others save with fear, pulling them out of the fire; hating even the garment spotted by the flesh.",
            "Now unto him that is able to keep you from falling, and to present you faultless before the presence of his glory with exceeding joy,",
            "To the only wise God our Savior, be glory and majesty, dominion and power, both now and ever. Amen."]]
Revelation = [22]

root = Tk()
root.title("PBA: Portable Bible Application")
root.maxsize(width=900, height=600)
root.minsize(width=900, height=600)

#Create the Frames
StatusBarFrame = Frame(root, width=800, height=30)
SelectionFrame = Frame(root, width=800, height=50)
LeftButtonsFrame = Frame(root, width=200, height=520)
CenterFrame = Frame(root, width=600, height=520)
BookFrame = Frame(SelectionFrame)
ChapFrame = Frame(SelectionFrame)
VerseFrame = Frame(SelectionFrame)
StatusBarFrame.pack(side=TOP)
SelectionFrame.pack(side=TOP)
LeftButtonsFrame.pack(side=LEFT)
CenterFrame.pack(side=RIGHT)
BookFrame.pack(side=LEFT)
ChapFrame.pack(side=LEFT)
VerseFrame.pack(side=RIGHT)

#StatusBar
statusVal = StringVar(root)
status = Label(StatusBarFrame, textvariable=statusVal)
status.pack()

def changeTest():
    global newT_books
    global oldT_books
    global all_books
    test = testBox.get()
    if test == "New Testament":
        bookBox.config(value=oldT_books)
    elif test == "Old Testament":
        bookBox.config(value=newT_books)
    else:
        bookBox.config(value=all_books)
    getBook()

def retBook():
    book = bookBox.get()
    if book == "Genesis":
        return Genesis
    elif book == "Exodus":
        return Exodus
    elif book == "Leviticus":
        return Leviticus
    elif book == "Numbers":
        return Numbers
    elif book == "Deuteronomy":
        return Deuteronomy
    elif book == "Joshua":
        return Joshua
    elif book == "Judges":
        return Judges
    elif book == "Ruth":
        return Ruth
    elif book == "1 Samuel":
        return fSamuel
    elif book == "2 Samuel":
        return sSamuel
    elif book == "1 Kings":
        return fKings
    elif book == "2 Kings":
        return sKings
    elif book == "1 Chronicles":
        return fChronicles
    elif book == "2 Chronicles":
        return sChronicles
    elif book == "Ezra":
        return Ezra
    elif book == "Nehemiah":
        return Nehemiah
    elif book == "Esther":
        return Esther
    elif book == "Job":
        return Job
    elif book == "Psalms":
        return Psalms
    elif book == "Proverbs":
        return Proverbs
    elif book == "Ecclesiastes":
        return Ecclesiastes
    elif book == "Song of Solomon":
        return Song_of_Solomon
    elif book == "Isaiah":
        return Isaiah
    elif book == "Jeremiah":
        return Jeremiah
    elif book == "Lamentations":
        return Lamentations
    elif book == "Ezekiel":
        return Ezekiel
    elif book == "Daniel":
        return Daniel
    elif book == "Hosea":
        return Hosea
    elif book == "Joel":
        return Joel
    elif book == "Amos":
        return Amos
    elif book == "Obadiah":
        return Obadiah
    elif book == "Jonah":
        return Jonah
    elif book == "Micah":
        return Micah
    elif book == "Nahum":
        return Nahum
    elif book == "Habakkuk":
        return Habakkuk
    elif book == "Zephaniah":
        return Zephaniah
    elif book == "Haggai":
        return Haggai
    elif book == "Zechariah":
        return Zechariah
    elif book == "Malachi":
        return Malachi
    elif book == "Matthew":
        return Matthew
    elif book == "Mark":
        return Mark
    elif book == "Luke":
        return Luke
    elif book == "John":
        return John
    elif book == "Acts":
        return Acts
    elif book == "Romans":
        return Romans
    elif book == "1 Corinthians":
        return fCorinthians
    elif book == "2 Corinthians":
        return sCorinthians
    elif book == "Galatians":
        return Galatians
    elif book == "Ephesians":
        return Ephesians
    elif book == "Philippians":
        return Philippians
    elif book == "Colossians":
        return Colossians
    elif book == "1 Thessalonians":
        return fThessalonians
    elif book == "2 Thessalonians":
        return sThessalonians
    elif book == "1 Timothy":
        return fTimothy
    elif book == "2 Timothy":
        return sTimothy
    elif book == "Titus":
        return Titus
    elif book == "Philemon":
        return Philemon
    elif book == "Hebrews":
        return Hebrews
    elif book == "James":
        return James
    elif book == "1 Peter":
        return fPeter
    elif book == "2 Peter":
        return sPeter
    elif book == "1 John":
        return fJohn
    elif book == "2 John":
        return sJohn
    elif book == "3 John":
        return tJohn
    elif book == "Jude":
        return Jude
    elif book == "Revelation":
        return Revelation

def retChap():
    chap = chapBox.get()
    return chap

def getBook():
    global screen
    if screen == "read":
        book = retBook()
        addChaps(book[0])

def showText():
    global alertVal, screen
    if screen == "read":
        book = retBook()
        chap = int(retChap())
        verse = int(verseBox.get())
        mainText.config(state="normal")
        mainText.delete(0.0, END)
        num = 1
        if verse == 0:
            alertVal.set(bookBox.get() + " " + chapBox.get())
            for i in book[chap][1:]:
                mainText.insert(END, str(num) + "] " + i + "\n\n")
                num += 1
        else:
            alertVal.set(bookBox.get() + " " + chapBox.get() + ":" + verseBox.get())
            mainText.insert(END, str(book[chap].index(book[chap][verse])) + "] " + book[chap][verse])
        mainText.config(state="disabled")

def addChaps(ammountChaps):
    l = []
    for i in range(ammountChaps):
        l.append(i+1)
    chapBox.config(value=l)
    book = retBook()
    chap = int(retChap())
    addVerses(book[chap][0])
    showText()

def addVerses(ammountVerses):
    l = []
    num = ammountVerses+1
    for i in range(num):
        l.append(i)
    verseBox.config(value=l)

filename = 'mybookmarks.pk1'

def addBookmark():
    global filename, bookmarks
    book = bookBox.get()
    chap = chapBox.get()
    f = open(filename, 'wb')
    try:
        with open(filename):
            bookmark = mainText.get(SEL_FIRST, SEL_LAST)
            bookmarks.append(book + " " + chap + "\n" + bookmark)
            pickle.dump(bookmarks, f)
            f.close()
    except FileNotFoundError:
        showerror(title='Oops!', message="You didn't select anything to add...")

def removeBookmark():
    global filename
    f = open(filename, 'rb')
    try:
        with open(filename):
            l = pickle.load(f)
            f.close()
            bookmark = mainText.get(SEL_FIRST, SEL_LAST)
            l.remove(bookmark)
            f = open(filename, 'wb')
            pickle.dump(l, f)
            f.close()
            viewBookmarks()
    except TclError:
        showerror(title='Oops!', message="You didn't select anything to remove...")

def viewBookmarks():
    global button1, button2, button3, button4, screen, filename
    screen = "bookmarks"
    alertVal.set("My Bookmarks")
    button1.config(text="Remove", command=removeBookmark)
    button2.config(text="< Back to Reading", command=backToMain)
    mainText.config(state="normal")
    mainText.delete(0.0, END)
    try:
        with open(filename):
            f = open(filename, 'rb')
            l = pickle.load(f)
            for i in l:
                mainText.insert(END, i + "\n-----------------------------------------------------------------------------")
            f.close()
    except FileNotFoundError:
        showerror(title='Oops!', message="You do not have any bookmarks yet")
    except EOFError:
        showerror(title='Oops!', message="Error!")
    mainText.config(state="disabled")


def backToMain():
    global button1, button2, button3, button4, screen
    screen = "read"
    button1.config(text="Add Bookmark", command=addBookmark)
    button2.config(text="My Bookmarks", command=viewBookmarks)
    showText()

def prevChapter(event):
    global screen
    if screen == 'read' and mainText.cget("takefocus") == "false":
        chapBox.invoke("buttondown")

def nextChapter(event):
    global screen
    if screen == 'read' and mainText.cget("takefocus") == "false":
        chapBox.invoke("buttonup")

def prevVerse(event):
    global screen
    if screen == "read":
        verseBox.invoke("buttondown")

def nextVerse(event):
    global screen
    if screen == "read":
        verseBox.invoke("buttonup")

def enterButton(event):
    global screen
    if screen == 'read':
        showText()

def focus(event):
    root.focus_force()
    mainText.configure(takefocus="false")

def focusBook(event):
    bookBox.focus_force()

def focusText(event):
    mainText.configure(takefocus="true")

def changeBg():
    col = askcolor()
    col = col[1]
    root.config(bg=col)
    ChapFrame.config(bg=col)
    BookFrame.config(bg=col)
    VerseFrame.config(bg=col)
    StatusBarFrame.config(bg=col)
    CenterFrame.config(bg=col)
    LeftButtonsFrame.config(bg=col)
    testLabel.config(bg=col)
    bookLabel.config(bg=col)
    chapLabel.config(bg=col)
    verseLabel.config(bg=col)
    mainText.config(bg=col)
    testBox.config(bg=col)
    bookBox.config(bg=col)
    chapBox.config(bg=col)
    verseBox.config(bg=col)
    alertLabel.config(bg=col)
    status.config(bg=col)
    saveColors()

def changeFg():
    col = askcolor()
    col = col[1]
    testLabel.config(fg=col)
    bookLabel.config(fg=col)
    chapLabel.config(fg=col)
    verseLabel.config(fg=col)
    chapBox.config(fg=col)
    bookBox.config(fg=col)
    testBox.config(fg=col)
    verseBox.config(fg=col)
    mainText.config(fg=col)
    alertLabel.config(fg=col)
    status.config(fg=col)
    saveColors()
    
bbg = None
bfg = None
babg = None
hbg = None
hfg = None

def changeButtonsBg():
    global bbg
    col = askcolor()
    col = col[1]
    button1.config(bg=col)
    button2.config(bg=col)
    button3.config(bg=col)
    button4.config(bg=col)
    button5.config(bg=col)
    bbg = col
    saveColors()

def changeButtonsAbg():
    global babg
    col = askcolor()
    col = col[1]
    button1.config(activebackground=col)
    button2.config(activebackground=col)
    button3.config(activebackground=col)
    button4.config(activebackground=col)
    button5.config(activebackground=col)
    babg = col
    saveColors()

def changeButtonsFg():
    global bfg
    col = askcolor()
    col = col[1]
    button1.config(fg=col)
    button2.config(fg=col)
    button3.config(fg=col)
    button4.config(fg=col)
    button5.config(fg=col)
    bfg = col
    saveColors()

def changeHighlightBg():
    global hbg
    col = askcolor()
    col = col[1]
    mainText.config(selectbackground=col)
    hbg = col
    saveColors()

def changeHighlightFg():
    global hfg
    col = askcolor()
    col = col[1]
    mainText.config(selectforeground=col)
    hfg = col
    saveColors()

settings = 'Biblesettings.pk1'
def saveColors():
    global settings, bbg, bfg, babg, hbg, hfg
    mainBg = root.cget("bg")
    mainFg = mainText.cget("fg")
    cols = [mainBg, mainFg, bbg, bfg, babg, hbg, hfg, "true"]
    f = open(settings, 'wb')
    pickle.dump(cols, f)
    f.close()

def loadColors():
    global settings
    try:
        with open(settings):
            f = open(settings, 'rb')
            l = pickle.load(f)
            mbg = l[0]
            mfg = l[1]
            bbg = l[2]
            bfg = l[3]
            babg = l[4]
            hbg = l[5]
            hfg = l[6]
            root.config(bg=mbg)
            ChapFrame.config(bg=mbg)
            BookFrame.config(bg=mbg)
            VerseFrame.config(bg=mbg)
            StatusBarFrame.config(bg=mbg)
            CenterFrame.config(bg=mbg)
            LeftButtonsFrame.config(bg=mbg)
            testLabel.config(bg=mbg, fg=mfg)
            bookLabel.config(bg=mbg, fg=mfg)
            chapLabel.config(bg=mbg, fg=mfg)
            verseLabel.config(bg=mbg, fg=mfg)
            mainText.config(bg=mbg, fg=mfg, selectbackground=hbg, selectforeground=hfg)
            testBox.config(bg=mbg, fg=mfg)
            bookBox.config(bg=mbg, fg=mfg)
            chapBox.config(bg=mbg, fg=mfg)
            verseBox.config(bg=mbg, fg=mfg)
            alertLabel.config(bg=mbg, fg=mfg)
            status.config(bg=mbg, fg=mfg)
            button1.config(bg=bbg, fg=bfg, activebackground=babg)
            button2.config(bg=bbg, fg=bfg, activebackground=babg)
            button3.config(bg=bbg, fg=bfg, activebackground=babg)
            button4.config(bg=bbg, fg=bfg, activebackground=babg)
            button5.config(bg=bbg, fg=bfg, activebackground=babg)
            f.close()
    except IOError:
        mbg = "white"
        mfg = "black"
        bbg = "white"
        bfg = "black"
        babg = "white"
        hbg = "gray"
        hfg = "black"
        root.config(bg=mbg)
        ChapFrame.config(bg=mbg)
        BookFrame.config(bg=mbg)
        VerseFrame.config(bg=mbg)
        StatusBarFrame.config(bg=mbg)
        CenterFrame.config(bg=mbg)
        LeftButtonsFrame.config(bg=mbg)
        testLabel.config(bg=mbg, fg=mfg)
        bookLabel.config(bg=mbg, fg=mfg)
        chapLabel.config(bg=mbg, fg=mfg)
        verseLabel.config(bg=mbg, fg=mfg)
        mainText.config(bg=mbg, fg=mfg, selectbackground=hbg, selectforeground=hfg)
        testBox.config(bg=mbg, fg=mfg)
        bookBox.config(bg=mbg, fg=mfg)
        chapBox.config(bg=mbg, fg=mfg)
        verseBox.config(bg=mbg, fg=mfg)
        alertLabel.config(bg=mbg, fg=mfg)
        status.config(bg=mbg, fg=mfg)
        button1.config(bg=bbg, fg=bfg, activebackground=babg)
        button2.config(bg=bbg, fg=bfg, activebackground=babg)
        button3.config(bg=bbg, fg=bfg, activebackground=babg)
        button4.config(bg=bbg, fg=bfg, activebackground=babg)
        button5.config(bg=bbg, fg=bfg, activebackground=babg)
    


tl = None
tl2 = None

def showHelp():
    global tl
    tl = Toplevel(root)
    tl.title("Help/Info")
    tl.minsize(width=400, height=400)
    tl.maxsize(width=400, height=400)
    Label(tl, text="Help/Info", font=("Helvetica", 20, "bold")).pack()
    scroll = Scrollbar(tl, orient=VERTICAL, relief="ridge")
    t = Text(tl, font=("Helvetica", 15, "bold"), wrap="word", yscrollcommand=scroll.set, height=13)
    scroll.configure(command=t.yview)
    scroll.pack(side=RIGHT, fill=Y, expand=NO)
    t.pack(side=TOP)
    t.insert(END, "This will be the helpful text and the information about the app...")
    t.config(state='disabled')
    exitButton = Button(tl, text="close", command=closeHelp)
    exitButton.pack()

def showSettings():
    global tl2
    tl2 = Toplevel(root)
    tl2.title("Settings")
    tl2.minsize(width=400, height=400)
    tl2.maxsize(width=400, height=400)
    Label(tl2, text="Settings", font=("Helvetica", 20, "bold")).pack()
    Label(tl2, text="Background", font=("Helvetica", 14)).pack()
    cBg = Button(tl2, text="Main Background", command=changeBg).pack()
    cFg = Button(tl2, text="Main Text", command=changeFg).pack()
    Label(tl2, text="Buttons", font=("Helvetica", 14)).pack()
    cButtonsBg = Button(tl2, text="Buttons Background", command=changeButtonsBg)
    cButtonsAbg = Button(tl2, text="Buttons Clicked Background", command=changeButtonsAbg)
    cButtonsFg = Button(tl2, text="Buttons Text", command=changeButtonsFg)
    cButtonsBg.pack()
    cButtonsAbg.pack()
    cButtonsFg.pack()
    Label(tl2, text="Highlight", font=("Helvetica", 14)).pack()
    cHighlightBg = Button(tl2, text="Highlight Background", command=changeHighlightBg)
    cHighlightFg = Button(tl2, text="Highlight Text", command=changeHighlightFg)
    cHighlightBg.pack()
    cHighlightFg.pack()
    Label(tl2, text="", font=("Helvetica", 14)).pack()
    closeButton = Button(tl2, text="Close", command=tl2.destroy)
    closeButton.pack()

def closeHelp():
    global tl
    tl.destroy()
                       

#Lists and their scrollbars(selection stuff)...
alertVal = StringVar()
alertLabel = Label(CenterFrame, textvariable=alertVal, font=("Helvetica", 30, "bold"), height=3)
testLabel = Label(BookFrame, text="Testament:")   
bookLabel = Label(BookFrame, text="Book:")
chapLabel = Label(ChapFrame, text="Chapter:")
verseLabel = Label(VerseFrame, text="Verse:")
bookBox = Spinbox(BookFrame, command=getBook, wrap=True)
chapBox = Spinbox(ChapFrame, command=showText, wrap=True)
verseBox = Spinbox(VerseFrame, command=showText, wrap=True)
testBox = Spinbox(BookFrame, value=("Both","Old Testament", "New Testament"), wrap=True, command=changeTest)
testLabel.pack(side=LEFT, fill=BOTH, expand=YES)
testBox.pack(side=LEFT, fill=BOTH, expand=YES)
bookLabel.pack(side=LEFT, fill=BOTH, expand=YES)
bookBox.pack(side=LEFT, fill=BOTH, expand=YES)
chapLabel.pack(side=LEFT, fill=BOTH, expand=YES)
chapBox.pack(side=LEFT, fill=BOTH, expand=YES)
verseLabel.pack(side=LEFT, fill=BOTH, expand=YES)
verseBox.pack(side=LEFT, fill=BOTH, expand=YES)
alertLabel.pack(side=TOP, fill=BOTH, expand=YES)

#Central Text
scroller = Scrollbar(CenterFrame, orient=VERTICAL, relief="ridge")
mainText = Text(CenterFrame, yscrollcommand=scroller.set, state="disabled", wrap="word")
scroller.configure(command=mainText.yview)
scroller.pack(side=RIGHT, expand=NO, fill=Y)
mainText.pack(fill=BOTH, expand=YES)
mainText.bind("<Left>", prevChapter)
mainText.bind("<Right>", nextChapter)
mainText.bind("<Up>", nextVerse)
mainText.bind("<Down>", prevVerse)
#The root must keep the focus otherwise a bug occurs when the arrow keys
#are used to change chapter/verse (it increases/decreases by 2 instead of 1).
#mainText.bind("<Leave>", focus)
#mainText.bind("<Enter>", focus)
#mainText.bind("<ButtonRelease>", focus)
#root.bind("<Button-1>", focus)
#root.bind("<Enter>", focus)
root.bind("<Left>", prevChapter)
root.bind("<Right>", nextChapter)
root.bind("<Up>", nextVerse)
root.bind("<Down>", prevVerse)

testBox.bind("<Return>", enterButton)
bookBox.bind("<Return>", enterButton)
chapBox.bind("<Return>", enterButton)
verseBox.bind("<Return>", enterButton)

#simple passing function
def c():
    pass

#Left Buttons
button1 = Button(LeftButtonsFrame, command=addBookmark, text="Add Bookmark", width=20, height=7, relief="raised", bd=5)
button2 = Button(LeftButtonsFrame, command=viewBookmarks, text="My Bookmarks", width=20, height=7, relief="raised", bd=5)
button3 = Button(LeftButtonsFrame, command=showHelp, text="Help/Info", width=20, height=7, relief="raised", bd=5)
button4 = Button(LeftButtonsFrame, command=root.destroy, text="QUIT", width=20, height=7, relief="raised", bd=5)
button5 = Button(LeftButtonsFrame, command=showSettings, text="Settings", width=20, height=1, relief="raised", bd=5)
button1.pack(side=TOP, expand=YES, fill=BOTH)
button2.pack(side=TOP, expand=YES, fill=BOTH)
button3.pack(side=TOP, expand=YES, fill=BOTH)
button4.pack(side=TOP, expand=YES, fill=BOTH)
button5.pack(side=TOP, expand=YES, fill=BOTH)


# on loadup, initiate the colors (buttons, bgs, etc.)
# also load the Book titles and chapter texts
# then begin the root window's main loop
loadColors()
changeTest()
getBook()
root.mainloop()