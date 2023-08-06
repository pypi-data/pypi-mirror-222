from histcite.parse_reference import ParseReference

def test_wos_cr():
    cr_cell = 'Bengio Y, 2001, ADV NEUR IN, V13, P932; Chang Y, 2003, IEEE INTERNATIONAL WORKSHOP ON ANALYSIS AND MODELING OF FACE AND GESTURES, P28; Chen Z., 2000, 6 INT C SPOK LANG PR; CORTES C, 1995, MACH LEARN, V20, P273, DOI 10.1007/BF00994018; '
    parsed_citation_dict = ParseReference(0,cr_cell,'wos').parse_cr_cell()
    assert parsed_citation_dict is not None
    assert parsed_citation_dict[0]['First_AU']=='Bengio Y'
    assert parsed_citation_dict[0]['PY']=='2001'
    assert parsed_citation_dict[0]['VL']=='13'

def test_cssci_cr():
    cr_cell = '1.严栋.基于物联网的智慧图书馆.图书馆学刊.2010.32(7)'
    parsed_citation_dict = ParseReference(0,cr_cell,'cssci').parse_cr_cell()
    assert parsed_citation_dict is not None
    assert parsed_citation_dict[0]['First_AU']=='严栋'
    assert parsed_citation_dict[0]['TI']=='基于物联网的智慧图书馆'
    assert parsed_citation_dict[0]['VL']=='32(7)'

def test_scopus_cr():
    cr_cell = 'Negri E, Fumagalli L, Macchi M., A Review of the Roles of Digital Twin in CPS-based Production Systems, Procedia Manufacturing, 11, pp. 939-948, (2017); '
    parsed_citation_dict = ParseReference(0,cr_cell,'scopus').parse_cr_cell()
    assert parsed_citation_dict is not None
    assert parsed_citation_dict[0]['First_AU']=='Negri E'
    assert parsed_citation_dict[0]['TI']=='A Review of the Roles of Digital Twin in CPS-based Production Systems'
    assert parsed_citation_dict[0]['SO']=='Procedia Manufacturing'
    assert parsed_citation_dict[0]['VL']=='11'