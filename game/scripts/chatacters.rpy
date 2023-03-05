init python:

    #Упрощенная регестрация персонажей
    def reg_char(id, name, who_color, what_color = "#fff", pref = "", suf = ""):
        global Character
        gl = globals()
        
        gl[id] = Character( name, color=who_color, what_color=what_color, drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000", what_prefix=pref, what_suffix=suf )

    #Новые персонажи
    reg_char("th", '', "#18FFEB", pref="~", suf="~")