# Models
from src.models.lenguageModel import lenguageModel

def test_get_lenguage_not_none():
    lenguages=lenguageModel.get_lenguages()
    assert lenguages == None