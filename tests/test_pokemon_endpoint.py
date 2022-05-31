import json
import pytest
import jsonpath
from common.api.PokemonEndpoints import PokemonEndpoints
from common.api.RestRequests import RestRequests
from common.api.FileOperations import FileOperations

file_operations = FileOperations()
rest_requests = RestRequests()
pkm_endpoints = PokemonEndpoints()

# read env vars to determine base endpoint for tests
env_vars = file_operations.read_file_as_json_readonly('env_vars.json')
pokemon_base_endpoint = jsonpath.jsonpath(env_vars, 'pokeApiUrl')

@pytest.fixture(scope="module",autouse=True)
def before_all_after_all():
    print(" ")
    print("before all")
    print("---------------------------")
    yield
    print(" ")
    print("after all")
    print("---------------------------")


@pytest.fixture(autouse=True)
def before_each_after_each():
    print(" ")
    print("beforeEach")
    print("---------------------------")
    yield
    print(" ")
    print("afterEach")
    print("---------------------------")


pokemon_name_list = file_operations.read_file_as_json_readonly("fixtures/pokemonApi/pokemon_list.json")
@pytest.mark.parametrize('pokemon',pokemon_name_list)
def test_validate_pokemon_data_2(pokemon):
    pokemon_resource = pkm_endpoints.pokemon_name_resource(pokemon)
    resource_url=pokemon_base_endpoint[0]+pokemon_resource
    pkmn_response = rest_requests.get_request(resource_url)
    assert pkmn_response.status_code == 201
    assert pkmn_response.text is not None
    assert pkmn_response.text != ''
