from recordclass import recordclass

VelColor = recordclass("VelColor", "red green blue")

LAUNCHPAD_COLORS = [
    VelColor(  0,   0,   0),  #   0: off
    VelColor( 28,  28,  28),
    VelColor(124, 124, 124),  #   2: gray
    VelColor(252, 252, 252),  #   3: white
    VelColor(255,  74,  71),    VelColor(255,  10,   0),  #   5: red    VelColor( 90,   1,   0),
    VelColor( 25,   0,   0),
    VelColor(255, 189,  98),
    VelColor(255,  86,   0),
    VelColor( 90,  29,   0),  #  10
    VelColor( 36,  24,   0),
    VelColor(253, 253,  33),
    VelColor(253, 253,   0),
    VelColor( 88,  88,   0),
    VelColor( 24,  24,   0),
    VelColor(128, 253,  42),
    VelColor( 64, 253,   0),
    VelColor( 22,  88,   0),
    VelColor( 19,  40,   0),
    VelColor( 52, 253,  43),  #  20
    VelColor(  0, 253,   0),  #  21: green
    VelColor(  0,  88,   0),
    VelColor(  0,  24,   0),
    VelColor( 51, 253,  70),
    VelColor(  0, 253,   0),  #  25: green
    VelColor(  0,  88,   0),
    VelColor(  0,  24,   0),
    VelColor( 50, 253, 126),
    VelColor(  0, 253,  58),
    VelColor(  0,  88,  20),  #  30
    VelColor(  0,  28,  15),
    VelColor( 47, 252, 176),
    VelColor(  0, 252, 145),
    VelColor(  0,  88,  49),
    VelColor(  0,  24,  15),
    VelColor( 57, 191, 255),
    VelColor(  0, 167, 255),
    VelColor(  0,  64,  81),
    VelColor(  0,  16,  24),
    VelColor( 65, 134, 255),  #  40
    VelColor(  0,  80, 255),
    VelColor(  0,  26,  90),
    VelColor(  0,   7,  25),
    VelColor( 70,  71, 255),
    VelColor(  0,   0, 255),  #  45: blue
    VelColor(  0,   0,  91),
    VelColor(  0,   0,  25),
    VelColor(131,  71, 255),
    VelColor( 80,   0, 255),
    VelColor( 22,   0, 103),  #  50
    VelColor( 11,   0,  50),
    VelColor(255,  73, 255),
    VelColor(255,   0, 255),
    VelColor( 90,   0,  90),
    VelColor( 25,   0,  25),
    VelColor(255,  77, 132),
    VelColor(255,   7,  82),
    VelColor( 90,   1,  27),
    VelColor( 33,   0,  16),
    VelColor(255,  25,   0),  #  60: red
    VelColor(155,  53,   0),
    VelColor(122,  81,   0),
    VelColor( 62, 100,   0),
    VelColor(  0,  56,   0),
    VelColor(  0,  84,  50),
    VelColor(  0,  83, 126),
    VelColor(  0,   0, 255),  #  67: blue
    VelColor(  0,  68,  77),
    VelColor( 27,   0, 210),
    VelColor(124, 124, 124),  #  70: grey
    VelColor( 32,  32,  32),
    VelColor(255,  10,   0),  #  72: red
    VelColor(186, 253,   0),
    VelColor(170, 237,   0),
    VelColor( 86, 253,   0),
    VelColor(  0, 136,   0),
    VelColor(  0, 252, 122),
    VelColor(  0, 167, 255),
    VelColor(  0,  27, 255),  #  79: blue
    VelColor( 53,   0, 255),  #  80
    VelColor(119,   0, 255),
    VelColor(180,  23, 126),
    VelColor( 65,  32,   0),
    VelColor(255,  74,   0),
    VelColor(131, 225,   0),
    VelColor(101, 253,   0),
    VelColor(  0, 253,   0),  #  87: green
    VelColor(  0, 253,   0),  #  88: green
    VelColor( 69, 253,  97),
    VelColor(  0, 252, 202),  #  90
    VelColor( 80, 134, 255),
    VelColor( 39,  77, 201),
    VelColor(130, 122, 237),
    VelColor(211,  12, 255),
    VelColor(255,   6,  90),
    VelColor(255, 125,   0),
    VelColor(185, 177,   0),
    VelColor(138, 253,   0),
    VelColor(130,  93,   0),
    VelColor( 57,  40,   0),  # 100
    VelColor( 13,  76,   5),
    VelColor(  0,  80,  55),
    VelColor( 19,  19,  41),
    VelColor( 16,  31,  90),
    VelColor(106,  60,  23),
    VelColor(172,   4,   0),
    VelColor(225,  81,  53),
    VelColor(220, 105,   0),
    VelColor(255, 225,   0),
    VelColor(153, 225,   0),  # 110
    VelColor( 95, 181,   0),
    VelColor( 27,  27,  49),
    VelColor(220, 253,  84),
    VelColor(118, 252, 184),
    VelColor(150, 151, 255),
    VelColor(139,  97, 255),
    VelColor( 64,  64,  64),  # 117: grey
    VelColor(116, 116, 116),  # 118: grey
    VelColor(222, 252, 252),
    VelColor(164,   4,   0),  # 120
    VelColor( 53,   0,   0),
    VelColor(  0, 209,   0),
    VelColor(  0,  64,   0),
    VelColor(185, 177,   0),
    VelColor( 61,  48,   0),
    VelColor(180,  93,   0),
    VelColor( 74,  20,   0)   # 127
]