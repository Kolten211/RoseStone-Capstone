from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import event
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    native_language = db.Column(db.String(25))
    learning_language = db.Column(db.String(25))
    level = db.Column(db.String(25))
    score = db.Column(db.Integer)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    # def __init__(self,*args, **kwargs):
    #     super(User, self).__init__(*args, **kwargs)
    #     self._score = kwargs.get('score', 0)
    #     print(f"Initializing user with score: {self.score}")
    #     self._level = None
    #     self._update_level()
    #     print(f"User initialized with level: {self._level}")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    

    # _ used before the variable in a property is just a flag to let the dev know this is for backend use only

    # @property
    # def user_id(self):
    #     return self.id
    
    # @property
    # def score(self):
    #     return self._score
    
    # @score.setter
    # def score(self, new_score):
    #     self._score = new_score
    #     self._update_level()
    
    # @property
    # def level(self):
    #     return self._level
    
    # @level.setter
    # def level(self, new_level):
    #     self._level = new_level

    # def _update_level(self):
    #     new_level = self._calculate_level(self._score)
    #     if new_level != self._level:
    #         self._level = new_level
    #         print(f"User {self.id} leveled up to {self._level}")

    # def _calculate_level(self, score):

    #     LEVEL_RANGES = [
    #         (0, "Beginner"),
    #         (300, "Intermediate"),
    #         (750, "Advanced"),
    #         (1001, "Expert")
    #     ]
    #     for min_score, level_name in LEVEL_RANGES:
    #         if score < min_score:
    #             return LEVEL_RANGES[LEVEL_RANGES.index((min_score, level_name))-1][1] if LEVEL_RANGES.index((min_score, level_name)) > 0 else LEVEL_RANGES[0][1]
    #         return LEVEL_RANGES[-1][1]

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'natative_language': self.native_language,
            'learning_language': self.learning_language,
            "level": self.level,
            "score": self.score,
            'email': self.email,
            'hashed_password': self.hashed_password
        }
    
    # @event.listens_for(db.session, 'after_begin')
    # def do_the_stuff(session, transaction, context):
    #     print("Event listener triggered!")
    #     for obj in session.identity_map.values():
    #         print(f"User object found: {obj.id}") 
    #         if isinstance(obj, User):
    #             if not hasattr(obj, "_score"):
    #                 obj._score = obj.score if obj.score is not None else 0
    #                 obj._level = None
    #                 obj._update_level()