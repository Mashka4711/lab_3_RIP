import Child
from datetime import datetime

user=Child.Client("http://api.vk.com/method","users.get")
user.param="user_ids="+input("Введите vk-id пользователя или username: ")
resp=user.execute()
id=user.findId(resp)

friend=Child.Client('http://api.vk.com/method','friends.get')
friend.param="user_id="+str(id)+"&fields=bdate"
friends=friend.execute()

friend_l=friends.get('response')
friend_dict=friend.friends_count(friend_l)
friend.print_friends(friend_dict)