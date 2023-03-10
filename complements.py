# -*- coding: utf-8 -*-

import random

def read_data():
    compl_data = [

        'Здесь очень жарко или это из-за тебя?',
        'Ты словно Google или Яндекс. В тебе есть все, что я искал.',
        'Мне нужна карта и компас, чтобы не заблудиться в твоих глазах.',
        'Ты словно кофе: горячая, крепкая, вкусная, бодрящая и ароматная.',
        'Мне не нужен от тебя один секс. Мне нужны от тебя все твои сексы.',
        'С тобой можно в ресторан, в разведку и в ЗАГС.',
        'Я еще не выпил, но ты мне уже нравишься до умопомрачения.',
        'Красота спасет мир, а ты стоишь в самом первом ряду спасительниц.',
        'По шкале от 1 до 10, ты 100 баллов.',
        'Я принес тебе цветы, чтобы они увидели, что такое настоящая красота.',
        'К тебе даже мухи/комары/пчелы клеятся.',
        'Твои родители, наверное, кулинары, раз у них вышла такая великолепная крошка.',
        'Ты прекрасная на 60%. К сожалению, остальные 40% тебя скрыты одеждой.',
        'Ты просто идеальна, но в тебе нужно поменять одно. Сменить фамилию на мою.',
        'Как тебе удается с каждым разом выглядеть все лучше и лучше?',
        'Платье на тебе тютелька в тютельку. Мне нравятся твои тютельки.',
        'Мое утро начинается не с кофе, а мысли о тебе.',
        'Спасибо за твою нежность, доброту и заботу.',
        'Ты потрясающая и клевая девчонка. Честно; честно.',
        'В средние века тебя бы сожгли на костре, из-за волшебной красоты.',
        'Ты невероятно красивая, словно греческая богиня из мифологии.',
        'Ты самая классная девушка в мире. 100%',
        'Твой отец был боксером? Своей внешностью ты посылаешь в нокаут любого.',
        'У тебя ангельское личико, но тело грешницы.',
        'У меня внезапно потемнело в глазах. От твоей красоты.',
        'Все, что мне нужно для счастья – это ты.',
        'Я постоянно думаю о тебе, а ты поселилась в моих мыслях.',
        'Ты не нуждаешься в косметике. Она нуждается в тебе.',
        'Ты мой любимый вид наркотиков и алкоголя.',
        'Я не смотрю на твои потрясающие сиськи. Я смотрю на горячее сердце.',
        'Вместо Венеры Милосской должна быть твоя фигура.',
        'В мире всего есть три таких красотки: это ты, ты и еще раз ты.',
        'Я очень ценю и уважаю твое мнение.',
        'Думая о тебе, я начинаю улыбаться до ушей.',
        'Спасибо за поддержку и заботу, что ты оказываешь.',
        'Платье и аксессуары подходят к цвету твоих потрясающих глаз.',
        'Среди конкурса ангелов ты победила бы всех еще на кастинге.',
        'Твоя улыбка сводит меня с ума. Как у тебя получается так улыбаться?',
        'Я сделаю тебя по-настоящему счастливой.',
        'Твои родители воспитали отличную дочку. Золотая медаль.',
        'Ты потрясающая девушка. Ты должна это знаешь.',
        'Ради твоей улыбки хочется свернуть горы.',
        'Спасибо за то, что ты есть и такая замечательная.',
        'Ты определенно украшаешь этот мир и делаешь его лучше.',
        'Я очень скучаю по тебе.',
        'Мне кажется, что я в тебя влюбляюсь все сильнее и сильнее.',
        'Я никому тебя не отдам. Никому.',
        'Самое сложное с тобой – это прощаться.',
        'Твои уста сладкие и манящие, словно мед. А я «мохнатый пчол».',
        'Твои волосы и прическа восхитительны.',
        'У тебя ангельская и няшная внешность.',
        'Хочу быть только с тобой всю жизнь.',
        'Обожаю твою жизнерадостность и неиссякаемый позитив.',
        'Твои объятия нежные, словно я оказался в раю.',
        'Никогда не верил в любовь, до встречи с тобой.',
        'Вместе с тобой я чувствую себя живым.',
        'На тебя невозможно сердиться.',
        'У тебя очень заразительный смех. Словно колокольчики звенят.',
        'Ты всегда гармонично и безупречно выглядишь. Это природное?',
        'У тебя очень добрая, отзывчивая и нежная душа.',
        'Ты шикарно, отпадно и сногсшибательно выглядишь.',
        'Мне повезло, что судьба нас столкнула вместе.',
        'Ты мне больше, чем просто нравишься.',
        'Я бы сравнил тебя с цветком, но такого красивого не существует.',
        'Ты делаешь меня самым счастливым человеком на свете.',
        'Надеюсь, что наши дети будут похожи на тебя.',
        'Хочу заботиться о тебе и оберегать от всего мира.',
        'Ты девушка моей мечты. Или мечта моей жизни.',
        'От твоего внешнего вида у меня, иногда, перехватывает дыхание.',
        'Ты моя единственная.',
        'Ты родственная и самая близкая мне душа.',
        'В толпе людей подсознательно пытаюсь найти тебя.',
        'Когда ты улыбаешься, то словно солнце выходит из-за туч.',
        'Куда ты спрятала крылья и нимб? Ты определено ангел.',
        'Ты понимаешь меня без слов. С одного взгляда и мысли.',
        'Ты по-настоящему прикольная девчонка.',
        'Звуки твоего голоса заставляют мое сердце биться быстрее.',
        'Ты самый важный человек для меня на всем целом свете.',
        'Твоя фигура очень стройная, словно тростинка.',
        'Ты словно счастливый талисман, который приносит удачу и радость.',
        'Хочу, чтобы время останавливалось, когда мы рядом.',
        'Твой голос очень очаровательный и мелодичный. Как у волшебницы.',
        'Ты сумасшедшая и непостижимая девушка. Таких уже не выпускают.',
        'Красотка – это твое прозвище в детстве и второе имя.',
        'Идеальных людей не бывает. Но ты ведь есть.',
        'Во времена Трои, война была бы из-за тебя.',
        'Ты очень экстравагантная и необычная девушка.',
        'Ты из тех роковых красоток, в которых влюбляются без памяти.',
        'У тебя скромный и одновременно сильный характер.',
        'Ты волшебная и изумительная девушка, словно из сказки.',
        'Ты очень женственная и красивая. Само воплощение женственности.',
        'С тобой я становлюсь лучшей версией самого себя.',
        'Ты украсила мою жизнь и сделала ее яркой.',
        'У тебя очень нежная и приятная кожа, как у ребенка.',
        'Ты само совершенство, от улыбки до жестов выше всяких похвал.',
        'Ты не только мое солнце и луна, но и целая вселенная.',
        'Мне очень хорошо с тобой.',
        'У тебя очень милое и нежное лицо, когда ты спишь.',
        'У тебя выразительный, ясный, проницательный и умный взгляд.',
        'Мое сердце трепещет при встрече с тобой.',
        'Ты словно принцесса, которая вдохновляет на подвиги.',
        'В твоих глазах можно утонуть.',
        'Твой голос заставляет меня влюбляться раз за разом.',
        'В тебе кроется бесшабашная девчонка, которая потрясает меня.',
        'Твои движения, слова и внешность всегда меня заводят.',
        'У тебя прекрасное чувство юмора.',
        'Ты покорила меня своим совершенством. Порой мне кажется, что так не бывает.',
        'У тебя отличный загар/белоснежная кожа.',
        'Твой румянец на щечках очень милый.',
        'Платье сидит на тебе идеально и восхитительно.',
        'Ты очень целеустремленная и волевая девушка.',
        'Мне кажется, что ты умеешь читать мои мысли.',
        'Ты очень хорошая хозяйка.',
        'Не могу дождаться нашей встречи.',
        'У тебя шаловливый и непосредственно детский характер.',
        'О тебе я думаю утром, когда просыпаюсь. С мыслями о тебе ложусь спать.',
        'В тебе живет мечтательница и чуткая душа. Это редкость.',
        'Заметно, что ты занимаешься спортом.',
        'Ты очень стильная и умеешь подбирать гардероб.',
        'У тебя прекрасный и необычный цвет глаз.',
        'Ты неповторимая и уникальная.',
        'Люблю разговоры с тобой.',
        'У меня отнялась речь, когда я тебя увидел. Отлично выглядишь.',
        'Ты бесценная и неповторимая девушка.',
        'После нашей встречи я начал верить в судьбу.',
        'Ты привлекательна даже тогда, когда злишься.',
        'Твои манеры отличны и даже безупречны.',
        'Ты замечательная напарница по любому делу.',
        'Ты словно глоток воздуха в морской бездне.',
        'У тебя прелестные, пушистые и длинные реснички.',
        'Ты выглядишь как ТОП – модель с обложки.',
        'Не могу представить жизнь без тебя.',
        'Вне нравится в тебе внешностью, характер, темперамент. Абсолютно все.',
        'Ты очень горячая и сексуальная цыпочка.',
        'У тебя очень много талантов и достоинств. Природа постаралась.',
        'Ты так отлично и сексуально выглядишь, что это почти неприлично.',
        'Твои ножки очень красивые и горячие.',
        'У тебя незабываемые глаза и взгляд, которые запоминаешь на всю жизнь.',
        'Твой голос и внешность опьяняют.',
        'У тебя ослепительная и подкупающая улыбка.',
        'Своим характером ты способна установить мир на земле.',
        'Ты умеешь завораживать и очаровывать.',
        'У тебя очень мудрый и рассудительный ум. Откуда это?',
        'Ты отлично двигаешься, гибкая и очень пластична.',
        'В тебе скрывается опасная секс-бомба или даже порно звезда.',
        'Ты похожа на произведение искусства. Неповторима и бесценна.',
        'В тебе естественная женственность и очарование.',
        'Моя душа искала твою целую вечность.',
        'Ты поменяла мою жизнь к лучшему. Это много стоит.',
        'Ты очень утонченная, чуткая и ранимая натура.',
        'Ты даришь мне положительные эмоции и ощущения.',
        'Твои губы очень сладкие и нежные.',
        'Ты пахнешь очень вкусно и неповторимо.',
        'Мне нравится проводить с тобой время. Утром, днем, вечером и ночью.',
        'Ты энергичная, словно в тебе есть вечная батарейка в прелестной попке.',
        'Время с тобой всегда бежит очень быстро.',
        'Ты словно тигрица, опасная, красивая и грациозная.',
        'Никогда не встречал такую умную и проницательную девушку.',
        'Ты готовишь очень вкусно, пальчики оближешь.',
        'Я завидую сам себе, что у меня есть ты.',
        'Ты заводная, импульсивная и воинственная забияка, которая мне нравится.',
        'Твои обнимающие руки и голос – это словно бальзам на душу.',
        'У тебя великолепная, красивая и упругая грудь.',
        'Ты моя маленькая и беззащитная принцесса.',
        'Ты сладкая, словно конфетка или тортик.',
        'Думаю, тебя скоро посадит полиция. Ты украла мое сердце.',
        'У тебя очень выразительные черты лица.',
        'Ты еще сильнее похудела. Ты очень стройная.',
        'Ты очень ослепительно и восхитительно выглядишь для этой планеты.',
        'У тебя отличная фигура и задница. Ты могла быть моделью, если захотела.',
        'Твоя душа прекрасна и безгранична, словно океан.',
        'Эта одежда подчеркивает твою отличную фигуру.',
        'Ты всесторонне развита, умна и красива. Как такое бывает?',
        'Какого дракона нужно убить, чтобы завоевать такую принцессу?',
        'Твой животик очень аппетитный и привлекательный.',
        'Я горжусь твоими успехами и достижениями.',
        'Ты очень, очень, очень симпатичная. Нет. Очень красивая.',
        'Ты одинаково прекрасна снаружи и внутри.',
        'У тебя очень грандиозные цели и мечты. Поддерживаю.',
        'Ты великолепный и интересный собеседник.',
        'По утрам ты выглядишь очень мило и беззащитно.',
        'Откуда ты так много всего знаешь? Ты ходячая энциклопедия.',
        'Твоя фигура и внешность заслуживает кисти художников.',
        'Ты будоражащая и волнительная, словно ранняя весна.',
        'Мне нравится твоя независимость и сильный пробивной характер.',
        'Богиня красоты Афродита лишь слабая твоя копия.',
        'Ты настоящее сокровище, которое я никому не отдам.',
        'У тебя красивое и мелодичное имя. Мне нравится.',
        'Ты будоражишь своей внешностью всех мужчин этой планеты, а женщины завидуют.',
        'Как тебе удается так отлично выглядеть? У тебя сделка с дьяволом?',
        'Мне делали вчера кардиограмму и нашли тебя в моем сердце.',
        'У тебя спортивная и подтянутая фигура, а ты настоящая няшка.',
        'Ты обворожительна и безупречна, словно модель с обложки журнала.',
        'У тебя лучезарная улыбка, словно лучик солнца выглядывает из-за туч.',
        'Без тебя жизнь не жизнь. В ней нет смысла.',
        'В тебе есть характер и сила из легенд про амазонок. Ты была бы там главной.',
        'Ты луч солнца среди обыденности и серости этого мира.',
        'Выглядишь неотразимо и шикарно. Впрочем, как всегда.',
        'Твои прикосновения вызывают у меня мурашки по всему телу.',
        'Как жаль, что мы не встретились раньше. В детстве было бы идеально.',
        'Мне нравится с тобой даже молчать.',
        'Ты непредсказуемая и неординарная девушка. Этого у тебя не отнять.',
        'Ты кокетливая, озорная и игривая девчонка.',
        'Как тебе удается так гармонично и здорово подбирать аксессуары?',
        'У тебя очень пылкая натура и горячее честное сердце.',
        'От твоей внешности захватывает дух, словно я на краю пропасти.',
        'Ты дополняешь меня, моя половинка.',
        'Не могу перестать думать о тебе каждую секунду.',
        'Мне нравится твой природный запах. Он женственный и сексуальный.',
        'Ты не похожа на других людей. Ты странная, чудная и самая лучшая.',
        'Что ты говорила? Я так залюбовался тобой, что потерял слух.',
        'В тебе кроется множество загадок и непредсказуемости. Это заводит.',
        'Я не могу сосредоточиться. Ты выглядишь слишком волнительно.',
        'С тобой очень комфортно, словно мы знаем друг друга 1000 лет.',
        'Ты не только моя девушка, но и мой лучший друг. Я думал, что так не бывает.',
        'В твоей волнующей груди бьется пылкое сердце.',
        'Я обезоружен твоей внешностью и клевым характером.',
        'Твои губы соблазнительные, вызывающие и манящие.',
        'Голосок твой прелестный и одурманивает, словно музыка сирен.',
        'Невозможно выразить словами то, что я чувствую к тебе.',
        'Твоя попа словно круглый, упругий и аппетитный орех.',
        'После алкоголя ты становишься смешливой и опасной львицей.',
        'Тебе идут эти туфли, они подчеркивают красоту и длину ног.',
        'Мне нравится твои причуды и странности. С тобой не соскучишься.',
        'У тебя искрометный взгляд и манящая улыбка.',
        'У тебя великолепные и красивые волосы. Можно потрогать?',
        'Ты чертовски обаятельная и зажигательная. Это настоящее и природное.',
        'Тебе не занимать деликатности и такта. Ты словно леди в 21 веке.',
        'Тобой невозможно насытиться, ненаглядная моя.',
        'Ты миниатюрная и крошечная, которую хочется оберегать.',
        'Твоя непосредственность и восторженность ребенка покоряет меня.',
        'В тебе кроется бескорыстная, добрая и открытая душа.',
        'Я не равнодушен к твоим соблазнительным и порочным изгибам фигуры.',
        'Ты очень крутая и клевая девушка. Ты даже не подозреваешь насколько.',
        'Наверняка тебя любят дети, животные и даже природа.',
        'Сколько тебе лет? Ты не выглядишь на свои годы. Ты, наверное, врешь.',
        'В тебе есть что-то неуловимое и неземное, что невозможно тебя разгадать.',
        'Я тебя вижу каждую ночь во снах. Сны не всегда приличные.',
        'С тобой мы занимаемся не сексом, а настоящей любовью.',
        'Ты одна из немногих людей, кто умеет быть сама собой.',
        'У меня челюсть отвисла, ты так сногсшибательно выглядела.',
        'Моя одежда пахнет твоим незабываемым и любимым ароматом.',
        'Почему все восхищаются Анджелиной Джоли? Ты лучше в миллион раз.',
        'Твой голос лучше музыки чарует и услаждает слух.',
        'Никогда не думал, что встречу такую красотку и такую умную девчонку одновременно.',
        'У тебя большая/изящная грудь.',
        'Ты отличный пример для подражания другим.',
        'У тебя аристократический профиль лица. У тебя в роду не было аристократов?',
        'Ты словно фейерверк: умеешь зажигать и впечатлять.',
        'У тебя хрупкие и красивые плечи. Просто захватывает дух.',
        'Мне нравятся блондинки/брюнетки/шатенки/рыжие.',
        'У тебя романтичная натура. Ты последний романтик на земле.',
        'Ты определенно выглядишь на миллион баксов мелкими купюрами.',
        'В тебе природная кокетливость, какая бывает у одной из миллиона женщин.',
        'Я очень горжусь и восхищаюсь тобой.',
        'С того момента, как встретились, это мое лучшее время в жизни.',
        'У тебя порочная походка, которая заведет даже мертвых.',
        'Ты могла бы быть легко музой для художников, поэтов и писателей.',
        'В тебе кроется милый ангел и маленький чертенок.',
        'Ты очень молодо и отлично выглядишь.',
        'У тебя горячий темперамент в постели. Ты невероятная в сексе.',
        'Я хочу тебя снова и снова.',
        'Ты выглядишь трогательно, нежно и мило, словно принцесса.',
        'В тебе кроется азартный человек, который любит приключения.',
        'Я краснею, когда смотрю на тебя даже в одежде.',
        'У тебя очень аппетитные и горячие булочки.',
        'Ты эффектно и шикарно выглядишь в любой одежде.',
        'С тобой я бы отправился хоть на край света.',
        'Ты самая, самая, самая…',
        'Ты словно прекрасная нимфа, воплощающая женственность всех женщин.',
        'У тебя необузданная и неуправляемая сексуальность, которая сбивает с ног.',
        'Твои ножки – это словно ворота для входа в рай.',
        'Ты лучшая девушка, лучший друг, лучшая любовница и лучшая жена.',
        'От твоего декольте невозможно оторвать взгляд. Это выше моих сил.',
        'Ты прекрасный специалист и профессионал в своем деле.',
        'Когда ты намокла под дождем, то еще выглядишь лучше.',
        'Ты смесь хорошей и плохой девочки. Разве такое бывает?',
        'Меня притягивает к тебе. Где ты прячешь магнит?',
        'В тебя невозможно не влюбиться.',
        'Ты страстная, изобретательная и сексуальная кошечка.',
        'Без макияжа ты выглядишь лучше и соблазнительнее.',
        'У тебя клевая, упругая и аппетитная задница.',
        'Твое тело создано для любви и ласк.',
        'Ты очень развратная, пошлая и открытая в сексе. Мне это нравится.',
        'Ты словно шальная императрица Ирины Аллегровой. Оставляешь впечатление.',
        'Никогда не подозревал, что в тебе кроется столько страсти и сексуальности.',
        'Если за красоту садили бы в тюрьму, то ты имела бы несколько пожизненных.',
        'Ты просто улетный космос, детка.',
        'Ты потрясающая и невероятная в постели. Я даже захотел закурить.',
        'При виде тебя у меня поднимается настроение и все остальное.',
        'Если за секунду не ответишь, как дела, то должна 100 поцелуев. Ты не успела.',
        'Ты словно Джульетта из пьесы Уильяма Шекспира, только лучше.',
        'Ты как глоток шампанского, который пьянит голову и сбивает с ног.',
        'Когда я с тобой, то чувствую завистливые взгляды мужчин.',
        'Выходи за меня замуж.',
        'Я очень сильно тебя люблю.',

    ]

    return compl_data[random.randint(0, len(compl_data))]

#def read_file(): # из-за ебаной кодировки сервера это работать не будет

    #with open('compliment.txt') as f:
        #line = f.read().splitlines()

        #text = (line[random.randint(0, len(line))])

        #return text

        #return line[random.randint(0, len(line))]

