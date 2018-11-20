from DataBase.DBControl import *
from enum import Enum

DBQuery = DBQuery()


class state(Enum):
    ok = 1
    fail = 2


def login1(username, passwd):
    
    new_user = User(id='1', name=username, passwd=passwd,
                    userTpye=UserTpye.ordinary)
    if DBQuery.login(new_user) == True:
        return state.ok
    else:
        return state.fail


def login(ls):
    return login1(ls[0], ls[1])
