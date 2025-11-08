from exercise_utils.file import create_or_update_file
from exercise_utils.git import add, commit, checkout
from exercise_utils.gitmastery import create_start_tag


def setup(verbose: bool = False):
    create_start_tag(verbose)

    create_or_update_file("joey.txt", "Matt LeBlanc")
    add(["joey.txt"], verbose)
    commit("Add Joey", verbose)

    create_or_update_file("phoebe.txt", "Lisa Kudrow")
    add(["phoebe.txt"], verbose)
    commit("Add Phoebe", verbose)

    checkout("supporting", True, verbose)
    create_or_update_file("mike.txt", "Paul Rudd")
    add(["mike.txt"], verbose)
    commit("Add Mike", verbose)

    create_or_update_file("janice.txt", "Maggie Wheeler")
    add(["janice.txt"], verbose)
    commit("Add Janice", verbose)

    checkout("main", False, verbose)
    create_or_update_file("ross.txt", "David Schwimmer")
    add(["ross.txt"], verbose)
    commit("Add Ross", verbose)
