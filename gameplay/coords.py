#side: 1280x720* | 1920x1080
#large: 1920x1080*

coords = {
    "side": {
        #craft_rage
        "craft_button": (-1109, 425),
        "temporary_craft": (-1020, 1020),
        "down_scroll": (-804, 928),
        "craft_rage_pill": (-881, 668),
        "rage_button": (-186, 444), #rage
        "exit_menu": (-831, 1013),

        #dash
        "dash_end": (-1171, 935),
        "dash_button": (-1160, 935),

        #claim_divinities
        "ascension_tab": (-1188, 445),
        "close_ascension": (-688, 1009),
        "minions_tab": (-928, 1006),
        "skilltree_tab": (-1043, 1006),
        "send_minions": (-973, 505),
        "daily": (-1197, 635),
        "send_minions2": (-1185, 752),

        #special_stage_start
        "B": (-772, 496),
        "divinities": (-1187, 440),

        #special_stage_close
        "close_run": (-532, 913),
        "man": (-644, 598),

        #activate_silver_boxes
        "activate_boxes": (-701, 378),

        #organise_levels
        "shop_button": (-81, 1011),
        "weapon_button": (-421, 1018),
        "fifty_button": (-170, 955),
        "bottom_scroll_button": (-35, 918),
        "max_button": (-83, 955),
        "upgrade_button": (-352, 1014)
    },
    "large": {
        #craft_rage
        "craft_button": (256, 104),
        "temporary_craft": (390, 997),
        "down_scroll": (715, 860),
        "craft_rage_pill": (600, 453),
        "rage_button": (1641, 127), #rage
        "exit_menu": (660, 995),

        #dash
        "dash_end": (167, 862),
        "dash_button": (177, 871),

        #claim_divinities
        "ascension_tab": (134, 132),
        "close_ascension": (884, 985),
        "minions_tab": (524, 973),
        "skilltree_tab": (355, 975),
        "send_minions": (486, 228),
        "daily": (488, 211),
        "send_minions2": (485, 359),

        #special_stage_start
        "B": (763, 199),
        "divinities": (140, 102),

        #special_stage_close
        "close_run": (1123, 833),
        "man": (959, 371),

        #activate_silver_boxes
        "activate_boxes": (870, 27),

        #organise_levels
        "shop_button": (1798, 976),
        "weapon_button": (1284, 984),
        "fifty_button": (1669, 889),
        "bottom_scroll_button": (1864, 848),
        "max_button": (1801, 901),
        "upgrade_button": (1396, 987)
    }
}

def coords_iter_from_names(screen, names_iter):
    return [(coords[screen][name], sleeptime) for name, sleeptime in names_iter]
