# characters


class CharacterError(Exception):
    pass


class Character(object):
    """Manages characters"""
    
    HEALTH_STYLE_LAMBDA = 0
    HEALTH_STYLE_PC = 1
    
    def __init__(self, **kwargs):
        """boop"""
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('id', None)
        self.earth = kwargs.get('earth', None)  #health calculation
        self.init = kwargs.get('init', None)
        self.description = kwargs.get('description', None)
        self.health_style = kwargs.get('health_style',
                                       Character.HEALTH_STYLE_PC)
        self.wounds = kwargs.get('wounds', 0)
    
    def compute_max_wounds(self):
        if self.health_style == Character.HEALTH_STYLE_LAMBDA:
            self.max_wounds = 10 * self.earth
        elif self.health_style == Character.HEALTH_STYLE_PC:
            self.max_wounds = 19 * self.earth
        else:
            raise CharacterError("Je ne peux pas calculer ça!")


class PlayerCharacter(Character):
    """ Only for players """