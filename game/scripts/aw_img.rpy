init:



    $ style.mnd_paratext_liya = Style(style.default)
    $ style.mnd_paratext_liya.color = "#FF7C00"
    $ style.mnd_paratext_liya.xalign = 0.5
    $ style.mnd_paratext_liya.yalign = 0.5
    $ style.mnd_paratext_liya.font = "gesmemories/fnt/beer money.ttf"
    $ style.mnd_paratext_liya.italic = False
    $ style.mnd_paratext_liya.bold = False


    define dis = Dissolve(0.5, alpha=True)
    $ flash = Fade(1, 0, 1, color="#fff")
    $ flash2 = Fade(2, 2, 2, color="#fff")
    $ flash_red = Fade(1, 0, 1, color="#e11")
    $ flash_red2 = Fade(2, 2, 2, color="#e11")
    $ flash_fast = Fade(0.25, 0, 0.75, color="#fff")
    $ flash_fast2 = Fade(0.05, 0, 0.35, color="#fff")
    $ flash_fast_red = Fade(0.25, 0, 0.75, color="#ff0000")
    $ flash_fast_red2 = Fade(0.05, 0, 0.75, color="#ff0000")
    $ fade3 = Fade(1.5, 0, 1.5)
    $ fade2 = Fade(1, 0, 1)
    $ hell_dissolve = Dissolve(50)
    $ dissolve2 = Dissolve(2)
    $ dissolve3 = Dissolve(3)
    $ dissolve4 = Dissolve(4)
    $ dissolve_fast = Dissolve(0.5)
    $ dissolve_long = Dissolve(100)
    $ dspr = Dissolve(.2)
    $ dissolve4 = Dissolve(4)
    $ awrain = ImageDissolve("away/img/eff/awrain.png", 1.5, 60, reverse=False)
    $ awrain2 = ImageDissolve("away/img/eff/awrain.png", 4.5, 80, reverse=False)
    $ awrain3 = ImageDissolve("away/img/eff/awrain.png", 0.5, 30, reverse=False)
    $ awwhole = ImageDissolve("away/img/eff/awwhole.png", 4.5, 60, reverse=False)
    $ awbhole = ImageDissolve("away/img/eff/awbhole.png", 3.5, 60, reverse=True)
    $ awmad = ImageDissolve("away/img/eff/awmad.png", 3.0, 75, reverse=False)
    $ awspot = ImageDissolve("away/img/eff/aw_eff_spot.png", 3.5, 60, reverse=True)
    $ awspot2 = ImageDissolve("away/img/eff/aw_eff_spot.png", 3.5, 60, reverse=False)
    $ awnoose = ImageDissolve("away/img/eff/aw_noose.png", 3.5, 60, reverse=True)


    #CHAR
    $ aw_j1 = Character(u'Женщина', color="#666666", what_color="E2C778",)
    $ aw_j2 = Character(u'Женщина', color="#a0899c", what_color="E2C778",)
    $ aw_j3 = Character(u'Женщина', color="#c8a6c4", what_color="E2C778",)
    $ aw_doc_h = Character(u'Доктор', color="#666666", what_color="E2C778",)
    $ aw_gg_hide = Character(u'...', color="#666666", what_color="E2C778",)
    $ aw_dad = Character(u'Папа', color="#2e3953", what_color="E2C778",)
    $ aw_mom = Character(u'Мама', color="#2e533f", what_color="E2C778",)
    $ aw_voice = Character(u'Голос', color="#7a7d8d", what_color="E2C778",)
    $ aw_sanit = Character(u'Санитар', color="#7a7d8d", what_color="E2C778",)
    $ aw_lili = Character(u'Лиллиян', color="#d26c44", what_color="E2C778",)
    $ aw_nikit = Character(u'Никита', color="#5867b0", what_color="E2C778",)
    $ aw_olu4i = Character(u'Олучи', color="#9e7457", what_color="E2C778",)
    $ aw_d1 = Character(u'Девушка', color="#ada6b6", what_color="E2C778",)
    $ aw_d2 = Character(u'Девушка', color="#92a4b1", what_color="E2C778",)
    $ aw_d3 = Character(u'Девушка', color="#8ab88f", what_color="E2C778",)
    $ aw_d4 = Character(u'Девушка', color="#7a956d", what_color="E2C778",)
    $ aw_d5 = Character(u'Девушка', color="#b8b273", what_color="E2C778",)
    $ aw_d6 = Character(u'Девушка', color="#d9a583", what_color="E2C778",)
    $ aw_mch = Character(u'Опекунша', color="#c8a6c4", what_color="E2C778",)
    $ aw_mj1 = Character(u'Мужчина', color="#bb8282", what_color="E2C778",)
    $ aw_mj2 = Character(u'Мужчина', color="#c2b466", what_color="E2C778",)
    $ aw_hi = Character(u'Химори', color="#CB94F0", what_color="E2C778",)
    $ aw_mjl = Character(u'Мужчина', color="#2e3953", what_color="E2C778",)
    $ aw_mmom = Character(u'Мама', color="#c8a6c4", what_color="E2C778",)
    $ aw_p1 = Character(u'Одноклассник', color="#ada6b6", what_color="E2C778",)
    $ aw_mj3 = Character(u'Мужчина', color="#a48f5d", what_color="E2C778",)
    $ aw_kat = Character(u'Катя', color="#ada6b6", what_color="E2C778",)
    $ aw_messag = Character(u'Сообщение', color="#666666", what_color="E2C778",)
    $ aw_madlen = Character(u'Маделин', color="#83e3d4", what_color="E2C778",)
    $ aw_locdoc = Character(u'Доктор', color="#7ec1bb", what_color="E2C778",)
    $ aw_opk = Character(u'Опекун', color="#997171", what_color="E2C778",)



    $ aw_gg_hide_kmpr = Character(u'...', color="#666666", what_color="E2C778", what_prefix="{font=away/fnt/away_km_mes.otf}", what_suffix="{/font}")

    image aw_mm_bg_v = Movie(play="away/img/eff/aw_mm_bg_v.ogv", channel="movie", size=(1920, 1080))
    image aw_rain_road_1 = Movie(play="away/img/eff/aw_rain_road_1.ogv", channel="movie", size=(1920, 1080))
    image aw_rain_road_2 = Movie(play="away/img/eff/aw_rain_road_2.ogv", channel="movie", size=(1920, 1080))
    image aw_rain_road_3 = Movie(play="away/img/eff/aw_rain_road_3.ogv", channel="movie", size=(1920, 1080))
    image aw_rain_road_4 = Movie(play="away/img/eff/aw_rain_road_4.ogv", channel="movie", size=(1920, 1080))
    image aw_rain_road_5 = Movie(play="away/img/eff/aw_rain_road_5.ogv", channel="movie", size=(1920, 1080))
    image aw_rain_road_6 = Movie(play="away/img/eff/aw_rain_road_6.ogv", channel="movie", size=(1920, 1080))
    image aw_rain_road_7 = Movie(play="away/img/eff/aw_rain_road_7.ogv", channel="movie", size=(1920, 1080))

    image aw_bad_ending = Movie(play="away/img/eff/aw_bad_ending.ogv", channel="movie", size=(1920, 1080))
    image aw_good_ending = Movie(play="away/img/eff/aw_good_ending.ogv", channel="movie", size=(1920, 1080))
    image aw_true_ending = Movie(play="away/img/eff/aw_true_ending.ogv", channel="movie", size=(1920, 1080))

    image aw_bad_end = Movie(play="away/img/eff/aw_bad_end.ogv", channel="movie", size=(1920, 1080))

    image aw_tv_v1 = Movie(play="away/img/eff/aw_tv_v1.ogv", channel="movie", size=(850, 1250))

    #ANI
    image anim blink_down = "away/img/eff/blink_down.png"
    image anim blink_up = "away/img/eff/blink_up.png"

    image unblink:
        contains:
            "anim blink_up" 
            xalign 0yalign 0
            ease 1.5pos (0,-1080)
        contains:
            "anim blink_down" 
            xalign 0yalign 0
            ease 1.5pos (0,1080)

    image blink:
        contains:
            "anim blink_up" 
            pos (0,-1080)
            ease 1.5xalign 0yalign 0
        contains:
            "anim blink_down" 
            pos (0,1080)
            ease 1.5xalign 0yalign 0


    image blinking:
        contains:
            "anim blink_up" 
            pos (0,-1080)
            ease 1.5xalign 0yalign 0
        contains:
            "anim blink_down" 
            pos (0,1080)
            ease 1.5xalign 0yalign 0
        pause 2.0
        contains:
            "anim blink_up" 
            xalign 0yalign 0
            ease 1.5pos (0,-1080)
        contains:
            "anim blink_down" 
            xalign 0yalign 0
            ease 1.5pos (0,1080)





    #Свет
    image aw_light:
        contains:
            "away/img/eff/aw_light_eff.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 0
            linear 120 rotate 360
            repeat
        contains:
            "away/img/eff/aw_light_eff.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 180
            linear 150 rotate -180
            repeat
        contains:
            "away/img/eff/aw_light_eff.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 90
            linear 180 rotate 450
            repeat
        contains:
            "away/img/eff/aw_light_eff.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate -90
            linear 210 rotate -450
            repeat
        contains:
            "away/img/eff/aw_light_eff.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 45
            linear 240 rotate 405
            repeat
        contains:
            "away/img/eff/aw_light_eff.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate -45
            linear 270 rotate -405
            repeat

    image aw_light_red:
        contains:
            "away/img/eff/aw_light_eff_red.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 0
            linear 120 rotate 360
            repeat
        contains:
            "away/img/eff/aw_light_eff_red.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 180
            linear 150 rotate -180
            repeat
        contains:
            "away/img/eff/aw_light_eff_red.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 90
            linear 180 rotate 450
            repeat
        contains:
            "away/img/eff/aw_light_eff_red.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate -90
            linear 210 rotate -450
            repeat
        contains:
            "away/img/eff/aw_light_eff_red.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 45
            linear 240 rotate 405
            repeat
        contains:
            "away/img/eff/aw_light_eff_red.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate -45
            linear 270 rotate -405
            repeat


    #Rain
    image awrain_c:
        contains:
            "away/img/eff/rain.png"
            xpos 0.5 ypos -1.0
        contains:
            "away/img/eff/rain.png"
            xpos -0.5 ypos -1.0
        contains:
            "away/img/eff/rain.png"
            xpos 0.5 ypos 0.0
        contains:
            "away/img/eff/rain.png"
            xpos -0.5 ypos 0.0
        contains:
            "away/img/eff/rain.png"
            xpos 0.5 ypos 1.0
        contains:
            "away/img/eff/rain.png"
            xpos -0.5 ypos 1.0
        contains:
             "away/img/eff/rain.png"
             xpos 0.5 ypos 2.0
        contains:
             "away/img/eff/rain.png"
             xpos -0.5 ypos 2.0
        block:
            yanchor 1.0
            linear 0.3 yanchor 0.0
            repeat

    image awrain_l:
        contains:
            "awrain_c"
            rotate 10

    image awrain_r:
        contains:
            "awrain_c"
            rotate -10

    image awrain2_c:
        contains:
            "awrain_c"
        contains:
            "awrain_c"
            zoom 0.75

    image awrain2_l:
        contains:
            "awrain2_c"
            rotate 10

    image awrain2_r:
        contains:
            "awrain2_c"
            rotate -10


    #TRANSFORM

    $ bg_dissolve = ImageDissolve("away/img/eff/dissolve.jpg", 1, 32)
    $ bg_dissolve2 = ImageDissolve("away/img/eff/dissolve2.jpg", 15, 32)

    transform rain_on_face(bg1, bg2):
        bg2 with bg_dissolve2
        pause 15
    transform rain_on_face2(bg1, bg2):
        bg2
        pause 1
        bg1 with bg_dissolve
        pause 1
        rain_on_face(bg1, bg2)

    transform aw_master_tryas:
        xalign 0.5 yalign 0.5
        parallel:
            ease 0.25 zoom 1.1
            ease 0.5 zoom 1.0
        parallel:
            ease 0.25 rotate -1.5
            ease 0.25 rotate 1.0
            ease 0.25 rotate 0.0


    transform aw_center_zoom:
        ease 3.9 zoom 3 xpos -0.8 ypos -0.5

    transform aw_sprite_zoom(z=1, yp=1.0, time=0.25, alp=1.0):
        xanchor 0.5 yanchor 1.0 alpha alp
        ease time zoom z ypos yp


    transform aw_dance_2:
        parallel:
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            ease 0.6 zoom 1.04 xpos 0.5 ypos 0.49
        parallel:
            ease 0.6 xpos 0.5 ypos 0.49
            ease 0.6 xpos 0.48 ypos 0.51
            ease 0.6 xpos 0.5 ypos 0.49
            ease 0.6 xpos 0.52 ypos 0.51
            repeat


    image aw_df_a:
        contains:
            choice:
                "aw_df_a_1"
            choice:
                "aw_df_a_2"
            choice:
                "aw_df_a_3"
            choice:
                "aw_df_a_4"
            pause 0.05
            repeat
        contains:
            choice:
                "aw_df_a_1"
            choice:
                "aw_df_a_2"
            choice:
                "aw_df_a_3"
            choice:
                "aw_df_a_4"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "aw_df_a_1"
            choice:
                "aw_df_a_2"
            choice:
                "aw_df_a_3"
            choice:
                "aw_df_a_4"
            alpha 0.25
            pause 0.05
            repeat


    image aw_sch_p_a:
        contains:
            choice:
                "aw_sch_p_a_1"
            choice:
                "aw_sch_p_a_2"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_sch_p_a_1"
            choice:
                "aw_sch_p_a_2"
            alpha 0.25
            pause 0.15
            repeat
        contains:
            choice:
                "aw_sch_p_a_1"
            choice:
                "aw_sch_p_a_2"
            alpha 0.25
            pause 0.15
            repeat


    image aw_mmn:
        contains:
            choice:
                "aw_mmn_1"
            choice:
                "aw_mmn_2"
            choice:
                "aw_mmn_3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_mmn_1"
            choice:
                "aw_mmn_2"
            choice:
                "aw_mmn_3"
            alpha 0.25
            pause 0.15
            repeat
        contains:
            choice:
                "aw_mmn_1"
            choice:
                "aw_mmn_2"
            choice:
                "aw_mmn_3"
            alpha 0.25
            pause 0.15
            repeat


    image aw_eff_spot:
        contains:
            choice:
                "aw_eff_spot_1"
            choice:
                "aw_eff_spot_2"
            choice:
                "aw_eff_spot_3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_eff_spot_1"
            choice:
                "aw_eff_spot_2"
            choice:
                "aw_eff_spot_3"
            alpha 0.25
            pause 0.15
            repeat
        contains:
            choice:
                "aw_eff_spot_1"
            choice:
                "aw_eff_spot_2"
            choice:
                "aw_eff_spot_3"
            alpha 0.25
            pause 0.15
            repeat


    image aw_kn_bear:
        contains:
            choice:
                "aw_kn_bear_p1"
            choice:
                "aw_kn_bear_p2"
            choice:
                "aw_kn_bear_p3"
            choice:
                "aw_kn_bear_p4"
            pause 0.35
            repeat
        contains:
            choice:
                "aw_kn_bear_p1"
            choice:
                "aw_kn_bear_p2"
            choice:
                "aw_kn_bear_p3"
            choice:
                "aw_kn_bear_p4"
            alpha 0.0
            pause 0.35
            repeat
        contains:
            choice:
                "aw_kn_bear_p1"
            choice:
                "aw_kn_bear_p2"
            choice:
                "aw_kn_bear_p3"
            choice:
                "aw_kn_bear_p4"
            alpha 0.0
            pause 0.35
            repeat


    image aw_p2_an:
        contains:
            choice:
                "aw_p2_an_1"
            choice:
                "aw_p2_an_2"
            choice:
                "aw_p2_an_3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_p2_an_1"
            choice:
                "aw_p2_an_2"
            choice:
                "aw_p2_an_3"
            alpha 0.25
            pause 0.15
            repeat
        contains:
            choice:
                "aw_p2_an_1"
            choice:
                "aw_p2_an_2"
            choice:
                "aw_p2_an_3"
            alpha 0.25
            pause 0.15
            repeat

    image aw_p2_ap:
        contains:
            choice:
                "aw_p2_ap_1"
            choice:
                "aw_p2_ap_2"
            choice:
                "aw_p2_ap_3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_p2_ap_1"
            choice:
                "aw_p2_ap_2"
            choice:
                "aw_p2_ap_3"
            alpha 0.25
            pause 0.15
            repeat
        contains:
            choice:
                "aw_p2_ap_1"
            choice:
                "aw_p2_ap_2"
            choice:
                "aw_p2_ap_3"
            alpha 0.25
            pause 0.15
            repeat

    image aw_p2_dt:
        contains:
            choice:
                "aw_p2_dt_1"
            choice:
                "aw_p2_dt_2"
            choice:
                "aw_p2_dt_3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_p2_dt_1"
            choice:
                "aw_p2_dt_2"
            choice:
                "aw_p2_dt_3"
            alpha 0.25
            pause 0.15
            repeat
        contains:
            choice:
                "aw_p2_dt_1"
            choice:
                "aw_p2_dt_2"
            choice:
                "aw_p2_dt_3"
            alpha 0.25
            pause 0.15
            repeat

    image aw_p2_li:
        contains:
            choice:
                "aw_p2_li_1"
            choice:
                "aw_p2_li_2"
            choice:
                "aw_p2_li_3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_p2_li_1"
            choice:
                "aw_p2_li_2"
            choice:
                "aw_p2_li_3"
            alpha 0.25
            pause 0.15
            repeat
        contains:
            choice:
                "aw_p2_li_1"
            choice:
                "aw_p2_li_2"
            choice:
                "aw_p2_li_3"
            alpha 0.25
            pause 0.15
            repeat

    image aw_p2_prl:
        contains:
            choice:
                "aw_p2_prl_1"
            choice:
                "aw_p2_prl_2"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_p2_prl_1"
            choice:
                "aw_p2_prl_2"
            alpha 0.25
            pause 0.15
            repeat
        contains:
            choice:
                "aw_p2_prl_1"
            choice:
                "aw_p2_prl_2"
            alpha 0.25
            pause 0.15
            repeat

    image aw_afd_dth1:
        contains:
            choice:
                "aw_afd_dth1_1"
            choice:
                "aw_afd_dth1_2"
            choice:
                "aw_afd_dth1_3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_afd_dth1_1"
            choice:
                "aw_afd_dth1_2"
            choice:
                "aw_afd_dth1_3"
            alpha 0.45
            pause 0.15
            repeat
        contains:
            choice:
                "aw_afd_dth1_1"
            choice:
                "aw_afd_dth1_2"
            choice:
                "aw_afd_dth1_3"
            alpha 0.45
            pause 0.15
            repeat


    image aw_afd_ky1:
        contains:
            choice:
                "aw_afd_ky1_1"
            choice:
                "aw_afd_ky1_2"
            choice:
                "aw_afd_ky1_3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_afd_ky1_1"
            choice:
                "aw_afd_ky1_2"
            choice:
                "aw_afd_ky1_3"
            alpha 0.45
            pause 0.15
            repeat
        contains:
            choice:
                "aw_afd_ky1_1"
            choice:
                "aw_afd_ky1_2"
            choice:
                "aw_afd_ky1_3"
            alpha 0.45
            pause 0.15
            repeat

    image aw_dam_tv_eff:
        contains:
            choice:
                "aw_dam_tv_eff_1"
            choice:
                "aw_dam_tv_eff_2"
            choice:
                "aw_dam_tv_eff_3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_dam_tv_eff_1"
            choice:
                "aw_dam_tv_eff_2"
            choice:
                "aw_dam_tv_eff_3"
            alpha 0.45
            pause 0.15
            repeat
        contains:
            choice:
                "aw_dam_tv_eff_1"
            choice:
                "aw_dam_tv_eff_2"
            choice:
                "aw_dam_tv_eff_3"
            alpha 0.45
            pause 0.15
            repeat









    transform qte_button_ani:
        parallel:
            choice:
                alpha 1.0
            choice:
                alpha 0.9
            choice:
                alpha 0.8
            choice:
                alpha 0.7
            choice:
                alpha 0.6
            choice:
                alpha 0.5
            choice:
                alpha 0.4
            pause 0.02
            repeat



    transform aw_drinkscreens:
        xalign 0.5 yalign 0.5
        parallel:
            ease 2.0 xpos 0.505
            ease 2.0 xpos 0.4975
            ease 2.0 xpos 0.5025
            ease 2.0 xpos 0.495
            repeat
        parallel:
            ease 1.9 ypos 0.505
            ease 1.9 ypos 0.495
            ease 1.9 ypos 0.5025
            ease 1.9 ypos 0.4975
            repeat
        parallel:
            ease 2.25 rotate -0.75
            ease 2.25 rotate -0.25
            ease 2.25 rotate -0.5
            ease 2.25 rotate 0.5
            ease 2.25 rotate 0.0
            ease 2.25 rotate 0.25
            ease 2.25 rotate 0.7
            repeat
        parallel:
            ease 2.15 zoom 1.01
            ease 2.15 zoom 1.03
            ease 2.15 zoom 1.02
            ease 2.15 zoom 1.05
            ease 2.15 zoom 1.04
            ease 2.15 zoom 1.02
            ease 2.15 zoom 1.03
            ease 2.15 zoom 1.01
            ease 2.15 zoom 1.02
            repeat

    image bg aw_club_f:
        contains:
            choice:
                "aw_club_f1"
            choice:
                "aw_club_f2"
            choice:
                "aw_club_f3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_club_f1"
            choice:
                "aw_club_f2"
            choice:
                "aw_club_f3"
            alpha 0.25
            pause 0.15
            repeat
        contains:
            choice:
                "aw_club_f1"
            choice:
                "aw_club_f2"
            choice:
                "aw_club_f3"
            alpha 0.25
            pause 0.15
            repeat

    image aw_fmind_2:
        contains:
            choice:
                "aw_fmind_2_3"
            choice:
                "aw_fmind_2_2"
            choice:
                "aw_fmind_2_1"
            pause 0.05
            repeat
        contains:
            choice:
                "aw_fmind_2_3"
            choice:
                "aw_fmind_2_2"
            choice:
                "aw_fmind_2_1"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "aw_fmind_2_3"
            choice:
                "aw_fmind_2_2"
            choice:
                "aw_fmind_2_1"
            alpha 0.25
            pause 0.05
            repeat

    image aw_fmind_1:
        contains:
            choice:
                "aw_fmind_1_1"
            choice:
                "aw_fmind_1_2"
            choice:
                "aw_fmind_1_3"
            pause 0.05
            repeat
        contains:
            choice:
                "aw_fmind_1_1"
            choice:
                "aw_fmind_1_2"
            choice:
                "aw_fmind_1_3"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "aw_fmind_1_1"
            choice:
                "aw_fmind_1_2"
            choice:
                "aw_fmind_1_3"
            alpha 0.25
            pause 0.05
            repeat

    image aw_kat_murd:
        contains:
            choice:
                "aw_kat_murd_3"
            choice:
                "aw_kat_murd_2"
            choice:
                "aw_kat_murd_1"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_kat_murd_3"
            choice:
                "aw_kat_murd_2"
            choice:
                "aw_kat_murd_1"
            alpha 0.25
            pause 0.15
            repeat
        contains:
            choice:
                "aw_kat_murd_3"
            choice:
                "aw_kat_murd_2"
            choice:
                "aw_kat_murd_1"
            alpha 0.25
            pause 0.15
            repeat



    #BG_ANIM
    image bg aw_mm_bg1:
        contains:
            "away/img/bg/aw_mm_bg1_1.png"
        contains:
            "away/img/bg/aw_mm_bg1_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat

    image aw_mm_bg1:
        contains:
            "away/img/bg/aw_mm_bg1_1.png"
        contains:
            "away/img/bg/aw_mm_bg1_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat


    image bg aw_r1_match_1:
        contains:
            "away/img/bg/aw_r1_match_1_1.png"
        contains:
            "away/img/bg/aw_r1_match_1_2.png"
            alpha 0.0
            ease 4.6 alpha 1.0
            ease 4.6 alpha 0.0
            repeat



    image bg aw_r1_match_2:
        contains:
            "away/img/bg/aw_r1_match_2_1.png"
        contains:
            "away/img/bg/aw_r1_match_2_2.png"
            alpha 0.0
            ease 4.6 alpha 1.0
            ease 4.6 alpha 0.0
            repeat

    image bg aw_snddis:
        contains:
            "away/img/eff/aw_snddis_1.png"
        contains:
            "away/img/eff/aw_snddis_2.png"
            alpha 0.0
            ease 1.6 alpha 1.0
            ease 1.6 alpha 0.0
            repeat


    image aw_km_balet_l:
        contains:
            "away/img/parts/aw_km_balet_l_1.png"
        contains:
            "away/img/parts/aw_km_balet_l_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat


    image aw_km_kr_fp:
        contains:
            "away/img/parts/aw_km_kr_fp_1.png"
        contains:
            "away/img/parts/aw_km_kr_fp_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat


    image bg aw_km_auqa:
        contains:
            "away/img/parts/aw_km_auqa_1.png"
        contains:
            "away/img/parts/aw_km_auqa_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat


    image bg aw_km_dam_s:
        contains:
            "away/img/parts/aw_km_dam_s_1.png"
        contains:
            "away/img/parts/aw_km_dam_s_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat

    image aw_km_kr_fp:
        contains:
            "away/img/parts/aw_km_kr_fp_1.png"
        contains:
            "away/img/parts/aw_km_kr_fp_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat


    image aw_km_ia:
        contains:
            "away/img/parts/aw_km_ia_1.png"
        contains:
            "away/img/parts/aw_km_ia_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat


    image bg aw_himori_smoke:
        contains:
            "away/img/bg/aw_himori_smoke_1.png"
        contains:
            "away/img/bg/aw_himori_smoke_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat

    image aw_p2_kp:
        contains:
            "away/img/parts/aw_p2_kp_1.png"
        contains:
            "away/img/parts/aw_p2_kp_2.png"
            alpha 0.0
            ease 4.6 alpha 1.0
            ease 4.6 alpha 0.0
            repeat

    image bg aw_lav_n:
        contains:
            "away/img/parts/aw_lav_n_1.png"
        contains:
            "away/img/parts/aw_lav_n_2.png"
            alpha 0.0
            ease 3.6 alpha 1.0
            ease 3.6 alpha 0.0
            repeat


    image bg aw_madeleine_vs_himpri:
        contains:
            "away/img/bg/aw_madeleine_vs_himpri_1.png"
        contains:
            "away/img/bg/aw_madeleine_vs_himpri_2.png"
            alpha 0.0
            ease 2.6 alpha 1.0
            ease 2.6 alpha 0.0
            repeat




    #OVERLAYS
    image overlay aw_pe1:
        contains:
            parallel:
                choice:
                    "away/img/eff/aw_pe1_1.png"
                choice:
                    "away/img/eff/aw_pe1_2.png"
                choice:
                    "away/img/eff/aw_pe1_3.png"
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

    image aw_pe1:
        contains:
            parallel:
                choice:
                    "away/img/eff/aw_pe1_1.png"
                choice:
                    "away/img/eff/aw_pe1_2.png"
                choice:
                    "away/img/eff/aw_pe1_3.png"
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

    image overlay aw_memory_back_1:
        contains:
            parallel:
                choice:
                    "away/img/eff/aw_o_1.png"
                choice:
                    "away/img/eff/aw_o_2.png"
                choice:
                    "away/img/eff/aw_o_3.png"
                choice:
                    "away/img/eff/aw_o_4.png"
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



    image overlay aw_memory_back_2:
        contains:
            parallel:
                choice:
                    "away/img/eff/a_1.png"
                choice:
                    "away/img/eff/a_2.png"
                choice:
                    "away/img/eff/a_3.png"
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


    image aw_memory_back_1_no:
        contains:
            parallel:
                choice:
                    "away/img/eff/aw_o_1.png"
                choice:
                    "away/img/eff/aw_o_2.png"
                choice:
                    "away/img/eff/aw_o_3.png"
                choice:
                    "away/img/eff/aw_o_4.png"
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






    image aw_book_c:
        contains:
            "away/img/parts/aw_r1_book_u.png"
            xpos 0.05 ypos 1.0 xanchor 0.5 yanchor 0.5 rotate 30
            ease 1.5 xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5 rotate 0

    image aw_book_d:
        contains:
            "away/img/parts/aw_r1_book_d.png"
            xpos 0.05 ypos 1.0 xanchor 0.5 yanchor 0.5 rotate 30
            ease 1.5 xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5 rotate 0

    image aw_book_ph:
        contains:
            "away/img/parts/aw_r1_book_m.png"
            xpos 0.05 ypos 1.0 xanchor 0.5 yanchor 0.5 rotate 30
            ease 1.5 xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5 rotate 0

    image aw_diray_r1:
        contains:
            "away/img/parts/aw_r1_diray.png"
            xpos 0.05 ypos 1.0 xanchor 0.5 yanchor 0.5 rotate 30
            ease 1.5 xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5 rotate 0




    #IMG

    #BG
    image bg aw_ges_logo_bg = "away/img/bg/aw_ges_logo_bg.png"
    image aw_ges_logo_fp = "away/img/bg/aw_ges_logo_fp.png"
    image aw_df_1 = "away/img/bg/aw_df_1.png"
    image bg aw_df_2 = "away/img/bg/aw_df_2.png"
    image bg aw_sch_p_bg = "away/img/bg/aw_sch_p_bg.png"
    image bg aw_kms_s = "away/img/bg/aw_kms_s.png"
    image aw_kms_1 = "away/img/bg/aw_kms_1.png"
    image aw_kms_2 = "away/img/bg/aw_kms_2.png"
    image aw_kms_3 = "away/img/bg/aw_kms_3.png"
    image aw_kms_4 = "away/img/bg/aw_kms_4.png"
    image aw_kms_5 = "away/img/bg/aw_kms_5.png"
    image aw_kms_6 = "away/img/bg/aw_kms_6.png"
    image aw_kms_f = "away/img/bg/aw_kms_f.png"
    image aw_kms_fb = "away/img/bg/aw_kms_fb.png"
    image bg aw_bg = "away/img/bg/aw_bg.png"
    image bg aw_himori_bg_1 = "away/img/bg/aw_himori_bg_1.png"
    image bg aw_yellow_jacket_bg1 = "away/img/bg/aw_yellow_jacket_bg1.png"
    image bg aw_r1_bg = "away/img/bg/aw_r1_bg.png"
    image bg aw_r2_bg = "away/img/bg/aw_r2_bg.png"
    image bg aw_r1_match_end = "away/img/bg/aw_r1_match_end.png"
    image bg aw_r1_bg_tv = "away/img/bg/aw_r1_bg_tv.png"
    image bg aw_pr_pod = "away/img/bg/aw_pr_pod.png"
    image bg aw_r2_l_bg = "away/img/bg/aw_r2_l_bg.png"
    image bg aw_r1_bg_l = "away/img/bg/aw_r1_bg_l.png"
    image bg aw_r1_bg_ltv = "away/img/bg/aw_r1_bg_ltv.png"
    image bg aw_r2_l_bg = "away/img/bg/aw_r2_l_bg.png"
    image bg aw_warn_bg = "away/img/bg/aw_warn_bg.png"
    image bg aw_r_int_bg_1 = "away/img/bg/aw_r_int_bg_1.png"
    image bg aw_r_int_bg_2 = "away/img/bg/aw_r_int_bg_2.png"
    image bg aw_r_int_bg_3 = "away/img/bg/aw_r_int_bg_3.png"
    image bg aw_km_bal_m = "away/img/bg/aw_km_bal_m.png"
    image bg aw_km_dadr_bg = "away/img/bg/aw_km_dadr_bg.png"
    image bg aw_km_kor = "away/img/bg/aw_km_kor.png"
    image bg aw_km_kr_bg = "away/img/bg/aw_km_kr_bg.png"
    image bg aw_km_kr_bg_nl = "away/img/bg/aw_km_kr_bg_nl.png"
    image bg aw_km_mr_psy = "away/img/bg/aw_km_mr_psy.png"
    image bg aw_km_mroom_bg1 = "away/img/bg/aw_km_mroom_bg1.png"
    image bg aw_km_mroom_bg2 = "away/img/bg/aw_km_mroom_bg2.png"
    image bg aw_km_mroom_opd_bg = "away/img/bg/aw_km_mroom_opd_bg.png"
    image bg aw_km_wom_bm = "away/img/bg/aw_km_wom_bm.png"
    image bg aw_mad_cut_bed = "away/img/bg/aw_mad_cut_bed.png"
    image bg aw_lili_kid_1 = "away/img/bg/aw_lili_kid_1.png"
    image bg aw_v_cut_1 = "away/img/bg/aw_v_cut_1.png"
    image bg aw_v_cut_2 = "away/img/bg/aw_v_cut_2.png"
    image bg aw_v_cut_3 = "away/img/bg/aw_v_cut_3.png"
    image bg aw_v_cut_4 = "away/img/bg/aw_v_cut_4.png"
    image bg aw_km_mondead_1 = "away/img/bg/aw_km_mondead_1.png"
    image bg aw_km_mondead_2 = "away/img/bg/aw_km_mondead_2.png"
    image bg aw_km_mondead_3 = "away/img/bg/aw_km_mondead_3.png"
    image bg aw_km_mondead_4 = "away/img/bg/aw_km_mondead_4.png"
    image bg aw_km_mondead_5 = "away/img/bg/aw_km_mondead_5.png"
    image bg aw_hi_cab = "away/img/bg/aw_hi_cab.png"
    image bg aw_clas_room = "away/img/bg/aw_clas_room.png"
    image bg aw_cut_urslf_1 = "away/img/bg/aw_cut_urslf_1.png"
    image bg aw_cut_urslf_2 = "away/img/bg/aw_cut_urslf_2.png"
    image bg aw_himori_bg_2 = "away/img/bg/aw_himori_bg_2.png"
    image bg aw_himori_bg_3 = "away/img/bg/aw_himori_bg_3.png"
    image bg aw_lavka_m = "away/img/bg/aw_lavka_m.png"
    image bg aw_lilian_mirror = "away/img/bg/aw_lilian_mirror.png"
    image bg aw_madeline_shc = "away/img/bg/aw_madeline_shc.png"
    image bg aw_ment_dch = "away/img/bg/aw_ment_dch.png"
    image bg aw_niya = "away/img/bg/aw_niya.png"
    image bg aw_r1_bg_v1 = "away/img/bg/aw_r1_bg_v1.png"
    image bg aw_r1_bg_v2 = "away/img/bg/aw_r1_bg_v2.png"
    image bg aw_r1_bg_v3 = "away/img/bg/aw_r1_bg_v3.png"
    image bg aw_r1_bg_v4 = "away/img/bg/aw_r1_bg_v4.png"
    image bg aw_shcool_toulet = "away/img/bg/aw_shcool_toulet.png"
    image bg aw_shcool_toulet_3g = "away/img/bg/aw_shcool_toulet_3g.png"
    image bg aw_shcool_toulet_5g = "away/img/bg/aw_shcool_toulet_5g.png"
    image bg aw_st_fs_1 = "away/img/bg/aw_st_fs_1.png"
    image bg aw_st_fs_2 = "away/img/bg/aw_st_fs_2.png"
    image bg aw_st_fs_3 = "away/img/bg/aw_st_fs_3.png"
    image bg aw_st_fs_4 = "away/img/bg/aw_st_fs_4.png"
    image bg aw_st_fs_5 = "away/img/bg/aw_st_fs_5.png"
    image bg aw_st_fs_6 = "away/img/bg/aw_st_fs_6.png"
    image bg aw_st_fs_7 = "away/img/bg/aw_st_fs_7.png"
    image bg aw_st_fs_end = "away/img/bg/aw_st_fs_end.png"
    image bg aw_str_morn = "away/img/bg/aw_str_morn.png"
    image bg aw_str_old_morn = "away/img/bg/aw_str_old_morn.png"
    image bg aw_str_prom_morn = "away/img/bg/aw_str_prom_morn.png"

    image bg aw_2man_bg = "away/img/bg/aw_2man_bg.png"
    image bg aw_aft_end_scene_1 = "away/img/bg/aw_aft_end_scene_1.png"
    image bg aw_aft_end_scene_2 = "away/img/bg/aw_aft_end_scene_2.png"
    image bg aw_aft_end_scene_3 = "away/img/bg/aw_aft_end_scene_3.png"
    image bg aw_as_cor_r = "away/img/bg/aw_as_cor_r.png"
    image bg aw_axe_zam = "away/img/bg/aw_axe_zam.png"
    image bg aw_bloodeye_1 = "away/img/bg/aw_bloodeye_1.png"
    image bg aw_bloodeye_2 = "away/img/bg/aw_bloodeye_2.png"
    image bg aw_chorch = "away/img/bg/aw_chorch.png"
    image bg aw_chorch_baw = "away/img/bg/aw_chorch_baw.png"
    image bg aw_doclog = "away/img/bg/aw_doclog.png"
    image bg aw_f_cor_1 = "away/img/bg/aw_f_cor_1.png"
    image bg aw_f_cor_2 = "away/img/bg/aw_f_cor_2.png"
    image bg aw_f_cor_3 = "away/img/bg/aw_f_cor_3.png"
    image bg aw_f_cor_4 = "away/img/bg/aw_f_cor_4.png"
    image bg aw_f_cor_5 = "away/img/bg/aw_f_cor_5.png"
    image bg aw_f_cor_6 = "away/img/bg/aw_f_cor_6.png"
    image bg aw_f_cor_7 = "away/img/bg/aw_f_cor_7.png"
    image bg aw_f_cor_8 = "away/img/bg/aw_f_cor_8.png"
    image bg aw_f_cor_9 = "away/img/bg/aw_f_cor_9.png"
    image bg aw_final_madeline_mad_1 = "away/img/bg/aw_final_madeline_mad_1.png"
    image bg aw_final_madeline_mad_2 = "away/img/bg/aw_final_madeline_mad_2.png"
    image bg aw_him_sh_1 = "away/img/bg/aw_him_sh_1.png"
    image bg aw_him_sh_2 = "away/img/bg/aw_him_sh_2.png"
    image bg aw_him_sh_3 = "away/img/bg/aw_him_sh_3.png"
    image bg aw_him_sh_4 = "away/img/bg/aw_him_sh_4.png"
    image bg aw_kd_cor_sun = "away/img/bg/aw_kd_cor_sun.png"
    image bg aw_korpusd_d = "away/img/bg/aw_korpusd_d.png"
    image bg aw_korpusd_d_w_bg = "away/img/bg/aw_korpusd_d_w_bg.png"
    image bg aw_kul_pm_1 = "away/img/bg/aw_kul_pm_1.png"
    image bg aw_kul_pm_2 = "away/img/bg/aw_kul_pm_2.png"
    image bg aw_kul_pm_3 = "away/img/bg/aw_kul_pm_3.png"
    image bg aw_kul_pm_4 = "away/img/bg/aw_kul_pm_4.png"
    image bg aw_lavka_night = "away/img/bg/aw_lavka_night.png"
    image bg aw_liftcabin = "away/img/bg/aw_liftcabin.png"
    image bg aw_mad_dead_1 = "away/img/bg/aw_mad_dead_1.png"
    image bg aw_mad_dead_2 = "away/img/bg/aw_mad_dead_2.png"
    image bg aw_mad_dead_3 = "away/img/bg/aw_mad_dead_3.png"
    image bg aw_madelein_dead = "away/img/bg/aw_madelein_dead.png"
    image bg aw_madelein_last_word = "away/img/bg/aw_madelein_last_word.png"
    image bg aw_madeleine_dead = "away/img/bg/aw_madeleine_dead.png"
    image bg aw_madeleine_dead_end = "away/img/bg/aw_madeleine_dead_end.png"
    image bg aw_madeleine_here = "away/img/bg/aw_madeleine_here.png"
    image bg aw_madeleine_shed = "away/img/bg/aw_madeleine_shed.png"
    image bg aw_madl_r = "away/img/bg/aw_madl_r.png"
    image bg aw_mental_cor_sun = "away/img/bg/aw_mental_cor_sun.png"
    image bg aw_murder_house = "away/img/bg/aw_murder_house.png"
    image bg aw_murderer_1 = "away/img/bg/aw_murderer_1.png"
    image bg aw_murderer_2 = "away/img/bg/aw_murderer_2.png"
    image bg aw_murderer_3 = "away/img/bg/aw_murderer_3.png"
    image bg aw_murderer_4 = "away/img/bg/aw_murderer_4.png"
    image bg aw_murderer_5 = "away/img/bg/aw_murderer_5.png"
    image bg aw_murderer_6 = "away/img/bg/aw_murderer_6.png"
    image bg aw_murderer_7 = "away/img/bg/aw_murderer_7.png"
    image bg aw_operation_bg = "away/img/bg/aw_operation_bg.png"
    image bg aw_par_memo_bg = "away/img/bg/aw_par_memo_bg.png"
    image bg aw_private_ms_1 = "away/img/bg/aw_private_ms_1.png"
    image bg aw_private_ms_2 = "away/img/bg/aw_private_ms_2.png"
    image bg aw_private_ms_3 = "away/img/bg/aw_private_ms_3.png"
    image bg aw_private_ms_4 = "away/img/bg/aw_private_ms_4.png"
    image bg aw_private_ms_end = "away/img/bg/aw_private_ms_end.png"
    image bg aw_private_r_1 = "away/img/bg/aw_private_r_1.png"
    image bg aw_private_r_2 = "away/img/bg/aw_private_r_2.png"
    image bg aw_sklad_bg = "away/img/bg/aw_sklad_bg.png"
    image bg aw_sklad_photos = "away/img/bg/aw_sklad_photos.png"
    image bg aw_sklad_trash_1 = "away/img/bg/aw_sklad_trash_1.png"
    image bg aw_sklad_trash_2 = "away/img/bg/aw_sklad_trash_2.png"
    image bg aw_sklad_trash_3 = "away/img/bg/aw_sklad_trash_3.png"
    image bg aw_str_bhndskld = "away/img/bg/aw_str_bhndskld.png"
    image bg aw_streat_rain = "away/img/bg/aw_streat_rain.png"
    image bg aw_wrdiray = "away/img/bg/aw_wrdiray.png"
    image bg aw_zanaves_bg = "away/img/bg/aw_zanaves_bg.png"


    #EFF
    image aw_ges_logo_gl = "away/img/eff/aw_ges_logo_gl.png"
    image aw_df_a_1 = "away/img/eff/aw_df_a_1.png"
    image aw_df_a_2 = "away/img/eff/aw_df_a_2.png"
    image aw_df_a_3 = "away/img/eff/aw_df_a_3.png"
    image aw_df_a_4 = "away/img/eff/aw_df_a_4.png"
    image aw_sch_p_a_1 = "away/img/eff/aw_sch_p_a_1.png"
    image aw_sch_p_a_2 = "away/img/eff/aw_sch_p_a_2.png"
    image aw_mmn_1 = "away/img/eff/aw_mmn_1.png"
    image aw_mmn_2 = "away/img/eff/aw_mmn_2.png"
    image aw_mmn_3 = "away/img/eff/aw_mmn_3.png"
    image blood = "away/img/eff/blood.png"


    #SCENE
    image bg aw_prologue_crash_reakt = "away/img/scn/aw_prologue_crash_reakt.png"


    #PARTS
    image aw_r1_pc_desctop_bg = "away/img/parts/aw_r1_pc_desctop_bg.png"
    image aw_r1_pc_desctop_load = "away/img/parts/aw_r1_pc_desctop_load.png"
    image aw_r1_pc_f_doc = "away/img/parts/aw_r1_pc_f_doc.png"
    image aw_r1_pc_f_game = "away/img/parts/aw_r1_pc_f_game.png"
    image aw_r1_pc_f_mus = "away/img/parts/aw_r1_pc_f_mus.png"
    image aw_r1_pc_f_pic = "away/img/parts/aw_r1_pc_f_pic.png"
    image aw_r1_pc_fb_mess_bg = "away/img/parts/aw_r1_pc_fb_mess_bg.png"
    image aw_r1_pc_fb_mp = "away/img/parts/aw_r1_pc_fb_mp.png"
    image aw_r1_pc_bg_1 = "away/img/parts/aw_r1_pc_bg_1.png"
    image aw_r1_pc_bg_2 = "away/img/parts/aw_r1_pc_bg_2.png"
    image aw_r1_pc_bg_off = "away/img/parts/aw_r1_pc_bg_off.png"
    image aw_r1_pc_code_bg = "away/img/parts/aw_r1_pc_code_bg.png"
    image aw_r1_pc_p1 = "away/img/parts/aw_r1_pc_p1.png"
    image aw_r1_pc_p2 = "away/img/parts/aw_r1_pc_p2.png"
    image aw_r1_pc_p3 = "away/img/parts/aw_r1_pc_p3.png"
    image aw_r1_pc_p4 = "away/img/parts/aw_r1_pc_p4.png"
    image aw_r1_pc_p5 = "away/img/parts/aw_r1_pc_p5.png"
    image aw_r1_pc_p6 = "away/img/parts/aw_r1_pc_p6.png"
    image aw_r1_pc_p7 = "away/img/parts/aw_r1_pc_p7.png"
    image aw_r1_pc_p8 = "away/img/parts/aw_r1_pc_p8.png"
    image aw_r1_pc_p9 = "away/img/parts/aw_r1_pc_p9.png"
    image aw_pc_msg_1 = "away/img/parts/aw_pc_msg_1.png"
    image aw_pc_msg_2 = "away/img/parts/aw_pc_msg_2.png"
    image aw_pc_msg_3 = "away/img/parts/aw_pc_msg_3.png"
    image aw_pc_msg_4 = "away/img/parts/aw_pc_msg_4.png"
    image aw_pc_msg_5 = "away/img/parts/aw_pc_msg_5.png"
    image aw_pc_msg_6 = "away/img/parts/aw_pc_msg_6.png"
    image aw_pc_msg_7 = "away/img/parts/aw_pc_msg_7.png"
    image aw_pc_msg_8 = "away/img/parts/aw_pc_msg_8.png"
    image aw_pc_msg_9 = "away/img/parts/aw_pc_msg_9.png"
    image aw_pc_msg_10 = "away/img/parts/aw_pc_msg_10.png"
    image aw_pc_msg_scrbg = "away/img/parts/aw_pc_msg_scrbg.png"
    image aw_r1_pc_bg_pashelp = "away/img/parts/aw_r1_pc_bg_pashelp.png"
    image aw_r_ges_spl = "away/img/parts/aw_r_ges_spl.png"
    image aw_r_tv_log = "away/img/parts/aw_r_tv_log.png"
    image aw_warn_1 = "away/img/parts/aw_warn_1.png"
    image aw_warn_2 = "away/img/parts/aw_warn_2.png"
    image aw_ig_int_1 = "away/img/parts/aw_ig_int_1.png"
    image aw_ig_int_2 = "away/img/parts/aw_ig_int_2.png"
    image aw_ig_int_3 = "away/img/parts/aw_ig_int_3.png"
    image aw_ig_int_4 = "away/img/parts/aw_ig_int_4.png"
    image aw_km_dadesk_fp = "away/img/parts/aw_km_dadesk_fp.png"
    image aw_km_mr_pht = "away/img/parts/aw_km_mr_pht.png"
    image aw_kn_bear_p1 = "away/img/parts/aw_kn_bear_p1.png"
    image aw_kn_bear_p2 = "away/img/parts/aw_kn_bear_p2.png"
    image aw_kn_bear_p3 = "away/img/parts/aw_kn_bear_p3.png"
    image aw_kn_bear_p4 = "away/img/parts/aw_kn_bear_p4.png"
    image aw_kn_r1_door = "away/img/parts/aw_kn_r1_door.png"
    image aw_kn_r1_door2 = "away/img/parts/aw_kn_r1_door2.png"
    image aw_kn_r1_door3 = "away/img/parts/aw_kn_r1_door3.png"
    image aw_km_susuk_1 = "away/img/parts/aw_km_susuk_1.png"
    image aw_km_susuk_2 = "away/img/parts/aw_km_susuk_2.png"
    image aw_km_susuk_3 = "away/img/parts/aw_km_susuk_3.png"
    image aw_km_susuk_4 = "away/img/parts/aw_km_susuk_4.png"
    image aw_km_susuk_5 = "away/img/parts/aw_km_susuk_5.png"
    image aw_kn_bear_b1 = "away/img/parts/aw_kn_bear_b1.png"
    image aw_kn_bear_b2 = "away/img/parts/aw_kn_bear_b2.png"
    image aw_kn_bear_b3 = "away/img/parts/aw_kn_bear_b3.png"
    image aw_kn_bear_trace_r1_1 = "away/img/parts/aw_kn_bear_trace_r1_1.png"
    image aw_kn_bear_trace_r1_2 = "away/img/parts/aw_kn_bear_trace_r1_2.png"
    image aw_kn_bear_trace_r1_3 = "away/img/parts/aw_kn_bear_trace_r1_3.png"
    image aw_kn_bear_trace_r1_4 = "away/img/parts/aw_kn_bear_trace_r1_4.png"
    image aw_km_safe_bg = "away/img/parts/aw_km_safe_bg.png"
    image aw_km_safe_open = "away/img/parts/aw_km_safe_open.png"
    image aw_km_balet_l_1 = "away/img/parts/aw_km_balet_l_1.png"
    image aw_afd_dth1_1 = "away/img/parts/aw_afd_dth1_1.png"
    image aw_afd_dth1_2 = "away/img/parts/aw_afd_dth1_2.png"
    image aw_afd_dth1_3 = "away/img/parts/aw_afd_dth1_3.png"
    image aw_afd_ky1_1 = "away/img/parts/aw_afd_ky1_1.png"
    image aw_afd_ky1_2 = "away/img/parts/aw_afd_ky1_2.png"
    image aw_afd_ky1_3 = "away/img/parts/aw_afd_ky1_3.png"
    image aw_dam_tv_eff_1 = "away/img/parts/aw_dam_tv_eff_1.png"
    image aw_dam_tv_eff_2 = "away/img/parts/aw_dam_tv_eff_2.png"
    image aw_dam_tv_eff_3 = "away/img/parts/aw_dam_tv_eff_3.png"



    image aw_cl_n1_0 = "away/img/parts/codelock/aw_cl_n1_0.png"
    image aw_cl_n1_1 = "away/img/parts/codelock/aw_cl_n1_1.png"
    image aw_cl_n1_2 = "away/img/parts/codelock/aw_cl_n1_2.png"
    image aw_cl_n1_3 = "away/img/parts/codelock/aw_cl_n1_3.png"
    image aw_cl_n1_4 = "away/img/parts/codelock/aw_cl_n1_4.png"
    image aw_cl_n1_5 = "away/img/parts/codelock/aw_cl_n1_5.png"
    image aw_cl_n1_6 = "away/img/parts/codelock/aw_cl_n1_6.png"
    image aw_cl_n1_7 = "away/img/parts/codelock/aw_cl_n1_7.png"
    image aw_cl_n1_8 = "away/img/parts/codelock/aw_cl_n1_8.png"
    image aw_cl_n1_9 = "away/img/parts/codelock/aw_cl_n1_9.png"
    image aw_cl_n2_0 = "away/img/parts/codelock/aw_cl_n2_0.png"
    image aw_cl_n2_1 = "away/img/parts/codelock/aw_cl_n2_1.png"
    image aw_cl_n2_2 = "away/img/parts/codelock/aw_cl_n2_2.png"
    image aw_cl_n2_3 = "away/img/parts/codelock/aw_cl_n2_3.png"
    image aw_cl_n2_4 = "away/img/parts/codelock/aw_cl_n2_4.png"
    image aw_cl_n2_5 = "away/img/parts/codelock/aw_cl_n2_5.png"
    image aw_cl_n2_6 = "away/img/parts/codelock/aw_cl_n2_6.png"
    image aw_cl_n2_7 = "away/img/parts/codelock/aw_cl_n2_7.png"
    image aw_cl_n2_8 = "away/img/parts/codelock/aw_cl_n2_8.png"
    image aw_cl_n2_9 = "away/img/parts/codelock/aw_cl_n2_9.png"
    image aw_cl_n3_0 = "away/img/parts/codelock/aw_cl_n3_0.png"
    image aw_cl_n3_1 = "away/img/parts/codelock/aw_cl_n3_1.png"
    image aw_cl_n3_2 = "away/img/parts/codelock/aw_cl_n3_2.png"
    image aw_cl_n3_3 = "away/img/parts/codelock/aw_cl_n3_3.png"
    image aw_cl_n3_4 = "away/img/parts/codelock/aw_cl_n3_4.png"
    image aw_cl_n3_5 = "away/img/parts/codelock/aw_cl_n3_5.png"
    image aw_cl_n3_6 = "away/img/parts/codelock/aw_cl_n3_6.png"
    image aw_cl_n3_7 = "away/img/parts/codelock/aw_cl_n3_7.png"
    image aw_cl_n3_8 = "away/img/parts/codelock/aw_cl_n3_8.png"
    image aw_cl_n3_9 = "away/img/parts/codelock/aw_cl_n3_9.png"
    image aw_cl_n4_0 = "away/img/parts/codelock/aw_cl_n4_0.png"
    image aw_cl_n4_1 = "away/img/parts/codelock/aw_cl_n4_1.png"
    image aw_cl_n4_2 = "away/img/parts/codelock/aw_cl_n4_2.png"
    image aw_cl_n4_3 = "away/img/parts/codelock/aw_cl_n4_3.png"
    image aw_cl_n4_4 = "away/img/parts/codelock/aw_cl_n4_4.png"
    image aw_cl_n4_5 = "away/img/parts/codelock/aw_cl_n4_5.png"
    image aw_cl_n4_6 = "away/img/parts/codelock/aw_cl_n4_6.png"
    image aw_cl_n4_7 = "away/img/parts/codelock/aw_cl_n4_7.png"
    image aw_cl_n4_8 = "away/img/parts/codelock/aw_cl_n4_8.png"
    image aw_cl_n4_9 = "away/img/parts/codelock/aw_cl_n4_9.png"
    image aw_cl_n5_0 = "away/img/parts/codelock/aw_cl_n5_0.png"
    image aw_cl_n5_1 = "away/img/parts/codelock/aw_cl_n5_1.png"
    image aw_cl_n5_2 = "away/img/parts/codelock/aw_cl_n5_2.png"
    image aw_cl_n5_3 = "away/img/parts/codelock/aw_cl_n5_3.png"
    image aw_cl_n5_4 = "away/img/parts/codelock/aw_cl_n5_4.png"
    image aw_cl_n5_5 = "away/img/parts/codelock/aw_cl_n5_5.png"
    image aw_cl_n5_6 = "away/img/parts/codelock/aw_cl_n5_6.png"
    image aw_cl_n5_7 = "away/img/parts/codelock/aw_cl_n5_7.png"
    image aw_cl_n5_8 = "away/img/parts/codelock/aw_cl_n5_8.png"
    image aw_cl_n5_9 = "away/img/parts/codelock/aw_cl_n5_9.png"
    image aw_cl_n6_0 = "away/img/parts/codelock/aw_cl_n6_0.png"
    image aw_cl_n6_1 = "away/img/parts/codelock/aw_cl_n6_1.png"
    image aw_cl_n6_2 = "away/img/parts/codelock/aw_cl_n6_2.png"
    image aw_cl_n6_3 = "away/img/parts/codelock/aw_cl_n6_3.png"
    image aw_cl_n6_4 = "away/img/parts/codelock/aw_cl_n6_4.png"
    image aw_cl_n6_5 = "away/img/parts/codelock/aw_cl_n6_5.png"
    image aw_cl_n6_6 = "away/img/parts/codelock/aw_cl_n6_6.png"
    image aw_cl_n6_7 = "away/img/parts/codelock/aw_cl_n6_7.png"
    image aw_cl_n6_8 = "away/img/parts/codelock/aw_cl_n6_8.png"
    image aw_cl_n6_9 = "away/img/parts/codelock/aw_cl_n6_9.png"
    image aw_code_lock_m = "away/img/parts/codelock/aw_code_lock_m.png"
    image aw_code_lock_m_op = "away/img/parts/codelock/aw_code_lock_m_op.png"

    image aw_km_dd_n1_1 = "away/img/parts/tablecode/aw_km_dd_n1_1.png"
    image aw_km_dd_n1_2 = "away/img/parts/tablecode/aw_km_dd_n1_2.png"
    image aw_km_dd_n1_3 = "away/img/parts/tablecode/aw_km_dd_n1_3.png"
    image aw_km_dd_n1_4 = "away/img/parts/tablecode/aw_km_dd_n1_4.png"
    image aw_km_dd_n1_5 = "away/img/parts/tablecode/aw_km_dd_n1_5.png"
    image aw_km_dd_n1_6 = "away/img/parts/tablecode/aw_km_dd_n1_6.png"
    image aw_km_dd_n2_1 = "away/img/parts/tablecode/aw_km_dd_n2_1.png"
    image aw_km_dd_n2_2 = "away/img/parts/tablecode/aw_km_dd_n2_2.png"
    image aw_km_dd_n2_3 = "away/img/parts/tablecode/aw_km_dd_n2_3.png"
    image aw_km_dd_n2_4 = "away/img/parts/tablecode/aw_km_dd_n2_4.png"
    image aw_km_dd_n2_5 = "away/img/parts/tablecode/aw_km_dd_n2_5.png"
    image aw_km_dd_n2_6 = "away/img/parts/tablecode/aw_km_dd_n2_6.png"
    image aw_km_dd_n3_1 = "away/img/parts/tablecode/aw_km_dd_n3_1.png"
    image aw_km_dd_n3_2 = "away/img/parts/tablecode/aw_km_dd_n3_2.png"
    image aw_km_dd_n3_3 = "away/img/parts/tablecode/aw_km_dd_n3_3.png"
    image aw_km_dd_n3_4 = "away/img/parts/tablecode/aw_km_dd_n3_4.png"
    image aw_km_dd_n3_5 = "away/img/parts/tablecode/aw_km_dd_n3_5.png"
    image aw_km_dd_n3_6 = "away/img/parts/tablecode/aw_km_dd_n3_6.png"
    image aw_km_dd_n4_1 = "away/img/parts/tablecode/aw_km_dd_n4_1.png"
    image aw_km_dd_n4_2 = "away/img/parts/tablecode/aw_km_dd_n4_2.png"
    image aw_km_dd_n4_3 = "away/img/parts/tablecode/aw_km_dd_n4_3.png"
    image aw_km_dd_n4_4 = "away/img/parts/tablecode/aw_km_dd_n4_4.png"
    image aw_km_dd_n4_5 = "away/img/parts/tablecode/aw_km_dd_n4_5.png"
    image aw_km_dd_n4_6 = "away/img/parts/tablecode/aw_km_dd_n4_6.png"

    image aw_p2_an_1 = "away/img/parts/aw_p2_an_1.png"
    image aw_p2_an_2 = "away/img/parts/aw_p2_an_2.png"
    image aw_p2_an_3 = "away/img/parts/aw_p2_an_3.png"
    image aw_p2_ap_1 = "away/img/parts/aw_p2_ap_1.png"
    image aw_p2_ap_2 = "away/img/parts/aw_p2_ap_2.png"
    image aw_p2_ap_3 = "away/img/parts/aw_p2_ap_3.png"
    image aw_p2_dt_1 = "away/img/parts/aw_p2_dt_1.png"
    image aw_p2_dt_2 = "away/img/parts/aw_p2_dt_2.png"
    image aw_p2_dt_3 = "away/img/parts/aw_p2_dt_3.png"
    image aw_p2_li_1 = "away/img/parts/aw_p2_li_1.png"
    image aw_p2_li_2 = "away/img/parts/aw_p2_li_2.png"
    image aw_p2_li_3 = "away/img/parts/aw_p2_li_3.png"
    image aw_p2_prl_1 = "away/img/parts/aw_p2_prl_1.png"
    image aw_p2_prl_2 = "away/img/parts/aw_p2_prl_2.png"
    image aw_p2_outs = "away/img/parts/aw_p2_outs.png"
    image aw_p2_lon = "away/img/parts/aw_p2_lon.png"

    image aw_club_f3 = "away/img/parts/aw_club_f3.png"
    image aw_club_f2 = "away/img/parts/aw_club_f2.png"
    image aw_club_f1 = "away/img/parts/aw_club_f1.png"
    image aw_fmind_2_3 = "away/img/parts/aw_fmind_2_3.png"
    image aw_fmind_2_2 = "away/img/parts/aw_fmind_2_2.png"
    image aw_fmind_2_1 = "away/img/parts/aw_fmind_2_1.png"
    image aw_fmind_1_3 = "away/img/parts/aw_fmind_1_3.png"
    image aw_fmind_1_2 = "away/img/parts/aw_fmind_1_2.png"
    image aw_fmind_1_1 = "away/img/parts/aw_fmind_1_1.png"
    image aw_kat_murd_3 = "away/img/parts/aw_kat_murd_3.png"
    image aw_kat_murd_2 = "away/img/parts/aw_kat_murd_2.png"
    image aw_kat_murd_1 = "away/img/parts/aw_kat_murd_1.png"
    image aw_korpusd_d_w_fp = "away/img/parts/aw_korpusd_d_w_fp.png"
    image aw_single_match = "away/img/parts/aw_single_match.png"

    image aw_himori_mess_bg = "away/img/parts/aw_himori_mess/aw_himori_mess_bg.png"
    image aw_himori_mess_bg2 = "away/img/parts/aw_himori_mess/aw_himori_mess_bg2.png"
    image aw_kul_pc_mes_1 = "away/img/parts/aw_himori_mess/aw_kul_pc_mes_1.png"
    image aw_kul_pc_mes_2 = "away/img/parts/aw_himori_mess/aw_kul_pc_mes_2.png"
    image aw_kul_pc_mes_3 = "away/img/parts/aw_himori_mess/aw_kul_pc_mes_3.png"
    image aw_kul_pc_mes_4 = "away/img/parts/aw_himori_mess/aw_kul_pc_mes_4.png"
    image aw_kul_pc_mes_5 = "away/img/parts/aw_himori_mess/aw_kul_pc_mes_5.png"
    image aw_kul_pc_mes_6 = "away/img/parts/aw_himori_mess/aw_kul_pc_mes_6.png"
    image aw_kul_pc_mes_7 = "away/img/parts/aw_himori_mess/aw_kul_pc_mes_7.png"
    image aw_kul_pc_mes_8 = "away/img/parts/aw_himori_mess/aw_kul_pc_mes_8.png"
    image aw_kul_pc_mes_9 = "away/img/parts/aw_himori_mess/aw_kul_pc_mes_9.png"
    image aw_kul_pc_mes_10 = "away/img/parts/aw_himori_mess/aw_kul_pc_mes_10.png"
    image aw_kul_pc_mes_11 = "away/img/parts/aw_himori_mess/aw_kul_pc_mes_11.png"
    image aw_kul_pc_mes_12 = "away/img/parts/aw_himori_mess/aw_kul_pc_mes_12.png"

    image aw_f_title_am = "away/img/parts/aw_f_title_am.png"
    image aw_f_title_gm = "away/img/parts/aw_f_title_gm.png"
    image aw_f_title_m = "away/img/parts/aw_f_title_m.png"
    image aw_f_title_tfp = "away/img/parts/aw_f_title_tfp.png"


    #OUTFIT
    image aw_keycard_r1 = "away/img/spr/outfit/aw_keycard_r1.png"
    image aw_r1_fuse = "away/img/spr/outfit/aw_r1_fuse.png"
    image aw_tvbattarey = "away/img/spr/outfit/aw_tvbattarey.png"
    image aw_p_pills = "away/img/spr/outfit/aw_p_pills.png"
    image aw_r1_paper_p = "away/img/spr/outfit/aw_r1_paper_p.png"
    image aw_r1_paper_p_2 = "away/img/spr/outfit/aw_r1_paper_p_2.png"
    image aw_r1_paper_p_3 = "away/img/spr/outfit/aw_r1_paper_p_3.png"
    image aw_diray_open_e = "away/img/spr/outfit/aw_diray_open_e.png"
    image aw_km_mrkey = "away/img/spr/outfit/aw_km_mrkey.png"
    image aw_dr_mess = "away/img/spr/outfit/aw_dr_mess.png"
    image aw_diray_open_af1m = "away/img/spr/outfit/aw_diray_open_af1m.png"

    #SPR
    image aw_niki_srp = "away/img/spr/nik/aw_niki_srp.png"
    image aw_niki_srp_o = "away/img/spr/nik/aw_niki_srp_o.png"

    image aw_sil_shcool_girl = "away/img/spr/char/aw_sil_shcool_girl.png"
    image aw_man_spr = "away/img/spr/char/aw_man_spr.png"

    image aw_madeleine_spr = "away/img/spr/mad/aw_madeleine_spr.png"



