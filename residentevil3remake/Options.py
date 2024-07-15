from dataclasses import dataclass
from Options import (Choice, OptionList, NamedRange, 
    StartInventoryPool,
    PerGameCommonOptions, DeathLinkMixin)

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
    """Standard: Most people should play on this.
    Hardcore: Good luck, and thanks for testing deaths. Kappa"""
    display_name = "Difficulty to Play On"
    option_standard = 0
    option_hardcore = 1
    default = 0

class UnlockedTypewriters(OptionList):
    """Specify the exact name of typewriters from the warp buttons in-game, as a YAML array.
    """
    display_name = "Unlocked Typewriters"

class StartingHipPouches(NamedRange):
    """The number of hip pouches you want to start the game with, to a max of 3. 
    Any that you start with are taken out of the item pool and replaced with junk."""
    default = 0
    range_start = 0
    range_end = 3
    display_name = "Starting Hip Pouches"
    special_range_names = {
        "pockets": 0,
        "fanny pack": 1,
        "purse": 2,
        "backpack": 3
    }

class BonusStart(Choice):
    """Some players might want to start with a little help in the way of a few extra heal items and packs of ammo.
    This will give you grenades instead of ammo if Oops All Grenades option is set.

    False: Normal, don't start with extra heal items and packs of ammo.
    True: Start with those helper items."""
    display_name = "Bonus Start"
    option_false = 0
    option_true = 1
    default = 0

class ExtraDowntownItems(Choice):
    """Not getting Bolt Cutters or Fire Hose early can lead to some intense BK.
    This option adds an extra set of these items so the odds of BK are lower.

    False: Normal, only 1 set are in the item pool.
    True: Now, 2 of each are in the item pool."""
    display_name = "Extra Downtown Items"
    option_false = 0
    option_true = 1
    default = 0

class ExtraSewerItems(Choice):
    """Not getting Battery Pack or Kendo's Gate Key early can lead to the same situation.
    This option adds an extra set of these items so the odds of BK are lower.

    False: Normal, only 1 of each are in the item pool.
    True: Now, 2 of each are in the item pool."""
    display_name = "Extra Sewer Items"
    option_false = 0
    option_true = 1
    default = 0

class ForbidProgressionDowntown(Choice):
    """Accidentally skipping item locations early can lead to softlocking as certain story triggers make it impossible to backtrack. 
    This option seeks to avoid that by limiting item placements.

    False: Progression can be placed Downtown in locations that can be missed if story progresses too far, you've been warned.
    
    True: (Default) Will place your items into locations that are not permanently missable after fighting Nemesis on the Demolition Site Rooftop.
    This severely limits where progression can be to prevent softlocking of any kind. Will also remove progression for others if multiworld.

    NOTE - This option only affects *YOUR* Downtown. Your progression can still be in someone else's if they have this option enabled."""
    display_name = "Forbid Progression Downtown"
    option_false = 0
    option_true = 1
    default = 1
    
class ForbidProgressionInLabs(Choice):
    """While next to impossible to skip anything in NEST, it would certainly feel bad if someones Morph Ball ended up there.
    This option will completely remove progression from being at your end game, including the ten locations in Nemesis Final Fight. 

    False: Progression can be placed in NEST, remind everyone it was your fault when you are holding them hostage.

    True: (Default) Will place useful/junk items into NEST, the non-randomized locations will stay the same.

    NOTE - This option only affects *YOUR* NEST. Your progression can still be in someone else's if they have this option enabled."""
    display_name = "Allow Progression in Labs"
    option_false = 0
    option_true = 1
    default = 1
	
class OopsAllGrenades(Choice):
    """Enabling this swaps all weapons, weapon ammo, subweapons and explosive/gunpowder to Grenades. 
    (Except your starting weapon, the shotgun, and maybe one grenade launcher if it decides to spawn in the labs.)"""
    display_name = "Oops! All Grenades"
    option_false = 0
    option_true = 1
    default = 0
    
class OopsAllHandguns(Choice):
    """Enabling this swaps all weapons, weapon ammo, subweapons and explosive/gunpowder to Handgun Ammo. 
    (Except your starting weapon, the shotgun, and maybe one grenade launcher if it decides to spawn in the labs)"""
    display_name = "Oops! Only Handgun"
    option_false = 0
    option_true = 1
    default = 0
	
class NoFirstAidSpray(Choice):
    """Enabling this swaps all first aid sprays to filler or less useful items. 
    """
    display_name = "No First Aid Spray"
    option_false = 0
    option_true = 1
    default = 0

class NoGreenHerb(Choice):
    """Enabling this swaps all green herbs to filler or less useful items. 
    """
    display_name = "No Green Herbs"
    option_false = 0
    option_true = 1
    default = 0

class NoRedHerb(Choice):
    """Enabling this swaps all red herbs to filler or less useful items. 
    """
    display_name = "No Red Herbs"
    option_false = 0
    option_true = 1
    default = 0

class NoGunpowder(Choice):
    """Enabling this swaps all gunpowder of all types to filler or less useful items. 
    """
    display_name = "No Gunpowder"
    option_false = 0
    option_true = 1
    default = 0
    
class AddDamageTraps(Choice):
    """Enabling this adds traps to your game that, when received, deal 1 health state of damage to you. e.g., if you're "Fine", first one puts you in "Caution". 
    By default, these traps cannot kill you, but the "Damage Traps Can Kill" option can make them lethal.
    """
    display_name = "Add Damage Traps"
    option_false = 0
    option_true = 1
    default = 0

class DamageTrapCount(NamedRange):
    """While the "AddDamageTraps" option is enabled, this option specifies how many of this trap should be placed.
    """
    default = 10
    range_start = 0
    range_end = 30 
    display_name = "Damage Trap Count"
    special_range_names = {
        "disabled": 0,
        "half": 15,
        "all": 30,
    }

class DamageTrapsCanKill(Choice):
    """Enabling this while "Add Damage Traps" is enabled will allow the damage traps to drop your health state below "Danger". As in, they can kill you. 
    """
    display_name = "Damage Traps Can Kill"
    option_false = 0
    option_true = 1
    default = 0

# making this mixin so we can keep actual game options separate from AP core options that we want enabled
# not sure why this isn't a mixin in core atm, anyways
@dataclass
class StartInventoryFromPoolMixin:
    start_inventory_from_pool: StartInventoryPool

@dataclass
class RE3ROptions(StartInventoryFromPoolMixin, DeathLinkMixin, PerGameCommonOptions):
    character: Character
    scenario: Scenario
    difficulty: Difficulty
    unlocked_typewriters: UnlockedTypewriters
    starting_hip_pouches: StartingHipPouches
    bonus_start: BonusStart
    extra_downtown_items: ExtraDowntownItems
    extra_sewer_items: ExtraSewerItems
    forbid_progression_downtown: ForbidProgressionDowntown
    forbid_progression_in_labs: ForbidProgressionInLabs
    oops_all_grenades: OopsAllGrenades
    oops_all_handguns: OopsAllHandguns
    no_first_aid_spray: NoFirstAidSpray
    no_green_herb: NoGreenHerb
    no_red_herb: NoRedHerb
    no_gunpowder: NoGunpowder
    add_damage_traps: AddDamageTraps
    damage_trap_count: DamageTrapCount
    damage_traps_can_kill: DamageTrapsCanKill

