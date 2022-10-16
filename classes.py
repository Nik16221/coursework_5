from dataclasses import dataclass

from skills import Skill, FuryPunch, HardShot, FireBall


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="Воин",
    max_health=60,
    max_stamina=30,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryPunch()
)  # TODO Инициализируем экземпляр класса UnitClass и присваиваем ему необходимые значения аттрибутов

ThiefClass = UnitClass(
    name="Вор",
    max_health=50,
    max_stamina=25,
    attack=1.5,
    stamina=1.2,
    armor=1.0,
    skill=HardShot()
)  # TODO действуем так же как и с воином

MageClass = UnitClass(
    name="Маг",
    max_health=40,
    max_stamina=50,
    attack=2,
    stamina=1.0,
    armor=0.8,
    skill=FireBall()
)


unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass,
    MageClass.name: MageClass
}
