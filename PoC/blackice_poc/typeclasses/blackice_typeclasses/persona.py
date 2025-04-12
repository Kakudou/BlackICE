from evennia import DefaultCharacter

class Persona(DefaultCharacter):

    def at_cmdset_get(self, **kwargs):
        pass


    def at_first_login(self):
        pass

    def at_post_login(self):
        pass

    def at_disconnect(self):
        pass

    def at_object_creation(self):
        pass

