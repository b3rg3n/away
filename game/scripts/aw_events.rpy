#####БУДЬТЕ ЧЕСТНЫ САМИ С СОБОЙ, ИЛИ КИШКА ТОНКА ПРОЙТИ ВСЁ БЕЗ ЖУЛЬНИЧЕСТВА? НЕУДАЧНИК.#####
label away_ch1_event:
    $ renpy.block_rollback()
    $ aw_fr_light = 0
    $ aw_fr_light_ckek = 0
    $ aw_fr_tv_chek = 0
    $ aw_fr_tv_music = 0
    $ aw_fr_book1 = 0
    $ aw_fr_book2 = 0
    $ aw_fr_book3 = 0
    $ aw_fr_book4 = 0
    $ aw_fr_lockerbox = 0
    $ aw_fr_lockerbox_chek = 0
    $ aw_fr_boxbot = 0
    $ aw_fr_card = 0
    $ aw_fr_card_take = 0
    $ aw_fr_battarey = 0
    $ aw_fr_battarey_take = 0
    $ aw_fr_battarey_use = 0
    $ aw_fr_pc_on = 0
    $ aw_fr_pc_unlock = 0
    $ aw_fr_pills = 0
    $ aw_fr_pills_take = 0
    $ aw_fr_fuse = 0
    $ aw_fr_screw = 0
    $ aw_fr_knife = 0
    $ aw_fr_br_door = 0
    $ aw_fr_room2 = 0
    $ aw_lock_1 = 0
    $ aw_lock_2 = 0
    $ aw_lock_3 = 0
    $ aw_fr_lamp_on = 0
    $ aw_lock_shkaf_check = 0
    $ aw_pr_clotches = 0
    $ aw_lock_shkaf_open = 0

    $ aw_pccp1 = 0
    $ aw_pccp2 = 0
    $ aw_pccp3 = 0
    $ aw_pccp4 = 0
    $ aw_pccp5 = 0
    $ aw_pccp6 = 0
    $ aw_pccp7 = 0
    $ aw_pccp8 = 0
    $ aw_pccp9 = 0

    $ aw_pc_r1_game_chek = 0
    $ aw_pc_r1_dock_chek = 0
    $ aw_pc_r1_mus__chek = 0
    $ aw_pc_r1_picks_chek = 0

    $ aw_r1_lock_op = 0
    $ aw_codenumb_1 = 0
    $ aw_codenumb_2 = 0
    $ aw_codenumb_3 = 1
    $ aw_codenumb_4 = 0
    $ aw_codenumb_5 = 0
    $ aw_codenumb_6 = 0
    $ aw_cl_w_1 = 0
    $ aw_cl_w_2 = 0
    $ aw_cl_w_3 = 0
    $ aw_cl_w_4 = 0
    $ aw_cl_w_5 = 0
    $ aw_cl_w_6 = 0

    $ aw_kat_alive = 0

#Комната 1
label aw_r1_cheker:
    $ renpy.block_rollback()
    if aw_fr_fuse == 1:
        jump r1_f_cheker

    if aw_fr_tv_music == 1 and aw_fr_lamp_on ==1:
        scene bg aw_r1_bg_ltv with dissolve
        call screen aw_r1_s2_scr with dissolve

    if aw_fr_tv_music == 0 and aw_fr_lamp_on ==1:
        scene bg aw_r1_bg_l with dissolve
        call screen aw_r1_s1_2_scr with dissolve
        with dissolve2

    if aw_fr_tv_music == 1 and aw_fr_lamp_on ==0:
        scene bg aw_r1_bg_tv
        call screen aw_r1_s1_1_scr
        with dissolve2

    if aw_fr_tv_music and aw_fr_lamp_on ==0:
        scene bg aw_r1_bg with dissolve
        jump aw_r1_all

label r1_f_cheker:
    $ renpy.block_rollback()
    if aw_fr_tv_music and aw_fr_lamp_on ==1:
        scene bg aw_r1_bg_ltv with dissolve
        call screen aw_r1_f_s2_scr with dissolve

    if aw_fr_tv_music == 0 and aw_fr_lamp_on ==1:
        scene bg aw_r1_bg_l with dissolve
        call screen aw_r1_f_s1_2_scr with dissolve

    if aw_fr_tv_music == 1 and aw_fr_lamp_on ==0:
        scene bg aw_r1_bg_tv with dissolve
        call screen aw_r1_f_s1_1_scr with dissolve

    if aw_fr_tv_music and aw_fr_lamp_on ==0:
        scene bg aw_r1_bg with dissolve
        jump aw_r1_f_all
    

label aw_r1_all:
    $ renpy.block_rollback()
    call screen aw_r1_all_scr with dissolve2
screen aw_r1_all_scr:
    tag aw_r1 
    modal True
    imagemap: 
        ground "away/img/scr/aw_r1_h_all_n.png" 
        hover "away/img/scr/aw_r1_h_all_y.png" 
        alpha True
        hotspot (753, 846, 106, 133) clicked[Jump("aw_r1_buk_chek")]
        hotspot (854, 717, 75, 39) clicked[Jump("aw_r1_b1_chek")]
        hotspot (868, 808, 73, 42) clicked[Jump("aw_r1_b2_chek")]
        hotspot (882, 850, 94, 80) clicked[Jump("aw_r1_b3_chek")]
        hotspot (1101, 535, 44, 74) clicked[Jump("aw_r1_lamp_chek")]
        hotspot (1137, 617, 93, 80) clicked[Jump("aw_r1_pc_chek")]
        hotspot (1265, 611, 104, 101) clicked[Jump("aw_r1_b4_chek")]
        hotspot (1167, 776, 99, 55) clicked[Jump("aw_r1_lock_box_chek")]
        hotspot (1166, 852, 99, 125) clicked[Jump("aw_r1_box_chek")]
        hotspot (1543, 681, 150, 151) clicked[Jump("aw_r1_tv_chek")]
        hotspot (0, 950, 75, 130) clicked[Jump("aw_r2_chek")]

label aw_r1_f_all:
    $ renpy.block_rollback()
    call screen aw_r1_f_all_scr with dissolve2
screen aw_r1_f_all_scr:
    tag aw_r1 
    modal True
    imagemap: 
        ground "away/img/scr/aw_r1_f_h_all_n.png" 
        hover "away/img/scr/aw_r1_f_h_all_y.png" 
        alpha True
        hotspot (753, 846, 106, 133) clicked[Jump("aw_r1_buk_chek")]
        hotspot (854, 717, 75, 39) clicked[Jump("aw_r1_b1_chek")]
        hotspot (868, 808, 73, 42) clicked[Jump("aw_r1_b2_chek")]
        hotspot (882, 850, 94, 80) clicked[Jump("aw_r1_b3_chek")]
        hotspot (1101, 535, 44, 74) clicked[Jump("aw_r1_lamp_chek")]
        hotspot (1137, 617, 93, 80) clicked[Jump("aw_r1_pc_chek")]
        hotspot (1265, 611, 104, 101) clicked[Jump("aw_r1_b4_chek")]
        hotspot (1167, 776, 99, 55) clicked[Jump("aw_r1_lock_box_chek")]
        hotspot (1166, 852, 99, 125) clicked[Jump("aw_r1_box_chek")]
        hotspot (1543, 681, 150, 151) clicked[Jump("aw_r1_tv_chek")]
        hotspot (0, 950, 75, 130) clicked[Jump("aw_r2_chek")]

    #BUCKET
label aw_r1_buk_chek:
    $ renpy.block_rollback()
    if aw_fr_battarey_take == 1:
        jump aw_r1_buk_empt
    if aw_fr_tv_chek == 0:
        th "Тут целая гора всякого и всякого."
        th "Давно пора вытряхнуть эту мусорную корзинку."
        window hide
        jump aw_r1_all
    if aw_fr_tv_chek == 1:
        play sound aw_appear
        $ renpy.pause(2, hard=True)
        show aw_tvbattarey with easeinbottom
        th "Не зря мусор скапливала, слава моей лени!"
        th "Старая батарея от центра."
        th "Кажется, я заменила ее, когда она еще не до конца села. Может быть заряда хватит, чтобы с ее помощью запустить центр и скрасить эту ночь музыкой?"
        $ aw_fr_battarey_take += 1
        hide aw_tvbattarey with dspr
        window hide
        jump aw_r1_all
label aw_r1_buk_empt:
    $ renpy.block_rollback()
    play sound aw_appear
    th "Больше тут нет ничего стоющего. Пора завязывать копаться в мусоре"
    window hide
    jump aw_r1_cheker

    #LAMP
label aw_r1_lamp_chek:
    $ renpy.block_rollback()
    if aw_fr_light == 0:
        jump aw_r1_lamp_use_nl
    if aw_fr_light == 1:
        jump aw_r1_lamp_yl
label aw_r1_lamp_use_nl:
    $ renpy.block_rollback()
    if aw_fr_light_ckek == 0:
        play sound aw_buton_1
        $ renpy.pause(0.6, hard=True)
        play sound aw_buton_1
        $ renpy.pause(0.2, hard=True)
        play sound aw_buton_1
        $ renpy.pause(0.2, hard=True)
        play sound aw_buton_1
        th "Вот-ж блядь, не уж-то свет опять похерился?"
        th "Может, опять пробки выбило, или предохронитель сдох?{w} Снова..."
        $ aw_fr_light_ckek += 1
        window hide
        jump aw_r1_all
    th "Света нет, ровно как и смысла дрюкать светильник. "
    window hide
    jump aw_r1_cheker

label aw_r1_lamp_yl:
    $ renpy.block_rollback()
    play sound aw_buton_1
    $ aw_fr_lamp_on += 1
    if aw_fr_tv_music == 1 and aw_fr_lamp_on ==1:
        scene bg aw_r1_bg_ltv with dissolve
        jump aw_r1_cheker
    scene bg aw_r1_bg_l with dissolve
    jump aw_r1_cheker

    #PC
label aw_r1_pc_chek:
    $ renpy.block_rollback()
    if aw_fr_light == 1:
        jump aw_ly_pc_on
label aw_r1_pc_use_nl:
    $ renpy.block_rollback()
    if aw_fr_light_ckek == 0:
        play sound aw_buton_1
        $ renpy.pause(0.6, hard=True)
        play sound aw_buton_1
        $ renpy.pause(0.2, hard=True)
        th "Отлично..." with dissolve2
        play sound aw_buton_1
        th "Кажется, опять пробки выбило, или предохронитель сдох. Снова...{w} Твою мать." with dissolve
        $ aw_fr_light_ckek +=1
        window hide
        jump aw_r1_cheker
    if aw_fr_light_ckek == 1:
        th "Мне кажется, какая-то тупая часть меня не может понять, что без света его не включить."
        window hide
        jump aw_r1_cheker
label aw_ly_pc_on:
    $ renpy.block_rollback()
    if aw_fr_pc_on == 0:
        play sound aw_pc_on
        show aw_r1_pc_bg_off with dissolve
        $ renpy.pause(3, hard=True)
        show aw_r1_pc_bg_1
        $ renpy.pause(2, hard=True)
        hide aw_r1_pc_bg_1
        $ renpy.pause(2, hard=True)
        play sound aw_computer_logon
        show aw_r1_pc_bg_2 with dspr
        jump aw_r1_pc_turn_on
    if aw_fr_pc_on == 1:
        jump aw_pc_on_msg_scr_l
    if aw_fr_pc_unlock == 0:
        jump aw_r1_pc_turn_on


label aw_r1_pc_turn_on:
    $ renpy.block_rollback()
    show aw_r1_pc_bg_2 with dspr
    call screen aw_r1_pclogin
screen aw_r1_pclogin:
    tag r1
    modal True
    imagemap: 
        ground "away/img/scr/aw_r1_pc_hn.png" 
        hover "away/img/scr/aw_r1_pc_hy.png" 
        alpha True
        hotspot (772, 686, 394, 48) clicked[Jump("aw_r1_pc_code")]
        hotspot (1553, 931, 98, 47) clicked[Jump("aw_r1_cheker")]


label aw_r1_pc_code:
    $ renpy.block_rollback()
    hide aw_r1_pc_p1
    hide aw_r1_pc_p2
    hide aw_r1_pc_p3
    hide aw_r1_pc_p4
    hide aw_r1_pc_p5
    hide aw_r1_pc_p6
    hide aw_r1_pc_p7
    hide aw_r1_pc_p8
    hide aw_r1_pc_p9
    hide aw_r1_pc_code_bg
    hide aw_r1_pc_bg_pashelp
    play sound aw_pc_keyb_s
    show aw_r1_pc_p1
    pause 0.2
    play sound aw_pc_keyb_s
    show aw_r1_pc_p2
    pause 0.2
    play sound aw_pc_keyb_s
    show aw_r1_pc_p3
    pause 0.2
    play sound aw_pc_keyb_s
    show aw_r1_pc_p4
    pause 0.2
    play sound aw_pc_keyb_s
    show aw_r1_pc_p5
    pause 0.2
    play sound aw_pc_keyb_s
    show aw_r1_pc_p6
    pause 0.2
    play sound aw_pc_keyb_s
    show aw_r1_pc_p7
    pause 0.2
    play sound aw_pc_keyb_s
    show aw_r1_pc_p8
    pause 0.2
    play sound aw_pc_keyb_s
    show aw_r1_pc_p9
    play sound aw_ges_hallo
    jump aw_pc_desktop_active


    #call screen aw_pc_but_0_s
screen aw_pc_but_0_s:
    tag pc
    modal True
    key "i" action Jump("aw_pc_code_point1")
    key "ш" action Jump("aw_pc_code_point1")
    key "q" or "й" action Jump("aw_pc_but_1")
    key "w" or "ц" action Jump("aw_pc_but_1")
    key "e" or "у" action Jump("aw_pc_but_1")
    key "r" or "к" action Jump("aw_pc_but_1")
    key "t" or "е" action Jump("aw_pc_but_1")
    key "y" or "н" action Jump("aw_pc_but_1")
    key "u" or "г" action Jump("aw_pc_but_1")
    key "o" or "щ" action Jump("aw_pc_but_1")
    key "p" or "з" action Jump("aw_pc_but_1")
    key "a" or "ф" action Jump("aw_pc_but_1")
    key "s" or "ы" action Jump("aw_pc_but_1")
    key "d" or "в" action Jump("aw_pc_but_1")
    key "f" or "а" action Jump("aw_pc_but_1")
    key "g" or "п" action Jump("aw_pc_but_1")
    key "h" or "р" action Jump("aw_pc_but_1")
    key "j" or "о" action Jump("aw_pc_but_1")
    key "k" or "л" action Jump("aw_pc_but_1")
    key "l" or "д" action Jump("aw_pc_but_1")
    key "z" or "я" action Jump("aw_pc_but_1")
    key "x" or "ч" action Jump("aw_pc_but_1")
    key "c" or "с" action Jump("aw_pc_but_1")
    key "v" or "м" action Jump("aw_pc_but_1")
    key "b" or "и" action Jump("aw_pc_but_1")
    key "n" or "т" action Jump("aw_pc_but_1")
    key "m" or "ь" action Jump("aw_pc_but_1")
    key "1" action Jump("aw_pc_but_1")
    key "2" action Jump("aw_pc_but_1")
    key "3" action Jump("aw_pc_but_1")
    key "4" action Jump("aw_pc_but_1")
    key "5" action Jump("aw_pc_but_1")
    key "6" action Jump("aw_pc_but_1")
    key "7" action Jump("aw_pc_but_1")
    key "8" action Jump("aw_pc_but_1")
    key "9" action Jump("aw_pc_but_1")
    key "0" action Jump("aw_pc_but_1")

label aw_pc_code_point1:
    $ renpy.block_rollback()
    $ aw_pccp1 += 1
    jump aw_pc_but_1

    #BUTTON2
label aw_pc_but_1:
    $ renpy.block_rollback()
    play sound aw_pc_keyb_s
    show aw_r1_pc_p1
    call screen aw_pc_but_1_s
screen aw_pc_but_1_s:
    tag pc
    modal True
    key "g" action Jump("aw_pc_code_point2")
    key "п" action Jump("aw_pc_code_point2")
    key "q" or "й" action Jump("aw_pc_but_2")
    key "w" or "ц" action Jump("aw_pc_but_2")
    key "e" or "у" action Jump("aw_pc_but_2")
    key "r" or "к" action Jump("aw_pc_but_2")
    key "t" or "е" action Jump("aw_pc_but_2")
    key "y" or "н" action Jump("aw_pc_but_2")
    key "u" or "г" action Jump("aw_pc_but_2")
    key "i" or "ш" action Jump("aw_pc_but_2")
    key "o" or "щ" action Jump("aw_pc_but_2")
    key "p" or "з" action Jump("aw_pc_but_2")
    key "a" or "ф" action Jump("aw_pc_but_2")
    key "s" or "ы" action Jump("aw_pc_but_2")
    key "d" or "в" action Jump("aw_pc_but_2")
    key "f" or "а" action Jump("aw_pc_but_2")
    key "h" or "р" action Jump("aw_pc_but_2")
    key "j" or "о" action Jump("aw_pc_but_2")
    key "k" or "л" action Jump("aw_pc_but_2")
    key "l" or "д" action Jump("aw_pc_but_2")
    key "z" or "я" action Jump("aw_pc_but_2")
    key "x" or "ч" action Jump("aw_pc_but_2")
    key "c" or "с" action Jump("aw_pc_but_2")
    key "v" or "м" action Jump("aw_pc_but_2")
    key "b" or "и" action Jump("aw_pc_but_2")
    key "n" or "т" action Jump("aw_pc_but_2")
    key "m" or "ь" action Jump("aw_pc_but_2")
    key "1" action Jump("aw_pc_but_2")
    key "2" action Jump("aw_pc_but_2")
    key "3" action Jump("aw_pc_but_2")
    key "4" action Jump("aw_pc_but_2")
    key "5" action Jump("aw_pc_but_2")
    key "6" action Jump("aw_pc_but_2")
    key "7" action Jump("aw_pc_but_2")
    key "8" action Jump("aw_pc_but_2")
    key "9" action Jump("aw_pc_but_2")
    key "0" action Jump("aw_pc_but_2")

label aw_pc_code_point2:
    $ renpy.block_rollback()
    $ aw_pccp2 += 1
    jump aw_pc_but_2

    #BUTTON3
label aw_pc_but_2:
    $ renpy.block_rollback()
    play sound aw_pc_keyb_s
    show aw_r1_pc_p2
    call screen aw_pc_but_2_s
screen aw_pc_but_2_s:
    tag pc
    modal True
    key "o" action Jump("aw_pc_code_point3")
    key "щ" action Jump("aw_pc_code_point3")
    key "q" or "й" action Jump("aw_pc_but_3")
    key "w" or "ц" action Jump("aw_pc_but_3")
    key "e" or "у" action Jump("aw_pc_but_3")
    key "r" or "к" action Jump("aw_pc_but_3")
    key "t" or "е" action Jump("aw_pc_but_3")
    key "y" or "н" action Jump("aw_pc_but_3")
    key "u" or "г" action Jump("aw_pc_but_3")
    key "i" or "ш" action Jump("aw_pc_but_3")
    key "p" or "з" action Jump("aw_pc_but_3")
    key "a" or "ф" action Jump("aw_pc_but_3")
    key "s" or "ы" action Jump("aw_pc_but_3")
    key "d" or "в" action Jump("aw_pc_but_3")
    key "f" or "а" action Jump("aw_pc_but_3")
    key "g" or "п" action Jump("aw_pc_but_3")
    key "h" or "р" action Jump("aw_pc_but_3")
    key "j" or "о" action Jump("aw_pc_but_3")
    key "k" or "л" action Jump("aw_pc_but_3")
    key "l" or "д" action Jump("aw_pc_but_3")
    key "z" or "я" action Jump("aw_pc_but_3")
    key "x" or "ч" action Jump("aw_pc_but_3")
    key "c" or "с" action Jump("aw_pc_but_3")
    key "v" or "м" action Jump("aw_pc_but_3")
    key "b" or "и" action Jump("aw_pc_but_3")
    key "n" or "т" action Jump("aw_pc_but_3")
    key "m" or "ь" action Jump("aw_pc_but_3")
    key "1" action Jump("aw_pc_but_3")
    key "2" action Jump("aw_pc_but_3")
    key "3" action Jump("aw_pc_but_3")
    key "4" action Jump("aw_pc_but_3")
    key "5" action Jump("aw_pc_but_3")
    key "6" action Jump("aw_pc_but_3")
    key "7" action Jump("aw_pc_but_3")
    key "8" action Jump("aw_pc_but_3")
    key "9" action Jump("aw_pc_but_3")
    key "0" action Jump("aw_pc_but_3")

label aw_pc_code_point3:
    $ renpy.block_rollback()
    $ aw_pccp3 += 1
    jump aw_pc_but_3

    #BUTTON4
label aw_pc_but_3:
    $ renpy.block_rollback()
    play sound aw_pc_keyb_s
    show aw_r1_pc_p3
    call screen aw_pc_but_3_s
screen aw_pc_but_3_s:
    tag pc
    modal True
    key "t" action Jump("aw_pc_code_point4")
    key "е" action Jump("aw_pc_code_point4")
    key "q" or "й" action Jump("aw_pc_but_4")
    key "w" or "ц" action Jump("aw_pc_but_4")
    key "e" or "у" action Jump("aw_pc_but_4")
    key "r" or "к" action Jump("aw_pc_but_4")
    key "y" or "н" action Jump("aw_pc_but_4")
    key "u" or "г" action Jump("aw_pc_but_4")
    key "i" or "ш" action Jump("aw_pc_but_4")
    key "o" or "щ" action Jump("aw_pc_but_4")
    key "p" or "з" action Jump("aw_pc_but_4")
    key "a" or "ф" action Jump("aw_pc_but_4")
    key "s" or "ы" action Jump("aw_pc_but_4")
    key "d" or "в" action Jump("aw_pc_but_4")
    key "f" or "а" action Jump("aw_pc_but_4")
    key "g" or "п" action Jump("aw_pc_but_4")
    key "h" or "р" action Jump("aw_pc_but_4")
    key "j" or "о" action Jump("aw_pc_but_4")
    key "k" or "л" action Jump("aw_pc_but_4")
    key "l" or "д" action Jump("aw_pc_but_4")
    key "z" or "я" action Jump("aw_pc_but_4")
    key "x" or "ч" action Jump("aw_pc_but_4")
    key "c" or "с" action Jump("aw_pc_but_4")
    key "v" or "м" action Jump("aw_pc_but_4")
    key "b" or "и" action Jump("aw_pc_but_4")
    key "n" or "т" action Jump("aw_pc_but_4")
    key "m" or "ь" action Jump("aw_pc_but_4")
    key "1" action Jump("aw_pc_but_4")
    key "2" action Jump("aw_pc_but_4")
    key "3" action Jump("aw_pc_but_4")
    key "4" action Jump("aw_pc_but_4")
    key "5" action Jump("aw_pc_but_4")
    key "6" action Jump("aw_pc_but_4")
    key "7" action Jump("aw_pc_but_4")
    key "8" action Jump("aw_pc_but_4")
    key "9" action Jump("aw_pc_but_4")
    key "0" action Jump("aw_pc_but_4")

label aw_pc_code_point4:
    $ renpy.block_rollback()
    $ aw_pccp4 += 1
    jump aw_pc_but_4

    #BUTTON5
label aw_pc_but_4:
    $ renpy.block_rollback()
    play sound aw_pc_keyb_s
    show aw_r1_pc_p4
    call screen aw_pc_but_4_s
screen aw_pc_but_4_s:
    tag pc
    modal True
    key "5" action Jump("aw_pc_code_point5")
    key "5" action Jump("aw_pc_code_point5")
    key "q" or "й" action Jump("aw_pc_but_5")
    key "w" or "ц" action Jump("aw_pc_but_5")
    key "e" or "у" action Jump("aw_pc_but_5")
    key "r" or "к" action Jump("aw_pc_but_5")
    key "t" or "е" action Jump("aw_pc_but_5")
    key "y" or "н" action Jump("aw_pc_but_5")
    key "u" or "г" action Jump("aw_pc_but_5")
    key "i" or "ш" action Jump("aw_pc_but_5")
    key "o" or "щ" action Jump("aw_pc_but_5")
    key "p" or "з" action Jump("aw_pc_but_5")
    key "a" or "ф" action Jump("aw_pc_but_5")
    key "s" or "ы" action Jump("aw_pc_but_5")
    key "d" or "в" action Jump("aw_pc_but_5")
    key "f" or "а" action Jump("aw_pc_but_5")
    key "g" or "п" action Jump("aw_pc_but_5")
    key "h" or "р" action Jump("aw_pc_but_5")
    key "j" or "о" action Jump("aw_pc_but_5")
    key "k" or "л" action Jump("aw_pc_but_5")
    key "l" or "д" action Jump("aw_pc_but_5")
    key "z" or "я" action Jump("aw_pc_but_5")
    key "x" or "ч" action Jump("aw_pc_but_5")
    key "c" or "с" action Jump("aw_pc_but_5")
    key "v" or "м" action Jump("aw_pc_but_5")
    key "b" or "и" action Jump("aw_pc_but_5")
    key "n" or "т" action Jump("aw_pc_but_5")
    key "m" or "ь" action Jump("aw_pc_but_5")
    key "1" action Jump("aw_pc_but_5")
    key "2" action Jump("aw_pc_but_5")
    key "3" action Jump("aw_pc_but_5")
    key "4" action Jump("aw_pc_but_5")
    key "6" action Jump("aw_pc_but_5")
    key "7" action Jump("aw_pc_but_5")
    key "8" action Jump("aw_pc_but_5")
    key "9" action Jump("aw_pc_but_5")
    key "0" action Jump("aw_pc_but_5")

label aw_pc_code_point5:
    $ renpy.block_rollback()
    $ aw_pccp5 += 1
    jump aw_pc_but_5

    #BUTTON6
label aw_pc_but_5:
    $ renpy.block_rollback()
    play sound aw_pc_keyb_s
    show aw_r1_pc_p5
    call screen aw_pc_but_5_s
screen aw_pc_but_5_s:
    tag pc
    modal True
    key "o" action Jump("aw_pc_code_point6")
    key "щ" action Jump("aw_pc_code_point6")
    key "q" or "й" action Jump("aw_pc_but_6")
    key "w" or "ц" action Jump("aw_pc_but_6")
    key "e" or "у" action Jump("aw_pc_but_6")
    key "r" or "к" action Jump("aw_pc_but_6")
    key "t" or "е" action Jump("aw_pc_but_6")
    key "y" or "н" action Jump("aw_pc_but_6")
    key "u" or "г" action Jump("aw_pc_but_6")
    key "i" or "ш" action Jump("aw_pc_but_6")
    key "p" or "з" action Jump("aw_pc_but_6")
    key "a" or "ф" action Jump("aw_pc_but_6")
    key "s" or "ы" action Jump("aw_pc_but_6")
    key "d" or "в" action Jump("aw_pc_but_6")
    key "f" or "а" action Jump("aw_pc_but_6")
    key "g" or "п" action Jump("aw_pc_but_6")
    key "h" or "р" action Jump("aw_pc_but_6")
    key "j" or "о" action Jump("aw_pc_but_6")
    key "k" or "л" action Jump("aw_pc_but_6")
    key "l" or "д" action Jump("aw_pc_but_6")
    key "z" or "я" action Jump("aw_pc_but_6")
    key "x" or "ч" action Jump("aw_pc_but_6")
    key "c" or "с" action Jump("aw_pc_but_6")
    key "v" or "м" action Jump("aw_pc_but_6")
    key "b" or "и" action Jump("aw_pc_but_6")
    key "n" or "т" action Jump("aw_pc_but_6")
    key "m" or "ь" action Jump("aw_pc_but_6")
    key "1" action Jump("aw_pc_but_6")
    key "2" action Jump("aw_pc_but_6")
    key "3" action Jump("aw_pc_but_6")
    key "4" action Jump("aw_pc_but_6")
    key "5" action Jump("aw_pc_but_6")
    key "6" action Jump("aw_pc_but_6")
    key "7" action Jump("aw_pc_but_6")
    key "8" action Jump("aw_pc_but_6")
    key "9" action Jump("aw_pc_but_6")
    key "0" action Jump("aw_pc_but_6")

label aw_pc_code_point6:
    $ renpy.block_rollback()
    $ aw_pccp6 += 1
    jump aw_pc_but_6

    #BUTTON7
label aw_pc_but_6:
    $ renpy.block_rollback()
    play sound aw_pc_keyb_s
    show aw_r1_pc_p6
    call screen aw_pc_but_6_s
screen aw_pc_but_6_s:
    tag pc
    modal True
    key "n" action Jump("aw_pc_code_point7")
    key "т" action Jump("aw_pc_code_point7")
    key "q" or "й" action Jump("aw_pc_but_7")
    key "w" or "ц" action Jump("aw_pc_but_7")
    key "e" or "у" action Jump("aw_pc_but_7")
    key "r" or "к" action Jump("aw_pc_but_7")
    key "t" or "е" action Jump("aw_pc_but_7")
    key "y" or "н" action Jump("aw_pc_but_7")
    key "u" or "г" action Jump("aw_pc_but_7")
    key "i" or "ш" action Jump("aw_pc_but_7")
    key "o" or "щ" action Jump("aw_pc_but_7")
    key "p" or "з" action Jump("aw_pc_but_7")
    key "a" or "ф" action Jump("aw_pc_but_7")
    key "s" or "ы" action Jump("aw_pc_but_7")
    key "d" or "в" action Jump("aw_pc_but_7")
    key "f" or "а" action Jump("aw_pc_but_7")
    key "g" or "п" action Jump("aw_pc_but_7")
    key "h" or "р" action Jump("aw_pc_but_7")
    key "j" or "о" action Jump("aw_pc_but_7")
    key "k" or "л" action Jump("aw_pc_but_7")
    key "l" or "д" action Jump("aw_pc_but_7")
    key "z" or "я" action Jump("aw_pc_but_7")
    key "x" or "ч" action Jump("aw_pc_but_7")
    key "c" or "с" action Jump("aw_pc_but_7")
    key "v" or "м" action Jump("aw_pc_but_7")
    key "b" or "и" action Jump("aw_pc_but_7")
    key "m" or "ь" action Jump("aw_pc_but_7")
    key "1" action Jump("aw_pc_but_7")
    key "2" action Jump("aw_pc_but_7")
    key "3" action Jump("aw_pc_but_7")
    key "4" action Jump("aw_pc_but_7")
    key "5" action Jump("aw_pc_but_7")
    key "6" action Jump("aw_pc_but_7")
    key "7" action Jump("aw_pc_but_7")
    key "8" action Jump("aw_pc_but_7")
    key "9" action Jump("aw_pc_but_7")
    key "0" action Jump("aw_pc_but_7")

label aw_pc_code_point7:
    $ renpy.block_rollback()
    $ aw_pccp7 += 1
    jump aw_pc_but_7

    #BUTTON8
label aw_pc_but_7:
    $ renpy.block_rollback()
    play sound aw_pc_keyb_s
    show aw_r1_pc_p7
    call screen aw_pc_but_7_s
screen aw_pc_but_7_s:
    tag pc
    modal True
    key "i" action Jump("aw_pc_code_point8")
    key "ш" action Jump("aw_pc_code_point8")
    key "q" or "й" action Jump("aw_pc_but_8")
    key "w" or "ц" action Jump("aw_pc_but_8")
    key "e" or "у" action Jump("aw_pc_but_8")
    key "r" or "к" action Jump("aw_pc_but_8")
    key "t" or "е" action Jump("aw_pc_but_8")
    key "y" or "н" action Jump("aw_pc_but_8")
    key "u" or "г" action Jump("aw_pc_but_8")
    key "o" or "щ" action Jump("aw_pc_but_8")
    key "p" or "з" action Jump("aw_pc_but_8")
    key "a" or "ф" action Jump("aw_pc_but_8")
    key "s" or "ы" action Jump("aw_pc_but_8")
    key "d" or "в" action Jump("aw_pc_but_8")
    key "f" or "а" action Jump("aw_pc_but_8")
    key "g" or "п" action Jump("aw_pc_but_8")
    key "h" or "р" action Jump("aw_pc_but_8")
    key "j" or "о" action Jump("aw_pc_but_8")
    key "k" or "л" action Jump("aw_pc_but_8")
    key "l" or "д" action Jump("aw_pc_but_8")
    key "z" or "я" action Jump("aw_pc_but_8")
    key "x" or "ч" action Jump("aw_pc_but_8")
    key "c" or "с" action Jump("aw_pc_but_8")
    key "v" or "м" action Jump("aw_pc_but_8")
    key "b" or "и" action Jump("aw_pc_but_8")
    key "n" or "т" action Jump("aw_pc_but_8")
    key "m" or "ь" action Jump("aw_pc_but_8")
    key "1" action Jump("aw_pc_but_8")
    key "2" action Jump("aw_pc_but_8")
    key "3" action Jump("aw_pc_but_8")
    key "4" action Jump("aw_pc_but_8")
    key "5" action Jump("aw_pc_but_8")
    key "6" action Jump("aw_pc_but_8")
    key "7" action Jump("aw_pc_but_8")
    key "8" action Jump("aw_pc_but_8")
    key "9" action Jump("aw_pc_but_8")
    key "0" action Jump("aw_pc_but_8")

label aw_pc_code_point8:
    $ renpy.block_rollback()
    $ aw_pccp8 += 1
    jump aw_pc_but_8

    #BUTTON9
label aw_pc_but_8:
    $ renpy.block_rollback()
    play sound aw_pc_keyb_s
    show aw_r1_pc_p8
    call screen aw_pc_but_8_s
screen aw_pc_but_8_s:
    tag pc
    modal True
    key "t" action Jump("aw_pc_code_point9")
    key "е" action Jump("aw_pc_code_point9")
    key "q" or "й" action Jump("aw_pc_but_cheker")
    key "w" or "ц" action Jump("aw_pc_but_cheker")
    key "e" or "у" action Jump("aw_pc_but_cheker")
    key "r" or "к" action Jump("aw_pc_but_cheker")
    key "y" or "н" action Jump("aw_pc_but_cheker")
    key "u" or "г" action Jump("aw_pc_but_cheker")
    key "i" or "ш" action Jump("aw_pc_but_cheker")
    key "o" or "щ" action Jump("aw_pc_but_cheker")
    key "p" or "з" action Jump("aw_pc_but_cheker")
    key "a" or "ф" action Jump("aw_pc_but_cheker")
    key "s" or "ы" action Jump("aw_pc_but_cheker")
    key "d" or "в" action Jump("aw_pc_but_cheker")
    key "f" or "а" action Jump("aw_pc_but_cheker")
    key "g" or "п" action Jump("aw_pc_but_cheker")
    key "h" or "р" action Jump("aw_pc_but_cheker")
    key "j" or "о" action Jump("aw_pc_but_cheker")
    key "k" or "л" action Jump("aw_pc_but_cheker")
    key "l" or "д" action Jump("aw_pc_but_cheker")
    key "z" or "я" action Jump("aw_pc_but_cheker")
    key "x" or "ч" action Jump("aw_pc_but_cheker")
    key "c" or "с" action Jump("aw_pc_but_cheker")
    key "v" or "м" action Jump("aw_pc_but_cheker")
    key "b" or "и" action Jump("aw_pc_but_cheker")
    key "n" or "т" action Jump("aw_pc_but_cheker")
    key "m" or "ь" action Jump("aw_pc_but_cheker")
    key "1" action Jump("aw_pc_but_cheker")
    key "2" action Jump("aw_pc_but_cheker")
    key "3" action Jump("aw_pc_but_cheker")
    key "4" action Jump("aw_pc_but_cheker")
    key "5" action Jump("aw_pc_but_cheker")
    key "6" action Jump("aw_pc_but_cheker")
    key "7" action Jump("aw_pc_but_cheker")
    key "8" action Jump("aw_pc_but_cheker")
    key "9" action Jump("aw_pc_but_cheker")
    key "0" action Jump("aw_pc_but_cheker")

label aw_pc_code_point9:
    $ renpy.block_rollback()
    $ aw_pccp9 += 1
    jump aw_pc_but_cheker


    #CHEKER
label aw_pc_but_cheker:
    $ renpy.block_rollback()
    play sound aw_pc_keyb_s
    show aw_r1_pc_p9
    if aw_pccp1 == 0:
        jump aw_pc_error
    if aw_pccp2 == 0:
        jump aw_pc_error
    if aw_pccp3 == 0:
        jump aw_pc_error
    if aw_pccp4 == 0:
        jump aw_pc_error
    if aw_pccp5 == 0:
        jump aw_pc_error
    if aw_pccp6 == 0:
        jump aw_pc_error
    if aw_pccp7 == 0:
        jump aw_pc_error
    if aw_pccp8 == 0:
        jump aw_pc_error
    if aw_pccp9 == 0:
        jump aw_pc_error
    play sound aw_ges_hallo
    jump aw_pc_desktop_active

    #ERROR
label aw_pc_error:
    $ renpy.block_rollback()
    play sound aw_computer_deny
    if aw_pccp1 == 1:
        $ aw_pccp1 -= 1
    if aw_pccp2 == 1:
        $ aw_pccp2 -= 1
    if aw_pccp3 == 1:
        $ aw_pccp3 -= 1
    if aw_pccp4 == 1:
        $ aw_pccp4 -= 1
    if aw_pccp5 == 1:
        $ aw_pccp5 -= 1
    if aw_pccp6 == 1:
        $ aw_pccp6 -= 1
    if aw_pccp7 == 1:
        $ aw_pccp7 -= 1
    if aw_pccp8 == 1:
        $ aw_pccp8 -= 1
    if aw_pccp9 == 1:
        $ aw_pccp9 -= 1
    show aw_r1_pc_code_bg with dspr
    hide aw_r1_pc_bg_pashelp with dspr
    $ renpy.pause(1, hard=True)
    call screen aw_r1_pclogin_err with dspr
screen aw_r1_pclogin_err:
    tag pc
    modal True
    imagemap: 
        ground "away/img/scr/aw_r1_pc2_hn.png" 
        hover "away/img/scr/aw_r1_pc2_hy.png" 
        alpha True
        hotspot (772, 686, 394, 48) clicked[Jump("aw_r1_pc_code")]
        hotspot (1553, 931, 98, 47) clicked[Jump("aw_r1_cheker")]
        hotspot (1024, 747, 152, 25) clicked[Jump("aw_r1_rem_pas")]

label aw_r1_rem_pas:
    $ renpy.block_rollback()
    show aw_r1_pc_bg_pashelp with dspr
    call screen aw_r1_pclogin_er with dspr
screen aw_r1_pclogin_er:
    tag r1
    modal True
    imagemap: 
        ground "away/img/scr/aw_r1_pc_hn.png" 
        hover "away/img/scr/aw_r1_pc_hn.png" 
        alpha True
        hotspot (772, 686, 394, 48) clicked[Jump("aw_r1_pc_code")]
        hotspot (1553, 931, 98, 47) clicked[Jump("aw_r1_cheker")]






#PC ACTIVE
label aw_pc_desktop_active:
    $ renpy.block_rollback()
    if aw_pccp1 == 1:
        $ aw_pccp1 -= 1
    if aw_pccp2 == 1:
        $ aw_pccp2 -= 1
    if aw_pccp3 == 1:
        $ aw_pccp3 -= 1
    if aw_pccp4 == 1:
        $ aw_pccp4 -= 1
    if aw_pccp5 == 1:
        $ aw_pccp5 -= 1
    if aw_pccp6 == 1:
        $ aw_pccp6 -= 1
    if aw_pccp7 == 1:
        $ aw_pccp7 -= 1
    if aw_pccp8 == 1:
        $ aw_pccp8 -= 1
    if aw_pccp9 == 1:
        $ aw_pccp9 -= 1
    play sound aw_computer_logon
    show aw_r1_pc_desctop_load with dissolve2
    $ renpy.pause(2, hard=True)
    show aw_r1_pc_desctop_bg with dissolve
    $ renpy.pause(0.5, hard=True)
label aw_pc_desktop_choose:
    call screen aw_r1_pc_desctop_scr with dissolve


#FOLDERS

label aw_r1_pc_gamefolder:
    $ renpy.block_rollback()
    play sound aw_m_dbl_click
    show aw_r1_pc_f_game with dspr
    $ renpy.pause(0.5, hard=True)
    th "Единственно-неизменный." with dissolve
    th "Но я не так давно закрыла последние задания, да и играть, честно говоря, желания нет."
    window hide
    play sound aw_m_click
    hide aw_r1_pc_f_game with dspr
    jump aw_pc_desktop_choose

label aw_r1_pc_docfolder:
    $ renpy.block_rollback()
    play sound aw_m_dbl_click
    show aw_r1_pc_f_doc with dspr
    $ renpy.pause(0.5, hard=True)
    th "Сколько же здесь бездарного хлама." with dissolve
    th "Мне нравится придумывать и писать всякое. Истории. Стихи."
    th "Со временем я поняла, что постоянно пытаюсь высказать одно и тоже, заворачивая мысль в разные обёртки, и это понимание побудило меня бросить это дерьмо."
    th "Всё равно - это лишь бездарно написанный, некрасивый текст, повторяющий себя раз за разом."
    th "Может быть, когда-нибудь, я снова начну писать."
    th "Но точно не сегодня."
    window hide
    play sound aw_m_click
    hide aw_r1_pc_f_doc with dspr
    jump aw_pc_desktop_choose

label aw_r1_pc_musicfolder:
    $ renpy.block_rollback()
    play sound aw_m_dbl_click
    show aw_r1_pc_f_mus with dspr
    $ renpy.pause(0.5, hard=True)
    th "Всё никак не могу накачать хорошей музыки." with dissolve
    window hide
    call screen aw_r1_pc_musfold

label aw_r1_pc_imgfolder:
    $ renpy.block_rollback()
    play sound aw_m_dbl_click
    show aw_r1_pc_f_pic with dspr
    $ renpy.pause(0.5, hard=True)
    th "Фотографии, картинки, рисунки, кадры из кино." with dissolve
    th "Немного того, немного сего."
    th "Особо не налюбуешься.{w} Да и нечем."
    window hide
    play sound aw_m_click
    hide aw_r1_pc_f_pic with dspr
    jump aw_pc_desktop_choose

label aw_r1_pc_internet:
    $ renpy.block_rollback()
    play sound aw_m_click
    show aw_r1_pc_fb_mp with dissolve
    $ renpy.pause(1.5, hard=True)
    th "И зачем я вообще сюда захожу?" with dissolve
    th "Понятия не имею." with dissolve2
    th "В какой-то момент времени мне нравилось общаться с людьми здесь. Со знакомыми, и с людьми, которые живут далеко-далеко от меня."
    th "Сейчас же я, порой, даже не отвечаю на сообщения."
    th "Хотя, должна признать, в такие вот бессонные ночи - просто сидеть и втыкать в экран, отключая мозги - самое то."
    th "Ведь соцсети - это настолько нудное дерьмо, что от этого быстро засыпаешь."
    window hide
    $ renpy.pause(1.5, hard=True)
    play sound aw_m_click
    show aw_r1_pc_fb_mess_bg
    hide aw_r1_pc_fb_mp
    with dspr
    $ renpy.pause(2.1, hard=True)
    th "Скука." with dissolve
    window hide
    $ renpy.pause(5.5, hard=True)
    stop music fadeout 4
    scene black with fade3
    $ renpy.pause(5.5, hard=True)
    play music away_polar_day
    $ renpy.pause(2.5, hard=True)
    scene bg aw_r1_bg_ltv
    show aw_r1_pc_fb_mess_bg
    with dissolve2
    $ renpy.pause(3.5, hard=True)
    play sound aw_pc_sms
    show aw_pc_msg_1 with dspr
    play sound2 aw_v_hm
    $ renpy.pause(1.5, hard=True)
    th "Что?"
    th "Какого чёрта?"
    window hide
    play sound aw_pc_keyboard
    $ renpy.pause(3, hard=True)
    show aw_pc_msg_2 with dspr
    hide aw_pc_msg_1
    $ renpy.pause(0.5, hard=True)
    play sound aw_pc_sms
    show aw_pc_msg_3 with dspr
    hide aw_pc_msg_2
    th "Я никто, и это никогда не было важно..."
    th "Это...{w} Это мне знакомо."
    th "Но..."
    th "Не понимаю. О чём она вообще?"
    window hide
    play sound aw_pc_keyboard
    $ renpy.pause(3, hard=True)
    show aw_pc_msg_4 with dspr
    hide aw_pc_msg_3
    $ renpy.pause(1.5, hard=True)
    play sound aw_pc_sms
    show aw_pc_msg_5 with dspr
    hide aw_pc_msg_4
    $ renpy.pause(1.5, hard=True)
    th "Она?" with dissolve
    window hide
    play sound aw_pc_sms
    show aw_pc_msg_6 with dspr
    hide aw_pc_msg_5
    $ renpy.pause(2.7, hard=True)
    play sound aw_pc_sms
    show aw_pc_msg_7 with dspr
    hide aw_pc_msg_6
    $ renpy.pause(1.7, hard=True)
    play sound aw_pc_sms
    show aw_pc_msg_8 with dspr
    hide aw_pc_msg_7
    $ renpy.pause(1.7, hard=True)
    play sound aw_pc_sms
    show aw_pc_msg_scrbg
    show aw_pc_msg_10
    $ aw_fr_pc_on += 1
    with dspr
    hide aw_pc_msg_8
    call screen aw_pc_msg_link_scr


#CUSTOM PC LABELS
label aw_pc_hide_mus_f:
    $ renpy.block_rollback()
    hide aw_r1_pc_f_mus with dspr
    jump aw_pc_desktop_choose

label aw_pc_on_msg_scr_l:
    $ renpy.block_rollback()
    show aw_r1_pc_desctop_load
    show aw_pc_msg_scrbg
    with fade2
    call screen aw_pc_msg_link_scr
    

    #BOOK S
label aw_r1_b4_chek:
    $ renpy.block_rollback()
    if aw_fr_lamp_on == 0:
        th "Я вряд-ли что-то увижу здесь без света."
        window hide
        jump aw_r1_cheker
    if aw_fr_book4 == 0:
        play sound aw_paper1
        $ renpy.pause(0.4, hard=True)
        "«Что есть сознание?», «Что есть истина?», «Что есть жизнь?», «Что есть «я»?»" with dissolve2
        th "Дерьмо." with dissolve
        th "Возится с учебным материалом посреди ночи у меня нет никакого желания."
        $ aw_fr_book4 += 1
        window hide
        jump aw_r1_cheker
    th "Тут только головная боль и полная безнадёжная скука."
    jump aw_r1_cheker

    #BOOK L-U
label aw_r1_b1_chek:
    $ renpy.block_rollback()
    if aw_fr_lamp_on == 0:
        th "Я вряд-ли что-то увижу здесь без света."
        window hide
        jump aw_r1_cheker
    if aw_fr_book1 == 0:
        play sound aw_raise
        show aw_book_c with dissolve
        $ renpy.pause(0.5, hard=True)
        th "«Потом были бабочки.»" with dissolve
        th "«Наверное, это даже было красиво.»"
        th "«Да.»"
        th "«Они красиво подобраны и уложены, их бедные мёртвые крылышки распростерты все под одним углом.»"
        th "«И мне было так жаль их, бедных, мёртвых: они такие же его жертвы, как я.»"
        aw_gg_hide "Обожаю эту книгу."
        window hide
        hide aw_book_c with dspr
        $ aw_fr_book1 += 1
        play sound aw_paper1
        $ renpy.pause(1, hard=True)
        play sound2 aw_paper2
        "Пролистав страницы, вдыхая запах книжной пыльной бумаги, я хотела было убрать книгу на место, как вдруг к моим ногам из нее выпало несколько пожелтевших листков бумаги." with dissolve
        th "Не уж то разваливается?"
        "Только и подумала я, подбирая листы."
        window hide
        play sound aw_paper2
        show aw_r1_paper_p with dissolve
        $ renpy.pause(5, hard=True)
        play sound aw_v_hm
        th "Какие-то странные стихи." with dissolve
        th "Когда я их написала? Не припомню..."
        play sound aw_paper2
        hide aw_r1_paper_p
        with dspr
        show aw_r1_paper_p_2 with dspr
        $ renpy.pause(3, hard=True)
        th "Ну и бред." with dissolve
        th "Откуда всё это только берется?"
        play sound aw_paper3
        hide aw_r1_paper_p_2 with dspr
        "Встряхнув головой, я запихала листы в книгу и положила на место."
        window hide
        jump aw_r1_cheker
    play sound aw_paper2
    show aw_r1_paper_p_3 with dissolve
    $ renpy.pause(10)
    play sound aw_v_hm
    aw_gg_hide "С Северо-запада на Юго-восток...{w} От Индианы до Кримсона..."
    play sound2 aw_paper3
    hide aw_r1_paper_p3 with dspr
    window hide
    jump aw_r1_cheker

    #BOOK L-C
label aw_r1_b2_chek:
    $ renpy.block_rollback()
    if aw_fr_lamp_on == 0:
        th "Я вряд-ли что-то увижу здесь без света."
        window hide
        jump aw_r1_all
    if aw_fr_book2 == 0:
        play sound aw_raise
        show aw_book_ph with dissolve
        $ renpy.pause(0.5, hard=True)
        th "О-о-у нет, только не это." with dissolve
        th "Лучше дождусь, пока по ней снимут кино."
        $ aw_fr_book2 += 1
        hide aw_book_ph with dspr
        window hide
        jump aw_r1_cheker
    th "Я завязала с физикой." with dissolve
    window hide
    jump aw_r1_cheker

    #BOOK L-D
label aw_r1_b3_chek:
    $ renpy.block_rollback()
    if aw_fr_lamp_on == 0:
        th "Я вряд-ли что-то увижу здесь без света."
        window hide
        jump aw_r1_all
    if aw_fr_book3 == 0:
        play sound aw_raise
        show aw_book_d with dissolve
        $ renpy.pause(0.5, hard=True)
        th "Детектив «БаР»" with dissolve
        th "Я так и не дочитала ее до конца, всё никак нет достаточно времени."
        play sound aw_paper1
        hide aw_book_d with dspr
        $ renpy.pause(1, hard=True)
        "Приоткрыв книгу, я обнаружила там закладку, коей оказалась моя проходная карта."
        show aw_keycard_r1 with dissolve
        th "Так вот куда ты делась, а я тебя в своё время обыскалась."
        $ aw_fr_book3 += 1
        hide aw_keycard_r1 with dspr
        if aw_lock_shkaf_check ==1:
            play sound aw_v_hm
            th "Хм. А ведь ей можно отпереть заклинивший замочек."
            $ aw_fr_card_take += 1
            window hide
            jump aw_r1_cheker
        "С улыбкой произнесла в голове я, убирая закладку, а следом и книгу, на место."
        window hide
        jump aw_r1_cheker
    if aw_lock_shkaf_check ==0:
        th "Сейчас мне точно не до чтения. Голова расскалывается." with dissolve
        window hide
        jump aw_r1_cheker
    if aw_lock_shkaf_check ==1:
        play sound aw_paper1
        show aw_keycard_r1 with dissolve
        th "Моя старая проходная карта. Вроде подойдет, чтобы отпереть заклинившую дверь." with dissolve
        $ aw_fr_card_take += 1
        hide aw_keycard_r1 with dissolve
        window hide
        jump aw_r1_cheker
    if aw_fr_card_take == 1:
        th "Сейчас мне точно не до чтения. Голова расскалывается." with dissolve
        window hide
        jump aw_r1_cheker


    #TV
label aw_r1_tv_chek:
    $ renpy.block_rollback()
    if aw_fr_tv_chek == 1:
        jump aw_r1_tv_chek2
    if aw_fr_tv_chek == 0:
        th "Моя старенькая магнитола с экраном." with dissolve
        th "Когда-то давно меня поразило то, что можно слушать песни и смотреть клипы не на телевизоре, а на какой-то небольшой штучке с экраном."
        th "Должна признать —  видео-кассет с клипами на эту штуку было днём с огнём не сыскать, так что в большинстве своём — наслаждалась я эквалайзером, или же вовсе — отключала экран."
        th "Который, к слову, уже давненько сел, и заместо картинки, при всём желании, может издать лишь слабое свечение."
        aw_gg_hide "Неплохо прокрутить по кругу пару старых кассет, а?"
        window hide
        if aw_fr_light_ckek == 0:
            play sound aw_buton_2
            $ renpy.pause(0.9, hard=True)
            play sound aw_buton_2
            $ renpy.pause(0.4, hard=True)
            play sound2 aw_buton_2
            $ renpy.pause(0.3, hard=True)
            play sound aw_buton_2
            $ renpy.pause(0.4, hard=True)
            play sound2 aw_buton_2
            th "Да твою мать..." with dissolve
            th "Опять света нет?"
            $ aw_fr_light_ckek += 1
        if aw_fr_light_ckek == 1:
            th "К счастью — эта кроха может работать от батареи, так что ей не страшно отсутствие света."
            window hide
        play sound aw_buton_l
        $ renpy.pause(4, hard=True)
        stop sound fadeout 2
        th "И батарея сдохла? Да твою налево то а..."
        $ aw_fr_tv_chek += 1
        window hide
        jump aw_r1_cheker
label aw_r1_tv_chek2:
    $ renpy.block_rollback()
    if aw_fr_battarey_take == 1:
        th "Иди-ка сюда детка..." with dissolve
        window hide
        play sound aw_assembly_p
        $ renpy.pause(6, hard=True)
        play sound2 aw_buton_2
        $ renpy.pause(0.3, hard=True)
        play sound aw_rewind
        scene bg aw_r1_bg_tv with dissolve2
        th "… вот тебе конфетка!"
        stop sound fadeout 3
        play sound2 aw_buton_2
        play music aw_igot5onit fadein 3
        $ aw_fr_tv_music += 1
        $ renpy.pause(1, hard=True)
        play sound aw_v_eah
        aw_gg_hide "О да, моя любимая песня!"
        window hide
        jump aw_r1_cheker
    if aw_fr_light == 1:
        th "Иди-ка сюда детка..." with dissolve
        window hide
        play sound2 aw_buton_2
        $ renpy.pause(0.3, hard=True)
        play sound aw_rewind
        scene bg aw_r1_bg_tv with dissolve2
        th "… вот тебе конфетка!"
        stop sound fadeout 3
        play sound2 aw_buton_2
        play music aw_igot5onit fadein 3
        $ aw_fr_tv_music += 1
        $ renpy.pause(1, hard=True)
        play sound aw_v_eah
        aw_gg_hide "О да, моя любимая песня!"
        window hide
        jump aw_r1_cheker
    if aw_fr_battarey_take == 0 and aw_fr_light ==0 :
        th "Света нет. Батарея сдохла. Музла не будет."
        window hide
        jump aw_r1_cheker

    #BOX D
label aw_r1_box_chek:
    $ renpy.block_rollback()
    if aw_fr_tv_chek == 0:
        th "Там столько всякого хлама - мама не горюй."
        th "Отложим копание в нём на потом, м?"
        window hide
        jump aw_r1_cheker
    if aw_fr_fuse == 0:
        play sound aw_table_op
        th "И что я тут ищу?" with dissolve
        window hide
        play sound aw_serch_table
        $ renpy.pause(3.2, hard=True)
        play sound aw_v_eah
        show aw_r1_fuse with dspr
        th "То что надо!"
        $ aw_fr_fuse += 1
        hide aw_r1_fuse with dspr
        play sound aw_table_cl
        window hide
        jump aw_r1_cheker
    play sound aw_table_op
    $ renpy.pause(0.8, hard=True)
    play sound aw_serch_table
    $ renpy.pause(3.1, hard=True)
    play sound aw_serch_table
    $ renpy.pause(3.2, hard=True)
    th "Ничего интересного."
    play sound aw_table_cl
    window hide
    jump aw_r1_cheker

    #ROOM 2
label aw_r2_chek_ent:
    $ renpy.block_rollback()
    window hide
    play sound aw_door_handle
    scene black with fade2
    play sound2 aw_door_close_1
    scene bg aw_r2_bg with dissolve2
    jump aw_r2_chek

label aw_r2_chek:
    $ renpy.block_rollback()
    window hide
    scene bg aw_r2_bg with dissolve
    if aw_pr_clotches and aw_fr_light and aw_fr_pills == 1:
        jump aw_r2_empty
    if aw_pr_clotches and aw_fr_light == 1:
        jump aw_r2_shkaf_only
    if aw_pr_clotches == 1:
        jump aw_r2_clotch_no
    call screen aw_r2_scr_all with dissolve2

label aw_r2_empty:
    call screen aw_r2_scr_empty with dissolve2

label aw_r2_shkaf_only:
    call screen aw_r2_shk_onl_scr with dissolve2

label aw_r2_clotch_no:
    call screen aw_r2_clotch_no with dissolve2



label aw_r2_s1_chek:
    $ renpy.block_rollback()
    if aw_lock_shkaf_check == 0:
        play sound aw_door_handle
        $ renpy.pause(0.3, hard=True)
        play sound2 aw_latchlocked2
        th "Чёрт, опять эта развалюха заклинила."
        th "Если просунуть в щель между дверью и косяком что-нибудь тоненькое, то замок можно будет отпереть"
        $ aw_lock_shkaf_check += 1
        window hide
        jump aw_r2_chek
    if aw_lock_shkaf_check == 1:
        jump aw_r2_sl_chek_y
label aw_r2_sl_chek_y:
    $ renpy.block_rollback()
    if aw_fr_card_take == 0:
        th "Мне нужно что-то просунуть между полотном и косяком, чтобы поддеть заклинивший язычок."
        window hide
        jump aw_r2_chek
    if aw_fr_card_take == 1:
        jump aw_sr_ls_chek
label aw_sr_ls_chek:
    $ renpy.block_rollback()
    if aw_lock_shkaf_open == 0:
        play sound aw_serch_table
        $ renpy.pause(3, hard=True)
        play sound2 aw_door_handle2
        $ renpy.pause(0.5, hard=True)
        play sound aw_door_wood_op
        $ renpy.pause(1.2, hard=True)
        play sound2 aw_pilltake
        show aw_p_pills with dspr
        th "Риталин..." with dissolve
        th "Я была уверена, что избавилась от этого дерьма."
        th "Честно признать - я никогда не верила своему доктору..."
        play sound aw_v_hm
        th "Действительно-ли мне нужны эти таблетки?"
        menu:
           "Взять с собой":
               window show
               $ aw_fr_pills_take += 1
               $ aw_fr_pills += 1
               jump aw_r2_chek
           "Оставить":
               window show
               th "Не думаю, что мне это нужно." with dissolve
               window hide
               jump aw_r2_chek

    if aw_lock_shkaf_open == 1:
        play sound2 aw_door_handle2
        $ renpy.pause(0.5, hard=True)
        play sound aw_door_wood_op
        $ renpy.pause(0.2, hard=True)
        play sound2 aw_pilltake
        show aw_p_pills with dspr
        play sound aw_v_hm
        menu:
           "Взять с собой":
               window show
               $ aw_fr_pills_take += 1
               $ aw_fr_pills += 1
               jump aw_r2_chek
           "Оставить":
               window show
               th "Не думаю, что мне это нужно." with dissolve
               window hide
               jump aw_r2_chek

label aw_r2_s2_chek:
    $ renpy.block_rollback()
    window hide
    play sound aw_door_wood_op
    "Открыв шкаф, я не долго думая схватила свои старые джинсы и потёртую, еще более древнюю, толстовку." with dissolve
    window hide
    play sound aw_clotch_eqpt
    $ aw_pr_clotches += 1
    scene black with fade2
    $ renpy.pause(1, hard=True)
    scene bg aw_r2_bg with dissolve2
    play sound2 aw_door_close_1
    jump aw_r2_chek


label aw_r2_r1_chek:
    $ renpy.block_rollback()
    play sound aw_door_11
    scene black with fade2
    jump aw_r1_cheker

label aw_r1_lock_box_chek:
    $ renpy.block_rollback()
    jump aw_r1_hack_lock_checker


label aw_r1_hack_lock_checker:
    $ renpy.block_rollback()
    show aw_code_lock_m
    show aw_cl_n1_0
    show aw_cl_n2_0
    show aw_cl_n3_0
    show aw_cl_n4_0
    show aw_cl_n5_0
    show aw_cl_n6_0
    with fade2
    menu:
        "Ввести правильный код":
            jump aw_code_lock_box_open
        "Ввести самому":
            jump aw_r1_hack_lock


label aw_r1_hack_lock:
    $ renpy.block_rollback()
    if aw_codenumb_1 and aw_codenumb_2 and aw_codenumb_3 and aw_codenumb_4 and aw_codenumb_5 and aw_codenumb_6 == 1:
        jump aw_code_lock_box_open
    call screen aw_r1_lock_hack_s with dspr
screen aw_r1_lock_hack_s:
    tag menu 
    modal True
    imagemap: 
        ground "away/img/parts/codelock/aw_code_lock_h_n.png" 
        hover  "away/img/parts/codelock/aw_code_lock_h_y.png" 
        alpha True

        hotspot (893, 393, 24, 89) clicked[Jump("aw_r1_code_1_cheker")]
        hotspot (926, 393, 24, 89) clicked[Jump("aw_r1_code_2_cheker")]
        hotspot (961, 393, 24, 89) clicked[Jump("aw_r1_code_3_cheker")]
        hotspot (994, 393, 24, 89) clicked[Jump("aw_r1_code_4_cheker")]
        hotspot (1029, 393, 24, 89) clicked[Jump("aw_r1_code_5_cheker")]
        hotspot (1062, 393, 24, 89) clicked[Jump("aw_r1_code_6_cheker")]
        hotspot (1841, 1011, 79, 69) clicked[Jump("aw_r1_cant_hack_lock")]

    # WHEELS

label aw_r1_code_1_cheker:
    $ renpy.block_rollback()
    play sound aw_padl_turn
    if aw_cl_w_1 == 0:
        $ aw_cl_w_1 += 1
        hide aw_cl_n1_0
        show aw_cl_n1_1
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_1 == 1:
        $ aw_cl_w_1 += 1
        $ aw_codenumb_1 += 1
        hide aw_cl_n1_1
        show aw_cl_n1_2
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_1 == 2:
        $ aw_cl_w_1 += 1
        $ aw_codenumb_1 -= 1
        hide aw_cl_n1_2
        show aw_cl_n1_3
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_1 == 3:
        $ aw_cl_w_1 += 1
        hide aw_cl_n1_3
        show aw_cl_n1_4
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_1 == 4:
        $ aw_cl_w_1 += 1
        hide aw_cl_n1_4
        show aw_cl_n1_5
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_1 == 5:
        $ aw_cl_w_1 += 1
        hide aw_cl_n1_5
        show aw_cl_n1_6
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_1 == 6:
        $ aw_cl_w_1 += 1
        hide aw_cl_n1_6
        show aw_cl_n1_7
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_1 == 7:
        $ aw_cl_w_1 += 1
        hide aw_cl_n1_7
        show aw_cl_n1_8
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_1 == 8:
        $ aw_cl_w_1 += 1
        hide aw_cl_n1_8
        show aw_cl_n1_9
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_1 == 9:
        $ aw_cl_w_1 -= 9
        hide aw_cl_n1_9
        show aw_cl_n1_0
        with dspr
        jump aw_r1_hack_lock



label aw_r1_code_2_cheker:
    $ renpy.block_rollback()
    play sound aw_padl_turn
    if aw_cl_w_2 == 0:
        $ aw_cl_w_2 += 1
        hide aw_cl_n2_0
        show aw_cl_n2_1
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_2 == 1:
        $ aw_cl_w_2 += 1
        hide aw_cl_n2_1
        show aw_cl_n2_2
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_2 == 2:
        $ aw_cl_w_2 += 1
        hide aw_cl_n2_2
        show aw_cl_n2_3
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_2 == 3:
        $ aw_cl_w_2 += 1
        $ aw_codenumb_2 += 1
        hide aw_cl_n2_3
        show aw_cl_n2_4
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_2 == 4:
        $ aw_cl_w_2 += 1
        $ aw_codenumb_2 -= 1
        hide aw_cl_n2_4
        show aw_cl_n2_5
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_2 == 5:
        $ aw_cl_w_2 += 1
        hide aw_cl_n2_5
        show aw_cl_n2_6
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_2 == 6:
        $ aw_cl_w_2 += 1
        hide aw_cl_n2_6
        show aw_cl_n2_7
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_2 == 7:
        $ aw_cl_w_2 += 1
        hide aw_cl_n2_7
        show aw_cl_n2_8
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_2 == 8:
        $ aw_cl_w_2 += 1
        hide aw_cl_n2_8
        show aw_cl_n2_9
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_2 == 9:
        $ aw_cl_w_2 -= 9
        hide aw_cl_n2_9
        show aw_cl_n2_0
        with dspr
        jump aw_r1_hack_lock

label aw_r1_code_3_cheker:
    $ renpy.block_rollback()
    play sound aw_padl_turn
    if aw_cl_w_3 == 0:
        $ aw_cl_w_3 += 1
        $ aw_codenumb_3 -= 1
        hide aw_cl_n3_0
        show aw_cl_n3_1
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_3 == 1:
        $ aw_cl_w_3 += 1
        hide aw_cl_n3_1
        show aw_cl_n3_2
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_3 == 2:
        $ aw_cl_w_3 += 1
        hide aw_cl_n3_2
        show aw_cl_n3_3
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_3 == 3:
        $ aw_cl_w_3 += 1
        hide aw_cl_n3_3
        show aw_cl_n3_4
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_3 == 4:
        $ aw_cl_w_3 += 1
        hide aw_cl_n3_4
        show aw_cl_n3_5
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_3 == 5:
        $ aw_cl_w_3 += 1
        hide aw_cl_n3_5
        show aw_cl_n3_6
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_3 == 6:
        $ aw_cl_w_3 += 1
        hide aw_cl_n3_6
        show aw_cl_n3_7
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_3 == 7:
        $ aw_cl_w_3 += 1
        hide aw_cl_n3_7
        show aw_cl_n3_8
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_3 == 8:
        $ aw_cl_w_3 += 1
        hide aw_cl_n3_8
        show aw_cl_n3_9
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_3 == 9:
        $ aw_cl_w_3 -= 9
        $ aw_codenumb_3 += 1
        hide aw_cl_n3_9
        show aw_cl_n3_0
        with dspr
        jump aw_r1_hack_lock


label aw_r1_code_4_cheker:
    $ renpy.block_rollback()
    play sound aw_padl_turn
    if aw_cl_w_4 == 0:
        $ aw_cl_w_4 += 1
        $ aw_codenumb_4 += 1
        hide aw_cl_n4_0
        show aw_cl_n4_1
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_4 == 1:
        $ aw_cl_w_4 += 1
        $ aw_codenumb_4 -= 1
        hide aw_cl_n4_1
        show aw_cl_n4_2
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_4 == 2:
        $ aw_cl_w_4 += 1
        hide aw_cl_n4_2
        show aw_cl_n4_3
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_4 == 3:
        $ aw_cl_w_4 += 1
        hide aw_cl_n4_3
        show aw_cl_n4_4
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_4 == 4:
        $ aw_cl_w_4 += 1
        hide aw_cl_n4_4
        show aw_cl_n4_5
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_4 == 5:
        $ aw_cl_w_4 += 1
        hide aw_cl_n4_5
        show aw_cl_n4_6
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_4 == 6:
        $ aw_cl_w_4 += 1
        hide aw_cl_n4_6
        show aw_cl_n4_7
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_4 == 7:
        $ aw_cl_w_4 += 1
        hide aw_cl_n4_7
        show aw_cl_n4_8
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_4 == 8:
        $ aw_cl_w_4 += 1
        hide aw_cl_n4_8
        show aw_cl_n4_9
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_4 == 9:
        $ aw_cl_w_4 -= 9
        hide aw_cl_n4_9
        show aw_cl_n4_0
        with dspr
        jump aw_r1_hack_lock

label aw_r1_code_5_cheker:
    $ renpy.block_rollback()
    play sound aw_padl_turn
    if aw_cl_w_5 == 0:
        $ aw_cl_w_5 += 1
        hide aw_cl_n5_0
        show aw_cl_n5_1
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_5 == 1:
        $ aw_cl_w_5 += 1
        hide aw_cl_n5_1
        show aw_cl_n5_2
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_5 == 2:
        $ aw_cl_w_5 += 1
        hide aw_cl_n5_2
        show aw_cl_n5_3
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_5 == 3:
        $ aw_cl_w_5 += 1
        hide aw_cl_n5_3
        show aw_cl_n5_4
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_5 == 4:
        $ aw_cl_w_5 += 1
        hide aw_cl_n5_4
        show aw_cl_n5_5
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_5 == 5:
        $ aw_cl_w_5 += 1
        $ aw_codenumb_5 += 1
        hide aw_cl_n5_5
        show aw_cl_n5_6
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_5 == 6:
        $ aw_cl_w_5 += 1
        $ aw_codenumb_5 -= 1
        hide aw_cl_n5_6
        show aw_cl_n5_7
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_5 == 7:
        $ aw_cl_w_5 += 1
        hide aw_cl_n5_7
        show aw_cl_n5_8
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_5 == 8:
        $ aw_cl_w_5 += 1
        hide aw_cl_n5_8
        show aw_cl_n5_9
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_5 == 9:
        $ aw_cl_w_5 -= 9
        hide aw_cl_n5_9
        show aw_cl_n5_0
        with dspr
        jump aw_r1_hack_lock

label aw_r1_code_6_cheker:
    $ renpy.block_rollback()
    play sound aw_padl_turn
    if aw_cl_w_6 == 0:
        $ aw_cl_w_6 += 1
        hide aw_cl_n6_0
        show aw_cl_n6_1
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_6 == 1:
        $ aw_cl_w_6 += 1
        hide aw_cl_n6_1
        show aw_cl_n6_2
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_6 == 2:
        $ aw_cl_w_6 += 1
        hide aw_cl_n6_2
        show aw_cl_n6_3
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_6 == 3:
        $ aw_cl_w_6 += 1
        hide aw_cl_n6_3
        show aw_cl_n6_4
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_6 == 4:
        $ aw_cl_w_6 += 1
        hide aw_cl_n6_4
        show aw_cl_n6_5
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_6 == 5:
        $ aw_cl_w_6 += 1
        $ aw_codenumb_6 += 1
        hide aw_cl_n6_5
        show aw_cl_n6_6
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_6 == 6:
        $ aw_cl_w_6 += 1
        $ aw_codenumb_6 -= 1
        hide aw_cl_n6_6
        show aw_cl_n6_7
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_6 == 7:
        $ aw_cl_w_6 += 1
        hide aw_cl_n6_7
        show aw_cl_n6_8
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_6 == 8:
        $ aw_cl_w_6 += 1
        hide aw_cl_n6_8
        show aw_cl_n6_9
        with dspr
        jump aw_r1_hack_lock
    if aw_cl_w_6 == 9:
        $ aw_cl_w_6 -= 9
        hide aw_cl_n6_9
        show aw_cl_n6_0
        with dspr
        jump aw_r1_hack_lock


label aw_r1_cant_hack_lock:
    $ renpy.block_rollback()
    if aw_codenumb_1 == 1:
        $ aw_codenumb_1 -= 1
    if aw_codenumb_2 == 1:
        $ aw_codenumb_2 -= 1
    if aw_codenumb_3 == 0:
        $ aw_codenumb_3 += 1
    if aw_codenumb_4 == 1:
        $ aw_codenumb_4 -= 1
    if aw_codenumb_5 == 1:
        $ aw_codenumb_5 -= 1
    if aw_codenumb_6 == 1:
        $ aw_codenumb_6 -= 1
    if aw_cl_w_1 == 1:
        $ aw_cl_w_1 -= 1
    if aw_cl_w_1 == 2:
        $ aw_cl_w_1 -= 2
    if aw_cl_w_1 == 3:
        $ aw_cl_w_1 -= 3
    if aw_cl_w_1 == 4:
        $ aw_cl_w_1 -= 4
    if aw_cl_w_1 == 5:
        $ aw_cl_w_1 -= 5
    if aw_cl_w_1 == 6:
        $ aw_cl_w_1 -= 6
    if aw_cl_w_1 == 7:
        $ aw_cl_w_1 -= 7
    if aw_cl_w_1 == 8:
        $ aw_cl_w_1 -= 8
    if aw_cl_w_1 == 9:
        $ aw_cl_w_1 -= 9
    if aw_cl_w_2 == 1:
        $ aw_cl_w_2 -= 1
    if aw_cl_w_2 == 2:
        $ aw_cl_w_2 -= 2
    if aw_cl_w_2 == 3:
        $ aw_cl_w_2 -= 3
    if aw_cl_w_2 == 4:
        $ aw_cl_w_2 -= 4
    if aw_cl_w_2 == 5:
        $ aw_cl_w_2 -= 5
    if aw_cl_w_2 == 6:
        $ aw_cl_w_2 -= 6
    if aw_cl_w_2 == 7:
        $ aw_cl_w_2 -= 7
    if aw_cl_w_2 == 8:
        $ aw_cl_w_2 -= 8
    if aw_cl_w_2 == 9:
        $ aw_cl_w_2 -= 9
    if aw_cl_w_3 == 1:
        $ aw_cl_w_3 -= 1
    if aw_cl_w_3 == 2:
        $ aw_cl_w_3 -= 2
    if aw_cl_w_3 == 3:
        $ aw_cl_w_3 -= 3
    if aw_cl_w_3 == 4:
        $ aw_cl_w_3 -= 4
    if aw_cl_w_3 == 5:
        $ aw_cl_w_3 -= 5
    if aw_cl_w_3 == 6:
        $ aw_cl_w_3 -= 6
    if aw_cl_w_3 == 7:
        $ aw_cl_w_3 -= 7
    if aw_cl_w_3 == 8:
        $ aw_cl_w_3 -= 8
    if aw_cl_w_3 == 9:
        $ aw_cl_w_3 -= 9
    if aw_cl_w_4 == 1:
        $ aw_cl_w_4 -= 1
    if aw_cl_w_4 == 2:
        $ aw_cl_w_4 -= 2
    if aw_cl_w_4 == 3:
        $ aw_cl_w_4 -= 3
    if aw_cl_w_4 == 4:
        $ aw_cl_w_4 -= 4
    if aw_cl_w_4 == 5:
        $ aw_cl_w_4 -= 5
    if aw_cl_w_4 == 6:
        $ aw_cl_w_4 -= 6
    if aw_cl_w_4 == 7:
        $ aw_cl_w_4 -= 7
    if aw_cl_w_4 == 8:
        $ aw_cl_w_4 -= 8
    if aw_cl_w_4 == 9:
        $ aw_cl_w_4 -= 9
    if aw_cl_w_5 == 1:
        $ aw_cl_w_5 -= 1
    if aw_cl_w_5 == 2:
        $ aw_cl_w_5 -= 2
    if aw_cl_w_5 == 3:
        $ aw_cl_w_5 -= 3
    if aw_cl_w_5 == 4:
        $ aw_cl_w_5 -= 4
    if aw_cl_w_5 == 5:
        $ aw_cl_w_5 -= 5
    if aw_cl_w_5 == 6:
        $ aw_cl_w_5 -= 6
    if aw_cl_w_5 == 7:
        $ aw_cl_w_5 -= 7
    if aw_cl_w_5 == 8:
        $ aw_cl_w_5 -= 8
    if aw_cl_w_5 == 9:
        $ aw_cl_w_5 -= 9
    if aw_cl_w_6 == 1:
        $ aw_cl_w_6 -= 1
    if aw_cl_w_6 == 2:
        $ aw_cl_w_6 -= 2
    if aw_cl_w_6 == 3:
        $ aw_cl_w_6 -= 3
    if aw_cl_w_6 == 4:
        $ aw_cl_w_6 -= 4
    if aw_cl_w_6 == 5:
        $ aw_cl_w_6 -= 5
    if aw_cl_w_6 == 6:
        $ aw_cl_w_6 -= 6
    if aw_cl_w_6 == 7:
        $ aw_cl_w_6 -= 7
    if aw_cl_w_6 == 8:
        $ aw_cl_w_6 -= 8
    if aw_cl_w_6 == 9:
        $ aw_cl_w_6 -= 9
    hide aw_cl_n1_0
    hide aw_cl_n1_1
    hide aw_cl_n1_2
    hide aw_cl_n1_3
    hide aw_cl_n1_4
    hide aw_cl_n1_5
    hide aw_cl_n1_6
    hide aw_cl_n1_7
    hide aw_cl_n1_8
    hide aw_cl_n1_9
    hide aw_cl_n2_0
    hide aw_cl_n2_1
    hide aw_cl_n2_2
    hide aw_cl_n2_3
    hide aw_cl_n2_4
    hide aw_cl_n2_5
    hide aw_cl_n2_6
    hide aw_cl_n2_7
    hide aw_cl_n2_8
    hide aw_cl_n2_9
    hide aw_cl_n3_0
    hide aw_cl_n3_1
    hide aw_cl_n3_2
    hide aw_cl_n3_3
    hide aw_cl_n3_4
    hide aw_cl_n3_5
    hide aw_cl_n3_6
    hide aw_cl_n3_7
    hide aw_cl_n3_8
    hide aw_cl_n3_9
    hide aw_cl_n4_0
    hide aw_cl_n4_1
    hide aw_cl_n4_2
    hide aw_cl_n4_3
    hide aw_cl_n4_4
    hide aw_cl_n4_5
    hide aw_cl_n4_6
    hide aw_cl_n4_7
    hide aw_cl_n4_8
    hide aw_cl_n4_9
    hide aw_cl_n5_0
    hide aw_cl_n5_1
    hide aw_cl_n5_2
    hide aw_cl_n5_3
    hide aw_cl_n5_4
    hide aw_cl_n5_5
    hide aw_cl_n5_6
    hide aw_cl_n5_7
    hide aw_cl_n5_8
    hide aw_cl_n5_9
    hide aw_cl_n6_0
    hide aw_cl_n6_1
    hide aw_cl_n6_2
    hide aw_cl_n6_3
    hide aw_cl_n6_4
    hide aw_cl_n6_5
    hide aw_cl_n6_6
    hide aw_cl_n6_7
    hide aw_cl_n6_8
    hide aw_cl_n6_9
    hide aw_code_lock_m
    hide screen mnd_lock_hack_s
    with fade2
    jump aw_r1_cheker

label aw_code_lock_box_open:
    play sound aw_padl_unlock
    show aw_code_lock_m_op
    hide aw_code_lock_m with dspr
    scene bg aw_r1_bg_ltv with dissolve2
    play sound aw_table_op
    $ renpy.pause(0.8, hard=True)
    play sound aw_serch_table
    $ renpy.pause(3.1, hard=True)
    play sound aw_v_hm
    show aw_diray_r1 with dissolve
    th "А?" with dissolve
    th "Мой старый дневник?{w} Откуда он тут взялся?"
    th "Мне кажется, я давно от него избавилась..."
    th "А может поэтому и заперла его, чтобы не..."
    $ Aw_Alko("overlay aw_memory_back_1")
    th "Бред!" with hpunch
    th "Откуда вообще здесь замок?"
    th "Я... "
    th "Не понимаю.{w} Не помню."
    window hide
    scene bg aw_r1_bg_ltv
    show aw_diray_r1
    with fade3
    "Я лишь встряхнула головой, продолжая разглядывать кожаную обложку дневника." 
    th "Мой старый дневник." with dissolve2
    th "Помню, как я писала там всякое..."
    th "О чём я?" with dissolve
    th "Нет." with dissolve2
    $ Aw_Alko("overlay aw_memory_back_1")
    th "Я знаю...{w} Уверена, что было что-то другое. Только что же..."
    th "Мысли...{w} Словно каша."
    $ Aw_Alko("overlay aw_pe1")
    th "Я просто не выспалась. Нужно больше спать." with dissolve2
    th "Даже думать тяжело." with awrain2
    th "В любом случае — мне всё равно нечем заняться." with dissolve2
    window hide
    scene bg aw_r1_bg_ltv with fade2
    play sound aw_paper1
    "Словно в оправдание перед кем-то, кто усердно встряхивал мои мозги, переворачивая сознание, стирая из памяти мысли, что секунду назад были в моей голове, сказала я, пододвинув стул поближе к столу."
    "Открыв дневник и, пролистав немного, положила на стол, подперев голову рукой, опустила глаза, вчитываясь в текст."
    play sound aw_paper2
    show aw_diray_open_e with dissolve2
    aw_gg_hide "Привет, дневничок..." with dissolve
    window hide
    stop music fadeout 3
    stop ambience fadeout 4
    scene black with fade3
    $ renpy.pause(4.1, hard=True)
    jump aw_kmlable

label aw_km_cor_1_ch:
    $ renpy.block_rollback()
    scene bg aw_km_kor with dissolve2
    call screen aw_km_mc_scr with dissolve

    #PR
label aw_km_pr_cheker:
    $ renpy.block_rollback()
    play sound aw_r_creak
    scene black with fade2
label aw_km_pr_r:
    $ renpy.block_rollback()
    scene bg aw_km_dadr_bg with dissolve2
    if awkmpt == 1:
        jump aw_km_pr_nt
    call screen aw_pa_r_scr with dissolve


label aw_pa_r_ba_l_ch:
    $ renpy.block_rollback()
    if awkmbaletlist == 1:
        play sound aw_paper2
        show aw_km_balet_l with dissolve
        $ renpy.pause(5, hard=True)
        jump aw_km_pr_r
    stop music fadeout 2
    play sound aw_paper2
    show aw_km_balet_l_1 with dissolve2
    $ renpy.pause(1, hard=True)
    play music aw_spook_box fadein 3
    show aw_km_balet_l with dissolve2
    $ renpy.pause(8, hard=True)
    scene bg aw_km_bal_m with dissolve4
    $ Aw_Alko("bg aw_km_bal_m")
    $ renpy.pause(4, hard=True)
    scene bg aw_km_wom_bm
    show overlay aw_memory_back_1
    with dissolve2
    aw_j1 "У тебя хорошо получается." with dissolve2
    aw_gg_hide "Не уверена. Многое мне не удается."
    aw_j1 "У тебя получается доставлять удовольствие зрителям своими выступлениями."
    aw_j1 "И знаешь, тебя заметили."
    aw_gg_hide "Кто?"
    aw_j1 "Есть один человек. Ты ему очень нравишься.{w} Кхм."
    aw_j1 "Точнее — твой талант."
    aw_j1 "И у него есть для тебя предложение, которое поможет тебе...{w} Продвинуться дальше."
    aw_j1 "Я понимаю, что наша школа — не способна дать многого, оставляя множество закрытых дверей. А тот человек — способен помочь."
    aw_j1 "Ты достойна этого. Ты много стараешься..."
    window hide
    $ renpy.pause(1, hard=True)
    stop music fadeout 6
    play sound aw_tv_noise_2
    $ renpy.pause(2, hard=True)
    scene black
    show overlay aw_memory_back_1
    with dissolve2
    $ renpy.pause(4, hard=True)
    stop sound fadeout 2
    $ renpy.pause(2, hard=True)
    play music aw_grotesque_fantasia fadein 3
    $ awkmbaletlist += 1
    scene bg aw_km_dadr_bg
    show aw_km_balet_l
    with dissolve2
    $ renpy.pause(2, hard=True)
    th "???"
    window hide
    play sound aw_paper2
    jump aw_km_pr_r

label aw_pa_r_pas_l:
    $ renpy.block_rollback()
    play sound aw_paper2
    show aw_dr_mess with dissolve
    aw_gg_hide_kmpr "Пускай призренным будет сей\nЗакончив хуже чем забойный скот"
    aw_gg_hide_kmpr "Чтоб не было измены в памяти моей\nНапоминанием мне будет день тот"
    window hide
    $ renpy.pause(2, hard=True)
    play sound aw_paper2
    jump aw_km_pr_r

label aw_km_pr_nt:
    $ renpy.block_rollback()
    call screen aw_pa_r_nt_scr with dissolve


label aw_pa_r_t_ch:
    $ renpy.block_rollback()
    show aw_km_dadesk_fp
    show aw_km_dd_n1_1
    show aw_km_dd_n2_1
    show aw_km_dd_n3_1
    show aw_km_dd_n4_1
    with dissolve2
    menu:
        "Ввести правильный код":
            jump aw_pa_r_t_open
        "Ввести самому":
            jump aw_pa_r_tlh

label aw_pa_r_tlh:
    $ renpy.block_rollback()
    if awprt1n and awprt2n and awprt3n and awprt4n == 1:
        jump aw_pa_r_t_open
    call screen aw_pa_r_tl_scr with dspr

label aw_km_pr_b1_ch:
    $ renpy.block_rollback()
    play sound aw_m_click
    if awprb1 == 0:
        $ awprt1n -= 1
        $ awprb1 += 1
        hide aw_km_dd_n1_1
        show aw_km_dd_n1_2
        jump aw_pa_r_tlh
    if awprb1 == 1:
        $ awprb1 += 1
        hide aw_km_dd_n1_2
        show aw_km_dd_n1_3
        jump aw_pa_r_tlh
    if awprb1 == 2:
        $ awprb1 += 1
        hide aw_km_dd_n1_3
        show aw_km_dd_n1_4
        jump aw_pa_r_tlh
    if awprb1 == 3:
        $ awprb1 += 1
        hide aw_km_dd_n1_4
        show aw_km_dd_n1_5
        jump aw_pa_r_tlh
    if awprb1 == 4:
        $ awprb1 += 1
        hide aw_km_dd_n1_5
        show aw_km_dd_n1_6
        jump aw_pa_r_tlh
    if awprb1 == 5:
        $ awprt1n += 1
        $ awprb1 -= 5
        hide aw_km_dd_n1_6
        show aw_km_dd_n1_1
        jump aw_pa_r_tlh

label aw_km_pr_b2_ch:
    $ renpy.block_rollback()
    play sound aw_m_click
    if awprb2 == 0:
        $ awprb2 += 1
        hide aw_km_dd_n2_1
        show aw_km_dd_n2_2
        jump aw_pa_r_tlh
    if awprb2 == 1:
        $ awprt2n += 1
        $ awprb2 += 1
        hide aw_km_dd_n2_2
        show aw_km_dd_n2_3
        jump aw_pa_r_tlh
    if awprb2 == 2:
        $ awprt2n -= 1
        $ awprb2 += 1
        hide aw_km_dd_n2_3
        show aw_km_dd_n2_4
        jump aw_pa_r_tlh
    if awprb2 == 3:
        $ awprb2 += 1
        hide aw_km_dd_n2_4
        show aw_km_dd_n2_5
        jump aw_pa_r_tlh
    if awprb2 == 4:
        $ awprb2 += 1
        hide aw_km_dd_n2_5
        show aw_km_dd_n2_6
        jump aw_pa_r_tlh
    if awprb2 == 5:
        $ awprb2 -= 5
        hide aw_km_dd_n2_6
        show aw_km_dd_n2_1
        jump aw_pa_r_tlh

label aw_km_pr_b3_ch:
    $ renpy.block_rollback()
    play sound aw_m_click
    if awprb3 == 0:
        $ awprb3 += 1
        hide aw_km_dd_n3_1
        show aw_km_dd_n3_2
        jump aw_pa_r_tlh
    if awprb3 == 1:
        $ awprt3n += 1
        $ awprb3 += 1
        hide aw_km_dd_n3_2
        show aw_km_dd_n3_3
        jump aw_pa_r_tlh
    if awprb3 == 2:
        $ awprt3n -= 1
        $ awprb3 += 1
        hide aw_km_dd_n3_3
        show aw_km_dd_n3_4
        jump aw_pa_r_tlh
    if awprb3 == 3:
        $ awprb3 += 1
        hide aw_km_dd_n3_4
        show aw_km_dd_n3_5
        jump aw_pa_r_tlh
    if awprb3 == 4:
        $ awprb3 += 1
        hide aw_km_dd_n3_5
        show aw_km_dd_n3_6
        jump aw_pa_r_tlh
    if awprb3 == 5:
        $ awprb3 -= 5
        hide aw_km_dd_n3_6
        show aw_km_dd_n3_1
        jump aw_pa_r_tlh

label aw_km_pr_b4_ch:
    $ renpy.block_rollback()
    play sound aw_m_click
    if awprb4 == 0:
        $ awprb4 += 1
        hide aw_km_dd_n4_1
        show aw_km_dd_n4_2
        jump aw_pa_r_tlh
    if awprb4 == 1:
        $ awprt4n += 1
        $ awprb4 += 1
        hide aw_km_dd_n4_2
        show aw_km_dd_n4_3
        jump aw_pa_r_tlh
    if awprb4 == 2:
        $ awprt4n -= 1
        $ awprb4 += 1
        hide aw_km_dd_n4_3
        show aw_km_dd_n4_4
        jump aw_pa_r_tlh
    if awprb4 == 3:
        $ awprb4 += 1
        hide aw_km_dd_n4_4
        show aw_km_dd_n4_5
        jump aw_pa_r_tlh
    if awprb4 == 4:
        $ awprb4 += 1
        hide aw_km_dd_n4_5
        show aw_km_dd_n4_6
        jump aw_pa_r_tlh
    if awprb4 == 5:
        $ awprb4 -= 5
        hide aw_km_dd_n4_6
        show aw_km_dd_n4_1
        jump aw_pa_r_tlh

label aw_km_pr_t_chl:
    $ renpy.block_rollback()
    if awprb1 == 1:
        $ awprb1 -= 1
    if awprb1 == 2:
        $ awprb1 -= 2
    if awprb1 == 3:
        $ awprb1 -= 3
    if awprb1 == 4:
        $ awprb1 -= 4
    if awprb1 == 5:
        $ awprb1 -= 5
    if awprb1 == 6:
        $ awprb1 -= 6
    if awprb2 == 1:
        $ awprb2 -= 1
    if awprb2 == 2:
        $ awprb2 -= 2
    if awprb2 == 3:
        $ awprb2 -= 3
    if awprb2 == 4:
        $ awprb2 -= 4
    if awprb2 == 5:
        $ awprb2 -= 5
    if awprb2 == 6:
        $ awprb2 -= 6
    if awprb3 == 1:
        $ awprb3 -= 1
    if awprb3 == 2:
        $ awprb3 -= 2
    if awprb3 == 3:
        $ awprb3 -= 3
    if awprb3 == 4:
        $ awprb3 -= 4
    if awprb3 == 5:
        $ awprb3 -= 5
    if awprb3 == 6:
        $ awprb3 -= 6
    if awprb4 == 1:
        $ awprb4 -= 1
    if awprb4 == 2:
        $ awprb4 -= 2
    if awprb4 == 3:
        $ awprb4 -= 3
    if awprb4 == 4:
        $ awprb4 -= 4
    if awprb4 == 5:
        $ awprb4 -= 5
    if awprb4 == 6:
        $ awprb4 -= 6
    if awprt1n == 0:
        $ awprt1n += 1
    if awprt2n == 1:
        $ awprt2n -= 1
    if awprt3n == 1:
        $ awprt3n -= 1
    if awprt4n == 1:
        $ awprt4n -= 1
    jump aw_km_pr_r
    
label aw_pa_r_t_open:
    $ renpy.block_rollback()
    play sound aw_m_click
    scene bg aw_km_dadr_bg with dissolve
    play sound2 aw_table_op
    $ renpy.pause(1.1, hard=True)
    $ awkmpt += 1
    play sound aw_takemetalsmall
    show aw_km_mrkey with dspr
    $ renpy.pause(1.1, hard=True)
    hide aw_km_mrkey with dspr
    jump aw_km_pr_r

    #MR
label aw_km_mr_int:
    $ renpy.block_rollback()
    play sound aw_door_o_2
    scene black with fade3
label aw_km_mr_cheker:
    $ renpy.block_rollback()
    if awkmmriu == 1:
        jump aw_km_mr_safe_op
    if awkmmrphoto == 1:
        jump aw_km_mr_fall_ph
    scene bg aw_km_mroom_bg1 with dissolve
    call screen aw_km_mr_all_scr with dissolve


label aw_km_mr_safe_op:
    $ renpy.block_rollback()
    scene bg aw_km_mroom_opd_bg with dissolve
    call screen aw_km_mr_safeop_scr with dissolve

label aw_km_mr_fall_ph:
    $ renpy.block_rollback()
    scene bg aw_km_mroom_bg2 with dissolve
    call screen aw_km_mr_nph1_scr with dissolve


label aw_km_mmr_phtip:
    $ renpy.block_rollback()
    show aw_km_mr_pht with dissolve
    $ renpy.pause(6, hard=True)
    scene black with fade2
    jump aw_km_mr_cheker

label aw_km_mr_chk_ph:
    $ renpy.block_rollback()
    $ awkmmrphoto += 1
    play sound aw_glass_break_2
    scene bg aw_km_mroom_bg2 at aw_master_tryas
    $ renpy.pause(0.7, hard=True)
    call screen aw_km_mr_nph1_scr with dissolve

label aw_km_mr_safe_ch:
    $ renpy.block_rollback()
    show aw_km_safe_bg
    menu:
        "Ввести правильный код":
            jump aw_km_mr_safe_open
        "Ввести самому":
            call screen aw_km_mr_safe_scr
            with dissolve

label aw_km_mr_safe_b2_r:
    $ renpy.block_rollback()
    $ awkmmrsb += 1
    jump aw_km_mr_safe_b2

label aw_km_mr_safe_b3_r:
    $ renpy.block_rollback()
    $ awkmmrsb += 1
    jump aw_km_mr_safe_b3

label aw_km_mr_safe_b4_r:
    $ renpy.block_rollback()
    $ awkmmrsb += 1
    jump aw_km_mr_safe_b4

label aw_km_mr_safe_r:
    $ renpy.block_rollback()
    $ awkmmrsb += 1
    jump aw_km_mr_safe_chek_b

label aw_km_mr_safe_chek_b:
    $ renpy.block_rollback()
    play sound aw_buton_2
    if awkmmrsb == 4:
        jump aw_km_mr_safe_open
    if awkmmrsb == 1:
        $ awkmmrsb -= 1
    if awkmmrsb == 2:
        $ awkmmrsb -= 2
    if awkmmrsb == 3:
        $ awkmmrsb -= 3
    jump aw_km_mr_safe_ch
    

label aw_km_mr_cant_opsf:
    $ renpy.block_rollback()
    if awkmmrsb == 1:
        $ awkmmrsb -= 1
    if awkmmrsb == 2:
        $ awkmmrsb -= 2
    if awkmmrsb == 3:
        $ awkmmrsb -= 3
    jump aw_km_mr_cheker

label aw_km_mr_safe_open:
    $ renpy.block_rollback()
    play sound aw_mist_1
    stop music fadeout 1
    show aw_km_safe_open with awrain2
    $ renpy.pause(1.5, hard=True)
    scene bg aw_km_mroom_bg2 with fade2
    play sound aw_mist_2
    scene bg aw_km_mroom_opd_bg with awrain
    $ renpy.pause(1.5, hard=True)
    $ awkmmriu += 1
    scene bg aw_km_mroom_opd_bg with fade2
    jump aw_km_mr_cheker

label aw_km_mr_door_ch:
    $ renpy.block_rollback()
    if awkmpt == 1:
        jump aw_km_mom_room
    play sound aw_latchlocked2
    aw_gg_hide "Закрыто..." with dissolve2
    window hide
    jump aw_km_mr_cheker

label aw_km_mom_room:
    $ renpy.block_rollback()
    play sound aw_latch_unlocked
    $ renpy.pause(0.8, hard=True)
    play sound2 aw_door_o_2
    stop music fadeout 3
    scene black with dissolve4
    $ renpy.pause(1.8, hard=True)
    play music aw_is_that fadein 3
    show aw_km_stars with dissolve
    $ renpy.pause(2.8, hard=True)
    show aw_kn_bear behind aw_km_stars with dissolve
    $ renpy.pause(0.8, hard=True)
    play sound aw_bear_snd_5
    $ renpy.pause(5, hard=True)
    play sound aw_psy_eff_2
    stop music
    scene black
    $ renpy.pause(3, hard=True)
    play music aw_possessed_room
    show aw_pe1
    $ renpy.pause(3, hard=True)
    show aw_kn_bear_p1 behind aw_pe1 with dissolve
    $ renpy.pause(1, hard=True)
    show aw_km_susuk_1 behind aw_pe1 with dissolve 
    call screen aw_km_susuk_scr1 with dissolve

label aw_km_susk_l:
    $ renpy.block_rollback()
    play sound aw_bear_snd_2
    play music aw_mask_save
    scene bg aw_km_mondead_1
    show overlay aw_memory_back_2
    $ Aw_Alko("bg aw_km_mondead_1")
    $ renpy.pause(0.5, hard=True)
    scene black
    show overlay aw_pe1
    show aw_kn_bear_p1
    show aw_ig_int_1
    show aw_km_susuk_2
    with flash_fast2
    call screen aw_km_susuk_scr2 with dissolve

label aw_km_susk_l2:
    $ renpy.block_rollback()
    play sound aw_bear_snd_1
    play music aw_infected
    scene bg aw_km_mondead_2
    show overlay aw_memory_back_2
    $ Aw_Alko("bg aw_km_mondead_2")
    $ renpy.pause(0.5, hard=True)
    scene black
    show overlay aw_pe1
    show aw_kn_bear_p1
    show aw_ig_int_1
    show aw_ig_int_2
    show aw_km_susuk_3
    with flash_fast2
    call screen aw_km_susuk_scr3 with dissolve

label aw_km_susk_l3:
    $ renpy.block_rollback()
    play sound aw_bear_snd_1
    play music aw_stage2
    scene bg aw_km_mondead_3
    show overlay aw_memory_back_2
    $ Aw_Alko("bg aw_km_mondead_3")
    $ renpy.pause(0.5, hard=True)
    scene black
    show overlay aw_pe1
    show aw_kn_bear_p1
    show aw_ig_int_1
    show aw_ig_int_2
    show aw_ig_int_3
    show aw_km_susuk_4
    with flash_fast2
    call screen aw_km_susuk_scr4 with dissolve


label aw_km_susk_l4:
    $ renpy.block_rollback()
    play sound2 aw_bear_snd_1
    play sound aw_cashback
    stop music 
    scene bg aw_km_mondead_4
    show overlay aw_memory_back_2
    $ Aw_Alko("bg aw_km_mondead_4")
    $ renpy.pause(0.5, hard=True)
    scene black
    show overlay aw_pe1
    show aw_kn_bear_p1
    show aw_ig_int_1
    show aw_ig_int_2
    show aw_ig_int_3
    show aw_ig_int_4
    show aw_km_susuk_5
    with flash_fast2
    call screen aw_km_susuk_scr5 with dissolve

label aw_km_susk_l5:
    $ renpy.block_rollback()
    play sound2 aw_bear_snd_4
    scene bg aw_km_mondead_5
    show overlay aw_memory_back_2
    with flash_fast2
    $ Aw_Alko("bg aw_km_mondead_5")
    stop sound fadeout 3
    $ renpy.pause(1.5, hard=True)
    play music away_intorial_full
    scene bg aw_km_mondead_5
    show aw_memory_back_1_no
    show overlay aw_memory_back_1
    with dissolve2
    $ Aw_Alko("bg aw_km_mondead_5")
    $ renpy.pause(1.5, hard=True)
    aw_gg_hide "Мамуля играла с иголочками" with dissolve2
    aw_gg_hide "И уснула, запачкав простыни"
    aw_gg_hide "Вокруг нее витают мушки"
    aw_gg_hide "Жужжат и кусают ее синие ручки"
    aw_gg_hide "Хочется кушать. Хоть хлеба корочку"
    aw_gg_hide "Но я счастлива, смотря на мамочку сонную"
    aw_gg_hide "Примерно семь дней она отсыпается"
    aw_gg_hide "Плохо пахнет, но не ругается"
    aw_gg_hide "Мамуля уснула, запачкав простыни" with dissolve
    aw_gg_hide "И больше не играет в иголочки" with dissolve2
    window hide
    $ renpy.pause(4, hard=True)
    stop music fadeout 5
    scene black with dissolve4
    $ renpy.pause(6, hard=True)
    jump aw_km_end
    
    
    
    




















