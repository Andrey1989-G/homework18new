from dao.model.models import Director


class DirectorDAO:
    def __int__(self, session):
        self.session = session

    def get_all_directors(self):
        return self.session.query(Director).all

    def get_director_by_id(self, yid):
        return self.session.query(Director).filter(Director.id == yid).one()
