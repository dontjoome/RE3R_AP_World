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
    Hardcore: Slightly tougher, but not by much. 
    Nightmare: It actually rains zombies, Kappa
    Inferno: Hope your name isn't Gohan, because you need to dodge... a lot"""
    display_name = "Difficulty to Play On"
    option_standard = 0
    option_hardcore = 1
    option_nightmare = 2
    option_inferno = 3
    default = 0

class UnlockedTypewriters(OptionList):
    """Specify the exact name of typewriters from the warp buttons in-game, as a YAML array.
    """
    display_name = "Unlocked Typewriters"

class StartingHipPouches(Choice):
    """The number of hip pouches you want to start the game with, to a max of 3. 
    Any that you start with are taken out of the item pool and replaced with junk.
    
    Pockets: Equivalent of zero starting hip pouches. 
    Fanny pack: Equivalent of one starting hip pouch. 
    Purse: Equivalent of two starting hip pouches.
    Backpack: Equivalent of three starting hip pouches."""
    display_name = "Starting Hip Pouches"
    option_pockets = 0
    option_fanny_pack = 1
    option_purse = 2
    option_backpack = 3
    default = 0

class BonusStart(Choice):
    """Some players might want to start with a little help in the way of a few extra heal items and packs of ammo.
    This will give you grenades instead of ammo if Oops All Grenades option is set.

    False: Normal, don't start with extra heal items and packs of ammo.
    True: Start with those helper items."""
    display_name = "Bonus Start"
    option_false = 0
    option_true = 1
    default = 0

class EarlyFireHose(Choice):
    """Receiving Fire Hose late can lead to some intense BK.
    This option will place it early to lower the odds of BK.

    False: Normal, will place it anywhere in the world and you may be waiting a bit to progress.
    True: Will place it in Sphere 1 of the world, and should prevent lengthy BK."""
    display_name = "Early Fire Hose"
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

class AllowMissableLocations(Choice):
    """Accidentally skipping item locations early can lead to softlocking as certain story triggers make it impossible to backtrack. 
    This option seeks to avoid that by limiting item placements.

    False: (Default) Will place items so they are not permanently missable.
    This severely limits where progression can be to prevent softlocking of any kind. 
    Will also remove progression for others if multiworld.
    
    True: Progression can be placed in locations that can be missed if story progresses too far, you've been warned (use the poptracker).

    NOTE - This option only affects *YOUR* game. Your progression can still be in someone else's if they have this option enabled."""
    display_name = "Allow Missable Locations"
    option_false = 0
    option_true = 1
    default = 0
    
class AllowProgressionInLabs(Choice):
    """While next to impossible to skip anything in NEST, it would certainly feel bad if someones Morph Ball ended up there.
    This option will completely remove progression from being at your end game, including the ten locations in Nemesis Final Fight. 

    False: (Default) Will place useful/junk items into NEST, the non-randomized locations will stay the same.

    True: Progression can be placed in NEST, remind everyone it was your fault when you are holding them hostage.

    NOTE - This option only affects *YOUR* NEST. Your progression can still be in someone else's if they have this option enabled."""
    display_name = "Allow Progression in Labs"
    option_false = 0
    option_true = 1
    default = 0
	
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
    display_name = "Oops! All Handguns"
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
    
# class AddParasiteTraps(Choice):
    # """Enabling this adds traps to your game that, when received, gives you parasites. e.g., when you get grabbed by deimos. 
    # These traps cannot kill you, but they will continuously damage you over time, similar to the Poison status in RE2R.
    # """
    # display_name = "Add Parasite Traps"
    # option_false = 0
    # option_true = 1
    # default = 0

# class ParasiteTrapCount(NamedRange):
    # """While the "AddParasiteTraps" option is enabled, this option specifies how many of this trap should be placed.
    # """
    # default = 10
    # range_start = 0
    # range_end = 30 
    # display_name = "Parasite Trap Count"
    # special_range_names = {
    #     "disabled": 0,
    #     "half": 15,
    #     "all": 30,
    # }
    
# class AddPukeTraps(Choice):
    # """Enabling this adds traps to your game that, when received, will cause you to vomit. e.g., when you heal yourself from parasites. 
    # These traps are more of a nuisance than anything, but can be trolly if you're in the middle of combat.
    # """
    # display_name = "Add Puke Traps"
    # option_false = 0
    # option_true = 1
    # default = 0
    
# class PukeTrapCount(NamedRange):
    # """While the "AddPukeTraps" option is enabled, this option specifies how many of this trap should be placed.
    # """
    # default = 10
    # range_start = 0
    # range_end = 30 
    # display_name = "Puke Trap Count"
    # special_range_names = {
    #     "disabled": 0,
    #     "half": 15,
    #     "all": 30,
    # }

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
    early_fire_hose: EarlyFireHose
    extra_sewer_items: ExtraSewerItems
    allow_missable_locations: AllowMissableLocations
    allow_progression_in_labs: AllowProgressionInLabs
    oops_all_grenades: OopsAllGrenades
    oops_all_handguns: OopsAllHandguns
    no_first_aid_spray: NoFirstAidSpray
    no_green_herb: NoGreenHerb
    no_red_herb: NoRedHerb
    no_gunpowder: NoGunpowder
    add_damage_traps: AddDamageTraps
    damage_trap_count: DamageTrapCount
    damage_traps_can_kill: DamageTrapsCanKill
    # add_parasite_traps: AddParasiteTraps
    # parasite_trap_count: ParasiteTrapCount
    # add_puke_traps: AddPukeTraps
    # puke_trap_count: PukeTrapCount

