"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4833 import AbstractAssemblyModalAnalysisAtAStiffness
    from ._4834 import AbstractShaftModalAnalysisAtAStiffness
    from ._4835 import AbstractShaftOrHousingModalAnalysisAtAStiffness
    from ._4836 import AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness
    from ._4837 import AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
    from ._4838 import AGMAGleasonConicalGearModalAnalysisAtAStiffness
    from ._4839 import AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
    from ._4840 import AssemblyModalAnalysisAtAStiffness
    from ._4841 import BearingModalAnalysisAtAStiffness
    from ._4842 import BeltConnectionModalAnalysisAtAStiffness
    from ._4843 import BeltDriveModalAnalysisAtAStiffness
    from ._4844 import BevelDifferentialGearMeshModalAnalysisAtAStiffness
    from ._4845 import BevelDifferentialGearModalAnalysisAtAStiffness
    from ._4846 import BevelDifferentialGearSetModalAnalysisAtAStiffness
    from ._4847 import BevelDifferentialPlanetGearModalAnalysisAtAStiffness
    from ._4848 import BevelDifferentialSunGearModalAnalysisAtAStiffness
    from ._4849 import BevelGearMeshModalAnalysisAtAStiffness
    from ._4850 import BevelGearModalAnalysisAtAStiffness
    from ._4851 import BevelGearSetModalAnalysisAtAStiffness
    from ._4852 import BoltedJointModalAnalysisAtAStiffness
    from ._4853 import BoltModalAnalysisAtAStiffness
    from ._4854 import ClutchConnectionModalAnalysisAtAStiffness
    from ._4855 import ClutchHalfModalAnalysisAtAStiffness
    from ._4856 import ClutchModalAnalysisAtAStiffness
    from ._4857 import CoaxialConnectionModalAnalysisAtAStiffness
    from ._4858 import ComponentModalAnalysisAtAStiffness
    from ._4859 import ConceptCouplingConnectionModalAnalysisAtAStiffness
    from ._4860 import ConceptCouplingHalfModalAnalysisAtAStiffness
    from ._4861 import ConceptCouplingModalAnalysisAtAStiffness
    from ._4862 import ConceptGearMeshModalAnalysisAtAStiffness
    from ._4863 import ConceptGearModalAnalysisAtAStiffness
    from ._4864 import ConceptGearSetModalAnalysisAtAStiffness
    from ._4865 import ConicalGearMeshModalAnalysisAtAStiffness
    from ._4866 import ConicalGearModalAnalysisAtAStiffness
    from ._4867 import ConicalGearSetModalAnalysisAtAStiffness
    from ._4868 import ConnectionModalAnalysisAtAStiffness
    from ._4869 import ConnectorModalAnalysisAtAStiffness
    from ._4870 import CouplingConnectionModalAnalysisAtAStiffness
    from ._4871 import CouplingHalfModalAnalysisAtAStiffness
    from ._4872 import CouplingModalAnalysisAtAStiffness
    from ._4873 import CVTBeltConnectionModalAnalysisAtAStiffness
    from ._4874 import CVTModalAnalysisAtAStiffness
    from ._4875 import CVTPulleyModalAnalysisAtAStiffness
    from ._4876 import CycloidalAssemblyModalAnalysisAtAStiffness
    from ._4877 import CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness
    from ._4878 import CycloidalDiscModalAnalysisAtAStiffness
    from ._4879 import CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness
    from ._4880 import CylindricalGearMeshModalAnalysisAtAStiffness
    from ._4881 import CylindricalGearModalAnalysisAtAStiffness
    from ._4882 import CylindricalGearSetModalAnalysisAtAStiffness
    from ._4883 import CylindricalPlanetGearModalAnalysisAtAStiffness
    from ._4884 import DatumModalAnalysisAtAStiffness
    from ._4885 import DynamicModelAtAStiffness
    from ._4886 import ExternalCADModelModalAnalysisAtAStiffness
    from ._4887 import FaceGearMeshModalAnalysisAtAStiffness
    from ._4888 import FaceGearModalAnalysisAtAStiffness
    from ._4889 import FaceGearSetModalAnalysisAtAStiffness
    from ._4890 import FEPartModalAnalysisAtAStiffness
    from ._4891 import FlexiblePinAssemblyModalAnalysisAtAStiffness
    from ._4892 import GearMeshModalAnalysisAtAStiffness
    from ._4893 import GearModalAnalysisAtAStiffness
    from ._4894 import GearSetModalAnalysisAtAStiffness
    from ._4895 import GuideDxfModelModalAnalysisAtAStiffness
    from ._4896 import HypoidGearMeshModalAnalysisAtAStiffness
    from ._4897 import HypoidGearModalAnalysisAtAStiffness
    from ._4898 import HypoidGearSetModalAnalysisAtAStiffness
    from ._4899 import InterMountableComponentConnectionModalAnalysisAtAStiffness
    from ._4900 import KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness
    from ._4901 import KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness
    from ._4902 import KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness
    from ._4903 import KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness
    from ._4904 import KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness
    from ._4905 import KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness
    from ._4906 import KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness
    from ._4907 import KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness
    from ._4908 import KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness
    from ._4909 import MassDiscModalAnalysisAtAStiffness
    from ._4910 import MeasurementComponentModalAnalysisAtAStiffness
    from ._2619 import ModalAnalysisAtAStiffness
    from ._4911 import MountableComponentModalAnalysisAtAStiffness
    from ._4912 import OilSealModalAnalysisAtAStiffness
    from ._4913 import PartModalAnalysisAtAStiffness
    from ._4914 import PartToPartShearCouplingConnectionModalAnalysisAtAStiffness
    from ._4915 import PartToPartShearCouplingHalfModalAnalysisAtAStiffness
    from ._4916 import PartToPartShearCouplingModalAnalysisAtAStiffness
    from ._4917 import PlanetaryConnectionModalAnalysisAtAStiffness
    from ._4918 import PlanetaryGearSetModalAnalysisAtAStiffness
    from ._4919 import PlanetCarrierModalAnalysisAtAStiffness
    from ._4920 import PointLoadModalAnalysisAtAStiffness
    from ._4921 import PowerLoadModalAnalysisAtAStiffness
    from ._4922 import PulleyModalAnalysisAtAStiffness
    from ._4923 import RingPinsModalAnalysisAtAStiffness
    from ._4924 import RingPinsToDiscConnectionModalAnalysisAtAStiffness
    from ._4925 import RollingRingAssemblyModalAnalysisAtAStiffness
    from ._4926 import RollingRingConnectionModalAnalysisAtAStiffness
    from ._4927 import RollingRingModalAnalysisAtAStiffness
    from ._4928 import RootAssemblyModalAnalysisAtAStiffness
    from ._4929 import ShaftHubConnectionModalAnalysisAtAStiffness
    from ._4930 import ShaftModalAnalysisAtAStiffness
    from ._4931 import ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
    from ._4932 import SpecialisedAssemblyModalAnalysisAtAStiffness
    from ._4933 import SpiralBevelGearMeshModalAnalysisAtAStiffness
    from ._4934 import SpiralBevelGearModalAnalysisAtAStiffness
    from ._4935 import SpiralBevelGearSetModalAnalysisAtAStiffness
    from ._4936 import SpringDamperConnectionModalAnalysisAtAStiffness
    from ._4937 import SpringDamperHalfModalAnalysisAtAStiffness
    from ._4938 import SpringDamperModalAnalysisAtAStiffness
    from ._4939 import StraightBevelDiffGearMeshModalAnalysisAtAStiffness
    from ._4940 import StraightBevelDiffGearModalAnalysisAtAStiffness
    from ._4941 import StraightBevelDiffGearSetModalAnalysisAtAStiffness
    from ._4942 import StraightBevelGearMeshModalAnalysisAtAStiffness
    from ._4943 import StraightBevelGearModalAnalysisAtAStiffness
    from ._4944 import StraightBevelGearSetModalAnalysisAtAStiffness
    from ._4945 import StraightBevelPlanetGearModalAnalysisAtAStiffness
    from ._4946 import StraightBevelSunGearModalAnalysisAtAStiffness
    from ._4947 import SynchroniserHalfModalAnalysisAtAStiffness
    from ._4948 import SynchroniserModalAnalysisAtAStiffness
    from ._4949 import SynchroniserPartModalAnalysisAtAStiffness
    from ._4950 import SynchroniserSleeveModalAnalysisAtAStiffness
    from ._4951 import TorqueConverterConnectionModalAnalysisAtAStiffness
    from ._4952 import TorqueConverterModalAnalysisAtAStiffness
    from ._4953 import TorqueConverterPumpModalAnalysisAtAStiffness
    from ._4954 import TorqueConverterTurbineModalAnalysisAtAStiffness
    from ._4955 import UnbalancedMassModalAnalysisAtAStiffness
    from ._4956 import VirtualComponentModalAnalysisAtAStiffness
    from ._4957 import WormGearMeshModalAnalysisAtAStiffness
    from ._4958 import WormGearModalAnalysisAtAStiffness
    from ._4959 import WormGearSetModalAnalysisAtAStiffness
    from ._4960 import ZerolBevelGearMeshModalAnalysisAtAStiffness
    from ._4961 import ZerolBevelGearModalAnalysisAtAStiffness
    from ._4962 import ZerolBevelGearSetModalAnalysisAtAStiffness
else:
    import_structure = {
        '_4833': ['AbstractAssemblyModalAnalysisAtAStiffness'],
        '_4834': ['AbstractShaftModalAnalysisAtAStiffness'],
        '_4835': ['AbstractShaftOrHousingModalAnalysisAtAStiffness'],
        '_4836': ['AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness'],
        '_4837': ['AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness'],
        '_4838': ['AGMAGleasonConicalGearModalAnalysisAtAStiffness'],
        '_4839': ['AGMAGleasonConicalGearSetModalAnalysisAtAStiffness'],
        '_4840': ['AssemblyModalAnalysisAtAStiffness'],
        '_4841': ['BearingModalAnalysisAtAStiffness'],
        '_4842': ['BeltConnectionModalAnalysisAtAStiffness'],
        '_4843': ['BeltDriveModalAnalysisAtAStiffness'],
        '_4844': ['BevelDifferentialGearMeshModalAnalysisAtAStiffness'],
        '_4845': ['BevelDifferentialGearModalAnalysisAtAStiffness'],
        '_4846': ['BevelDifferentialGearSetModalAnalysisAtAStiffness'],
        '_4847': ['BevelDifferentialPlanetGearModalAnalysisAtAStiffness'],
        '_4848': ['BevelDifferentialSunGearModalAnalysisAtAStiffness'],
        '_4849': ['BevelGearMeshModalAnalysisAtAStiffness'],
        '_4850': ['BevelGearModalAnalysisAtAStiffness'],
        '_4851': ['BevelGearSetModalAnalysisAtAStiffness'],
        '_4852': ['BoltedJointModalAnalysisAtAStiffness'],
        '_4853': ['BoltModalAnalysisAtAStiffness'],
        '_4854': ['ClutchConnectionModalAnalysisAtAStiffness'],
        '_4855': ['ClutchHalfModalAnalysisAtAStiffness'],
        '_4856': ['ClutchModalAnalysisAtAStiffness'],
        '_4857': ['CoaxialConnectionModalAnalysisAtAStiffness'],
        '_4858': ['ComponentModalAnalysisAtAStiffness'],
        '_4859': ['ConceptCouplingConnectionModalAnalysisAtAStiffness'],
        '_4860': ['ConceptCouplingHalfModalAnalysisAtAStiffness'],
        '_4861': ['ConceptCouplingModalAnalysisAtAStiffness'],
        '_4862': ['ConceptGearMeshModalAnalysisAtAStiffness'],
        '_4863': ['ConceptGearModalAnalysisAtAStiffness'],
        '_4864': ['ConceptGearSetModalAnalysisAtAStiffness'],
        '_4865': ['ConicalGearMeshModalAnalysisAtAStiffness'],
        '_4866': ['ConicalGearModalAnalysisAtAStiffness'],
        '_4867': ['ConicalGearSetModalAnalysisAtAStiffness'],
        '_4868': ['ConnectionModalAnalysisAtAStiffness'],
        '_4869': ['ConnectorModalAnalysisAtAStiffness'],
        '_4870': ['CouplingConnectionModalAnalysisAtAStiffness'],
        '_4871': ['CouplingHalfModalAnalysisAtAStiffness'],
        '_4872': ['CouplingModalAnalysisAtAStiffness'],
        '_4873': ['CVTBeltConnectionModalAnalysisAtAStiffness'],
        '_4874': ['CVTModalAnalysisAtAStiffness'],
        '_4875': ['CVTPulleyModalAnalysisAtAStiffness'],
        '_4876': ['CycloidalAssemblyModalAnalysisAtAStiffness'],
        '_4877': ['CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness'],
        '_4878': ['CycloidalDiscModalAnalysisAtAStiffness'],
        '_4879': ['CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness'],
        '_4880': ['CylindricalGearMeshModalAnalysisAtAStiffness'],
        '_4881': ['CylindricalGearModalAnalysisAtAStiffness'],
        '_4882': ['CylindricalGearSetModalAnalysisAtAStiffness'],
        '_4883': ['CylindricalPlanetGearModalAnalysisAtAStiffness'],
        '_4884': ['DatumModalAnalysisAtAStiffness'],
        '_4885': ['DynamicModelAtAStiffness'],
        '_4886': ['ExternalCADModelModalAnalysisAtAStiffness'],
        '_4887': ['FaceGearMeshModalAnalysisAtAStiffness'],
        '_4888': ['FaceGearModalAnalysisAtAStiffness'],
        '_4889': ['FaceGearSetModalAnalysisAtAStiffness'],
        '_4890': ['FEPartModalAnalysisAtAStiffness'],
        '_4891': ['FlexiblePinAssemblyModalAnalysisAtAStiffness'],
        '_4892': ['GearMeshModalAnalysisAtAStiffness'],
        '_4893': ['GearModalAnalysisAtAStiffness'],
        '_4894': ['GearSetModalAnalysisAtAStiffness'],
        '_4895': ['GuideDxfModelModalAnalysisAtAStiffness'],
        '_4896': ['HypoidGearMeshModalAnalysisAtAStiffness'],
        '_4897': ['HypoidGearModalAnalysisAtAStiffness'],
        '_4898': ['HypoidGearSetModalAnalysisAtAStiffness'],
        '_4899': ['InterMountableComponentConnectionModalAnalysisAtAStiffness'],
        '_4900': ['KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness'],
        '_4901': ['KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness'],
        '_4902': ['KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness'],
        '_4903': ['KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness'],
        '_4904': ['KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness'],
        '_4905': ['KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness'],
        '_4906': ['KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness'],
        '_4907': ['KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness'],
        '_4908': ['KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness'],
        '_4909': ['MassDiscModalAnalysisAtAStiffness'],
        '_4910': ['MeasurementComponentModalAnalysisAtAStiffness'],
        '_2619': ['ModalAnalysisAtAStiffness'],
        '_4911': ['MountableComponentModalAnalysisAtAStiffness'],
        '_4912': ['OilSealModalAnalysisAtAStiffness'],
        '_4913': ['PartModalAnalysisAtAStiffness'],
        '_4914': ['PartToPartShearCouplingConnectionModalAnalysisAtAStiffness'],
        '_4915': ['PartToPartShearCouplingHalfModalAnalysisAtAStiffness'],
        '_4916': ['PartToPartShearCouplingModalAnalysisAtAStiffness'],
        '_4917': ['PlanetaryConnectionModalAnalysisAtAStiffness'],
        '_4918': ['PlanetaryGearSetModalAnalysisAtAStiffness'],
        '_4919': ['PlanetCarrierModalAnalysisAtAStiffness'],
        '_4920': ['PointLoadModalAnalysisAtAStiffness'],
        '_4921': ['PowerLoadModalAnalysisAtAStiffness'],
        '_4922': ['PulleyModalAnalysisAtAStiffness'],
        '_4923': ['RingPinsModalAnalysisAtAStiffness'],
        '_4924': ['RingPinsToDiscConnectionModalAnalysisAtAStiffness'],
        '_4925': ['RollingRingAssemblyModalAnalysisAtAStiffness'],
        '_4926': ['RollingRingConnectionModalAnalysisAtAStiffness'],
        '_4927': ['RollingRingModalAnalysisAtAStiffness'],
        '_4928': ['RootAssemblyModalAnalysisAtAStiffness'],
        '_4929': ['ShaftHubConnectionModalAnalysisAtAStiffness'],
        '_4930': ['ShaftModalAnalysisAtAStiffness'],
        '_4931': ['ShaftToMountableComponentConnectionModalAnalysisAtAStiffness'],
        '_4932': ['SpecialisedAssemblyModalAnalysisAtAStiffness'],
        '_4933': ['SpiralBevelGearMeshModalAnalysisAtAStiffness'],
        '_4934': ['SpiralBevelGearModalAnalysisAtAStiffness'],
        '_4935': ['SpiralBevelGearSetModalAnalysisAtAStiffness'],
        '_4936': ['SpringDamperConnectionModalAnalysisAtAStiffness'],
        '_4937': ['SpringDamperHalfModalAnalysisAtAStiffness'],
        '_4938': ['SpringDamperModalAnalysisAtAStiffness'],
        '_4939': ['StraightBevelDiffGearMeshModalAnalysisAtAStiffness'],
        '_4940': ['StraightBevelDiffGearModalAnalysisAtAStiffness'],
        '_4941': ['StraightBevelDiffGearSetModalAnalysisAtAStiffness'],
        '_4942': ['StraightBevelGearMeshModalAnalysisAtAStiffness'],
        '_4943': ['StraightBevelGearModalAnalysisAtAStiffness'],
        '_4944': ['StraightBevelGearSetModalAnalysisAtAStiffness'],
        '_4945': ['StraightBevelPlanetGearModalAnalysisAtAStiffness'],
        '_4946': ['StraightBevelSunGearModalAnalysisAtAStiffness'],
        '_4947': ['SynchroniserHalfModalAnalysisAtAStiffness'],
        '_4948': ['SynchroniserModalAnalysisAtAStiffness'],
        '_4949': ['SynchroniserPartModalAnalysisAtAStiffness'],
        '_4950': ['SynchroniserSleeveModalAnalysisAtAStiffness'],
        '_4951': ['TorqueConverterConnectionModalAnalysisAtAStiffness'],
        '_4952': ['TorqueConverterModalAnalysisAtAStiffness'],
        '_4953': ['TorqueConverterPumpModalAnalysisAtAStiffness'],
        '_4954': ['TorqueConverterTurbineModalAnalysisAtAStiffness'],
        '_4955': ['UnbalancedMassModalAnalysisAtAStiffness'],
        '_4956': ['VirtualComponentModalAnalysisAtAStiffness'],
        '_4957': ['WormGearMeshModalAnalysisAtAStiffness'],
        '_4958': ['WormGearModalAnalysisAtAStiffness'],
        '_4959': ['WormGearSetModalAnalysisAtAStiffness'],
        '_4960': ['ZerolBevelGearMeshModalAnalysisAtAStiffness'],
        '_4961': ['ZerolBevelGearModalAnalysisAtAStiffness'],
        '_4962': ['ZerolBevelGearSetModalAnalysisAtAStiffness'],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()['__file__'],
        import_structure,
    )
