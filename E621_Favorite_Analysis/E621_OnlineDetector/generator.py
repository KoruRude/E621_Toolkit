login = input("Enter login account name for API: ")
api_key = input("Enter API Key: ")
discord_webhook_URL = input("Enter Discord Webhook URL: ")


target_user = input("Enter username of target: ")
user_id = input("Enter user ID of target: ")

def append(input):
	with open("runner" + target_user + ".sh", "a") as myfile:
		myfile.write(input)
		myfile.write("\n")

append('rm "' + user_id + '.json?login"*')
append('wget "https://e621.net/users/' + user_id + '.json?login=' + login + '&api_key=' + api_key +'" --user-agent "Delta Ping Test"')

append('newJSON=$(cat "' + user_id + '.json?login"*)')

append('oldJSON=$(cat "oldJSON' + str(user_id) + '.json")')

append('if [ "$newJSON" = "$oldJSON" ]; then')
append('	echo "Infromation matches, no action taken"')
append('else')
append('	echo "Infromation does not match, taking action..."')
append('	cat ' + user_id + '.json* > oldJSON' + str(user_id) + '.json')

append('	cat ' + user_id + '.json* > "log/' + target_user + '_$(date +%F%t%r).json"')

append("	url='" + discord_webhook_URL + "';")
append('generate_post_data() {')
append('	cat <<EOF')
append('{')
append('	"content": "Change Detected for \`' + target_user + '(' + user_id + ')\` on \`$(date)\`"')
append('}')
append('EOF')
append('}')

append('echo "$(generate_post_data)"')

append('curl -H "Content-Type: application/json" -X POST -d "$(generate_post_data)" $url')

append('fi')



