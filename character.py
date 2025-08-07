import json
from pathlib import Path
from messages import Messages
from .classes import Class
from file_handler import FileHandler


class Character:
    def __init__(self, master):
        self.master = master      
        self.class_handler = Class()
        self.file_handler = FileHandler

        self.name: str = None
        self.hit_points: int = None
        self.class_hit_points: int = None
        self.level: int = None
        self._class: str = None
        self.race: str = None

        self.armor_class: int = None
        self.initiative: int = None
        self.proficiency_bonus = None

        self.ability_scores: dict[str, int] = {
            'strength': None,
            'dexterity': None,
            'constitution': None,
            'intelligence': None,
            'wisdom': None,
            'charisma': None
        }

        self.ability_modifiers: dict[str, int] = {
            key: None for key in self.ability_scores
        }

        self.saving_throws: dict[str, int] = {
            key: None for key in self.ability_scores
        }

        self.strength_skills: dict[str, int] = {
            'athletics': None
        }

        self.dexterity_skills: dict[str, int] = {
            'acrobatics': None,
            'sleight of hand': None,
            'stealth': None
        }

        self.constitution_skills: dict[str, int] = {}

        self.intelligence_skills: dict[str, int] = {
            'arcana': None,
            'history': None,
            'investigation': None,
            'nature': None,
            'religion': None
        }

        self.wisdom_skills: dict[str, int] = {
            'animal handling': None,
            'insight': None,
            'medicine': None,
            'perception': None,
            'survival': None
        }

        self.charisma_skills: dict[str, int] = {
            'deception': None,
            'intimidation': None,
            'performance': None,
            'persuasion': None
        }

        self.skills: dict[str, int] = {
            **self.strength_skills,
            **self.dexterity_skills,
            **self.constitution_skills,
            **self.intelligence_skills,
            **self.wisdom_skills,
            **self.charisma_skills
        }
        
        self.sorted_skills = dict(sorted(self.skills.items()))
        
        self.info = {
            'ability scores': self.ability_scores,
            'armor class': self.armor_class,
            'class': self._class,
            'class hit points': self.class_hit_points,
            'hit points': self.hit_points,
            'initiative': self.initiative,
            'level': self.level,
            'name': self.name,
            'procifiency bonus': self.proficiency_bonus,
            'race': self.race
        }

    def set_ability_scores(self, nums):
        if isinstance(nums, str):
            nums = nums.split(',')
        if len(nums) == len(self.ability_scores):
            for idx, ability in enumerate(self.ability_scores):
                try:
                    self.set_ability_score(ability, int(nums[idx].strip()))
                except ValueError:
                    self.master.display_entry(f"Invalid number: {nums[idx]}")
                    return
        else: 
            self.master.display_entry(f'{Messages.invalid_set_all_ability_scores}')

    def set_ability_score(self, ability: str, value: int):
        if ability in self.ability_scores:
            mod = (int(value) - 10) // 2
            self.ability_scores[ability] = value
            self.ability_modifiers[ability] = mod
            self.set_skill(ability, mod)
            if ability == 'consitution':
                self.set_hit_points(in_set=True)
            elif ability == 'dexterity':
                self.set_armor_class()
                self.set_initiative()
            self.update()
            self.display_ability_score(ability)
        else:
            self.master.display_entry(f"Invalid ability: {ability}")

    def set_armor_class(self):
        if self.ability_modifiers['dexterity'] is not None:
            self.armor_class = 10 + int(self.ability_modifiers['dexterity'])
            self.update()

    def set_class(self, value: str):
        value = value.lower().strip()
        if value in self.class_handler.classes:
            self._class = value.capitalize().strip()
            self.set_class_hit_points()
            self.update()
            self.display_class()
        else:
            self.master.display_entry(f'{Messages.invalid_class}: {value}')

    def set_class_hit_points(self):
        self.class_hit_points = self.class_handler.level_1_max_hit_points[self._class.lower()]
        self.update()

    def set_hit_points(self, value=None, in_set=False):
        value = value.lower().strip()
        con_mod = self.ability_modifiers['constitution'] if self.ability_modifiers['constitution'] is not None else 0
        if self._class is not None:
            if value is None:
                self.hit_points = self.class_hit_points + con_mod
            elif value == 'auto':
                if self.level == 1 or '1':
                    self.hit_points = self.class_hit_points + con_mod
            self.update()
            self.display_hit_points()
        else:
            if in_set:
                return
            else:
                self.master.display_entry(f'{Messages.missing_class}')

    def set_initiative(self):
        self.initiative = self.ability_modifiers['dexterity'] if self.ability_modifiers['dexterity'] is not None else '?'
        self.update()
        
    def set_level(self, value: int):
        if 1 <= int(value) <= 20:
            self.level = value
            self.set_proficiency_bonus()
            self.update()
            self.display_level()
        else:
            self.master.display_entry(f'{Messages.invalid_level_selection}: {value}')

    def set_name(self, name: str):
        self.name = name.strip().capitalize()
        self.update()
        self.display_name()

    def set_proficiency_bonus(self):
        level = int(self.level) if self.level is not None else 0
        if level in range(1, 21):
            if 1 <= level <= 4:
                self.proficiency_bonus = 2
            elif 5 <= level <= 8:
                self.proficiency_bonus = 3
            elif 9 <= level <= 12:
                self.proficiency_bonus = 4
            elif 13 <= level <= 16:
                self.proficiency_bonus = 5
            elif 17 <= level <= 20:
                self.proficiency_bonus = 6
            self.update()
        else:
            self.master.display_entry("Invalid level for proficiency bonus.")

    def set_race(self, value: str):
        self.race = value.capitalize().strip()
        self.update()
        self.display_race()

    def set_skill(self, ability, value: int):
        if ability == 'strength':
            for skill in self.strength_skills:
                self.strength_skills[skill] = value
        elif ability == 'dexterity':
            for skill in self.dexterity_skills:
                self.dexterity_skills[skill] = value
        elif ability == 'constitution':
            for skill in self.constitution_skills:
                self.constitution_skills[skill] = value
        elif ability == 'intelligence':
            for skill in self.intelligence_skills:
                self.intelligence_skills[skill] = value
        elif ability == 'wisdom':
            for skill in self.wisdom_skills:
                self.wisdom_skills[skill] = value
        elif ability == 'charisma':
            for skill in self.charisma_skills:
                self.charisma_skills[skill] = value

        self.skills = {
            **self.strength_skills,
            **self.dexterity_skills,
            **self.constitution_skills,
            **self.intelligence_skills,
            **self.wisdom_skills,
            **self.charisma_skills
        }
        self.sorted_skills = dict(sorted(self.skills.items()))
        self.update()



    def display_ability_scores(self):
        for ability in self.ability_scores:
            score = self.ability_scores[ability]
            mod = self.ability_modifiers[ability]

            score_text = str(score) if score is not None else "?"
            mod_text = f"{mod:+d}" if isinstance(mod, int) else "?"
            
            self.master.display_entry(f"{ability.capitalize()}: {score_text} (mod {mod_text})")
    
    def display_ability_score(self, ability):
            score = self.ability_scores[ability]
            mod = self.ability_modifiers[ability]

            score_text = str(score) if score is not None else "?"
            mod_text = f"{mod:+d}" if isinstance(mod, int) else "?"
            
            self.master.display_entry(f"{ability.capitalize()}: {score_text} (mod {mod_text})")

    def display_armor_class(self):
        ac = self.armor_class if self.armor_class is not None else '?'
        self.master.display_entry(f"Armor Class: {ac}")

    def display_character(self):

        self.display_name()
        self.display_level()
        self.display_race()
        self.display_class()
        self.gap()
        self.display_hit_points()
        self.display_armor_class()
        self.display_initiative()
        self.display_proficiency_bonus()
        self.gap()
        self.display_ability_scores()
        self.gap()
        self.display_skills()
        
    def display_class(self):
        _class = self._class if self._class is not None else '?'
        self.master.display_entry(f'Class: {_class.capitalize()}')

    def display_initiative(self):
        init = self.initiative if self.initiative is not None else '?'
        self.master.display_entry(f'Initiative: {init}')

    def display_hit_points(self):
        hit_points = self.hit_points if self.hit_points is not None else '?'
        self.master.display_entry(f'Hit Points: {hit_points}')

    def display_level(self):
        level = self.level if self.level is not None else '?'
        self.master.display_entry(f'Level: {level}')

    def display_name(self):
        name = self.name if self.name is not None else '?'
        self.master.display_entry(f'Name: {name}')

    def display_proficiency_bonus(self):
        prof_bonus = self.proficiency_bonus if self.proficiency_bonus is not None else '?'
        self.master.display_entry(f'Proficieancy Bonus: {prof_bonus}')

    def display_race(self):
        race = self.race if self.race is not None else '?'
        self.master.display_entry(f'Race: {race.capitalize().strip()}')

    def display_skills(self):
        for skill in self.sorted_skills:
            mod = self.skills[skill]
            skill_mod = str(mod) if mod is not None else '?'
            self.master.display_entry(f'{skill.capitalize()}: {skill_mod}')
            
    def display_skill(self, skill: str):
        mod = self.skills[skill]
        self.master.display_entry(f'{skill.capitalize()}: {mod}')

    def gap(self):
        self.master.display_entry('----------')


    def update(self):
        self.info = {
            'ability scores': self.ability_scores,
            'armor class': self.armor_class,
            'class': self._class,
            'class hit points': self.class_hit_points,
            'hit points': self.hit_points,
            'initiative': self.initiative,
            'level': self.level,
            'name': self.name,
            'procifiency bonus': self.proficiency_bonus,
            'race': self.race
        }
        
    def save(self):
        name = self.name.strip().lower() if self.name else None
        if name:
            try:
                Path(self.file_handler.chardir).mkdir(parents=True, exist_ok=True)
                charfile = Path(f'{FileHandler.chardir}/{name}')
                with open(charfile, 'w') as file:
                    json.dump(self.info, file, indent=4)
                self.master.display_entry(f'{self.name.capitalize()} {Messages.save_character}')
            except Exception as e:
                self.master.display_entry(f'Error saving character: {str(e)}')
        else:
            self.master.display_entry(Messages.missing_name)
