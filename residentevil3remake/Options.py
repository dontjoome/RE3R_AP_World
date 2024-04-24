from Options import Choice, OptionList, NamedRange

class Character(Choice):
    """Jill: Only Choice.
    """
    display_name = "Character to Play"
    option_jill = 0
    default = 0

class Scenario(Choice):
    """A: Only Choice.
    """
    display_name = "Scenario to Play"
    option_a = 0
    default = 0

class Difficulty(Choice):
    """Standard: Most people should play on this.
    Hardcore: Good luck, and thanks for testing deaths. Kappa
    Assisted: No. Do Standard."""
    display_name = "Difficulty to Play On"
    option_standard = 0
    option_hardcore = 1
    default = 0

class UnlockedTypewriters(OptionList):
    """Specify the exact name of typewriters from the warp buttons in-game, as a YAML array.
    """
    display_name = "Unlocked Typewriters"

class StartingHipPouches(NamedRange):
    """Not Implemented yet, but soon."""
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
    """Not Implemented yet, but soon."""
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
    "bonus_start": BonusStart
}
