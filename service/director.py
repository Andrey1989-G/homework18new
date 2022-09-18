from typing import List
from dao.director import DirectorDAO



class DirectorService:
    def __int__(self, director_dao):
        self.director_dao = director_dao

    def get_directors(self) -> List[DirectorDAO]:
        return self.director_dao.get_all_directors()

    def get_director_by_id(self, uid):
        return self.director_dao.get_director_by_id(uid)

