from __future__ import annotations

from typing import List


class Plant:
	def __init__(
		self,
		name: str,
		species: str,
		age_days: int,
		height_cm: float,
		health_status: str = "healthy",
	) -> None:
		self.name = name
		self.species = species
		self.age_days = age_days
		self.height_cm = height_cm
		self.health_status = health_status


class Flower(Plant):
	def __init__(
		self,
		name: str,
		species: str,
		age_days: int,
		height_cm: float,
		color: str,
		petals_count: int,
		is_blooming: bool,
		fragrance_level: int,
		health_status: str = "healthy",
	) -> None:
		super().__init__(
			name=name,
			species=species,
			age_days=age_days,
			height_cm=height_cm,
			health_status=health_status,
		)
		self.color = color
		self.petals_count = petals_count
		self.is_blooming = is_blooming
		self.fragrance_level = fragrance_level


class Tree(Plant):
	def __init__(
		self,
		name: str,
		species: str,
		age_days: int,
		height_cm: float,
		trunk_diameter_cm: float,
		is_evergreen: bool,
		fruit_type: str | None = None,
		health_status: str = "healthy",
	) -> None:
		super().__init__(
			name=name,
			species=species,
			age_days=age_days,
			height_cm=height_cm,
			health_status=health_status,
		)
		self.trunk_diameter_cm = trunk_diameter_cm
		self.is_evergreen = is_evergreen
		self.fruit_type = fruit_type


class Garden:
	def __init__(
		self,
		owner: str,
		location: str,
		flowers: List[Flower] | None = None,
		trees: List[Tree] | None = None,
	) -> None:
		self.owner = owner
		self.location = location
		self.flowers = flowers if flowers is not None else []
		self.trees = trees if trees is not None else []

	@property
	def plants(self) -> List[Plant]:
		return [*self.flowers, *self.trees]


def build_bob_garden() -> Garden:
	flowers = [
		Flower(
			name="Daisy",
			species="Bellis perennis",
			age_days=45,
			height_cm=21.0,
			color="white",
			petals_count=34,
			is_blooming=True,
			fragrance_level=2,
		),
		Flower(
			name="Rose",
			species="Rosa rubiginosa",
			age_days=90,
			height_cm=58.0,
			color="red",
			petals_count=40,
			is_blooming=True,
			fragrance_level=8,
		),
	]

	trees = [
		Tree(
			name="Olive",
			species="Olea europaea",
			age_days=1500,
			height_cm=245.0,
			trunk_diameter_cm=18.5,
			is_evergreen=True,
			fruit_type="olive",
		),
		Tree(
			name="Apple",
			species="Malus domestica",
			age_days=1200,
			height_cm=310.0,
			trunk_diameter_cm=22.0,
			is_evergreen=False,
			fruit_type="apple",
		),
	]

	return Garden(owner="Bob", location="Backyard", flowers=flowers, trees=trees)


bob_garden = build_bob_garden()
 