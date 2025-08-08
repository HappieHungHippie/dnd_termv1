from character import Character
from messages import Messages

class CharCommand:
    def __init__(self, master):
        self.master = master
        self.char = Character(self.master)

    def process_tag(self, tag):
        *_, secondary, value = tag
        if secondary == 'abilities':
            if value:
                self.char.set_ability_scores(value)
            else:
                self.char.display_ability_scores()
        elif secondary == 'ac':
            self.char.display_armor_class()
        elif secondary == 'basics':
            if value:
                self.char.set_basics(value)
            else:
                self.char.display_basics()
        elif secondary == 'class':
            if value:
                self.char.set_class(value)
            else:
                self.char.display_class()
        elif secondary == 'clear':
            self.char.clear()
        elif secondary == 'display':
            self.char.display_character()
        elif secondary == 'init':
            self.char.display_initiative()
        elif secondary == 'hp':
            if value:
                self.char.set_hit_points(value)
            else:
                self.char.display_hit_points()
        elif secondary == 'level':
            if value:
                self.char.set_level(value)
            else:
                self.char.display_level()
        elif secondary == 'list':
            self.char.display_list()
        elif secondary == 'name':
            if value:
                self.char.set_name(value)
            else:
                self.char.display_name()
        elif secondary == 'prof':
            if value:
                self.char.set_proficient_skills(value=value)
            else:
                self.char.display_proficiency_bonus()
        elif secondary == 'race':
            if value:
                self.char.set_race(value)
            else:
                self.char.display_race()
        elif secondary == 'save':
            self.char.save()
        elif secondary == 'skills':
            if value:
                self.char.display_skills(value=value)
            else:
                self.char.display_skills()

        elif secondary in self.char.ability_scores:
            if value:
                self.char.set_ability_score(secondary, value)
            else:
                self.char.display_ability_score(secondary)
        elif secondary in self.char.skills:
            self.char.display_skill(secondary)
        else:
            self.master.display_entry(f'{Messages.invalid_secondary}: {secondary}')
