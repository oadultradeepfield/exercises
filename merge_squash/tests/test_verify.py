from git_autograder import GitAutograderStatus, GitAutograderTestLoader, assert_output

from ..verify import (
    NO_SQUASH_MERGE,
    NOT_ON_MAIN,
    REGULAR_MERGE,
    RESET_MESSAGE,
    UNCOMMITTED_CHANGES,
    verify,
)

REPOSITORY_NAME = "merge-squash"

loader = GitAutograderTestLoader(__file__, REPOSITORY_NAME, verify)


def test_base():
    with loader.load("specs/base.yml", "start") as output:
        assert_output(output, GitAutograderStatus.SUCCESSFUL)


def test_no_merge():
    with loader.load("specs/no_merge.yml", "start") as output:
        assert_output(
            output,
            GitAutograderStatus.UNSUCCESSFUL,
            [NO_SQUASH_MERGE, RESET_MESSAGE],
        )


def test_regular_merge():
    with loader.load("specs/regular_merge.yml", "start") as output:
        assert_output(
            output,
            GitAutograderStatus.UNSUCCESSFUL,
            [REGULAR_MERGE, RESET_MESSAGE],
        )


def test_uncommitted():
    with loader.load("specs/uncommitted.yml") as output:
        assert_output(output, GitAutograderStatus.UNSUCCESSFUL, [UNCOMMITTED_CHANGES])


def test_not_main():
    with loader.load("specs/not_main.yml") as output:
        assert_output(output, GitAutograderStatus.UNSUCCESSFUL, [NOT_ON_MAIN])
