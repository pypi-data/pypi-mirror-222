"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2492 import ActiveCylindricalGearSetDesignSelection
    from ._2493 import ActiveGearSetDesignSelection
    from ._2494 import ActiveGearSetDesignSelectionGroup
    from ._2495 import AGMAGleasonConicalGear
    from ._2496 import AGMAGleasonConicalGearSet
    from ._2497 import BevelDifferentialGear
    from ._2498 import BevelDifferentialGearSet
    from ._2499 import BevelDifferentialPlanetGear
    from ._2500 import BevelDifferentialSunGear
    from ._2501 import BevelGear
    from ._2502 import BevelGearSet
    from ._2503 import ConceptGear
    from ._2504 import ConceptGearSet
    from ._2505 import ConicalGear
    from ._2506 import ConicalGearSet
    from ._2507 import CylindricalGear
    from ._2508 import CylindricalGearSet
    from ._2509 import CylindricalPlanetGear
    from ._2510 import FaceGear
    from ._2511 import FaceGearSet
    from ._2512 import Gear
    from ._2513 import GearOrientations
    from ._2514 import GearSet
    from ._2515 import GearSetConfiguration
    from ._2516 import HypoidGear
    from ._2517 import HypoidGearSet
    from ._2518 import KlingelnbergCycloPalloidConicalGear
    from ._2519 import KlingelnbergCycloPalloidConicalGearSet
    from ._2520 import KlingelnbergCycloPalloidHypoidGear
    from ._2521 import KlingelnbergCycloPalloidHypoidGearSet
    from ._2522 import KlingelnbergCycloPalloidSpiralBevelGear
    from ._2523 import KlingelnbergCycloPalloidSpiralBevelGearSet
    from ._2524 import PlanetaryGearSet
    from ._2525 import SpiralBevelGear
    from ._2526 import SpiralBevelGearSet
    from ._2527 import StraightBevelDiffGear
    from ._2528 import StraightBevelDiffGearSet
    from ._2529 import StraightBevelGear
    from ._2530 import StraightBevelGearSet
    from ._2531 import StraightBevelPlanetGear
    from ._2532 import StraightBevelSunGear
    from ._2533 import WormGear
    from ._2534 import WormGearSet
    from ._2535 import ZerolBevelGear
    from ._2536 import ZerolBevelGearSet
else:
    import_structure = {
        '_2492': ['ActiveCylindricalGearSetDesignSelection'],
        '_2493': ['ActiveGearSetDesignSelection'],
        '_2494': ['ActiveGearSetDesignSelectionGroup'],
        '_2495': ['AGMAGleasonConicalGear'],
        '_2496': ['AGMAGleasonConicalGearSet'],
        '_2497': ['BevelDifferentialGear'],
        '_2498': ['BevelDifferentialGearSet'],
        '_2499': ['BevelDifferentialPlanetGear'],
        '_2500': ['BevelDifferentialSunGear'],
        '_2501': ['BevelGear'],
        '_2502': ['BevelGearSet'],
        '_2503': ['ConceptGear'],
        '_2504': ['ConceptGearSet'],
        '_2505': ['ConicalGear'],
        '_2506': ['ConicalGearSet'],
        '_2507': ['CylindricalGear'],
        '_2508': ['CylindricalGearSet'],
        '_2509': ['CylindricalPlanetGear'],
        '_2510': ['FaceGear'],
        '_2511': ['FaceGearSet'],
        '_2512': ['Gear'],
        '_2513': ['GearOrientations'],
        '_2514': ['GearSet'],
        '_2515': ['GearSetConfiguration'],
        '_2516': ['HypoidGear'],
        '_2517': ['HypoidGearSet'],
        '_2518': ['KlingelnbergCycloPalloidConicalGear'],
        '_2519': ['KlingelnbergCycloPalloidConicalGearSet'],
        '_2520': ['KlingelnbergCycloPalloidHypoidGear'],
        '_2521': ['KlingelnbergCycloPalloidHypoidGearSet'],
        '_2522': ['KlingelnbergCycloPalloidSpiralBevelGear'],
        '_2523': ['KlingelnbergCycloPalloidSpiralBevelGearSet'],
        '_2524': ['PlanetaryGearSet'],
        '_2525': ['SpiralBevelGear'],
        '_2526': ['SpiralBevelGearSet'],
        '_2527': ['StraightBevelDiffGear'],
        '_2528': ['StraightBevelDiffGearSet'],
        '_2529': ['StraightBevelGear'],
        '_2530': ['StraightBevelGearSet'],
        '_2531': ['StraightBevelPlanetGear'],
        '_2532': ['StraightBevelSunGear'],
        '_2533': ['WormGear'],
        '_2534': ['WormGearSet'],
        '_2535': ['ZerolBevelGear'],
        '_2536': ['ZerolBevelGearSet'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
