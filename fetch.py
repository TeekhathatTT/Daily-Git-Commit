# from git import Repo

# # Repo.clone_from('https://github.com/TeekhathatTT/Daily-Git-Commit', 'D:\daily_commit\Daily')

# FILE_TO_COMMIT_NAME = 'update_me.yaml'


# repo_path = 'D:/daily_commit/Daily'

# # Initialize the Repo object by providing the path to the Git repository
# repo = Repo(repo_path)

# repo.index.add([FILE_TO_COMMIT_NAME])
# commit_message = f'Updated {yaml_data["UPDATE_TIMES"]} times. Last update was on {yaml_data["LAST_UPDATE"]}.'
# repo.index.commit(commit_message)
# origin = repo.remote('origin')
# origin.push()

# print(repo)