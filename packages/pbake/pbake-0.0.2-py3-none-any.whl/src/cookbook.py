import typing
from dataclasses import dataclass


class UnknownRecipeException(Exception):
    def __init__(self, recipe_name: str) -> None:
        self.message = f"Unknown Recipe: {recipe_name} is not a known recipe!"
        super().__init__(self.message)


@dataclass
class Recipe:
    cookbook: "CookBook"
    name: str
    func: typing.Any
    doc: str
    prereqs: typing.List[str]

    def invoke(self):
        for prereq_name in self.prereqs:
            self.cookbook.get_recipe(prereq_name).invoke()
        self.func()


class CookBook:
    recipes: dict = {}
    name: str

    def __init__(self, name) -> None:
        self.name = name

    def recipe(self, name: str, prereqs: typing.List[str] = []) -> typing.Any:
        def wrapper(func: typing.Any) -> typing.Any:
            self.recipes[name] = Recipe(
                self, name=name, func=func, doc=func.__doc__, prereqs=prereqs
            )
            return func
        return wrapper

    def get_recipe(self, name) -> typing.Optional[Recipe]:
        if name in self.recipes:
          return self.recipes[name]
        raise UnknownRecipeException(name)


    def text(self):
        sorted_keys = sorted(self.recipes.keys())
        longest_recipe_name_len = len(max(sorted_keys, key=lambda x: len(x)))
        message = f"USAGE: bake [{'|'.join(sorted_keys)}]\n"
        for key in sorted_keys:
            recipe = self.recipes[key]
            message += f"\t%{longest_recipe_name_len}s %s\n" % (
                recipe.name,
                recipe.doc,
            )
        return message
