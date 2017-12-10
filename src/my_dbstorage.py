from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(firstname='%s', lastname='%s'" % (
            self.firstname, self.lastname)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user = User(firstname="Peter", lastname="Petrovic", password="heslo")
session.add(user)

our_user = session.query(User).filter_by(firstname='Peter').first()
print(user is our_user)
