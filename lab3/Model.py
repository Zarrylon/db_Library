from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# author books subscription reader
# author 1:M reader
# books M:N sub
# reader M:N sub

engine = create_engine('postgresql+psycopg2://postgres:qwerty'
                       '@localhost:5434/Library', echo=True)
Session = sessionmaker(bind=engine)
s = Session()
Base = declarative_base()


def recreate_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


class author(Base):
    __tablename__ = 'author'
    author_id = Column(Integer, primary_key=True)
    name = Column(String)
    bk = relationship("books", order_by="books.books_id",
                      back_populates="aut")


class subscription(Base):
    __tablename__ = 'subscription'
    subscription_id = Column(Integer, primary_key=True)
    books_id = Column(Integer, ForeignKey('books.books_id'), primary_key=True)
    reader_id = Column(Integer, ForeignKey('reader.reader_id'), primary_key=True)
    startdate = Column(Date)
    duedate = Column(Date)


class books(Base):
    __tablename__ = 'books'
    books_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('author.author_id'))
    name = Column(String)
    size = Column(Integer)
    isavailable = Column(Boolean)
    aut = relationship("author", back_populates="bk")
    rd = relationship("reader", secondary='subscription', back_populates='bk')


class reader(Base):
    __tablename__ = 'reader'
    reader_id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    number = Column(String)
    bk = relationship("books", secondary='subscription', back_populates='rd')


class Model_db:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    @staticmethod
    def insert_data(table_name, values):
        if table_name == 'author':
            s.add(author(author_id=values[0], name=values[1]))
            s.commit()
        elif table_name == 'books':
            s.add(books(books_id=values[0], author_id=values[1], name=values[2],
                        size=values[3], isavailable=bool(values[4])))
            s.commit()
        elif table_name == 'reader':
            s.add(reader(reader_id=values[0], name=values[1], address=values[2],
                         number=values[3]))
            s.commit()
        elif table_name == 'subscription':
            s.add(subscription(subscription_id=values[0],
                               books_id=values[1], reader_id=values[2],
                               startdate=values[3], duedate=values[4]))
            s.commit()

    @staticmethod
    def delete_data(table_name, value_id):
        if table_name == 'author':
            s.query(author).filter_by(author_id=value_id).delete()
            s.commit()
        elif table_name == 'books':
            s.query(books).filter_by(books_id=value_id).delete()
            s.commit()
        elif table_name == 'reader':
            s.query(reader).filter_by(reader_id=value_id).delete()
            s.commit()
        elif table_name == 'subscription':
            s.query(subscription).filter_by(subscription_id=value_id).delete()
            s.commit()

    @staticmethod
    def update_data(table_name, values):
        if table_name == 'author':
            s.query(author).filter_by(author_id=values[0]).update({author.name: values[1]})
            s.commit()
        elif table_name == 'books':
            s.query(books).filter_by(books_id=values[0]).update(
                {books.name: values[1], books.size: values[2],
                 books.isavailable: values[3]})
            s.commit()
        elif table_name == 'reader':
            s.query(reader).filter_by(reader_id=values[0]).update({reader.name: values[1],
                                                                   reader.address: values[2],
                                                                   reader.number: values[3]})
            s.commit()
        elif table_name == 'subscription':
            s.query(subscription).filter_by(subscription_id=values[0]).update({subscription.startdate: values[1],
                                                                               subscription.duedate: values[2]})
            s.commit()
