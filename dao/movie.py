from dao.model.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def get_movies_by_id(self, yid):
        return self.session.query(Movie).filter(Movie.id == yid).one()

    def get_by_kwargs(self, **kwargs):
        return self.session.query(Movie).filter_by(**kwargs).all()

    def update_movie(self, uid, **kwargs):
        try:
            if uid == Movie.id:
                self.session.query(Movie).filter(Movie.id == kwargs.get('id')).update(kwargs)
                self.session.commit()
                return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False

    def create_movie(self, **kwargs):
        try:
            self.session.add(Movie(**kwargs))
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False

    def delete_movies(self, vid):
        try:
            self.session.query(Movie).filter(Movie.id == vid).delete()
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False
