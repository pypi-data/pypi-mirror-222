import json
import random
from slugify import slugify
import dice
from autonomous.logger import log
from autonomous.apis import OpenAI
from dmtoolkit.models import Monster, Item, Spell, Character, Player, Shop


class DMTools:
    """
    _summary_

    Returns:
        _type_: _description_
    """

    LOOT_MULTIPLIER = 3

    @classmethod
    def roll_dice(roll_str):
        return dice.roll(roll_str)

    @classmethod
    def updatedb(cls):
        Monster.update_db()
        Spell.update_db()
        Item.update_db()

    @classmethod
    def _query(cls, api, **kwargs):
        # log(api, kwargs)
        if "pk" in kwargs:
            results = [api.get(kwargs["pk"])]
        elif kwargs:
            kwargs["slug"] = slugify(kwargs.get("name", ""))
            results = api.search(**kwargs)
        else:
            results = api.all()
        return results

    @classmethod
    def monsters(cls, **kwargs):
        return cls._query(Monster, **kwargs)

    @classmethod
    def items(cls, **kwargs):
        return cls._query(Item, **kwargs)

    @classmethod
    def spells(cls, **kwargs):
        return cls._query(Spell, **kwargs)

    @classmethod
    def characters(cls, **kwargs):
        # log(kwargs)
        return cls._query(Character, **kwargs)

    @classmethod
    def pcs(cls, **kwargs):
        kwargs.update({"npc": False})
        return cls._query(Character, **kwargs)

    @classmethod
    def npcs(cls, **kwargs):
        kwargs.update({"npc": True})
        return cls._query(Character, **kwargs)

    @classmethod
    def shops(cls, **kwargs):
        return cls._query(Shop, **kwargs)

    @classmethod
    def generatenpc(cls, name=None, summary=None, generate_image=False):
        age = random.randint(15, 100)
        personality = [
            "shy",
            "outgoing",
            "friendly",
            "mean",
            "snooty",
            "aggressive",
            "sneaky",
            "greedy",
            "kind",
            "generous",
            "smart",
            "dumb",
            "loyal",
            "dishonest",
            "honest",
            "lazy",
            "hardworking",
            "stubborn",
            "flexible",
            "proud",
            "humble",
            "confident",
            "insecure",
            "courageous",
            "cowardly",
            "optimistic",
            "pessimistic",
            "silly",
            "serious",
            "sensitive",
            "insensitive",
            "creative",
            "imaginative",
            "practical",
            "logical",
            "intuitive",
            "intelligent",
            "wise",
            "foolish",
            "curious",
            "nosy",
            "adventurous",
            "cautious",
            "careful",
            "reckless",
            "careless",
            "patient",
            "impatient",
            "tolerant",
            "intolerant",
            "forgiving",
            "unforgiving",
            "honest",
            "unfriendly",
            "outgoing",
            "shy",
            "sneaky",
            "honest",
            "dishonest",
            "disloyal",
            "unfriendly",
        ]

        gender = random.choices(["male", "female", "non-binary"], weights=[10, 10, 1], k=1)[0]
        primer = """
        You are a D&D 5e NPC generator that creates interesting random NPC's with complete stats and backstory
        """
        traits = ", ".join(random.sample(personality, 3))
        if summary:
            prompt = f"Generate an Dungeons and Dragons style NPC aged {age} years who is {summary}. Write a detailed NPC backstory that contains an unexpected twist or secret. The NPC should also have the following personality traits: {traits}"
        else:
            prompt = f"Generate an Dungeons and Dragons style {gender} NPC aged {age} years with the following personality traits: {traits}. Include a backstory that contains an unexpected twist or secret"
        # log(prompt)
        funcobj = {
            "name": "generate_npc",
            "description": "builds NPC data object",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The character's name",
                    },
                    "age": {
                        "type": "integer",
                        "description": "The character's age",
                    },
                    "gender": {
                        "type": "string",
                        "description": "The character's gender",
                    },
                    "race": {
                        "type": "string",
                        "description": "The character's race",
                    },
                    "personality": {
                        "type": "array",
                        "description": "The character's personality traits",
                        "items": {"type": "string"},
                    },
                    "desc": {
                        "type": "array",
                        "description": "A physical description of the character",
                        "items": {"type": "string"},
                    },
                    "backstory": {
                        "type": "string",
                        "description": "The character's backstory",
                    },
                    "class_name": {
                        "type": "string",
                        "description": "The character's DnD class",
                    },
                    "occupation": {
                        "type": "string",
                        "description": "The character's daily occupation",
                    },
                    "inventory": {
                        "type": "array",
                        "description": "The character's inventory of items",
                        "items": {"type": "string"},
                    },
                    "str": {
                        "type": "number",
                        "description": "The amount of Strength the character has from 1-20",
                    },
                    "dex": {
                        "type": "integer",
                        "description": "The amount of Dexterity the character has from 1-20",
                    },
                    "con": {
                        "type": "integer",
                        "description": "The amount of Constitution the character has from 1-20",
                    },
                    "int": {
                        "type": "integer",
                        "description": "The amount of Intelligence the character has from 1-20",
                    },
                    "wis": {
                        "type": "integer",
                        "description": "The amount of Wisdom the character has from 1-20",
                    },
                    "cha": {
                        "type": "integer",
                        "description": "The amount of Charisma the character has from 1-20",
                    },
                },
            },
        }
        required = funcobj["parameters"]["properties"].keys()
        funcobj["parameters"]["required"] = list(required)
        response = OpenAI().generate_text(prompt, primer, functions=funcobj)
        try:
            npc_data = json.loads(response)
        except Exception as e:
            log(e)
            raise Exception(response)

        npc = Character(**npc_data)
        return npc

    @classmethod
    def generateencounter(cls, num_players=5, level=1):
        difficulty_list = [
            "trivial",
            "easy",
            "medium",
            "hard",
        ]
        loot = [
            "gold",
            "gems",
            "magic item",
            "junk",
            "weapon",
            "armor",
        ]

        primer = """
        You are a D&D 5e Encounter generator that creates level appropriate random encounters and specific loot rewards.
        """
        difficulty = random.choice(list(enumerate(difficulty_list)))
        loot_type = random.choices(
            loot,
            weights=[10, 5, 3, 30, 10, 10],
            k=(difficulty[0] * DMTools.LOOT_MULTIPLIER) + 1,
        )
        prompt = f"Generate an appropriate Dungeons and Dragons 5e encounter for a party of {num_players} at level {level} that is {difficulty[1]} and rewards the following type of loot items: {loot_type}"
        funcobj = {
            "name": "generate_encounter",
            "description": "Generate an Encounter object",
            "parameters": {
                "type": "object",
                "properties": {
                    "enemies": {
                        "type": "array",
                        "description": "A list of enemies faced in the encounter",
                        "items": {"type": "string"},
                    },
                    "scenario": {
                        "type": "string",
                        "description": "The situation that led to the encounter from the enemy's perspective",
                    },
                    "difficulty": {
                        "type": "string",
                        "description": "The difficulty of the encounter",
                    },
                    "loot": {
                        "type": "array",
                        "description": "Loot gained from the encounter",
                        "items": {"type": "string"},
                    },
                },
            },
        }
        funcobj["parameters"]["required"] = list(funcobj["parameters"]["properties"].keys())
        # breakpoint()
        encounter = OpenAI().generate_text(prompt, primer, functions=funcobj)
        encounter = json.loads(encounter)
        return encounter

    @classmethod
    def generateshop(cls):
        primer = """
        You are a D&D 5e Shop generator that creates random shops.
        """
        prompt = "Generate a random shop"
        funcobj = {
            "name": "generate_shop",
            "description": "builds an Shop model object",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The shop's name",
                    },
                    "shoptype": {
                        "type": "string",
                        "description": "The type of wares the shop sells",
                    },
                    "desc": {
                        "type": "string",
                        "description": "A short description of the inside of the shop",
                    },
                    "inventory": {
                        "type": "array",
                        "description": "The shop's inventory of purchasable items",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string",
                                    "description": "The name of the item",
                                },
                                "desc": {
                                    "type": "string",
                                    "description": "A short description of the item",
                                },
                                "cost": {
                                    "type": "string",
                                    "description": "the cost of the item",
                                },
                            },
                        },
                    },
                },
            },
        }
        funcobj["parameters"]["required"] = list(funcobj["parameters"]["properties"].keys())
        shop = OpenAI().generate_text(prompt, primer, functions=funcobj)
        try:
            shop = json.loads(shop)
        except Exception as e:
            log(e)
            return None
        else:
            shopowner = cls.generatenpc(summary=f"Owner of {shop['name']}, a {shop['shoptype']} shop.")
            shopowner.save()
            shop["owner"] = shopowner
            shop_obj = Shop(**shop)
            shop_obj.save()
            return shop_obj
