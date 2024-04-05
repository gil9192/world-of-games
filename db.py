from sqlalchemy import create_engine, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Player(Base):
    """
    Player entity layput to store in the database.
    """
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, autoincrement=True)
    score = Column("score", Integer)
    username = Column("name", String, unique=True)

    def __init__(self, username, score=0):
        self.username = username
        self.score = score
    
    def __repr__(self):
        return f"{self.id} {self.username} {self.score}"


class PlayerDB():
    def __init__(self, path: str="wog.db" ) -> None:
        """
        Create sqlite database at the provided path.

        Args:
            path (str, optional): Path for the database. Defaults to "wog.db".
        """
        self.engine = create_engine(f"sqlite:///{path}", echo=False)
        Base.metadata.create_all(bind=self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        return

    def create_player(self, username: str):
        """
        Create new player in database if doesn't exist.

        Args:
            username (str): Player's username.

        Returns:
            bool: True if user created, False if already exists.
        """
        players = self.session.query(Player).filter(Player.username == username)
        if players.count() == 0:
            self.session.add(Player(username))
            self.session.commit()
            return True
        return False
    
    def read_player(self, username: str) -> tuple:
        """
        Get playr's data from database.

        Args:
            username (str): Player's username.

        Returns:
            tuple: id, username, score
        """
        players = self.session.query(Player).filter(Player.username == username)
        for player in players:
            return player.id, player.username, player.score

    def update_player(self, username: str, score: int) -> bool:
        """
        Update player's score data.

        Args:
            username (str): Player's username.
            score (int): Score to set.

        Returns:
            bool: True if updated successfuly, else False.
        """
        players = self.session.query(Player).filter(Player.username == username)
        if players.count() == 1:
            for player in players:
                player.score = score
            self.session.commit()
            return True
        else:
            return False

    def show_all(self):
        results = self.session.query(Player).all()
        for result in results:
            print(result)


if __name__ == "__main__":
    db = PlayerDB()
    db.create_player("test")
    id, username, score = db.read_player("test")
    assert id == 1
    assert username == "test"
    db.update_player("test", score + 1)
    _, __, new_score = db.read_player("test")
    assert new_score == score + 1
    db.show_all()
