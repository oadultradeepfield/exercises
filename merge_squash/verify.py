from git_autograder import (
    GitAutograderOutput,
    GitAutograderExercise,
    GitAutograderStatus,
)

UNCOMMITTED_CHANGES = "You still have uncommitted changes. Commit them first!"
NOT_ON_MAIN = (
    "You aren't currently on the main branch. Checkout to that branch and try again!"
)
DETACHED_HEAD = "You should not be in a detached HEAD state! Use git checkout main to get back to main"
NO_SQUASH_MERGE = "You need to squash merge the supporting branch onto main"
FAST_FORWARD_MERGE = "You performed a fast-forward merge instead of a squash merge. The supporting branch commits should be squashed into one commit."
REGULAR_MERGE = "You performed a regular merge instead of a squash merge. The supporting branch commits should be squashed into one commit."
RESET_MESSAGE = 'Reset the repository using "gitmastery progress reset" and start again'


def verify(exercise: GitAutograderExercise) -> GitAutograderOutput:
    main_branch = exercise.repo.branches.branch("main")
    if exercise.repo.repo.is_dirty():
        raise exercise.wrong_answer([UNCOMMITTED_CHANGES])

    try:
        if exercise.repo.repo.active_branch.name != "main":
            raise exercise.wrong_answer([NOT_ON_MAIN])
    except TypeError:
        raise exercise.wrong_answer([DETACHED_HEAD])

    main_reflog = main_branch.reflog
    merge_logs = [entry for entry in main_reflog if entry.action.startswith("merge")]

    if len(merge_logs) == 0:
        raise exercise.wrong_answer([NO_SQUASH_MERGE, RESET_MESSAGE])

    latest_merge = merge_logs[-1]
    if latest_merge.action != "merge supporting":
        raise exercise.wrong_answer([NO_SQUASH_MERGE, RESET_MESSAGE])

    if "squash" not in latest_merge.message.lower():
        raise exercise.wrong_answer([REGULAR_MERGE, RESET_MESSAGE])

    return exercise.to_output(
        ["Great work squash merging the supporting branch!"],
        GitAutograderStatus.SUCCESSFUL,
    )
