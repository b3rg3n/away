init:

    $ aw_gg_hide = Character(u'...', color="#666666", what_color="c8c8c8",what_outlines=[ (1, "#000000") ]) 

#START
screen aw_warning_mess:
    tag aw_r1 
    modal True
    imagemap:
        ground "away/img/scr/aw_warn_h_n.png" 
        hover "away/img/scr/aw_warn_h_y.png" 
        alpha True
        hotspot (0, 918, 343, 162) action Quit(confirm=not main_menu)
        hotspot (1306, 953, 614, 127) clicked[Jump("aw_begining_play")]

#ROOM1_STAGE2
screen aw_r1_s2_scr:
    tag aw_r1 
    modal True
    imagemap:
        ground "away/img/scr/aw_r1_h_s2_n.png" 
        hover "away/img/scr/aw_r1_h_s2_y.png" 
        alpha True
        hotspot (854, 717, 75, 39) clicked[Jump("aw_r1_b1_chek")]
        hotspot (868, 808, 73, 42) clicked[Jump("aw_r1_b2_chek")]
        hotspot (882, 850, 94, 80) clicked[Jump("aw_r1_b3_chek")]
        hotspot (1137, 617, 93, 80) clicked[Jump("aw_r1_pc_chek")]
        hotspot (1265, 611, 104, 101) clicked[Jump("aw_r1_b4_chek")]
        hotspot (1167, 776, 99, 55) clicked[Jump("aw_r1_lock_box_chek")]
        hotspot (0, 950, 75, 130) clicked[Jump("aw_r2_chek")]


#ROOM1_STAGE1_1
screen aw_r1_s1_1_scr:
    tag aw_r1 
    modal True
    imagemap: 
        ground "away/img/scr/aw_r1_h_s11_n.png" 
        hover "away/img/scr/aw_r1_h_s11_y.png" 
        alpha True
        hotspot (854, 717, 75, 39) clicked[Jump("aw_r1_b1_chek")]
        hotspot (868, 808, 73, 42) clicked[Jump("aw_r1_b2_chek")]
        hotspot (882, 850, 94, 80) clicked[Jump("aw_r1_b3_chek")]
        hotspot (1101, 535, 44, 74) clicked[Jump("aw_r1_lamp_chek")]
        hotspot (1137, 617, 93, 80) clicked[Jump("aw_r1_pc_chek")]
        hotspot (1265, 611, 104, 101) clicked[Jump("aw_r1_b4_chek")]
        hotspot (1167, 776, 99, 55) clicked[Jump("aw_r1_lock_box_chek")]
        hotspot (1166, 852, 99, 125) clicked[Jump("aw_r1_box_chek")]
        hotspot (0, 950, 75, 130) clicked[Jump("aw_r2_chek")]


#ROOM1_STAGE1_2
screen aw_r1_s1_2_scr:
    tag aw_r1 
    modal True
    imagemap: 
        ground "away/img/scr/aw_r1_h_s12_n.png" 
        hover "away/img/scr/aw_r1_h_s12_y.png" 
        alpha True
        hotspot (753, 846, 106, 133) clicked[Jump("aw_r1_buk_chek")]
        hotspot (854, 717, 75, 39) clicked[Jump("aw_r1_b1_chek")]
        hotspot (868, 808, 73, 42) clicked[Jump("aw_r1_b2_chek")]
        hotspot (882, 850, 94, 80) clicked[Jump("aw_r1_b3_chek")]
        hotspot (1137, 617, 93, 80) clicked[Jump("aw_r1_pc_chek")]
        hotspot (1265, 611, 104, 101) clicked[Jump("aw_r1_b4_chek")]
        hotspot (1167, 776, 99, 55) clicked[Jump("aw_r1_lock_box_chek")]
        hotspot (1543, 681, 150, 151) clicked[Jump("aw_r1_tv_chek")]
        hotspot (0, 950, 75, 130) clicked[Jump("aw_r2_chek")]

#ROOM1_F_STAGE2
screen aw_r1_f_s2_scr:
    tag aw_r1 
    modal True
    imagemap:
        ground "away/img/scr/aw_r1_f_h_s2_n.png" 
        hover "away/img/scr/aw_r1_f_h_s2_y.png" 
        alpha True
        hotspot (854, 717, 75, 39) clicked[Jump("aw_r1_b1_chek")]
        hotspot (868, 808, 73, 42) clicked[Jump("aw_r1_b2_chek")]
        hotspot (882, 850, 94, 80) clicked[Jump("aw_r1_b3_chek")]
        hotspot (1137, 617, 93, 80) clicked[Jump("aw_r1_pc_chek")]
        hotspot (1265, 611, 104, 101) clicked[Jump("aw_r1_b4_chek")]
        hotspot (1167, 776, 99, 55) clicked[Jump("aw_r1_lock_box_chek")]
        hotspot (0, 950, 150, 130) clicked[Jump("aw_r2_chek")]


#ROOM1_F_STAGE1_1
screen aw_r1_f_s1_1_scr:
    tag aw_r1 
    modal True
    imagemap: 
        ground "away/img/scr/aw_r1_f_h_s11_n.png" 
        hover "away/img/scr/aw_r1_f_h_s11_y.png" 
        alpha True
        hotspot (854, 717, 75, 39) clicked[Jump("aw_r1_b1_chek")]
        hotspot (868, 808, 73, 42) clicked[Jump("aw_r1_b2_chek")]
        hotspot (882, 850, 94, 80) clicked[Jump("aw_r1_b3_chek")]
        hotspot (1101, 535, 44, 74) clicked[Jump("aw_r1_lamp_chek")]
        hotspot (1137, 617, 93, 80) clicked[Jump("aw_r1_pc_chek")]
        hotspot (1265, 611, 104, 101) clicked[Jump("aw_r1_b4_chek")]
        hotspot (1167, 776, 99, 55) clicked[Jump("aw_r1_lock_box_chek")]
        hotspot (1166, 852, 99, 125) clicked[Jump("aw_r1_box_chek")]
        hotspot (0, 950, 150, 130) clicked[Jump("aw_r2_chek")]


#ROOM1_F_STAGE1_2
screen aw_r1_f_s1_2_scr:
    tag aw_r1 
    modal True
    imagemap: 
        ground "away/img/scr/aw_r1_f_h_s12_n.png" 
        hover "away/img/scr/aw_r1_f_h_s12_y.png" 
        alpha True
        hotspot (753, 846, 106, 133) clicked[Jump("aw_r1_buk_chek")]
        hotspot (854, 717, 75, 39) clicked[Jump("aw_r1_b1_chek")]
        hotspot (868, 808, 73, 42) clicked[Jump("aw_r1_b2_chek")]
        hotspot (882, 850, 94, 80) clicked[Jump("aw_r1_b3_chek")]
        hotspot (1137, 617, 93, 80) clicked[Jump("aw_r1_pc_chek")]
        hotspot (1265, 611, 104, 101) clicked[Jump("aw_r1_b4_chek")]
        hotspot (1167, 776, 99, 55) clicked[Jump("aw_r1_lock_box_chek")]
        hotspot (1543, 681, 150, 151) clicked[Jump("aw_r1_tv_chek")]
        hotspot (0, 950, 150, 130) clicked[Jump("aw_r2_chek_ent")]


#PC_R1

screen aw_r1_pc_desctop_scr:
    tag aw_pc1 
    modal True
    imagemap: 
        ground "away/img/scr/aw_r1_pc_desc_h_n.png" 
        hover "away/img/scr/aw_r1_pc_desc_h_y.png" 
        alpha True
        hotspot (260, 85, 79, 115) clicked[Jump("aw_r1_pc_gamefolder")]
        hotspot (367, 85, 79, 115) clicked[Jump("aw_r1_pc_docfolder")]
        hotspot (470, 85, 79, 115) clicked[Jump("aw_r1_pc_musicfolder")]
        hotspot (574, 85, 79, 115) clicked[Jump("aw_r1_pc_imgfolder")]
        hotspot (342, 952, 32, 36) clicked[Jump("aw_r1_pc_internet")]

screen aw_r1_pc_musfold:
    tag aw_pc1 
    modal True
    imagemap: 
        ground "away/img/scr/aw_r1_pc_mh_n.png" 
        hover "away/img/scr/aw_r1_pc_mh_y.png" 
        alpha True
        hotspot (498,199,597,31) clicked[Play('music',"away/snd/mp3/aw_mnd_ost.mp3")]
        hotspot (1572, 81, 30, 21) clicked[Jump("aw_pc_hide_mus_f")]

#ROOM2

screen aw_r2_scr_all:
    tag aw_r2
    modal True
    imagemap:
        ground "away/img/scr/aw_r2_scr_h_n.png" 
        hover "away/img/scr/aw_r2_scr_h_y.png" 
        alpha True
        hotspot (0, 0, 309, 1080) clicked[Jump("aw_r2_s1_chek")]
        hotspot (456, 0, 144, 1080) clicked[Jump("aw_r2_s2_chek")]
        hotspot (1045, 218, 224, 526) clicked[Jump("aw_r2_ed_chek")]
        hotspot (1841, 1011, 79, 69) clicked[Jump("aw_r2_r1_chek")]

screen aw_r2_clotch_no:
    tag aw_r2
    modal True
    imagemap:
        ground "away/img/scr/aw_r2_nc_scr_h_n.png" 
        hover "away/img/scr/aw_r2_nc_scr_h_y.png" 
        alpha True
        hotspot (0, 0, 309, 1080) clicked[Jump("aw_r2_s1_chek")]
        hotspot (1045, 218, 224, 526) clicked[Jump("aw_r2_ed_chek")]
        hotspot (1841, 1011, 79, 69) clicked[Jump("aw_r2_r1_chek")]

screen aw_r2_shkaf_only:
    tag aw_r2
    modal True
    imagemap:
        ground "away/img/scr/aw_r2_lo_scr_h_n.png" 
        hover "away/img/scr/aw_r2_lo_scr_h_y.png" 
        alpha True
        hotspot (0, 0, 309, 1080) clicked[Jump("aw_r2_s1_chek")]
        hotspot (1841, 1011, 79, 69) clicked[Jump("aw_r2_r1_chek")]

screen aw_r2_shk_onl_scr:
    tag aw_r2
    modal True
    imagemap:
        ground "away/img/scr/aw_r2_lo_scr_h_n.png" 
        hover "away/img/scr/aw_r2_lo_scr_h_y.png" 
        alpha True
        hotspot (0, 0, 309, 1080) clicked[Jump("aw_r2_s1_chek")]
        hotspot (1841, 1011, 79, 69) clicked[Jump("aw_r2_r1_chek")]

screen aw_r2_scr_empty:
    tag aw_r2
    modal True
    imagemap:
        ground "away/img/scr/aw_r2_e_scr_h_n.png" 
        hover "away/img/scr/aw_r2_e_scr_h_y.png" 
        alpha True
        hotspot (1841, 1011, 79, 69) clicked[Jump("aw_r2_r1_chek")]

    #PC
screen aw_pc_msg_link_scr:
    tag aw_pcm
    modal True
    imagemap:
        ground "away/img/scr/aw_pc_msg_scrbg_hn.png" 
        hover "away/img/scr/aw_pc_msg_scrbg_hy.png" 
        alpha True
        hotspot (1558, 67, 45, 28) clicked[Jump ("aw_r1_cheker")]
        hotspot (738, 810, 59, 15) clicked[OpenURL("https://colorscheme.ru/html-colors.html")]


    #KID MEMORY

screen aw_km_mc_scr:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_kor_hn.png" 
        hover "away/img/scr/aw_km_kor_hy.png" 
        alpha True
        hotspot (342, 7, 236, 1072) clicked[Jump("aw_km_pr_cheker")]
        hotspot (1121, 509, 70, 653) clicked[Jump("aw_km_mr_int")]


screen aw_pa_r_scr:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_pa_r_hn.png" 
        hover "away/img/scr/aw_pa_r_hy.png" 
        alpha True
        hotspot (1377, 624, 46, 29) clicked[Jump("aw_pa_r_t_ch")]
        hotspot (1568, 883, 113, 83) clicked[Jump("aw_pa_r_ba_l_ch")]
        hotspot (1694, 923, 132, 83) clicked[Jump("aw_pa_r_pas_l")]
        hotspot (0, 950, 137, 130) clicked[Jump("aw_km_cor_1_ch")]

screen aw_pa_r_nt_scr:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_pa_r_to_hn.png" 
        hover "away/img/scr/aw_pa_r_to_hy.png" 
        alpha True
        hotspot (1568, 883, 113, 83) clicked[Jump("aw_pa_r_ba_l_ch")]
        hotspot (1694, 923, 132, 83) clicked[Jump("aw_pa_r_pas_l")]
        hotspot (0, 950, 137, 130) clicked[Jump("aw_km_cor_1_ch")]

screen aw_pa_r_tl_scr:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_prt_hn.png" 
        hover "away/img/scr/aw_km_prt_hy.png" 
        alpha True
        hotspot (825, 523, 53, 45) clicked[Jump("aw_km_pr_b1_ch")]
        hotspot (913, 523, 53, 45) clicked[Jump("aw_km_pr_b2_ch")]
        hotspot (1001, 523, 53, 45) clicked[Jump("aw_km_pr_b3_ch")]
        hotspot (1099, 523, 53, 45) clicked[Jump("aw_km_pr_b4_ch")]
        hotspot (0, 950, 137, 130) clicked[Jump("aw_km_pr_t_chl")]


screen aw_km_mr_all_scr:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_mroom_hn.png" 
        hover "away/img/scr/aw_km_mroom_hy.png" 
        alpha True
        hotspot (489, 413, 161, 122) clicked[Jump("aw_km_mr_chk_ph")]
        hotspot (689, 413, 161, 122) clicked[Jump("aw_km_mmr_phtip")]
        hotspot (0, 950, 137, 130) clicked[Jump("aw_km_cor_1_ch")]

screen aw_km_mr_safeop_scr:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_mroom_so_nh.png" 
        hover "away/img/scr/aw_km_mroom_so_yh.png" 
        alpha True
        hotspot (1065, 175, 362, 794) clicked[Jump("aw_km_mr_door_ch")]
        hotspot (689, 413, 161, 122) clicked[Jump("aw_km_mmr_phtip")]
        hotspot (0, 950, 137, 130) clicked[Jump("aw_km_cor_1_ch")]

screen aw_km_mr_nph1_scr:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_mroom_np_hn.png" 
        hover "away/img/scr/aw_km_mroom_np_hy.png" 
        alpha True
        hotspot (489, 413, 161, 122) clicked[Jump("aw_km_mr_safe_ch")]
        hotspot (689, 413, 161, 122) clicked[Jump("aw_km_mmr_phtip")]
        hotspot (0, 950, 137, 130) clicked[Jump("aw_km_cor_1_ch")]


screen aw_km_mr_safe_scr:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_safe_h_n.png" 
        hover "away/img/scr/aw_km_safe_h_y.png" 
        alpha True
        hotspot (497, 501, 42, 109) clicked[Jump("aw_km_mr_safe_b2")]
        hotspot (561, 501, 71, 109) clicked[Jump("aw_km_mr_safe_b2")]
        hotspot (654, 501, 67, 109) clicked[Jump("aw_km_mr_safe_b2_r")]
        hotspot (748, 501, 70, 109) clicked[Jump("aw_km_mr_safe_b2")]
        hotspot (847, 501, 69, 109) clicked[Jump("aw_km_mr_safe_b2")]
        hotspot (941, 480, 61, 129) clicked[Jump("aw_km_mr_safe_b2")]
        hotspot (1033, 501, 62, 109) clicked[Jump("aw_km_mr_safe_b2")]
        hotspot (1115, 501, 60, 109) clicked[Jump("aw_km_mr_safe_b2")]
        hotspot (1212, 501, 61, 109) clicked[Jump("aw_km_mr_safe_b2")]
        hotspot (1308, 501, 67, 109) clicked[Jump("aw_km_mr_safe_b2")]
        hotspot (0, 950, 137, 130) clicked[Jump("aw_km_mr_cant_opsf")]

label aw_km_mr_safe_b2:
    play sound aw_buton_2
    call screen aw_km_mr_safe_scr2
screen aw_km_mr_safe_scr2:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_safe_h_n.png" 
        hover "away/img/scr/aw_km_safe_h_y.png" 
        alpha True
        hotspot (497, 501, 42, 109) clicked[Jump("aw_km_mr_safe_b3")]
        hotspot (561, 501, 71, 109) clicked[Jump("aw_km_mr_safe_b3")]
        hotspot (654, 501, 67, 109) clicked[Jump("aw_km_mr_safe_b3")]
        hotspot (748, 501, 70, 109) clicked[Jump("aw_km_mr_safe_b3")]
        hotspot (847, 501, 69, 109) clicked[Jump("aw_km_mr_safe_b3")]
        hotspot (941, 480, 61, 129) clicked[Jump("aw_km_mr_safe_b3")]
        hotspot (1033, 501, 62, 109) clicked[Jump("aw_km_mr_safe_b3")]
        hotspot (1115, 501, 60, 109) clicked[Jump("aw_km_mr_safe_b3")]
        hotspot (1212, 501, 61, 109) clicked[Jump("aw_km_mr_safe_b3")]
        hotspot (1308, 501, 67, 109) clicked[Jump("aw_km_mr_safe_b3_r")]
        hotspot (0, 950, 137, 130) clicked[Jump("aw_km_mr_cant_opsf")]

label aw_km_mr_safe_b3:
    play sound aw_buton_11
    call screen aw_km_mr_safe_scr3
screen aw_km_mr_safe_scr3:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_safe_h_n.png" 
        hover "away/img/scr/aw_km_safe_h_y.png" 
        alpha True
        hotspot (497, 501, 42, 109) clicked[Jump("aw_km_mr_safe_b4")]
        hotspot (561, 501, 71, 109) clicked[Jump("aw_km_mr_safe_b4")]
        hotspot (654, 501, 67, 109) clicked[Jump("aw_km_mr_safe_b4")]
        hotspot (748, 501, 70, 109) clicked[Jump("aw_km_mr_safe_b4_r")]
        hotspot (847, 501, 69, 109) clicked[Jump("aw_km_mr_safe_b4")]
        hotspot (941, 480, 61, 129) clicked[Jump("aw_km_mr_safe_b4")]
        hotspot (1033, 501, 62, 109) clicked[Jump("aw_km_mr_safe_b4")]
        hotspot (1115, 501, 60, 109) clicked[Jump("aw_km_mr_safe_b4")]
        hotspot (1212, 501, 61, 109) clicked[Jump("aw_km_mr_safe_b4")]
        hotspot (1308, 501, 67, 109) clicked[Jump("aw_km_mr_safe_b4")]
        hotspot (0, 950, 137, 130) clicked[Jump("aw_km_mr_cant_opsf")]

label aw_km_mr_safe_b4:
    play sound aw_buton_11
    call screen aw_km_mr_safe_scr4
screen aw_km_mr_safe_scr4:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_safe_h_n.png" 
        hover "away/img/scr/aw_km_safe_h_y.png" 
        alpha True
        hotspot (497, 501, 42, 109) clicked[Jump("aw_km_mr_safe_chek_b")]
        hotspot (561, 501, 71, 109) clicked[Jump("aw_km_mr_safe_chek_b")]
        hotspot (654, 501, 67, 109) clicked[Jump("aw_km_mr_safe_chek_b")]
        hotspot (748, 501, 70, 109) clicked[Jump("aw_km_mr_safe_chek_b")]
        hotspot (847, 501, 69, 109) clicked[Jump("aw_km_mr_safe_chek_b")]
        hotspot (941, 480, 61, 129) clicked[Jump("aw_km_mr_safe_chek_b")]
        hotspot (1033, 501, 62, 109) clicked[Jump("aw_km_mr_safe_r")]
        hotspot (1115, 501, 60, 109) clicked[Jump("aw_km_mr_safe_chek_b")]
        hotspot (1212, 501, 61, 109) clicked[Jump("aw_km_mr_safe_chek_b")]
        hotspot (1308, 501, 67, 109) clicked[Jump("aw_km_mr_safe_chek_b")]
        hotspot (0, 950, 137, 130) clicked[Jump("aw_km_mr_cant_opsf")]



screen aw_km_susuk_scr1:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_igscr_hn1.png" 
        hover "away/img/scr/aw_km_igscr_hy1.png" 
        alpha True
        hotspot (167, 216, 171, 209) clicked[Jump("aw_km_susk_l")]
        hotspot (312, 477, 165, 262) clicked[Jump("aw_km_susk_l")]
        hotspot (781, 80, 261, 160) clicked[Jump("aw_km_susk_l")]
        hotspot (1404, 100, 128, 277) clicked[Jump("aw_km_susk_l")]
        hotspot (1478, 568, 59, 298) clicked[Jump("aw_km_susk_l")]

screen aw_km_susuk_scr2:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_igscr_hn2.png" 
        hover "away/img/scr/aw_km_igscr_hy2.png" 
        alpha True
        hotspot (477,271,241,227) clicked[Jump("aw_km_susk_l2")]
        hotspot (466, 727, 241, 227) clicked[Jump("aw_km_susk_l2")]
        hotspot (1236, 297, 241, 227) clicked[Jump("aw_km_susk_l2")]
        hotspot (1151, 744, 241, 227) clicked[Jump("aw_km_susk_l2")]

screen aw_km_susuk_scr3:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_igscr_hn3.png" 
        hover "away/img/scr/aw_km_igscr_hy3.png" 
        alpha True
        hotspot (336, 619, 341, 32) clicked[Jump("aw_km_susk_l3")]
        hotspot (1232, 600, 341, 32) clicked[Jump("aw_km_susk_l3")]
        hotspot (927, 1, 347, 301) clicked[Jump("aw_km_susk_l3")]


screen aw_km_susuk_scr4:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_igscr_hn4.png" 
        hover "away/img/scr/aw_km_igscr_hy4.png" 
        alpha True
        hotspot (498, 476, 41, 304) clicked[Jump("aw_km_susk_l4")]
        hotspot (1305, 466, 41, 304) clicked[Jump("aw_km_susk_l4")]


screen aw_km_susuk_scr5:
    tag aw_km 
    modal True
    imagemap:
        ground "away/img/scr/aw_km_igscr_hn5.png" 
        hover "away/img/scr/aw_km_igscr_hy5.png" 
        alpha True
        hotspot (479, 240, 602, 37) clicked[Jump("aw_km_susk_l5")]



