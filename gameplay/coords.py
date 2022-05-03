#side: 1280x720* | 1920x1080
#large: 1920x1080*

coords = {
    "side": {
        #craft_rage
        "craft_button": (-1109, 425),
        "temporary_craft": (-1020, 1020),
        "down_scroll": (-804, 928),
        "craft_rage_pill": (-881, 668),
        "rage_button": (-185, 450),
        "exit_menu": (-831, 1013),

        #dash
        "dash_end": (-1171, 935),
        "dash_button": (-1160, 935),

        #claim divinities
        "ascension_tab": (-1188, 445),
        "close_ascension": (-688, 1009),
        "minions_tab": (-928, 1006),
        "skilltree_tab": (-1043, 1006),
        "send_minions": (-973, 505),
        "daily": (-1197, 635),
        "send_minions2": (-1185, 752)
    },
    "large": {
        #craft_rage
        "craft_button": (256, 104),
        "temporary_craft": (390, 997),
        "down_scroll": (715, 860),
        "craft_rage_pill": (600, 453),
        "rage_button": (1644, 177),
        "exit_menu": (660, 995),

        #dash
        "dash_end": (167, 862),
        "dash_button": (177, 871),

        #claim divinities
        "ascension_tab": (134, 132),
        "close_ascension": (884, 985),
        "minions_tab": (524, 973),
        "skilltree_tab": (355, 975),
        "send_minions": (486, 228),
        "daily": (488, 211),
        "send_minions2": (485, 359)
    }
}

def coords_iter_from_names(screen, names_iter):
    return [(coords[screen][name], sleeptime) for name, sleeptime in names_iter]
