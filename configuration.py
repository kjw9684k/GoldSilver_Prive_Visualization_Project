# 데이터베이스 접속 비밀번호
DB_PASSWORD = 'HTqxlT3g'
HOST = 'goldsilverprice-db.c4ca5hhwyuky.ap-northeast-2.rds.amazonaws.com'
USER = 'admin'

SECRET_KEY = 'django-insecure--@bw(8tp-_&waq2u(xk_=0g7zl_((e=r*_xb!^n&gpd^-yu!i0'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # engine: mysql
        'NAME' : 'sys', 
        'USER' : USER, # DB User
        'PASSWORD' : DB_PASSWORD, 
        'HOST': HOST,
        'PORT': '3306', # 데이터베이스 포트
        'OPTIONS':{
            'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}