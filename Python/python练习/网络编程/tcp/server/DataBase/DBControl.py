
from sqlalchemy import Column, String, create_engine,text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3
# 创建对象的基类:
Base = declarative_base()

class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    passwd =Column(String(20))

    def __str__(self):
        return (str(self.id)+" "+str(self.name)+" "+str(self.passwd))

def registerToDB(id_,name_,passwd_):
    new_user =User(id=id_,name=name_,passwd=passwd_)

def getMaxId():
    
    #id_ = session.query(User).all()
    #id_ = session.query(User).order_by(User.id).first() 
    id_ = session.query(User).from_statement(text("select * From user where id=(select max(id) from user)")).one()
    return id_.id

# 初始化数据库连接:
engine = create_engine('sqlite:///test.db',echo=False)

#创建
Base.metadata.create_all(engine)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
def insert():
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = User(id='4', name='Bob',passwd="123")
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()

#https://blog.csdn.net/Lotfee/article/details/57406450
def main():
    #insert()
    id_=getMaxId()
    print(id_)
   
if __name__ == '__main__':
    main()