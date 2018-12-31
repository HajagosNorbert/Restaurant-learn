import os

project_dir = os.path.dirname(os.path.abspath(__file__+'/..'))
database_file = f'sqlite:///{os.path.join(project_dir, "restaurantmenu.db")}'


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY').encode()
    SQLALCHEMY_DATABASE_URI = database_file

    SEND_FILE_MAX_AGE_DEFAULT = 0
