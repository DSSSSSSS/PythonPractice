'''http://jzqt.github.io/2015/12/29/SQLAlchemy%E7%AC%94%E8%AE%B0/'''

from sqlalchemy import Column, String, create_engine, text, Enum, INT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3

# 创建对象的基类:
Base = declarative_base()

maxid = -1


class DBError(ValueError):
    pass


class UserTpye(Enum):
    ordinary = 1
    Super = 2


class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    passwd = Column(String(20))
    userTpye = Column(INT)

    def __str__(self):
        return (str(self.id)+" "+str(self.name)+" "+str(self.passwd))+" "+str(self.userTpye)


class DBQuery():
    def __init__(self):
        # 创建Session:
        self.session = DBSession()

    def __del__(self):
        # 关闭session:
        self.session.close()

    def getMaxId(self):
        #id_ = session.query(User).all()
        #id_ = session.query(User).order_by(User.id).first()
        
        try:
            id_ = self.session.query(User).from_statement(
                text("select * From user where id=(select max(id) from user)")).one()
        except:
            return 0
        return id_.id

    def query(self):
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        user = self.session.query(User).filter(User.id == '5').one()
        # 打印类型和对象的name属性:
        print('type:', type(user))
        print('name:', user.name)
        # 关闭Session:
        self.session.close()

    # 把给定user date 插入数据库
    def __register1(self, name_, passwd_):
        #global maxid
        # if maxid == -1:
        maxid = self.getMaxId()
        if (self.session.query(User).filter(User.name == name_).count()) != 0:
            raise DBError("name is invalid")  # 重名异常
        new_user = User(maxid, name=name_, passwd=passwd_)

        self.insert(new_user)
        maxid += 1

    def register(self, user: User):
        user.id = self.getMaxId()+1
        if (self.session.query(User).filter(User.name == user.name).count()) != 0:
            raise DBError("name is invalid")  # 重名异常
        self.insert(user)

    def login(self, user: User):
        #re =self.session.query(User).filter(User.name==name).filter(User.passwd==passwd).all()
        # for i in re:
            # print(i)
        if self.session.query(User).filter(User.name == user.name).filter(User.passwd == user.passwd).count() != 0:
            return True
        else:
            return False

    def insert(self, new_user):
        # 创建session对象:
        #session = DBSession()
        # 创建新User对象:
        #new_user = User(id='4', name='Bob',passwd="123")
        # 添加到session:
        self.session.add(new_user)
        # 提交即保存到数据库:
        self.session.commit()



# 初始化数据库连接:
engine = create_engine('sqlite:///test.db', echo=False)

# 创建
Base.metadata.create_all(engine)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# https://blog.csdn.net/Lotfee/article/details/57406450
def main():
    new_user = User(id='1', name='Bob', passwd="123",
                    userTpye=UserTpye.ordinary)
    q = DBQuery()
    #q.register(name_="Bob", passwd_="123")
    q.register(new_user)
    id_ = q.getMaxId()
    re = q.login(new_user)
    print(re)
    # print(id_)


if __name__ == '__main__':
    main()
