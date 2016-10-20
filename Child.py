import requests
import Base
from datetime import datetime

class Client(Base.BaseClient):

    def __init__(self,url,method):
     self.BASE_URL=url
     self.method=method

    def generate_url(self, method):
        return '{0}/{1}'.format(self.BASE_URL, method)

    def _get_data(self, method):
        response=requests.get(self.generate_url(method),self.param)
        return response.json()

    def findId(self,inf):
        try:
            id1 = inf.get("response")
            id = id1[0].get('uid')
        except:
            print ("Пользователь не найден!!!")
            exit()
        return id

    def age_count(self,date):
        try:
            date=datetime.strptime(date,'%d.%m.%Y')
        except: return None
        year_now=datetime.now().year
        month_now=datetime.now().month
        day_now=datetime.now().day
        age=year_now-date.year
        if (month_now == date.month and date.day > day_now) or date.month > month_now:
            age -= 1
        return age

    def friends_count(self,friend_l):
        if (friend_l == None):
            print ('Пользователь заблокирован или страница удалена!!!')
            exit()
        if (len(friend_l) == 0):
            print ('У пользователя нет друзей, или они скрыты!!!')
            exit()
        friend_none={'Не указан возраст у: ':0}
        for friend in friend_l:
            date = friend.get('bdate')
            age = self.age_count(date)
            if (age == None):
                friend_none['Не указан возраст у: '] += 1
                continue
            if (friend_none.get(age) == None):
                friend_none[age] = ''
            friend_none[age] += '*'
        return friend_none

    def print_friends(self,dict):
        print('Не указан возраст у: ', dict['Не указан возраст у: '])
        del dict['Не указан возраст у: ']
        for key in sorted(dict):
            print(key, ': ', dict[key])

