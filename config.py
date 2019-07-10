class ConfConst:
    @property
    def URL(self):
        return 'https://www.irctc.co.in/'
    @property
    def USER(self):
        return 'sivav8'
    @property
    def UNKEY(self):
        return b'yTOusj8kju9egEFprd3ojT0CDGdKFak38mRuerRmXjo='
    @property
    def PASSWORD(self):
        return b'gAAAAABdJZxAXHfoZpA-emNTn2fln5QtjCeKU7rcRkB8F3QGLiQnCGu4GbPWlBSjEFXMhxWdobDk_mlG1nPSXp3JPhbS8Iy5Ow=='
    def __getattr__(self,name):
        raise AttributeError("Undefined Constant")
