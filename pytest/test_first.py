from _pytest.warning_types import PytestExperimentalApiWarning
import pytest

def test_our_first_test() -> None:
    assert 1==1


@pytest.mark.skip
def test_skip_uncond() -> None:
    assert 1 == 3


@pytest.mark.skipif(2==1, reason="1 is obsly equal to 1")
def test_skip_cond() -> None:
    assert 1==1


@pytest.mark.xfail
def  test_dont_care_if_fails() -> None:
    assert 1==1


@pytest.mark.slow  #use -p no:warining to not to show any warnings  
def test_custom_mark() -> None:
    assert 1==1
    #to only run this test -m slow or to deselect it run -m "no slow"


class Company:
    def __init__(self, name:str, stock_symbol:str):
        self.name= name
        self.stock_symbol= stock_symbol

    def __str__(self):
        return (f"{self.name}:{self.stock_symbol}")


@pytest.fixture
def company() -> Company:
    return Company(name="Start", stock_symbol="SU")



def test_with_fixture(company: Company) -> None:
    print(f"Printing {company} from fixture")


@pytest.mark.parametrize(
    "companyNames",
    ["Apple","Google"],
    ids=["apple_test","google_test"],
) 


def test_parametrized(companyNames:str) -> None:
    print(f"\n Test with {companyNames}")


def raise_covid_error() -> None:
    raise ValueError("Error detected")

@pytest.mark.new
def test_raise_covid() -> None:
    with pytest.raises(ValueError) as error:
        raise_covid_error()
    assert "Error detected" == str(error.value)

