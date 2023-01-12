import requests
# from models import User


if __name__ == '__main__':
	r = requests.get('https://jsonplaceholder.typicode.com/users')
	users = r.json()
	users_info = [
	# {
	# 	'username': x.get('username'),
	# 	'email': x.get('email'),
	# 	'age': x.get('age', 25),
	# 	'country': x.get('address').get('city'),
	# } 
	f'user = User(username=\'{x.get("username")}\', email=\'{x.get("email")}\', age={x.get("age", 25)}, country=\'{x.get("address").get("city")}\')'
	for x in users]

	print(len(users_info))
	for user_info in users_info:
		print(user_info)