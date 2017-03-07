# coding: utf-8
# Copyright © 2016 YunXing Zuo, WeiJi Hsiao

__author__ = 'YunXing Zuo, WeiJi Hsiao'
__email__ = 'weiji.hsiao@gmail.com'
__date__ = 'Oct. 25, 2016'

class ElementDoesNotExistError(Exception):
    def __init__(self, arg):
        self.__unknown_element = arg
    def __str__(self):
        return "It seems that element {} doesn't exist.".format(repr(self.__unknown_element))

class Element(object):
    def __init__(self, arg):
        """
        Create a Element object.
        Args:
            arg (str/int): An atomic symbol string or an atomic number.
        """
        if arg in elements_dict:
            self.__atomic_symbol = arg
            self.__atomic_number = elements_dict[arg]
            self.__atomic_mass = elements_data[self.atomic_number][3]
            self.__atomic_radius = elements_data[self.atomic_number][4]
            self.__atomic_radius_cal = elements_data[self.atomic_number][5]
            self.__van_der_waals_radius = elements_data[self.atomic_number][6]
        else:
            for symbol, number in elements_dict.items():
                if number == arg:
                    self.__atomic_symbol = symbol
                    self.__atomic_number = number
                    self.__atomic_mass = elements_data[self.atomic_number][3]
                    self.__atomic_radius = elements_data[self.atomic_number][4]
                    self.__atomic_radius_cal = elements_data[self.atomic_number][5]
                    self.__van_der_waals_radius = elements_data[self.atomic_number][6]
                    break
            else:
                raise ElementDoesNotExistError(arg)

    def __repr__(self):
        return self.__atomic_symbol

    def __eq__(self, other):
        if isinstance(other, Element):
            if self.atomic_number == other.atomic_number:
                return True
        return False

    def __gt__(self, other):
        if isinstance(other, Element):
            if self.atomic_number > other.atomic_number:
                return True
        return False

    def __lt__(self, other):
        if isinstance(other, Element):
            if self.atomic_number < other.atomic_number:
                return True
        return False

    @property
    def atomic_symbol(self):
        return self.__atomic_symbol

    @property
    def atomic_number(self):
        return self.__atomic_number

    @property
    def atomic_mass(self):
        return self.__atomic_mass

    @property
    def atomic_radius(self):
        return self.__atomic_radius

    @property
    def atomic_radius_cal(self):
        return self.__atomic_radius_cal

    @property
    def van_der_waals_radius(self):
        return self.__van_der_waals_radius

elements_dict = {
    "H":1,
    "He":2,
    "Li":3,
    "Be":4,
    "B":5,
    "C":6,
    "N":7,
    "O":8,
    "F":9,
    "Ne":10,
    "Na":11,
    "Mg":12,
    "Al":13,
    "Si":14,
    "P":15,
    "S":16,
    "Cl":17,
    "Ar":18,
    "K":19,
    "Ca":20,
    "Sc":21,
    "Ti":22,
    "V":23,
    "Cr":24,
    "Mn":25,
    "Fe":26,
    "Co":27,
    "Ni":28,
    "Cu":29,
    "Zn":30,
    "Ga":31,
    "Ge":32,
    "As":33,
    "Se":34,
    "Br":35,
    "Kr":36,
    "Rb":37,
    "Sr":38,
    "Y":39,
    "Zr":40,
    "Nb":41,
    "Mo":42,
    "Tc":43,
    "Ru":44,
    "Rh":45,
    "Pd":46,
    "Ag":47,
    "Cd":48,
    "In":49,
    "Sn":50,
    "Sb":51,
    "Te":52,
    "I":53,
    "Xe":54,
    "Cs":55,
    "Ba":56,
    "La":57,
    "Ce":58,
    "Pr":59,
    "Nd":60,
    "Pm":61,
    "Sm":62,
    "Eu":63,
    "Gd":64,
    "Tb":65,
    "Dy":66,
    "Ho":67,
    "Er":68,
    "Tm":69,
    "Yb":70,
    "Lu":71,
    "Hf":72,
    "Ta":73,
    "W":74,
    "Re":75,
    "Os":76,
    "Ir":77,
    "Pt":78,
    "Au":79,
    "Hg":80,
    "Tl":81,
    "Pb":82,
    "Bi":83,
    "Po":84,
    "At":85,
    "Rn":86,
    "Fr":87,
    "Ra":88,
    "Ac":89,
    "Th":90,
    "Pa":91,
    "U":92,
    "Np":93,
    "Pu":94,
    "Am":95,
    "Cm":96,
    "Bk":97,
    "Cf":98,
    "Es":99,
    "Fm":100,
    "Md":101,
    "No":102,
    "Lr":103,
    "Rf":104,
    "Db":105,
    "Sg":106,
    "Bh":107,
    "Hs":108,
    "Mt":109,
    "Ds":110,
    "Rg":111,
    "Cn":112,
    "Uut":113,
    "Uuq":114,
    "Uup":115,
    "Uuh":116,
    "Uus":117,
    "Uuo":118,
    }

elements_data = [
    [0,"X","X",None,None,None,None,None,None],
    [1,"H","Hydrogen",1.00794,25,53,120,38,None],
    [2,"He","Helium",4.002602,None,31,140,32,None],
    [3,"Li","Lithium",6.941,145,167,182,134,None,152],
    [4,"Be","Beryllium",9.012182,105,112,153,90,85,112],
    [5,"B","Boron",10.811,85,87,192,82,73],
    [6,"C","Carbon",12.0107,70,67,170,77,60],
    [7,"N","Nitrogen",14.0067,65,56,155,75,54],
    [8,"O","Oxygen",15.9994,60,48,152,73,53],
    [9,"F","Fluorine",18.9984032,50,42,147,71,53],
    [10,"Ne","Neon",20.1797,None,38,154,69,None],
    [11,"Na","Sodium",22.98976928,180,190,227,154,None,186],
    [12,"Mg","Magnesium",24.3050,150,145,173,130,127,160],
    [13,"Al","Aluminium",26.9815386,125,118,184,118,111,143],
    [14,"Si","Silicon",28.0855,110,111,210,111,102],
    [15,"P","Phosphorus",30.973762,100,98,180,106,94],
    [16,"S","Sulfur",32.065,100,88,180,102,95],
    [17,"Cl","Chlorine",35.453,100,79,175,99,93],
    [18,"Ar","Argon",39.948,71,71,188,97,96],
    [19,"K","Potassium",39.0983,220,243,275,196,None,227],
    [20,"Ca","Calcium",40.078,180,194,231,174,133,197],
    [21,"Sc","Scandium",44.955912,160,184,211,144,114,162],
    [22,"Ti","Titanium",47.867,140,176,None,136,108,147],
    [23,"V","Vanadium",50.9415,135,171,None,125,106,134],
    [24,"Cr","Chromium",51.9961,140,166,None,127,103,128],
    [25,"Mn","Manganese",54.938045,140,161,None,139,103,127],
    [26,"Fe","Iron",55.845,140,156,None,125,102,126],
    [27,"Co","Cobalt",58.933195,135,152,None,126,96,125],
    [28,"Ni","Nickel",58.6934,135,149,163,121,101,124],
    [29,"Cu","Copper",63.546,135,145,140,138,120,128],
    [30,"Zn","Zinc",65.38,135,142,139,131,None,134],
    [31,"Ga","Gallium",69.723,130,136,187,126,121,135],
    [32,"Ge","Germanium",72.64,125,125,211,122,114],
    [33,"As","Arsenic",74.92160,115,114,185,119,106],
    [34,"Se","Selenium",78.96,115,103,190,116,107],
    [35,"Br","Bromine",79.904,115,94,185,114,110],
    [36,"Kr","Krypton",83.798,None,88,202,110,108],
    [37,"Rb","Rubidium",85.4678,235,265,303,211,None,248],
    [38,"Sr","Strontium",87.62,200,219,249,192,139,215],
    [39,"Y","Yttrium",88.90585,180,212,None,162,124,180],
    [40,"Zr","Zirconium",91.224,155,206,None,148,121,160],
    [41,"Nb","Niobium",92.90638,145,198,None,137,116,146],
    [42,"Mo","Molybdenum",95.96,145,190,None,145,113,139],
    [43,"Tc","Technetium",None,135,183,None,156,110,136],
    [44,"Ru","Ruthenium",101.07,130,178,None,126,103,134],
    [45,"Rh","Rhodium",102.90550,135,173,None,135,106,134],
    [46,"Pd","Palladium",106.42,140,169,163,131,112,137],
    [47,"Ag","Silver",107.8682,160,165,172,153,137,144],
    [48,"Cd","Cadmium",112.411,155,161,158,148,None,151],
    [49,"In","Indium",114.818,155,156,193,144,146,167],
    [50,"Sn","Tin",118.710,145,145,217,141,132],
    [51,"Sb","Antimony",121.760,145,133,206,138,127],
    [52,"Te","Tellurium",127.60,140,123,206,135,121],
    [53,"I","Iodine",126.90447,140,115,198,133,125],
    [54,"Xe","Xenon",131.293,None,108,216,130,122],
    [55,"Cs","Caesium",132.9054519,260,298,343,225,None,265],
    [56,"Ba","Barium",137.327,215,253,268,198,149,222],
    [57,"La","Lanthanum",138.90547,195,None,None,169,139,187],
    [58,"Ce","Cerium",140.116,185,None,None,None,131,181.8],
    [59,"Pr","Praseodymium",140.90765,185,247,None,None,128,182.4],
    [60,"Nd","Neodymium",144.242,185,206,None,None,None,181.4],
    [61,"Pm","Promethium",None,185,205,None,None,None,183.4],
    [62,"Sm","Samarium",150.36,185,238,None,None,None,180.4],
    [63,"Eu","Europium",151.964,185,231,None,None,None,180.4],
    [64,"Gd","Gadolinium",157.25,180,233,None,None,132,180.4],
    [65,"Tb","Terbium",158.92535,175,225,None,None,None,177.3],
    [66,"Dy","Dysprosium",162.500,175,228,None,None,None,178.1],
    [67,"Ho","Holmium",164.93032,175,None,None,None,None,176.2],
    [68,"Er","Erbium",167.259,175,226,None,None,None,176.1],
    [69,"Tm","Thulium",168.93421,175,222,None,None,None,175.9],
    [70,"Yb","Ytterbium",173.054,175,222,None,None,None,176],
    [71,"Lu","Lutetium",174.9668,175,217,None,160,131,173.8],
    [72,"Hf","Hafnium",178.49,155,208,None,150,122,159],
    [73,"Ta","Tantalum",180.94788,145,200,None,138,119,146],
    [74,"W","Tungsten",183.84,135,193,None,146,115,139],
    [75,"Re","Rhenium",186.207,135,188,None,159,110,137],
    [76,"Os","Osmium",190.23,130,185,None,128,109,135],
    [77,"Ir","Iridium",192.217,135,180,None,137,107,135.5],
    [78,"Pt","Platinum",195.084,135,177,175,128,110,138.5],
    [79,"Au","Gold",196.966569,135,174,166,144,123,144],
    [80,"Hg","Mercury",200.59,150,171,155,149,None,151],
    [81,"Tl","Thallium",204.3833,190,156,196,148,150,170],
    [82,"Pb","Lead",207.2,180,154,202,147,137],
    [83,"Bi","Bismuth",208.98040,160,143,207,146,135],
    [84,"Po","Polonium",None,190,135,197,None,129],
    [85,"At","Astatine",None,None,None,202,None,138],
    [86,"Rn","Radon",None,None,120,220,145,133],
    [87,"Fr","Francium",None,None,None,348,None,None,None],
    [88,"Ra","Radium",None,215,None,283,None,159,None],
    [89,"Ac","Actinium",None,195,None,None,None,140],
    [90,"Th","Thorium",232.03806,180,None,None,None,136,179],
    [91,"Pa","Protactinium",231.03588,180,None,None,None,129,163],
    [92,"U","Uranium",238.02891,175,None,186,None,118,156],
    [93,"Np","Neptunium",None,175,None,None,None,116,155],
    [94,"Pu","Plutonium",None,175,None,None,None,None,159],
    [95,"Am","Americium",None,175,None,None,None,None,173],
    [96,"Cm","Curium",None,None,None,None,None,None,174],
    [97,"Bk","Berkelium",None,None,None,None,None,None,170],
    [98,"Cf","Californium",None,None,None,None,None,None,186],
    [99,"Es","Einsteinium",None,None,None,None,None,None,186],
    [100,"Fm","Fermium",None,None,None,None,None,None,None],
    [101,"Md","Mendelevium",None,None,None,None,None,None,None],
    [102,"No","Nobelium",None,None,None,None,None,None,None],
    [103,"Lr","Lawrencium",None,None,None,None,None,None,None],
    [104,"Rf","Rutherfordium",None,None,None,None,None,131,None],
    [105,"Db","Dubnium",None,None,None,None,None,126,None],
    [106,"Sg","Seaborgium",None,None,None,None,None,121,None],
    [107,"Bh","Bohrium",None,None,None,None,None,119,None],
    [108,"Hs","Hassium",None,None,None,None,None,118,None],
    [109,"Mt","Meitnerium",None,None,None,None,None,113,None],
    [110,"Ds","Darmstadtium",None,None,None,None,None,112,None],
    [111,"Rg","Roentgenium",None,None,None,None,None,118,None],
    [112,"Cn","Copernicium",None,None,None,None,None,130,None],
    [113,"Uut","Ununtrium",None,None,None,None,None,None,None],
    [114,"Uuq","Ununquadium",None,None,None,None,None,None,None],
    [115,"Uup","Ununpentium",None,None,None,None,None,None,None],
    [116,"Uuh","Ununhexium",None,None,None,None,None,None,None],
    [117,"Uus","Ununseptium",None,None,None,None,None,None,None],
    [118,"Uuo","Ununoctium",None,None,None,None,None,None,None]
    ]