from mit_campus import Location, MITCampus


def test_mit_campus():
    c = MITCampus(Location(1, 2))
    assert(c.add_tent(Location(2, 3)) == True)
    assert(c.add_tent(Location(1, 2)) == True)
    assert(c.add_tent(Location(0, 0)) == False)
    assert(c.add_tent(Location(2, 3)) == False)
    assert(c.get_tents() == ['<0,0>', '<1,2>', '<2,3>'])
