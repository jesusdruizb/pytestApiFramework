import pytest
import jsonpath
import requests
from cerberus import Validator
import json
from assertpy import assert_that
from common.api.PokemonEndpoints import PokemonEndpoints
from common.api.RestRequests import RestRequests
from common.api.FileOperations import FileOperations
from common.JsonOperations import JsonOperations

json_operations = JsonOperations()
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


pokemon_name_list = file_operations.read_file_as_json_readonly("data/pokemonApi/pokemon_list.json")
@pytest.mark.parametrize('pokemon',pokemon_name_list)
@pytest.mark.Smoke
def test_validate_pokemon_data_2(pokemon):
    pokemon_resource = pkm_endpoints.pokemon_name_resource(pokemon)
    resource_url=pokemon_base_endpoint[0]+pokemon_resource
    pkmn_response = rest_requests.get_request(resource_url)
    assert pkmn_response.status_code == requests.codes.ok
    assert pkmn_response.text is not None
    assert pkmn_response.text != ''


pokemon_name_list = file_operations.read_file_as_json_readonly("data/pokemonApi/pokemon_list.json")
@pytest.mark.parametrize('pokemon',pokemon_name_list)
@pytest.mark.Smoke
def test_validate_pokemon_data_fluent(pokemon):
    pokemon_resource = pkm_endpoints.pokemon_name_resource(pokemon)
    resource_url=pokemon_base_endpoint[0]+pokemon_resource
    pkmn_response = rest_requests.get_request(resource_url)
    assert_that(pkmn_response.status_code).is_equal_to(requests.codes.ok)
    assert_that(pkmn_response.text).is_not_none()
    assert_that(pkmn_response.text).is_not_empty()
    assert_that(json_operations.search_response_by_jsonpath(pkmn_response, 'name')).is_not_empty().contains(pokemon)


pokemon_move_list = file_operations.read_file_as_json_readonly("data/pokemonApi/move_list.json")
@pytest.mark.parametrize('move',pokemon_move_list)
@pytest.mark.Smoke
def test_validate_pokemon_moves_endpoint(move):
    # Setup
    moves_schema = file_operations.read_file_as_json_readonly('data/pokemonApi/schemas/moves_schema.json')
    validator = Validator(moves_schema, require_all=False)
    pokemon_resource = pkm_endpoints.pokemon_move_base_resource(move)
    resource_url=pokemon_base_endpoint[0]+pokemon_resource

    # Execution
    pkmn_response = rest_requests.get_request(resource_url)
    # print(json.dumps(json_operations.transform_response_to_json(pkmn_response)))

    # Validation
    is_valid_schema = validator.validate(json_operations.transform_response_to_json(pkmn_response))
    assert_that(is_valid_schema, description = validator.errors).is_true()
    assert_that(pkmn_response.status_code).is_equal_to(requests.codes.ok)
    assert_that(pkmn_response.text).is_not_none()
    assert_that(pkmn_response.text).is_not_empty()