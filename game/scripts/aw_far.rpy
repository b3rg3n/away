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
            "gesmemories/image/logo/mnd_ham_list1.webp"
        choice:
            "gesmemories/image/logo/mnd_ham_list2.webp"
        choice:
            "gesmemories/image/logo/mnd_ham_list3.webp"
        choice:
            "gesmemories/image/logo/mnd_ham_list4.webp"
        choice:
            "gesmemories/image/logo/mnd_ham_list5.webp"
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
            "gesmemories/image/logo/mnd_liya_lep_1.webp"
        choice:
            "gesmemories/image/logo/mnd_liya_lep_2.webp"
        choice:
            "gesmemories/image/logo/mnd_liya_lep_3.webp"
        choice:
            "gesmemories/image/logo/mnd_liya_lep_4.webp"
        choice:
            "gesmemories/image/logo/mnd_liya_lep_5.webp"
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

    $ mnd_dissolve_hands = ImageDissolve("gesmemories/image/spr/old/zmey/hands_dissolve.webp", 2.5, 100, alpha=True)

    image zmey_hands_stars:
        "gesmemories/image/spr/old/zmey/hands_stars1.webp" with Dissolve(2.0, alpha=True)
        pause 2.0
        "gesmemories/image/spr/old/zmey/hands_stars2.webp" with Dissolve(2.0, alpha=True)
        pause 2.0
        "gesmemories/image/spr/old/zmey/hands_stars3.webp" with Dissolve(2.0, alpha=True)
        pause 2.0
        "gesmemories/image/spr/old/zmey/hands_stars4.webp" with Dissolve(2.0, alpha=True)
        pause 2.0
        repeat

    image zmey_hands_hands:
        "gesmemories/image/spr/old/zmey/hands.webp" with mnd_dissolve_hands
        pause 2.5
        "gesmemories/image/spr/old/zmey/hands2.webp" with mnd_dissolve_hands
        pause 2.5
        repeat

    image zmey_hands:
        contains:
            "gesmemories/image/spr/old/zmey/mndzmey.webp"
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
                if( i.startswith("gesmemories/snd/"+dir+"/") and i.endswith((".ogg", ".ogg", ".ogg"))):
                    gl = globals()
                    gl[(str(i[len("gesmemories/snd/"+dir+"/"):-4]))] = i




init python:

    import math
    class FireGlowDot(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = [ ]
            self.rd = "gesmemories/image/logo/firedrop.webp"

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
            self.rd = "gesmemories/image/logo/mndlist.webp"

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
            self.rd = "gesmemories/image/logo/chast1.webp"

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
            self.rd = "gesmemories/image/scene/cutm.webp"

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
            self.rd = "gesmemories/image/logo/fish_drop.webp"

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
            self.rd = "away/img/eff/aw_km_st_1.webp"
            self.rd = "away/img/eff/aw_km_st_2.webp"
            self.rd = "away/img/eff/aw_km_st_1.webp"

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



    $ mndmenutheme = "gesmemories/snd/mp3/mndmenutheme.ogg"
    $ mnd_longing = "gesmemories/snd/mp3/mnd_longing.ogg"
    $ amb01_l = "gesmemories/snd/mp3/amb01_l.ogg"
    $ inwest = "gesmemories/snd/mp3/inwest.ogg"
    $ sophie = "gesmemories/snd/mp3/sophie.ogg"
    $ anna_talk = "gesmemories/snd/mp3/anna_talk.ogg"
    $ aphex = "gesmemories/snd/mp3/aphex.ogg"
    $ arcano = "gesmemories/snd/mp3/arcano.ogg"
    $ deadisland = "gesmemories/snd/mp3/deadisland.ogg"
    $ diefor = "gesmemories/snd/mp3/diefor.ogg"
    $ firstforthefirst = "gesmemories/snd/mp3/firstforthefirst.ogg"
    $ gesgoodbye = "gesmemories/snd/mp3/gesgoodbye.ogg"
    $ intig_cut = "gesmemories/snd/mp3/intig_cut.ogg"
    $ letmefall = "gesmemories/snd/mp3/letmefall.ogg"
    $ liyadance = "gesmemories/snd/mp3/liyadance.ogg"
    $ minin = "gesmemories/snd/mp3/minin.ogg"
    $ mus4 = "gesmemories/snd/mp3/mus4.ogg"
    $ oblivionamb1 = "gesmemories/snd/mp3/oblivionamb1.ogg"
    $ oblivionamb2 = "gesmemories/snd/mp3/oblivionamb2.ogg"
    $ oftherside = "gesmemories/snd/mp3/oftherside.ogg"
    $ outofit0 = "gesmemories/snd/mp3/outofit0.ogg"
    $ psyhosis = "gesmemories/snd/mp3/psyhosis.ogg"
    $ sexuallobster = "gesmemories/snd/mp3/sexuallobster.ogg"
    $ tentheme = "gesmemories/snd/mp3/tentheme.ogg"
    $ train_station = "gesmemories/snd/mp3/train_station.ogg"
    $ deadislandtheme = "gesmemories/snd/mp3/deadislandtheme.ogg"
    $ hatelife = "gesmemories/snd/mp3/hatelife.ogg"
    $ trolwow = "gesmemories/snd/mp3/trolwow.ogg"
    $ dead_more = "gesmemories/snd/mp3/deadmore.ogg"
    $ sneak_peek = "gesmemories/snd/mp3/sneakpeek.ogg"
    $ notefind = "gesmemories/snd/mp3/notefind.ogg"
    $ oblivionamb3 = "gesmemories/snd/mp3/oblivionamb3.ogg"
    $ oblivionamb4 = "gesmemories/snd/mp3/oblivionamb4.ogg"
    $ mndchaplogo = "gesmemories/snd/mp3/mndchaplogo.ogg"
    $ mndcrow = "gesmemories/snd/mp3/mndcrow.ogg"
    $ goodamb1 = "gesmemories/snd/mp3/goodamb1.ogg"
    $ mndsad1 = "gesmemories/snd/mp3/mndsad1.ogg"
    $ goodamb2 = "gesmemories/snd/mp3/goodamb2.ogg"
    $ likeastranger = "gesmemories/snd/mp3/likeastranger.ogg"
    $ mndfuck = "gesmemories/snd/mp3/mndfuck.ogg"
    $ mndnervsr = "gesmemories/snd/mp3/mndnervsr.ogg"
    $ mndbrtp = "gesmemories/snd/mp3/mndbrtp.ogg"
    $ wasbounce = "gesmemories/snd/mp3/wasbounce.ogg"
    $ mndtencar = "gesmemories/snd/mp3/mndtencar.ogg"
    $ mndoldchap = "gesmemories/snd/mp3/mndoldchap.ogg"
    $ mndmaincraftamd1 = "gesmemories/snd/mp3/mndmaincraftamd1.ogg"
    $ mndreveilcut = "gesmemories/snd/mp3/mndreveilcut.ogg"
    $ mndtentheme = "gesmemories/snd/mp3/MND_Ten_Theme.ogg"
    $ mnddo1 = "gesmemories/snd/mp3/mnddo1.ogg"
    $ mnddo2 = "gesmemories/snd/mp3/mnddo2.ogg"
    $ mndreveilcut = "gesmemories/snd/mp3/mndreveilcut.ogg"
    $ mndtentheme = "gesmemories/snd/mp3/MND_Ten_Theme.ogg"
    $ mnddo1 = "gesmemories/snd/mp3/mnddo1.ogg"
    $ mnddo2 = "gesmemories/snd/mp3/mnddo2.ogg"
    $ mnddo3 = "gesmemories/snd/mp3/mnddo3.ogg"
    $ mnddo4 = "gesmemories/snd/mp3/mnddo4.ogg"
    $ mnddo5 = "gesmemories/snd/mp3/mnddo5.ogg"
    $ mndkidfight = "gesmemories/snd/mp3/mndkidfight.ogg"
    $ mndnomore = "gesmemories/snd/mp3/mndnomore.ogg"
    $ mndlabmusic = "gesmemories/snd/mp3/mndlabmusic.ogg"
    $ mndcda = "gesmemories/snd/mp3/mndcda.ogg"
    $ mndreveilfull = "gesmemories/snd/mp3/mndreveilfull.ogg"
    $ mndtenfinaltit = "gesmemories/snd/mp3/mndtenfinaltit.ogg"
    $ jojoawaken = "gesmemories/snd/mp3/jojoawaken.ogg"
    $ mndarahnatheme = "gesmemories/snd/mp3/mndarahnatheme.ogg"
    $ mndbcl = "gesmemories/snd/mp3/mndbcl.ogg"
    $ mndhklfa = "gesmemories/snd/mp3/mndhklfa.ogg"
    $ mndfight2 = "gesmemories/snd/mp3/mndfight2.ogg"
    $ mnd8room1 = "gesmemories/snd/mp3/mnd8room1.ogg"
    $ mndsguv = "gesmemories/snd/mp3/mndsguv.ogg"
    $ mndmorning = "gesmemories/snd/mp3/mndmorning.ogg"
    $ mndsmertsong = "gesmemories/snd/mp3/mndsmertsong.ogg"
    $ mndsnzu = "gesmemories/snd/mp3/mndsnzu.ogg"
    $ mndarb = "gesmemories/snd/mp3/mndarb.ogg"
    $ mnd8room2 = "gesmemories/snd/mp3/mnd8room2.ogg"
    $ mndgluhnorm = "gesmemories/snd/mp3/mndgluhnorm.ogg"
    $ mndhimdio = "gesmemories/snd/mp3/mndhimdio.ogg"
    $ mndhimeratheme = "gesmemories/snd/mp3/mndhimeratheme.ogg"
    $ mndintotherain = "gesmemories/snd/mp3/mndintotherain.ogg"
    $ mndmemodead = "gesmemories/snd/mp3/mndmemodead.ogg"
    $ mndbledvszmey = "gesmemories/snd/mp3/mndbledvszmey.ogg"
    $ mndelvinforest = "gesmemories/snd/mp3/mndelvinforest.ogg"
    $ mndgraveyard = "gesmemories/snd/mp3/mndgraveyard.ogg"
    $ mndhandandeyes = "gesmemories/snd/mp3/mndhandandeyes.ogg"
    $ mndparachute = "gesmemories/snd/mp3/mndparachute.ogg"
    $ mndcrossingtrack = "gesmemories/snd/mp3/mndcrossingtrack.ogg"
    $ mnddanger111 = "gesmemories/snd/mp3/mnddanger111.ogg"
    $ mndfmt = "gesmemories/snd/mp3/mndfmt.ogg"
    $ mndhallucination = "gesmemories/snd/mp3/mndhallucination.ogg"
    $ mndhelvete = "gesmemories/snd/mp3/mndhelvete.ogg"
    $ mndnmrih1 = "gesmemories/snd/mp3/mndnmrih1.ogg"
    $ mndtogiveup = "gesmemories/snd/mp3/mndtogiveup.ogg"
    $ mnd_grace_behind_the_curtain = "gesmemories/snd/mp3/mnd_grace_behind_the_curtain.ogg"
    $ mnd_psy_lift_numbers_start = "gesmemories/snd/mp3/mnd_psy_lift_numbers_start.ogg"
    $ mnd_psy_lift_numbers_porcessed = "gesmemories/snd/mp3/mnd_psy_lift_numbers_porcessed.ogg"
    $ mnd_enertity = "gesmemories/snd/mp3/mnd_enertity.ogg"
    $ mnd_intig_hvatit = "gesmemories/snd/mp3/mnd_intig_hvatit.ogg"
    $ mnd_college = "gesmemories/snd/mp3/mnd_college.ogg"
    $ mnd_death_theme = "gesmemories/snd/mp3/mnd_death_theme.ogg"
    $ mnd_survive_hotel_terror = "gesmemories/snd/mp3/mnd_survive_hotel_terror.ogg"
    $ mnd_faster = "gesmemories/snd/mp3/mnd_faster.ogg"
    $ mnd_slowerfight = "gesmemories/snd/mp3/mnd_slowerfight.ogg"
    $ mnd_introreal = "gesmemories/snd/mp3/mnd_introreal.ogg"
    $ mnd_nmrinh7 = "gesmemories/snd/mp3/mnd_nmrinh7.ogg"
    $ mnd_ges_tears = "gesmemories/snd/mp3/mnd_ges_tears.ogg"
    $ mnd_nmrih1 = "gesmemories/snd/mp3/mnd_nmrih1.ogg"
    $ mnd_sled_cut = "gesmemories/snd/mp3/mnd_sled_cut.ogg"
    $ mnd_gluhar_z_mix = "gesmemories/snd/mp3/mnd_gluhar_z_mix.ogg"
    $ mnd_gluhar_z = "gesmemories/snd/mp3/mnd_gluhar_z.ogg"
    $ mnd_karpov_1 = "gesmemories/snd/mp3/mnd_karpov_1.ogg"
    $ mnd_kapdon = "gesmemories/snd/mp3/mnd_kapdon.ogg"
    $ outofit1 = "gesmemories/snd/mp3/outofit1.ogg"
    $ mnd_gluhar_utro = "gesmemories/snd/mp3/mnd_gluhar_utro.ogg"
    $ mnd_arahna_theme_2 = "gesmemories/snd/mp3/mnd_arahna_theme_2.ogg"
    $ mnd_memories_1 = "gesmemories/snd/mp3/mnd_memories_1.ogg"
    $ mnd_tarakan_joke_1 = "gesmemories/snd/mp3/mnd_tarakan_joke_1.ogg"
    $ mnd_rain_stand_a_window = "gesmemories/snd/mp3/mnd_rain_stand_a_window.ogg"
    $ mnd_cityend = "gesmemories/snd/mp3/mnd_cityend.ogg"
    $ mnd_chap_logo_new = "gesmemories/snd/mp3/mnd_chap_logo_new.ogg"
    $ mnd_hurt_cut = "gesmemories/snd/mp3/mnd_hurt_cut.ogg"
    $ mnd_new_menu_music = "gesmemories/snd/mp3/mnd_new_menu_music.ogg"
    $ mnd_aom = "gesmemories/snd/mp3/mnd_aom.ogg"
    $ mnd_riptide_1 = "gesmemories/snd/mp3/mnd_riptide_1.ogg"
    $ mnd_asia = "gesmemories/snd/mp3/mnd_asia.ogg"
    $ mnd_karpov_2_ff = "gesmemories/snd/mp3/mnd_karpov_2_ff.ogg"
    $ mnd_arahna_full = "gesmemories/snd/mp3/mnd_arahna_full.ogg"
    $ mnd_hurt = "gesmemories/snd/mp3/mnd_hurt.ogg"
    $ mnd_mind_the_garp = "gesmemories/snd/mp3/mnd_mind_the_garp.ogg"
    $ mnd_khait_theme = "gesmemories/snd/mp3/mnd_khait_theme.ogg"
    $ mnd_ronberg_goodbye = "gesmemories/snd/mp3/mnd_ronberg_goodbye.ogg"
    $ mnd_luci_theme = "gesmemories/snd/mp3/mnd_luci_theme.ogg"
    $ mnd_hb_mus_1 = "gesmemories/snd/mp3/mnd_hb_mus_1.ogg"
    $ mnd_credits = "gesmemories/snd/mp3/mnd_credits.ogg"
    $ mnd_just_like_sleep = "gesmemories/snd/mp3/mnd_just_like_sleep.ogg"
    $ mnd_just_like_sleep_short = "gesmemories/snd/mp3/mnd_just_like_sleep_short.ogg"
    $ mnd_recollection = "gesmemories/snd/mp3/mnd_recollection.ogg"
    $ mnd_13_hi_cab_music = "gesmemories/snd/mp3/mnd_13_hi_cab_music.ogg"
    $ mnd_final_credit_theme = "gesmemories/snd/mp3/mnd_final_credit_theme.ogg"
    $ mnd_finale_credits = "gesmemories/snd/mp3/mnd_finale_credits.ogg"
    $ mnd_tv_dance_music = "gesmemories/snd/mp3/mnd_tv_dance_music.ogg"
    $ mnd_u_z_best = "gesmemories/snd/mp3/mnd_u_z_best.ogg"
    $ mnd_finale_credits_cut = "gesmemories/snd/mp3/mnd_finale_credits_cut.ogg"
    $ mnd_a3_menu = "gesmemories/snd/mp3/mnd_a3_menu.ogg"
    $ mnd_fallen = "gesmemories/snd/mp3/mnd_fallen.ogg"
    $ mnd_i_got_5_on_it = "gesmemories/snd/mp3/mnd_i_got_5_on_it.ogg"
    $ mnd_times_inst = "gesmemories/snd/mp3/mnd_times_inst.ogg"
    $ mnd_final_theme = "gesmemories/snd/mp3/mnd_final_theme.ogg"
    $ mnd_amb_mix_1 = "gesmemories/snd/mp3/mnd_amb_mix_1.ogg"
    $ mnd_kad = "gesmemories/snd/mp3/mnd_kad.ogg"
    $ mnd_harts_theme_17_1 = "gesmemories/snd/mp3/mnd_harts_theme_17_1.ogg"
    $ mnd_myimmortal = "gesmemories/snd/mp3/mnd_myimmortal.ogg"
    $ mnd_c17h27no2 = "gesmemories/snd/mp3/mnd_c17h27no2.ogg"
    $ mnd_aft_long_day = "gesmemories/snd/mp3/mnd_aft_long_day.ogg"
    $ mnd_sexygitl = "gesmemories/snd/mp3/mnd_sexygitl.ogg"
    $ mnd_luciena_theme_2 = "gesmemories/snd/mp3/mnd_luciena_theme_2.ogg"
    $ mnd_rainagain = "gesmemories/snd/mp3/mnd_rainagain.ogg"
    $ mnd_brandon_gp = "gesmemories/snd/mp3/mnd_brandon_gp.ogg"
    $ mnd_monage_daydream = "gesmemories/snd/mp3/mnd_monage_daydream.ogg"
    $ mnd_u_will_not_survive = "gesmemories/snd/mp3/mnd_u_will_not_survive.ogg"
    $ mnd_scrxlrd = "gesmemories/snd/mp3/mnd_scrxlrd.ogg"
    $ mnd_luciena_kiss = "gesmemories/snd/mp3/mnd_luciena_kiss.ogg"
    $ mnd_ningyou = "gesmemories/snd/mp3/mnd_ningyou.ogg"
    $ mnd_tape_1 = "gesmemories/snd/mp3/mnd_tape_1.ogg"
    $ mnd_tape_3 = "gesmemories/snd/mp3/mnd_tape_3.ogg"
    $ mnd_tape_7 = "gesmemories/snd/mp3/mnd_tape_7.ogg"
    $ mnd_nebesa = "gesmemories/snd/mp3/mnd_nebesa.ogg"
    $ mnd_final_close_title = "gesmemories/snd/mp3/mnd_final_close_title.ogg"
    $ mnd_all_its_over = "gesmemories/snd/mp3/mnd_all_its_over.ogg"
    $ mnd_disheartened = "gesmemories/snd/mp3/mnd_disheartened.ogg"
    $ mnd_forest_end = "gesmemories/snd/mp3/mnd_forest_end.ogg"
    $ mnd_arahna_theme = "gesmemories/snd/mp3/mnd_arahna_theme.ogg"
    $ mnd_polar_day = "gesmemories/snd/mp3/mnd_polar_day.ogg"
    $ mnd_anxiety = "gesmemories/snd/mp3/mnd_anxiety.ogg"
    $ mnd_mms_final = "gesmemories/snd/mp3/mnd_mms_final.ogg"
    $ mnd_aft_end_scene_music = "gesmemories/snd/mp3/mnd_aft_end_scene_music.ogg"
    $ mnd_smert_song = "gesmemories/snd/mp3/mnd_smert_song.ogg"


    $ rainstandwindow = "gesmemories/snd/ambient/rainstandwindow.ogg"
    $ mndrainstr = "gesmemories/snd/ambient/mndrainstr.ogg"
    $ rainingarage = "gesmemories/snd/ambient/rainingarage.ogg"
    $ mndsea = "gesmemories/snd/ambient/mndsea.ogg"
    $ mndambosen = "gesmemories/snd/ambient/mndambosen.ogg"
    $ mndambbirdsd = "gesmemories/snd/ambient/mndambbirdsd.ogg"
    $ mndambdayforest = "gesmemories/snd/ambient/mndambdayforest.ogg"
    $ mndfireamb = "gesmemories/snd/ambient/mndfireamb.ogg"
    $ mndhavyrainforest = "gesmemories/snd/ambient/mndhavyrainforest.ogg"
    $ mndriveramb = "gesmemories/snd/ambient/mndriveramb.ogg"
    $ mndwolfs1 = "gesmemories/snd/ambient/mndwolfs1.ogg"
    $ mndforestn = "gesmemories/snd/ambient/mndforestn.ogg"
    $ mndvih1 = "gesmemories/snd/ambient/mndvih1.ogg"
    $ mndvih2 = "gesmemories/snd/ambient/mndvih2.ogg"
    $ mndforestmamb = "gesmemories/snd/ambient/mndforestmamb.ogg"
    $ mndwolfsplays = "gesmemories/snd/ambient/mndwolfsplays.ogg"
    $ mndwolfangramb = "gesmemories/snd/ambient/mndwolfangramb.ogg"
    $ mndfightwolf = "gesmemories/snd/ambient/mndfightwolf.ogg"
    $ mndfloortash = "gesmemories/snd/ambient/mndfloortash.ogg"
    $ mndeatmeetten = "gesmemories/snd/ambient/mndeatmeetten.ogg"
    $ mnd_coridors_ambience_1 = "gesmemories/snd/ambient/mnd_coridors_ambience_1.ogg"
    $ mnd_coridors_ambience_2 = "gesmemories/snd/ambient/mnd_coridors_ambience_2.ogg"
    $ mnd_coridors_ambience_3 = "gesmemories/snd/ambient/mnd_coridors_ambience_3.ogg"
    $ mnd_coridors_ambience_4 = "gesmemories/snd/ambient/mnd_coridors_ambience_4.ogg"
    $ mnd_floor_amb = "gesmemories/snd/ambient/mnd_floor_amb.ogg"
    $ mnd_liya_good_wispers = "gesmemories/snd/ambient/mnd_liya_good_wispers.ogg"
    $ mnd_rain_voice_amb = "gesmemories/snd/ambient/mnd_rain_voice_amb.ogg"


    $ mndroll = "gesmemories/snd/sfx/mndroll.ogg"
    $ mndgrom = "gesmemories/snd/sfx/mndgrom.ogg"
    $ mndhallo = "gesmemories/snd/sfx/mndhallo.ogg"
    $ opdoor1 = "gesmemories/snd/sfx/opdoor1.ogg"
    $ paper = "gesmemories/snd/sfx/paper.ogg"
    $ mndbed = "gesmemories/snd/sfx/mndbed.ogg"
    $ w810 = "gesmemories/snd/sfx/w810.ogg"
    $ phbutton = "gesmemories/snd/sfx/phbutton.ogg"
    $ cldoor1 = "gesmemories/snd/sfx/cldoor1.ogg"
    $ latch1 = "gesmemories/snd/sfx/latch1.ogg"
    $ btn1 = "gesmemories/snd/sfx/btn1.ogg"
    $ mndliftmove = "gesmemories/snd/sfx/mndliftmove.ogg"
    $ hrddoor1 = "gesmemories/snd/sfx/hrddoor1.ogg"
    $ woodstep = "gesmemories/snd/sfx/woodstep.ogg"
    $ phgudok = "gesmemories/snd/sfx/phgudok.ogg"
    $ mnddoorcol = "gesmemories/snd/sfx/mnddoorcol.ogg"
    $ mndwatsteps = "gesmemories/snd/sfx/mndwatsteps.ogg"
    $ attempt = "gesmemories/snd/sfx/attempt.ogg"
    $ mndhlop = "gesmemories/snd/sfx/mndhlop.ogg"
    $ carride = "gesmemories/snd/sfx/carride.ogg"
    $ cartorm = "gesmemories/snd/sfx/cartorm.ogg"
    $ sloweff = "gesmemories/snd/sfx/sloweff.ogg"
    $ raise_1 = "gesmemories/snd/sfx/raise_1.ogg"
    $ foll = "gesmemories/snd/sfx/foll.ogg"
    $ injekt = "gesmemories/snd/sfx/injekt.ogg"
    $ flashback = "gesmemories/snd/sfx/flashback.ogg"
    $ screbdoor = "gesmemories/snd/sfx/screbdoor.ogg"
    $ doorknok = "gesmemories/snd/sfx/doorknok.ogg"
    $ eating = "gesmemories/snd/sfx/eating.ogg"
    $ watherin = "gesmemories/snd/sfx/watherin.ogg"
    $ alkodrink = "gesmemories/snd/sfx/alkodrink.ogg"
    $ hrustbone = "gesmemories/snd/sfx/hrustbone.ogg"
    $ step_wather = "gesmemories/snd/sfx/step_wather.ogg"
    $ psystart = "gesmemories/snd/sfx/psystart.ogg"
    $ psyvoices = "gesmemories/snd/sfx/psyvoices.ogg"
    $ glass_break = "gesmemories/snd/sfx/glass_break.ogg"
    $ crashglass = "gesmemories/snd/sfx/crashglass.ogg"
    $ olddoor = "gesmemories/snd/sfx/olddoor.ogg"
    $ door1 = "gesmemories/snd/sfx/door1.ogg"
    $ narko_dream = "gesmemories/snd/sfx/narko_dream.ogg"
    $ wailchaircrash = "gesmemories/snd/sfx/wailchaircrash.ogg"
    $ dam1 = "gesmemories/snd/sfx/dam1.ogg"
    $ knifehard = "gesmemories/snd/sfx/knifehard.ogg"
    $ woodskr = "gesmemories/snd/sfx/woodskr.ogg"
    $ mndpaper = "gesmemories/snd/sfx/mndpaper.ogg"
    $ olddoor1 = "gesmemories/snd/sfx/olddoor.ogg"
    $ metalstack = "gesmemories/snd/sfx/metalstack.ogg"
    $ doorrageop = "gesmemories/snd/sfx/doorrageop.ogg"
    $ gurgle_loop1 = "gesmemories/snd/sfx/gurgle_loop1.ogg"
    $ smallmedkit1 = "gesmemories/snd/sfx/smallmedkit1.ogg"
    $ mndhorscr1 = "gesmemories/snd/sfx/mndhorscr1.ogg"
    $ mndboom1 = "gesmemories/snd/sfx/mndboom1.ogg"
    $ mndfirescream  = "gesmemories/snd/sfx/mndfirescream .ogg"
    $ mndhitw1 = "gesmemories/snd/sfx/mndhitw1.ogg"
    $ mndheavygrom = "gesmemories/snd/sfx/mndheavygrom.ogg"
    $ mndwolfvoy = "gesmemories/snd/sfx/mndwolfvoy.ogg"
    $ mndwolfangr = "gesmemories/snd/sfx/mndwolfangr.ogg"
    $ mndhitw1 = "gesmemories/snd/sfx/mndhitw1.ogg"
    $ mndheavygrom = "gesmemories/snd/sfx/mndheavygrom.ogg"
    $ mndwolfvoy = "gesmemories/snd/sfx/mndwolfvoy.ogg"
    $ mndwolfangr = "gesmemories/snd/sfx/mndwolfangr.ogg"
    $ mndcrowvoise1 = "gesmemories/snd/sfx/mndcrowvoise1.ogg"
    $ mndwolfhurt = "gesmemories/snd/sfx/mndwolfhurt.ogg"
    $ mndlitlewolfs = "gesmemories/snd/sfx/mndlitlewolfs.ogg"
    $ mndwolfhit = "gesmemories/snd/sfx/mndwolfhit.ogg"
    $ mndtenobr = "gesmemories/snd/sfx/mndtenobr.ogg"
    $ mndtenroar = "gesmemories/snd/sfx/mndtenroar.ogg"
    $ mndphoto = "gesmemories/snd/sfx/mndphoto.ogg"
    $ mnddeathscream = "gesmemories/snd/sfx/mnddeathscream.ogg"
    $ mndsplash = "gesmemories/snd/sfx/mndsplash.ogg"
    $ mnddcls2 = "gesmemories/snd/sfx/mnddcls2.ogg"
    $ mnddoorop2 = "gesmemories/snd/sfx/mnddoorop2.ogg"
    $ mndhitcof = "gesmemories/snd/sfx/mndhitcof.ogg"
    $ mndlutch = "gesmemories/snd/sfx/mndlutch.ogg"
    $ mndmetalclose = "gesmemories/snd/sfx/mndmetalclose.ogg"
    $ mndmetalclose1 = "gesmemories/snd/sfx/mndmetalclose1.ogg"
    $ mndpunch = "gesmemories/snd/sfx/mndpunch.ogg"
    $ mndbuttonclickrelease = "gesmemories/snd/sfx/mndbuttonclickrelease.ogg"
    $ mndknife_slash1 = "gesmemories/snd/sfx/mndknife_slash1.ogg"
    $ mndknife_slash3 = "gesmemories/snd/sfx/mndknife_slash3.ogg"
    $ mndknife_stab3 = "gesmemories/snd/sfx/mndknife_stab3.ogg"
    $ mndpiano = "gesmemories/snd/sfx/mndpiano.ogg"
    $ sub_kettei2 = "gesmemories/snd/sfx/sub_kettei2.ogg"
    $ mnd_4_button_clik = "gesmemories/snd/sfx/mnd_4_button_clik.ogg"
    $ mnd_5_button_clik = "gesmemories/snd/sfx/mnd_5_button_clik.ogg"
    $ mnd_metal_breack_start = "gesmemories/snd/sfx/mnd_metal_breack_start.ogg"
    $ mdn_lift_psy_stop_hard = "gesmemories/snd/sfx/mdn_lift_psy_stop_hard.ogg"
    $ mnd_electro_1 = "gesmemories/snd/sfx/mnd_electro_1.ogg"
    $ mdn_lift_psy_stop = "gesmemories/snd/sfx/mdn_lift_psy_stop.ogg"
    $ mnd_metal_plank_greak_1 = "gesmemories/snd/sfx/mnd_metal_plank_greak_1.ogg"
    $ mnd_tv_noise = "gesmemories/snd/sfx/mnd_tv_noise.ogg"
    $ mnd_car_ride_closer = "gesmemories/snd/sfx/mnd_car_ride_closer.ogg"
    $ mnd_piano_lie_2 = "gesmemories/snd/sfx/mnd_piano_lie_2.ogg"
    $ mnd_piano_lie_1 = "gesmemories/snd/sfx/mnd_piano_lie_1.ogg"
    $ mnd_lift_doors_open = "gesmemories/snd/sfx/mnd_lift_doors_open.ogg"
    $ mnd_drip = "gesmemories/snd/sfx/mnd_drip.ogg"
    $ mnd_lift_fall_down = "gesmemories/snd/sfx/mnd_lift_fall_down.ogg"
    $ mnd_apartmentholecrash1 = "gesmemories/snd/sfx/mnd_apartmentholecrash1.ogg"
    $ mnd_big_wood_droor_scr = "gesmemories/snd/sfx/mnd_big_wood_droor_scr.ogg"
    $ mnd_latchlocked1 = "gesmemories/snd/sfx/mnd_latchlocked1.ogg"
    $ mnd_axe_hit = "gesmemories/snd/sfx/mnd_axe_hit.ogg"
    $ mnd_axe_hit_2 = "gesmemories/snd/sfx/mnd_axe_hit_2.ogg"
    $ mnd_zippo_open = "gesmemories/snd/sfx/mnd_zippo_open.ogg"
    $ mnd_zippo_strike = "gesmemories/snd/sfx/mnd_zippo_strike.ogg"
    $ mnd_zippo_flame = "gesmemories/snd/sfx/mnd_zippo_flame.ogg"
    $ mnd_smoke_g = "gesmemories/snd/sfx/mnd_smoke_g.ogg"
    $ mnd_zippo_close = "gesmemories/snd/sfx/mnd_zippo_close.ogg"
    $ mnd_zombie_head_explode_03 = "gesmemories/snd/sfx/mnd_zombie_head_explode_03.ogg"
    $ mnd_faster_alert1 = "gesmemories/snd/sfx/mnd_faster_alert1.ogg"
    $ mnd_faster_death = "gesmemories/snd/sfx/mnd_faster_death.ogg"
    $ mnd_faster_pain = "gesmemories/snd/sfx/mnd_faster_pain.ogg"
    $ mnd_kabluki_slow = "gesmemories/snd/sfx/mnd_kabluki_slow.ogg"
    $ mnd_jason = "gesmemories/snd/sfx/mnd_jason.ogg"
    $ mnd_steps = "gesmemories/snd/sfx/mnd_steps.ogg"
    $ mnd_metallicrustle = "gesmemories/snd/sfx/mnd_metallicrustle.ogg"
    $ mnd_padl_turn = "gesmemories/snd/sfx/mnd_padl_turn.ogg"
    $ mnd_padl_unlock = "gesmemories/snd/sfx/mnd_padl_unlock.ogg"
    $ mnd_doormove1 = "gesmemories/snd/sfx/mnd_doormove1.ogg"
    $ mnd_gay_do_break = "gesmemories/snd/sfx/mnd_gay_do_break.ogg"
    $ mnd_valve = "gesmemories/snd/sfx/mnd_valve.ogg"
    $ mnd_asy_startle = "gesmemories/snd/sfx/mnd_asy_startle.ogg"
    $ mnd_kranwather = "gesmemories/snd/sfx/mnd_kranwather.ogg"
    $ mnd_water_outside = "gesmemories/snd/sfx/mnd_water_outside.ogg"
    $ mnd_blev_started = "gesmemories/snd/sfx/mnd_blev_started.ogg"
    $ mnd_asy_door_close2 = "gesmemories/snd/sfx/mnd_asy_door_close2.ogg"
    $ mnd_asy_door_open3 = "gesmemories/snd/sfx/mnd_asy_door_open3.ogg"
    $ mnd_lever5 = "gesmemories/snd/sfx/mnd_lever5.ogg"
    $ mnd_lever1 = "gesmemories/snd/sfx/mnd_lever1.ogg"
    $ mnd_ropeplace = "gesmemories/snd/sfx/mnd_ropeplace.ogg"
    $ mnd_boiler_start = "gesmemories/snd/sfx/mnd_boiler_start.ogg"
    $ mnd_hitmiss_1 = "gesmemories/snd/sfx/mnd_hitmiss_1.ogg"
    $ mnd_hitmiss_2 = "gesmemories/snd/sfx/mnd_hitmiss_2.ogg"
    $ mnd_ten_gitara_sound = "gesmemories/snd/sfx/mnd_ten_gitara_sound.ogg"
    $ mnd_door_signal = "gesmemories/snd/sfx/mnd_door_signal.ogg"
    $ mnd_glass_bottle = "gesmemories/snd/sfx/mnd_glass_bottle.ogg"
    $ mnd_chap_logo_new2 = "gesmemories/snd/sfx/mnd_chap_logo_new2.ogg"
    $ mnd_door_col = "gesmemories/snd/sfx/mnd_door_col.ogg"
    $ mnd_tv_termin_snd = "gesmemories/snd/sfx/mnd_tv_termin_snd.ogg"
    $ mnd_a4_chaplog = "gesmemories/snd/sfx/mnd_a4_chaplog.ogg"
    $ mnd_r_creak = "gesmemories/snd/sfx/mnd_r_creak.ogg"
    $ mnd_r_creak2 = "gesmemories/snd/sfx/mnd_r_creak2.ogg"
    $ mnd_r_vine = "gesmemories/snd/sfx/mnd_r_vine.ogg"
    $ mnd_first_act_logos = "gesmemories/snd/sfx/mnd_first_act_logos.ogg"



    $ liyav1 = "gesmemories/snd/vocal/liya/liyav1.ogg"
    $ mndlml = "gesmemories/snd/vocal/liya/mndlml.ogg"
    $ bloodkashl = "gesmemories/snd/vocal/vas/bloodkashl.ogg"
    $ hardbreath = "gesmemories/snd/vocal/vas/hardbreath.ogg"
    $ hightpain1 = "gesmemories/snd/vocal/vas/hightpain1.ogg"
    $ hightpain2 = "gesmemories/snd/vocal/vas/hightpain2.ogg"
    $ pained = "gesmemories/snd/vocal/vas/pained.ogg"
    $ vascry = "gesmemories/snd/vocal/vas/vascry.ogg"
    $ vaspain1 = "gesmemories/snd/vocal/vas/vaspain1.ogg"
    $ vaspain2 = "gesmemories/snd/vocal/vas/vaspain2.ogg"
    $ mndkashl = "gesmemories/snd/vocal/vas/mndkashl.ogg"
    $ wsl = "gesmemories/snd/vocal/womvoise/wsl.ogg"
    $ mndvzdoh = "gesmemories/snd/vocal/vas/mndvzdoh.ogg"
    $ vasshortpl = "gesmemories/snd/vocal/vas/vasshortpl.ogg"
    $ vasist = "gesmemories/snd/vocal/vas/vasist.ogg"
    $ mndvpl = "gesmemories/snd/vocal/vas/mndvpl.ogg"
    $ mndpanic1 = "gesmemories/snd/vocal/vas/mndpanic1.ogg"
    $ mndpanic2 = "gesmemories/snd/vocal/vas/mndpanic2.ogg"
    $ mndcombo = "gesmemories/snd/vocal/vas/mndcombo.ogg"
    $ whl = "gesmemories/snd/vocal/womvoise/whl.ogg"
    $ mndvnl = "gesmemories/snd/vocal/vas/mndvnl.ogg"
    $ mnddrink = "gesmemories/snd/vocal/vas/mnddrink.ogg"
    $ mndblev = "gesmemories/snd/vocal/vas/mndblev.ogg"
    $ mndkidboyscr = "gesmemories/snd/vocal/man/mndkidboyscr.ogg"
    $ mndwakeup = "gesmemories/snd/vocal/vas/mndwakeup.ogg"
    $ mndkidboyscr = "gesmemories/snd/vocal/man/mndkidboyscr.ogg"
    $ mndwakeup = "gesmemories/snd/vocal/vas/mndwakeup.ogg"
    $ mndch4logo = "gesmemories/snd/vocal/vas/mndch4logo.ogg"
    $ mndarlau = "gesmemories/snd/vocal/womvoise/mndarlau.ogg"
    $ mndvaspsyl = "gesmemories/snd/vocal/vas/mndvaspsyl.ogg"
    $ mnd_panic_breath = "gesmemories/snd/vocal/vas/mnd_panic_breath.ogg"
    $ mnd_vas_kalustro_breath = "gesmemories/snd/vocal/vas/mnd_vas_kalustro_breath.ogg"
    $ vaspain3 = "gesmemories/snd/vocal/vas/vaspain3.ogg"
    $ mnd_vas_afther_wather = "gesmemories/snd/vocal/vas/mnd_vas_afther_wather.ogg"
    $ mnd_vas_fast_breath = "gesmemories/snd/vocal/vas/mnd_vas_fast_breath.ogg"
    $ mnd_vas_usilie = "gesmemories/snd/vocal/vas/mnd_vas_usilie.ogg"
    $ mnd_vas_dead = "gesmemories/snd/vocal/vas/mnd_vas_dead.ogg"
    $ mnd_heart_bit = "gesmemories/snd/vocal/vas/mnd_heart_bit.ogg"
    $ mnd_out_of_my_head = "gesmemories/snd/vocal/vas/mnd_out_of_my_head.ogg"
    $ mnd_get_down = "gesmemories/snd/vocal/vas/mnd_get_down.ogg"
    $ mnd_get_up_14 = "gesmemories/snd/vocal/vas/mnd_get_up_14.ogg"
    $ mnd_swing_1 = "gesmemories/snd/vocal/vas/mnd_swing_1.ogg"
    $ mnd_swing_2 = "gesmemories/snd/vocal/vas/mnd_swing_2.ogg"


    $ mnd_psyvas_dyshish = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_dyshish.ogg"
    $ mnd_psyvas_est_kto = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_est_kto.ogg"
    $ mnd_psyvas_idu_na_strah = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_idu_na_strah.ogg"
    $ mnd_psyvas_istochaesh_strah = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_istochaesh_strah.ogg"
    $ mnd_psyvas_strashno = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_strashno.ogg"
    $ mnd_psyvas_tesno = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_tesno.ogg"
    $ mnd_psyvas_ti_mena_slishish = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_ti_mena_slishish.ogg"
    $ mnd_psyvas_ti_mena_vidish = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_ti_mena_vidish.ogg"
    $ mnd_psyvas_ti_zdes = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_ti_zdes.ogg"
    $ mnd_psyvas_ya_znau_gde_ti = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_ya_znau_gde_ti.ogg"
    $ mnd_psyvas_zubi = "gesmemories/snd/vocal/vas/pshychotalk/mnd_psyvas_zubi.ogg"
    $ mnd_zachem_ubegaesh = "gesmemories/snd/vocal/vas/pshychotalk/mnd_zachem_ubegaesh.ogg"



    $ mnd_voice_in_head_1 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_1.ogg"
    $ mnd_voice_in_head_2 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_2.ogg"
    $ mnd_voice_in_head_3 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_3.ogg"
    $ mnd_voice_in_head_4 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_4.ogg"
    $ mnd_voice_in_head_5 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_5.ogg"
    $ mnd_voice_in_head_6 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_6.ogg"
    $ mnd_voice_in_head_7 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_7.ogg"
    $ mnd_voice_in_head_8 = "gesmemories/snd/vocal/headvoice/mnd_voice_in_head_8.ogg"
    $ mnd_try_voice_1 = "gesmemories/snd/vocal/headvoice/mnd_try_voice_1.ogg"
    $ mnd_try_voice_2 = "gesmemories/snd/vocal/headvoice/mnd_try_voice_2.ogg"
    $ mnd_try_voice_3 = "gesmemories/snd/vocal/headvoice/mnd_try_voice_3.ogg"
    $ mnd_try_voice_4 = "gesmemories/snd/vocal/headvoice/mnd_try_voice_4.ogg"
    $ mnd_try_voise_help_1 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_1.ogg"
    $ mnd_try_voise_help_2 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_2.ogg"
    $ mnd_try_voise_help_3 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_3.ogg"
    $ mnd_try_voise_help_4 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_4.ogg"
    $ mnd_try_voise_help_5 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_5.ogg"
    $ mnd_try_voise_help_6 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_6.ogg"
    $ mnd_try_voise_help_7 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_7.ogg"
    $ mnd_try_voise_help_8 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_8.ogg"
    $ mnd_try_voise_help_9 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_9.ogg"
    $ mnd_try_voise_help_10 = "gesmemories/snd/vocal/headvoice/mnd_try_voise_help_10.ogg"



    $ mndpsyeff1 = "gesmemories/snd/psy/mndpsyeff1.ogg"
    $ mndpsyamb1 = "gesmemories/snd/psy/mndpsyamb1.ogg"
    $ mndpsyamb2 = "gesmemories/snd/psy/mndpsyamb2.ogg"
    $ mndcornightvoise = "gesmemories/snd/psy/mndcornightvoise.ogg"
    $ mndwomanpsyl = "gesmemories/snd/psy/mndwomanpsyl.ogg"
    $ mndnejdan = "gesmemories/snd/psy/mndnejdan.ogg"
    $ mndlitlemonster = "gesmemories/snd/psy/mndlitlemonster.ogg"
    $ mndstrangemusic = "gesmemories/snd/psy/mndstrangemusic.ogg"
    $ mndtenkiller1 = "gesmemories/snd/psy/mndtenkiller1.ogg"
    $ mndtekillerl = "gesmemories/snd/psy/mndtekillerl.ogg"
    $ mndtenroar = "gesmemories/snd/psy/mndtenroar.ogg"
    $ mnd_snuff666 = "gesmemories/snd/psy/mnd_snuff666.ogg"
    $ mnd_hit_final_psy = "gesmemories/snd/psy/mnd_hit_final_psy.ogg"
    $ mnd_metal_breack_breack = "gesmemories/snd/psy/mnd_metal_breack_breack.ogg"
    $ mnd_psy_fast_1 = "gesmemories/snd/psy/mnd_psy_fast_1.ogg"
    $ mnd_psy_fast_2 = "gesmemories/snd/psy/mnd_psy_fast_2.ogg"
    $ mnd_psy_fast_3 = "gesmemories/snd/psy/mnd_psy_fast_3.ogg"
    $ mnd_hit_cof = "gesmemories/snd/psy/mnd_hit_cof.ogg"
    $ mnd_hum_song_2 = "gesmemories/snd/psy/mnd_hum_song_2.ogg"
    $ mnd_hum_song_1 = "gesmemories/snd/psy/mnd_hum_song_1.ogg"
    $ mnd_psy_lift_strange_noise_1 = "gesmemories/snd/psy/mnd_psy_lift_strange_noise_1.ogg"
    $ mnd_psy_lift_strange_noise_2 = "gesmemories/snd/psy/mnd_psy_lift_strange_noise_2.ogg"
    $ mnd_psy_lift_strange_noise_3 = "gesmemories/snd/psy/mnd_psy_lift_strange_noise_3.ogg"
    $ mnd_psy_lift_strange_noise_4 = "gesmemories/snd/psy/mnd_psy_lift_strange_noise_4.ogg"
    $ mnd_psy_lift_strange_noise_5 = "gesmemories/snd/psy/mnd_psy_lift_strange_noise_5.ogg"
    $ mnd_lift_body_drop = "gesmemories/snd/psy/mnd_lift_body_drop.ogg"
    $ mnd_psyhosis_vas_amb = "gesmemories/snd/psy/mnd_psyhosis_vas_amb.ogg"
    $ mnd_comone_over_here = "gesmemories/snd/psy/mnd_comone_over_here.ogg"
    $ mnd_psy_lift_strange_noise_6 = "gesmemories/snd/psy/mnd_psy_lift_strange_noise_6.ogg"
    $ mnd_rumpelcutscene = "gesmemories/snd/psy/mnd_rumpelcutscene.ogg"
    $ mnd_church_bell = "gesmemories/snd/psy/mnd_church_bell.ogg"
    $ mnd_church_monks = "gesmemories/snd/psy/mnd_church_monks.ogg"
    $ mnd_moan_2 = "gesmemories/snd/psy/mnd_moan_2.ogg"
    $ mnd_lost_squeak_1 = "gesmemories/snd/psy/mnd_lost_squeak_1.ogg"
    $ mnd_lost_rdm_3 = "gesmemories/snd/psy/mnd_lost_rdm_3.ogg"
    $ mnd_asy_crying = "gesmemories/snd/psy/mnd_asy_crying.ogg"
    $ mnd_lost_blinds = "gesmemories/snd/psy/mnd_lost_blinds.ogg"
    $ mnd_scream_amb_1 = "gesmemories/snd/psy/mnd_scream_amb_1.ogg"
    $ mnd_wood_door_creac_10 = "gesmemories/snd/psy/mnd_wood_door_creac_10.ogg"
    $ mnd_dredka_1 = "gesmemories/snd/psy/mnd_dredka_1.ogg"
    $ mnd_strangle_strangle1 = "gesmemories/snd/psy/mnd_strangle_strangle1.ogg"
    $ mnd_unsafe = "gesmemories/snd/psy/mnd_unsafe.ogg"
    $ mnd_c9_voises_1 = "gesmemories/snd/psy/mnd_c9_voises_1.ogg"
    $ mnd_c9_voises_2 = "gesmemories/snd/psy/mnd_c9_voises_2.ogg"
    $ mnd_horror_hit = "gesmemories/snd/psy/mnd_horror_hit.ogg"
    $ mnd_shove = "gesmemories/snd/psy/mnd_shove.ogg"
    $ mnd_takemetalsmall = "gesmemories/snd/psy/mnd_takemetalsmall.ogg"
    $ mnd_tape_noise = "gesmemories/snd/psy/mnd_tape_noise.ogg"
    $ mnd_tape_load = "gesmemories/snd/psy/mnd_tape_load.ogg"
    $ mnd_tape_pickup = "gesmemories/snd/psy/mnd_tape_pickup.ogg"
    $ mnd_tape_insert = "gesmemories/snd/psy/mnd_tape_insert.ogg"
    $ mnd_tape_off = "gesmemories/snd/psy/mnd_tape_off.ogg"
    $ mnd_girlpsylau = "gesmemories/snd/psy/mnd_girlpsylau.ogg"
    $ mnd_open_center_door = "gesmemories/snd/psy/mnd_open_center_door.ogg"
    $ mnd_memory_murder_1 = "gesmemories/snd/psy/mnd_memory_murder_1.ogg"
    $ mnd_psy_music_13_1 = "gesmemories/snd/psy/mnd_psy_music_13_1.ogg"
    $ mnd_psy_music_13_2 = "gesmemories/snd/psy/mnd_psy_music_13_2.ogg"
    $ mnd_psyhosis_fear_allert_1 = "gesmemories/snd/psy/mnd_psyhosis_fear_allert_1.ogg"
    $ mnd_psyhosis_fear_allert_2 = "gesmemories/snd/psy/mnd_psyhosis_fear_allert_2.ogg"
    


    $ flash_fast = Fade(0.25, 0, 0.75, color="#fff")
    $ flash_fast2 = Fade(0.05, 0, 0.35, color="#fff")
    $ flash_fast_red = Fade(0.25, 0, 0.75, color="#ff0000")
    $ flash_fast_red2 = Fade(0.05, 0, 0.75, color="#ff0000")




    image gesundheit_logos2 = Movie(play="gesmemories/image/logo/mnd_ges_bg.webm", channel="movie", size=(1920, 1080))
    image gesundheit_logos = Movie(play="gesmemories/image/logo/new_logo.webm", channel="movie", size=(1920, 1080))





    image bg doclog = "gesmemories/image/bg/doclog.webp"
    image bg mndggroom = "gesmemories/image/bg/mndggroom.webp"
    image bg mndrainbalk = "gesmemories/image/bg/mndrainbalk.webp"
    image bg skyrain = "gesmemories/image/bg/skyrain.webp"
    image bg busstoprain1 = "gesmemories/image/bg/busstoprain1.webp"
    image bg rainofwindow = "gesmemories/image/bg/rainofwindow.webp"
    image bg mndflowermark = "gesmemories/image/bg/mndflowermark.webp"
    image bg mndrainaspd = "gesmemories/image/bg/mndrainaspd.webp"
    image bg mndparkr = "gesmemories/image/bg/mndparkr.webp"
    image bg 4roomd = "gesmemories/image/bg/4roomd.webp"
    image bg 4roomn = "gesmemories/image/bg/4roomn.webp"
    image bg ashollcor = "gesmemories/image/bg/ashollcor.webp"
    image ashollcor_fp = "gesmemories/image/bg/ashollcor_fp.webp"
    image carride_s = "gesmemories/image/bg/carride_s.webp"
    image carride_fw = "gesmemories/image/bg/carride_fw.webp"
    image bg damage4 = "gesmemories/image/bg/damage4.webp"
    image bg darkdoor = "gesmemories/image/bg/darkdoor.webp"
    image bg dreamrain = "gesmemories/image/bg/dreamrain.webp"
    image bg farlights = "gesmemories/image/bg/farlights.webp"
    image bg firstpsy = "gesmemories/image/bg/firstpsy.webp"
    image bg lastkiss = "gesmemories/image/bg/lastkiss.webp"
    image bg liliyainblood = "gesmemories/image/bg/liliyainblood.webp"
    image bg lmdance = "gesmemories/image/bg/lmdance.webp"
    image bg lmhouse = "gesmemories/image/bg/lmhouse.webp"
    image bg lmplliya = "gesmemories/image/bg/lmplliya.webp"
    image bg lmplsolo = "gesmemories/image/bg/lmplsolo.webp"
    image bg lmrainsky = "gesmemories/image/bg/lmrainsky.webp"
    image bg lmstolovka = "gesmemories/image/bg/lmstolovka.webp"
    image bg lmsunrise = "gesmemories/image/bg/lmsunrise.webp"
    image bg medcor = "gesmemories/image/bg/medcor.webp"
    image bg medmorn = "gesmemories/image/bg/medmorn.webp"
    image bg medpalat = "gesmemories/image/bg/medpalat.webp"
    image bg mentaldushd = "gesmemories/image/bg/mentaldushd.webp"
    image bg mentaldushn = "gesmemories/image/bg/mentaldushn.webp"
    image bg mentalvannad = "gesmemories/image/bg/mentalvannad.webp"
    image bg mentalvannan = "gesmemories/image/bg/mentalvannan.webp"
    image bg mhnight = "gesmemories/image/bg/mhnight.webp"
    image bg mndascor = "gesmemories/image/bg/mndascor.webp"
    image bg mndascorn = "gesmemories/image/bg/mndascorn.webp"
    image bg mndasstol = "gesmemories/image/bg/mndasstol.webp"
    image bg mnday = "gesmemories/image/bg/mnday.webp"
    image bg mndharts = "gesmemories/image/bg/mndharts.webp"
    image bg mndlightindark1 = "gesmemories/image/bg/mndlightindark1.webp"
    image bg mndlightindark2 = "gesmemories/image/bg/mndlightindark2.webp"
    image bg mndstrrain2 = "gesmemories/image/bg/mndstrrain2.webp"
    image bg mndwindrain = "gesmemories/image/bg/mndwindrain.webp"
    image bg nsr1 = "gesmemories/image/bg/nsr1.webp"
    image bg rainskyn = "gesmemories/image/bg/rainskyn.webp"
    image bg rainsky = "gesmemories/image/bg/rainsky.webp"
    image bg strnight1 = "gesmemories/image/bg/strnight1.webp" 
    image bg vascrit = "gesmemories/image/bg/vascrit.webp"
    image bg zihcab = "gesmemories/image/bg/zihcab.webp"
    image bg finalfirstpsy = "gesmemories/image/bg/finalfirstpsy.webp"
    image bg updream = "gesmemories/image/bg/updream.webp"
    image bg llkstr = "gesmemories/image/bg/llkstr.webp"
    image bg invanna = "gesmemories/image/bg/invanna.webp"
    image bg mnd = "gesmemories/image/bg/mnd.webp"
    image bg mndliftcabin = "gesmemories/image/bg/mndliftcabin.webp"
    image bg linroom = "gesmemories/image/bg/linroom.webp"
    image bg mndkd = "gesmemories/image/bg/mndkd.webp"
    image bg mndkn = "gesmemories/image/bg/mndkn.webp"
    image bg 10room = "gesmemories/image/bg/10room.webp"
    image bg 8room = "gesmemories/image/bg/8room.webp"
    image bg mndkd = "gesmemories/image/bg/mndkd.webp"
    image bg mndkn = "gesmemories/image/bg/mndkn.webp"
    image bg mndkn = "gesmemories/image/bg/mndkn.webp"
    image bg mndpsydoor = "gesmemories/image/bg/mndpsydoor.webp"
    image bg raiseforest = "gesmemories/image/bg/raiseforest.webp"
    image bg mndaslight = "gesmemories/image/bg/mndaslight.webp"
    image bg mnddushnight = "gesmemories/image/bg/mnddushnight.webp"
    image bg mndblood1 = "gesmemories/image/bg/mndblood1.webp"
    image bg mndbloodfull = "gesmemories/image/bg/mndbloodfull.webp"
    image bg mndch2startbg = "gesmemories/image/bg/mndch2startbg.webp"
    image bg mndoldshcroom = "gesmemories/image/bg/mndoldshcroom.webp"
    image bg mndfire1 = "gesmemories/image/bg/mndfire1.webp"
    image bg mndfire2 = "gesmemories/image/bg/mndfire2.webp"
    image bg mndmshbg1 = "gesmemories/image/bg/mndmshbg1.webp"
    image bg mndmshbg3 = "gesmemories/image/bg/mndmshbg3.webp"
    image bg mndnightforest = "gesmemories/image/bg/mndnightforest.webp"
    image bg mndwolfstay = "gesmemories/image/bg/mndwolfstay.webp"
    image bg mndrunforest1 = "gesmemories/image/bg/mndrunforest1.webp"
    image bg mndinwood = "gesmemories/image/bg/mndinwood.webp"
    image bg mndforestm = "gesmemories/image/bg/mndforestm.webp"
    image bg invannablood = "gesmemories/image/bg/invannablood.webp"
    image bg mndwintforest = "gesmemories/image/bg/mndwintforest.webp"
    image bg mndablock = "gesmemories/image/bg/mndablock.webp"
    image bg mndmdoccab = "gesmemories/image/bg/mndmdoccab.webp"
    image bg mndpitroom = "gesmemories/image/bg/mndpitroom.webp"
    image bg 8roomold = "gesmemories/image/bg/8roomold.webp"
    image bg 8roomoldn = "gesmemories/image/bg/8roomoldn.webp"
    image bg mndoldcor = "gesmemories/image/bg/mndoldcor.webp"
    image bg 1roomold = "gesmemories/image/bg/1roomold.webp"
    image bg mndoldcornight = "gesmemories/image/bg/mndoldcornight.webp"
    image bg mndredforest2 = "gesmemories/image/bg/mndredforest2.webp"
    image bg mndforestpound = "gesmemories/image/bg/mndforestpound.webp"
    image bg mndforsky = "gesmemories/image/bg/mndforsky.webp"
    image mndfp_yh = "gesmemories/image/nightmare/mndfp_yh.webp"
    image bg mndroofnoara = "gesmemories/image/bg/mndroofnoara.webp"
    image bg mndwayroof = "gesmemories/image/bg/mndwayroof.webp"
    image bg mndnonumberroomold = "gesmemories/image/bg/mndnonumberroomold.webp"
    image bg mndolddush = "gesmemories/image/bg/mndolddush.webp"
    image bg mnd_lift_no_light = "gesmemories/image/bg/mnd_lift_no_light.webp"
    image bg mnd_car_night_dead = "gesmemories/image/bg/mnd_car_night_dead.webp"
    image bg mnd_lift_psy_open_door = "gesmemories/image/bg/mnd_lift_psy_open_door.webp"
    image bg mnd_grave_bg = "gesmemories/image/bg/mnd_grave_bg.webp"
    image bg mnd_lift_psy_open_door_or = "gesmemories/image/bg/mnd_lift_psy_open_door_or.webp"
    image bg mnd_lift_mine = "gesmemories/image/bg/mnd_lift_mine.webp"
    image bg mnd_a2_ch7_cor_1 = "gesmemories/image/bg/mnd_a2_ch7_cor_1.webp"
    image bg mnd_blood_drip_1 = "gesmemories/image/bg/mnd_blood_drip_1.webp"
    image bg mnd_blood_drip_2 = "gesmemories/image/bg/mnd_blood_drip_2.webp"
    image bg mnd_blood_drip_3 = "gesmemories/image/bg/mnd_blood_drip_3.webp"
    image bg mnd_blood_drip_4 = "gesmemories/image/bg/mnd_blood_drip_4.webp"
    image bg mnd_blood_drip_5 = "gesmemories/image/bg/mnd_blood_drip_5.webp"
    image bg mnd_blood_drip_6 = "gesmemories/image/bg/mnd_blood_drip_6.webp"
    image bg mnd_blood_drip_7 = "gesmemories/image/bg/mnd_blood_drip_7.webp"
    image bg mnd_blood_drip_8 = "gesmemories/image/bg/mnd_blood_drip_8.webp"
    image bg mnd_blood_drip_9 = "gesmemories/image/bg/mnd_blood_drip_9.webp"
    image bg mnd_a2_c7_lab_1_g1 = "gesmemories/image/bg/mnd_a2_c7_lab_1_g1.webp"
    image bg mnd_a2_c7_lab_1_g2 = "gesmemories/image/bg/mnd_a2_c7_lab_1_g2.webp"
    image bg mnd_a2_c7_lab_1_g3 = "gesmemories/image/bg/mnd_a2_c7_lab_1_g3.webp"
    image bg mnd_a2_c7_lab_1_gc = "gesmemories/image/bg/mnd_a2_c7_lab_1_gc.webp"
    image bg mnd_a2_c7_lab_1_d1 = "gesmemories/image/bg/mnd_a2_c7_lab_1_d1.webp"
    image bg mnd_a2_c7_lab_1_d2 = "gesmemories/image/bg/mnd_a2_c7_lab_1_d2.webp"
    image bg mnd_a2_c7_lab_1_d3 = "gesmemories/image/bg/mnd_a2_c7_lab_1_d3.webp"
    image bg mnd_a2_c7_lab_1_d4 = "gesmemories/image/bg/mnd_a2_c7_lab_1_d4.webp"
    image bg mnd_vent_1 = "gesmemories/image/bg/mnd_vent_1.webp"
    image bg mnd_sspc_bg = "gesmemories/image/bg/mnd_sspc_bg.webp"
    image bg mnd_ist_doc_cab_bg = "gesmemories/image/bg/mnd_ist_doc_cab_bg.webp"
    image mnd_ist_doc_cab = "gesmemories/image/bg/mnd_ist_doc_cab_bg.webp"
    image mnd_himori_smoke_dark = "gesmemories/image/bg/mnd_himori_smoke_dark.webp"
    image bg mnd_arahna_psy_bg = "gesmemories/image/bg/mnd_arahna_psy_bg.webp"
    image bg mnd_himori_smoke = "gesmemories/image/bg/mnd_himori_smoke.webp"
    image bg mnd_wite_cor_normal = "gesmemories/image/bg/mnd_wite_cor_normal.webp"
    image bg mnd_secret_wall_2 = "gesmemories/image/bg/mnd_secret_wall_2.webp"
    image bg mnd_secret_wall_1 = "gesmemories/image/bg/mnd_secret_wall_1.webp"
    image bg mnd_way_in_roof_night = "gesmemories/image/bg/mnd_way_in_roof_night.webp"
    image bg 4roomd_close_1 = "gesmemories/image/bg/4roomd_close_1.webp"
    image 4roomd_close_1 = "gesmemories/image/bg/4roomd_close_1.webp"
    image 4roomd_close_2 = "gesmemories/image/bg/4roomd_close_2.webp"
    image bg mnd_ar_angr_1 = "gesmemories/image/bg/mnd_ar_angr_1.webp"
    image mnd_ar_angr_1 = "gesmemories/image/bg/mnd_ar_angr_1.webp"
    image mnd_ar_angr_2 = "gesmemories/image/bg/mnd_ar_angr_2.webp"
    image bg mnd_arahna_dance_chair = "gesmemories/image/bg/mnd_arahna_dance_chair.webp"
    image 4roomd_1 = "gesmemories/image/bg/4roomd_1.webp"
    image bg mnd_final_a2_bg_mental = "gesmemories/image/bg/mnd_final_a2_bg_mental.webp"
    image bg mnd_final_a2_bg_palata = "gesmemories/image/bg/mnd_final_a2_bg_palata.webp"
    image bg mnd_winter_window = "gesmemories/image/bg/mnd_winter_window.webp"
    image bg mndggroom_n = "gesmemories/image/bg/mndggroom_n.webp"
    image bg mndggroom_n_l = "gesmemories/image/bg/mndggroom_n_l.webp"
    image bg mnd_windrain_far = "gesmemories/image/bg/mnd_windrain_far.webp"
    image bg mnd2b = "gesmemories/image/bg/mnd2b.webp"
    image mnd2b = "gesmemories/image/bg/mnd2b.webp"
    image mnd = "gesmemories/image/bg/mnd.webp"
    image bg mnd = "gesmemories/image/bg/mnd.webp"
    image bg mnd_12_shnow_str_n = "gesmemories/image/bg/mnd_12_shnow_str_n.webp"
    image bg mnd_try_gg_room_1 = "gesmemories/image/bg/mnd_try_gg_room_1.webp"
    image bg mnd_14_pk_nd = "gesmemories/image/bg/mnd_14_pk_nd.webp"
    image bg mnd_14_pk_yd = "gesmemories/image/bg/mnd_14_pk_yd.webp"
    image bg mnd_14_ten_talk_1 = "gesmemories/image/bg/mnd_14_ten_talk_1.webp"
    image bg mnd_14_ten_talk_2 = "gesmemories/image/bg/mnd_14_ten_talk_2.webp"
    image bg mnd_14_ten_talk_3 = "gesmemories/image/bg/mnd_14_ten_talk_3.webp"
    image bg mnd_14_4rtru = "gesmemories/image/bg/mnd_14_4rtru.webp"
    image bg mnd_14_memo_corinvanna = "gesmemories/image/bg/mnd_14_memo_corinvanna.webp"
    image bg mnd_podezd_gg_n = "gesmemories/image/bg/mnd_podezd_gg_n.webp"
    image bg mnd_ext_graveyard = "gesmemories/image/bg/mnd_ext_graveyard.webp"
    image bg mnd_podezd_bg = "gesmemories/image/bg/mnd_podezd_bg.webp"
    image bg mnd_gg_bath = "gesmemories/image/bg/mnd_gg_bath.webp"
    image bg mnd_doclog_nd = "gesmemories/image/bg/mnd_doclog_nd.webp"
    image bg mnd_16_fchbg = "gesmemories/image/bg/mnd_16_fchbg.webp"
    image bg mnd_16_autok_bg = "gesmemories/image/bg/mnd_16_autok_bg.webp"
    image bg mnd_16_auto_bg = "gesmemories/image/bg/mnd_16_auto_bg.webp"
    image mnd_16_autok_fakewindow = "gesmemories/image/bg/mnd_16_autok_fakewindow.webp"
    image mnd_16_auto_fakewindow = "gesmemories/image/bg/mnd_16_auto_fakewindow.webp"
    image bg mnd_ch18_kor_cent = "gesmemories/image/bg/mnd_ch18_kor_cent.webp"
    image bg mnd_ch18_cur = "gesmemories/image/bg/mnd_ch18_cur.webp"
    image bg mnd_c18_secret_door = "gesmemories/image/bg/mnd_c18_secret_door.webp"
    image bg mnd_flower_bg = "gesmemories/image/bg/mnd_flower_bg.webp"
    image carride1_fp = "gesmemories/image/bg/carride1_fp.webp"
    image bg mnd_chap18_ladder = "gesmemories/image/bg/mnd_chap18_ladder.webp"
    image bg mnd_18_cor_p_1 = "gesmemories/image/bg/mnd_18_cor_p_1.webp"
    image bg mnd_true_coridor = "gesmemories/image/bg/mnd_true_coridor.webp"





    image mnd1 = "gesmemories/image/psybg/mnd1.webp"
    image mnd2 = "gesmemories/image/psybg/mnd2.webp"
    image mnd3 = "gesmemories/image/psybg/mnd3.webp"
    image mnd4 = "gesmemories/image/psybg/mnd4.webp"
    image mnd5 = "gesmemories/image/psybg/mnd5.webp"
    image mnd6 = "gesmemories/image/psybg/mnd6.webp"
    image mnd7 = "gesmemories/image/psybg/mnd7.webp"
    image mnd8 = "gesmemories/image/psybg/mnd8.webp"
    image mnd9 = "gesmemories/image/psybg/mnd9.webp"
    image mnd10 = "gesmemories/image/psybg/mnd10.webp"
    image mnd11 = "gesmemories/image/psybg/mnd11.webp"
    image mnd12 = "gesmemories/image/psybg/mnd12.webp"
    image mnd13 = "gesmemories/image/psybg/mnd13.webp"
    image mnd14 = "gesmemories/image/psybg/mnd14.webp"
    image finalfirstpsy22 = "gesmemories/image/psybg/finalfirstpsy22.webp"
    image lastkiss22 = "gesmemories/image/psybg/lastkiss22.webp"
    image liliyainblood22 = "gesmemories/image/psybg/liliyainblood22.webp"
    image lmhit22 = "gesmemories/image/psybg/lmhit22.webp"
    image mndbloodfull22 = "gesmemories/image/psybg/mndbloodfull22.webp"
    image mndliyadead22 = "gesmemories/image/psybg/mndliyadead22.webp"
    image invanna22 = "gesmemories/image/psybg/invanna22.webp"
    image invannablood22 = "gesmemories/image/psybg/invannablood22.webp"
    image mnd_psy_doll_1 = "gesmemories/image/psybg/mnd_psy_doll_1.webp"
    image mnd_psy_doll_2 = "gesmemories/image/psybg/mnd_psy_doll_2.webp"
    image mnd_psy_doll_3 = "gesmemories/image/psybg/mnd_psy_doll_3.webp"
    image mnd_bt_a2_c7_1 = "gesmemories/image/psybg/mnd_bt_a2_c7_1.webp"
    image mnd_bt_a2_c7_2 = "gesmemories/image/psybg/mnd_bt_a2_c7_2.webp"
    image mnd_bt_a2_c7_3 = "gesmemories/image/psybg/mnd_bt_a2_c7_3.webp"
    image mnd_bt_a2_c7_4 = "gesmemories/image/psybg/mnd_bt_a2_c7_4.webp"
    image mnd_lift_no_light_green = "gesmemories/image/psybg/mnd_lift_no_light_green.webp"
    image mnd_lift_no_light_red = "gesmemories/image/psybg/mnd_lift_no_light_red.webp"
    image mnd_ring_1 = "gesmemories/image/psybg/mnd_ring_1.webp"
    image mnd_ring_2 = "gesmemories/image/psybg/mnd_ring_2.webp"
    image mnd_ring_3 = "gesmemories/image/psybg/mnd_ring_3.webp"
    image mnd_kid_dead_1 = "gesmemories/image/psybg/mnd_kid_dead_1.webp"
    image mnd_kid_dead_2 = "gesmemories/image/psybg/mnd_kid_dead_2.webp"
    image mnd_kid_dead_3 = "gesmemories/image/psybg/mnd_kid_dead_3.webp"


    image bg mnd_a2_c7_r1_nh = "gesmemories/image/psycho/mnd_a2_c7_r1_nh.webp"
    image bg mnd_a2_c7_r1_nh_na = "gesmemories/image/psycho/mnd_a2_c7_r1_nh_na.webp"
    image bg mnd_a2_c7_r1_nh_ng = "gesmemories/image/psycho/mnd_a2_c7_r1_nh_ng.webp"
    image bg mnd_a2_c7_r1_nh_np = "gesmemories/image/psycho/mnd_a2_c7_r1_nh_np.webp"
    image bg mnd_a2_c7_r1_o1 = "gesmemories/image/psycho/mnd_a2_c7_r1_o1.webp"
    image bg mnd_a2_c7_r1_o2 = "gesmemories/image/psycho/mnd_a2_c7_r1_o2.webp"
    image bg mnd_a2_c7_r1_o3 = "gesmemories/image/psycho/mnd_a2_c7_r1_o3.webp"
    image bg mnd_a2_c7_r1_o3_2 = "gesmemories/image/psycho/mnd_a2_c7_r1_o3_2.webp"
    image bg mnd_a2_c7_r1_yh = "gesmemories/image/psycho/mnd_a2_c7_r1_yh.webp"
    image bg mnd_a2_c7_r1_yh_na = "gesmemories/image/psycho/mnd_a2_c7_r1_yh_na.webp"
    image bg mnd_a2_c7_r1_yh_ng = "gesmemories/image/psycho/mnd_a2_c7_r1_yh_ng.webp"
    image bg mnd_a2_c7_r1_yh_np = "gesmemories/image/psycho/mnd_a2_c7_r1_yh_np.webp"
    image bg mnd_a2_ch7_c1_nh = "gesmemories/image/psycho/mnd_a2_ch7_c1_nh.webp"
    image bg mnd_a2_ch7_c1_yh = "gesmemories/image/psycho/mnd_a2_ch7_c1_yh.webp"
    image bg mnd_cor_suicide_bg = "gesmemories/image/psycho/mnd_cor_suicide_bg.webp"
    image bg mnd_vas_dead_bg = "gesmemories/image/psycho/mnd_vas_dead_bg.webp"
    image mnd_a2_c7_r1_map = "gesmemories/image/psycho/mnd_a2_c7_r1_map.webp"
    image mnd_psy_ten_a2 = "gesmemories/image/psycho/mnd_psy_ten_a2.webp"
    image bg mnd_a2_c7_r2_o1 = "gesmemories/image/psycho/mnd_a2_c7_r2_o1.webp"
    image bg mnd_a2_c7_r2_o2 = "gesmemories/image/psycho/mnd_a2_c7_r2_o2.webp"
    image bg mnd_a2_c7_r2_o3 = "gesmemories/image/psycho/mnd_a2_c7_r2_o3.webp"
    image mnd_a2_c7_r2_o2_message = "gesmemories/image/psycho/mnd_a2_c7_r2_o2_message.webp"
    image mnd_a2_c7_lab2_light_1 = "gesmemories/image/psycho/mnd_a2_c7_lab2_light_1.webp"
    image mnd_a2_c7_lab2_light_2 = "gesmemories/image/psycho/mnd_a2_c7_lab2_light_2.webp"
    image bg mnd_a2_c7_lab_2_d1 = "gesmemories/image/psycho/mnd_a2_c7_lab_2_d1.webp"
    image bg mnd_a2_c7_lab_2_d2 = "gesmemories/image/psycho/mnd_a2_c7_lab_2_d2.webp"
    image bg mnd_a2_c7_lab_2_d3 = "gesmemories/image/psycho/mnd_a2_c7_lab_2_d3.webp"
    image bg mnd_med_room_bg = "gesmemories/image/psycho/mnd_med_room_bg.webp"
    image mnd_medsestrichka = "gesmemories/image/psycho/mnd_medsestrichka.webp"
    image mnd_ftr_2_x_1 = "gesmemories/image/psycho/mnd_ftr_2_x_1.webp"
    image mnd_ftr_2_x_2 = "gesmemories/image/psycho/mnd_ftr_2_x_2.webp"
    image mnd_ftr_2_x_3 = "gesmemories/image/psycho/mnd_ftr_2_x_3.webp"
    image mnd_ftr_2_x_4 = "gesmemories/image/psycho/mnd_ftr_2_x_4.webp"
    image mnd_ftr_2_x_5 = "gesmemories/image/psycho/mnd_ftr_2_x_5.webp"
    image mnd_ftr_2_x_6 = "gesmemories/image/psycho/mnd_ftr_2_x_6.webp"
    image mnd_ftr_2_x_7 = "gesmemories/image/psycho/mnd_ftr_2_x_7.webp"
    image mnd_ftr_2_x_8 = "gesmemories/image/psycho/mnd_ftr_2_x_8.webp"
    image mnd_ftr_3_h_1 = "gesmemories/image/psycho/mnd_ftr_3_h_1.webp"
    image mnd_ftr_3_h_2 = "gesmemories/image/psycho/mnd_ftr_3_h_2.webp"
    image mnd_ftr_3_h_3 = "gesmemories/image/psycho/mnd_ftr_3_h_3.webp"
    image mnd_ftr_3_p_2 = "gesmemories/image/psycho/mnd_ftr_3_p_2.webp"
    image mnd_ftr_3_p_1 = "gesmemories/image/psycho/mnd_ftr_3_p_1.webp"
    image mnd_ftr_3_p_3 = "gesmemories/image/psycho/mnd_ftr_3_p_3.webp"
    image bg mnd_ftr_3_bg = "gesmemories/image/psycho/mnd_ftr_3_bg.webp"
    image bg mnd_aom_bg_1 = "gesmemories/image/psycho/mnd_aom_bg_1.webp"
    image bg mnd_med_room_bg = "gesmemories/image/psycho/mnd_med_room_bg.webp"
    image bg mnd_dead_vas_coridor_1_1 = "gesmemories/image/psycho/mnd_dead_vas_coridor_1_1.webp"
    image bg mnd_dead_vas_coridor_1_2 = "gesmemories/image/psycho/mnd_dead_vas_coridor_1_2.webp"
    image bg mnd_dead_vas_coridor_1_p1 = "gesmemories/image/psycho/mnd_dead_vas_coridor_1_p1.webp"
    image bg mnd_dead_vas_coridor_1_p2 = "gesmemories/image/psycho/mnd_dead_vas_coridor_1_p2.webp"
    image bg mnd_psy_and_vas_dio_bg = "gesmemories/image/psycho/mnd_psy_and_vas_dio_bg.webp"
    image mnd_vas_psy_axe  = "gesmemories/image/psycho/mnd_vas_psy_axe.webp"
    image mnd_dead_vas_cor_psy1  = "gesmemories/image/psycho/mnd_dead_vas_cor_psy1.webp"
    image mnd_dead_vas_cor_psy2  = "gesmemories/image/psycho/mnd_dead_vas_cor_psy2.webp"
    image mnd_psy_and_vas_dio_g1  = "gesmemories/image/psycho/mnd_psy_and_vas_dio_g1.webp"
    image mnd_psy_and_vas_dio_g2  = "gesmemories/image/psycho/mnd_psy_and_vas_dio_g2.webp"
    image mnd_psy_and_vas_dio_g3  = "gesmemories/image/psycho/mnd_psy_and_vas_dio_g3.webp"
    image mnd_c9_sbg_1  = "gesmemories/image/psycho/mnd_c9_sbg_1.webp"
    image mnd_c9_sbg_2  = "gesmemories/image/psycho/mnd_c9_sbg_2.webp"
    image mnd_d1_scr_1  = "gesmemories/image/psycho/mnd_d1_scr_1.webp"
    image bg mnd_c10_1h_room = "gesmemories/image/psycho/mnd_c10_1h_room.webp"
    image bg mnd_c10_1h_room1 = "gesmemories/image/psycho/mnd_c10_1h_room1.webp"
    image bg mnd_c10_r1_bath_1 = "gesmemories/image/psycho/mnd_c10_r1_bath_1.webp"
    image bg mnd_c10_r1_bath_2 = "gesmemories/image/psycho/mnd_c10_r1_bath_2.webp"
    image bg mnd_c10_r1_bath_3 = "gesmemories/image/psycho/mnd_c10_r1_bath_3.webp"
    image bg mnd_c10_room1_bg = "gesmemories/image/psycho/mnd_c10_room1_bg.webp"
    image mnd_c10_1h_room_eff_1 = "gesmemories/image/psycho/mnd_c10_1h_room_eff_1.webp"
    image mnd_c10_1h_room_eff_2 = "gesmemories/image/psycho/mnd_c10_1h_room_eff_2.webp"
    image mnd_c10_1h_room_eff_3 = "gesmemories/image/psycho/mnd_c10_1h_room_eff_3.webp"
    image mnd_c10_r1_dead_1 = "gesmemories/image/psycho/mnd_c10_r1_dead_1.webp"
    image mnd_c10_r1_dead_2 = "gesmemories/image/psycho/mnd_c10_r1_dead_2.webp"
    image mnd_c10_r1_key_item = "gesmemories/image/psycho/mnd_c10_r1_key_item.webp"
    image mnd_c10_r1_mess_1 = "gesmemories/image/psycho/mnd_c10_r1_mess_1.webp"
    image mnd_c10_r1_mess_2 = "gesmemories/image/psycho/mnd_c10_r1_mess_2.webp"
    image mnd_c10_r1_mess_3 = "gesmemories/image/psycho/mnd_c10_r1_mess_3.webp"
    image bg mnd_10_r2_bg = "gesmemories/image/psycho/mnd_10_r2_bg.webp"
    image bg mnd_c10_c2_bg = "gesmemories/image/psycho/mnd_c10_c2_bg.webp"
    image bg mnd_c10_r2_hbg_1 = "gesmemories/image/psycho/mnd_c10_r2_hbg_1.webp"
    image mnd_zippo_ch10 = "gesmemories/image/psycho/mnd_zippo_ch10.webp"
    image bg mnd_10_c2_lp_ld_sbg_1 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sbg_1.webp"
    image bg mnd_10_c2_lp_ld_sbg_2 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sbg_2.webp"
    image bg mnd_10_c2_lp_ld_ebg = "gesmemories/image/psycho/mnd_10_c2_lp_ld_ebg.webp"
    image bg mnd_10_c2_lp_bg = "gesmemories/image/psycho/mnd_10_c2_lp_bg.webp"
    image mnd_10_c2_lp_ld_sbg_a1 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sbg_a1.webp"
    image mnd_10_c2_lp_ld_sbg_a2 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sbg_a2.webp"
    image mnd_10_c2_lp_ld_sbg_a3 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sbg_a3.webp"
    image mnd_10_c2_lp_ld_sspr_1 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sspr_1.webp"
    image mnd_10_c2_lp_ld_sspr_2 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sspr_2.webp"
    image mnd_10_c2_lp_ld_sspr_3 = "gesmemories/image/psycho/mnd_10_c2_lp_ld_sspr_3.webp"
    image mnd_10_lp_ld_key = "gesmemories/image/psycho/mnd_10_lp_ld_key.webp"
    image mnd_10_lp_ld_otvert = "gesmemories/image/psycho/mnd_10_lp_ld_otvert.webp"
    image mnd_tvroom_bg1 = "gesmemories/image/psycho/mnd_tvroom_bg1.webp"
    image mnd_tvroom_bg2 = "gesmemories/image/psycho/mnd_tvroom_bg2.webp"
    image mnd_tvroom_1 = "gesmemories/image/psycho/mnd_tvroom_1.webp"
    image mnd_tvroom_2 = "gesmemories/image/psycho/mnd_tvroom_2.webp"
    image mnd_tvroom_3 = "gesmemories/image/psycho/mnd_tvroom_3.webp"
    image mnd_tvroom_code_1 = "gesmemories/image/psycho/mnd_tvroom_code_1.webp"
    image mnd_tvroom_code_2 = "gesmemories/image/psycho/mnd_tvroom_code_2.webp"
    image mnd_tvroom_code_3 = "gesmemories/image/psycho/mnd_tvroom_code_3.webp"
    image mnd_cl_n_1_1 = "gesmemories/image/psycho/code/mnd_cl_n_1_1.webp"
    image mnd_cl_n_1_2 = "gesmemories/image/psycho/code/mnd_cl_n_1_2.webp"
    image mnd_cl_n_1_3 = "gesmemories/image/psycho/code/mnd_cl_n_1_3.webp"
    image mnd_cl_n_1_4 = "gesmemories/image/psycho/code/mnd_cl_n_1_4.webp"
    image mnd_cl_n_1_5 = "gesmemories/image/psycho/code/mnd_cl_n_1_5.webp"
    image mnd_cl_n_1_6 = "gesmemories/image/psycho/code/mnd_cl_n_1_6.webp"
    image mnd_cl_n_2_1 = "gesmemories/image/psycho/code/mnd_cl_n_2_1.webp"
    image mnd_cl_n_2_2 = "gesmemories/image/psycho/code/mnd_cl_n_2_2.webp"
    image mnd_cl_n_2_3 = "gesmemories/image/psycho/code/mnd_cl_n_2_3.webp"
    image mnd_cl_n_2_4 = "gesmemories/image/psycho/code/mnd_cl_n_2_4.webp"
    image mnd_cl_n_2_5 = "gesmemories/image/psycho/code/mnd_cl_n_2_5.webp"
    image mnd_cl_n_2_6 = "gesmemories/image/psycho/code/mnd_cl_n_2_6.webp"
    image mnd_cl_n_3_1 = "gesmemories/image/psycho/code/mnd_cl_n_3_1.webp"
    image mnd_cl_n_3_2 = "gesmemories/image/psycho/code/mnd_cl_n_3_2.webp"
    image mnd_cl_n_3_3 = "gesmemories/image/psycho/code/mnd_cl_n_3_3.webp"
    image mnd_cl_n_3_4 = "gesmemories/image/psycho/code/mnd_cl_n_3_4.webp"
    image mnd_cl_n_3_5 = "gesmemories/image/psycho/code/mnd_cl_n_3_5.webp"
    image mnd_cl_n_3_6 = "gesmemories/image/psycho/code/mnd_cl_n_3_6.webp"
    image mnd_code_lock_open = "gesmemories/image/psycho/code/mnd_code_lock_open.webp"
    image mnd_code_lock = "gesmemories/image/psycho/code/mnd_code_lock.webp"
    image bg mnd_c10_ld_pds = "gesmemories/image/psycho/mnd_c10_ld_pds.webp"
    image bg mnd_break_glass_bg = "gesmemories/image/psycho/mnd_break_glass_bg.webp"
    image bg mnd_10_2_rp_room_bg = "gesmemories/image/psycho/mnd_10_2_rp_room_bg.webp"
    image mndtenpaper1v_ytz = "gesmemories/image/psycho/mndtenpaper1v_ytz.webp"
    image mnd_fake_key = "gesmemories/image/psycho/mnd_fake_key.webp"
    image mnd_fake_key_1 = "gesmemories/image/psycho/mnd_fake_key_1.webp"
    image bg mnd_10_rp_bg = "gesmemories/image/psycho/mnd_10_rp_bg.webp"
    image bg mnd_10_rp_2_bg = "gesmemories/image/psycho/mnd_10_rp_2_bg.webp"
    image bg mnd_10_rp2_ld_bg = "gesmemories/image/psycho/mnd_10_rp2_ld_bg.webp"
    image bg mnd_exitpsy_bg_1 = "gesmemories/image/psycho/mnd_exitpsy_bg_1.webp"
    image bg mnd_exitpsy_bg_2 = "gesmemories/image/psycho/mnd_exitpsy_bg_2.webp"
    image bg mnd_exitpsy_bg_break_vanna = "gesmemories/image/psycho/mnd_exitpsy_bg_break_vanna.webp"
    image bg mnd_exitpsy_bg_bv_wat_1 = "gesmemories/image/psycho/mnd_exitpsy_bg_bv_wat_1.webp"
    image bg mnd_exitpsy_bg_bv_wat_2 = "gesmemories/image/psycho/mnd_exitpsy_bg_bv_wat_2.webp"
    image bg mnd_exitpsy_bg_bv_wat_3 = "gesmemories/image/psycho/mnd_exitpsy_bg_bv_wat_3.webp"
    image bg mnd_exitpsy_bg_wather_in_vanna = "gesmemories/image/psycho/mnd_exitpsy_bg_wather_in_vanna.webp"
    image bg mnd_exitpsy_nolight_1 = "gesmemories/image/psycho/mnd_exitpsy_nolight_1.webp"
    image bg mnd_exitpsy_nolight_2 = "gesmemories/image/psycho/mnd_exitpsy_nolight_2.webp"
    image bg mnd_exitpsy_nolight_3 = "gesmemories/image/psycho/mnd_exitpsy_nolight_3.webp"
    image bg mnd_exitpsy_nolight_4 = "gesmemories/image/psycho/mnd_exitpsy_nolight_4.webp"
    image bg mnd_exitpsy_nolight_5 = "gesmemories/image/psycho/mnd_exitpsy_nolight_5.webp"
    image bg mnd_exitpsy_nolight_6 = "gesmemories/image/psycho/mnd_exitpsy_nolight_6.webp"
    image bg mnd_exitpsy_nolight_7 = "gesmemories/image/psycho/mnd_exitpsy_nolight_7.webp"
    image mnd_10f_bg_d_0_1 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_0_1.webp"
    image mnd_10f_bg_d_0_0 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_0_0.webp"
    image mnd_10f_bg_d_1 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_1.webp"
    image mnd_10f_bg_d_2 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_2.webp"
    image mnd_10f_bg_d_3 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_3.webp"
    image mnd_10f_bg_d_4 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_4.webp"
    image mnd_10f_bg_d_5 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_5.webp"
    image mnd_10f_bg_d_6 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_6.webp"
    image mnd_10f_bg_d_7 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_7.webp"
    image mnd_10f_bg_d_8 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_8.webp"
    image mnd_10f_bg_d_9 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_9.webp"
    image mnd_10f_bg_d_10 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_10.webp"
    image mnd_10f_bg_d_11 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_11.webp"
    image mnd_10f_bg_d_12 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_12.webp"
    image mnd_10f_bg_d_13 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_13.webp"
    image mnd_10f_bg_d_14 = "gesmemories/image/psycho/wall/mnd_10f_bg_d_14.webp"
    image mnd_10f_bg_d_open = "gesmemories/image/psycho/wall/mnd_10f_bg_d_open.webp"
    image mnd_10f_bg_f = "gesmemories/image/psycho/mnd_10f_bg_f.webp"
    image mnd_10f_w_mag_1 = "gesmemories/image/psycho/mnd_10f_w_mag_1.webp"
    image mnd_10f_w_mag_2 = "gesmemories/image/psycho/mnd_10f_w_mag_2.webp"
    image mnd_10f_w_mag_3 = "gesmemories/image/psycho/mnd_10f_w_mag_3.webp"
    image bg mnd_exitpsy_water_floor = "gesmemories/image/psycho/mnd_exitpsy_water_floor.webp"
    image bg mnd_himorI_memo_bg_1 = "gesmemories/image/psycho/mnd_himorI_memo_bg_1.webp"
    image bg mnd_himorI_memo_bg_2 = "gesmemories/image/psycho/mnd_himorI_memo_bg_2.webp"
    image bg mnd_fight_memo_1 = "gesmemories/image/psycho/mnd_fight_memo_1.webp"
    image bg mnd_fight_memo_2 = "gesmemories/image/psycho/mnd_fight_memo_2.webp"
    image bg mnd_c3_p2_lu = "gesmemories/image/psycho/mnd_c3_p2_lu.webp"
    image bg mnd_c3_p3_bg = "gesmemories/image/psycho/mnd_c3_p3_bg.webp"
    image bg mnd_10_bottom_floor_p2_ld_close = "gesmemories/image/psycho/mnd_10_bottom_floor_p2_ld_close.webp"
    image bg mnd_10_cafe_bg = "gesmemories/image/psycho/mnd_10_cafe_bg.webp"
    image bg mnd_10_c3_p1_ld = "gesmemories/image/psycho/mnd_10_c3_p1_ld.webp"
    image bg mnd_c3_p2_bg = "gesmemories/image/psycho/mnd_c3_p2_bg.webp"
    image bg mnd_himori_cab_bg = "gesmemories/image/psycho/mnd_himori_cab_bg.webp"
    image bg mnd_10_cd_bg = "gesmemories/image/psycho/mnd_10_cd_bg.webp"
    image bg mnd_fvcd_bg = "gesmemories/image/psycho/mnd_fvcd_bg.webp"
    image mnd_flaga_spr = "gesmemories/image/psycho/mnd_flaga_spr.webp"
    image mnd_fvcd_doc = "gesmemories/image/psycho/mnd_fvcd_doc.webp"
    image mnd_10_cd_gkey = "gesmemories/image/psycho/mnd_10_cd_gkey.webp"
    image mnd_fvcd_walls = "gesmemories/image/psycho/mnd_fvcd_walls.webp"
    image mnd_fvcd_screamer = "gesmemories/image/psycho/mnd_fvcd_screamer.webp"
    image bg mnd_c10_room1_bg_bw = "gesmemories/image/psycho/mnd_c10_room1_bg_bw.webp"
    image bg mnd_10_roof_bg = "gesmemories/image/psycho/mnd_10_roof_bg.webp"
    image bg mnd_10_c3_p2_roof_exit = "gesmemories/image/psycho/mnd_10_c3_p2_roof_exit.webp"
    image mnd_c10_room1_posilka = "gesmemories/image/psycho/mnd_c10_room1_posilka.webp"
    image mnd_10_tape_spr = "gesmemories/image/psycho/mnd_10_tape_spr.webp"
    image mnd_10_roof_mes = "gesmemories/image/psycho/mnd_10_roof_mes.webp"
    image bg mnd_basement10_bg = "gesmemories/image/psycho/mnd_basement10_bg.webp"
    image bg mnd_10_bot_coridor_bg = "gesmemories/image/psycho/mnd_10_bot_coridor_bg.webp"
    image bg mnd_10_dociventcab_bg = "gesmemories/image/psycho/mnd_10_dociventcab_bg.webp"
    image bg mnd_10_go_bodv_bg = "gesmemories/image/psycho/mnd_10_go_bodv_bg.webp"
    image bg mnd_shahta10_bg = "gesmemories/image/psycho/mnd_shahta10_bg.webp"
    image bg mnd_basement10_wrong_bg = "gesmemories/image/psycho/mnd_basement10_wrong_bg.webp"
    image bg mnd_basement10_2d_bg = "gesmemories/image/psycho/mnd_basement10_2d_bg.webp"
    image bg mnd_waterhome_bg = "gesmemories/image/psycho/mnd_waterhome_bg.webp"
    image bg mnd_powerroom10_bg = "gesmemories/image/psycho/mnd_powerroom10_bg.webp"
    image bg mnddushnigh2 = "gesmemories/image/psycho/mnddushnigh2.webp"
    image bg mnddushnigh1 = "gesmemories/image/psycho/mnddushnigh1.webp"
    image mnd_bf_doc_mes_spr1 = "gesmemories/image/psycho/mnd_bf_doc_mes_spr1.webp"
    image mnd_bf_doc_mes_spr2 = "gesmemories/image/psycho/mnd_bf_doc_mes_spr2.webp"
    image mnd_bf_doc_mes_spr3 = "gesmemories/image/psycho/mnd_bf_doc_mes_spr3.webp"
    image mnd_bf_doc_mes_spr4 = "gesmemories/image/psycho/mnd_bf_doc_mes_spr4.webp"
    image mnd_fake_key4 = "gesmemories/image/psycho/mnd_fake_key4.webp"
    image mnd_waterhome_mes_spr = "gesmemories/image/psycho/mnd_waterhome_mes_spr.webp"
    image mnd_light_house_mes_spr = "gesmemories/image/psycho/mnd_light_house_mes_spr.webp"
    image mnd_shahta10_key_spr = "gesmemories/image/psycho/mnd_shahta10_key_spr.webp"
    image bg mnd_10_fsc_bg_1 = "gesmemories/image/psycho/mnd_10_fsc_bg_1.webp"
    image bg mnd_10_fsc_bg_2 = "gesmemories/image/psycho/mnd_10_fsc_bg_2.webp"
    image bg mnd_10_fsc_bg_3 = "gesmemories/image/psycho/mnd_10_fsc_bg_3.webp"
    image bg mnd_10_fsc_bg_4 = "gesmemories/image/psycho/mnd_10_fsc_bg_4.webp"
    image bg mnd_run_10_bg = "gesmemories/image/psycho/mnd_run_10_bg.webp"
    image mnd_10_fsc_bg_1_vasp = "gesmemories/image/psycho/mnd_10_fsc_bg_1_vasp.webp"
    image bg mnd_arah_bw = "gesmemories/image/psycho/mnd_arah_bw.webp"
    image bg mnd_arah_foll_12 = "gesmemories/image/psycho/mnd_arah_foll_12.webp"
    image bg mnd_ch11_bg3_up = "gesmemories/image/psycho/mnd_ch11_bg3_up.webp"
    image bg mnd_ch11_axe_fb1 = "gesmemories/image/psycho/mnd_ch11_axe_fb1.webp"
    image mnd_ch11_axe_hit = "gesmemories/image/psycho/mnd_ch11_axe_hit.webp"
    image mnd_ch11_axe_in_hand_1 = "gesmemories/image/psycho/mnd_ch11_axe_in_hand_1.webp"
    image mnd_ch11_axe_z = "gesmemories/image/psycho/mnd_ch11_axe_z.webp"
    image bg mnd_ch11_bg1 = "gesmemories/image/psycho/mnd_ch11_bg1.webp"
    image bg mnd_ch11_bg3_down = "gesmemories/image/psycho/mnd_ch11_bg3_down.webp"
    image mndggroom_p_p2 = "gesmemories/image/psycho/mndggroom_p_p2.webp"
    image mndggroom_p_p1 = "gesmemories/image/psycho/mndggroom_p_p1.webp"
    image mnd_aom_hand2_3 = "gesmemories/image/psycho/mnd_aom_hand2_3.webp"
    image mnd_aom_hand2_2 = "gesmemories/image/psycho/mnd_aom_hand2_2.webp"
    image mnd_aom_hand2_1 = "gesmemories/image/psycho/mnd_aom_hand2_1.webp"
    image mnd_aom_hand1_3 = "gesmemories/image/psycho/mnd_aom_hand1_3.webp"
    image mnd_aom_hand1_2 = "gesmemories/image/psycho/mnd_aom_hand1_2.webp"
    image mnd_aom_hand1_1 = "gesmemories/image/psycho/mnd_aom_hand1_1.webp"
    image mnd_vas_psy_axe_fake = "gesmemories/image/psycho/mnd_vas_psy_axe_fake.webp"
    image mnd_vas_psy_axe_true = "gesmemories/image/psycho/mnd_vas_psy_axe_true.webp"



    image mnd_c11_wa_b1_s1 = "gesmemories/image/trymemo/mnd_c11_wa_b1_s1.webp"
    image mnd_c11_wa_b1_s2 = "gesmemories/image/trymemo/mnd_c11_wa_b1_s2.webp"
    image mnd_c11_wa_b1_s3 = "gesmemories/image/trymemo/mnd_c11_wa_b1_s3.webp"
    image mnd_c11_wa_b1_s4 = "gesmemories/image/trymemo/mnd_c11_wa_b1_s4.webp"
    image mnd_c11_wa_b1_stay = "gesmemories/image/trymemo/mnd_c11_wa_b1_stay.webp"
    image mnd_c11_wa_b1_stay_f = "gesmemories/image/trymemo/mnd_c11_wa_b1_stay_f.webp"
    image bg mnd_ch11_bg1 = "gesmemories/image/trymemo/mnd_ch11_bg1.webp"
    image mnd_ch11_who1_g1 = "gesmemories/image/trymemo/mnd_ch11_who1_g1.webp"
    image mnd_ch11_who1_g2 = "gesmemories/image/trymemo/mnd_ch11_who1_g2.webp"
    image mnd_ch11_who1_g3 = "gesmemories/image/trymemo/mnd_ch11_who1_g3.webp"
    image mnd_ch11_who1_spr = "gesmemories/image/trymemo/mnd_ch11_who1_spr.webp"
    image mnd_c11_wa_s_axe_1 = "gesmemories/image/trymemo/mnd_c11_wa_s_axe_1.webp"
    image mnd_c11_wa_s_axe_2 = "gesmemories/image/trymemo/mnd_c11_wa_s_axe_2.webp"
    image mnd_c11_wa_s_axe_3 = "gesmemories/image/trymemo/mnd_c11_wa_s_axe_3.webp"
    image mnd_c11_wa_s_axe_4 = "gesmemories/image/trymemo/mnd_c11_wa_s_axe_4.webp"
    image mnd_13_lk_spr = "gesmemories/image/trymemo/mnd_13_lk_spr.webp"
    image mnd_c11_wa_stay_axe = "gesmemories/image/trymemo/mnd_c11_wa_stay_axe.webp"
    image mnd_c11_wa_stay_end_axe = "gesmemories/image/trymemo/mnd_c11_wa_stay_end_axe.webp"
    image mnd_c13_ladd_stay = "gesmemories/image/trymemo/mnd_c13_ladd_stay.webp"
    image mnd_c13_ladd_stay_axe = "gesmemories/image/trymemo/mnd_c13_ladd_stay_axe.webp"
    image bg mnd_ch11_bg2_1 = "gesmemories/image/trymemo/mnd_ch11_bg2_1.webp"
    image bg mnd_ch11_bg2_2 = "gesmemories/image/trymemo/mnd_ch11_bg2_2.webp"
    image bg mnd_ch11_bg2_lc = "gesmemories/image/trymemo/mnd_ch11_bg2_lc.webp"
    image bg mnd_ch11_bg2_lo = "gesmemories/image/trymemo/mnd_ch11_bg2_lo.webp"
    image bg mnd_ch11_doors1 = "gesmemories/image/trymemo/mnd_ch11_doors1.webp"
    image bg mnd_ch11_doors2 = "gesmemories/image/trymemo/mnd_ch11_doors2.webp"
    image bg mnd_ch11_doors3 = "gesmemories/image/trymemo/mnd_ch11_doors3.webp"
    image bg mnd_ch11_doors4 = "gesmemories/image/trymemo/mnd_ch11_doors4.webp"
    image bg mnd_ch11_doors5 = "gesmemories/image/trymemo/mnd_ch11_doors5.webp"
    image bg mnd_ch11_doors6 = "gesmemories/image/trymemo/mnd_ch11_doors6.webp"
    image bg mnd_ch11_ladder = "gesmemories/image/trymemo/mnd_ch11_ladder.webp"
    image bg mnd_ch11_room1 = "gesmemories/image/trymemo/mnd_ch11_room1.webp"
    image bg mnd_ch11_up_floor = "gesmemories/image/trymemo/mnd_ch11_up_floor.webp"
    image bg mnd_ch13_base_cor = "gesmemories/image/trymemo/mnd_ch13_base_cor.webp"
    image mnd_ch13_db_1 = "gesmemories/image/trymemo/mnd_ch13_db_1.webp"
    image mnd_ch13_db_2 = "gesmemories/image/trymemo/mnd_ch13_db_2.webp"
    image mnd_ch13_db_3 = "gesmemories/image/trymemo/mnd_ch13_db_3.webp"
    image mnd_ch13_db_4 = "gesmemories/image/trymemo/mnd_ch13_db_4.webp"
    image mnd_ch13_db_5 = "gesmemories/image/trymemo/mnd_ch13_db_5.webp"
    image mnd_ch13_lk_h_1 = "gesmemories/image/trymemo/mnd_ch13_lk_h_1.webp"
    image mnd_ch13_lk_h_2 = "gesmemories/image/trymemo/mnd_ch13_lk_h_2.webp"
    image mnd_ch13_lk_h_3 = "gesmemories/image/trymemo/mnd_ch13_lk_h_3.webp"
    image bg mnd_lift_mine_baw = "gesmemories/image/trymemo/mnd_lift_mine_baw.webp"
    image mnd_paket_ch13_1 = "gesmemories/image/trymemo/mnd_paket_ch13_1.webp"
    image mnd_paket_ch13_2 = "gesmemories/image/trymemo/mnd_paket_ch13_2.webp"
    image mnd_paket_ch13_3 = "gesmemories/image/trymemo/mnd_paket_ch13_3.webp"
    image mnd_qte_button_w = "gesmemories/image/trymemo/mnd_qte_button_w.webp"
    image mnd_qte_fone_1 = "gesmemories/image/trymemo/mnd_qte_fone_1.webp"
    image mnd_qte_fone_2 = "gesmemories/image/trymemo/mnd_qte_fone_2.webp"
    image bg mnd_shaht_down_bg13 = "gesmemories/image/trymemo/mnd_shaht_down_bg13.webp"
    image bg mnd_skyrain_baw = "gesmemories/image/trymemo/mnd_skyrain_baw.webp"
    image bg mnd_13_3k_cor_1 = "gesmemories/image/trymemo/mnd_13_3k_cor_1.webp"
    image bg mnd_13_3k_cor_2 = "gesmemories/image/trymemo/mnd_13_3k_cor_2.webp"
    image bg mnd_13_3k_cor_3 = "gesmemories/image/trymemo/mnd_13_3k_cor_3.webp"
    image bg mnd_13_3k_cor_4 = "gesmemories/image/trymemo/mnd_13_3k_cor_4.webp"
    image bg mnd_13_3k_cor_5 = "gesmemories/image/trymemo/mnd_13_3k_cor_5.webp"
    image bg mnd_13_3k_cor_6 = "gesmemories/image/trymemo/mnd_13_3k_cor_6.webp"
    image bg mnd_13_3k_cor_jump_1 = "gesmemories/image/trymemo/mnd_13_3k_cor_jump_1.webp"
    image bg mnd_13_3k_cor_jump_1_j = "gesmemories/image/trymemo/mnd_13_3k_cor_jump_1_j.webp"
    image bg mnd_13_10c_base_bg = "gesmemories/image/trymemo/mnd_13_10c_base_bg.webp"
    image bg mnd_13_10c_bath_bg = "gesmemories/image/trymemo/mnd_13_10c_bath_bg.webp"
    image bg mnd_13_10c_code_color = "gesmemories/image/trymemo/mnd_13_10c_code_color.webp"
    image bg mnd_13_10c_f10_bg = "gesmemories/image/trymemo/mnd_13_10c_f10_bg.webp"
    image bg mnd_13_10c_f10_bg_od = "gesmemories/image/trymemo/mnd_13_10c_f10_bg_od.webp"
    image bg mnd_13_10c_fimale_lc = "gesmemories/image/trymemo/mnd_13_10c_fimale_lc.webp"
    image bg mnd_13_10c_fimale_lo = "gesmemories/image/trymemo/mnd_13_10c_fimale_lo.webp"
    image bg mnd_13_10c_himori_kab_bg = "gesmemories/image/trymemo/mnd_13_10c_himori_kab_bg.webp"
    image bg mnd_13_10c_k1_bg = "gesmemories/image/trymemo/mnd_13_10c_k1_bg.webp"
    image bg mnd_13_10c_k1_lp_bg = "gesmemories/image/trymemo/mnd_13_10c_k1_lp_bg.webp"
    image bg mnd_13_10c_k1_rp_bg = "gesmemories/image/trymemo/mnd_13_10c_k1_rp_bg.webp"
    image bg mnd_13_10c_k1_rp_ld_bg1 = "gesmemories/image/trymemo/mnd_13_10c_k1_rp_ld_bg1.webp"
    image bg mnd_13_10c_k1_rp_ld_bg2 = "gesmemories/image/trymemo/mnd_13_10c_k1_rp_ld_bg2.webp"
    image bg mnd_13_10c_k1_rp_rp_bg = "gesmemories/image/trymemo/mnd_13_10c_k1_rp_rp_bg.webp"
    image bg mnd_13_10c_k2_ck1_bg = "gesmemories/image/trymemo/mnd_13_10c_k2_ck1_bg.webp"
    image bg mnd_13_10c_k2_ck2_bg = "gesmemories/image/trymemo/mnd_13_10c_k2_ck2_bg.webp"
    image bg mnd_13_10c_k2_ld_bg = "gesmemories/image/trymemo/mnd_13_10c_k2_ld_bg.webp"
    image bg mnd_13_10c_pr_bg = "gesmemories/image/trymemo/mnd_13_10c_pr_bg.webp"
    image mnd_13_10c_pr_bg_dec_1  = "gesmemories/image/trymemo/mnd_13_10c_pr_bg_dec_1.webp"
    image mnd_13_10c_pr_bg_dec_2  = "gesmemories/image/trymemo/mnd_13_10c_pr_bg_dec_2.webp"
    image mnd_13_10c_provod  = "gesmemories/image/trymemo/mnd_13_10c_provod.webp"
    image mnd_13_10c_skey  = "gesmemories/image/trymemo/mnd_13_10c_skey.webp"
    image bg mnd_13_10c_sklad_bg = "gesmemories/image/trymemo/mnd_13_10c_sklad_bg.webp"
    image mnd_13_10c_tape_spr = "gesmemories/image/trymemo/mnd_13_10c_tape_spr.webp"
    image bg mnd_13_10c_tr_bg = "gesmemories/image/trymemo/mnd_13_10c_tr_bg.webp"
    image mnd_13_10c_tvr_axe  = "gesmemories/image/trymemo/mnd_13_10c_tvr_axe.webp"
    image mnd_13_10c_tvr_bc  = "gesmemories/image/trymemo/mnd_13_10c_tvr_bc.webp"
    image mnd_13_10c_tvr_bo  = "gesmemories/image/trymemo/mnd_13_10c_tvr_bo.webp"
    image bg mnd_13_10c_tvr_bc  = "gesmemories/image/trymemo/mnd_13_10c_tvr_bc.webp"
    image bg mnd_13_10c_tvr_bo  = "gesmemories/image/trymemo/mnd_13_10c_tvr_bo.webp"
    image mnd_13_10c_tvr_code  = "gesmemories/image/trymemo/mnd_13_10c_tvr_code.webp"
    image bg mnd_13_10c_wr_bg = "gesmemories/image/trymemo/mnd_13_10c_wr_bg.webp"
    image bg mnd_13_ascor_1 = "gesmemories/image/trymemo/mnd_13_ascor_1.webp"
    image bg mnd_13_ascor_2 = "gesmemories/image/trymemo/mnd_13_ascor_2.webp"
    image bg mnd_13_ascor_3 = "gesmemories/image/trymemo/mnd_13_ascor_3.webp"
    image bg mnd_13_blood_bath = "gesmemories/image/trymemo/mnd_13_blood_bath.webp"
    image bg mnd_13_bot_s_bg_1 = "gesmemories/image/trymemo/mnd_13_bot_s_bg_1.webp"
    image bg mnd_13_bot_s_bg_2 = "gesmemories/image/trymemo/mnd_13_bot_s_bg_2.webp"
    image bg mnd_13_bot_s_bg_3 = "gesmemories/image/trymemo/mnd_13_bot_s_bg_3.webp"
    image bg mnd_13_bot_s_bg_4 = "gesmemories/image/trymemo/mnd_13_bot_s_bg_4.webp"
    image bg mnd_13_bot_s_bg_5 = "gesmemories/image/trymemo/mnd_13_bot_s_bg_5.webp"
    image bg mnd_13_bot_s_bg_6 = "gesmemories/image/trymemo/mnd_13_bot_s_bg_6.webp"
    image bg mnd_13_kur = "gesmemories/image/trymemo/mnd_13_kur.webp"
    image bg mnd_13_vent_fall = "gesmemories/image/trymemo/mnd_13_vent_fall.webp"
    image mnd_ch11_key  = "gesmemories/image/trymemo/mnd_ch11_key.webp"
    image mnd_qte_button_e  = "gesmemories/image/trymemo/mnd_qte_button_e.webp"
    image mnd_qte_button_r  = "gesmemories/image/trymemo/mnd_qte_button_r.webp"
    image bg mnd_13_3k_bf_l1 = "gesmemories/image/trymemo/mnd_13_3k_bf_l1.webp"
    image bg mnd_13_3k_bf_l2 = "gesmemories/image/trymemo/mnd_13_3k_bf_l2.webp"
    image bg mnd_13_3k_bf_l3 = "gesmemories/image/trymemo/mnd_13_3k_bf_l3.webp"
    image mnd_13_3k_bf_ld_1  = "gesmemories/image/trymemo/mnd_13_3k_bf_ld_1.webp"
    image mnd_13_3k_bf_ld_2  = "gesmemories/image/trymemo/mnd_13_3k_bf_ld_2.webp"
    image bg mnd_13_3k_cor_block = "gesmemories/image/trymemo/mnd_13_3k_cor_block.webp"
    image bg mnd_13_3k_cor_block2 = "gesmemories/image/trymemo/mnd_13_3k_cor_block2.webp"
    image bg mnd_13_3k_cor_move_1 = "gesmemories/image/trymemo/mnd_13_3k_cor_move_1.webp"
    image bg mnd_13_3k_cor_move_2 = "gesmemories/image/trymemo/mnd_13_3k_cor_move_2.webp"
    image bg mnd_13_3k_cor_move_3 = "gesmemories/image/trymemo/mnd_13_3k_cor_move_3.webp"
    image bg mnd_13_3k_cor_move_4 = "gesmemories/image/trymemo/mnd_13_3k_cor_move_4.webp"
    image bg mnd_13_3k_cor_move_5 = "gesmemories/image/trymemo/mnd_13_3k_cor_move_5.webp"
    image bg mnd_13_3k_cor_r_1 = "gesmemories/image/trymemo/mnd_13_3k_cor_r_1.webp"
    image bg mnd_13_3k_cor_r_2 = "gesmemories/image/trymemo/mnd_13_3k_cor_r_2.webp"
    image bg mnd_13_3k_cor_r_3 = "gesmemories/image/trymemo/mnd_13_3k_cor_r_3.webp"
    image bg mnd_13_3k_cor_r_4 = "gesmemories/image/trymemo/mnd_13_3k_cor_r_4.webp"
    image bg mnd_13_3k_cor_r_5 = "gesmemories/image/trymemo/mnd_13_3k_cor_r_5.webp"
    image bg mnd_13_3k_mv_1 = "gesmemories/image/trymemo/mnd_13_3k_mv_1.webp"
    image bg mnd_13_3k_mv_2 = "gesmemories/image/trymemo/mnd_13_3k_mv_2.webp"
    image bg mnd_13_3k_mv_3 = "gesmemories/image/trymemo/mnd_13_3k_mv_3.webp"
    image bg mnd_13_3k_mv_4 = "gesmemories/image/trymemo/mnd_13_3k_mv_4.webp"
    image bg mnd_13_3k_mv_5 = "gesmemories/image/trymemo/mnd_13_3k_mv_5.webp"
    image bg mnd_13_3k_mv_6 = "gesmemories/image/trymemo/mnd_13_3k_mv_6.webp"
    image bg mnd_13_3k_mv_7 = "gesmemories/image/trymemo/mnd_13_3k_mv_7.webp"
    image bg mnd_13_3k_mv_8 = "gesmemories/image/trymemo/mnd_13_3k_mv_8.webp"
    image bg mnd_13_3k_mv_9 = "gesmemories/image/trymemo/mnd_13_3k_mv_9.webp"
    image bg mnd_13_3k_mv_10 = "gesmemories/image/trymemo/mnd_13_3k_mv_10.webp"
    image bg mnd_13_3k_mv_11 = "gesmemories/image/trymemo/mnd_13_3k_mv_11.webp"
    image mnd_13_darkness_1  = "gesmemories/image/trymemo/mnd_13_darkness_1.webp"
    image mnd_13_darkness_2  = "gesmemories/image/trymemo/mnd_13_darkness_2.webp"
    image mnd_13_darkness_3  = "gesmemories/image/trymemo/mnd_13_darkness_3.webp"
    image mnd_13_darkness_4  = "gesmemories/image/trymemo/mnd_13_darkness_4.webp"



















    image bg mndcorpsy1 = "gesmemories/image/nightmare/mndcorpsy1.webp"
    image bg mndcorpsy2 = "gesmemories/image/nightmare/mndcorpsy2.webp"
    image bg mndfr_nh = "gesmemories/image/nightmare/mndfr_nh.webp"
    image mndtenpaper1_ntz  = "gesmemories/image/nightmare/mndtenpaper1_ntz.webp"
    image mndtenpaper1_ytz  = "gesmemories/image/nightmare/mndtenpaper1_ytz.webp"
    image mndlinda  = "gesmemories/image/nightmare/mndlinda.webp"
    image mndphotopsy  = "gesmemories/image/nightmare/mndphotopsy.webp"
    image bg mndtenpsyfsc_d = "gesmemories/image/nightmare/mndtenpsyfsc_d.webp"
    image bg mndtenpsyfsc_l = "gesmemories/image/nightmare/mndtenpsyfsc_l.webp"
    image bg mndtenpsylight_f = "gesmemories/image/nightmare/mndtenpsylight_f.webp"
    image bg mndlight_c = "gesmemories/image/nightmare/mndlight_c.webp"
    image bg mnddoorlight_nh = "gesmemories/image/nightmare/mnddoorlight_nh.webp"
    image bg mndpsycor1_1 = "gesmemories/image/nightmare/mndpsycor1_1.webp"
    image bg mndpsycor1_2 = "gesmemories/image/nightmare/mndpsycor1_2.webp"
    image bg mndpsycor1_3 = "gesmemories/image/nightmare/mndpsycor1_3.webp"
    image bg mndpsycor1_4 = "gesmemories/image/nightmare/mndpsycor1_4.webp"
    image bg mndpsycor1_5 = "gesmemories/image/nightmare/mndpsycor1_5.webp"
    image bg mndpsycor1_6 = "gesmemories/image/nightmare/mndpsycor1_6.webp"
    image bg mndpsycor1_7 = "gesmemories/image/nightmare/mndpsycor1_7.webp"
    image bg mndpsycor1_8 = "gesmemories/image/nightmare/mndpsycor1_8.webp"
    image bg mndpsycor1_9 = "gesmemories/image/nightmare/mndpsycor1_9.webp"
    image bg mndpsycor1_10 = "gesmemories/image/nightmare/mndpsycor1_10.webp"
    image bg mndpsycor1_11 = "gesmemories/image/nightmare/mndpsycor1_11.webp"
    image bg mndpsycor1_12 = "gesmemories/image/nightmare/mndpsycor1_12.webp"
    image bg mndpsycor2_1 = "gesmemories/image/nightmare/mndpsycor2_1.webp"
    image bg mndpsycor2_2 = "gesmemories/image/nightmare/mndpsycor2_2.webp"
    image bg mndpsycor2_3 = "gesmemories/image/nightmare/mndpsycor2_3.webp"
    image bg mnd3door1 = "gesmemories/image/nightmare/mnd3door1.webp"
    image bg mnd3door2 = "gesmemories/image/nightmare/mnd3door2.webp"
    image bg mndnr1_nh = "gesmemories/image/nightmare/mndnr1_nh.webp"
    image mndoldclock = "gesmemories/image/nightmare/mndoldclock.webp"
    image mndcorscr = "gesmemories/image/nightmare/mndcorscr.webp"
    image bg mndgameover = "gesmemories/image/nightmare/mndgameover.webp"
    image bg mndwebcorold = "gesmemories/image/nightmare/mndwebcorold.webp"


    image mndsd1 = "gesmemories/image/logo/mndsd1.webp"
    image mndsd2 = "gesmemories/image/logo/mndsd2.webp"
    image testph2 = "gesmemories/image/logo/testph2.webp"
    image liyapaint = "gesmemories/image/logo/liyapaint.webp"
    image bg mndps = "gesmemories/image/logo/mndps.webp"
    image savemess = "gesmemories/image/logo/savemess.webp"
    image mndgessplash = "gesmemories/image/logo/mndgessplash.webp"
    image bg mndc1l1 = "gesmemories/image/logo/mndc1l1.webp"
    image bg mndc1l2 = "gesmemories/image/logo/mndc1l2.webp"
    image bg mndch2l1 = "gesmemories/image/logo/mndch2l1.webp"
    image bg mndch2l2 = "gesmemories/image/logo/mndch2l2.webp"
    image bg mndch2l3 = "gesmemories/image/logo/mndch2l3.webp"
    image bg mndch2l4 = "gesmemories/image/logo/mndch2l4.webp"
    image sprtbk  = "gesmemories/image/logo/sprtbk.webp"
    image mndch4l1 = "gesmemories/image/logo/mndch4l1.webp"
    image mndch4l2 = "gesmemories/image/logo/mndch4l2.webp"
    image mndch4l3 = "gesmemories/image/logo/mndch4l3.webp"
    image bg mndalienmemologo = "gesmemories/image/logo/mndalienmemologo.webp"
    image mndfinal1actn1 = "gesmemories/image/logo/mndfinal1actn1.webp"
    image mndfinal1actn2 = "gesmemories/image/logo/mndfinal1actn2.webp"
    image mnd_2act_logo = "gesmemories/image/logo/mnd_2act_logo.webp"
    image mnd_lift_psy_1 = "gesmemories/image/logo/mnd_lift_psy_1.webp"
    image mnd_lift_psy_2 = "gesmemories/image/logo/mnd_lift_psy_2.webp"
    image mnd_lift_psy_3 = "gesmemories/image/logo/mnd_lift_psy_3.webp"
    image mnd_lift_psy_4 = "gesmemories/image/logo/mnd_lift_psy_4.webp"
    image mnd_lift_psy_5 = "gesmemories/image/logo/mnd_lift_psy_5.webp"
    image mnd_lift_psy_6 = "gesmemories/image/logo/mnd_lift_psy_6.webp"
    image mnd_lift_psy_7 = "gesmemories/image/logo/mnd_lift_psy_7.webp"
    image mnd_lift_psy_8 = "gesmemories/image/logo/mnd_lift_psy_8.webp"
    image mnd_himore_scene_smoke_1 = "gesmemories/image/logo/mnd_himore_scene_smoke_1.webp"
    image mnd_himore_scene_smoke_2 = "gesmemories/image/logo/mnd_himore_scene_smoke_2.webp"
    image mnd_a2final_logo_1 = "gesmemories/image/logo/mnd_a2final_logo_1.webp"
    image mnd_a2final_logo_2 = "gesmemories/image/logo/mnd_a2final_logo_2.webp"
    image mnd_a2final_logo_3 = "gesmemories/image/logo/mnd_a2final_logo_3.webp"
    image mnd_a2final_logo_4 = "gesmemories/image/logo/mnd_a2final_logo_4.webp"
    image mnd_snow = "gesmemories/image/logo/mnd_snow.webp"
    image mnd_winter_window_no_back = "gesmemories/image/logo/mnd_winter_window_no_back.webp"
    image mnd_windrain_close = "gesmemories/image/logo/mnd_windrain_close.webp"
    image mnd_load_scr_1 = "gesmemories/image/logo/mnd_load_scr_1.webp"
    image mnd_load_scr_2 = "gesmemories/image/logo/mnd_load_scr_2.webp"
    image mnd_load_scr_3 = "gesmemories/image/logo/mnd_load_scr_3.webp"
    image mnd_load_scr_4 = "gesmemories/image/logo/mnd_load_scr_4.webp"
    image mnd_load_scr_5 = "gesmemories/image/logo/mnd_load_scr_5.webp"
    image mnd_load_scr_6 = "gesmemories/image/logo/mnd_load_scr_6.webp"
    image mnd_12_phone_n_1am = "gesmemories/image/logo/mnd_12_phone_n_1am.webp"
    image mnd_12_phone_n = "gesmemories/image/logo/mnd_12_phone_n.webp"
    image mnd_12_phone_n_r = "gesmemories/image/logo/mnd_12_phone_n_r.webp"
    image mnd_12_phone_n_rt = "gesmemories/image/logo/mnd_12_phone_n_1am.webp"
    image mndggroom_p_s = "gesmemories/image/logo/mndggroom_p_s.webp"
    image mndggroom_p_l = "gesmemories/image/logo/mndggroom_p_l.webp"
    image mnd_a3_menu_1 = "gesmemories/image/logo/mnd_a3_menu_1.webp"
    image mnd_a3_menu_2 = "gesmemories/image/logo/mnd_a3_menu_2.webp"
    image mnd_new_dis_1 = "gesmemories/image/logo/mnd_new_dis_1.webp"
    image mnd_new_dis_2 = "gesmemories/image/logo/mnd_new_dis_2.webp"
    image mnd_new_dis_3 = "gesmemories/image/logo/mnd_new_dis_3.webp"
    image mnd_tv_spr_true = "gesmemories/image/logo/mnd_tv_spr_true.webp"
    image mnd_podezd_fakewindow = "gesmemories/image/logo/mnd_podezd_fakewindow.webp"
    image mnd_auto_fakewindow = "gesmemories/image/logo/mnd_auto_fakewindow.webp"
    image bg mnd_18_t1 = "gesmemories/image/logo/mnd_18_t1.webp"
    image bg mnd_18_t2 = "gesmemories/image/logo/mnd_18_t2.webp"
    image bg mnd_18_t3 = "gesmemories/image/logo/mnd_18_t3.webp"
    image bg mnd_18_t4 = "gesmemories/image/logo/mnd_18_t4.webp"
    image bg mnd_18_t5 = "gesmemories/image/logo/mnd_18_t5.webp"
    image bg mnd_18_t6 = "gesmemories/image/logo/mnd_18_t6.webp"
    image bg mnd_18_t7 = "gesmemories/image/logo/mnd_18_t7.webp"
    image bg mnd_18_t8 = "gesmemories/image/logo/mnd_18_t8.webp"
    image bg mnd_18_t9 = "gesmemories/image/logo/mnd_18_t9.webp"
    image bg mnd_sb_mm_mf_bg = "gesmemories/image/logo/mnd_sb_mm_mf_bg.webp"
    image mnd_sb_mm_mf_1 = "gesmemories/image/logo/mnd_sb_mm_mf_1.webp"
    image mnd_sb_mm_mf_2 = "gesmemories/image/logo/mnd_sb_mm_mf_2.webp"
    image mnd_sb_mm_mf_spr = "gesmemories/image/logo/mnd_sb_mm_mf_spr.webp"
    image mnd_r_ges_spl = "gesmemories/image/logo/mnd_r_ges_spl.webp"
    image bg mnd_r_int_bg_1 = "gesmemories/image/logo/mnd_r_int_bg_1.webp"
    image bg mnd_r_int_bg_2 = "gesmemories/image/logo/mnd_r_int_bg_2.webp"
    image bg mnd_r_int_bg_3 = "gesmemories/image/logo/mnd_r_int_bg_3.webp"
    image mnd_r_tv_log = "gesmemories/image/logo/mnd_r_tv_log.webp"
    image blood = "gesmemories/image/logo/blood.webp"
    image mnd_flower_fp = "gesmemories/image/logo/mnd_flower_fp.webp"
    image mnd_flower_fw = "gesmemories/image/logo/mnd_flower_fw.webp"
    image mndrainaspd_fp = "gesmemories/image/logo/mndrainaspd_fp.webp"
    image mndrainaspd_s1 = "gesmemories/image/logo/mndrainaspd_s1.webp"
    image mndrainaspd_s2 = "gesmemories/image/logo/mndrainaspd_s2.webp"
    image medpalat_fw = "gesmemories/image/logo/medpalat_fw.webp"
    image medpalat_fp = "gesmemories/image/logo/medpalat_fp.webp"



    image psyapaty = "gesmemories/image/status/psyapaty.webp"
    image psybad = "gesmemories/image/status/psybad.webp"
    image psycrit = "gesmemories/image/status/psycrit.webp"
    image psygood = "gesmemories/image/status/psygood.webp"
    image psynorm = "gesmemories/image/status/psynorm.webp"
    image psystress = "gesmemories/image/status/psystress.webp"
    image mndnesr = "gesmemories/image/status/mndnesr.webp"



    image bg 1car = "gesmemories/image/scene/1car.webp"
    image bg 2car = "gesmemories/image/scene/2car.webp"
    image bg 3car = "gesmemories/image/scene/3car.webp"
    image bg 4car = "gesmemories/image/scene/4car.webp"
    image bg cutters = "gesmemories/image/scene/cutters.webp"
    image bg filindream1 = "gesmemories/image/scene/filindream1.webp"
    image bg liyahartsdance = "gesmemories/image/scene/liyahartsdance.webp"
    image bg lmhit = "gesmemories/image/scene/lmhit.webp"
    image bg mndliyadead = "gesmemories/image/scene/mndliyadead.webp"
    image bg swoosh1 = "gesmemories/image/scene/swoosh1.webp"
    image bg zihaologo = "gesmemories/image/scene/zihaologo.webp"
    image kuklanote1 = "gesmemories/image/scene/kuklanote1.webp"
    image kuklanote2 = "gesmemories/image/scene/kuklanote2.webp"
    image kuklanote3 = "gesmemories/image/scene/kuklanote3.webp"
    image kuklanote4 = "gesmemories/image/scene/kuklanote4.webp"
    image kuklanote5 = "gesmemories/image/scene/kuklanote5.webp"
    image kuklanote6 = "gesmemories/image/scene/kuklanote6.webp"
    image kuklanote7 = "gesmemories/image/scene/kuklanote7.webp"
    image kuklanote8 = "gesmemories/image/scene/kuklanote8.webp"
    image kuklanote9 = "gesmemories/image/scene/kuklanote9.webp"
    image kuklanote10 = "gesmemories/image/scene/kuklanote10.webp"
    image kuklanote11 = "gesmemories/image/scene/kuklanote11.webp"
    image bg mndseabg = "gesmemories/image/scene/mndseabg.webp"
    image bg mndbulpsy = "gesmemories/image/scene/mndbulpsy.webp"
    image bg mnderdie = "gesmemories/image/scene/mnderdie.webp"
    image bg mndlisapsych1 = "gesmemories/image/scene/mndlisapsych1.webp"
    image bg mndhimerapsych1 = "gesmemories/image/scene/mndhimerapsych1.webp"
    image bg takanpsych1 = "gesmemories/image/scene/takanpsych1.webp"
    image bg mndtenkilleretic = "gesmemories/image/scene/mndtenkilleretic.webp"
    image bg kuklapsych1 = "gesmemories/image/scene/kuklapsych1.webp"
    image bg raise1 = "gesmemories/image/scene/raise1.webp"
    image bg raise2 = "gesmemories/image/scene/raise2.webp"
    image bg mndtenfa = "gesmemories/image/scene/mndtenfa.webp"
    image bg mndtenfa = "gesmemories/image/scene/mndtenfa.webp"
    image bg mndtensavecrow1 = "gesmemories/image/scene/mndtensavecrow1.webp"
    image bg mndmatwolf1 = "gesmemories/image/scene/mndmatwolf1.webp"
    image bg mndmatwolf2 = "gesmemories/image/scene/mndmatwolf2.webp"
    image bg mndmatwolf3 = "gesmemories/image/scene/mndmatwolf3.webp"
    image bg mndbloodforest = "gesmemories/image/scene/mndbloodforest.webp"
    image bg mndtenpsycg2 = "gesmemories/image/scene/mndtenpsycg2.webp"
    image bg mndtenpsycg3 = "gesmemories/image/scene/mndtenpsycg3.webp"
    image bg mndtenpsycg4 = "gesmemories/image/scene/mndtenpsycg4.webp"
    image bg mndtenfindcops = "gesmemories/image/scene/mndtenfindcops.webp"
    image bg mndkidsablock = "gesmemories/image/scene/mndkidsablock.webp"
    image bg mndslavya = "gesmemories/image/scene/mndslavya.webp"
    image bg mndteninpitroom = "gesmemories/image/scene/mndteninpitroom.webp"
    image bg mndoldsmertcg = "gesmemories/image/scene/mndoldsmertcg.webp"
    image bg mndvaskisshim = "gesmemories/image/scene/mndvaskisshim.webp"
    image bg mndvkh1 = "gesmemories/image/scene/mndvkh1.webp"
    image bg mndvkh2 = "gesmemories/image/scene/mndvkh2.webp"
    image bg mndatf = "gesmemories/image/scene/mndatf.webp"
    image bg mndfightcor = "gesmemories/image/scene/mndfightcor.webp"
    image bg mndarroofside = "gesmemories/image/scene/mndarroofside.webp"
    image bg mndliyainsvete = "gesmemories/image/scene/mndliyainsvete.webp"
    image bg mndbookbg1 = "gesmemories/image/scene/mndbookbg1.webp"
    image bg mndact1finalbg = "gesmemories/image/scene/mndact1finalbg.webp"
    image bg mndliyam1 = "gesmemories/image/scene/mndliyam1.webp"
    image bg mndvasandhimsmoke = "gesmemories/image/scene/mndvasandhimsmoke.webp"
    image bg mndhimeradie = "gesmemories/image/scene/mndhimeradie.webp"
    image bg mnd_kiss_night = "gesmemories/image/scene/mnd_kiss_night.webp"
    image bg mnd_liya_dead_ring = "gesmemories/image/scene/mnd_liya_dead_ring.webp"
    image bg mnd_arahna_bed_1 = "gesmemories/image/scene/mnd_arahna_bed_1.webp"
    image bg mnd_arahna_bed_2 = "gesmemories/image/scene/mnd_arahna_bed_2.webp"
    image mnd_hit_wall_1 = "gesmemories/image/scene/mnd_hit_wall_1.webp"
    image mnd_hit_wall_2 = "gesmemories/image/scene/mnd_hit_wall_2.webp"
    image bg mnd_arahna_final_scene = "gesmemories/image/scene/mnd_arahna_final_scene.webp"
    image bg mnd_ch11_bed_scene = "gesmemories/image/scene/mnd_ch11_bed_scene.webp"
    image mnd_aom_wood_1 = "gesmemories/image/scene/mnd_aom_wood_1.webp"
    image mnd_aom_wood_2 = "gesmemories/image/scene/mnd_aom_wood_2.webp"
    image mnd_aom_wood_3 = "gesmemories/image/scene/mnd_aom_wood_3.webp"
    image mnd_ch6_hp = "gesmemories/image/scene/mnd_ch6_hp.webp"


    image brod = "gesmemories/image/spr/ofther/brod.webp"
    image ptms = "gesmemories/image/spr/ofther/ptms.webp"
    image ptmn = "gesmemories/image/spr/ofther/ptmn.webp"
    image dart = "gesmemories/image/spr/ofther/dart.webp"
    image mnd_bul_real_1 = "gesmemories/image/spr/ofther/mnd_bul_real_1.webp"
    image mnd_bul_real_2 = "gesmemories/image/spr/ofther/mnd_bul_real_2.webp"
    image mnd_16_sec_spr = "gesmemories/image/spr/ofther/mnd_16_sec_spr.webp"
    image mnd_ks_med_n = "gesmemories/image/spr/ofther/mnd_ks_med_n.webp"
    image mnd_ks_med_s = "gesmemories/image/spr/ofther/mnd_ks_med_s.webp"
    image mnd_ks_med_se = "gesmemories/image/spr/ofther/mnd_ks_med_se.webp"

    image mnddenn = "gesmemories/image/spr/den/mnddenn.webp"

    image mndoldteach = "gesmemories/image/spr/old/mndoldteach.webp"
    image mndgirlold = "gesmemories/image/spr/old/mndgirlold.webp"
    image mndbled = "gesmemories/image/spr/old/mndbled.webp"
    image mndbledeyes = "gesmemories/image/spr/old/mndbledeyes.webp"
    image mndoldmanold = "gesmemories/image/spr/old/mndoldmanold.webp"
    image mndorela = "gesmemories/image/spr/old/mndorela.webp"
    image mndorels = "gesmemories/image/spr/old/mndorels.webp"
    image mndorelu = "gesmemories/image/spr/old/mndorelu.webp"
    image mndosgirls = "gesmemories/image/spr/old/mndosgirls.webp"
    image mndreshsad = "gesmemories/image/spr/old/mndreshsad.webp"
    image mndzmeyhands = "gesmemories/image/spr/old/mndzmeyhands.webp"
    image mndldmanleroy = "gesmemories/image/spr/old/mndldmanleroy.webp"

    image anc = "gesmemories/image/spr/andr/andrc.webp"
    image ani = "gesmemories/image/spr/andr/andri.webp"
    image ann = "gesmemories/image/spr/andr/andrn.webp"
    image ans = "gesmemories/image/spr/andr/andrs.webp"
    image andri = "gesmemories/image/spr/andr/andri.webp"
    image andrs = "gesmemories/image/spr/andr/andrs.webp"
    image andr_w = "gesmemories/image/spr/andr/andr_w.webp"

    image mndlisanu = "gesmemories/image/spr/lisa/mndlnu.webp"
    image mndlisann = "gesmemories/image/spr/lisa/mndlnn.webp"
    image mndlisanl = "gesmemories/image/spr/lisa/mndlnl.webp"
    image mndlisana = "gesmemories/image/spr/lisa/mndlna.webp"
    image mndlds = "gesmemories/image/spr/lisa/mndlds.webp"


    image xian_g = "gesmemories/image/spr/xian/xian_g.webp"
    image xian_n = "gesmemories/image/spr/xian/xian_n.webp"
    image xian_s = "gesmemories/image/spr/xian/xian_s.webp"
    image xian_t = "gesmemories/image/spr/xian/xian_t.webp"


    image mnd_himori_af = "gesmemories/image/spr/himori/mnd_himori_af.webp"
    image mnd_himori_norm = "gesmemories/image/spr/himori/mnd_himori_norm.webp"
    image mnd_himori_sm = "gesmemories/image/spr/himori/mnd_himori_sm.webp"
    image mnd_himori_st = "gesmemories/image/spr/himori/mnd_himori_st.webp"





    image hia = "gesmemories/image/spr/himera/hia.webp"
    image hia2 = "gesmemories/image/spr/himera/hia2.webp"
    image hin = "gesmemories/image/spr/himera/hin.webp"
    image hin2 = "gesmemories/image/spr/himera/hin2.webp"
    image hip = "gesmemories/image/spr/himera/hip.webp"
    image hip2 = "gesmemories/image/spr/himera/hip2.webp"
    image his = "gesmemories/image/spr/himera/his.webp"
    image his2 = "gesmemories/image/spr/himera/his2.webp"
    image hiu = "gesmemories/image/spr/himera/hiu.webp"
    image hiu2 = "gesmemories/image/spr/himera/hiu2.webp"
    image mndhoh = "gesmemories/image/spr/himera/mndhoh.webp"
    image mndhon = "gesmemories/image/spr/himera/mndhon.webp"
    image mndhos = "gesmemories/image/spr/himera/mndhos.webp"
    image him_p_12_1 = "gesmemories/image/spr/himera/him_p_12_1.webp"
    image him_p_12_2 = "gesmemories/image/spr/himera/him_p_12_2.webp"


    image ggpsy = "gesmemories/image/spr/vas/ggpsy.webp"
    image mnd_vas_psy_joke = "gesmemories/image/spr/vas/mnd_vas_psy_joke.webp"
    image mnd_14_vas_g = "gesmemories/image/spr/vas/mnd_14_vas_g.webp"
    image mnd_c18_psyv_sh = "gesmemories/image/spr/vas/mnd_c18_psyv_sh.webp"

    image mndfish = "gesmemories/image/spr/mental/mndfish.webp"

    image mndkukn = "gesmemories/image/spr/kukla/mndkukn.webp"
    image mndkukpsy = "gesmemories/image/spr/kukla/mndkukpsy.webp"

    image mndera = "gesmemories/image/spr/eretic/mndera.webp"
    image mndern = "gesmemories/image/spr/eretic/mndern.webp"
    image mnders = "gesmemories/image/spr/eretic/mnders.webp"
    image mnderz = "gesmemories/image/spr/eretic/mnderz.webp"





    image bulangr = "gesmemories/image/spr/mental/bulangr.webp"
    image mentalmed = "gesmemories/image/spr/mental/mentalmed.webp"
    image mentalsa = "gesmemories/image/spr/mental/mentalsa.webp"
    image mndzih = "gesmemories/image/spr/mental/mndzih.webp"
    image takan = "gesmemories/image/spr/mental/takan.webp"
    image mndelic = "gesmemories/image/spr/mental/mndelic.webp"

    image smertn = "gesmemories/image/spr/smert/smertn.webp"
    image sdn = "gesmemories/image/spr/smert/sdn.webp"
    image sdkn = "gesmemories/image/spr/smert/sdkn.webp"
    image smertpsy = "gesmemories/image/spr/smert/smertpsy.webp"
    image mndsmertold = "gesmemories/image/spr/smert/mndsmertold.webp"

    image mndten = "gesmemories/image/spr/ten/mndten.webp"
    image tenpsy = "gesmemories/image/spr/ten/tenpsy.webp"

    image yaf = "gesmemories/image/spr/yasher/yaf.webp"
    image yna = "gesmemories/image/spr/yasher/yna.webp"
    image ynl = "gesmemories/image/spr/yasher/ynl.webp"
    image ynn = "gesmemories/image/spr/yasher/ynn.webp"
    image lizardpsy = "gesmemories/image/spr/yasher/lizardpsy.webp"


    image mndliyalove = "gesmemories/image/spr/liya/mndliyalove.webp"
    image mndlnu = "gesmemories/image/spr/liya/mndlnu.webp"
    image mndlhg = "gesmemories/image/spr/liya/mndlhg.webp"
    image mndlhn = "gesmemories/image/spr/liya/mndlhn.webp"
    image mndlho = "gesmemories/image/spr/liya/mndlho.webp"
    image mndlhs = "gesmemories/image/spr/liya/mndlhs.webp"
    image mndlhu = "gesmemories/image/spr/liya/mndlhu.webp"
    image mndliyaghost = "gesmemories/image/spr/liya/mndliyaghost.webp"
    image mndlln = "gesmemories/image/spr/liya/mndlln.webp"
    image mndlls = "gesmemories/image/spr/liya/mndlls.webp"
    image mndllu = "gesmemories/image/spr/liya/mndllu.webp"
    image mndlna = "gesmemories/image/spr/liya/mndlna.webp"
    image mndlnl = "gesmemories/image/spr/liya/mndlnl.webp"
    image mndlnn = "gesmemories/image/spr/liya/mndlnn.webp"
    image mndliyapsy = "gesmemories/image/spr/liya/mndliyapsy.webp"
    image mnd_church_liya_spr = "gesmemories/image/spr/liya/mnd_church_liya_spr.webp"
    image mnd_church_liya_spr2 = "gesmemories/image/spr/liya/mnd_church_liya_spr2.webp"
    image mnd_liya_psy_noise_1 = "gesmemories/image/spr/liya/mnd_liya_psy_noise_1.webp"
    image mnd_liya_psy_noise_2 = "gesmemories/image/spr/liya/mnd_liya_psy_noise_2.webp"
    image mnd_liya_psy_noise_3 = "gesmemories/image/spr/liya/mnd_liya_psy_noise_3.webp"
    image mnd_liya_psy_noise_4 = "gesmemories/image/spr/liya/mnd_liya_psy_noise_4.webp"


    image bg mndfp_nh = "gesmemories/image/nightmare/mndfp_nh.webp"
    image bg mnddeadincor = "gesmemories/image/nightmare/mnddeadincor.webp"
    image mndghost1_1 = "gesmemories/image/nightmare/mndghost1_1.webp"
    image mndghost1_2 = "gesmemories/image/nightmare/mndghost1_2.webp"
    image mndghost1_3 = "gesmemories/image/nightmare/mndghost1_3.webp"
    image mndfp_yh = "gesmemories/image/nightmare/mndfp_yh.webp"
    image bg mndtitscr = "gesmemories/image/nightmare/mndtitscr.webp"
    image mnd_vent_g_1 = "gesmemories/image/nightmare/mnd_vent_g_1.webp"
    image mnd_vent_g_2 = "gesmemories/image/nightmare/mnd_vent_g_2.webp"
    image mnd_vent_g_3 = "gesmemories/image/nightmare/mnd_vent_g_3.webp"

    image mndleroy = "gesmemories/image/spr/old/mndleroy.webp"
    image voronakid = "gesmemories/image/spr/old/voronakid.webp"
    image mndzmey = "gesmemories/image/spr/old/mndzmey.webp"
    image mndkrolchiha = "gesmemories/image/spr/old/mndkrol.webp"
    image mndkrol = "gesmemories/image/spr/old/mndkrol.webp"
    image mndlizghost = "gesmemories/image/spr/old/mndlizghost.webp"

    image vashc = "gesmemories/image/spr/vas/vashc.webp"

    image hivc = "gesmemories/image/spr/himera/hivc.webp"

    image mndsha = "gesmemories/image/spr/mental/mndsha.webp"
    image mndbha = "gesmemories/image/spr/mental/mndbha.webp"
    image mndbulmak = "gesmemories/image/spr/mental/mndbulmak.webp"
    image mndkuks = "gesmemories/image/spr/kukla/mndkuks.webp"
    image mndar1 = "gesmemories/image/spr/arahna/mndar1.webp"
    image mndar2 = "gesmemories/image/spr/arahna/mndar2.webp"
    image mndar3 = "gesmemories/image/spr/arahna/mndar3.webp"
    image mndar4 = "gesmemories/image/spr/arahna/mndar4.webp"
    image mndar5 = "gesmemories/image/spr/arahna/mndar5.webp"
    image mnd_h_ar3 = "gesmemories/image/spr/arahna/mnd_h_ar3.webp"
    image mnd_h_ar4 = "gesmemories/image/spr/arahna/mnd_h_ar4.webp"
    image mnd_ar_dr_far = "gesmemories/image/spr/arahna/mnd_ar_dr_far.webp"
    image mnd_ar_dr_1 = "gesmemories/image/spr/arahna/mnd_ar_dr_1.webp"
    image mnd_ar_dr_2 = "gesmemories/image/spr/arahna/mnd_ar_dr_2.webp"
    image mnd_ar_dr_3 = "gesmemories/image/spr/arahna/mnd_ar_dr_3.webp"
    image mnd_ar_jack_cry_nt = "gesmemories/image/spr/arahna/mnd_ar_jack_cry_nt.webp"
    image mnd_ar_jack_cry_t = "gesmemories/image/spr/arahna/mnd_ar_jack_cry_t.webp"
    image mnd_ar_jack_gr_be = "gesmemories/image/spr/arahna/mnd_ar_jack_gr_be.webp"
    image mnd_ar_jack_gr_bu = "gesmemories/image/spr/arahna/mnd_ar_jack_gr_bu.webp"
    image mnd_ar_jack_h_g = "gesmemories/image/spr/arahna/mnd_ar_jack_h_g.webp"
    image mnd_ar_jack_h_s = "gesmemories/image/spr/arahna/mnd_ar_jack_h_s.webp"
    image mnd_ar_jack_n = "gesmemories/image/spr/arahna/mnd_ar_jack_n.webp"



    image mnd_liya_psy_a2_1 = "gesmemories/image/spr/psy/mnd_liya_psy_a2_1.webp"
    image mnd_liya_psy_a2_2 = "gesmemories/image/spr/psy/mnd_liya_psy_a2_2.webp"
    image mnd_liya_psy_a2_3 = "gesmemories/image/spr/psy/mnd_liya_psy_a2_3.webp"
    image mnd_liya_psy_a2_4 = "gesmemories/image/spr/psy/mnd_liya_psy_a2_4.webp"





    image mnd_luci_n_f_sh = "gesmemories/image/spr/luciena/mnd_luci_n_f_sh.webp"
    image mnd_luci_n_sh = "gesmemories/image/spr/luciena/mnd_luci_n_sh.webp"
    image mnd_luci_n_s = "gesmemories/image/spr/luciena/mnd_luci_n_s.webp"
    image mnd_luci_n_n = "gesmemories/image/spr/luciena/mnd_luci_n_n.webp"
    image mnd_luci_b_sh = "gesmemories/image/spr/luciena/mnd_luci_b_sh.webp"
    image mnd_luci_b_s = "gesmemories/image/spr/luciena/mnd_luci_b_s.webp"
    image mnd_luci_b_n = "gesmemories/image/spr/luciena/mnd_luci_b_n.webp"
    image mnd_luci_dance = "gesmemories/image/spr/luciena/mnd_luci_dance.webp"














    image mndrain_c:
        contains:
            "gesmemories/image/logo/rain.webp"
            xpos 0.5 ypos -1.0
        contains:
            "gesmemories/image/logo/rain.webp"
            xpos -0.5 ypos -1.0
        contains:
            "gesmemories/image/logo/rain.webp"
            xpos 0.5 ypos 0.0
        contains:
            "gesmemories/image/logo/rain.webp"
            xpos -0.5 ypos 0.0
        contains:
            "gesmemories/image/logo/rain.webp"
            xpos 0.5 ypos 1.0
        contains:
            "gesmemories/image/logo/rain.webp"
            xpos -0.5 ypos 1.0
        contains:
             "gesmemories/image/logo/rain.webp"
             xpos 0.5 ypos 2.0
        contains:
             "gesmemories/image/logo/rain.webp"
             xpos -0.5 ypos 2.0
        block:
            yanchor 1.0
            linear 0.3 yanchor 0.0
            repeat

    image mndawaken:
        contains:
            "gesmemories/image/scene/awaken.webp"
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
            "gesmemories/image/logo/mnd_himori_smoke_close_1.webp"
        contains:
            "gesmemories/image/logo/mnd_himori_smoke_close_2.webp"
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
            "gesmemories/image/logo/mndmenu1.webp"
        contains:
            "gesmemories/image/logo/mndmenu2.webp"
            alpha 0.0
            ease 2.5 alpha 1.0
            ease 2.5 alpha 0.0
            repeat


    image menu_mnd2:
        contains:
            "gesmemories/image/logo/mnd_menu2_1.webp"
        contains:
            "gesmemories/image/logo/mnd_menu2_2.webp"
            alpha 0.0
            ease 2.8 alpha 1.0
            ease 2.8 alpha 0.0
            repeat





    image bg mndcutmemos:
        contains:
            "gesmemories/image/scene/cutmemo1.webp"
        contains:
            "gesmemories/image/scene/cutmemo2.webp"
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
            "gesmemories/image/spr/luciena/mnd_luci_dance.webp"
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
            "gesmemories/image/spr/liya/mnd_liya_dance.webp"
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
            "gesmemories/image/spr/liya/mnd_liya_dance.webp"
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
            "gesmemories/image/scene/mnd_harts_1.webp"
        contains:
            "gesmemories/image/scene/mnd_harts_2.webp"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat




    image bg mnd_16_himori_bg:
        contains:
            "gesmemories/image/scene/mnd_16_himori_bg_1.webp"
        contains:
            "gesmemories/image/scene/mnd_16_himori_bg_2.webp"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat



    image mndoldsmertcg_remake:
        contains:
            "gesmemories/image/scene/mndoldsmertcg_1.webp"
        contains:
            "gesmemories/image/scene/mndoldsmertcg_2.webp"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat







    image bg mnd_ch11_bg2:
        contains:
            "gesmemories/image/trymemo/mnd_ch11_bg2_1.webp"
        contains:
            "gesmemories/image/trymemo/mnd_ch11_bg2_2.webp"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat




    image mnd_a3_menu_3:
        contains:
            "gesmemories/image/logo/mnd_a3_menu_3_1.webp"
        contains:
            "gesmemories/image/logo/mnd_a3_menu_3_2.webp"
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
            "gesmemories/image/logo/mnd_snow.webp"
            xanchor 0.5 yanchor 0.75 xpos 0.5 ypos 0.5 alpha 0.5
            linear 0.5 xanchor 0.4 yanchor 0.25
            repeat
        contains:
            "gesmemories/image/logo/mnd_snow.webp"
            xanchor 0.6 yanchor 0.75 xpos 0.5 ypos 0.5 zoom 0.9 alpha 0.5
            linear 0.75 xanchor 0.5 yanchor 0.25
            repeat
        contains:
            "gesmemories/image/logo/mnd_snow.webp"
            xanchor 075 yanchor 0.7 xpos 0.5 ypos 0.5 zoom 0.8 alpha 0.5
            linear 1.0 xanchor 0.65 yanchor 0.3
            repeat





    image overlay mnd_memory_back_1:
        contains:
            parallel:
                choice:
                    "gesmemories/image/logo/mnd_o_1.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_2.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_3.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_4.webp"
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
                    "gesmemories/image/logo/mnd_ch6_hp_1.webp"
                choice:
                    "gesmemories/image/logo/mnd_ch6_hp_2.webp"
                choice:
                    "gesmemories/image/logo/mnd_ch6_hp_3.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_4.webp"
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
                    "gesmemories/image/logo/mnd_prologue_1.webp"
                choice:
                    "gesmemories/image/logo/mnd_prologue_2.webp"
                choice:
                    "gesmemories/image/logo/mnd_prologue_3.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_4.webp"
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
                    "gesmemories/image/logo/mnd_o_1.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_2.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_3.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_4.webp"
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
                    "gesmemories/image/logo/mnd_o_1.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_2.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_3.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_4.webp"
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
                    "gesmemories/image/logo/mnd_o_1.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_2.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_3.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_4.webp"
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
                    "gesmemories/image/logo/mnd_o_1.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_2.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_3.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_4.webp"
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
                    "gesmemories/image/logo/mnd_o_1.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_2.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_3.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_4.webp"
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
                    "gesmemories/image/logo/mnd_o_1.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_2.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_3.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_4.webp"
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
                    "gesmemories/image/logo/mnd_o_1.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_2.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_3.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_4.webp"
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
                    "gesmemories/image/logo/mnd_o_1.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_2.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_3.webp"
                choice:
                    "gesmemories/image/logo/mnd_o_4.webp"
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
            "gesmemories/image/logo/mnd_sb_mm_mf_1.webp"
        contains:
            "gesmemories/image/logo/mnd_sb_mm_mf_2.webp"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat



    image bg carride:
        contains:
            "gesmemories/image/bg/carride1.webp"
        contains:
            "gesmemories/image/bg/carride2.webp"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat


    image bg carride1:
        contains:
            "gesmemories/image/bg/carride1_1.webp"
        contains:
            "gesmemories/image/bg/carride1_2.webp"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat

    image carride1_fw:
        contains:
            "gesmemories/image/bg/carride1_fw_1.webp"
        contains:
            "gesmemories/image/bg/carride1_fw_2.webp"
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
        ground "gesmemories/image/logo/mnd_menu1sh_n.webp" 
        hover  "gesmemories/image/logo/mnd_menu1sh_y.webp"  
        alpha True

        hotspot (0, 305, 494, 103) clicked[Play("gesmemories/snd/sfx/mndstart.ogg"),Jump("gesmnds")] hovered[Play(mndroll)]
        hotspot (0,781, 344, 78) clicked[Play("gesmemories/snd/sfx/mdnquit.ogg"),Quit(confirm=True)] hovered[Play(mndroll)]



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
        ground "gesmemories/image/logo/mhoff.webp" 
        hover  "gesmemories/image/logo/mhon.webp"  
        alpha True

        hotspot (42, 100, 482, 425) clicked[Play("gesmemories/snd/sfx/mndstart.ogg"),Jump("gesmnds")] hovered[Play(mndroll)]
        hotspot (1442, 320, 1920, 648) clicked[Play("gesmemories/snd/psy/mndpsyeff1.ogg"),Jump("gesmndchsel1")] hovered[Play(mndroll)]
        hotspot (46,525,463,722) clicked[Play("gesmemories/snd/sfx/mdnquit.ogg"),Quit(confirm=True)] hovered[Play(mndroll)]


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
        ground "gesmemories/image/logo/mnd_act_nh.webp" 
        hover  "gesmemories/image/logo/mnd_act_yh.webp"  
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
        ground "gesmemories/image/logo/mnd_act_nh.webp" 
        hover  "gesmemories/image/logo/mnd_act_yh.webp"  
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
        ground "gesmemories/image/logo/mnd_chs2_nh.webp" 
        hover  "gesmemories/image/logo/mnd_chs2_yh.webp"  
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
        ground "gesmemories/image/logo/mnd_chs_nh.webp" 
        hover  "gesmemories/image/logo/mnd_chs_yh.webp"  
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
        ground "gesmemories/image/logo/mnd_chs2_nh.webp" 
        hover  "gesmemories/image/logo/mnd_chs2_yh.webp"  
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
        ground "gesmemories/image/logo/mnd_chs3_nh.webp" 
        hover  "gesmemories/image/logo/mnd_chs3_yh.webp"  
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
        ground "gesmemories/image/logo/mnd_chs4_nh.webp" 
        hover  "gesmemories/image/logo/mnd_chs4_yh.webp"  
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
        ground "gesmemories/image/logo/mnd_chs_nh.webp" 
        hover  "gesmemories/image/logo/mnd_chs_yh.webp"  
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
        ground "gesmemories/image/logo/mnd_menu2h_n.webp" 
        hover  "gesmemories/image/logo/mnd_menu2h_y.webp"  
        alpha True

        hotspot (0, 305, 494, 103) clicked[Play("gesmemories/snd/sfx/mndstart.ogg"),Jump("gesmnds")] hovered[Play(mndroll)]
        hotspot (0, 545, 432, 89) clicked[Play("gesmemories/snd/psy/mndpsyeff1.ogg"),Jump("gesmndactsel")] hovered[Play(mndroll)]
        hotspot (0,781, 344, 78) clicked[Play("gesmemories/snd/sfx/mdnquit.ogg"),Quit(confirm=True)] hovered[Play(mndroll)]




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
        ground "gesmemories/image/logo/mnd_menu_r_h_n.webp" 
        hover  "gesmemories/image/logo/mnd_menu_r_h_y.webp"  
        alpha True

        hotspot (0, 343, 486, 103) clicked[Jump("gesmnds")]
        hotspot (0, 492, 432, 89) action ShowMenu ("load")
        hotspot (0,639, 344, 90) clicked[Quit(confirm=True)]
        hotspot (0,799, 392, 117) action ShowMenu ("preferences")




