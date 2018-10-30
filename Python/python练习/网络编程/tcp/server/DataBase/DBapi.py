# DB API design
# register
    #  1.len of name and psswd
    #  2.name judge Repeat
    #  3.max id 查询最大ID，select max(id) from table
# login
import DBControl
maxid =-1

if maxid==-1:
    
def register(name,passwd):
    if len(name)>20 or len(passwd)>20:
        raise("len of name or password too long ")
    
