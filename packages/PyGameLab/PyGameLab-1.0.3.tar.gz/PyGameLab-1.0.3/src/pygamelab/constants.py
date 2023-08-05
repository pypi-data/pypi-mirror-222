import pygame

pygame.init()

TOP = "_tp/"
MIDDLE = "_md/"
BOTTOM = "_bt/"
LEFT = "_lt/"
CENTER = "_ct/"
RIGHT = "_rg/"


TOPCENTER = (CENTER, TOP)
TOPLEFT = (LEFT, TOP)
TOPRIGHT = (RIGHT, TOP)
MIDDLECENTER = (CENTER, MIDDLE)
MIDDLELEFT = (LEFT, MIDDLE)
MIDDLERIGHT = (RIGHT, MIDDLE)
BOTTOMCENTER = (CENTER, BOTTOM)
BOTTOMLEFT = (LEFT, BOTTOM)
BOTTOMRIGHT = (RIGHT, BOTTOM)


class keys:
    @staticmethod
    def get_pressed():
        key_names = {getattr(pygame, f"K_{key}"): key for key in dir(pygame) if key.startswith("K_")}
        ky = pygame.key.get_pressed()
        keys_pressed = {}
        for key_code, key_name in key_names.items():
            keys_pressed[key_name] = ky[key_code]
        return keys_pressed