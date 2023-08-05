"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2282 import AGMAGleasonConicalGearMesh
    from ._2283 import AGMAGleasonConicalGearTeethSocket
    from ._2284 import BevelDifferentialGearMesh
    from ._2285 import BevelDifferentialGearTeethSocket
    from ._2286 import BevelGearMesh
    from ._2287 import BevelGearTeethSocket
    from ._2288 import ConceptGearMesh
    from ._2289 import ConceptGearTeethSocket
    from ._2290 import ConicalGearMesh
    from ._2291 import ConicalGearTeethSocket
    from ._2292 import CylindricalGearMesh
    from ._2293 import CylindricalGearTeethSocket
    from ._2294 import FaceGearMesh
    from ._2295 import FaceGearTeethSocket
    from ._2296 import GearMesh
    from ._2297 import GearTeethSocket
    from ._2298 import HypoidGearMesh
    from ._2299 import HypoidGearTeethSocket
    from ._2300 import KlingelnbergConicalGearTeethSocket
    from ._2301 import KlingelnbergCycloPalloidConicalGearMesh
    from ._2302 import KlingelnbergCycloPalloidHypoidGearMesh
    from ._2303 import KlingelnbergCycloPalloidSpiralBevelGearMesh
    from ._2304 import KlingelnbergHypoidGearTeethSocket
    from ._2305 import KlingelnbergSpiralBevelGearTeethSocket
    from ._2306 import SpiralBevelGearMesh
    from ._2307 import SpiralBevelGearTeethSocket
    from ._2308 import StraightBevelDiffGearMesh
    from ._2309 import StraightBevelDiffGearTeethSocket
    from ._2310 import StraightBevelGearMesh
    from ._2311 import StraightBevelGearTeethSocket
    from ._2312 import WormGearMesh
    from ._2313 import WormGearTeethSocket
    from ._2314 import ZerolBevelGearMesh
    from ._2315 import ZerolBevelGearTeethSocket
else:
    import_structure = {
        '_2282': ['AGMAGleasonConicalGearMesh'],
        '_2283': ['AGMAGleasonConicalGearTeethSocket'],
        '_2284': ['BevelDifferentialGearMesh'],
        '_2285': ['BevelDifferentialGearTeethSocket'],
        '_2286': ['BevelGearMesh'],
        '_2287': ['BevelGearTeethSocket'],
        '_2288': ['ConceptGearMesh'],
        '_2289': ['ConceptGearTeethSocket'],
        '_2290': ['ConicalGearMesh'],
        '_2291': ['ConicalGearTeethSocket'],
        '_2292': ['CylindricalGearMesh'],
        '_2293': ['CylindricalGearTeethSocket'],
        '_2294': ['FaceGearMesh'],
        '_2295': ['FaceGearTeethSocket'],
        '_2296': ['GearMesh'],
        '_2297': ['GearTeethSocket'],
        '_2298': ['HypoidGearMesh'],
        '_2299': ['HypoidGearTeethSocket'],
        '_2300': ['KlingelnbergConicalGearTeethSocket'],
        '_2301': ['KlingelnbergCycloPalloidConicalGearMesh'],
        '_2302': ['KlingelnbergCycloPalloidHypoidGearMesh'],
        '_2303': ['KlingelnbergCycloPalloidSpiralBevelGearMesh'],
        '_2304': ['KlingelnbergHypoidGearTeethSocket'],
        '_2305': ['KlingelnbergSpiralBevelGearTeethSocket'],
        '_2306': ['SpiralBevelGearMesh'],
        '_2307': ['SpiralBevelGearTeethSocket'],
        '_2308': ['StraightBevelDiffGearMesh'],
        '_2309': ['StraightBevelDiffGearTeethSocket'],
        '_2310': ['StraightBevelGearMesh'],
        '_2311': ['StraightBevelGearTeethSocket'],
        '_2312': ['WormGearMesh'],
        '_2313': ['WormGearTeethSocket'],
        '_2314': ['ZerolBevelGearMesh'],
        '_2315': ['ZerolBevelGearTeethSocket'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
