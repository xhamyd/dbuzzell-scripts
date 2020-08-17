class PokemonType:

    _all_types = ("normal", "fighting", "poison", "ground", "rock", "bug", "ghost", "steel", "fire", "water", "grass",
                  "electric", "psychic", "ice", "dragon", "fairy", "dark", "flying")

    def __init__(self, type_name):
        if type_name not in self._all_types:
            raise ValueError(f"Invalid pokemon type name provided: {type_name}")

        self.type_name = type_name

    def __eq__(self, other):
        return isinstance(other, PokemonType) and self.type_name == other.type_name

    def __hash__(self):
        return hash(self.type_name)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"<PokemonType '{self.type_name}'>"

    @classmethod
    def all_types(cls):
        return cls._all_types


class PokemonTypeChart:

    _TYPE_BEATS = {
        "normal": tuple(),
        "fighting": ("normal", "rock", "steel", "ice", "dark"),
        "poison": ("grass", "fairy"),
        "ground": ("fire", "electric", "poison", "rock", "steel"),
        "rock": ("flying", "bug", "fire", "ice"),
        "bug": ("grass", "psychic", "dark"),
        "ghost": ("ghost", "psychic"),
        "steel": ("ice", "rock", "fairy"),
        "fire": ("bug", "steel", "grass"),
        "water": ("ground", "rock", "fire"),
        "grass": ("ground", "rock", "water"),
        "electric": ("flying", "water"),
        "psychic": ("fighting", "poison"),
        "ice": ("flying", "ground", "grass", "dragon"),
        "dragon": ("dragon", ),
        "fairy": ("fighting", "dragon", "dark"),
        "dark": ("ghost", "psychic"),
        "flying": ("fighting", "bug", "grass")
    }

    _TYPE_WEAKS = {
        "normal": ("rock", "steel"),
        "fighting": ("flying", "poison", "psychic", "fairy", "bug"),
        "poison": ("ground", "psychic", "rock", "ghost"),
        "ground": ("bug", "grass"),
        "rock": ("fighting", "ground", "steel"),
        "bug": ("fighting", "flying", "poison", "ghost", "steel", "fire", "fairy"),
        "ghost": ("dark", ),
        "steel": ("steel", "fire", "water", "electric"),
        "fire": ("rock", "fire", "water", "dragon"),
        "water": ("water", "grass", "dragon"),
        "grass": ("flying", "poison", "bug", "steel", "fire", "grass", "dragon"),
        "electric": ("grass", "electric", "dragon"),
        "psychic": ("steel", "psychic"),
        "ice": ("steel", "fire", "water", "ice"),
        "dragon": ("steel", ),
        "fairy": ("fire", "steel", "poison"),
        "dark": ("fighting", "dark", "fairy"),
        "flying": ("rock", "steel", "electric")
    }

    _TYPE_FAILS = {
        "normal": ("ghost", ),
        "fighting": ("ghost", ),
        "poison": ("steel", ),
        "ground": ("flying", ),
        "rock": tuple(),
        "bug": tuple(),
        "ghost": ("normal", ),
        "steel": tuple(),
        "fire": tuple(),
        "water": tuple(),
        "grass": tuple(),
        "electric": ("ground", ),
        "psychic": ("dark", ),
        "ice": tuple(),
        "dragon": ("fairy", ),
        "fairy": tuple(),
        "dark": tuple(),
        "flying": tuple()
    }

    @staticmethod
    def all_types():
        return list(PokemonType(p_type) for p_type in PokemonType.all_types())

    @classmethod
    def types_it_beats(cls, pokemon_type):
        return list(PokemonType(type_name) for type_name in cls._TYPE_BEATS[pokemon_type.type_name])

    @classmethod
    def types_it_is_weak_against(cls, pokemon_type):
        return list(PokemonType(type_name) for type_name in cls._TYPE_WEAKS[pokemon_type.type_name])

    @classmethod
    def types_it_fails_against(cls, pokemon_type):
        return list(PokemonType(type_name) for type_name in cls._TYPE_FAILS[pokemon_type.type_name])


def best_types_against(*args, moves_only=False):
    CAN_BEAT_MODIFIER, WEAK_AGAINST_MODIFIER, FAILS_AGAINST_MODIFIER = 1.0, -0.8, -2.0
    CAN_GET_BEATEN_MODIFIER, IS_WEAK_FOR_MODIFIER, CANNOT_BE_HIT_MODIFIER = -1.0, 0.5, 2.0
    res = {p_type: 0 for p_type in PokemonTypeChart.all_types()}
    for arg in args:
        main_type = PokemonType(arg)
        for p_type in PokemonTypeChart.all_types():
            if main_type in PokemonTypeChart.types_it_beats(p_type):
                # print(f"{p_type} can beat {main_type} ({CAN_BEAT_MODIFIER:+0.1f})")
                res[p_type] += CAN_BEAT_MODIFIER

            if main_type in PokemonTypeChart.types_it_is_weak_against(p_type):
                # print(f"{p_type} is weak against {main_type} ({WEAK_AGAINST_MODIFIER:+0.1f})")
                res[p_type] += WEAK_AGAINST_MODIFIER

            if main_type in PokemonTypeChart.types_it_fails_against(p_type):
                # print(f"{p_type} cannot affect {main_type} ({FAILS_AGAINST_MODIFIER:+0.1f})")
                res[p_type] += FAILS_AGAINST_MODIFIER

            if not moves_only:
                if p_type in PokemonTypeChart.types_it_beats(main_type):
                    # print(f"{p_type} gets beaten by {main_type} ({CAN_GET_BEATEN_MODIFIER:+0.1f})")
                    res[p_type] += CAN_GET_BEATEN_MODIFIER

                if p_type in PokemonTypeChart.types_it_is_weak_against(main_type):
                    # print(f"{p_type} is weak for {main_type} ({IS_WEAK_FOR_MODIFIER:+0.1f})")
                    res[p_type] += IS_WEAK_FOR_MODIFIER

                if p_type in PokemonTypeChart.types_it_fails_against(main_type):
                    # print(f"{p_type} cannot be affected by {main_type} ({CANNOT_BE_HIT_MODIFIER:+0.1f})")
                    res[p_type] += CANNOT_BE_HIT_MODIFIER

    filtered_types = {p_type.type_name: modifier_val for (p_type, modifier_val) in res.items() if modifier_val >= 1.0}
    # Source: https://stackoverflow.com/a/1915631
    # print(filtered_types)
    return sorted(filtered_types, key=filtered_types.get, reverse=True)


def best_moves_against(*args):
    return best_types_against(*args, moves_only=True)


types = "water", "ice"
print(best_types_against(*types))
print(best_moves_against(*types))
