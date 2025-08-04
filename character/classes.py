class Class:
    def __init__(self):
        self.classes: list = [
            'barbarian',
            'bard',
            'cleric',
            'druid',
            'fighter',
            'monk',
            'paladin',
            'ranger',
            'rogue',
            'sorcerer',
            'warlock',
            'wizard'
        ]
        
        self.barbarian_subclasses: list = [
            'path of the berserker',
            'path of the totem warrior'
        ]
        
        self.bard_subclasses: list = [
            'college of lore',
            'college of valor'
        ]
        
        self.cleric_subclasses: list = [
            'knowledge domain',
            'life domain',
            'light domain',
            'nature domain',
            'tempest domain',
            'trickery domain',
            'war domain'
        ]
        
        self.druid_subclasses: list = [
            'circle of the land',
            'circle of the moon'
        ]
        
        self.fighter_subclasses: list = [
            'champion',
            'battle master',
            'eldritch knight'
        ]
        
        self.monk_subclasses: list = [
            'way of the open hand',
            'way of the shadow',
            'way of the four elements'
        ]
        
        self.paladin_subclasses: list = [
            'oath of devotion',
            'oath of ancients',
            'oath of vengeance'
        ]
        
        self.ranger_subclasses: list = [
            'hunter',
            'beast master'
        ]
        
        self.rogue_subclasses: list = [
            'thief',
            'assassin',
            'arcane trickster'
        ]
        
        self.sorcerer_subclasses: list = [
            'draconic bloodline',
            'wild magic'
        ]
        
        self.warlock_subclasses: list = [
            'the archfay',
            'the fiend',
            'the great old one'
        ]
        
        self.wizard_subclasses: list = [
            'school of abjuration',
            'school of conjuration',
            'school of divination',
            'school of enchantment',
            'school of evocation',
            'school of illusion',
            'school of necromancy',
            'school of transmutation'
        ]
        
        self.level_1_max_hit_points: dict[str, int] = {
            'barbarian': 12,
            'bard': 8,
            'cleric': 8,
            'druid': 8,
            'fighter': 10,
            'monk': 8,
            'paladin': 10,
            'ranger': 10,
            'rogue': 8,
            'sorcerer': 6,
            'warlock': 8,
            'wizard': 6
        }
