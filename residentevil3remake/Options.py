from Options import Choice, OptionList, NamedRange

class Character(Choice):
    """Jill: Was almost a sandwich.
    """
    display_name = "Character to Play"
    option_jill = 0
    default = 0

class Scenario(Choice):
    """A: Capcom did us dirty for this one.
    """
    display_name = "Scenario to Play"
    option_a = 0
    default = 0

class Difficulty(Choice):
    """Standard: Will add the others later.
    """
    display_name = "Difficulty to Play On"
    option_standard = 0
    default = 0

class UnlockedTypewriters(OptionList):
    """Specify the exact name of typewriters from the warp buttons in-game, as a YAML array.
    """
    display_name = "Unlocked Typewriters"

class StartingHipPouches(NamedRange):
    """The number of hip pouches you want to start the game with, to a max of 6 (or 5 for Hardcore). 
    Any that you start with are taken out of the item pool and replaced with junk."""
    default = 0
    range_start = 0
    range_end = 6
    display_name = "Starting Hip Pouches"
    special_range_names = {
        "disabled": 0,
        "half": 3,
        "all": 6,
    }

class BonusStart(Choice):
    """Some players might want to start with a little help in the way of a few extra heal items and packs of ammo.
    This option IS affected by cross-scenario weapon randomization, if that option is set.

    False: Normal, don't start with extra heal items and packs of ammo.
    True: Start with those helper items."""
    display_name = "Bonus Start"
    option_false = 0
    option_true = 1
    default = 0

re3roptions = {
    "character": Character,
    "scenario": Scenario,
    "difficulty": Difficulty,
    "unlocked_typewriters": UnlockedTypewriters,
    "starting_hip_pouches": StartingHipPouches,
    "bonus_start": BonusStart,
}
