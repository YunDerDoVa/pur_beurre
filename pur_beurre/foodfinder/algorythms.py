class Algorythm:

    def search_substitutes(self):
        pass

    @staticmethod
    def get_algorythm_by_classname(classname):
        algorythm = eval(classname)
        return algorythm


class ByFat(Algorythm):

    pass
