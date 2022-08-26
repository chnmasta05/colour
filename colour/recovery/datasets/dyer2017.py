"""
Dyer et al. (2017) - Camera Sensitivities Basis Functions
=========================================================

Defines the datasets for camera sensitivities recovery using
*Jiang, Liu, Gu and Süsstrunk (2013)* method.

References
----------
-   :cite:`Dyer2017` : Dyer, S., Forsythe, A., Irons, J., Mansencal, T., & Zhu,
    M. (2017). RAW to ACES Utility Data.
"""

from __future__ import annotations

import numpy as np

from colour.colorimetry import SpectralShape
from colour.hints import NDArray

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "SPECTRAL_SHAPE_BASIS_FUNCTIONS_DYER2017",
    "BASIS_FUNCTIONS_DYER2017",
]


SPECTRAL_SHAPE_BASIS_FUNCTIONS_DYER2017: SpectralShape = SpectralShape(
    400, 700, 10
)
"""
Spectral shape of the *Dyer et al. (2017)* basis functions.
"""

BASIS_FUNCTIONS_DYER2017: NDArray = np.array(
    [
        [
            [0.007056580228771, 0.004260510453546, 0.012005618620200],
            [0.011381496848887, 0.006321217690762, 0.045027969134397],
            [0.027779786584473, 0.024975081551722, 0.188574571223502],
            [0.027929892918492, 0.036191610500504, 0.274088722176641],
            [0.024759529580195, 0.049025997461696, 0.340401494061343],
            [0.020066939864197, 0.060686557895203, 0.382755892579880],
            [0.018499202799556, 0.083596670808663, 0.403985829516869],
            [0.021465476619957, 0.130176921242351, 0.396398753888955],
            [0.024358608984108, 0.170753903111829, 0.358003599358587],
            [0.022659147338778, 0.180723148722989, 0.298626359044260],
            [0.026496433105336, 0.245498793554607, 0.220468380201821],
            [0.036373129195418, 0.305482584796608, 0.152297894267469],
            [0.060522819643377, 0.360076573614139, 0.091691352961671],
            [0.081116009214622, 0.390636751859141, 0.059725454341826],
            [0.063352950368475, 0.368623417549019, 0.041796861087791],
            [0.046988408632270, 0.342597905636779, 0.028889944000113],
            [0.054726403228406, 0.297254271129783, 0.017681191917457],
            [0.110568321046071, 0.249018364062728, 0.012364876865565],
            [0.316047750272402, 0.192214635749393, 0.009237159175472],
            [0.463732048221454, 0.136041628030821, 0.007140017304699],
            [0.448956553433107, 0.085635739019874, 0.005222509267285],
            [0.392741250962143, 0.047247794263920, 0.004134815864185],
            [0.339257586565581, 0.029261031365458, 0.003678466835340],
            [0.275367075471943, 0.019711489043930, 0.003442532792040],
            [0.225901097315302, 0.015020203376133, 0.003751759321379],
            [0.170001446689159, 0.010765128085284, 0.004326627248599],
            [0.124233614845955, 0.008136519690130, 0.003940203973203],
            [0.061543164568938, 0.004450196619192, 0.002367904177762],
            [0.026839475779711, 0.002505569466067, 0.001515973507939],
            [0.008721968072898, 0.001425573874960, 0.001153509914116],
            [0.004458494738728, 0.001117391421727, 0.001082958854945],
        ],
        [
            [0.021160727093171, 0.003975146241944, 0.033635532081472],
            [0.065806550882905, 0.018737921399270, -0.168719238544940],
            [0.052325761228238, 0.140056359387242, -0.360944098088563],
            [0.012170284565759, 0.148251775479272, 0.001364356425645],
            [-0.001665228691833, 0.157434860682720, 0.189145789657900],
            [-0.003545181645837, 0.181238112489566, 0.198100364651556],
            [0.001264880780895, 0.201963722553195, 0.309845262948425],
            [0.006763577438418, 0.182340829833346, 0.016901049405139],
            [0.010816008391765, 0.195275360828128, -0.044212787593191],
            [0.017754680285932, 0.199101960624998, -0.048832386686802],
            [0.039483497364419, 0.078838851280208, -0.204413284621037],
            [0.079187397408507, -0.013513630893084, -0.250798472525326],
            [0.143595473707413, -0.200750395483148, -0.325529483693918],
            [0.254118576566913, -0.260199735373274, -0.358804847624876],
            [0.330058211038821, -0.300226873950545, -0.350927938576308],
            [0.300249539166331, -0.166333261704966, -0.292969194665670],
            [0.350757259994278, -0.024737275095798, -0.219474931454819],
            [0.537614303581055, 0.145752303972221, -0.168764486206991],
            [0.252782876857908, 0.303034063636591, -0.125105120389868],
            [0.036432060699235, 0.336658828422581, -0.098071642226893],
            [-0.022261517081375, 0.363722414361932, -0.068197168564714],
            [-0.057325006215470, 0.272952249086995, -0.053966227300086],
            [-0.101881734032915, 0.186453596283735, -0.046780808288388],
            [-0.225573456104208, 0.147067621435676, -0.034497423648908],
            [-0.218241801391556, 0.114693483574327, -0.034432302579158],
            [-0.248201853424336, 0.089292004357548, -0.032745220681580],
            [-0.217673160440788, 0.069698636250452, -0.026241546249328],
            [-0.002114902252771, 0.013509330240244, -0.014751096791826],
            [0.023604959617054, 0.000501753614813, -0.008081194123459],
            [0.009857818708534, -0.001524729565106, -0.001275834711673],
            [0.011029064580407, -0.001594785983066, 0.001357330441782],
        ],
        [
            [-0.004309988975027, -0.018223086534628, -0.052421150867518],
            [-0.011778032646058, 0.006714507851388, -0.108185777407753],
            [0.117721993240248, -0.010751380224935, -0.729654257063469],
            [0.130354079147339, -0.023839122392197, -0.433897708653614],
            [0.113375429504338, -0.031571436676701, -0.033322223694872],
            [0.091076110380871, 0.011056965857760, 0.059374341458545],
            [0.073081649902897, -0.005211523537450, 0.014637355149423],
            [0.080119920658227, -0.065364232539103, 0.286332344046856],
            [0.098696157315176, -0.328268712300578, 0.136735977580658],
            [0.087768413172893, -0.363574163514732, 0.096758225695688],
            [0.083481336108280, -0.477112182467364, 0.073707370267109],
            [0.085413749776661, -0.358932479044341, 0.035032091908761],
            [0.105670766026780, -0.069303884250012, 0.073141773470164],
            [0.098306140607497, 0.036587345110652, 0.104116166223933],
            [-0.011959967955416, 0.287731521894164, 0.168140808471508],
            [-0.085058305184231, 0.230757854214720, 0.169938727146765],
            [-0.172075810349947, 0.201765319548719, 0.159201303751304],
            [-0.386518874328835, 0.160302346682394, 0.136703322678275],
            [-0.213854982119529, 0.146805572544442, 0.102229884676862],
            [0.413708717558238, 0.163902086374957, 0.086002930274665],
            [0.286282676340194, 0.173177428806174, 0.056924890293709],
            [0.082088257771010, 0.186456482828721, 0.046203528783779],
            [-0.099418741164821, 0.166160446085273, 0.039256686968755],
            [-0.215346951363227, 0.138495677422786, 0.025119086886869],
            [-0.331711064179235, 0.121089091954140, 0.020184536330692],
            [-0.371430024329899, 0.096922785931456, 0.010663647196507],
            [-0.294296989504651, 0.066477156367276, 0.002034213946052],
            [0.005855712087158, 0.007124804442671, 0.005317231029937],
            [0.025140105484972, -0.000490804388833, 0.002945684646578],
            [0.000734123263960, -0.002402433448733, -0.000171277232276],
            [-0.006734036178947, -0.004868174632932, -0.000189913585875],
        ],
        [
            [-0.011932450783829, -0.018645783890481, -0.344308522924234],
            [0.058475574638404, -0.029825413330037, -0.772059187011760],
            [0.163704462660226, 0.164226010418817, -0.117757698216254],
            [0.111181737584814, 0.308204543811965, 0.330840849308760],
            [0.079949236714769, 0.337925407304040, 0.131371615247128],
            [0.066423917933273, 0.368126272975852, -0.080861034001005],
            [0.054248238237257, 0.435091065272715, -0.128528914326506],
            [0.075357193742855, 0.393422165799321, -0.166897123260280],
            [0.100163476698617, 0.103240465586451, -0.016540656358730],
            [0.103719045265512, -0.088465311023489, 0.049059022357451],
            [0.124735945916520, -0.267629472539400, 0.113812596471617],
            [0.173972213724777, -0.114694332841285, 0.132161148691658],
            [0.271270408315827, -0.033300766586062, 0.166311766592561],
            [0.372499233037028, 0.090233828268153, 0.120499902388481],
            [0.360554815926590, 0.138784492454222, 0.048021856454922],
            [0.267927534297346, 0.024123285674057, -0.014878410866256],
            [0.138881268410617, -0.024595581582219, -0.051009621655339],
            [-0.244711832337032, -0.159925001058129, -0.058528206005187],
            [-0.439806149367461, -0.139303987853964, -0.048917830122966],
            [-0.114290968328648, -0.160932332479358, -0.042372583002074],
            [-0.057258922899326, -0.213667788546929, -0.034526381254664],
            [-0.021591922850354, -0.106509577910112, -0.034034981055061],
            [0.022334073184688, -0.090827586331118, -0.028924781640274],
            [0.096860273942182, -0.071751240413694, -0.021495860192457],
            [0.167160263197135, -0.063802156430558, -0.022666429863548],
            [0.289123134615653, -0.050004494196012, -0.028015955920103],
            [0.175739116414947, -0.043704097911303, -0.021364810952033],
            [-0.091280245842045, 0.003585416147333, -0.009256348995533],
            [-0.077026261573825, 0.002595305121794, -0.011243615807535],
            [-0.026006361218915, -0.008975738427864, -0.012361900461486],
            [-0.021409793252415, -0.013578159081530, -0.009470852669032],
        ],
        [
            [0.046906236546002, 0.014605826402485, 0.002389639477927],
            [-0.049211968549663, 0.044504515338490, -0.052468130874360],
            [-0.365802561698117, -0.127073408469181, 0.005259006404977],
            [-0.260854026688281, -0.173301391463837, 0.167759013576317],
            [-0.228839265021012, -0.110445689127768, 0.359374197538974],
            [-0.205366762028393, -0.082904542288337, -0.026408426939991],
            [-0.207900345837004, 0.158095747020005, 0.320353250478407],
            [-0.242534911300270, 0.225635890649377, -0.039204521757134],
            [-0.260814036201038, 0.038962495748541, -0.117189448454830],
            [-0.220102719935655, -0.195336275732601, -0.589249260560145],
            [-0.197323948673413, 0.143941099707759, -0.220385615178451],
            [-0.173789861385581, -0.027700093299945, -0.218642230440544],
            [-0.063983389550069, -0.024182332069173, -0.039327052456266],
            [0.151239662075131, 0.540759848191117, 0.128825456046813],
            [0.181201569740636, -0.148188585425114, 0.197838445579564],
            [0.205204543064016, -0.091601128742439, 0.238043899130228],
            [0.144409388329628, -0.308820126012275, 0.232530259479385],
            [-0.193125113678900, -0.134063854657228, 0.210271778920561],
            [-0.288886894120930, -0.090234545790747, 0.160208771993245],
            [-0.044003092879323, -0.179961533752924, 0.130892953344121],
            [0.223544484535552, 0.003987265526023, 0.087411919770879],
            [0.089359296853773, 0.169347553703772, 0.070097224893036],
            [0.087011602631701, 0.263043770747226, 0.056050093752879],
            [0.131357411914828, 0.256484667537944, 0.019292834517555],
            [-0.079269918049103, 0.258857148137896, 0.002695140524853],
            [-0.207058716218617, 0.223692062410162, -0.048751442471326],
            [-0.032624397576902, 0.182581737513444, -0.054648615575268],
            [0.117865487100581, 0.051208842538089, 0.014024087222368],
            [0.114751035027465, 0.019990586179843, 0.018424489443976],
            [0.057887415793754, 0.023269772957801, 0.021658140664927],
            [0.049550369859502, 0.025366233100474, 0.016188179882089],
        ],
        [
            [-0.078411333266335, -0.025218232396168, 0.367603194273513],
            [-0.228932414546550, -0.113101498066253, 0.200936645089791],
            [0.012197965651326, -0.262426955668118, -0.374227027992151],
            [0.227896959944270, -0.125967427298347, 0.605949572996692],
            [0.186032668479669, -0.061271863516113, -0.005687175526945],
            [0.123100740851563, 0.041679827835621, 0.055934924300539],
            [0.102362151951225, 0.252577545620682, -0.379023225467773],
            [0.067483567602974, 0.178621178106894, -0.080895744906160],
            [0.047861842590741, -0.231399800204092, 0.189944985738527],
            [-0.005254793669296, -0.444321142970566, 0.127791379627731],
            [-0.094941248962405, 0.017380597063262, -0.110728962619803],
            [-0.140795945551575, 0.183610630076962, -0.221368880157934],
            [-0.216925233990225, 0.253559067118363, 0.006583597982240],
            [-0.083193936964763, 0.029943756597225, 0.060738881913470],
            [-0.090995245083803, -0.278424436377245, 0.086461055463695],
            [-0.029243784501792, -0.306350796511160, 0.054343033373090],
            [0.156803512666940, 0.125473875351587, 0.034061595241968],
            [0.340152217564400, 0.132609273944181, 0.023601622455916],
            [-0.389480156333656, 0.313761779318986, 0.012591387988104],
            [-0.249752285788506, 0.159495290558886, 0.004163791386221],
            [0.325379579218187, 0.009289829863465, -0.017548855867834],
            [0.205031638239942, -0.201463203891298, -0.023979157744712],
            [-0.000305970338765, -0.204094292725436, -0.025356519728925],
            [0.075505398103885, -0.127857958544548, -0.049604165421236],
            [-0.039718874692209, -0.106234251406174, -0.062897236314809],
            [-0.088369185475117, -0.074889567819855, -0.107591229919299],
            [-0.026945797896717, -0.027050431452033, -0.107320476930048],
            [0.052723214428869, -0.055094829580194, -0.033611010206027],
            [-0.269092499599358, -0.042295248069876, -0.023031079290309],
            [-0.311989365377289, -0.021739904807602, -0.022977794746507],
            [-0.199197027719029, -0.017008323933162, -0.030893935422190],
        ],
    ]
)
"""
*Dyer et al. (2017)* basis functions for *Jiang, Liu, Gu and Süsstrunk (2013)*
method.

Notes
-----

The *Dyer et al. (2017)* basis functions were computed as follows using
*colour-datasets*::

    shape = colour.SpectralShape(400, 700, 10)
    database_camera_sensitivities = colour_datasets.load(
        "RAW to ACES Utility Data - Dyer et al. (2017)"
    )
    database = {
        camera: msds.copy().align(shape)
        for camera, msds in database_camera_sensitivities["camera"].items()
    }

    w, v = colour.recovery.PCA_Jiang2013(database, 6, True)

    BASIS_FUNCTIONS_DYER2017 = np.transpose(w)

References
----------
:cite:`Dyer2017`
"""