init:


    #NOTREADY
    transform ss_tryasuchki(image1, image2, image3):
        contains:
            xalign 0.5 yalign 1.0
            choice:
                image1
            choice:
                image2
            choice:
                image3
            pause 0.05
            repeat
        contains:
            xalign 0.5 yalign 1.0
            choice:
                image1
            choice:
                image2
            choice:
                image3
            alpha 0.25
            pause 0.05
            repeat
        contains:
            xalign 0.5 yalign 1.0
            choice:
                image1
            choice:
                image2
            choice:
                image3
            alpha 0.25
            pause 0.05
            repeat
    image mnd_child_dead = At("mnd_kid_dead_1", ss_tryasuchki("mnd_kid_dead_1", "mnd_kid_dead_2", "mnd_kid_dead_3"))


    transform mnd_jump1(dyz=0.01, dxz=0.005, dt=.4):
        yzoom 1.0
        easein dt*0.25 yzoom 1.0+dyz xzoom 1.0-dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        easein dt*0.25 yzoom 1.0-dyz xzoom 1.0+dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0







    image mnd_random_leaf:
        choice:
            "gesmemories/image/logo/mnd_ham_list1.png"
        choice:
            "gesmemories/image/logo/mnd_ham_list2.png"
        choice:
            "gesmemories/image/logo/mnd_ham_list3.png"
        choice:
            "gesmemories/image/logo/mnd_ham_list4.png"
        choice:
            "gesmemories/image/logo/mnd_ham_list5.png"
        xanchor 0.5 yanchor 0.5 rotate 0
        parallel:
            choice:
                rotate 0
                linear 5 rotate 360
                repeat
            choice:
                rotate 0
                linear 7 rotate -360
                repeat
            choice:
                rotate 0
                linear 9 rotate 360
                repeat
            choice:
                rotate 0
                linear 11 rotate -360
                repeat
            choice:
                rotate 0
                linear 13 rotate 360
                repeat
            choice:
                rotate 0
                linear 15 rotate -360
                repeat

    image mnd_moving_leaf:
        "mnd_random_leaf"
        parallel:
            choice:
                xpos -0.1 ypos 0.2
            choice:
                xpos -0.1 ypos 0.1
            choice:
                xpos -0.1 ypos 0.0
            choice:
                xpos 0.0 ypos -0.1
            choice:
                xpos 0.0 ypos -0.2
            choice:
                xpos 0.1 ypos -0.1
            choice:
                xpos 0.1 ypos -0.2
            choice:
                xpos 0.2 ypos -0.1
            choice:
                xpos 0.2 ypos -0.2
            choice:
                xpos 0.3 ypos -0.1
            choice:
                xpos 0.3 ypos -0.2
        parallel:
            choice:
                easeout 10 xpos 0.5
            choice:
                easeout 10 xpos 0.6
            choice:
                easeout 10 xpos 0.7
            choice:
                easeout 10 xpos 0.8
            choice:
                easeout 10 xpos 0.9
            choice:
                easeout 10 xpos 1.0
            choice:
                easeout 10 xpos 1.1
        parallel:
            choice:
                linear 7 ypos 1.1
            choice:
                linear 8 ypos 1.1
            choice:
                linear 9 ypos 1.1
            choice:
                linear 10 ypos 1.1
            choice:
                linear 10 ypos 1.1
        repeat

    image mnd_leafs:
        contains:
            "mnd_moving_leaf"
        contains:
            pause 0.5
            "mnd_moving_leaf"
        contains:
            pause 1.0
            "mnd_moving_leaf"
        contains:
            pause 1.5
            "mnd_moving_leaf"
        contains:
            pause 2.0
            "mnd_moving_leaf"
        contains:
            pause 2.5
            "mnd_moving_leaf"
        contains:
            pause 3.0
            "mnd_moving_leaf"
        contains:
            pause 3.5
            "mnd_moving_leaf"
        contains:
            pause 4.0
            "mnd_moving_leaf"
        contains:
            pause 4.5
            "mnd_moving_leaf"
        contains:
            pause 5.0
            "mnd_moving_leaf"
        contains:
            pause 5.5
            "mnd_moving_leaf"
        contains:
            pause 6.0
            "mnd_moving_leaf"
        contains:
            pause 6.5
            "mnd_moving_leaf"
        contains:
            pause 7.0
            "mnd_moving_leaf"
        contains:
            pause 7.5
            "mnd_moving_leaf"
        contains:
            pause 8.0
            "mnd_moving_leaf"
        contains:
            pause 8.5
            "mnd_moving_leaf"
        contains:
            pause 9.0
            "mnd_moving_leaf"
        contains:
            pause 9.5
            "mnd_moving_leaf"

    image mnd_leafs2:
        contains:
            "mnd_leafs"
        contains:
            "mnd_leafs"

    image mnd_leafs3:
        contains:
            "mnd_leafs"
        contains:
            "mnd_leafs"
        contains:
            "mnd_leafs"




    #####LIYA_SHARDS#####
    image mnd_random_liliya:
        choice:
            "gesmemories/image/logo/mnd_liya_lep_1.png"
        choice:
            "gesmemories/image/logo/mnd_liya_lep_2.png"
        choice:
            "gesmemories/image/logo/mnd_liya_lep_3.png"
        choice:
            "gesmemories/image/logo/mnd_liya_lep_4.png"
        choice:
            "gesmemories/image/logo/mnd_liya_lep_5.png"
        xanchor 0.5 yanchor 0.5 rotate 0
        parallel:
            choice:
                rotate 0
                linear 5 rotate 360
                repeat
            choice:
                rotate 0
                linear 7 rotate -360
                repeat
            choice:
                rotate 0
                linear 9 rotate 360
                repeat
            choice:
                rotate 0
                linear 11 rotate -360
                repeat
            choice:
                rotate 0
                linear 13 rotate 360
                repeat
            choice:
                rotate 0
                linear 15 rotate -360
                repeat

    image mnd_moving_liliya:
        "mnd_random_liliya"
        parallel:
            choice:
                xpos -0.1 ypos 0.2
            choice:
                xpos -0.1 ypos 0.1
            choice:
                xpos -0.1 ypos 0.0
            choice:
                xpos 0.0 ypos -0.1
            choice:
                xpos 0.0 ypos -0.2
            choice:
                xpos 0.1 ypos -0.1
            choice:
                xpos 0.1 ypos -0.2
            choice:
                xpos 0.2 ypos -0.1
            choice:
                xpos 0.2 ypos -0.2
            choice:
                xpos 0.3 ypos -0.1
            choice:
                xpos 0.3 ypos -0.2
        parallel:
            choice:
                easeout 10 xpos 0.5
            choice:
                easeout 10 xpos 0.6
            choice:
                easeout 10 xpos 0.7
            choice:
                easeout 10 xpos 0.8
            choice:
                easeout 10 xpos 0.9
            choice:
                easeout 10 xpos 1.0
            choice:
                easeout 10 xpos 1.1
        parallel:
            choice:
                linear 7 ypos 1.1
            choice:
                linear 8 ypos 1.1
            choice:
                linear 9 ypos 1.1
            choice:
                linear 10 ypos 1.1
            choice:
                linear 10 ypos 1.1
        repeat

    image mnd_liliya_shards:
        contains:
            "mnd_moving_liliya"
        contains:
            pause 0.5
            "mnd_moving_liliya"
        contains:
            pause 1.0
            "mnd_moving_liliya"
        contains:
            pause 1.5
            "mnd_moving_liliya"
        contains:
            pause 2.0
            "mnd_moving_liliya"
        contains:
            pause 2.5
            "mnd_moving_liliya"
        contains:
            pause 3.0
            "mnd_moving_liliya"
        contains:
            pause 3.5
            "mnd_moving_liliya"
        contains:
            pause 4.0
            "mnd_moving_liliya"
        contains:
            pause 4.5
            "mnd_moving_liliya"
        contains:
            pause 5.0
            "mnd_moving_liliya"
        contains:
            pause 5.5
            "mnd_moving_liliya"
        contains:
            pause 6.0
            "mnd_moving_liliya"
        contains:
            pause 6.5
            "mnd_moving_liliya"
        contains:
            pause 7.0
            "mnd_moving_liliya"
        contains:
            pause 7.5
            "mnd_moving_liliya"
        contains:
            pause 8.0
            "mnd_moving_liliya"
        contains:
            pause 8.5
            "mnd_moving_liliya"
        contains:
            pause 9.0
            "mnd_moving_liliya"
        contains:
            pause 9.5
            "mnd_moving_liliya"

    image mnd_liliya2:
        contains:
            "mnd_liliya"
        contains:
            "mnd_liliya"

    image mnd_liliya3:
        contains:
            "mnd_liliya"
        contains:
            "mnd_liliya"
        contains:
            "mnd_liliya"



































    transform aw_heartattack(img):
        #contains:
        #    img
        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 1.10
            repeat
        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 0.90
            repeat
        contains:
            "blood"
            alpha 0.0
            block:
                ease 0.25 alpha 1.0
                ease 0.75 alpha 0.75
                repeat
    python:
        def Aw_HeartAttack(img):
            renpy.show(img, tag="bg2", at_list=[aw_heartattack(img)])





    transform aw_alko(img):
        #contains:
        #    img
        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 1.10
            repeat
        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 0.90
            repeat

    python:
        def Aw_Alko(img):
            renpy.show(img, tag="bg2", at_list=[aw_alko(img)])


















init:

    $ mnd_dissolve_hands = ImageDissolve("gesmemories/image/spr/old/zmey/hands_dissolve.png", 2.5, 100, alpha=True)

    image zmey_hands_stars:
        "gesmemories/image/spr/old/zmey/hands_stars1.png" with Dissolve(2.0, alpha=True)
        pause 2.0
        "gesmemories/image/spr/old/zmey/hands_stars2.png" with Dissolve(2.0, alpha=True)
        pause 2.0
        "gesmemories/image/spr/old/zmey/hands_stars3.png" with Dissolve(2.0, alpha=True)
        pause 2.0
        "gesmemories/image/spr/old/zmey/hands_stars4.png" with Dissolve(2.0, alpha=True)
        pause 2.0
        repeat

    image zmey_hands_hands:
        "gesmemories/image/spr/old/zmey/hands.png" with mnd_dissolve_hands
        pause 2.5
        "gesmemories/image/spr/old/zmey/hands2.png" with mnd_dissolve_hands
        pause 2.5
        repeat

    image zmey_hands:
        contains:
            "gesmemories/image/spr/old/zmey/mndzmey.png"
        contains:
            "zmey_hands_hands"
        contains:
            "zmey_hands_stars"







init:
    image bg videobg = Movie(play="gesmemories/video/rain.mp4", channel="movie", size=(1920, 1080))

    image mndrain_l:
        contains:
            "mndrain_c"
            rotate 10

    image mndrain_r:
        contains:
            "mndrain_c"
            rotate -10

    image mndrain2_c:
        contains:
            "mndrain_c"
        contains:
            "mndrain_c"
            zoom 0.75

    image mndrain2_l:
        contains:
            "mndrain2_c"
            rotate 10

    image mndrain2_r:
        contains:
            "mndrain2_c"
            rotate -10



    transform mnd_master_tryas:
        xalign 0.5 yalign 0.5
        parallel:
            ease 0.25 zoom 1.1
            ease 0.5 zoom 1.0
        parallel:
            ease 0.25 rotate -1.5
            ease 0.25 rotate 1.0
            ease 0.25 rotate 0.0

    transform mnd_jump(dyz=0.01, dxz=0.005, dt=.4):
        yzoom 1.0
        easein dt*0.25 yzoom 1.0+dyz xzoom 1.0-dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        easein dt*0.25 yzoom 1.0-dyz xzoom 1.0+dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0

    python:
        for i in renpy.list_files():
            for dir in ["amb", "mp3", "sfx", "vocal"]:
                if( i.startswith("gesmemories/snd/"+dir+"/") and i.endswith((".mp3", ".wav", ".ogg"))):
                    gl = globals()
                    gl[(str(i[len("gesmemories/snd/"+dir+"/"):-4]))] = i




init python:

    import math
    class FireGlowDot(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = [ ]
            self.rd = "gesmemories/image/logo/firedrop.png"

            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))

            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)

            self.glows.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)

            return 0
    renpy.image("fireeffmnd", FireGlowDot().sm)

init python:

    class MndOldCh(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = [ ]
            self.rd = "gesmemories/image/logo/mndlist.png"

            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))

            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)

            self.glows.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start + speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)

            return 0
    renpy.image("mndoldanim1", MndOldCh().sm)


init python:

    class MndMenuCh(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = [ ]
            self.rd = "gesmemories/image/logo/chast1.png"

            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))

            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)

            self.glows.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)

            return 0
    renpy.image("menuanima", MndMenuCh().sm)



init python:

    class MndCutM(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = [ ]
            self.rd = "gesmemories/image/scene/cutm.png"

            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))

            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)

            self.glows.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)

            return 0
    renpy.image("mndcutm", MndCutM().sm)

init python:
    class SmertGlowDot(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = [ ]
            self.rd = "gesmemories/image/logo/fish_drop.png"

            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))

            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)

            self.glows.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)

            return 0
    renpy.image("smertfishdrop", SmertGlowDot().sm)

###AWAYAWAYAWAY
init python:
    import math
    class AwKmStr(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = [ ]
            self.rd = "away/img/eff/aw_km_st_1.png"
            self.rd = "away/img/eff/aw_km_st_2.png"
            self.rd = "away/img/eff/aw_km_st_1.png"

            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))

            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)

            self.glows.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start + speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)

            return 0
    renpy.image("aw_km_stars", AwKmStr().sm)

###






init:

    $ vas = Character(u'Василий', color="#666666", what_color="E2C778",)
    $ vasi = Character(u'Василий', color="#9950fd", what_color="E2C778",)
    $ vast = Character(u'Василий', color="#666666", what_color="E2C778", what_prefix="{font=gesmemories/fnt/beermoney.ttf}", what_suffix="{/font}")
    $ vasb = Character(u'Василий', color="#1743ff", what_color="891111", what_prefix="{font=gesmemories/fnt/beermoney.ttf}", what_suffix="{/font}")
    $ vasg = Character(u'Василий', color="#1743ff", what_color="E2C778",)
    $ psyth = Character(u'...', color="#891111", what_color="01fff6",)
    $ logdoc = Character(u'Доктор', color="#18FFEB", what_color="E2C778",)
    $ mndneiz = Character(u'Неизвестный', color="#870909", what_color="E2C778",)
    $ brod = Character(u'Бродяга', color="#BF5522", what_color="E2C778",)
    $ phvoise = Character(u'Голос в динамике', color="#6BB7B2", what_color="E2C778",)
    $ hartsman = Character(u'Посетитель бара', color="#6BB7B2", what_color="E2C778",)
    $ liya = Character(u'Лия', color="#FF7C00", what_color="E2C778",)
    $ liyar = Character(u'Лия', color="#870909", what_color="FF7C00",)
    $ dart = Character(u'Артём', color="#4B3DD1", what_color="E2C778",)
    $ lizard = Character(u'Ящер', color="#0F722D", what_color="E2C778",)
    $ mndneiz = Character(u'Неизвестный', color="#870909", what_color="E2C778",)
    $ gldoc = Character(u'Глав-врач', color="#B2B087", what_color="E2C778",)
    $ zihao = Character(u'Доктор Зихао', color="#18FFEB", what_color="E2C778",)
    $ travmdoc = Character(u'Tравматолог', color="#4B3DD1", what_color="E2C778",)
    $ qqpats = Character(u'Парень', color="#CB94F0", what_color="E2C778",)
    $ qqdev = Character(u'Девушка', color="#EDE7E7", what_color="E2C778",)
    $ andr = Character(u'Андрей', color="#FFB700", what_color="E2C778",)
    $ ten = Character(u'Тень', color="#7C00B6", what_color="E2C778",)
    $ tarak = Character(u'Таракан', color="#BF5522", what_color="E2C778",)
    $ voise1 = Character(u'Голос', color="#BF5522", what_color="E2C778",)
    $ voice2 = Character(u'Голос', color="#42CB8B", what_color="E2C778",)
    $ voise2 = Character(u'Голос', color="#42CB8B", what_color="E2C778",)
    $ vs1 = Character(u'Голос', color="#BF5522", what_color="E2C778",)
    $ vs2 = Character(u'Голос', color="#EDE7E7", what_color="E2C778",)
    $ filin = Character(u'Филин', color="#3DCA00", what_color="E2C778",)
    $ psyvas = Character(u'Василий', color="#891111", what_color="E2C778",)
    $ deads = Character(u'Смерть', color="#812CE8", what_color="1CF0DA",)
    $ smert = Character(u'Смерть', color="#812CE8", what_color="1CF0DA",)
    $ medbr = Character(u'Мед-брат', color="#42CB8B", what_color="E2C778",)
    $ miya = Character(u'Мия', color="#6BB7B2", what_color="E2C778",)
    $ thz = Character(u'...', color="#891111", what_color="1CF0DA", what_prefix="{font=gesmemories/fnt/beermoney.ttf}", what_suffix="{/font}")
    $ thn = Character(u'...', color="#E2C778", what_color="E2C778", what_prefix="{font=gesmemories/fnt/beermoney.ttf}", what_suffix="{/font}")
    $ himera = Character(u'Химера', color="#CB94F0", what_color="E2C778",)
    $ himori = Character(u'Химори', color="#CB94F0", what_color="E2C778",)
    $ lin = Character(u'Лин', color="#BF2525", what_color="E2C778",)
    $ riba = Character(u'Рыба', color="#01fff6", what_color="E2C778",)
    $ lisa = Character(u'Лиса', color="#ff4900", what_color="E2C778",)
    $ eretic = Character(u'Еретик', color="#9c9872", what_color="E2C778",)
    $ mndlapa = Character(u'Лапа', color="#3c2818", what_color="E2C778",)
    $ mndbul = Character(u'Булыжник', color="#47573c", what_color="E2C778",)
    $ mndel = Character(u'Электрик', color="#6f929d", what_color="E2C778",)
    $ kukla = Character(u'Кукла', color="#595859", what_color="E2C778",)
    $ mndmuj = Character(u'Мужчина', color="#af865d", what_color="E2C778",)
    $ tenoldkid = Character(u'...', color="#69028b", what_color="8decf2",)
    $ tenkid = Character(u'...', color="#69028b", what_color="8decf2",)
    $ qqwom = Character(u'Женщина', color="#EDE7E7", what_color="E2C778",)
    $ mndkidm1 = Character(u'Мальчик', color="#9a8c30", what_color="E2C778",)
    $ mndkidm2 = Character(u'Мальчик', color="#a53232", what_color="E2C778",)
    $ mndkidm3 = Character(u'Мальчик', color="#ef7c2f", what_color="E2C778",)
    $ mndkidm4 = Character(u'Мальчик', color="#3256a5", what_color="E2C778",)
    $ mndler = Character(u'Лерой', color="#EDE7E7", what_color="E2C768",)
    $ mndsan = Character(u'Cанитар', color="#4B3DD1", what_color="E2C778",)
    $ mndgirl = Character(u'Девочка', color="#78d8c7", what_color="E2C778",)
    $ mndzmey= Character(u'Змей', color="#146036", what_color="E2C778",)
    $ mndoldman= Character(u'Cтарик', color="#725e37", what_color="E2C778",)
    $ mndkrolch= Character(u'Крольчиха', color="#959494", what_color="E2C778",)
    $ mndliza = Character(u'Лиза', color="#01F8B2", what_color="E2C778",)
    $ mndslep = Character(u'Слепая', color="#808080", what_color="E2C778",)
    $ mndvorona = Character(u'Ворона', color="#c6c6c6", what_color="E2C778",)
    $ tenold = Character(u'Ворон', color="#9324cc", what_color="E2C778",)
    $ mndden = Character(u'Денис', color="#2f74ff", what_color="E2C778",)
    $ mndarah = Character(u'Арахна', color="#9950fd", what_color="E2C778",)
    $ mndshak = Character(u'Шакал', color="#a66f3a", what_color="E2C778",)
    $ mndsugar = Character(u'Сахарок', color="#CB94F0", what_color="E2C778",)
    $ mndbleed = Character(u'Бледный', color="#e3e3e3", what_color="E2C778",)
    $ mndtarold = Character(u'Орёл', color="#BF5522", what_color="E2C778",)
    $ mndtrubo = Character(u'Трубадур', color="#af865d", what_color="E2C778",)
    $ medsestr = Character(u'Медсестра', color="#EDE7E7", what_color="E2C778",)
    $ xian = Character(u'Сянь', color="#812CE8", what_color="CABADC",)
    $ mnddevu = Character(u'Девушка', color="#9950fd", what_color="E2C778",)
    $ mndluci = Character(u'Люсьена', color="#01fff6", what_color="E2C778",)
    $ mndpsyvoice = Character(u'Голос', color="#ffffff", what_color="ffffff",)
    $ mndofits = Character(u'Официантка', color="#EDE7E7", what_color="E2C778",)
    $ mndstoroj = Character(u'Сторож', color="#2f74ff", what_color="E2C778",)
    $ mndbor = Character(u'Борис', color="#47573c", what_color="E2C778",)
    $ mndksen = Character(u'Ксения', color="#4B3DD1", what_color="E2C778",)
    $ sl = Character(u'Милдред Джекил', color="#f4e71b", what_color="E2C778",)



    $ mndmenutheme = "gesmemories/snd/mp3/mndmenutheme.mp3"
    $ mnd_longing = "gesmemories/snd/mp3/mnd_longing.mp3"
    $ amb01_l = "gesmemories/snd/mp3/amb01_l.ogg"
    $ inwest = "gesmemories/snd/mp3/inwest.mp3"
    $ sophie = "gesmemories/snd/mp3/sophie.mp3"
    $ anna_talk = "gesmemories/snd/mp3/anna_talk.ogg"
    $ aphex = "gesmemories/snd/mp3/aphex.mp3"
    $ arcano = "gesmemories/snd/mp3/arcano.ogg"
    $ deadisland = "gesmemories/snd/mp3/deadisland.mp3"
    $ diefor = "gesmemories/snd/mp3/diefor.mp3"
    $ firstforthefirst = "gesmemories/snd/mp3/firstforthefirst.mp3"
    $ gesgoodbye = "gesmemories/snd/mp3/gesgoodbye.mp3"
    $ intig_cut = "gesmemories/snd/mp3/intig_cut.mp3"
    $ letmefall = "gesmemories/snd/mp3/letmefall.mp3"
    $ liyadance = "gesmemories/snd/mp3/liyadance.mp3"
    $ minin = "gesmemories/snd/mp3/minin.mp3"
    $ mus4 = "gesmemories/snd/mp3/mus4.ogg"
    $ oblivionamb1 = "gesmemories/snd/mp3/oblivionamb1.mp3"
    $ oblivionamb2 = "gesmemories/snd/mp3/oblivionamb2.mp3"
    $ oftherside = "gesmemories/snd/mp3/oftherside.mp3"
    $ outofit0 = "gesmemories/snd/mp3/outofit0.mp3"
    $ psyhosis = "gesmemories/snd/mp3/psyhosis.mp3"
    $ sexuallobster = "gesmemories/snd/mp3/sexuallobster.mp3"
    $ tentheme = "gesmemories/snd/mp3/tentheme.mp3"
    $ train_station = "gesmemories/snd/mp3/train_station.mp3"
    $ deadislandtheme = "gesmemories/snd/mp3/deadislandtheme.mp3"
    $ hatelife = "gesmemories/snd/mp3/hatelife.mp3"
    $ trolwow = "gesmemories/snd/mp3/trolwow.mp3"
    $ dead_more = "gesmemories/snd/mp3/deadmore.mp3"
    $ sneak_peek = "gesmemories/snd/mp3/sneakpeek.mp3"
    $ notefind = "gesmemories/snd/mp3/notefind.mp3"
    $ oblivionamb3 = "gesmemories/snd/mp3/oblivionamb3.mp3"
    $ oblivionamb4 = "gesmemories/snd/mp3/oblivionamb4.mp3"
    $ mndchaplogo = "gesmemories/snd/mp3/mndchaplogo.mp3"
    $ mndcrow = "gesmemories/snd/mp3/mndcrow.mp3"
    $ goodamb1 = "gesmemories/snd/mp3/goodamb1.mp3"
    $ mndsad1 = "gesmemories/snd/mp3/mndsad1.mp3"
    $ goodamb2 = "gesmemories/snd/mp3/goodamb2.mp3"
    $ likeastranger = "gesmemories/snd/mp3/likeastranger.mp3"
    $ mndfuck = "gesmemories/snd/mp3/mndfuck.mp3"
    $ mndnervsr = "gesmemories/snd/mp3/mndnervsr.wav"
    $ mndbrtp = "gesmemories/snd/mp3/mndbrtp.mp3"
    $ wasbounce = "gesmemories/snd/mp3/wasbounce.mp3"
    $ mndtencar = "gesmemories/snd/mp3/mndtencar.mp3"
    $ mndoldchap = "gesmemories/snd/mp3/mndoldchap.mp3"
    $ mndmaincraftamd1 = "gesmemories/snd/mp3/mndmaincraftamd1.mp3"
    $ mndreveilcut = "gesmemories/snd/mp3/mndreveilcut.mp3"
    $ mndtentheme = "gesmemories/snd/mp3/MND_Ten_Theme.mp3"
    $ mnddo1 = "gesmemories/snd/mp3/mnddo1.mp3"
    $ mnddo2 = "gesmemories/snd/mp3/mnddo2.mp3"
    $ mndreveilcut = "gesmemories/snd/mp3/mndreveilcut.mp3"
    $ mndtentheme = "gesmemories/snd/mp3/MND_Ten_Theme.mp3"
    $ mnddo1 = "gesmemories/snd/mp3/mnddo1.mp3"
    $ mnddo2 = "gesmemories/snd/mp3/mnddo2.mp3"
    $ mnddo3 = "gesmemories/snd/mp3/mnddo3.mp3"
    $ mnddo4 = "gesmemories/snd/mp3/mnddo4.mp3"
    $ mnddo5 = "gesmemories/snd/mp3/mnddo5.mp3"
    $ mndkidfight = "gesmemories/snd/mp3/mndkidfight.mp3"
    $ mndnomore = "gesmemories/snd/mp3/mndnomore.mp3"
    $ mndlabmusic = "gesmemories/snd/mp3/mndlabmusic.mp3"
    $ mndcda = "gesmemories/snd/mp3/mndcda.mp3"
    $ mndreveilfull = "gesmemories/snd/mp3/mndreveilfull.mp3"
    $ mndtenfinaltit = "gesmemories/snd/mp3/mndtenfinaltit.mp3"
    $ jojoawaken = "gesmemories/snd/mp3/jojoawaken.mp3"
    $ mndarahnatheme = "gesmemories/snd/mp3/mndarahnatheme.mp3"
    $ mndbcl = "gesmemories/snd/mp3/mndbcl.mp3"
    $ mndhklfa = "gesmemories/snd/mp3/mndhklfa.mp3"
    $ mndfight2 = "gesmemories/snd/mp3/mndfight2.mp3"
    $ mnd8room1 = "gesmemories/snd/mp3/mnd8room1.mp3"
    $ mndsguv = "gesmemories/snd/mp3/mndsguv.mp3"
    $ mndmorning = "gesmemories/snd/mp3/mndmorning.mp3"
    $ mndsmertsong = "gesmemories/snd/mp3/mndsmertsong.mp3"
    $ mndsnzu = "gesmemories/snd/mp3/mndsnzu.mp3"
    $ mndarb = "gesmemories/snd/mp3/mndarb.mp3"
    $ mnd8room2 = "gesmemories/snd/mp3/mnd8room2.mp3"
    $ mndgluhnorm = "gesmemories/snd/mp3/mndgluhnorm.mp3"
    $ mndhimdio = "gesmemories/snd/mp3/mndhimdio.mp3"
    $ mndhimeratheme = "gesmemories/snd/mp3/mndhimeratheme.mp3"
    $ mndintotherain = "gesmemories/snd/mp3/mndintotherain.mp3"
    $ mndmemodead = "gesmemories/snd/mp3/mndmemodead.mp3"
    $ mndbledvszmey = "gesmemories/snd/mp3/mndbledvszmey.mp3"
    $ mndelvinforest = "gesmemories/snd/mp3/mndelvinforest.mp3"
    $ mndgraveyard = "gesmemories/snd/mp3/mndgraveyard.mp3"
    $ mndhandandeyes = "gesmemories/snd/mp3/mndhandandeyes.mp3"
    $ mndparachute = "gesmemories/snd/mp3/mndparachute.mp3"
    $ mndcrossingtrack = "gesmemories/snd/mp3/mndcrossingtrack.mp3"
    $ mnddanger111 = "gesmemories/snd/mp3/mnddanger111.ogg"
    $ mndfmt = "gesmemories/snd/mp3/mndfmt.mp3"
    $ mndhallucination = "gesmemories/snd/mp3/mndhallucination.mp3"
    $ mndhelvete = "gesmemories/snd/mp3/mndhelvete.mp3"
    $ mndnmrih1 = "gesmemories/snd/mp3/mndnmrih1.ogg"
    $ mndtogiveup = "gesmemories/snd/mp3/mndtogiveup.ogg"
    $ mnd_grace_behind_the_curtain = "gesmemories/snd/mp3/mnd_grace_behind_the_curtain.mp3"
    $ mnd_psy_lift_numbers_start = "gesmemories/snd/mp3/mnd_psy_lift_numbers_start.mp3"
    $ mnd_psy_lift_numbers_porcessed = "gesmemories/snd/mp3/mnd_psy_lift_numbers_porcessed.mp3"
    $ mnd_enertity = "gesmemories/snd/mp3/mnd_enertity.mp3"
    $ mnd_intig_hvatit = "gesmemories/snd/mp3/mnd_intig_hvatit.mp3"
    $ mnd_college = "gesmemories/snd/mp3/mnd_college.mp3"
    $ mnd_death_theme = "gesmemories/snd/mp3/mnd_death_theme.mp3"
    $ mnd_survive_hotel_terror = "gesmemories/snd/mp3/mnd_survive_hotel_terror.mp3"
    $ mnd_faster = "gesmemories/snd/mp3/mnd_faster.mp3"
    $ mnd_slowerfight = "gesmemories/snd/mp3/mnd_slowerfight.mp3"
    $ mnd_introreal = "gesmemories/snd/mp3/mnd_introreal.mp3"
    $ mnd_nmrinh7 = "gesmemories/snd/mp3/mnd_nmrinh7.ogg"
    $ mnd_ges_tears = "gesmemories/snd/mp3/mnd_ges_tears.mp3"
    $ mnd_nmrih1 = "gesmemories/snd/mp3/mnd_nmrih1.ogg"
    $ mnd_sled_cut = "gesmemories/snd/mp3/mnd_sled_cut.mp3"
    $ mnd_gluhar_z_mix = "gesmemories/snd/mp3/mnd_gluhar_z_mix.mp3"
    $ mnd_gluhar_z = "gesmemories/snd/mp3/mnd_gluhar_z.mp3"
    $ mnd_karpov_1 = "gesmemories/snd/mp3/mnd_karpov_1.mp3"
    $ mnd_kapdon = "gesmemories/snd/mp3/mnd_kapdon.mp3"
    $ outofit1 = "gesmemories/snd/mp3/outofit1.mp3"
    $ mnd_gluhar_utro = "gesmemories/snd/mp3/mnd_gluhar_utro.mp3"
    $ mnd_arahna_theme_2 = "gesmemories/snd/mp3/mnd_arahna_theme_2.mp3"
    $ mnd_memories_1 = "gesmemories/snd/mp3/mnd_memories_1.mp3"
    $ mnd_tarakan_joke_1 = "gesmemories/snd/mp3/mnd_tarakan_joke_1.mp3"
    $ mnd_rain_stand_a_window = "gesmemories/snd/mp3/mnd_rain_stand_a_window.mp3"
    $ mnd_cityend = "gesmemories/snd/mp3/mnd_cityend.mp3"
    $ mnd_chap_logo_new = "gesmemories/snd/mp3/mnd_chap_logo_new.mp3"
    $ mnd_hurt_cut = "gesmemories/snd/mp3/mnd_hurt_cut.mp3"
    $ mnd_new_menu_music = "gesmemories/snd/mp3/mnd_new_menu_music.mp3"
    $ mnd_aom = "gesmemories/snd/mp3/mnd_aom.mp3"
    $ mnd_riptide_1 = "gesmemories/snd/mp3/mnd_riptide_1.mp3"
    $ mnd_asia = "gesmemories/snd/mp3/mnd_asia.mp3"
    $ mnd_karpov_2_ff = "gesmemories/snd/mp3/mnd_karpov_2_ff.mp3"
    $ mnd_arahna_full = "gesmemories/snd/mp3/mnd_arahna_full.mp3"
    $ mnd_hurt = "gesmemories/snd/mp3/mnd_hurt.mp3"
    $ mnd_mind_the_garp = "gesmemories/snd/mp3/mnd_mind_the_garp.mp3"
    $ mnd_khait_theme = "gesmemories/snd/mp3/mnd_khait_theme.mp3"
    $ mnd_ronberg_goodbye = "gesmemories/snd/mp3/mnd_ronberg_goodbye.mp3"
    $ mnd_luci_theme = "gesmemories/snd/mp3/mnd_luci_theme.mp3"
    $ mnd_hb_mus_1 = "gesmemories/snd/mp3/mnd_hb_mus_1.ogg"
    $ mnd_credits = "gesmemories/snd/mp3/mnd_credits.mp3"
    $ mnd_just_like_sleep = "gesmemories/snd/mp3/mnd_just_like_sleep.ogg"
    $ mnd_just_like_sleep_short = "gesmemories/snd/mp3/mnd_just_like_sleep_short.ogg"
    $ mnd_recollection = "gesmemories/snd/mp3/mnd_recollection.mp3"
    $ mnd_13_hi_cab_music = "gesmemories/snd/mp3/mnd_13_hi_cab_music.mp3"
    $ mnd_final_credit_theme = "gesmemories/snd/mp3/mnd_final_credit_theme.mp3"
    $ mnd_finale_credits = "gesmemories/snd/mp3/mnd_finale_credits.mp3"
    $ mnd_tv_dance_music = "gesmemories/snd/mp3/mnd_tv_dance_music.mp3"
    $ mnd_u_z_best = "gesmemories/snd/mp3/mnd_u_z_best.mp3"
    $ mnd_finale_credits_cut = "gesmemories/snd/mp3/mnd_finale_credits_cut.mp3"
    $ mnd_a3_menu = "gesmemories/snd/mp3/mnd_a3_menu.mp3"
    $ mnd_fallen = "gesmemories/snd/mp3/mnd_fallen.mp3"
    $ mnd_i_got_5_on_it = "gesmemories/snd/mp3/mnd_i_got_5_on_it.mp3"
    $ mnd_times_inst = "gesmemories/snd/mp3/mnd_times_inst.mp3"
    $ mnd_final_theme = "gesmemories/snd/mp3/mnd_final_theme.mp3"
    $ mnd_amb_mix_1 = "gesmemories/snd/mp3/mnd_amb_mix_1.mp3"
    $ mnd_kad = "gesmemories/snd/mp3/mnd_kad.mp3"
    $ mnd_harts_theme_17_1 = "gesmemories/snd/mp3/mnd_harts_theme_17_1.mp3"
    $ mnd_myimmortal = "gesmemories/snd/mp3/mnd_myimmortal.mp3"
    $ mnd_c17h27no2 = "gesmemories/snd/mp3/mnd_c17h27no2.mp3"
    $ mnd_aft_long_day = "gesmemories/snd/mp3/mnd_aft_long_day.mp3"
    $ mnd_sexygitl = "gesmemories/snd/mp3/mnd_sexygitl.mp3"
    $ mnd_luciena_theme_2 = "gesmemories/snd/mp3/mnd_luciena_theme_2.mp3"
    $ mnd_rainagain = "gesmemories/snd/mp3/mnd_rainagain.mp3"
    $ mnd_brandon_gp = "gesmemories/snd/mp3/mnd_brandon_gp.mp3"
    $ mnd_monage_daydream = "gesmemories/snd/mp3/mnd_monage_daydream.mp3"
    $ mnd_u_will_not_survive = "gesmemories/snd/mp3/mnd_u_will_not_survive.mp3"
    $ mnd_scrxlrd = "gesmemories/snd/mp3/mnd_scrxlrd.mp3"
    $ mnd_luciena_kiss = "gesmemories/snd/mp3/mnd_luciena_kiss.mp3"
    $ mnd_ningyou = "gesmemories/snd/mp3/mnd_ningyou.mp3"
    $ mnd_tape_1 = "gesmemories/snd/mp3/mnd_tape_1.mp3"
    $ mnd_tape_3 = "gesmemories/snd/mp3/mnd_tape_3.mp3"
    $ mnd_tape_7 = "gesmemories/snd/mp3/mnd_tape_7.mp3"
    $ mnd_nebesa = "gesmemories/snd/mp3/mnd_nebesa.mp3"
    $ mnd_final_close_title = "gesmemories/snd/mp3/mnd_final_close_title.mp3"
    $ mnd_all_its_over = "gesmemories/snd/mp3/mnd_all_its_over.mp3"
    $ mnd_disheartened = "gesmemories/snd/mp3/mnd_disheartened.mp3"
    $ mnd_forest_end = "gesmemories/snd/mp3/mnd_forest_end.mp3"
    $ mnd_arahna_theme = "gesmemories/snd/mp3/mnd_arahna_theme.mp3"
    $ mnd_polar_day = "gesmemories/snd/mp3/mnd_polar_day.mp3"
    $ mnd_anxiety = "gesmemories/snd/mp3/mnd_anxiety.mp3"
    $ mnd_mms_final = "gesmemories/snd/mp3/mnd_mms_final.mp3"
    $ mnd_aft_end_scene_music = "gesmemories/snd/mp3/mnd_aft_end_scene_music.mp3"
    $ mnd_smert_song = "gesmemories/snd/mp3/mnd_smert_song.mp3"


    $ rainstandwindow = "gesmemories/snd/ambient/rainstandwindow.mp3"
    $ mndrainstr = "gesmemories/snd/ambient/mndrainstr.mp3"
    $ rainingarage = "gesmemories/snd/ambient/rainingarage.wav"
    $ mndsea = "gesmemories/snd/ambient/mndsea.mp3"
    $ mndambosen = "gesmemories/snd/ambient/mndambosen.mp3"
    $ mndambbirdsd = "gesmemories/snd/ambient/mndambbirdsd.mp3"
    $ mndambdayforest = "gesmemories/snd/ambient/mndambdayforest.mp3"
    $ mndfireamb = "gesmemories/snd/ambient/mndfireamb.mp3"
    $ mndhavyrainforest = "gesmemories/snd/ambient/mndhavyrainforest.mp3"
    $ mndriveramb = "gesmemories/snd/ambient/mndriveramb.mp3"
    $ mndwolfs1 = "gesmemories/snd/ambient/mndwolfs1.mp3"
    $ mndforestn = "gesmemories/snd/ambient/mndforestn.mp3"
    $ mndvih1 = "gesmemories/snd/ambient/mndvih1.mp3"
    $ mndvih2 = "gesmemories/snd/ambient/mndvih2.mp3"
    $ mndforestmamb = "gesmemories/snd/ambient/mndforestmamb.mp3"
    $ mndwolfsplays = "gesmemories/snd/ambient/mndwolfsplays.mp3"
    $ mndwolfangramb = "gesmemories/snd/ambient/mndwolfangramb.mp3"
    $ mndfightwolf = "gesmemories/snd/ambient/mndfightwolf.mp3"
    $ mndfloortash = "gesmemories/snd/ambient/mndfloortash.mp3"
    $ mndeatmeetten = "gesmemories/snd/ambient/mndeatmeetten.mp3"
    $ mnd_coridors_ambience_1 = "gesmemories/snd/ambient/mnd_coridors_ambience_1.wav"
    $ mnd_coridors_ambience_2 = "gesmemories/snd/ambient/mnd_coridors_ambience_2.ogg"
    $ mnd_coridors_ambience_3 = "gesmemories/snd/ambient/mnd_coridors_ambience_3.wav"
    $ mnd_coridors_ambience_4 = "gesmemories/snd/ambient/mnd_coridors_ambience_4.mp3"
    $ mnd_floor_amb = "gesmemories/snd/ambient/mnd_floor_amb.mp3"
    $ mnd_liya_good_wispers = "gesmemories/snd/ambient/mnd_liya_good_wispers.mp3"
    $ mnd_rain_voice_amb = "gesmemories/snd/ambient/mnd_rain_voice_amb.mp3"


    $ mndroll = "gesmemories/snd/sfx/mndroll.wav"
    $ mndgrom = "gesmemories/snd/sfx/mndgrom.wav"
    $ mndhallo = "gesmemories/snd/sfx/mndhallo.ogg"
    $ opdoor1 = "gesmemories/snd/sfx/opdoor1.wav"
    $ paper = "gesmemories/snd/sfx/paper.wav"
    $ mndbed = "gesmemories/snd/sfx/mndbed.mp3"
    $ w810 = "gesmemories/snd/sfx/w810.mp3"
    $ phbutton = "gesmemories/snd/sfx/phbutton.wav"
    $ cldoor1 = "gesmemories/snd/sfx/cldoor1.wav"
    $ latch1 = "gesmemories/snd/sfx/latch1.wav"
    $ btn1 = "gesmemories/snd/sfx/btn1.wav"
    $ mndliftmove = "gesmemories/snd/sfx/mndliftmove.mp3"
    $ hrddoor1 = "gesmemories/snd/sfx/hrddoor1.wav"
    $ woodstep = "gesmemories/snd/sfx/woodstep.mp3"
    $ phgudok = "gesmemories/snd/sfx/phgudok.wav"
    $ mnddoorcol = "gesmemories/snd/sfx/mnddoorcol.mp3"
    $ mndwatsteps = "gesmemories/snd/sfx/mndwatsteps.mp3"
    $ attempt = "gesmemories/snd/sfx/attempt.wav"
    $ mndhlop = "gesmemories/snd/sfx/mndhlop.mp3"
    $ carride = "gesmemories/snd/sfx/carride.mp3"
    $ cartorm = "gesmemories/snd/sfx/cartorm.wav"
    $ sloweff = "gesmemories/snd/sfx/sloweff.mp3"
    $ raise_1 = "gesmemories/snd/sfx/raise_1.wav"
    $ foll = "gesmemories/snd/sfx/foll.wav"
    $ injekt = "gesmemories/snd/sfx/injekt.wav"
    $ flashback = "gesmemories/snd/sfx/flashback.ogg"
    $ screbdoor = "gesmemories/snd/sfx/screbdoor.mp3"
    $ doorknok = "gesmemories/snd/sfx/doorknok.mp3"
    $ eating = "gesmemories/snd/sfx/eating.ogg"
    $ watherin = "gesmemories/snd/sfx/watherin.wav"
    $ alkodrink = "gesmemories/snd/sfx/alkodrink.ogg"
    $ hrustbone = "gesmemories/snd/sfx/hrustbone.mp3"
    $ step_wather = "gesmemories/snd/sfx/step_wather.mp3"
    $ psystart = "gesmemories/snd/sfx/psystart.ogg"
    $ psyvoices = "gesmemories/snd/sfx/psyvoices.mp3"
    $ glass_break = "gesmemories/snd/sfx/glass_break.mp3"
    $ crashglass = "gesmemories/snd/sfx/crashglass.mp3"
    $ olddoor = "gesmemories/snd/sfx/olddoor.wav"
    $ door1 = "gesmemories/snd/sfx/door1.wav"
    $ narko_dream = "gesmemories/snd/sfx/narko_dream.wav"
    $ wailchaircrash = "gesmemories/snd/sfx/wailchaircrash.ogg"
    $ dam1 = "gesmemories/snd/sfx/dam1.wav"
    $ knifehard = "gesmemories/snd/sfx/knifehard.wav"
    $ woodskr = "gesmemories/snd/sfx/woodskr.ogg"
    $ mndpaper = "gesmemories/snd/sfx/mndpaper.wav"
    $ olddoor1 = "gesmemories/snd/sfx/olddoor.wav"
    $ metalstack = "gesmemories/snd/sfx/metalstack.ogg"
    $ doorrageop = "gesmemories/snd/sfx/doorrageop.wav"
    $ gurgle_loop1 = "gesmemories/snd/sfx/gurgle_loop1.wav"
    $ smallmedkit1 = "gesmemories/snd/sfx/smallmedkit1.wav"
    $ mndhorscr1 = "gesmemories/snd/sfx/mndhorscr1.mp3"
    $ mndboom1 = "gesmemories/snd/sfx/mndboom1.mp3"
    $ mndfirescream  = "gesmemories/snd/sfx/mndfirescream .mp3"
    $ mndhitw1 = "gesmemories/snd/sfx/mndhitw1.mp3"
    $ mndheavygrom = "gesmemories/snd/sfx/mndheavygrom.mp3"
    $ mndwolfvoy = "gesmemories/snd/sfx/mndwolfvoy.mp3"
    $ mndwolfangr = "gesmemories/snd/sfx/mndwolfangr.mp3"
    $ mndhitw1 = "gesmemories/snd/sfx/mndhitw1.mp3"
    $ mndheavygrom = "gesmemories/snd/sfx/mndheavygrom.mp3"
    $ mndwolfvoy = "gesmemories/snd/sfx/mndwolfvoy.mp3"
    $ mndwolfangr = "gesmemories/snd/sfx/mndwolfangr.mp3"
    $ mndcrowvoise1 = "gesmemories/snd/sfx/mndcrowvoise1.mp3"
    $ mndwolfhurt = "gesmemories/snd/sfx/mndwolfhurt.mp3"
    $ mndlitlewolfs = "gesmemories/snd/sfx/mndlitlewolfs.mp3"
    $ mndwolfhit = "gesmemories/snd/sfx/mndwolfhit.mp3"
    $ mndtenobr = "gesmemories/snd/sfx/mndtenobr.mp3"
    $ mndtenroar = "gesmemories/snd/sfx/mndtenroar.mp3"
    $ mndphoto = "gesmemories/snd/sfx/mndphoto.mp3"
    $ mnddeathscream = "gesmemories/snd/sfx/mnddeathscream.mp3"
    $ mndsplash = "gesmemories/snd/sfx/mndsplash.mp3"
    $ mnddcls2 = "gesmemories/snd/sfx/mnddcls2.mp3"
    $ mnddoorop2 = "gesmemories/snd/sfx/mnddoorop2.mp3"
    $ mndhitcof = "gesmemories/snd/sfx/mndhitcof.mp3"
    $ mndlutch = "gesmemories/snd/sfx/mndlutch.wav"
    $ mndmetalclose = "gesmemories/snd/sfx/mndmetalclose.ogg"
    $ mndmetalclose1 = "gesmemories/snd/sfx/mndmetalclose1.ogg"
    $ mndpunch = "gesmemories/snd/sfx/mndpunch.wav"
    $ mndbuttonclickrelease = "gesmemories/snd/sfx/mndbuttonclickrelease.wav"
    $ mndknife_slash1 = "gesmemories/snd/sfx/mndknife_slash1.wav"
    $ mndknife_slash3 = "gesmemories/snd/sfx/mndknife_slash3.wav"
    $ mndknife_stab3 = "gesmemories/snd/sfx/mndknife_stab3.wav"
    $ mndpiano = "gesmemories/snd/sfx/mndpiano.wav"
    $ sub_kettei2 = "gesmemories/snd/sfx/sub_kettei2.ogg"
    $ mnd_4_button_clik = "gesmemories/snd/sfx/mnd_4_button_clik.ogg"
    $ mnd_5_button_clik = "gesmemories/snd/sfx/mnd_5_button_clik.ogg"
    $ mnd_metal_breack_start = "gesmemories/snd/sfx/mnd_metal_breack_start.wav"
    $ mdn_lift_psy_stop_hard = "gesmemories/snd/sfx/mdn_lift_psy_stop_hard.wav"
    $ mnd_electro_1 = "gesmemories/snd/sfx/mnd_electro_1.wav"
    $ mdn_lift_psy_stop = "gesmemories/snd/sfx/mdn_lift_psy_stop.wav"
    $ mnd_metal_plank_greak_1 = "gesmemories/snd/sfx/mnd_metal_plank_greak_1.wav"
    $ mnd_tv_noise = "gesmemories/snd/sfx/mnd_tv_noise.wav"
    $ mnd_car_ride_closer = "gesmemories/snd/sfx/mnd_car_ride_closer.mp3"
    $ mnd_piano_lie_2 = "gesmemories/snd/sfx/mnd_piano_lie_2.ogg"
    $ mnd_piano_lie_1 = "gesmemories/snd/sfx/mnd_piano_lie_1.ogg"
    $ mnd_lift_doors_open = "gesmemories/snd/sfx/mnd_lift_doors_open.wav"
    $ mnd_drip = "gesmemories/snd/sfx/mnd_drip.wav"
    $ mnd_lift_fall_down = "gesmemories/snd/sfx/mnd_lift_fall_down.wav"
    $ mnd_apartmentholecrash1 = "gesmemories/snd/sfx/mnd_apartmentholecrash1.wav"
    $ mnd_big_wood_droor_scr = "gesmemories/snd/sfx/mnd_big_wood_droor_scr.ogg"
    $ mnd_latchlocked1 = "gesmemories/snd/sfx/mnd_latchlocked1.wav"
    $ mnd_axe_hit = "gesmemories/snd/sfx/mnd_axe_hit.ogg"
    $ mnd_axe_hit_2 = "gesmemories/snd/sfx/mnd_axe_hit_2.wav"
    $ mnd_zippo_open = "gesmemories/snd/sfx/mnd_zippo_open.wav"
    $ mnd_zippo_strike = "gesmemories/snd/sfx/mnd_zippo_strike.wav"
    $ mnd_zippo_flame = "gesmemories/snd/sfx/mnd_zippo_flame.wav"
    $ mnd_smoke_g = "gesmemories/snd/sfx/mnd_smoke_g.mp3"
    $ mnd_zippo_close = "gesmemories/snd/sfx/mnd_zippo_close.wav"
    $ mnd_zombie_head_explode_03 = "gesmemories/snd/sfx/mnd_zombie_head_explode_03.wav"
    $ mnd_faster_alert1 = "gesmemories/snd/sfx/mnd_faster_alert1.wav"
    $ mnd_faster_death = "gesmemories/snd/sfx/mnd_faster_death.wav"
    $ mnd_faster_pain = "gesmemories/snd/sfx/mnd_faster_pain.wav"
    $ mnd_kabluki_slow = "gesmemories/snd/sfx/mnd_kabluki_slow.mp3"
    $ mnd_jason = "gesmemories/snd/sfx/mnd_jason.wav"
    $ mnd_steps = "gesmemories/snd/sfx/mnd_steps.wav"
    $ mnd_metallicrustle = "gesmemories/snd/sfx/mnd_metallicrustle.wav"
    $ mnd_padl_turn = "gesmemories/snd/sfx/mnd_padl_turn.wav"
    $ mnd_padl_unlock = "gesmemories/snd/sfx/mnd_padl_unlock.wav"
    $ mnd_doormove1 = "gesmemories/snd/sfx/mnd_doormove1.wav"
    $ mnd_gay_do_break = "gesmemories/snd/sfx/mnd_gay_do_break.wav"
    $ mnd_valve = "gesmemories/snd/sfx/mnd_valve.wav"
    $ mnd_asy_startle = "gesmemories/snd/sfx/mnd_asy_startle.wav"
    $ mnd_kranwather = "gesmemories/snd/sfx/mnd_kranwather.mp3"
    $ mnd_water_outside = "gesmemories/snd/sfx/mnd_water_outside.mp3"
    $ mnd_blev_started = "gesmemories/snd/sfx/mnd_blev_started.wav"
    $ mnd_asy_door_close2 = "gesmemories/snd/sfx/mnd_asy_door_close2.wav"
    $ mnd_asy_door_open3 = "gesmemories/snd/sfx/mnd_asy_door_open3.wav"
    $ mnd_lever5 = "gesmemories/snd/sfx/mnd_lever5.wav"
    $ mnd_lever1 = "gesmemories/snd/sfx/mnd_lever1.wav"
    $ mnd_ropeplace = "gesmemories/snd/sfx/mnd_ropeplace.wav"
    $ mnd_boiler_start = "gesmemories/snd/sfx/mnd_boiler_start.wav"
    $ mnd_hitmiss_1 = "gesmemories/snd/sfx/mnd_hitmiss_1.ogg"
    $ mnd_hitmiss_2 = "gesmemories/snd/sfx/mnd_hitmiss_2.ogg"
    $ mnd_ten_gitara_sound = "gesmemories/snd/sfx/mnd_ten_gitara_sound.mp3"
    $ mnd_door_signal = "gesmemories/snd/sfx/mnd_door_signal.mp3"
    $ mnd_glass_bottle = "gesmemories/snd/sfx/mnd_glass_bottle.mp3"
    $ mnd_chap_logo_new2 = "gesmemories/snd/sfx/mnd_chap_logo_new2.mp3"
    $ mnd_door_col = "gesmemories/snd/sfx/mnd_door_col.mp3"
    $ mnd_tv_termin_snd = "gesmemories/snd/sfx/mnd_tv_termin_snd.mp3"
    $ mnd_a4_chaplog = "gesmemories/snd/sfx/mnd_a4_chaplog.mp3"
    $ mnd_r_creak = "gesmemories/snd/sfx/mnd_r_creak.wav"
    $ mnd_r_creak2 = "gesmemories/snd/sfx/mnd_r_creak2.ogg"
    $ mnd_r_vine = "gesmemories/snd/sfx/mnd_r_vine.mp3"
    $ mnd_first_act_logos = "gesmemories/snd/sfx/mnd_first_act_logos.mp3"



    $ liyav1 = "gesmemories/snd/vocal/liya/liyav1.mp3"
    $ mndlml = "gesmemories/snd/vocal/liya/mndlml.wav"
    $ bloodkashl = "gesmemories/snd/vocal/vas/bloodkashl.wav"
    $ hardbreath = "gesmemories/snd/vocal/vas/hardbreath.wav"
    $ hightpain1 = "gesmemories/snd/vocal/vas/hightpain1.wav"
    $ hightpain2 = "gesmemories/snd/vocal/vas/hightpain2.wav"
    $ pained = "gesmemories/snd/vocal/vas/pained.wav"
    $ vascry = "gesmemories/snd/vocal/vas/vascry.wav"
    $ vaspain1 = "gesmemories/snd/vocal/vas/vaspain1.wav"
    $ vaspain2 = "gesmemories/snd/vocal/vas/vaspain2.wav"
    $ mndkashl = "gesmemories/snd/vocal/vas/mndkashl.mp3"
    $ wsl = "gesmemories/snd/vocal/womvoise/wsl.wav"
    $ mndvzdoh = "gesmemories/snd/vocal/vas/mndvzdoh.wav"
    $ vasshortpl = "gesmemories/snd/vocal/vas/vasshortpl.mp3"
    $ vasist = "gesmemories/snd/vocal/vas/vasist.mp3"
    $ mndvpl = "gesmemories/snd/vocal/vas/mndvpl.mp3"
    $ mndpanic1 = "gesmemories/snd/vocal/vas/mndpanic1.wav"
    $ mndpanic2 = "gesmemories/snd/vocal/vas/mndpanic2.wav"
    $ mndcombo = "gesmemories/snd/vocal/vas/mndcombo.wav"
    $ whl = "gesmemories/snd/vocal/womvoise/whl.wav"
    $ mndvnl = "gesmemories/snd/vocal/vas/mndvnl.ogg"
    $ mnddrink = "gesmemories/snd/vocal/vas/mnddrink.ogg"
    $ mndblev = "gesmemories/snd/vocal/vas/mndblev.wav"
    $ mndkidboyscr = "gesmemories/snd/vocal/man/mndkidboyscr.mp3"
    $ mndwakeup = "gesmemories/snd/vocal/vas/mndwakeup.mp3"
    $ mndkidboyscr = "gesmemories/snd/vocal/man/mndkidboyscr.mp3"
    $ mndwakeup = "gesmemories/snd/vocal/vas/mndwakeup.wav"
    $ mndch4logo = "gesmemories/snd/vocal/vas/mndch4logo.mp3"
    $ mndarlau = "gesmemories/snd/vocal/womvoise/mndarlau.mp3"
    $ mndvaspsyl = "gesmemories/snd/vocal/vas/mndvaspsyl.mp3"
    $ mnd_panic_breath = "gesmemories/snd/vocal/vas/mnd_panic_breath.wav"
    $ mnd_vas_kalustro_breath = "gesmemories/snd/vocal/vas/mnd_vas_kalustro_breath.wav"
    $ vaspain3 = "gesmemories/snd/vocal/vas/vaspain3.wav"
    $ mnd_vas_afther_wather = "gesmemories/snd/vocal/vas/mnd_vas_afther_wather.wav"
    $ mnd_vas_fast_breath = "gesmemories/snd/vocal/vas/mnd_vas_fast_breath.wav"
    $ mnd_vas_usilie = "gesmemories/snd/vocal/vas/mnd_vas_usilie.wav"
    $ mnd_vas_dead = "gesmemories/snd/vocal/vas/mnd_vas_dead.wav"
    $ mnd_heart_bit = "gesmemories/snd/vocal/vas/mnd_heart_bit.ogg"
    $ mnd_out_of_my_head = "gesmemories/snd/vocal/vas/mnd_out_of_my_head.ogg"
    $ mnd_get_down = "gesmemories/snd/vocal/vas/mnd_get_down.wav"
    $ mnd_get_up_14 = "gesmemories/snd/vocal/vas/mnd_get_up_14.wav"
    $ mnd_swing_1 = "gesmemories/snd/vocal/vas/mnd_swing_1.wav"
    $ mnd_swing_2 = "gesmemories/snd/vocal/vas/mnd_swing_2.wav"


    $ mnd_psyvas_dyshish = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_dyshish.mp3"
    $ mnd_psyvas_est_kto = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_est_kto.mp3"
    $ mnd_psyvas_idu_na_strah = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_idu_na_strah.mp3"
    $ mnd_psyvas_istochaesh_strah = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_istochaesh_strah.mp3"
    $ mnd_psyvas_strashno = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_strashno.mp3"
    $ mnd_psyvas_tesno = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_tesno.mp3"
    $ mnd_psyvas_ti_mena_slishish = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_ti_mena_slishish.mp3"
    $ mnd_psyvas_ti_mena_vidish = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_ti_mena_vidish.mp3"
    $ mnd_psyvas_ti_zdes = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_ti_zdes.mp3"
    $ mnd_psyvas_ya_znau_gde_ti = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_ya_znau_gde_ti.mp3"
    $ mnd_psyvas_zubi = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_zubi.mp3"
    $ mnd_zachem_ubegaesh = "gesmemories/snd/vocal/vas/pshychotalk/mnd_zachem_ubegaesh.mp3"



    $ mnd_voice_in_head_1 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_1.mp3"
    $ mnd_voice_in_head_2 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_2.mp3"
    $ mnd_voice_in_head_3 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_3.mp3"
    $ mnd_voice_in_head_4 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_4.mp3"
    $ mnd_voice_in_head_5 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_5.mp3"
    $ mnd_voice_in_head_6 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_6.mp3"
    $ mnd_voice_in_head_7 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_7.mp3"
    $ mnd_voice_in_head_8 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_8.mp3"
    $ mnd_try_voice_1 = "gesmemories/snd/vocal/headvoice/mnd_try_voice_1.mp3"
    $ mnd_try_voice_2 = "gesmemories/snd/vocal/headvoice/mnd_try_voice_2.mp3"
    $ mnd_try_voice_3 = "gesmemories/snd/vocal/headvoice/mnd_try_voice_3.mp3"
    $ mnd_try_voice_4 = "gesmemories/snd/vocal/headvoice/mnd_try_voice_4.mp3"
    $ mnd_try_voise_help_1 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_1.mp3"
    $ mnd_try_voise_help_2 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_2.mp3"
    $ mnd_try_voise_help_3 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_3.mp3"
    $ mnd_try_voise_help_4 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_4.mp3"
    $ mnd_try_voise_help_5 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_5.mp3"
    $ mnd_try_voise_help_6 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_6.mp3"
    $ mnd_try_voise_help_7 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_7.mp3"
    $ mnd_try_voise_help_8 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_8.mp3"
    $ mnd_try_voise_help_9 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_9.mp3"
    $ mnd_try_voise_help_10 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_10.mp3"



    $ mndpsyeff1 = "gesmemories/snd/psy/mndpsyeff1.mp3"
    $ mndpsyamb1 = "gesmemories/snd/psy/mndpsyamb1.mp3"
    $ mndpsyamb2 = "gesmemories/snd/psy/mndpsyamb2.mp3"
    $ mndcornightvoise = "gesmemories/snd/psy/mndcornightvoise.mp3"
    $ mndwomanpsyl = "gesmemories/snd/psy/mndwomanpsyl.mp3"
    $ mndnejdan = "gesmemories/snd/psy/mndnejdan.mp3"
    $ mndlitlemonster = "gesmemories/snd/psy/mndlitlemonster.mp3"
    $ mndstrangemusic = "gesmemories/snd/psy/mndstrangemusic.mp3"
    $ mndtenkiller1 = "gesmemories/snd/psy/mndtenkiller1.mp3"
    $ mndtekillerl = "gesmemories/snd/psy/mndtekillerl.mp3"
    $ mndtenroar = "gesmemories/snd/psy/mndtenroar.mp3"
    $ mnd_snuff666 = "gesmemories/snd/psy/mnd_snuff666.mp3"
    $ mnd_hit_final_psy = "gesmemories/snd/psy/mnd_hit_final_psy.mp3"
    $ mnd_metal_breack_breack = "gesmemories/snd/psy/mnd_metal_breack_breack.wav"
    $ mnd_psy_fast_1 = "gesmemories/snd/psy/mnd_psy_fast_1.wav"
    $ mnd_psy_fast_2 = "gesmemories/snd/psy/mnd_psy_fast_2.wav"
    $ mnd_psy_fast_3 = "gesmemories/snd/psy/mnd_psy_fast_3.wav"
    $ mnd_hit_cof = "gesmemories/snd/psy/mnd_hit_cof.mp3"
    $ mnd_hum_song_2 = "gesmemories/snd/psy/mnd_hum_song_2.ogg"
    $ mnd_hum_song_1 = "gesmemories/snd/psy/mnd_hum_song_1.ogg"
    $ mnd_psy_lift_strange_noise_1 = "gesmemories/snd/psy/mnd_psy_lift_strange_noise_1.wav"
    $ mnd_psy_lift_strange_noise_2 = "gesmemories/snd/psy/mnd_psy_lift_strange_noise_2.wav"
    $ mnd_psy_lift_strange_noise_3 = "gesmemories/snd/psy/mnd_psy_lift_strange_noise_3.wav"
    $ mnd_psy_lift_strange_noise_4 = "gesmemories/snd/psy/mnd_psy_lift_strange_noise_4.wav"
    $ mnd_psy_lift_strange_noise_5 = "gesmemories/snd/psy/mnd_psy_lift_strange_noise_5.wav"
    $ mnd_lift_body_drop = "gesmemories/snd/psy/mnd_lift_body_drop.wav"
    $ mnd_psyhosis_vas_amb = "gesmemories/snd/psy/mnd_psyhosis_vas_amb.mp3"
    $ mnd_comone_over_here = "gesmemories/snd/psy/mnd_comone_over_here.wav"
    $ mnd_psy_lift_strange_noise_6 = "gesmemories/snd/psy/mnd_psy_lift_strange_noise_6.wav"
    $ mnd_rumpelcutscene = "gesmemories/snd/psy/mnd_rumpelcutscene.wav"
    $ mnd_church_bell = "gesmemories/snd/psy/mnd_church_bell.ogg"
    $ mnd_church_monks = "gesmemories/snd/psy/mnd_church_monks.ogg"
    $ mnd_moan_2 = "gesmemories/snd/psy/mnd_moan_2.ogg"
    $ mnd_lost_squeak_1 = "gesmemories/snd/psy/mnd_lost_squeak_1.ogg"
    $ mnd_lost_rdm_3 = "gesmemories/snd/psy/mnd_lost_rdm_3.ogg"
    $ mnd_asy_crying = "gesmemories/snd/psy/mnd_asy_crying.wav"
    $ mnd_lost_blinds = "gesmemories/snd/psy/mnd_lost_blinds.wav"
    $ mnd_scream_amb_1 = "gesmemories/snd/psy/mnd_scream_amb_1.wav"
    $ mnd_wood_door_creac_10 = "gesmemories/snd/psy/mnd_wood_door_creac_10.wav"
    $ mnd_dredka_1 = "gesmemories/snd/psy/mnd_dredka_1.mp3"
    $ mnd_strangle_strangle1 = "gesmemories/snd/psy/mnd_strangle_strangle1.wav"
    $ mnd_unsafe = "gesmemories/snd/psy/mnd_unsafe.mp3"
    $ mnd_c9_voises_1 = "gesmemories/snd/psy/mnd_c9_voises_1.wav"
    $ mnd_c9_voises_2 = "gesmemories/snd/psy/mnd_c9_voises_2.wav"
    $ mnd_horror_hit = "gesmemories/snd/psy/mnd_horror_hit.wav"
    $ mnd_shove = "gesmemories/snd/psy/mnd_shove.wav"
    $ mnd_takemetalsmall = "gesmemories/snd/psy/mnd_takemetalsmall.wav"
    $ mnd_tape_noise = "gesmemories/snd/psy/mnd_tape_noise.mp3"
    $ mnd_tape_load = "gesmemories/snd/psy/mnd_tape_load.wav"
    $ mnd_tape_pickup = "gesmemories/snd/psy/mnd_tape_pickup.wav"
    $ mnd_tape_insert = "gesmemories/snd/psy/mnd_tape_insert.wav"
    $ mnd_tape_off = "gesmemories/snd/psy/mnd_tape_off.mp3"
    $ mnd_girlpsylau = "gesmemories/snd/psy/mnd_girlpsylau.ogg"
    $ mnd_open_center_door = "gesmemories/snd/psy/mnd_open_center_door.wav"
    $ mnd_memory_murder_1 = "gesmemories/snd/psy/mnd_memory_murder_1.mp3"
    $ mnd_psy_music_13_1 = "gesmemories/snd/psy/mnd_psy_music_13_1.mp3"
    $ mnd_psy_music_13_2 = "gesmemories/snd/psy/mnd_psy_music_13_2.mp3"
    $ mnd_psyhosis_fear_allert_1 = "gesmemories/snd/psy/mnd_psyhosis_fear_allert_1.wav"
    $ mnd_psyhosis_fear_allert_2 = "gesmemories/snd/psy/mnd_psyhosis_fear_allert_2.wav"
    


    $ flash_fast = Fade(0.25, 0, 0.75, color="#fff")
    $ flash_fast2 = Fade(0.05, 0, 0.35, color="#fff")
    $ flash_fast_red = Fade(0.25, 0, 0.75, color="#ff0000")
    $ flash_fast_red2 = Fade(0.05, 0, 0.75, color="#ff0000")




    image gesundheit_logos2 = Movie(play="gesmemories/image/logo/mnd_ges_bg.ogv", channel="movie", size=(1920, 1080))
    image gesundheit_logos = Movie(play="gesmemories/image/logo/new_logo.ogv", channel="movie", size=(1920, 1080))





    image bg doclog = "gesmemories/image/bg/doclog.png"
    image bg mndggroom = "gesmemories/image/bg/mndggroom.png"
    image bg mndrainbalk = "gesmemories/image/bg/mndrainbalk.png"
    image bg skyrain = "gesmemories/image/bg/skyrain.png"
    image bg busstoprain1 = "gesmemories/image/bg/busstoprain1.png"
    image bg rainofwindow = "gesmemories/image/bg/rainofwindow.png"
    image bg mndflowermark = "gesmemories/image/bg/mndflowermark.png"
    image bg mndrainaspd = "gesmemories/image/bg/mndrainaspd.png"
    image bg mndparkr = "gesmemories/image/bg/mndparkr.png"
    image bg 4roomd = "gesmemories/image/bg/4roomd.png"
    image bg 4roomn = "gesmemories/image/bg/4roomn.png"
    image bg ashollcor = "gesmemories/image/bg/ashollcor.jpg"
    image ashollcor_fp = "gesmemories/image/bg/ashollcor_fp.png"
    image carride_s = "gesmemories/image/bg/carride_s.png"
    image carride_fw = "gesmemories/image/bg/carride_fw.png"
    image bg damage4 = "gesmemories/image/bg/damage4.jpg"
    image bg darkdoor = "gesmemories/image/bg/darkdoor.jpg"
    image bg dreamrain = "gesmemories/image/bg/dreamrain.png"
    image bg farlights = "gesmemories/image/bg/farlights.png"
    image bg firstpsy = "gesmemories/image/bg/firstpsy.png"
    image bg lastkiss = "gesmemories/image/bg/lastkiss.png"
    image bg liliyainblood = "gesmemories/image/bg/liliyainblood.png"
    image bg lmdance = "gesmemories/image/bg/lmdance.png"
    image bg lmhouse = "gesmemories/image/bg/lmhouse.png"
    image bg lmplliya = "gesmemories/image/bg/lmplliya.png"
    image bg lmplsolo = "gesmemories/image/bg/lmplsolo.png"
    image bg lmrainsky = "gesmemories/image/bg/lmrainsky.png"
    image bg lmstolovka = "gesmemories/image/bg/lmstolovka.png"
    image bg lmsunrise = "gesmemories/image/bg/lmsunrise.png"
    image bg medcor = "gesmemories/image/bg/medcor.png"
    image bg medmorn = "gesmemories/image/bg/medmorn.png"
    image bg medpalat = "gesmemories/image/bg/medpalat.png"
    image bg mentaldushd = "gesmemories/image/bg/mentaldushd.png"
    image bg mentaldushn = "gesmemories/image/bg/mentaldushn.png"
    image bg mentalvannad = "gesmemories/image/bg/mentalvannad.png"
    image bg mentalvannan = "gesmemories/image/bg/mentalvannan.png"
    image bg mhnight = "gesmemories/image/bg/mhnight.png"
    image bg mndascor = "gesmemories/image/bg/mndascor.png"
    image bg mndascorn = "gesmemories/image/bg/mndascorn.png"
    image bg mndasstol = "gesmemories/image/bg/mndasstol.png"
    image bg mnday = "gesmemories/image/bg/mnday.png"
    image bg mndharts = "gesmemories/image/bg/mndharts.png"
    image bg mndlightindark1 = "gesmemories/image/bg/mndlightindark1.png"
    image bg mndlightindark2 = "gesmemories/image/bg/mndlightindark2.png"
    image bg mndstrrain2 = "gesmemories/image/bg/mndstrrain2.png"
    image bg mndwindrain = "gesmemories/image/bg/mndwindrain.png"
    image bg nsr1 = "gesmemories/image/bg/nsr1.png"
    image bg rainskyn = "gesmemories/image/bg/rainskyn.png"
    image bg rainsky = "gesmemories/image/bg/rainsky.png"
    image bg strnight1 = "gesmemories/image/bg/strnight1.png" 
    image bg vascrit = "gesmemories/image/bg/vascrit.png"
    image bg zihcab = "gesmemories/image/bg/zihcab.png"
    image bg finalfirstpsy = "gesmemories/image/bg/finalfirstpsy.png"
    image bg updream = "gesmemories/image/bg/updream.jpg"
    image bg llkstr = "gesmemories/image/bg/llkstr.png"
    image bg invanna = "gesmemories/image/bg/invanna.jpg"
    image bg mnd = "gesmemories/image/bg/mnd.png"
    image bg mndliftcabin = "gesmemories/image/bg/mndliftcabin.png"
    image bg linroom = "gesmemories/image/bg/linroom.png"
    image bg mndkd = "gesmemories/image/bg/mndkd.png"
    image bg mndkn = "gesmemories/image/bg/mndkn.png"
    image bg 10room = "gesmemories/image/bg/10room.png"
    image bg 8room = "gesmemories/image/bg/8room.png"
    image bg mndkd = "gesmemories/image/bg/mndkd.png"
    image bg mndkn = "gesmemories/image/bg/mndkn.png"
    image bg mndkn = "gesmemories/image/bg/mndkn.png"
    image bg mndpsydoor = "gesmemories/image/bg/mndpsydoor.png"
    image bg raiseforest = "gesmemories/image/bg/raiseforest.png"
    image bg mndaslight = "gesmemories/image/bg/mndaslight.png"
    image bg mnddushnight = "gesmemories/image/bg/mnddushnight.png"
    image bg mndblood1 = "gesmemories/image/bg/mndblood1.png"
    image bg mndbloodfull = "gesmemories/image/bg/mndbloodfull.png"
    image bg mndch2startbg = "gesmemories/image/bg/mndch2startbg.png"
    image bg mndoldshcroom = "gesmemories/image/bg/mndoldshcroom.jpg"
    image bg mndfire1 = "gesmemories/image/bg/mndfire1.png"
    image bg mndfire2 = "gesmemories/image/bg/mndfire2.png"
    image bg mndmshbg1 = "gesmemories/image/bg/mndmshbg1.png"
    image bg mndmshbg3 = "gesmemories/image/bg/mndmshbg3.png"
    image bg mndnightforest = "gesmemories/image/bg/mndnightforest.png"
    image bg mndwolfstay = "gesmemories/image/bg/mndwolfstay.png"
    image bg mndrunforest1 = "gesmemories/image/bg/mndrunforest1.png"
    image bg mndinwood = "gesmemories/image/bg/mndinwood.png"
    image bg mndforestm = "gesmemories/image/bg/mndforestm.png"
    image bg invannablood = "gesmemories/image/bg/invannablood.jpg"
    image bg mndwintforest = "gesmemories/image/bg/mndwintforest.png"
    image bg mndablock = "gesmemories/image/bg/mndablock.png"
    image bg mndmdoccab = "gesmemories/image/bg/mndmdoccab.png"
    image bg mndpitroom = "gesmemories/image/bg/mndpitroom.png"
    image bg 8roomold = "gesmemories/image/bg/8roomold.png"
    image bg 8roomoldn = "gesmemories/image/bg/8roomoldn.png"
    image bg mndoldcor = "gesmemories/image/bg/mndoldcor.png"
    image bg 1roomold = "gesmemories/image/bg/1roomold.png"
    image bg mndoldcornight = "gesmemories/image/bg/mndoldcornight.png"
    image bg mndredforest2 = "gesmemories/image/bg/mndredforest2.png"
    image bg mndforestpound = "gesmemories/image/bg/mndforestpound.png"
    image bg mndforsky = "gesmemories/image/bg/mndforsky.png"
    image mndfp_yh = "gesmemories/image/nightmare/mndfp_yh.png"
    image bg mndroofnoara = "gesmemories/image/bg/mndroofnoara.png"
    image bg mndwayroof = "gesmemories/image/bg/mndwayroof.png"
    image bg mndnonumberroomold = "gesmemories/image/bg/mndnonumberroomold.png"
    image bg mndolddush = "gesmemories/image/bg/mndolddush.png"
    image bg mnd_lift_no_light = "gesmemories/image/bg/mnd_lift_no_light.png"
    image bg mnd_car_night_dead = "gesmemories/image/bg/mnd_car_night_dead.png"
    image bg mnd_lift_psy_open_door = "gesmemories/image/bg/mnd_lift_psy_open_door.png"
    image bg mnd_grave_bg = "gesmemories/image/bg/mnd_grave_bg.png"
    image bg mnd_lift_psy_open_door_or = "gesmemories/image/bg/mnd_lift_psy_open_door_or.png"
    image bg mnd_lift_mine = "gesmemories/image/bg/mnd_lift_mine.png"
    image bg mnd_a2_ch7_cor_1 = "gesmemories/image/bg/mnd_a2_ch7_cor_1.png"
    image bg mnd_blood_drip_1 = "gesmemories/image/bg/mnd_blood_drip_1.png"
    image bg mnd_blood_drip_2 = "gesmemories/image/bg/mnd_blood_drip_2.png"
    image bg mnd_blood_drip_3 = "gesmemories/image/bg/mnd_blood_drip_3.png"
    image bg mnd_blood_drip_4 = "gesmemories/image/bg/mnd_blood_drip_4.png"
    image bg mnd_blood_drip_5 = "gesmemories/image/bg/mnd_blood_drip_5.png"
    image bg mnd_blood_drip_6 = "gesmemories/image/bg/mnd_blood_drip_6.png"
    image bg mnd_blood_drip_7 = "gesmemories/image/bg/mnd_blood_drip_7.png"
    image bg mnd_blood_drip_8 = "gesmemories/image/bg/mnd_blood_drip_8.png"
    image bg mnd_blood_drip_9 = "gesmemories/image/bg/mnd_blood_drip_9.png"
    image bg mnd_a2_c7_lab_1_g1 = "gesmemories/image/bg/mnd_a2_c7_lab_1_g1.png"
    image bg mnd_a2_c7_lab_1_g2 = "gesmemories/image/bg/mnd_a2_c7_lab_1_g2.png"
    image bg mnd_a2_c7_lab_1_g3 = "gesmemories/image/bg/mnd_a2_c7_lab_1_g3.png"
    image bg mnd_a2_c7_lab_1_gc = "gesmemories/image/bg/mnd_a2_c7_lab_1_gc.png"
    image bg mnd_a2_c7_lab_1_d1 = "gesmemories/image/bg/mnd_a2_c7_lab_1_d1.png"
    image bg mnd_a2_c7_lab_1_d2 = "gesmemories/image/bg/mnd_a2_c7_lab_1_d2.png"
    image bg mnd_a2_c7_lab_1_d3 = "gesmemories/image/bg/mnd_a2_c7_lab_1_d3.png"
    image bg mnd_a2_c7_lab_1_d4 = "gesmemories/image/bg/mnd_a2_c7_lab_1_d4.png"
    image bg mnd_vent_1 = "gesmemories/image/bg/mnd_vent_1.png"
    image bg mnd_sspc_bg = "gesmemories/image/bg/mnd_sspc_bg.png"
    image bg mnd_ist_doc_cab_bg = "gesmemories/image/bg/mnd_ist_doc_cab_bg.png"
    image mnd_ist_doc_cab = "gesmemories/image/bg/mnd_ist_doc_cab_bg.png"
    image mnd_himori_smoke_dark = "gesmemories/image/bg/mnd_himori_smoke_dark.png"
    image bg mnd_arahna_psy_bg = "gesmemories/image/bg/mnd_arahna_psy_bg.png"
    image bg mnd_himori_smoke = "gesmemories/image/bg/mnd_himori_smoke.png"
    image bg mnd_wite_cor_normal = "gesmemories/image/bg/mnd_wite_cor_normal.png"
    image bg mnd_secret_wall_2 = "gesmemories/image/bg/mnd_secret_wall_2.png"
    image bg mnd_secret_wall_1 = "gesmemories/image/bg/mnd_secret_wall_1.png"
    image bg mnd_way_in_roof_night = "gesmemories/image/bg/mnd_way_in_roof_night.png"
    image bg 4roomd_close_1 = "gesmemories/image/bg/4roomd_close_1.png"
    image 4roomd_close_1 = "gesmemories/image/bg/4roomd_close_1.png"
    image 4roomd_close_2 = "gesmemories/image/bg/4roomd_close_2.png"
    image bg mnd_ar_angr_1 = "gesmemories/image/bg/mnd_ar_angr_1.png"
    image mnd_ar_angr_1 = "gesmemories/image/bg/mnd_ar_angr_1.png"
    image mnd_ar_angr_2 = "gesmemories/image/bg/mnd_ar_angr_2.png"
    image bg mnd_arahna_dance_chair = "gesmemories/image/bg/mnd_arahna_dance_chair.png"
    image 4roomd_1 = "gesmemories/image/bg/4roomd_1.png"
    image bg mnd_final_a2_bg_mental = "gesmemories/image/bg/mnd_final_a2_bg_mental.png"
    image bg mnd_final_a2_bg_palata = "gesmemories/image/bg/mnd_final_a2_bg_palata.png"
    image bg mnd_winter_window = "gesmemories/image/bg/mnd_winter_window.png"
    image bg mndggroom_n = "gesmemories/image/bg/mndggroom_n.png"
    image bg mndggroom_n_l = "gesmemories/image/bg/mndggroom_n_l.png"
    image bg mnd_windrain_far = "gesmemories/image/bg/mnd_windrain_far.png"
    image bg mnd2b = "gesmemories/image/bg/mnd2b.png"
    image mnd2b = "gesmemories/image/bg/mnd2b.png"
    image mnd = "gesmemories/image/bg/mnd.png"
    image bg mnd = "gesmemories/image/bg/mnd.png"
    image bg mnd_12_shnow_str_n = "gesmemories/image/bg/mnd_12_shnow_str_n.png"
    image bg mnd_try_gg_room_1 = "gesmemories/image/bg/mnd_try_gg_room_1.png"
    image bg mnd_14_pk_nd = "gesmemories/image/bg/mnd_14_pk_nd.png"
    image bg mnd_14_pk_yd = "gesmemories/image/bg/mnd_14_pk_yd.png"
    image bg mnd_14_ten_talk_1 = "gesmemories/image/bg/mnd_14_ten_talk_1.png"
    image bg mnd_14_ten_talk_2 = "gesmemories/image/bg/mnd_14_ten_talk_2.png"
    image bg mnd_14_ten_talk_3 = "gesmemories/image/bg/mnd_14_ten_talk_3.png"
    image bg mnd_14_4rtru = "gesmemories/image/bg/mnd_14_4rtru.png"
    image bg mnd_14_memo_corinvanna = "gesmemories/image/bg/mnd_14_memo_corinvanna.png"
    image bg mnd_podezd_gg_n = "gesmemories/image/bg/mnd_podezd_gg_n.png"
    image bg mnd_ext_graveyard = "gesmemories/image/bg/mnd_ext_graveyard.png"
    image bg mnd_podezd_bg = "gesmemories/image/bg/mnd_podezd_bg.png"
    image bg mnd_gg_bath = "gesmemories/image/bg/mnd_gg_bath.png"
    image bg mnd_doclog_nd = "gesmemories/image/bg/mnd_doclog_nd.png"
    image bg mnd_16_fchbg = "gesmemories/image/bg/mnd_16_fchbg.png"
    image bg mnd_16_autok_bg = "gesmemories/image/bg/mnd_16_autok_bg.png"
    image bg mnd_16_auto_bg = "gesmemories/image/bg/mnd_16_auto_bg.png"
    image mnd_16_autok_fakewindow = "gesmemories/image/bg/mnd_16_autok_fakewindow.png"
    image mnd_16_auto_fakewindow = "gesmemories/image/bg/mnd_16_auto_fakewindow.png"
    image bg mnd_ch18_kor_cent = "gesmemories/image/bg/mnd_ch18_kor_cent.png"
    image bg mnd_ch18_cur = "gesmemories/image/bg/mnd_ch18_cur.png"
    image bg mnd_c18_secret_door = "gesmemories/image/bg/mnd_c18_secret_door.png"
    image bg mnd_flower_bg = "gesmemories/image/bg/mnd_flower_bg.png"
    image carride1_fp = "gesmemories/image/bg/carride1_fp.png"
    image bg mnd_chap18_ladder = "gesmemories/image/bg/mnd_chap18_ladder.png"
    image bg mnd_18_cor_p_1 = "gesmemories/image/bg/mnd_18_cor_p_1.png"
    image bg mnd_true_coridor = "gesmemories/image/bg/mnd_true_coridor.png"





    image mnd1 = "gesmemories/image/psybg/mnd1.png"
    image mnd2 = "gesmemories/image/psybg/mnd2.png"
    image mnd3 = "gesmemories/image/psybg/mnd3.png"
    image mnd4 = "gesmemories/image/psybg/mnd4.png"
    image mnd5 = "gesmemories/image/psybg/mnd5.png"
    image mnd6 = "gesmemories/image/psybg/mnd6.png"
    image mnd7 = "gesmemories/image/psybg/mnd7.png"
    image mnd8 = "gesmemories/image/psybg/mnd8.png"
    image mnd9 = "gesmemories/image/psybg/mnd9.png"
    image mnd10 = "gesmemories/image/psybg/mnd10.png"
    image mnd11 = "gesmemories/image/psybg/mnd11.png"
    image mnd12 = "gesmemories/image/psybg/mnd12.png"
    image mnd13 = "gesmemories/image/psybg/mnd13.png"
    image mnd14 = "gesmemories/image/psybg/mnd14.png"
    image finalfirstpsy22 = "gesmemories/image/psybg/finalfirstpsy22.png"
    image lastkiss22 = "gesmemories/image/psybg/lastkiss22.png"
    image liliyainblood22 = "gesmemories/image/psybg/liliyainblood22.png"
    image lmhit22 = "gesmemories/image/psybg/lmhit22.png"
    image mndbloodfull22 = "gesmemories/image/psybg/mndbloodfull22.png"
    image mndliyadead22 = "gesmemories/image/psybg/mndliyadead22.png"
    image invanna22 = "gesmemories/image/psybg/invanna22.png"
    image invannablood22 = "gesmemories/image/psybg/invannablood22.png"
    image mnd_psy_doll_1 = "gesmemories/image/psybg/mnd_psy_doll_1.png"
    image mnd_psy_doll_2 = "gesmemories/image/psybg/mnd_psy_doll_2.png"
    image mnd_psy_doll_3 = "gesmemories/image/psybg/mnd_psy_doll_3.png"
    image mnd_bt_a2_c7_1 = "gesmemories/image/psybg/mnd_bt_a2_c7_1.png"
    image mnd_bt_a2_c7_2 = "gesmemories/image/psybg/mnd_bt_a2_c7_2.png"
    image mnd_bt_a2_c7_3 = "gesmemories/image/psybg/mnd_bt_a2_c7_3.png"
    image mnd_bt_a2_c7_4 = "gesmemories/image/psybg/mnd_bt_a2_c7_4.png"
    image mnd_lift_no_light_green = "gesmemories/image/psybg/mnd_lift_no_light_green.png"
    image mnd_lift_no_light_red = "gesmemories/image/psybg/mnd_lift_no_light_red.png"
    image mnd_ring_1 = "gesmemories/image/psybg/mnd_ring_1.png"
    image mnd_ring_2 = "gesmemories/image/psybg/mnd_ring_2.png"
    image mnd_ring_3 = "gesmemories/image/psybg/mnd_ring_3.png"
    image mnd_kid_dead_1 = "gesmemories/image/psybg/mnd_kid_dead_1.png"
    image mnd_kid_dead_2 = "gesmemories/image/psybg/mnd_kid_dead_2.png"
    image mnd_kid_dead_3 = "gesmemories/image/psybg/mnd_kid_dead_3.png"


    image bg mnd_a2_c7_r1_nh = "gesmemories/image/psycho/mnd_a2_c7_r1_nh.png"
    image bg mnd_a2_c7_r1_nh_na = "gesmemories/image/psycho/mnd_a2_c7_r1_nh_na.png"
    image bg mnd_a2_c7_r1_nh_ng = "gesmemories/image/psycho/mnd_a2_c7_r1_nh_ng.png"
    image bg mnd_a2_c7_r1_nh_np = "gesmemories/image/psycho/mnd_a2_c7_r1_nh_np.png"
    image bg mnd_a2_c7_r1_o1 = "gesmemories/image/psycho/mnd_a2_c7_r1_o1.png"
    image bg mnd_a2_c7_r1_o2 = "gesmemories/image/psycho/mnd_a2_c7_r1_o2.png"
    image bg mnd_a2_c7_r1_o3 = "gesmemories/image/psycho/mnd_a2_c7_r1_o3.png"
    image bg mnd_a2_c7_r1_o3_2 = "gesmemories/image/psycho/mnd_a2_c7_r1_o3_2.png"
    image bg mnd_a2_c7_r1_yh = "gesmemories/image/psycho/mnd_a2_c7_r1_yh.png"
    image bg mnd_a2_c7_r1_yh_na = "gesmemories/image/psycho/mnd_a2_c7_r1_yh_na.png"
    image bg mnd_a2_c7_r1_yh_ng = "gesmemories/image/psycho/mnd_a2_c7_r1_yh_ng.png"
    image bg mnd_a2_c7_r1_yh_np = "gesmemories/image/psycho/mnd_a2_c7_r1_yh_np.png"
    image bg mnd_a2_ch7_c1_nh = "gesmemories/image/psycho/mnd_a2_ch7_c1_nh.png"
    image bg mnd_a2_ch7_c1_yh = "gesmemories/image/psycho/mnd_a2_ch7_c1_yh.png"
    image bg mnd_cor_suicide_bg = "gesmemories/image/psycho/mnd_cor_suicide_bg.png"
    image bg mnd_vas_dead_bg = "gesmemories/image/psycho/mnd_vas_dead_bg.png"
    image mnd_a2_c7_r1_map = "gesmemories/image/psycho/mnd_a2_c7_r1_map.png"
    image mnd_psy_ten_a2 = "gesmemories/image/psycho/mnd_psy_ten_a2.png"
    image bg mnd_a2_c7_r2_o1 = "gesmemories/image/psycho/mnd_a2_c7_r2_o1.png"
    image bg mnd_a2_c7_r2_o2 = "gesmemories/image/psycho/mnd_a2_c7_r2_o2.png"
    image bg mnd_a2_c7_r2_o3 = "gesmemories/image/psycho/mnd_a2_c7_r2_o3.png"
    image mnd_a2_c7_r2_o2_message = "gesmemories/image/psycho/mnd_a2_c7_r2_o2_message.png"
    image mnd_a2_c7_lab2_light_1 = "gesmemories/image/psycho/mnd_a2_c7_lab2_light_1.png"
    image mnd_a2_c7_lab2_light_2 = "gesmemories/image/psycho/mnd_a2_c7_lab2_light_2.png"
    image bg mnd_a2_c7_lab_2_d1 = "gesmemories/image/psycho/mnd_a2_c7_lab_2_d1.png"
    image bg mnd_a2_c7_lab_2_d2 = "gesmemories/image/psycho/mnd_a2_c7_lab_2_d2.png"
    image bg mnd_a2_c7_lab_2_d3 = "gesmemories/image/psycho/mnd_a2_c7_lab_2_d3.png"
    image bg mnd_med_room_bg = "gesmemories/image/psycho/mnd_med_room_bg.png"
    image mnd_medsestrichka = "gesmemories/image/psycho/mnd_medsestrichka.png"
    image mnd_ftr_2_x_1 = "gesmemories/image/psycho/mnd_ftr_2_x_1.png"
    image mnd_ftr_2_x_2 = "gesmemories/image/psycho/mnd_ftr_2_x_2.png"
    image mnd_ftr_2_x_3 = "gesmemories/image/psycho/mnd_ftr_2_x_3.png"
    image mnd_ftr_2_x_4 = "gesmemories/image/psycho/mnd_ftr_2_x_4.png"
    image mnd_ftr_2_x_5 = "gesmemories/image/psycho/mnd_ftr_2_x_5.png"
    image mnd_ftr_2_x_6 = "gesmemories/image/psycho/mnd_ftr_2_x_6.png"
    image mnd_ftr_2_x_7 = "gesmemories/image/psycho/mnd_ftr_2_x_7.png"
    image mnd_ftr_2_x_8 = "gesmemories/image/psycho/mnd_ftr_2_x_8.png"
    image mnd_ftr_3_h_1 = "gesmemories/image/psycho/mnd_ftr_3_h_1.png"
    image mnd_ftr_3_h_2 = "gesmemories/image/psycho/mnd_ftr_3_h_2.png"
    image mnd_ftr_3_h_3 = "gesmemories/image/psycho/mnd_ftr_3_h_3.png"
    image mnd_ftr_3_p_2 = "gesmemories/image/psycho/mnd_ftr_3_p_2.png"
    image mnd_ftr_3_p_1 = "gesmemories/image/psycho/mnd_ftr_3_p_1.png"
    image mnd_ftr_3_p_3 = "gesmemories/image/psycho/mnd_ftr_3_p_3.png"
    image bg mnd_ftr_3_bg = "gesmemories/image/psycho/mnd_ftr_3_bg.png"
    image bg mnd_aom_bg_1 = "gesmemories/image/psycho/mnd_aom_bg_1.png"
    image bg mnd_med_room_bg = "gesmemories/image/psycho/mnd_med_room_bg.png"
    image bg mnd_dead_vas_coridor_1_1 = "gesmemories/image/psycho/mnd_dead_vas_coridor_1_1.png"
    image bg mnd_dead_vas_coridor_1_2 = "gesmemories/image/psycho/mnd_dead_vas_coridor_1_2.png"
    image bg mnd_dead_vas_coridor_1_p1 = "gesmemories/image/psycho/mnd_dead_vas_coridor_1_p1.png"
    image bg mnd_dead_vas_coridor_1_p2 = "gesmemories/image/psycho/mnd_dead_vas_coridor_1_p2.png"
    image bg mnd_psy_and_vas_dio_bg = "gesmemories/image/psycho/mnd_psy_and_vas_dio_bg.png"
    image mnd_vas_psy_axe  = "gesmemories/image/psycho/mnd_vas_psy_axe.png"
    image mnd_dead_vas_cor_psy1  = "gesmemories/image/psycho/mnd_dead_vas_cor_psy1.png"
    image mnd_dead_vas_cor_psy2  = "gesmemories/image/psycho/mnd_dead_vas_cor_psy2.png"
    image mnd_psy_and_vas_dio_g1  = "gesmemories/image/psycho/mnd_psy_and_vas_dio_g1.png"
    image mnd_psy_and_vas_dio_g2  = "gesmemories/image/psycho/mnd_psy_and_vas_dio_g2.png"
    image mnd_psy_and_vas_dio_g3  = "gesmemories/image/psycho/mnd_psy_and_vas_dio_g3.png"
    image mnd_c9_sbg_1  = "gesmemories/image/psycho/mnd_c9_sbg_1.png"
    image mnd_c9_sbg_2  = "gesmemories/image/psycho/mnd_c9_sbg_2.png"
    image mnd_d1_scr_1  = "gesmemories/image/psycho/mnd_d1_scr_1.png"
    image bg mnd_c10_1h_room = "gesmemories/image/psycho/mnd_c10_1h_room.png"
    image bg mnd_c10_1h_room1 = "gesmemories/image/psycho/mnd_c10_1h_room1.png"
    image bg mnd_c10_r1_bath_1 = "gesmemories/image/psycho/mnd_c10_r1_bath_1.png"
    image bg mnd_c10_r1_bath_2 = "gesmemories/image/psycho/mnd_c10_r1_bath_2.png"
    image bg mnd_c10_r1_bath_3 = "gesmemories/image/psycho/mnd_c10_r1_bath_3.png"
    image bg mnd_c10_room1_bg = "gesmemories/image/psycho/mnd_c10_room1_bg.png"
    image mnd_c10_1h_room_eff_1 = "gesmemories/image/psycho/mnd_c10_1h_room_eff_1.png"
    image mnd_c10_1h_room_eff_2 = "gesmemories/image/psycho/mnd_c10_1h_room_eff_2.png"
    image mnd_c10_1h_room_eff_3 = "gesmemories/image/psycho/mnd_c10_1h_room_eff_3.png"
    image mnd_c10_r1_dead_1 = "gesmemories/image/psycho/mnd_c10_r1_dead_1.png"
    image mnd_c10_r1_dead_2 = "gesmemories/image/psycho/mnd_c10_r1_dead_2.png"
    image mnd_c10_r1_key_item = "gesmemories/image/psycho/mnd_c10_r1_key_item.png"
    image mnd_c10_r1_mess_1 = "gesmemories/image/psycho/mnd_c10_r1_mess_1.png"
    image mnd_c10_r1_mess_2 = "gesmemories/image/psycho/mnd_c10_r1_mess_2.png"
    image mnd_c10_r1_mess_3 = "gesmemories/image/psycho/mnd_c10_r1_mess_3.png"
    image bg mnd_10_r2_bg = "gesmemories/image/psycho/mnd_10_r2_bg.png"
    image bg mnd_c10_c2_bg = "gesmemories/image/psycho/mnd_c10_c2_bg.png"
    image bg mnd_c10_r2_hbg_1 = "gesmemories/image/psycho/mnd_c10_r2_hbg_1.png"
    image mnd_zippo_ch10 = "gesmemories/image/psycho/mnd_zippo_ch10.png"
    image bg mnd_10_c2_lp_ld_sbg_1 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sbg_1.png"
    image bg mnd_10_c2_lp_ld_sbg_2 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sbg_2.png"
    image bg mnd_10_c2_lp_ld_ebg = "gesmemories/image/psycho/mnd_10_c2_lp_ld_ebg.png"
    image bg mnd_10_c2_lp_bg = "gesmemories/image/psycho/mnd_10_c2_lp_bg.png"
    image mnd_10_c2_lp_ld_sbg_a1 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sbg_a1.png"
    image mnd_10_c2_lp_ld_sbg_a2 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sbg_a2.png"
    image mnd_10_c2_lp_ld_sbg_a3 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sbg_a3.png"
    image mnd_10_c2_lp_ld_sspr_1 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sspr_1.png"
    image mnd_10_c2_lp_ld_sspr_2 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sspr_2.png"
    image mnd_10_c2_lp_ld_sspr_3 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sspr_3.png"
    image mnd_10_lp_ld_key = "gesmemories/image/psycho/mnd_10_lp_ld_key.png"
    image mnd_10_lp_ld_otvert = "gesmemories/image/psycho/mnd_10_lp_ld_otvert.png"
    image mnd_tvroom_bg1 = "gesmemories/image/psycho/mnd_tvroom_bg1.png"
    image mnd_tvroom_bg2 = "gesmemories/image/psycho/mnd_tvroom_bg2.png"
    image mnd_tvroom_1 = "gesmemories/image/psycho/mnd_tvroom_1.png"
    image mnd_tvroom_2 = "gesmemories/image/psycho/mnd_tvroom_2.png"
    image mnd_tvroom_3 = "gesmemories/image/psycho/mnd_tvroom_3.png"
    image mnd_tvroom_code_1 = "gesmemories/image/psycho/mnd_tvroom_code_1.png"
    image mnd_tvroom_code_2 = "gesmemories/image/psycho/mnd_tvroom_code_2.png"
    image mnd_tvroom_code_3 = "gesmemories/image/psycho/mnd_tvroom_code_3.png"
    image mnd_cl_n_1_1 = "gesmemories/image/psycho/code/mnd_cl_n_1_1.png"
    image mnd_cl_n_1_2 = "gesmemories/image/psycho/code/mnd_cl_n_1_2.png"
    image mnd_cl_n_1_3 = "gesmemories/image/psycho/code/mnd_cl_n_1_3.png"
    image mnd_cl_n_1_4 = "gesmemories/image/psycho/code/mnd_cl_n_1_4.png"
    image mnd_cl_n_1_5 = "gesmemories/image/psycho/code/mnd_cl_n_1_5.png"
    image mnd_cl_n_1_6 = "gesmemories/image/psycho/code/mnd_cl_n_1_6.png"
    image mnd_cl_n_2_1 = "gesmemories/image/psycho/code/mnd_cl_n_2_1.png"
    image mnd_cl_n_2_2 = "gesmemories/image/psycho/code/mnd_cl_n_2_2.png"
    image mnd_cl_n_2_3 = "gesmemories/image/psycho/code/mnd_cl_n_2_3.png"
    image mnd_cl_n_2_4 = "gesmemories/image/psycho/code/mnd_cl_n_2_4.png"
    image mnd_cl_n_2_5 = "gesmemories/image/psycho/code/mnd_cl_n_2_5.png"
    image mnd_cl_n_2_6 = "gesmemories/image/psycho/code/mnd_cl_n_2_6.png"
    image mnd_cl_n_3_1 = "gesmemories/image/psycho/code/mnd_cl_n_3_1.png"
    image mnd_cl_n_3_2 = "gesmemories/image/psycho/code/mnd_cl_n_3_2.png"
    image mnd_cl_n_3_3 = "gesmemories/image/psycho/code/mnd_cl_n_3_3.png"
    image mnd_cl_n_3_4 = "gesmemories/image/psycho/code/mnd_cl_n_3_4.png"
    image mnd_cl_n_3_5 = "gesmemories/image/psycho/code/mnd_cl_n_3_5.png"
    image mnd_cl_n_3_6 = "gesmemories/image/psycho/code/mnd_cl_n_3_6.png"
    image mnd_code_lock_open = "gesmemories/image/psycho/code/mnd_code_lock_open.png"
    image mnd_code_lock = "gesmemories/image/psycho/code/mnd_code_lock.png"
    image bg mnd_c10_ld_pds = "gesmemories/image/psycho/mnd_c10_ld_pds.png"
    image bg mnd_break_glass_bg = "gesmemories/image/psycho/mnd_break_glass_bg.png"
    image bg mnd_10_2_rp_room_bg = "gesmemories/image/psycho/mnd_10_2_rp_room_bg.png"
    image mndtenpaper1v_ytz = "gesmemories/image/psycho/mndtenpaper1v_ytz.png"
    image mnd_fake_key = "gesmemories/image/psycho/mnd_fake_key.png"
    image mnd_fake_key_1 = "gesmemories/image/psycho/mnd_fake_key_1.png"
    image bg mnd_10_rp_bg = "gesmemories/image/psycho/mnd_10_rp_bg.png"
    image bg mnd_10_rp_2_bg = "gesmemories/image/psycho/mnd_10_rp_2_bg.png"
    image bg mnd_10_rp2_ld_bg = "gesmemories/image/psycho/mnd_10_rp2_ld_bg.png"
    image bg mnd_exitpsy_bg_1 = "gesmemories/image/psycho/mnd_exitpsy_bg_1.png"
    image bg mnd_exitpsy_bg_2 = "gesmemories/image/psycho/mnd_exitpsy_bg_2.png"
    image bg mnd_exitpsy_bg_break_vanna = "gesmemories/image/psycho/mnd_exitpsy_bg_break_vanna.png"
    image bg mnd_exitpsy_bg_bv_wat_1 = "gesmemories/image/psycho/mnd_exitpsy_bg_bv_wat_1.png"
    image bg mnd_exitpsy_bg_bv_wat_2 = "gesmemories/image/psycho/mnd_exitpsy_bg_bv_wat_2.png"
    image bg mnd_exitpsy_bg_bv_wat_3 = "gesmemories/image/psycho/mnd_exitpsy_bg_bv_wat_3.png"
    image bg mnd_exitpsy_bg_wather_in_vanna = "gesmemories/image/psycho/mnd_exitpsy_bg_wather_in_vanna.png"
    image bg mnd_exitpsy_nolight_1 = "gesmemories/image/psycho/mnd_exitpsy_nolight_1.png"
    image bg mnd_exitpsy_nolight_2 = "gesmemories/image/psycho/mnd_exitpsy_nolight_2.png"
    image bg mnd_exitpsy_nolight_3 = "gesmemories/image/psycho/mnd_exitpsy_nolight_3.png"
    image bg mnd_exitpsy_nolight_4 = "gesmemories/image/psycho/mnd_exitpsy_nolight_4.png"
    image bg mnd_exitpsy_nolight_5 = "gesmemories/image/psycho/mnd_exitpsy_nolight_5.png"
    image bg mnd_exitpsy_nolight_6 = "gesmemories/image/psycho/mnd_exitpsy_nolight_6.png"
    image bg mnd_exitpsy_nolight_7 = "gesmemories/image/psycho/mnd_exitpsy_nolight_7.png"
    image mnd_10f_bg_d_0_1 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_0_1.png"
    image mnd_10f_bg_d_0_0 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_0_0.png"
    image mnd_10f_bg_d_1 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_1.png"
    image mnd_10f_bg_d_2 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_2.png"
    image mnd_10f_bg_d_3 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_3.png"
    image mnd_10f_bg_d_4 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_4.png"
    image mnd_10f_bg_d_5 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_5.png"
    image mnd_10f_bg_d_6 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_6.png"
    image mnd_10f_bg_d_7 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_7.png"
    image mnd_10f_bg_d_8 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_8.png"
    image mnd_10f_bg_d_9 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_9.png"
    image mnd_10f_bg_d_10 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_10.png"
    image mnd_10f_bg_d_11 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_11.png"
    image mnd_10f_bg_d_12 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_12.png"
    image mnd_10f_bg_d_13 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_13.png"
    image mnd_10f_bg_d_14 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_14.png"
    image mnd_10f_bg_d_open = "gesmemories/image/psycho/wall/mnd_10f_bg_d_open.png"
    image mnd_10f_bg_f = "gesmemories/image/psycho/mnd_10f_bg_f.png"
    image mnd_10f_w_mag_1 = "gesmemories/image/psycho/mnd_10f_w_mag_1.png"
    image mnd_10f_w_mag_2 = "gesmemories/image/psycho/mnd_10f_w_mag_2.png"
    image mnd_10f_w_mag_3 = "gesmemories/image/psycho/mnd_10f_w_mag_3.png"
    image bg mnd_exitpsy_water_floor = "gesmemories/image/psycho/mnd_exitpsy_water_floor.png"
    image bg mnd_himorI_memo_bg_1 = "gesmemories/image/psycho/mnd_himorI_memo_bg_1.png"
    image bg mnd_himorI_memo_bg_2 = "gesmemories/image/psycho/mnd_himorI_memo_bg_2.png"
    image bg mnd_fight_memo_1 = "gesmemories/image/psycho/mnd_fight_memo_1.png"
    image bg mnd_fight_memo_2 = "gesmemories/image/psycho/mnd_fight_memo_2.png"
    image bg mnd_c3_p2_lu = "gesmemories/image/psycho/mnd_c3_p2_lu.png"
    image bg mnd_c3_p3_bg = "gesmemories/image/psycho/mnd_c3_p3_bg.png"
    image bg mnd_10_bottom_floor_p2_ld_close = "gesmemories/image/psycho/mnd_10_bottom_floor_p2_ld_close.png"
    image bg mnd_10_cafe_bg = "gesmemories/image/psycho/mnd_10_cafe_bg.png"
    image bg mnd_10_c3_p1_ld = "gesmemories/image/psycho/mnd_10_c3_p1_ld.png"
    image bg mnd_c3_p2_bg = "gesmemories/image/psycho/mnd_c3_p2_bg.png"
    image bg mnd_himori_cab_bg = "gesmemories/image/psycho/mnd_himori_cab_bg.png"
    image bg mnd_10_cd_bg = "gesmemories/image/psycho/mnd_10_cd_bg.png"
    image bg mnd_fvcd_bg = "gesmemories/image/psycho/mnd_fvcd_bg.png"
    image mnd_flaga_spr = "gesmemories/image/psycho/mnd_flaga_spr.png"
    image mnd_fvcd_doc = "gesmemories/image/psycho/mnd_fvcd_doc.png"
    image mnd_10_cd_gkey = "gesmemories/image/psycho/mnd_10_cd_gkey.png"
    image mnd_fvcd_walls = "gesmemories/image/psycho/mnd_fvcd_walls.png"
    image mnd_fvcd_screamer = "gesmemories/image/psycho/mnd_fvcd_screamer.png"
    image bg mnd_c10_room1_bg_bw = "gesmemories/image/psycho/mnd_c10_room1_bg_bw.png"
    image bg mnd_10_roof_bg = "gesmemories/image/psycho/mnd_10_roof_bg.png"
    image bg mnd_10_c3_p2_roof_exit = "gesmemories/image/psycho/mnd_10_c3_p2_roof_exit.png"
    image mnd_c10_room1_posilka = "gesmemories/image/psycho/mnd_c10_room1_posilka.png"
    image mnd_10_tape_spr = "gesmemories/image/psycho/mnd_10_tape_spr.png"
    image mnd_10_roof_mes = "gesmemories/image/psycho/mnd_10_roof_mes.png"
    image bg mnd_basement10_bg = "gesmemories/image/psycho/mnd_basement10_bg.png"
    image bg mnd_10_bot_coridor_bg = "gesmemories/image/psycho/mnd_10_bot_coridor_bg.png"
    image bg mnd_10_dociventcab_bg = "gesmemories/image/psycho/mnd_10_dociventcab_bg.png"
    image bg mnd_10_go_bodv_bg = "gesmemories/image/psycho/mnd_10_go_bodv_bg.png"
    image bg mnd_shahta10_bg = "gesmemories/image/psycho/mnd_shahta10_bg.png"
    image bg mnd_basement10_wrong_bg = "gesmemories/image/psycho/mnd_basement10_wrong_bg.png"
    image bg mnd_basement10_2d_bg = "gesmemories/image/psycho/mnd_basement10_2d_bg.png"
    image bg mnd_waterhome_bg = "gesmemories/image/psycho/mnd_waterhome_bg.png"
    image bg mnd_powerroom10_bg = "gesmemories/image/psycho/mnd_powerroom10_bg.png"
    image bg mnddushnigh2 = "gesmemories/image/psycho/mnddushnigh2.png"
    image bg mnddushnigh1 = "gesmemories/image/psycho/mnddushnigh1.png"
    image mnd_bf_doc_mes_spr1 = "gesmemories/image/psycho/mnd_bf_doc_mes_spr1.png"
    image mnd_bf_doc_mes_spr2 = "gesmemories/image/psycho/mnd_bf_doc_mes_spr2.png"
    image mnd_bf_doc_mes_spr3 = "gesmemories/image/psycho/mnd_bf_doc_mes_spr3.png"
    image mnd_bf_doc_mes_spr4 = "gesmemories/image/psycho/mnd_bf_doc_mes_spr4.png"
    image mnd_fake_key4 = "gesmemories/image/psycho/mnd_fake_key4.png"
    image mnd_waterhome_mes_spr = "gesmemories/image/psycho/mnd_waterhome_mes_spr.png"
    image mnd_light_house_mes_spr = "gesmemories/image/psycho/mnd_light_house_mes_spr.png"
    image mnd_shahta10_key_spr = "gesmemories/image/psycho/mnd_shahta10_key_spr.png"
    image bg mnd_10_fsc_bg_1 = "gesmemories/image/psycho/mnd_10_fsc_bg_1.jpg"
    image bg mnd_10_fsc_bg_2 = "gesmemories/image/psycho/mnd_10_fsc_bg_2.jpg"
    image bg mnd_10_fsc_bg_3 = "gesmemories/image/psycho/mnd_10_fsc_bg_3.jpg"
    image bg mnd_10_fsc_bg_4 = "gesmemories/image/psycho/mnd_10_fsc_bg_4.jpg"
    image bg mnd_run_10_bg = "gesmemories/image/psycho/mnd_run_10_bg.png"
    image mnd_10_fsc_bg_1_vasp = "gesmemories/image/psycho/mnd_10_fsc_bg_1_vasp.png"
    image bg mnd_arah_bw = "gesmemories/image/psycho/mnd_arah_bw.png"
    image bg mnd_arah_foll_12 = "gesmemories/image/psycho/mnd_arah_foll_12.png"
    image bg mnd_ch11_bg3_up = "gesmemories/image/psycho/mnd_ch11_bg3_up.png"
    image bg mnd_ch11_axe_fb1 = "gesmemories/image/psycho/mnd_ch11_axe_fb1.png"
    image mnd_ch11_axe_hit = "gesmemories/image/psycho/mnd_ch11_axe_hit.png"
    image mnd_ch11_axe_in_hand_1 = "gesmemories/image/psycho/mnd_ch11_axe_in_hand_1.png"
    image mnd_ch11_axe_z = "gesmemories/image/psycho/mnd_ch11_axe_z.png"
    image bg mnd_ch11_bg1 = "gesmemories/image/psycho/mnd_ch11_bg1.png"
    image bg mnd_ch11_bg3_down = "gesmemories/image/psycho/mnd_ch11_bg3_down.png"
    image mndggroom_p_p2 = "gesmemories/image/psycho/mndggroom_p_p2.png"
    image mndggroom_p_p1 = "gesmemories/image/psycho/mndggroom_p_p1.png"
    image mnd_aom_hand2_3 = "gesmemories/image/psycho/mnd_aom_hand2_3.png"
    image mnd_aom_hand2_2 = "gesmemories/image/psycho/mnd_aom_hand2_2.png"
    image mnd_aom_hand2_1 = "gesmemories/image/psycho/mnd_aom_hand2_1.png"
    image mnd_aom_hand1_3 = "gesmemories/image/psycho/mnd_aom_hand1_3.png"
    image mnd_aom_hand1_2 = "gesmemories/image/psycho/mnd_aom_hand1_2.png"
    image mnd_aom_hand1_1 = "gesmemories/image/psycho/mnd_aom_hand1_1.png"
    image mnd_vas_psy_axe_fake = "gesmemories/image/psycho/mnd_vas_psy_axe_fake.png"
    image mnd_vas_psy_axe_true = "gesmemories/image/psycho/mnd_vas_psy_axe_true.png"



    image mnd_c11_wa_b1_s1 = "gesmemories/image/trymemo/mnd_c11_wa_b1_s1.png"
    image mnd_c11_wa_b1_s2 = "gesmemories/image/trymemo/mnd_c11_wa_b1_s2.png"
    image mnd_c11_wa_b1_s3 = "gesmemories/image/trymemo/mnd_c11_wa_b1_s3.png"
    image mnd_c11_wa_b1_s4 = "gesmemories/image/trymemo/mnd_c11_wa_b1_s4.png"
    image mnd_c11_wa_b1_stay = "gesmemories/image/trymemo/mnd_c11_wa_b1_stay.png"
    image mnd_c11_wa_b1_stay_f = "gesmemories/image/trymemo/mnd_c11_wa_b1_stay_f.png"
    image bg mnd_ch11_bg1 = "gesmemories/image/trymemo/mnd_ch11_bg1.png"
    image mnd_ch11_who1_g1 = "gesmemories/image/trymemo/mnd_ch11_who1_g1.png"
    image mnd_ch11_who1_g2 = "gesmemories/image/trymemo/mnd_ch11_who1_g2.png"
    image mnd_ch11_who1_g3 = "gesmemories/image/trymemo/mnd_ch11_who1_g3.png"
    image mnd_ch11_who1_spr = "gesmemories/image/trymemo/mnd_ch11_who1_spr.png"
    image mnd_c11_wa_s_axe_1 = "gesmemories/image/trymemo/mnd_c11_wa_s_axe_1.png"
    image mnd_c11_wa_s_axe_2 = "gesmemories/image/trymemo/mnd_c11_wa_s_axe_2.png"
    image mnd_c11_wa_s_axe_3 = "gesmemories/image/trymemo/mnd_c11_wa_s_axe_3.png"
    image mnd_c11_wa_s_axe_4 = "gesmemories/image/trymemo/mnd_c11_wa_s_axe_4.png"
    image mnd_13_lk_spr = "gesmemories/image/trymemo/mnd_13_lk_spr.png"
    image mnd_c11_wa_stay_axe = "gesmemories/image/trymemo/mnd_c11_wa_stay_axe.png"
    image mnd_c11_wa_stay_end_axe = "gesmemories/image/trymemo/mnd_c11_wa_stay_end_axe.png"
    image mnd_c13_ladd_stay = "gesmemories/image/trymemo/mnd_c13_ladd_stay.png"
    image mnd_c13_ladd_stay_axe = "gesmemories/image/trymemo/mnd_c13_ladd_stay_axe.png"
    image bg mnd_ch11_bg2_1 = "gesmemories/image/trymemo/mnd_ch11_bg2_1.png"
    image bg mnd_ch11_bg2_2 = "gesmemories/image/trymemo/mnd_ch11_bg2_2.png"
    image bg mnd_ch11_bg2_lc = "gesmemories/image/trymemo/mnd_ch11_bg2_lc.png"
    image bg mnd_ch11_bg2_lo = "gesmemories/image/trymemo/mnd_ch11_bg2_lo.png"
    image bg mnd_ch11_doors1 = "gesmemories/image/trymemo/mnd_ch11_doors1.png"
    image bg mnd_ch11_doors2 = "gesmemories/image/trymemo/mnd_ch11_doors2.png"
    image bg mnd_ch11_doors3 = "gesmemories/image/trymemo/mnd_ch11_doors3.png"
    image bg mnd_ch11_doors4 = "gesmemories/image/trymemo/mnd_ch11_doors4.png"
    image bg mnd_ch11_doors5 = "gesmemories/image/trymemo/mnd_ch11_doors5.png"
    image bg mnd_ch11_doors6 = "gesmemories/image/trymemo/mnd_ch11_doors6.png"
    image bg mnd_ch11_ladder = "gesmemories/image/trymemo/mnd_ch11_ladder.png"
    image bg mnd_ch11_room1 = "gesmemories/image/trymemo/mnd_ch11_room1.png"
    image bg mnd_ch11_up_floor = "gesmemories/image/trymemo/mnd_ch11_up_floor.png"
    image bg mnd_ch13_base_cor = "gesmemories/image/trymemo/mnd_ch13_base_cor.png"
    image mnd_ch13_db_1 = "gesmemories/image/trymemo/mnd_ch13_db_1.png"
    image mnd_ch13_db_2 = "gesmemories/image/trymemo/mnd_ch13_db_2.png"
    image mnd_ch13_db_3 = "gesmemories/image/trymemo/mnd_ch13_db_3.png"
    image mnd_ch13_db_4 = "gesmemories/image/trymemo/mnd_ch13_db_4.png"
    image mnd_ch13_db_5 = "gesmemories/image/trymemo/mnd_ch13_db_5.png"
    image mnd_ch13_lk_h_1 = "gesmemories/image/trymemo/mnd_ch13_lk_h_1.png"
    image mnd_ch13_lk_h_2 = "gesmemories/image/trymemo/mnd_ch13_lk_h_2.png"
    image mnd_ch13_lk_h_3 = "gesmemories/image/trymemo/mnd_ch13_lk_h_3.png"
    image bg mnd_lift_mine_baw = "gesmemories/image/trymemo/mnd_lift_mine_baw.png"
    image mnd_paket_ch13_1 = "gesmemories/image/trymemo/mnd_paket_ch13_1.png"
    image mnd_paket_ch13_2 = "gesmemories/image/trymemo/mnd_paket_ch13_2.png"
    image mnd_paket_ch13_3 = "gesmemories/image/trymemo/mnd_paket_ch13_3.png"
    image mnd_qte_button_w = "gesmemories/image/trymemo/mnd_qte_button_w.png"
    image mnd_qte_fone_1 = "gesmemories/image/trymemo/mnd_qte_fone_1.png"
    image mnd_qte_fone_2 = "gesmemories/image/trymemo/mnd_qte_fone_2.png"
    image bg mnd_shaht_down_bg13 = "gesmemories/image/trymemo/mnd_shaht_down_bg13.png"
    image bg mnd_skyrain_baw = "gesmemories/image/trymemo/mnd_skyrain_baw.png"
    image bg mnd_13_3k_cor_1 = "gesmemories/image/trymemo/mnd_13_3k_cor_1.png"
    image bg mnd_13_3k_cor_2 = "gesmemories/image/trymemo/mnd_13_3k_cor_2.png"
    image bg mnd_13_3k_cor_3 = "gesmemories/image/trymemo/mnd_13_3k_cor_3.png"
    image bg mnd_13_3k_cor_4 = "gesmemories/image/trymemo/mnd_13_3k_cor_4.png"
    image bg mnd_13_3k_cor_5 = "gesmemories/image/trymemo/mnd_13_3k_cor_5.png"
    image bg mnd_13_3k_cor_6 = "gesmemories/image/trymemo/mnd_13_3k_cor_6.png"
    image bg mnd_13_3k_cor_jump_1 = "gesmemories/image/trymemo/mnd_13_3k_cor_jump_1.png"
    image bg mnd_13_3k_cor_jump_1_j = "gesmemories/image/trymemo/mnd_13_3k_cor_jump_1_j.png"
    image bg mnd_13_10c_base_bg = "gesmemories/image/trymemo/mnd_13_10c_base_bg.png"
    image bg mnd_13_10c_bath_bg = "gesmemories/image/trymemo/mnd_13_10c_bath_bg.png"
    image bg mnd_13_10c_code_color = "gesmemories/image/trymemo/mnd_13_10c_code_color.png"
    image bg mnd_13_10c_f10_bg = "gesmemories/image/trymemo/mnd_13_10c_f10_bg.png"
    image bg mnd_13_10c_f10_bg_od = "gesmemories/image/trymemo/mnd_13_10c_f10_bg_od.png"
    image bg mnd_13_10c_fimale_lc = "gesmemories/image/trymemo/mnd_13_10c_fimale_lc.png"
    image bg mnd_13_10c_fimale_lo = "gesmemories/image/trymemo/mnd_13_10c_fimale_lo.png"
    image bg mnd_13_10c_himori_kab_bg = "gesmemories/image/trymemo/mnd_13_10c_himori_kab_bg.png"
    image bg mnd_13_10c_k1_bg = "gesmemories/image/trymemo/mnd_13_10c_k1_bg.png"
    image bg mnd_13_10c_k1_lp_bg = "gesmemories/image/trymemo/mnd_13_10c_k1_lp_bg.png"
    image bg mnd_13_10c_k1_rp_bg = "gesmemories/image/trymemo/mnd_13_10c_k1_rp_bg.png"
    image bg mnd_13_10c_k1_rp_ld_bg1 = "gesmemories/image/trymemo/mnd_13_10c_k1_rp_ld_bg1.png"
    image bg mnd_13_10c_k1_rp_ld_bg2 = "gesmemories/image/trymemo/mnd_13_10c_k1_rp_ld_bg2.png"
    image bg mnd_13_10c_k1_rp_rp_bg = "gesmemories/image/trymemo/mnd_13_10c_k1_rp_rp_bg.png"
    image bg mnd_13_10c_k2_ck1_bg = "gesmemories/image/trymemo/mnd_13_10c_k2_ck1_bg.png"
    image bg mnd_13_10c_k2_ck2_bg = "gesmemories/image/trymemo/mnd_13_10c_k2_ck2_bg.png"
    image bg mnd_13_10c_k2_ld_bg = "gesmemories/image/trymemo/mnd_13_10c_k2_ld_bg.png"
    image bg mnd_13_10c_pr_bg = "gesmemories/image/trymemo/mnd_13_10c_pr_bg.png"
    image mnd_13_10c_pr_bg_dec_1  = "gesmemories/image/trymemo/mnd_13_10c_pr_bg_dec_1.png"
    image mnd_13_10c_pr_bg_dec_2  = "gesmemories/image/trymemo/mnd_13_10c_pr_bg_dec_2.png"
    image mnd_13_10c_provod  = "gesmemories/image/trymemo/mnd_13_10c_provod.png"
    image mnd_13_10c_skey  = "gesmemories/image/trymemo/mnd_13_10c_skey.png"
    image bg mnd_13_10c_sklad_bg = "gesmemories/image/trymemo/mnd_13_10c_sklad_bg.png"
    image mnd_13_10c_tape_spr = "gesmemories/image/trymemo/mnd_13_10c_tape_spr.png"
    image bg mnd_13_10c_tr_bg = "gesmemories/image/trymemo/mnd_13_10c_tr_bg.png"
    image mnd_13_10c_tvr_axe  = "gesmemories/image/trymemo/mnd_13_10c_tvr_axe.png"
    image mnd_13_10c_tvr_bc  = "gesmemories/image/trymemo/mnd_13_10c_tvr_bc.png"
    image mnd_13_10c_tvr_bo  = "gesmemories/image/trymemo/mnd_13_10c_tvr_bo.png"
    image bg mnd_13_10c_tvr_bc  = "gesmemories/image/trymemo/mnd_13_10c_tvr_bc.png"
    image bg mnd_13_10c_tvr_bo  = "gesmemories/image/trymemo/mnd_13_10c_tvr_bo.png"
    image mnd_13_10c_tvr_code  = "gesmemories/image/trymemo/mnd_13_10c_tvr_code.png"
    image bg mnd_13_10c_wr_bg = "gesmemories/image/trymemo/mnd_13_10c_wr_bg.png"
    image bg mnd_13_ascor_1 = "gesmemories/image/trymemo/mnd_13_ascor_1.png"
    image bg mnd_13_ascor_2 = "gesmemories/image/trymemo/mnd_13_ascor_2.png"
    image bg mnd_13_ascor_3 = "gesmemories/image/trymemo/mnd_13_ascor_3.png"
    image bg mnd_13_blood_bath = "gesmemories/image/trymemo/mnd_13_blood_bath.png"
    image bg mnd_13_bot_s_bg_1 = "gesmemories/image/trymemo/mnd_13_bot_s_bg_1.png"
    image bg mnd_13_bot_s_bg_2 = "gesmemories/image/trymemo/mnd_13_bot_s_bg_2.png"
    image bg mnd_13_bot_s_bg_3 = "gesmemories/image/trymemo/mnd_13_bot_s_bg_3.png"
    image bg mnd_13_bot_s_bg_4 = "gesmemories/image/trymemo/mnd_13_bot_s_bg_4.png"
    image bg mnd_13_bot_s_bg_5 = "gesmemories/image/trymemo/mnd_13_bot_s_bg_5.png"
    image bg mnd_13_bot_s_bg_6 = "gesmemories/image/trymemo/mnd_13_bot_s_bg_6.png"
    image bg mnd_13_kur = "gesmemories/image/trymemo/mnd_13_kur.png"
    image bg mnd_13_vent_fall = "gesmemories/image/trymemo/mnd_13_vent_fall.png"
    image mnd_ch11_key  = "gesmemories/image/trymemo/mnd_ch11_key.png"
    image mnd_qte_button_e  = "gesmemories/image/trymemo/mnd_qte_button_e.png"
    image mnd_qte_button_r  = "gesmemories/image/trymemo/mnd_qte_button_r.png"
    image bg mnd_13_3k_bf_l1 = "gesmemories/image/trymemo/mnd_13_3k_bf_l1.png"
    image bg mnd_13_3k_bf_l2 = "gesmemories/image/trymemo/mnd_13_3k_bf_l2.png"
    image bg mnd_13_3k_bf_l3 = "gesmemories/image/trymemo/mnd_13_3k_bf_l3.png"
    image mnd_13_3k_bf_ld_1  = "gesmemories/image/trymemo/mnd_13_3k_bf_ld_1.png"
    image mnd_13_3k_bf_ld_2  = "gesmemories/image/trymemo/mnd_13_3k_bf_ld_2.png"
    image bg mnd_13_3k_cor_block = "gesmemories/image/trymemo/mnd_13_3k_cor_block.png"
    image bg mnd_13_3k_cor_block2 = "gesmemories/image/trymemo/mnd_13_3k_cor_block2.png"
    image bg mnd_13_3k_cor_move_1 = "gesmemories/image/trymemo/mnd_13_3k_cor_move_1.png"
    image bg mnd_13_3k_cor_move_2 = "gesmemories/image/trymemo/mnd_13_3k_cor_move_2.png"
    image bg mnd_13_3k_cor_move_3 = "gesmemories/image/trymemo/mnd_13_3k_cor_move_3.png"
    image bg mnd_13_3k_cor_move_4 = "gesmemories/image/trymemo/mnd_13_3k_cor_move_4.png"
    image bg mnd_13_3k_cor_move_5 = "gesmemories/image/trymemo/mnd_13_3k_cor_move_5.png"
    image bg mnd_13_3k_cor_r_1 = "gesmemories/image/trymemo/mnd_13_3k_cor_r_1.png"
    image bg mnd_13_3k_cor_r_2 = "gesmemories/image/trymemo/mnd_13_3k_cor_r_2.png"
    image bg mnd_13_3k_cor_r_3 = "gesmemories/image/trymemo/mnd_13_3k_cor_r_3.png"
    image bg mnd_13_3k_cor_r_4 = "gesmemories/image/trymemo/mnd_13_3k_cor_r_4.png"
    image bg mnd_13_3k_cor_r_5 = "gesmemories/image/trymemo/mnd_13_3k_cor_r_5.png"
    image bg mnd_13_3k_mv_1 = "gesmemories/image/trymemo/mnd_13_3k_mv_1.png"
    image bg mnd_13_3k_mv_2 = "gesmemories/image/trymemo/mnd_13_3k_mv_2.png"
    image bg mnd_13_3k_mv_3 = "gesmemories/image/trymemo/mnd_13_3k_mv_3.png"
    image bg mnd_13_3k_mv_4 = "gesmemories/image/trymemo/mnd_13_3k_mv_4.png"
    image bg mnd_13_3k_mv_5 = "gesmemories/image/trymemo/mnd_13_3k_mv_5.png"
    image bg mnd_13_3k_mv_6 = "gesmemories/image/trymemo/mnd_13_3k_mv_6.png"
    image bg mnd_13_3k_mv_7 = "gesmemories/image/trymemo/mnd_13_3k_mv_7.png"
    image bg mnd_13_3k_mv_8 = "gesmemories/image/trymemo/mnd_13_3k_mv_8.png"
    image bg mnd_13_3k_mv_9 = "gesmemories/image/trymemo/mnd_13_3k_mv_9.png"
    image bg mnd_13_3k_mv_10 = "gesmemories/image/trymemo/mnd_13_3k_mv_10.png"
    image bg mnd_13_3k_mv_11 = "gesmemories/image/trymemo/mnd_13_3k_mv_11.png"
    image mnd_13_darkness_1  = "gesmemories/image/trymemo/mnd_13_darkness_1.png"
    image mnd_13_darkness_2  = "gesmemories/image/trymemo/mnd_13_darkness_2.png"
    image mnd_13_darkness_3  = "gesmemories/image/trymemo/mnd_13_darkness_3.png"
    image mnd_13_darkness_4  = "gesmemories/image/trymemo/mnd_13_darkness_4.png"



















    image bg mndcorpsy1 = "gesmemories/image/nightmare/mndcorpsy1.png"
    image bg mndcorpsy2 = "gesmemories/image/nightmare/mndcorpsy2.png"
    image bg mndfr_nh = "gesmemories/image/nightmare/mndfr_nh.jpg"
    image mndtenpaper1_ntz  = "gesmemories/image/nightmare/mndtenpaper1_ntz.png"
    image mndtenpaper1_ytz  = "gesmemories/image/nightmare/mndtenpaper1_ytz.png"
    image mndlinda  = "gesmemories/image/nightmare/mndlinda.png"
    image mndphotopsy  = "gesmemories/image/nightmare/mndphotopsy.png"
    image bg mndtenpsyfsc_d = "gesmemories/image/nightmare/mndtenpsyfsc_d.jpg"
    image bg mndtenpsyfsc_l = "gesmemories/image/nightmare/mndtenpsyfsc_l.jpg"
    image bg mndtenpsylight_f = "gesmemories/image/nightmare/mndtenpsylight_f.jpg"
    image bg mndlight_c = "gesmemories/image/nightmare/mndlight_c.jpg"
    image bg mnddoorlight_nh = "gesmemories/image/nightmare/mnddoorlight_nh.jpg"
    image bg mndpsycor1_1 = "gesmemories/image/nightmare/mndpsycor1_1.jpg"
    image bg mndpsycor1_2 = "gesmemories/image/nightmare/mndpsycor1_2.jpg"
    image bg mndpsycor1_3 = "gesmemories/image/nightmare/mndpsycor1_3.jpg"
    image bg mndpsycor1_4 = "gesmemories/image/nightmare/mndpsycor1_4.jpg"
    image bg mndpsycor1_5 = "gesmemories/image/nightmare/mndpsycor1_5.jpg"
    image bg mndpsycor1_6 = "gesmemories/image/nightmare/mndpsycor1_6.jpg"
    image bg mndpsycor1_7 = "gesmemories/image/nightmare/mndpsycor1_7.jpg"
    image bg mndpsycor1_8 = "gesmemories/image/nightmare/mndpsycor1_8.jpg"
    image bg mndpsycor1_9 = "gesmemories/image/nightmare/mndpsycor1_9.jpg"
    image bg mndpsycor1_10 = "gesmemories/image/nightmare/mndpsycor1_10.jpg"
    image bg mndpsycor1_11 = "gesmemories/image/nightmare/mndpsycor1_11.jpg"
    image bg mndpsycor1_12 = "gesmemories/image/nightmare/mndpsycor1_12.jpg"
    image bg mndpsycor2_1 = "gesmemories/image/nightmare/mndpsycor2_1.jpg"
    image bg mndpsycor2_2 = "gesmemories/image/nightmare/mndpsycor2_2.jpg"
    image bg mndpsycor2_3 = "gesmemories/image/nightmare/mndpsycor2_3.jpg"
    image bg mnd3door1 = "gesmemories/image/nightmare/mnd3door1.jpg"
    image bg mnd3door2 = "gesmemories/image/nightmare/mnd3door2.jpg"
    image bg mndnr1_nh = "gesmemories/image/nightmare/mndnr1_nh.jpg"
    image mndoldclock = "gesmemories/image/nightmare/mndoldclock.png"
    image mndcorscr = "gesmemories/image/nightmare/mndcorscr.png"
    image bg mndgameover = "gesmemories/image/nightmare/mndgameover.png"
    image bg mndwebcorold = "gesmemories/image/nightmare/mndwebcorold.png"


    image mndsd1 = "gesmemories/image/logo/mndsd1.png"
    image mndsd2 = "gesmemories/image/logo/mndsd2.png"
    image testph2 = "gesmemories/image/logo/testph2.png"
    image liyapaint = "gesmemories/image/logo/liyapaint.png"
    image bg mndps = "gesmemories/image/logo/mndps.png"
    image savemess = "gesmemories/image/logo/savemess.png"
    image mndgessplash = "gesmemories/image/logo/mndgessplash.png"
    image bg mndc1l1 = "gesmemories/image/logo/mndc1l1.png"
    image bg mndc1l2 = "gesmemories/image/logo/mndc1l2.png"
    image bg mndch2l1 = "gesmemories/image/logo/mndch2l1.png"
    image bg mndch2l2 = "gesmemories/image/logo/mndch2l2.png"
    image bg mndch2l3 = "gesmemories/image/logo/mndch2l3.png"
    image bg mndch2l4 = "gesmemories/image/logo/mndch2l4.png"
    image sprtbk  = "gesmemories/image/logo/sprtbk.png"
    image mndch4l1 = "gesmemories/image/logo/mndch4l1.png"
    image mndch4l2 = "gesmemories/image/logo/mndch4l2.png"
    image mndch4l3 = "gesmemories/image/logo/mndch4l3.png"
    image bg mndalienmemologo = "gesmemories/image/logo/mndalienmemologo.png"
    image mndfinal1actn1 = "gesmemories/image/logo/mndfinal1actn1.png"
    image mndfinal1actn2 = "gesmemories/image/logo/mndfinal1actn2.png"
    image mnd_2act_logo = "gesmemories/image/logo/mnd_2act_logo.png"
    image mnd_lift_psy_1 = "gesmemories/image/logo/mnd_lift_psy_1.png"
    image mnd_lift_psy_2 = "gesmemories/image/logo/mnd_lift_psy_2.png"
    image mnd_lift_psy_3 = "gesmemories/image/logo/mnd_lift_psy_3.png"
    image mnd_lift_psy_4 = "gesmemories/image/logo/mnd_lift_psy_4.png"
    image mnd_lift_psy_5 = "gesmemories/image/logo/mnd_lift_psy_5.png"
    image mnd_lift_psy_6 = "gesmemories/image/logo/mnd_lift_psy_6.png"
    image mnd_lift_psy_7 = "gesmemories/image/logo/mnd_lift_psy_7.png"
    image mnd_lift_psy_8 = "gesmemories/image/logo/mnd_lift_psy_8.png"
    image mnd_himore_scene_smoke_1 = "gesmemories/image/logo/mnd_himore_scene_smoke_1.png"
    image mnd_himore_scene_smoke_2 = "gesmemories/image/logo/mnd_himore_scene_smoke_2.png"
    image mnd_a2final_logo_1 = "gesmemories/image/logo/mnd_a2final_logo_1.png"
    image mnd_a2final_logo_2 = "gesmemories/image/logo/mnd_a2final_logo_2.png"
    image mnd_a2final_logo_3 = "gesmemories/image/logo/mnd_a2final_logo_3.png"
    image mnd_a2final_logo_4 = "gesmemories/image/logo/mnd_a2final_logo_4.png"
    image mnd_snow = "gesmemories/image/logo/mnd_snow.png"
    image mnd_winter_window_no_back = "gesmemories/image/logo/mnd_winter_window_no_back.png"
    image mnd_windrain_close = "gesmemories/image/logo/mnd_windrain_close.png"
    image mnd_load_scr_1 = "gesmemories/image/logo/mnd_load_scr_1.png"
    image mnd_load_scr_2 = "gesmemories/image/logo/mnd_load_scr_2.png"
    image mnd_load_scr_3 = "gesmemories/image/logo/mnd_load_scr_3.png"
    image mnd_load_scr_4 = "gesmemories/image/logo/mnd_load_scr_4.png"
    image mnd_load_scr_5 = "gesmemories/image/logo/mnd_load_scr_5.png"
    image mnd_load_scr_6 = "gesmemories/image/logo/mnd_load_scr_6.png"
    image mnd_12_phone_n_1am = "gesmemories/image/logo/mnd_12_phone_n_1am.png"
    image mnd_12_phone_n = "gesmemories/image/logo/mnd_12_phone_n.png"
    image mnd_12_phone_n_r = "gesmemories/image/logo/mnd_12_phone_n_r.png"
    image mnd_12_phone_n_rt = "gesmemories/image/logo/mnd_12_phone_n_1am.png"
    image mndggroom_p_s = "gesmemories/image/logo/mndggroom_p_s.png"
    image mndggroom_p_l = "gesmemories/image/logo/mndggroom_p_l.png"
    image mnd_a3_menu_1 = "gesmemories/image/logo/mnd_a3_menu_1.png"
    image mnd_a3_menu_2 = "gesmemories/image/logo/mnd_a3_menu_2.png"
    image mnd_new_dis_1 = "gesmemories/image/logo/mnd_new_dis_1.png"
    image mnd_new_dis_2 = "gesmemories/image/logo/mnd_new_dis_2.png"
    image mnd_new_dis_3 = "gesmemories/image/logo/mnd_new_dis_3.png"
    image mnd_tv_spr_true = "gesmemories/image/logo/mnd_tv_spr_true.png"
    image mnd_podezd_fakewindow = "gesmemories/image/logo/mnd_podezd_fakewindow.png"
    image mnd_auto_fakewindow = "gesmemories/image/logo/mnd_auto_fakewindow.png"
    image bg mnd_18_t1 = "gesmemories/image/logo/mnd_18_t1.png"
    image bg mnd_18_t2 = "gesmemories/image/logo/mnd_18_t2.png"
    image bg mnd_18_t3 = "gesmemories/image/logo/mnd_18_t3.png"
    image bg mnd_18_t4 = "gesmemories/image/logo/mnd_18_t4.png"
    image bg mnd_18_t5 = "gesmemories/image/logo/mnd_18_t5.png"
    image bg mnd_18_t6 = "gesmemories/image/logo/mnd_18_t6.png"
    image bg mnd_18_t7 = "gesmemories/image/logo/mnd_18_t7.png"
    image bg mnd_18_t8 = "gesmemories/image/logo/mnd_18_t8.png"
    image bg mnd_18_t9 = "gesmemories/image/logo/mnd_18_t9.png"
    image bg mnd_sb_mm_mf_bg = "gesmemories/image/logo/mnd_sb_mm_mf_bg.png"
    image mnd_sb_mm_mf_1 = "gesmemories/image/logo/mnd_sb_mm_mf_1.png"
    image mnd_sb_mm_mf_2 = "gesmemories/image/logo/mnd_sb_mm_mf_2.png"
    image mnd_sb_mm_mf_spr = "gesmemories/image/logo/mnd_sb_mm_mf_spr.png"
    image mnd_r_ges_spl = "gesmemories/image/logo/mnd_r_ges_spl.png"
    image bg mnd_r_int_bg_1 = "gesmemories/image/logo/mnd_r_int_bg_1.png"
    image bg mnd_r_int_bg_2 = "gesmemories/image/logo/mnd_r_int_bg_2.png"
    image bg mnd_r_int_bg_3 = "gesmemories/image/logo/mnd_r_int_bg_3.png"
    image mnd_r_tv_log = "gesmemories/image/logo/mnd_r_tv_log.png"
    image blood = "gesmemories/image/logo/blood.png"
    image mnd_flower_fp = "gesmemories/image/logo/mnd_flower_fp.png"
    image mnd_flower_fw = "gesmemories/image/logo/mnd_flower_fw.png"
    image mndrainaspd_fp = "gesmemories/image/logo/mndrainaspd_fp.png"
    image mndrainaspd_s1 = "gesmemories/image/logo/mndrainaspd_s1.png"
    image mndrainaspd_s2 = "gesmemories/image/logo/mndrainaspd_s2.png"
    image medpalat_fw = "gesmemories/image/logo/medpalat_fw.png"
    image medpalat_fp = "gesmemories/image/logo/medpalat_fp.png"



    image psyapaty = "gesmemories/image/status/psyapaty.png"
    image psybad = "gesmemories/image/status/psybad.png"
    image psycrit = "gesmemories/image/status/psycrit.png"
    image psygood = "gesmemories/image/status/psygood.png"
    image psynorm = "gesmemories/image/status/psynorm.png"
    image psystress = "gesmemories/image/status/psystress.png"
    image mndnesr = "gesmemories/image/status/mndnesr.png"



    image bg 1car = "gesmemories/image/scene/1car.jpg"
    image bg 2car = "gesmemories/image/scene/2car.jpg"
    image bg 3car = "gesmemories/image/scene/3car.jpg"
    image bg 4car = "gesmemories/image/scene/4car.jpg"
    image bg cutters = "gesmemories/image/scene/cutters.png"
    image bg filindream1 = "gesmemories/image/scene/filindream1.png"
    image bg liyahartsdance = "gesmemories/image/scene/liyahartsdance.png"
    image bg lmhit = "gesmemories/image/scene/lmhit.png"
    image bg mndliyadead = "gesmemories/image/scene/mndliyadead.png"
    image bg swoosh1 = "gesmemories/image/scene/swoosh1.png"
    image bg zihaologo = "gesmemories/image/scene/zihaologo.png"
    image kuklanote1 = "gesmemories/image/scene/kuklanote1.png"
    image kuklanote2 = "gesmemories/image/scene/kuklanote2.png"
    image kuklanote3 = "gesmemories/image/scene/kuklanote3.png"
    image kuklanote4 = "gesmemories/image/scene/kuklanote4.png"
    image kuklanote5 = "gesmemories/image/scene/kuklanote5.png"
    image kuklanote6 = "gesmemories/image/scene/kuklanote6.png"
    image kuklanote7 = "gesmemories/image/scene/kuklanote7.png"
    image kuklanote8 = "gesmemories/image/scene/kuklanote8.png"
    image kuklanote9 = "gesmemories/image/scene/kuklanote9.png"
    image kuklanote10 = "gesmemories/image/scene/kuklanote10.png"
    image kuklanote11 = "gesmemories/image/scene/kuklanote11.png"
    image bg mndseabg = "gesmemories/image/scene/mndseabg.png"
    image bg mndbulpsy = "gesmemories/image/scene/mndbulpsy.png"
    image bg mnderdie = "gesmemories/image/scene/mnderdie.png"
    image bg mndlisapsych1 = "gesmemories/image/scene/mndlisapsych1.png"
    image bg mndhimerapsych1 = "gesmemories/image/scene/mndhimerapsych1.png"
    image bg takanpsych1 = "gesmemories/image/scene/takanpsych1.png"
    image bg mndtenkilleretic = "gesmemories/image/scene/mndtenkilleretic.png"
    image bg kuklapsych1 = "gesmemories/image/scene/kuklapsych1.png"
    image bg raise1 = "gesmemories/image/scene/raise1.png"
    image bg raise2 = "gesmemories/image/scene/raise2.png"
    image bg mndtenfa = "gesmemories/image/scene/mndtenfa.png"
    image bg mndtenfa = "gesmemories/image/scene/mndtenfa.png"
    image bg mndtensavecrow1 = "gesmemories/image/scene/mndtensavecrow1.png"
    image bg mndmatwolf1 = "gesmemories/image/scene/mndmatwolf1.png"
    image bg mndmatwolf2 = "gesmemories/image/scene/mndmatwolf2.png"
    image bg mndmatwolf3 = "gesmemories/image/scene/mndmatwolf3.png"
    image bg mndbloodforest = "gesmemories/image/scene/mndbloodforest.png"
    image bg mndtenpsycg2 = "gesmemories/image/scene/mndtenpsycg2.png"
    image bg mndtenpsycg3 = "gesmemories/image/scene/mndtenpsycg3.png"
    image bg mndtenpsycg4 = "gesmemories/image/scene/mndtenpsycg4.png"
    image bg mndtenfindcops = "gesmemories/image/scene/mndtenfindcops.png"
    image bg mndkidsablock = "gesmemories/image/scene/mndkidsablock.png"
    image bg mndslavya = "gesmemories/image/scene/mndslavya.png"
    image bg mndteninpitroom = "gesmemories/image/scene/mndteninpitroom.png"
    image bg mndoldsmertcg = "gesmemories/image/scene/mndoldsmertcg.png"
    image bg mndvaskisshim = "gesmemories/image/scene/mndvaskisshim.png"
    image bg mndvkh1 = "gesmemories/image/scene/mndvkh1.png"
    image bg mndvkh2 = "gesmemories/image/scene/mndvkh2.png"
    image bg mndatf = "gesmemories/image/scene/mndatf.png"
    image bg mndfightcor = "gesmemories/image/scene/mndfightcor.png"
    image bg mndarroofside = "gesmemories/image/scene/mndarroofside.png"
    image bg mndliyainsvete = "gesmemories/image/scene/mndliyainsvete.png"
    image bg mndbookbg1 = "gesmemories/image/scene/mndbookbg1.png"
    image bg mndact1finalbg = "gesmemories/image/scene/mndact1finalbg.png"
    image bg mndliyam1 = "gesmemories/image/scene/mndliyam1.png"
    image bg mndvasandhimsmoke = "gesmemories/image/scene/mndvasandhimsmoke.png"
    image bg mndhimeradie = "gesmemories/image/scene/mndhimeradie.png"
    image bg mnd_kiss_night = "gesmemories/image/scene/mnd_kiss_night.png"
    image bg mnd_liya_dead_ring = "gesmemories/image/scene/mnd_liya_dead_ring.png"
    image bg mnd_arahna_bed_1 = "gesmemories/image/scene/mnd_arahna_bed_1.png"
    image bg mnd_arahna_bed_2 = "gesmemories/image/scene/mnd_arahna_bed_2.png"
    image mnd_hit_wall_1 = "gesmemories/image/scene/mnd_hit_wall_1.png"
    image mnd_hit_wall_2 = "gesmemories/image/scene/mnd_hit_wall_2.png"
    image bg mnd_arahna_final_scene = "gesmemories/image/scene/mnd_arahna_final_scene.png"
    image bg mnd_ch11_bed_scene = "gesmemories/image/scene/mnd_ch11_bed_scene.png"
    image mnd_aom_wood_1 = "gesmemories/image/scene/mnd_aom_wood_1.png"
    image mnd_aom_wood_2 = "gesmemories/image/scene/mnd_aom_wood_2.png"
    image mnd_aom_wood_3 = "gesmemories/image/scene/mnd_aom_wood_3.png"
    image mnd_ch6_hp = "gesmemories/image/scene/mnd_ch6_hp.png"


    image brod = "gesmemories/image/spr/ofther/brod.png"
    image ptms = "gesmemories/image/spr/ofther/ptms.png"
    image ptmn = "gesmemories/image/spr/ofther/ptmn.png"
    image dart = "gesmemories/image/spr/ofther/dart.png"
    image mnd_bul_real_1 = "gesmemories/image/spr/ofther/mnd_bul_real_1.png"
    image mnd_bul_real_2 = "gesmemories/image/spr/ofther/mnd_bul_real_2.png"
    image mnd_16_sec_spr = "gesmemories/image/spr/ofther/mnd_16_sec_spr.png"
    image mnd_ks_med_n = "gesmemories/image/spr/ofther/mnd_ks_med_n.png"
    image mnd_ks_med_s = "gesmemories/image/spr/ofther/mnd_ks_med_s.png"
    image mnd_ks_med_se = "gesmemories/image/spr/ofther/mnd_ks_med_se.png"

    image mnddenn = "gesmemories/image/spr/den/mnddenn.png"

    image mndoldteach = "gesmemories/image/spr/old/mndoldteach.png"
    image mndgirlold = "gesmemories/image/spr/old/mndgirlold.png"
    image mndbled = "gesmemories/image/spr/old/mndbled.png"
    image mndbledeyes = "gesmemories/image/spr/old/mndbledeyes.png"
    image mndoldmanold = "gesmemories/image/spr/old/mndoldmanold.png"
    image mndorela = "gesmemories/image/spr/old/mndorela.png"
    image mndorels = "gesmemories/image/spr/old/mndorels.png"
    image mndorelu = "gesmemories/image/spr/old/mndorelu.png"
    image mndosgirls = "gesmemories/image/spr/old/mndosgirls.png"
    image mndreshsad = "gesmemories/image/spr/old/mndreshsad.png"
    image mndzmeyhands = "gesmemories/image/spr/old/mndzmeyhands.png"
    image mndldmanleroy = "gesmemories/image/spr/old/mndldmanleroy.png"

    image anc = "gesmemories/image/spr/andr/andrc.png"
    image ani = "gesmemories/image/spr/andr/andri.png"
    image ann = "gesmemories/image/spr/andr/andrn.png"
    image ans = "gesmemories/image/spr/andr/andrs.png"
    image andri = "gesmemories/image/spr/andr/andri.png"
    image andrs = "gesmemories/image/spr/andr/andrs.png"
    image andr_w = "gesmemories/image/spr/andr/andr_w.png"

    image mndlisanu = "gesmemories/image/spr/lisa/mndlnu.png"
    image mndlisann = "gesmemories/image/spr/lisa/mndlnn.png"
    image mndlisanl = "gesmemories/image/spr/lisa/mndlnl.png"
    image mndlisana = "gesmemories/image/spr/lisa/mndlna.png"
    image mndlds = "gesmemories/image/spr/lisa/mndlds.png"


    image xian_g = "gesmemories/image/spr/xian/xian_g.png"
    image xian_n = "gesmemories/image/spr/xian/xian_n.png"
    image xian_s = "gesmemories/image/spr/xian/xian_s.png"
    image xian_t = "gesmemories/image/spr/xian/xian_t.png"


    image mnd_himori_af = "gesmemories/image/spr/himori/mnd_himori_af.png"
    image mnd_himori_norm = "gesmemories/image/spr/himori/mnd_himori_norm.png"
    image mnd_himori_sm = "gesmemories/image/spr/himori/mnd_himori_sm.png"
    image mnd_himori_st = "gesmemories/image/spr/himori/mnd_himori_st.png"





    image hia = "gesmemories/image/spr/himera/hia.png"
    image hia2 = "gesmemories/image/spr/himera/hia2.png"
    image hin = "gesmemories/image/spr/himera/hin.png"
    image hin2 = "gesmemories/image/spr/himera/hin2.png"
    image hip = "gesmemories/image/spr/himera/hip.png"
    image hip2 = "gesmemories/image/spr/himera/hip2.png"
    image his = "gesmemories/image/spr/himera/his.png"
    image his2 = "gesmemories/image/spr/himera/his2.png"
    image hiu = "gesmemories/image/spr/himera/hiu.png"
    image hiu2 = "gesmemories/image/spr/himera/hiu2.png"
    image mndhoh = "gesmemories/image/spr/himera/mndhoh.png"
    image mndhon = "gesmemories/image/spr/himera/mndhon.png"
    image mndhos = "gesmemories/image/spr/himera/mndhos.png"
    image him_p_12_1 = "gesmemories/image/spr/himera/him_p_12_1.png"
    image him_p_12_2 = "gesmemories/image/spr/himera/him_p_12_2.png"


    image ggpsy = "gesmemories/image/spr/vas/ggpsy.png"
    image mnd_vas_psy_joke = "gesmemories/image/spr/vas/mnd_vas_psy_joke.png"
    image mnd_14_vas_g = "gesmemories/image/spr/vas/mnd_14_vas_g.png"
    image mnd_c18_psyv_sh = "gesmemories/image/spr/vas/mnd_c18_psyv_sh.png"

    image mndfish = "gesmemories/image/spr/mental/mndfish.png"

    image mndkukn = "gesmemories/image/spr/kukla/mndkukn.png"
    image mndkukpsy = "gesmemories/image/spr/kukla/mndkukpsy.png"

    image mndera = "gesmemories/image/spr/eretic/mndera.png"
    image mndern = "gesmemories/image/spr/eretic/mndern.png"
    image mnders = "gesmemories/image/spr/eretic/mnders.png"
    image mnderz = "gesmemories/image/spr/eretic/mnderz.png"





    image bulangr = "gesmemories/image/spr/mental/bulangr.png"
    image mentalmed = "gesmemories/image/spr/mental/mentalmed.png"
    image mentalsa = "gesmemories/image/spr/mental/mentalsa.png"
    image mndzih = "gesmemories/image/spr/mental/mndzih.png"
    image takan = "gesmemories/image/spr/mental/takan.png"
    image mndelic = "gesmemories/image/spr/mental/mndelic.png"

    image smertn = "gesmemories/image/spr/smert/smertn.png"
    image sdn = "gesmemories/image/spr/smert/sdn.png"
    image sdkn = "gesmemories/image/spr/smert/sdkn.png"
    image smertpsy = "gesmemories/image/spr/smert/smertpsy.png"
    image mndsmertold = "gesmemories/image/spr/smert/mndsmertold.png"

    image mndten = "gesmemories/image/spr/ten/mndten.png"
    image tenpsy = "gesmemories/image/spr/ten/tenpsy.png"

    image yaf = "gesmemories/image/spr/yasher/yaf.png"
    image yna = "gesmemories/image/spr/yasher/yna.png"
    image ynl = "gesmemories/image/spr/yasher/ynl.png"
    image ynn = "gesmemories/image/spr/yasher/ynn.png"
    image lizardpsy = "gesmemories/image/spr/yasher/lizardpsy.png"


    image mndliyalove = "gesmemories/image/spr/liya/mndliyalove.png"
    image mndlnu = "gesmemories/image/spr/liya/mndlnu.png"
    image mndlhg = "gesmemories/image/spr/liya/mndlhg.png"
    image mndlhn = "gesmemories/image/spr/liya/mndlhn.png"
    image mndlho = "gesmemories/image/spr/liya/mndlho.png"
    image mndlhs = "gesmemories/image/spr/liya/mndlhs.png"
    image mndlhu = "gesmemories/image/spr/liya/mndlhu.png"
    image mndliyaghost = "gesmemories/image/spr/liya/mndliyaghost.png"
    image mndlln = "gesmemories/image/spr/liya/mndlln.png"
    image mndlls = "gesmemories/image/spr/liya/mndlls.png"
    image mndllu = "gesmemories/image/spr/liya/mndllu.png"
    image mndlna = "gesmemories/image/spr/liya/mndlna.png"
    image mndlnl = "gesmemories/image/spr/liya/mndlnl.png"
    image mndlnn = "gesmemories/image/spr/liya/mndlnn.png"
    image mndliyapsy = "gesmemories/image/spr/liya/mndliyapsy.png"
    image mnd_church_liya_spr = "gesmemories/image/spr/liya/mnd_church_liya_spr.png"
    image mnd_church_liya_spr2 = "gesmemories/image/spr/liya/mnd_church_liya_spr2.png"
    image mnd_liya_psy_noise_1 = "gesmemories/image/spr/liya/mnd_liya_psy_noise_1.png"
    image mnd_liya_psy_noise_2 = "gesmemories/image/spr/liya/mnd_liya_psy_noise_2.png"
    image mnd_liya_psy_noise_3 = "gesmemories/image/spr/liya/mnd_liya_psy_noise_3.png"
    image mnd_liya_psy_noise_4 = "gesmemories/image/spr/liya/mnd_liya_psy_noise_4.png"


    image bg mndfp_nh = "gesmemories/image/nightmare/mndfp_nh.jpg"
    image bg mnddeadincor = "gesmemories/image/nightmare/mnddeadincor.jpg"
    image mndghost1_1 = "gesmemories/image/nightmare/mndghost1_1.png"
    image mndghost1_2 = "gesmemories/image/nightmare/mndghost1_2.png"
    image mndghost1_3 = "gesmemories/image/nightmare/mndghost1_3.png"
    image mndfp_yh = "gesmemories/image/nightmare/mndfp_yh.png"
    image bg mndtitscr = "gesmemories/image/nightmare/mndtitscr.png"
    image mnd_vent_g_1 = "gesmemories/image/nightmare/mnd_vent_g_1.png"
    image mnd_vent_g_2 = "gesmemories/image/nightmare/mnd_vent_g_2.png"
    image mnd_vent_g_3 = "gesmemories/image/nightmare/mnd_vent_g_3.png"

    image mndleroy = "gesmemories/image/spr/old/mndleroy.png"
    image voronakid = "gesmemories/image/spr/old/voronakid.png"
    image mndzmey = "gesmemories/image/spr/old/mndzmey.png"
    image mndkrolchiha = "gesmemories/image/spr/old/mndkrol.png"
    image mndkrol = "gesmemories/image/spr/old/mndkrol.png"
    image mndlizghost = "gesmemories/image/spr/old/mndlizghost.png"

    image vashc = "gesmemories/image/spr/vas/vashc.png"

    image hivc = "gesmemories/image/spr/himera/hivc.png"

    image mndsha = "gesmemories/image/spr/mental/mndsha.png"
    image mndbha = "gesmemories/image/spr/mental/mndbha.png"
    image mndbulmak = "gesmemories/image/spr/mental/mndbulmak.png"
    image mndkuks = "gesmemories/image/spr/kukla/mndkuks.png"
    image mndar1 = "gesmemories/image/spr/arahna/mndar1.png"
    image mndar2 = "gesmemories/image/spr/arahna/mndar2.png"
    image mndar3 = "gesmemories/image/spr/arahna/mndar3.png"
    image mndar4 = "gesmemories/image/spr/arahna/mndar4.png"
    image mndar5 = "gesmemories/image/spr/arahna/mndar5.png"
    image mnd_h_ar3 = "gesmemories/image/spr/arahna/mnd_h_ar3.png"
    image mnd_h_ar4 = "gesmemories/image/spr/arahna/mnd_h_ar4.png"
    image mnd_ar_dr_far = "gesmemories/image/spr/arahna/mnd_ar_dr_far.png"
    image mnd_ar_dr_1 = "gesmemories/image/spr/arahna/mnd_ar_dr_1.png"
    image mnd_ar_dr_2 = "gesmemories/image/spr/arahna/mnd_ar_dr_2.png"
    image mnd_ar_dr_3 = "gesmemories/image/spr/arahna/mnd_ar_dr_3.png"
    image mnd_ar_jack_cry_nt = "gesmemories/image/spr/arahna/mnd_ar_jack_cry_nt.png"
    image mnd_ar_jack_cry_t = "gesmemories/image/spr/arahna/mnd_ar_jack_cry_t.png"
    image mnd_ar_jack_gr_be = "gesmemories/image/spr/arahna/mnd_ar_jack_gr_be.png"
    image mnd_ar_jack_gr_bu = "gesmemories/image/spr/arahna/mnd_ar_jack_gr_bu.png"
    image mnd_ar_jack_h_g = "gesmemories/image/spr/arahna/mnd_ar_jack_h_g.png"
    image mnd_ar_jack_h_s = "gesmemories/image/spr/arahna/mnd_ar_jack_h_s.png"
    image mnd_ar_jack_n = "gesmemories/image/spr/arahna/mnd_ar_jack_n.png"



    image mnd_liya_psy_a2_1 = "gesmemories/image/spr/psy/mnd_liya_psy_a2_1.png"
    image mnd_liya_psy_a2_2 = "gesmemories/image/spr/psy/mnd_liya_psy_a2_2.png"
    image mnd_liya_psy_a2_3 = "gesmemories/image/spr/psy/mnd_liya_psy_a2_3.png"
    image mnd_liya_psy_a2_4 = "gesmemories/image/spr/psy/mnd_liya_psy_a2_4.png"





    image mnd_luci_n_f_sh = "gesmemories/image/spr/luciena/mnd_luci_n_f_sh.png"
    image mnd_luci_n_sh = "gesmemories/image/spr/luciena/mnd_luci_n_sh.png"
    image mnd_luci_n_s = "gesmemories/image/spr/luciena/mnd_luci_n_s.png"
    image mnd_luci_n_n = "gesmemories/image/spr/luciena/mnd_luci_n_n.png"
    image mnd_luci_b_sh = "gesmemories/image/spr/luciena/mnd_luci_b_sh.png"
    image mnd_luci_b_s = "gesmemories/image/spr/luciena/mnd_luci_b_s.png"
    image mnd_luci_b_n = "gesmemories/image/spr/luciena/mnd_luci_b_n.png"
    image mnd_luci_dance = "gesmemories/image/spr/luciena/mnd_luci_dance.png"














    image mndrain_c:
        contains:
            "gesmemories/image/logo/rain.png"
            xpos 0.5 ypos -1.0
        contains:
            "gesmemories/image/logo/rain.png"
            xpos -0.5 ypos -1.0
        contains:
            "gesmemories/image/logo/rain.png"
            xpos 0.5 ypos 0.0
        contains:
            "gesmemories/image/logo/rain.png"
            xpos -0.5 ypos 0.0
        contains:
            "gesmemories/image/logo/rain.png"
            xpos 0.5 ypos 1.0
        contains:
            "gesmemories/image/logo/rain.png"
            xpos -0.5 ypos 1.0
        contains:
             "gesmemories/image/logo/rain.png"
             xpos 0.5 ypos 2.0
        contains:
             "gesmemories/image/logo/rain.png"
             xpos -0.5 ypos 2.0
        block:
            yanchor 1.0
            linear 0.3 yanchor 0.0
            repeat

    image mndawaken:
        contains:
            "gesmemories/image/scene/awaken.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                choice:
                    zoom 1.025
                choice:
                    zoom 1.02
                choice:
                    zoom 1.015
                choice:
                    zoom 1.01
                pause 0.02
                repeat
            parallel:
                choice:
                    xpos 0.495
                choice:
                    xpos 0.5
                choice:
                    xpos 0.505
                pause 0.02
                repeat
            parallel:
                choice:
                    ypos 0.495
                choice:
                    ypos 0.5
                choice:
                    ypos 0.505
                pause 0.02
                repeat





    transform run_anim:
        parallel:
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            ease 0.2 zoom 1.04 xpos 0.5 ypos 0.49
        parallel:
            ease 0.2 xpos 0.5 ypos 0.49
            ease 0.2 xpos 0.48 ypos 0.51
            ease 0.2 xpos 0.5 ypos 0.49
            ease 0.2 xpos 0.52 ypos 0.51
            repeat
    
    transform run_anim_end:
        ease 0.2 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    
    image mndghost1:
        contains:
            choice:
                "mndghost1_1"
            choice:
                "mndghost1_2"
            choice:
                "mndghost1_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mndghost1_1"
            choice:
                "mndghost1_2"
            choice:
                "mndghost1_3"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "mndghost1_1"
            choice:
                "mndghost1_2"
            choice:
                "mndghost1_3"
            alpha 0.25
            pause 0.05
            repeat




    image mnd_aom_wood:
        contains:
            choice:
                "mnd_aom_wood_1"
            choice:
                "mnd_aom_wood_2"
            choice:
                "mnd_aom_wood_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_aom_wood_1"
            choice:
                "mnd_aom_wood_2"
            choice:
                "mnd_aom_wood_3"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_aom_wood_1"
            choice:
                "mnd_aom_wood_2"
            choice:
                "mnd_aom_wood_3"
            alpha 0.25
            pause 0.05
            repeat





    image mnd_psy_hands_1:
        contains:
            choice:
                "mnd_aom_hand1_1"
            choice:
                "mnd_aom_hand1_2"
            choice:
                "mnd_aom_hand1_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_aom_hand1_1"
            choice:
                "mnd_aom_hand1_2"
            choice:
                "mnd_aom_hand1_3"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_aom_hand1_1"
            choice:
                "mnd_aom_hand1_2"
            choice:
                "mnd_aom_hand1_3"
            alpha 0.25
            pause 0.05
            repeat



    image mnd_psy_hands_2:
        contains:
            choice:
                "mnd_aom_hand2_1"
            choice:
                "mnd_aom_hand2_2"
            choice:
                "mnd_aom_hand2_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_aom_hand2_1"
            choice:
                "mnd_aom_hand2_2"
            choice:
                "mnd_aom_hand2_3"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_aom_hand2_1"
            choice:
                "mnd_aom_hand2_2"
            choice:
                "mnd_aom_hand2_3"
            alpha 0.25
            pause 0.05
            repeat





    image mnd_ch13_lk_h:
        contains:
            choice:
                "mnd_ch13_lk_h_1"
            choice:
                "mnd_ch13_lk_h_2"
            choice:
                "mnd_ch13_lk_h_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_ch13_lk_h_1"
            choice:
                "mnd_ch13_lk_h_2"
            choice:
                "mnd_ch13_lk_h_3"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_ch13_lk_h_1"
            choice:
                "mnd_ch13_lk_h_2"
            choice:
                "mnd_ch13_lk_h_3"
            alpha 0.25
            pause 0.05
            repeat








    image mnd_paket_ch13:
        contains:
            choice:
                "mnd_paket_ch13_1"
            choice:
                "mnd_paket_ch13_2"
            choice:
                "mnd_paket_ch13_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_paket_ch13_1"
            choice:
                "mnd_paket_ch13_2"
            choice:
                "mnd_paket_ch13_3"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_paket_ch13_1"
            choice:
                "mnd_paket_ch13_2"
            choice:
                "mnd_paket_ch13_3"
            alpha 0.25
            pause 0.05
            repeat






    image mnd_qte_fone:
        contains:
            choice:
                "mnd_qte_fone_1"
            choice:
                "mnd_qte_fone_2"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_qte_fone_1"
            choice:
                "mnd_qte_fone_2"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_qte_fone_1"
            choice:
                "mnd_qte_fone_2"
            alpha 0.25
            pause 0.05
            repeat







    image mnd_b_and_w_bg:
        contains:
            choice:
                "mnd"
            choice:
                "mnd2b"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd"
            choice:
                "mnd2b"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "mnd"
            choice:
                "mnd2b"
            alpha 0.25
            pause 0.05
            repeat






    image mndggroom_p_p:
        contains:
            choice:
                "mndggroom_p_p2"
            choice:
                "mndggroom_p_p1"
            pause 0.05
            repeat
        contains:
            choice:
                "mndggroom_p_p2"
            choice:
                "mndggroom_p_p1"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "mndggroom_p_p2"
            choice:
                "mndggroom_p_p1"
            alpha 0.25
            pause 0.05
            repeat


















    image mnd_vent_ghost:
        contains:
            choice:
                "mnd_vent_g_1"
            choice:
                "mnd_vent_g_2"
            choice:
                "mnd_vent_g_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_vent_g_1"
            choice:
                "mnd_vent_g_2"
            choice:
                "mnd_vent_g_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_vent_g_1"
            choice:
                "mnd_vent_g_2"
            choice:
                "mnd_vent_g_3"
            pause 0.05
            repeat





    image mnd_r4_light:
        contains:
            choice:
                "mnd_a2_c7_lab2_light_1"
            choice:
                "mnd_a2_c7_lab2_light_2"
            pause 1.05
            repeat


    image mnd_tvroom_code:
        contains:
            choice:
                "mnd_tvroom_code_1"
            choice:
                "mnd_tvroom_code_2"
            choice:
                "mnd_tvroom_code_3"
            pause 0.10
            repeat
        contains:
            choice:
                "mnd_tvroom_code_1"
            choice:
                "mnd_tvroom_code_2"
            choice:
                "mnd_tvroom_code_3"
            pause 0.10
            repeat
        contains:
            choice:
                "mnd_tvroom_code_1"
            choice:
                "mnd_tvroom_code_2"
            choice:
                "mnd_tvroom_code_3"
            pause 0.10
            repeat












    image bg mnd_himori_smoke_close:
        contains:
            "gesmemories/image/logo/mnd_himori_smoke_close_1.png"
        contains:
            "gesmemories/image/logo/mnd_himori_smoke_close_2.png"
            alpha 0.0
            ease 2.8 alpha 1.0
            ease 2.8 alpha 0.0
            repeat



    image mnd_himori_smoke:
        contains:
            choice:
                "mnd_himore_scene_smoke_1"
            choice:
                "mnd_himore_scene_smoke_2"
            pause 1.05
            repeat
        contains:
            choice:
                "mnd_himore_scene_smoke_1"
            choice:
                "mnd_himore_scene_smoke_2"
            pause 1.05
            repeat
        contains:
            choice:
                "mnd_himore_scene_smoke_1"
            choice:
                "mnd_himore_scene_smoke_2"
            pause 1.05
            repeat







    image bg menu_mnd:
        contains:
            "gesmemories/image/logo/mndmenu1.png"
        contains:
            "gesmemories/image/logo/mndmenu2.png"
            alpha 0.0
            ease 2.5 alpha 1.0
            ease 2.5 alpha 0.0
            repeat


    image menu_mnd2:
        contains:
            "gesmemories/image/logo/mnd_menu2_1.png"
        contains:
            "gesmemories/image/logo/mnd_menu2_2.png"
            alpha 0.0
            ease 2.8 alpha 1.0
            ease 2.8 alpha 0.0
            repeat





    image bg mndcutmemos:
        contains:
            "gesmemories/image/scene/cutmemo1.png"
        contains:
            "gesmemories/image/scene/cutmemo2.png"
            alpha 0.0
            ease 2.5 alpha 1.0
            ease 2.5 alpha 0.0
            repeat






    image mndliyagluk1:
        contains:
            choice:
                "mndlhn"
            choice:
                "mndliyalove"
            choice:
                "mndllu"
            choice:
                "mndlnl"
            pause 0.05
            repeat
        contains:
            choice:
                "mndlhn"
            choice:
                "mndliyalove"
            choice:
                "mndllu"
            choice:
                "mndlnl"
            pause 0.05
            repeat
        contains:
            choice:
                "mndlhn"
            choice:
                "mndliyalove"
            choice:
                "mndllu"
            choice:
                "mndlnl"
            pause 0.05
            repeat













    image mndliyapsybg1:
        contains:
            choice:
                "mnd1"
            choice:
                "mnd2"
            choice:
                "lmhit22"
            choice:
                "mndliyadead22"
            choice:
                "lastkiss22"
            choice:
                "liliyainblood22"
            choice:
                "invanna22"
            choice:
                "invannablood22"
            choice:
                "mndbloodfull22"
            choice:
                "finalfirstpsy22"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd1"
            choice:
                "mnd2"
            choice:
                "lmhit22"
            choice:
                "mndliyadead22"
            choice:
                "lastkiss22"
            choice:
                "liliyainblood22"
            choice:
                "invanna22"
            choice:
                "invannablood22"
            choice:
                "mndbloodfull22"
            choice:
                "finalfirstpsy22"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd1"
            choice:
                "mnd2"
            choice:
                "lmhit22"
            choice:
                "mndliyadead22"
            choice:
                "lastkiss22"
            choice:
                "liliyainblood22"
            choice:
                "invanna22"
            choice:
                "invannablood22"
            choice:
                "mndbloodfull22"
            choice:
                "finalfirstpsy22"
            pause 0.05
            repeat








    image mndliyapsybg2:
        contains:
            choice:
                "mnd3"
            choice:
                "mnd4"
            choice:
                "mnd5"
            choice:
                "mnd6"
            choice:
                "mnd7"
            choice:
                "mnd8"
            choice:
                "mnd9"
            choice:
                "mnd10"
            choice:
                "mnd11"
            choice:
                "mnd12"
            choice:
                "mnd13"
            choice:
                "mnd14"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd3"
            choice:
                "mnd4"
            choice:
                "mnd5"
            choice:
                "mnd6"
            choice:
                "mnd7"
            choice:
                "mnd8"
            choice:
                "mnd9"
            choice:
                "mnd10"
            choice:
                "mnd11"
            choice:
                "mnd12"
            choice:
                "mnd13"
            choice:
                "mnd14"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd3"
            choice:
                "mnd4"
            choice:
                "mnd5"
            choice:
                "mnd6"
            choice:
                "mnd7"
            choice:
                "mnd8"
            choice:
                "mnd9"
            choice:
                "mnd10"
            choice:
                "mnd11"
            choice:
                "mnd12"
            choice:
                "mnd13"
            choice:
                "mnd14"
            pause 0.05
            repeat



    image mnd_lift_colors_psy:
        contains:
            choice:
                "mnd_lift_no_light_red"
            choice:
                "mnd_lift_no_light_green"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_lift_no_light_red"
            choice:
                "mnd_lift_no_light_green"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_lift_no_light_red"
            choice:
                "mnd_lift_no_light_green"
            pause 0.05
            repeat




    image mnd_psy_doll:
        contains:
            choice:
                "mnd_psy_doll_1"
            choice:
                "mnd_psy_doll_2"
            choice:
                "mnd_psy_doll_3"
            pause 0.03
            repeat
        contains:
            choice:
                "mnd_psy_doll_1"
            choice:
                "mnd_psy_doll_2"
            choice:
                "mnd_psy_doll_3"
            pause 0.03
            repeat
        contains:
            choice:
                "mnd_psy_doll_1"
            choice:
                "mnd_psy_doll_2"
            choice:
                "mnd_psy_doll_3"
            pause 0.03
            repeat

    image mnd_ring:
        contains:
            choice:
                "mnd_ring_1"
            choice:
                "mnd_ring_2"
            choice:
                "mnd_ring_3"
            pause 0.03
            repeat
        contains:
            choice:
                "mnd_ring_1"
            choice:
                "mnd_ring_2"
            choice:
                "mnd_ring_3"
            pause 0.03
            repeat
        contains:
            choice:
                "mnd_ring_1"
            choice:
                "mnd_ring_2"
            choice:
                "mnd_ring_3"
            pause 0.03
            repeat


    image mnd_liya_psy_act2:
        contains:
            choice:
                "mnd_liya_psy_a2_1"
            choice:
                "mnd_liya_psy_a2_2"
            choice:
                "mnd_liya_psy_a2_3"
            choice:
                "mnd_liya_psy_a2_4"
            pause 0.03
            repeat
        contains:
            choice:
                "mnd_liya_psy_a2_1"
            choice:
                "mnd_liya_psy_a2_2"
            choice:
                "mnd_liya_psy_a2_3"
            choice:
                "mnd_liya_psy_a2_4"
            pause 0.03
            repeat
        contains:
            choice:
                "mnd_liya_psy_a2_1"
            choice:
                "mnd_liya_psy_a2_2"
            choice:
                "mnd_liya_psy_a2_3"
            choice:
                "mnd_liya_psy_a2_4"
            pause 0.03
            repeat




    image mnd_black_and_white:
        contains:
            choice:
                "mnd"
            choice:
                "black"
            pause 0.03
            repeat
        contains:
            choice:
                "mnd"
            choice:
                "black"
            pause 0.03
            repeat
        contains:
            choice:
                "mnd"
            choice:
                "black"
            pause 0.03
            repeat



    image mnd_ch11_who1_g:
        contains:
            choice:
                "mnd_ch11_who1_g1"
            choice:
                "mnd_ch11_who1_g2"
            choice:
                "mnd_ch11_who1_g3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_ch11_who1_g1"
            choice:
                "mnd_ch11_who1_g2"
            choice:
                "mnd_ch11_who1_g3"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_ch11_who1_g1"
            choice:
                "mnd_ch11_who1_g2"
            choice:
                "mnd_ch11_who1_g3"
            alpha 0.25
            pause 0.05
            repeat







    image mnd_luci_dancing:
        contains:
            "bg mnd_harts"
            xanchor 0.5 yanchor 0.5 xpos 0.48 ypos 0.5 zoom 1.2
            block:
                ease 0.75 xpos 0.5
                ease 0.75 xpos 0.52
                pause 0.5
                ease 0.75 zoom 1.15 xpos 0.525
                ease 0.75 zoom 1.1 xpos 0.53
                pause 0.5
                ease 0.75 xpos 0.5
                ease 0.75 xpos 0.47
                pause 0.5
                ease 0.75 zoom 1.15 xpos 0.475
                ease 0.75 zoom 1.2 xpos 0.48
                pause 0.5
                repeat
        contains:
            "gesmemories/image/spr/luciena/mnd_luci_dance.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 zoom 1.06
            block:
                block:
                    ease 0.25 xpos 0.51
                    ease 0.5 xpos 0.5
                    repeat 2
                pause 0.5
                block:
                    ease 0.25 zoom 1.03
                    ease 0.5 zoom 1.06
                    repeat 2
                pause 0.5
                block:
                    ease 0.25 xpos 0.49
                    ease 0.5 xpos 0.5
                    repeat 2
                pause 0.5
                block:
                    ease 0.25 zoom 1.09
                    ease 0.5 zoom 1.06
                    repeat 2
                pause 0.5
                repeat


    image mnd_liya_dancing:
        contains:
            "bg mnd_harts"
            xanchor 0.5 yanchor 0.5 xpos 0.48 ypos 0.5 zoom 1.2
            block:
                ease 0.75 xpos 0.5
                ease 0.75 xpos 0.52
                pause 0.5
                ease 0.75 zoom 1.15 xpos 0.525
                ease 0.75 zoom 1.1 xpos 0.53
                pause 0.5
                ease 0.75 xpos 0.5
                ease 0.75 xpos 0.47
                pause 0.5
                ease 0.75 zoom 1.15 xpos 0.475
                ease 0.75 zoom 1.2 xpos 0.48
                pause 0.5
                repeat
        contains:
            "gesmemories/image/spr/liya/mnd_liya_dance.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 zoom 1.06
            block:
                block:
                    ease 0.25 xpos 0.51
                    ease 0.5 xpos 0.5
                    repeat 2
                pause 0.5
                block:
                    ease 0.25 zoom 1.03
                    ease 0.5 zoom 1.06
                    repeat 2
                pause 0.5
                block:
                    ease 0.25 xpos 0.49
                    ease 0.5 xpos 0.5
                    repeat 2
                pause 0.5
                block:
                    ease 0.25 zoom 1.09
                    ease 0.5 zoom 1.06
                    repeat 2
                pause 0.5
                repeat


    image bg mnd_liya_dancing:
        contains:
            "bg mnd_harts"
            xanchor 0.5 yanchor 0.5 xpos 0.48 ypos 0.5 zoom 1.2
            block:
                ease 0.75 xpos 0.5
                ease 0.75 xpos 0.52
                pause 0.5
                ease 0.75 zoom 1.15 xpos 0.525
                ease 0.75 zoom 1.1 xpos 0.53
                pause 0.5
                ease 0.75 xpos 0.5
                ease 0.75 xpos 0.47
                pause 0.5
                ease 0.75 zoom 1.15 xpos 0.475
                ease 0.75 zoom 1.2 xpos 0.48
                pause 0.5
                repeat
        contains:
            "gesmemories/image/spr/liya/mnd_liya_dance.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 zoom 1.06
            block:
                block:
                    ease 0.25 xpos 0.51
                    ease 0.5 xpos 0.5
                    repeat 2
                pause 0.5
                block:
                    ease 0.25 zoom 1.03
                    ease 0.5 zoom 1.06
                    repeat 2
                pause 0.5
                block:
                    ease 0.25 xpos 0.49
                    ease 0.5 xpos 0.5
                    repeat 2
                pause 0.5
                block:
                    ease 0.25 zoom 1.09
                    ease 0.5 zoom 1.06
                    repeat 2
                pause 0.5
                repeat









    #HARTSBG
    image bg mnd_harts:
        contains:
            "gesmemories/image/scene/mnd_harts_1.png"
        contains:
            "gesmemories/image/scene/mnd_harts_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat




    image bg mnd_16_himori_bg:
        contains:
            "gesmemories/image/scene/mnd_16_himori_bg_1.png"
        contains:
            "gesmemories/image/scene/mnd_16_himori_bg_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat



    image mndoldsmertcg_remake:
        contains:
            "gesmemories/image/scene/mndoldsmertcg_1.png"
        contains:
            "gesmemories/image/scene/mndoldsmertcg_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat







    image bg mnd_ch11_bg2:
        contains:
            "gesmemories/image/trymemo/mnd_ch11_bg2_1.png"
        contains:
            "gesmemories/image/trymemo/mnd_ch11_bg2_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat




    image mnd_a3_menu_3:
        contains:
            "gesmemories/image/logo/mnd_a3_menu_3_1.png"
        contains:
            "gesmemories/image/logo/mnd_a3_menu_3_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat

















    image mnd_psy_lift_numbers:
        contains:
            choice:
                "mnd_lift_psy_1"
            choice:
                "mnd_lift_psy_2"
            choice:
                "mnd_lift_psy_3"
            choice:
                "mnd_lift_psy_4"
            choice:
                "mnd_lift_psy_5"
            choice:
                "mnd_lift_psy_6"
            choice:
                "mnd_lift_psy_7"
            choice:
                "mnd_lift_psy_8"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_lift_psy_1"
            choice:
                "mnd_lift_psy_2"
            choice:
                "mnd_lift_psy_3"
            choice:
                "mnd_lift_psy_4"
            choice:
                "mnd_lift_psy_5"
            choice:
                "mnd_lift_psy_6"
            choice:
                "mnd_lift_psy_7"
            choice:
                "mnd_lift_psy_8"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_lift_psy_1"
            choice:
                "mnd_lift_psy_2"
            choice:
                "mnd_lift_psy_3"
            choice:
                "mnd_lift_psy_4"
            choice:
                "mnd_lift_psy_5"
            choice:
                "mnd_lift_psy_6"
            choice:
                "mnd_lift_psy_7"
            choice:
                "mnd_lift_psy_8"
            pause 0.05
            repeat







    image mnd_liya_psy_noise:
        contains:
            choice:
                "mnd_liya_psy_noise_1"
            choice:
                "mnd_liya_psy_noise_2"
            choice:
                "mnd_liya_psy_noise_3"
            choice:
                "mnd_liya_psy_noise_4"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_liya_psy_noise_1"
            choice:
                "mnd_liya_psy_noise_2"
            choice:
                "mnd_liya_psy_noise_3"
            choice:
                "mnd_liya_psy_noise_4"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_liya_psy_noise_1"
            choice:
                "mnd_liya_psy_noise_2"
            choice:
                "mnd_liya_psy_noise_3"
            choice:
                "mnd_liya_psy_noise_4"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_liya_psy_noise_1"
            choice:
                "mnd_liya_psy_noise_2"
            choice:
                "mnd_liya_psy_noise_3"
            choice:
                "mnd_liya_psy_noise_4"
            pause 0.05
            repeat







    image mnd_ftr_room2_1:
        contains:
            choice:
                "mnd_ftr_2_x_1"
            choice:
                "mnd_ftr_2_x_2"
            choice:
                "mnd_ftr_2_x_3"
            choice:
                "mnd_ftr_2_x_4"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_ftr_2_x_1"
            choice:
                "mnd_ftr_2_x_2"
            choice:
                "mnd_ftr_2_x_3"
            choice:
                "mnd_ftr_2_x_4"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_ftr_2_x_1"
            choice:
                "mnd_ftr_2_x_2"
            choice:
                "mnd_ftr_2_x_3"
            choice:
                "mnd_ftr_2_x_4"
            pause 0.05
            repeat


    image mnd_ftr_room2_2:
        contains:
            choice:
                "mnd_ftr_2_x_5"
            choice:
                "mnd_ftr_2_x_6"
            choice:
                "mnd_ftr_2_x_7"
            choice:
                "mnd_ftr_2_x_8"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_ftr_2_x_5"
            choice:
                "mnd_ftr_2_x_6"
            choice:
                "mnd_ftr_2_x_7"
            choice:
                "mnd_ftr_2_x_8"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_ftr_2_x_5"
            choice:
                "mnd_ftr_2_x_6"
            choice:
                "mnd_ftr_2_x_7"
            choice:
                "mnd_ftr_2_x_8"
            pause 0.05
            repeat




    image mnd_ftr_room3_1:
        contains:
            choice:
                "mnd_ftr_3_p_1"
            choice:
                "mnd_ftr_3_p_2"
            choice:
                "mnd_ftr_3_p_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_ftr_3_p_1"
            choice:
                "mnd_ftr_3_p_2"
            choice:
                "mnd_ftr_3_p_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_ftr_3_p_1"
            choice:
                "mnd_ftr_3_p_2"
            choice:
                "mnd_ftr_3_p_3"
            pause 0.05
            repeat

    image mnd_ftr_room3_2:
        contains:
            choice:
                "mnd_ftr_3_h_1"
            choice:
                "mnd_ftr_3_h_2"
            choice:
                "mnd_ftr_3_h_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_ftr_3_h_1"
            choice:
                "mnd_ftr_3_h_2"
            choice:
                "mnd_ftr_3_h_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_ftr_3_h_1"
            choice:
                "mnd_ftr_3_h_2"
            choice:
                "mnd_ftr_3_h_3"
            pause 0.05
            repeat




    image mnd_dead_vas_coridor_1_2_an:
        contains:
            choice:
                "mnd_dead_vas_cor_psy1"
            choice:
                "mnd_dead_vas_cor_psy2"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_dead_vas_cor_psy1"
            choice:
                "mnd_dead_vas_cor_psy2"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_dead_vas_cor_psy1"
            choice:
                "mnd_dead_vas_cor_psy2"
            pause 0.05
            repeat






    image mnd_diologue_a2:
        contains:
            choice:
                "mnd_psy_and_vas_dio_g1"
            choice:
                "mnd_psy_and_vas_dio_g2"
            choice:
                "mnd_psy_and_vas_dio_g3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_psy_and_vas_dio_g1"
            choice:
                "mnd_psy_and_vas_dio_g2"
            choice:
                "mnd_psy_and_vas_dio_g3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_psy_and_vas_dio_g1"
            choice:
                "mnd_psy_and_vas_dio_g2"
            choice:
                "mnd_psy_and_vas_dio_g3"
            pause 0.05
            repeat




    image mnd_10f_w_mag:
        contains:
            choice:
                "mnd_10f_w_mag_1"
            choice:
                "mnd_10f_w_mag_2"
            choice:
                "mnd_10f_w_mag_3"
            pause 0.10
            repeat
        contains:
            choice:
                "mnd_10f_w_mag_1"
            choice:
                "mnd_10f_w_mag_2"
            choice:
                "mnd_10f_w_mag_3"
            pause 0.10
            repeat
        contains:
            choice:
                "mnd_10f_w_mag_1"
            choice:
                "mnd_10f_w_mag_2"
            choice:
                "mnd_10f_w_mag_3"
            pause 0.10
            repeat
















    image mnd_c10_1h_room_eff:
        contains:
            choice:
                "mnd_c10_1h_room_eff_1"
            choice:
                "mnd_c10_1h_room_eff_2"
            choice:
                "mnd_c10_1h_room_eff_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_c10_1h_room_eff_1"
            choice:
                "mnd_c10_1h_room_eff_2"
            choice:
                "mnd_c10_1h_room_eff_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_c10_1h_room_eff_1"
            choice:
                "mnd_c10_1h_room_eff_2"
            choice:
                "mnd_c10_1h_room_eff_3"
            pause 0.05
            repeat




    image mnd_c10_r1_mess:
        contains:
            choice:
                "mnd_c10_r1_mess_1"
            choice:
                "mnd_c10_r1_mess_2"
            choice:
                "mnd_c10_r1_mess_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_c10_r1_mess_1"
            choice:
                "mnd_c10_r1_mess_2"
            choice:
                "mnd_c10_r1_mess_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_c10_r1_mess_1"
            choice:
                "mnd_c10_r1_mess_2"
            choice:
                "mnd_c10_r1_mess_3"
            pause 0.05
            repeat



    image mnd_10_c2_lp_ld_sspr:
        contains:
            choice:
                "mnd_10_c2_lp_ld_sspr_1"
            choice:
                "mnd_10_c2_lp_ld_sspr_2"
            choice:
                "mnd_10_c2_lp_ld_sspr_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_10_c2_lp_ld_sspr_1"
            choice:
                "mnd_10_c2_lp_ld_sspr_2"
            choice:
                "mnd_10_c2_lp_ld_sspr_3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_10_c2_lp_ld_sspr_1"
            choice:
                "mnd_10_c2_lp_ld_sspr_2"
            choice:
                "mnd_10_c2_lp_ld_sspr_3"
            pause 0.05
            repeat



    image mnd_10_c2_lp_ld_sbg:
        contains:
            choice:
                "mnd_10_c2_lp_ld_sbg_a1"
            choice:
                "mnd_10_c2_lp_ld_sbg_a2"
            choice:
                "mnd_10_c2_lp_ld_sbg_a3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_10_c2_lp_ld_sbg_a1"
            choice:
                "mnd_10_c2_lp_ld_sbg_a2"
            choice:
                "mnd_10_c2_lp_ld_sbg_a3"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_10_c2_lp_ld_sbg_a1"
            choice:
                "mnd_10_c2_lp_ld_sbg_a2"
            choice:
                "mnd_10_c2_lp_ld_sbg_a3"
            pause 0.05
            repeat



    image mnd_load_scr:
        contains:
            choice:
                "mnd_load_scr_1"
            choice:
                "mnd_load_scr_2"
            choice:
                "mnd_load_scr_3"
            choice:
                "mnd_load_scr_4"
            choice:
                "mnd_load_scr_5"
            choice:
                "mnd_load_scr_6"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_load_scr_1"
            choice:
                "mnd_load_scr_2"
            choice:
                "mnd_load_scr_3"
            choice:
                "mnd_load_scr_4"
            choice:
                "mnd_load_scr_5"
            choice:
                "mnd_load_scr_6"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd_load_scr_1"
            choice:
                "mnd_load_scr_2"
            choice:
                "mnd_load_scr_3"
            choice:
                "mnd_load_scr_4"
            choice:
                "mnd_load_scr_5"
            choice:
                "mnd_load_scr_6"
            pause 0.05
            repeat



    image him_p_12:
        contains:
            choice:
                "him_p_12_1"
            choice:
                "him_p_12_2"
            pause 0.05
            repeat
        contains:
            choice:
                "him_p_12_1"
            choice:
                "him_p_12_2"
            pause 0.05
            repeat
        contains:
            choice:
                "him_p_12_1"
            choice:
                "him_p_12_2"
            pause 0.05
            repeat






    image overlay mndliyapsybg22:
        contains:
            choice:
                "mnd1"
            choice:
                "mnd2"
            choice:
                "lmhit22"
            choice:
                "mndliyadead22"
            choice:
                "lastkiss22"
            choice:
                "liliyainblood22"
            choice:
                "invanna22"
            choice:
                "invannablood22"
            choice:
                "mndbloodfull22"
            choice:
                "finalfirstpsy22"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd1"
            choice:
                "mnd2"
            choice:
                "lmhit22"
            choice:
                "mndliyadead22"
            choice:
                "lastkiss22"
            choice:
                "liliyainblood22"
            choice:
                "invanna22"
            choice:
                "invannablood22"
            choice:
                "mndbloodfull22"
            choice:
                "finalfirstpsy22"
            pause 0.05
            repeat
        contains:
            choice:
                "mnd1"
            choice:
                "mnd2"
            choice:
                "lmhit22"
            choice:
                "mndliyadead22"
            choice:
                "lastkiss22"
            choice:
                "liliyainblood22"
            choice:
                "invanna22"
            choice:
                "invannablood22"
            choice:
                "mndbloodfull22"
            choice:
                "finalfirstpsy22"
            pause 0.05
            repeat





    
    



    image overlay mnd_snow_ccr: #Вправо вниз-вниз
        xzoom 1
        contains:
            "gesmemories/image/logo/mnd_snow.png"
            xanchor 0.5 yanchor 0.75 xpos 0.5 ypos 0.5 alpha 0.5
            linear 0.5 xanchor 0.4 yanchor 0.25
            repeat
        contains:
            "gesmemories/image/logo/mnd_snow.png"
            xanchor 0.6 yanchor 0.75 xpos 0.5 ypos 0.5 zoom 0.9 alpha 0.5
            linear 0.75 xanchor 0.5 yanchor 0.25
            repeat
        contains:
            "gesmemories/image/logo/mnd_snow.png"
            xanchor 075 yanchor 0.7 xpos 0.5 ypos 0.5 zoom 0.8 alpha 0.5
            linear 1.0 xanchor 0.65 yanchor 0.3
            repeat





    image overlay mnd_memory_back_1:
        contains:
            parallel:
                choice:
                    "gesmemories/image/logo/mnd_o_1.png"
                choice:
                    "gesmemories/image/logo/mnd_o_2.png"
                choice:
                    "gesmemories/image/logo/mnd_o_3.png"
                choice:
                    "gesmemories/image/logo/mnd_o_4.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat



    image overlay mnd_chap6_hp:
        contains:
            parallel:
                choice:
                    "gesmemories/image/logo/mnd_ch6_hp_1.png"
                choice:
                    "gesmemories/image/logo/mnd_ch6_hp_2.png"
                choice:
                    "gesmemories/image/logo/mnd_ch6_hp_3.png"
                choice:
                    "gesmemories/image/logo/mnd_o_4.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat







    image prologue_dream:
        contains:
            parallel:
                choice:
                    "gesmemories/image/logo/mnd_prologue_1.png"
                choice:
                    "gesmemories/image/logo/mnd_prologue_2.png"
                choice:
                    "gesmemories/image/logo/mnd_prologue_3.png"
                choice:
                    "gesmemories/image/logo/mnd_o_4.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat


    image mnd_move_1:
        contains:
            "bg 4roomd"
            zoom 1.1 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 10.0 xalign 1.0 yalign 0.4
        contains:
            parallel:
                choice:
                    "gesmemories/image/logo/mnd_o_1.png"
                choice:
                    "gesmemories/image/logo/mnd_o_2.png"
                choice:
                    "gesmemories/image/logo/mnd_o_3.png"
                choice:
                    "gesmemories/image/logo/mnd_o_4.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat



    image mnd_move_2:
        contains:
            "bg mndascor"
            zoom 1.1 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 10.0 xalign 1.0 yalign 0.4
        contains:
            parallel:
                choice:
                    "gesmemories/image/logo/mnd_o_1.png"
                choice:
                    "gesmemories/image/logo/mnd_o_2.png"
                choice:
                    "gesmemories/image/logo/mnd_o_3.png"
                choice:
                    "gesmemories/image/logo/mnd_o_4.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat




    image mnd_move_3:
        contains:
            "bg 8room"
            zoom 1.1 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 10.0 xalign 1.0 yalign 0.4
        contains:
            parallel:
                choice:
                    "gesmemories/image/logo/mnd_o_1.png"
                choice:
                    "gesmemories/image/logo/mnd_o_2.png"
                choice:
                    "gesmemories/image/logo/mnd_o_3.png"
                choice:
                    "gesmemories/image/logo/mnd_o_4.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat

    image mnd_move_4:
        contains:
            "mnd_ist_doc_cab"
            zoom 1.1 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 10.0 xalign 1.0 yalign 0.4
        contains:
            parallel:
                choice:
                    "gesmemories/image/logo/mnd_o_1.png"
                choice:
                    "gesmemories/image/logo/mnd_o_2.png"
                choice:
                    "gesmemories/image/logo/mnd_o_3.png"
                choice:
                    "gesmemories/image/logo/mnd_o_4.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat


    image mnd_move_5:
        contains:
            "bg mnd_wite_cor_normal"
            zoom 1.1 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 10.0 xalign 1.0 yalign 0.4
        contains:
            parallel:
                choice:
                    "gesmemories/image/logo/mnd_o_1.png"
                choice:
                    "gesmemories/image/logo/mnd_o_2.png"
                choice:
                    "gesmemories/image/logo/mnd_o_3.png"
                choice:
                    "gesmemories/image/logo/mnd_o_4.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat


    image mnd_move_6:
        contains:
            "bg mndroofnoara"
            zoom 1.1 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 10.0 xalign 1.0 yalign 0.4
        contains:
            parallel:
                choice:
                    "gesmemories/image/logo/mnd_o_1.png"
                choice:
                    "gesmemories/image/logo/mnd_o_2.png"
                choice:
                    "gesmemories/image/logo/mnd_o_3.png"
                choice:
                    "gesmemories/image/logo/mnd_o_4.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat


    image mnd_move_7:
        contains:
            "mnd_c9_sbg_1"
            zoom 1.1 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 10.0 xalign 1.0 yalign 0.4
        contains:
            parallel:
                choice:
                    "gesmemories/image/logo/mnd_o_1.png"
                choice:
                    "gesmemories/image/logo/mnd_o_2.png"
                choice:
                    "gesmemories/image/logo/mnd_o_3.png"
                choice:
                    "gesmemories/image/logo/mnd_o_4.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat



    image mnd_move_8:
        contains:
            "mnd_c9_sbg_2"
            zoom 1.1 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 10.0 xalign 1.0 yalign 0.4
        contains:
            parallel:
                choice:
                    "gesmemories/image/logo/mnd_o_1.png"
                choice:
                    "gesmemories/image/logo/mnd_o_2.png"
                choice:
                    "gesmemories/image/logo/mnd_o_3.png"
                choice:
                    "gesmemories/image/logo/mnd_o_4.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat



    image mnd_sb_mm_mf:
        contains:
            "gesmemories/image/logo/mnd_sb_mm_mf_1.png"
        contains:
            "gesmemories/image/logo/mnd_sb_mm_mf_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat



    image bg carride:
        contains:
            "gesmemories/image/bg/carride1.png"
        contains:
            "gesmemories/image/bg/carride2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat


    image bg carride1:
        contains:
            "gesmemories/image/bg/carride1_1.png"
        contains:
            "gesmemories/image/bg/carride1_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat

    image carride1_fw:
        contains:
            "gesmemories/image/bg/carride1_fw_1.png"
        contains:
            "gesmemories/image/bg/carride1_fw_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat






label gesundheitmemories:
    scene black 
    with Pause(1)
    play sound mnd_floor_amb
    play ambience mnd_coridors_ambience_1 fadein 8
    $ renpy.pause(4, hard=True)
    stop sound fadeout 3
    play sound2 mnd_r_creak
    scene bg mnd_r_int_bg_1 with dissolve2
    $ renpy.pause(1, hard=True)
    play sound mnd_r_creak2
    scene bg mnd_r_int_bg_2 with dissolve
    $ renpy.pause(0.5, hard=True)
    play sound mnd_r_vine
    scene bg mnd_r_int_bg_3 with dissolve2
    $ renpy.pause(0.5, hard=True)
    stop sound fadeout 2
    scene black
    show mnd_r_tv_log
    with fade3
    $ renpy.pause(1.5, hard=True)
    play sound mnd_tv_noise
    show mnd_r_ges_spl behind mnd_r_tv_log
    show overlay mnd_memory_back_1 behind mnd_r_tv_log
    with dissolve2
    $ renpy.pause(2.5, hard=True)
    stop sound fadeout 3
    stop ambience fadeout 4
    scene black with fade3
    show mnd_new_dis_2 with dissolve2
    $ renpy.pause(6.5, hard=True)
    scene black with fade2
    show mnd_new_dis_3 with dissolve2
    $ renpy.pause(4.5, hard=True)
    jump mnd_menu3s
label mnd_start_of_titr1:
    scene black with dissolve2
    if(renpy.seen_label("mnd_chapter_1")):
        jump mnd_menu
    jump mnd_first_run_menu

label mnd_first_run_menu:
    play music mndmemodead fadein 4
    scene bg mnd_sb_mm_mf_bg
    show mndrain2_r
    show mnd_sb_mm_mf_spr
    show mnd_sb_mm_mf
    with dissolve4
    $ renpy.pause(1.5, hard=True)
    call screen mndfirstmenu with dissolve2
screen mndfirstmenu:
    tag menu 
    modal True
    imagemap: 
        ground "gesmemories/image/logo/mnd_menu1sh_n.png" 
        hover  "gesmemories/image/logo/mnd_menu1sh_y.png"  
        alpha True

        hotspot (0, 305, 494, 103) clicked[Play("gesmemories/snd/sfx/mndstart.wav"),Jump("gesmnds")] hovered[Play(mndroll)]
        hotspot (0,781, 344, 78) clicked[Play("gesmemories/snd/sfx/mdnquit.wav"),Quit(confirm=True)] hovered[Play(mndroll)]



label mnd_menu:
    $_game_menu_screen = "game_menu_selector"
    $ renpy.block_rollback()
    scene black
    show bg menu_mnd
    show expression (MndMenuCh().sm) as mndmenuch
    with dissolve2
    call screen mndmenu with dissolve2
screen mndmenu:
    tag menu 
    modal True
    imagemap: 
        ground "gesmemories/image/logo/mhoff.png" 
        hover  "gesmemories/image/logo/mhon.png"  
        alpha True

        hotspot (42, 100, 482, 425) clicked[Play("gesmemories/snd/sfx/mndstart.wav"),Jump("gesmnds")] hovered[Play(mndroll)]
        hotspot (1442, 320, 1920, 648) clicked[Play("gesmemories/snd/psy/mndpsyeff1.mp3"),Jump("gesmndchsel1")] hovered[Play(mndroll)]
        hotspot (46,525,463,722) clicked[Play("gesmemories/snd/sfx/mdnquit.wav"),Quit(confirm=True)] hovered[Play(mndroll)]


label gesmndactsel:
    scene black
    scene bg mndascorn
    show expression (MndMenuCh().sm) as mndmenuch
    with dissolve2
    call screen mndactselect with dissolve2
screen mndactselect:
    tag menu 
    modal True
    imagemap: 
        ground "gesmemories/image/logo/mnd_act_nh.png" 
        hover  "gesmemories/image/logo/mnd_act_yh.png"  
        alpha True

        hotspot (279, 138, 1539, 90) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("gesmndchsel1")] hovered[Play(mndroll)]
        hotspot (279, 354, 1333, 90) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("gesmndchsel2")] hovered[Play(mndroll)]
        hotspot (279, 535, 1333, 110) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("gesmndchsel3")] hovered[Play(mndroll)]
        hotspot (269, 724, 1549, 115) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("gesmndchsel4")] hovered[Play(mndroll)]
        hotspot (37, 958, 163, 63) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_2.ogg"),Jump("mnd_menu3s")] hovered[Play(mndroll)]



    #АКТ СКРИН 2 МЕНЮ
label gesmndactsel_m2:
    scene black
    scene bg llkstr
    show mndrain2_c
    with dissolve2
    call screen mndactselect2 with dissolve2
screen mndactselect2:
    tag menu 
    modal True
    imagemap: 
        ground "gesmemories/image/logo/mnd_act_nh.png" 
        hover  "gesmemories/image/logo/mnd_act_yh.png"  
        alpha True

        hotspot (279, 138, 1539, 76) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("gesmndchsel1_m2")] hovered[Play(mndroll)]
        hotspot (279, 354, 1333, 84) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("gesmndchsel2_m2")] hovered[Play(mndroll)]
        hotspot (37, 958, 163, 63) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_2.ogg"),Jump("mnd_menu2")] hovered[Play(mndroll)]


label gesmndchsel2_m2:
    scene black
    scene bg llkstr
    show mndrain2_c
    with dissolve2
    call screen mndchapselect2 with dissolve2
screen mndchapselect2:
    tag menu 
    modal True
    imagemap: 
        ground "gesmemories/image/logo/mnd_chs2_nh.png" 
        hover  "gesmemories/image/logo/mnd_chs2_yh.png"  
        alpha True

        hotspot (279, 138, 1539, 90) clicked[Play("gesmemories/snd/sfx/sub_kettei2.ogg"),Jump("mnd_act2_ch7")] hovered[Play(mndroll)]
        hotspot (276, 275, 1521, 90) clicked[Play("gesmemories/snd/sfx/sub_kettei2.ogg"),Jump("mnd_chapter8")] hovered[Play(mndroll)]
        hotspot (276, 403, 1472, 90) clicked[Play("gesmemories/snd/sfx/sub_kettei2.ogg"),Jump("mnd_chapter9")] hovered[Play(mndroll)]
        hotspot (37, 958, 163, 63) clicked[Play("gesmemories/snd/sfx/sub_kettei2.ogg"),Jump("mnd_menu2")] hovered[Play(mndroll)]





label gesmndchsel1_m2:
    scene black
    scene bg llkstr
    show mndrain2_c
    with dissolve2
    call screen mndchapselect22 with dissolve2
screen mndchapselect22:
    tag menu 
    modal True
    imagemap: 
        ground "gesmemories/image/logo/mnd_chs_nh.png" 
        hover  "gesmemories/image/logo/mnd_chs_yh.png"  
        alpha True

        hotspot (279, 138, 1539, 76) clicked[Play("gesmemories/snd/sfx/sub_kettei2.ogg"),Jump("mnd_chapter_1")] hovered[Play(mndroll)]
        hotspot (279, 243, 1018, 88) clicked[Play("gesmemories/snd/sfx/sub_kettei2.ogg"),Jump("mnd_chapter2")] hovered[Play(mndroll)]
        hotspot (279, 354, 1333, 84) clicked[Play("gesmemories/snd/sfx/sub_kettei2.ogg"),Jump("mnd_chapter3")] hovered[Play(mndroll)]
        hotspot (279, 460, 1428, 93) clicked[Play("gesmemories/snd/sfx/sub_kettei2.ogg"),Jump("mnd_chapter4")] hovered[Play(mndroll)]
        hotspot (279, 567, 1018, 91) clicked[Play("gesmemories/snd/sfx/sub_kettei2.ogg"),Jump("mnd_chapter5")] hovered[Play(mndroll)]
        hotspot (279, 675, 1255, 85) clicked[Play("gesmemories/snd/sfx/sub_kettei2.ogg"),Jump("mnd_chapter6")] hovered[Play(mndroll)]
        hotspot (37, 958, 163, 63) clicked[Play("gesmemories/snd/sfx/sub_kettei2.ogg"),Jump("mnd_menu2")] hovered[Play(mndroll)]
    #####






label gesmndchsel2:
    scene black
    scene bg mndpsydoor
    show expression (MndMenuCh().sm) as mndmenuch
    with dissolve2
    call screen mndchapselect2 with dissolve2
screen mndchapselect2:
    tag menu 
    modal True
    imagemap: 
        ground "gesmemories/image/logo/mnd_chs2_nh.png" 
        hover  "gesmemories/image/logo/mnd_chs2_yh.png"  
        alpha True

        hotspot (279, 138, 1539, 90) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("mnd_act2_ch7")] hovered[Play(mndroll)]
        hotspot (276, 275, 1521, 90) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("mnd_chapter8")] hovered[Play(mndroll)]
        hotspot (276, 403, 1472, 90) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("mnd_chapter9")] hovered[Play(mndroll)]
        hotspot (260, 555, 1344, 112) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("mnd_chapter_10")] hovered[Play(mndroll)]
        hotspot (37, 958, 163, 63) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_2.ogg"),Jump("mnd_menu3s")] hovered[Play(mndroll)]




label gesmndchsel3:
    scene black
    scene bg mndroofnoara
    show mndrain2_r
    with dissolve2
    call screen mndchapselect3 with dissolve2
screen mndchapselect3:
    tag menu 
    modal True
    imagemap: 
        ground "gesmemories/image/logo/mnd_chs3_nh.png" 
        hover  "gesmemories/image/logo/mnd_chs3_yh.png"  
        alpha True

        hotspot (279, 138, 1539, 90) clicked[Play("gesmemories/snd/sfx/flashback.ogg"),Jump("mnd_chapter_11")] hovered[Play(mndroll)]
        hotspot (276, 275, 1559, 90) clicked[Play("gesmemories/snd/sfx/flashback.ogg"),Jump("mnd_chapter_12")] hovered[Play(mndroll)]
        hotspot (276, 403, 1472, 90) clicked[Play("gesmemories/snd/sfx/flashback.ogg"),Jump("mnd_chapter_13")] hovered[Play(mndroll)]
        hotspot (260, 555, 1539, 112) clicked[Play("gesmemories/snd/sfx/flashback.ogg"),Jump("mnd_chapter_14")] hovered[Play(mndroll)]
        hotspot (37, 958, 163, 63) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_2.ogg"),Jump("mnd_menu3s")] hovered[Play(mndroll)]



label gesmndchsel4:
    scene black
    scene bg mnd_a2_ch7_cor_1
    show expression (MndMenuCh().sm) as mndmenuch
    with dissolve2
    call screen mndchapselect4 with dissolve2
screen mndchapselect4:
    tag menu 
    modal True
    imagemap: 
        ground "gesmemories/image/logo/mnd_chs4_nh.png" 
        hover  "gesmemories/image/logo/mnd_chs4_yh.png"  
        alpha True

        hotspot (259, 138, 1539, 90) clicked[Play("gesmemories/snd/sfx/flashback.ogg"),Jump("mnd_chapter_15")] hovered[Play(mndroll)]
        hotspot (259, 275, 1579, 90) clicked[Play("gesmemories/snd/sfx/flashback.ogg"),Jump("mnd_chapter_16")] hovered[Play(mndroll)]
        hotspot (276, 403, 1472, 90) clicked[Play("gesmemories/snd/sfx/flashback.ogg"),Jump("mnd_chapter_17")] hovered[Play(mndroll)]
        hotspot (276, 555, 1539, 112) clicked[Play("gesmemories/snd/sfx/flashback.ogg"),Jump("mnd_chapter_18")] hovered[Play(mndroll)]
        hotspot (37, 958, 163, 63) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_2.ogg"),Jump("mnd_menu3s")] hovered[Play(mndroll)]



















label gesmndchsel1:
    scene black
    scene bg mndascorn
    show expression (MndMenuCh().sm) as mndmenuch
    with dissolve2
    call screen mndchapselect with dissolve2
screen mndchapselect:
    tag menu 
    modal True
    imagemap: 
        ground "gesmemories/image/logo/mnd_chs_nh.png" 
        hover  "gesmemories/image/logo/mnd_chs_yh.png"  
        alpha True

        hotspot (279, 138, 1539, 76) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("mnd_chapter_1")] hovered[Play(mndroll)]
        hotspot (279, 243, 1018, 88) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("mnd_chapter2")] hovered[Play(mndroll)]
        hotspot (279, 354, 1333, 84) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("mnd_chapter3")] hovered[Play(mndroll)]
        hotspot (279, 460, 1428, 93) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("mnd_chapter4")] hovered[Play(mndroll)]
        hotspot (279, 567, 1018, 91) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("mnd_chapter5")] hovered[Play(mndroll)]
        hotspot (279, 675, 1255, 85) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_1.ogg"),Jump("mnd_chapter6")] hovered[Play(mndroll)]
        hotspot (37, 958, 163, 63) clicked[Play("gesmemories/snd/sfx/mnd_piano_lie_2.ogg"),Jump("mnd_menu")] hovered[Play(mndroll)]




label mnd_menu2s:
    $_game_menu_screen = "game_menu_selector"
    scene black
    $ renpy.pause(4, hard=True)
    $ renpy.block_rollback()
    scene black
    show expression (MndMenuCh().sm) as mndmenuch
    with dissolve2
    show menu_mnd2
    show mndrain_c
    with dissolve2
    call screen mndmenu2 with dissolve2
screen mndmenu2:
    tag menu 
    modal True
    imagemap: 
        ground "gesmemories/image/logo/mnd_menu2h_n.png" 
        hover  "gesmemories/image/logo/mnd_menu2h_y.png"  
        alpha True

        hotspot (0, 305, 494, 103) clicked[Play("gesmemories/snd/sfx/mndstart.wav"),Jump("gesmnds")] hovered[Play(mndroll)]
        hotspot (0, 545, 432, 89) clicked[Play("gesmemories/snd/psy/mndpsyeff1.mp3"),Jump("gesmndactsel")] hovered[Play(mndroll)]
        hotspot (0,781, 344, 78) clicked[Play("gesmemories/snd/sfx/mdnquit.wav"),Quit(confirm=True)] hovered[Play(mndroll)]




label mnd_menu3s:
    $_game_menu_screen = "game_menu_selector"
    scene black with dissolve2
    play music mnd_a3_menu fadein 5
    $ renpy.pause(6, hard=True)
    $ renpy.block_rollback()
    show mnd_a3_menu_1
    show mnd_a3_menu_2
    show mnd_a3_menu_3
    show mndrain_l
    with dissolve4
label mnd_menu3sfff:
    call screen mndmenu2 with dissolve2
screen mndmenu2:
    tag menu
    modal True
    imagemap: 
        ground "gesmemories/image/logo/mnd_menu_r_h_n.png" 
        hover  "gesmemories/image/logo/mnd_menu_r_h_y.png"  
        alpha True

        hotspot (0, 343, 486, 103) clicked[Jump("gesmnds")]
        hotspot (0, 492, 432, 89) action ShowMenu ("load")
        hotspot (0,639, 344, 90) clicked[Quit(confirm=True)]
        hotspot (0,799, 392, 117) action ShowMenu ("preferences")




