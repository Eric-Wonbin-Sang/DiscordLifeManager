import os


project_dir = "/".join(os.path.dirname(os.path.realpath(__file__)).replace("\\", "/").split("/")[:-1])
projects_dir = "/".join(project_dir.split("/")[:-1])
secrets_dir = projects_dir + "/" + "0 - Secrets"

discord_credentials = open(secrets_dir + "/DiscordLifeBot/discord-token.txt").read()

weight_spreadsheet_credentials = secrets_dir + "/DiscordLifeBot/DiscordLifeBot-service-account-key.json"
