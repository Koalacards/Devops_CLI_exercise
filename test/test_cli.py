import pytest

from src.cli import CLIObject

cli = CLIObject("test_json.json")

def test_ls():
    ls = cli.ls()
    assert ls == "Current Employee Usernames:\ntestuser\nhdeangelis"

def test_get_hdeangelis():
    get_hdeangelis = cli.get("hdeangelis")
    assert get_hdeangelis == "Employee information for username hdeangelis: \n First name: Hayden \n Last name: DeAngelis \n Department: SRE"

def test_get_bad_username():
    bad_user = cli.get("notausername")
    assert bad_user == "An employee with username notausername could not be found. Please use ls to recieve the list of employee usernames."
