define e = Character('Эйлин', color="#c8ffc8")

label splashscreen:
    scene black with dissolve2
    $ renpy.pause(1, hard=True)
    play music aw_amb01_l fadein 3
    $ renpy.pause(2, hard=True)
    scene bg aw_warn_bg with dissolve4
    $ renpy.pause(1, hard=True)
    show aw_warn_2 with awrain
    $ renpy.pause(8, hard=True)
    call screen aw_warning_mess with dissolve2
label aw_begining_play:
    show aw_warn_1
    hide aw_warn_2
    with awrain2
    $ renpy.pause(8, hard=True)
    stop ambience fadeout 3
    scene black with dissolve4
    $ renpy.pause(1, hard=True)
    play sound aw_launch_snd
    scene bg aw_snddis with dissolve2
    $ renpy.pause(6, hard=True)
    stop sound fadeout 3
    scene black with fade3
    $ renpy.pause(2, hard=True)
    play sound2 aw_steps_wood_1
    $ renpy.pause(3, hard=True)
    play sound aw_r_creak
    $ renpy.pause(1, hard=True)
    scene bg aw_r_int_bg_1 with dissolve2
    $ renpy.pause(1.5, hard=True)
    play sound2 aw_wood_floor_creak
    scene bg aw_r_int_bg_2 with dissolve
    $ renpy.pause(1, hard=True)
    play sound aw_r_vine
    scene bg aw_r_int_bg_3 with dissolve2
    $ renpy.pause(1, hard=True)
    stop sound fadeout 3
    scene black
    show aw_r_tv_log
    with fade3
    $ renpy.pause(1, hard=True)
    play sound2 aw_buton_1
    play sound aw_tv_noise
    stop music fadeout 2
    show overlay aw_pe1 behind aw_r_tv_log
    $ renpy.pause(2, hard=True)
    play music aw_foolow_the_reditus fadein 3
    stop sound fadeout 2
    $ renpy.pause(1, hard=True)
    play sound aw_tv_noise_2
    scene black
    show aw_r_tv_log
    show aw_r_ges_spl behind aw_r_tv_log
    show overlay aw_memory_back_1 behind aw_r_tv_log
    with dissolve2
    $ renpy.pause(6, hard=True)
    stop sound fadeout 3
    scene bg aw_bg with flash_fast2
    $ renpy.pause(1.5, hard=True)
    scene black with awspot
    $ renpy.pause(1, hard=True)
    show aw_mm_bg_v
    show overlay aw_memory_back_1
    with dissolve4
    $ renpy.pause(2.5, hard=True)
    show aw_mmn with dissolve2
    $ renpy.pause(1.5, hard=True)
    return

    scene bg aw_ges_logo_bg with dissolve2
    $ renpy.pause(1, hard=True)
    play sound aw_steps_wood_1
    $ renpy.pause(3.9, hard=True)
    play sound aw_tv_noise
    show aw_ges_logo_gl
    show overlay aw_memory_back_1
    show aw_ges_logo_fp
    with dissolve
    $ renpy.pause(2.5, hard=True)
    stop sound fadeout 4
label splashscreen_2:
    scene black with fade3
    $ renpy.pause(1, hard=True)
    play music away_intorial_full
    scene bg aw_mm_bg1
    show overlay aw_memory_back_1
    with dissolve4
    $ renpy.pause(1.5, hard=True)
    show aw_mmn with dissolve2
    $ renpy.pause(0.7, hard=True)
    return



label start:
    show overlay aw_memory_back_1
    with dissolve2
    $ renpy.pause(0.3, hard=True)
    stop music fadeout 3
    scene black with dissolve4
    $ renpy.pause(1.5, hard=True)
    jump away
