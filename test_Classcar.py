"""Test Car class functions."""

import Classcar


def test_turn_on_the_car():
    #Test that method

    assert result in (True, "Please create a car first!")
    # Assert result
if __name__ == "__main__":
    test_turn_on_the_car()
'''
def test_drive():
    #Test drive method

    Test that look at results in cannot see message when one cannot see"""
    blind_person = person.Person()
    blind_person.can_see = False
    
    other_person = person.Person()
    
    #expect this to say that blind_person cannot see
    expected = blind_person.look_at(other_person)
    
    assert expected == f"{blind_person.name} is unable to see."

def test_look_at_can_see():
    """Test that look_at can see when appropriate."""
    sighted_person = person.Person()
    sighted_person.can_see = True
    
    other_person = person.Person()
    
    expected = f"{other_person.to_string()}"
    
    assert expected == sighted_person.look_at(other_person)

def test_succeed():
    assert True

#def test_fail():
#    assert False'''