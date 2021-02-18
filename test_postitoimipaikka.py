import postinumerot

def test_vain_yksi_postinumero():
    tulos = postinumerot.main("KORVATUNTURI")
    
    assert len(tulos) == 1


def test_useampi_postinumero():
    tulos = postinumerot.main("KIURUVESI")

    assert len(tulos) == 2

#epäonnistunut haku palauttaa tyhjän taulukon
def test_postinumero_jota_ei_loydy():
    tulos = postinumerot.main("Los Angeles")

    assert len(tulos) == 0
"""
#en korjannut bugia, tein vain testin.
def test_smartpost_bugi():
    tulos1 = postinumerot.main("SMARTPOST")
    tulos2 = postinumerot.main("SMART POST")
    tulos3 = postinumerot.main("SMARTPSOT")

    assert tulos1 == tulos2 and tulos1 == tulos3
    """
