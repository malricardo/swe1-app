"""Notes: Git branch and pull request workflow."""

# Create and switch to a new branch.
git_switch_new_branch = "git switch -c ci-test"

# Push the branch to GitHub.
git_push_branch = "git push -u origin ci-test"

# Open a pull request on GitHub from ci-test into main.
# Travis CI runs checks for the pull request before it is merged.

# After merging the pull request, switch back to the local main branch.
git_switch_main = "git switch main"

# Download and apply the latest changes from GitHub main.
git_pull_main = "git pull origin main"

# Workflow summary:
# 1. Make changes on a separate branch.
# 2. Push the branch to GitHub.
# 3. Open and review a pull request into main.
# 4. Wait for passing CI checks.
# 5. Merge the pull request.
# 6. Update the local main branch with git switch and git pull.
