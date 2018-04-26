# ./. coding=utf-8 ./.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager(app)
bf = Bootstrap(app)
lm.login_view = "auth.login"
nav = Nav()
nav.register_element('top',Navbar(u'simpleWeb站点',
                                  View(u'首页','main.index'),
                                  View(u'登入','auth.login'),
                                  View(u'登出','auth.logout'),
                                  Subgroup(u'功能',
                                           View(u'客户端信息','api.user_agent'),
                                           View(u'获取公网IP','api.remote_ip'),
                                           ),
                                  )
                     )
nav.init_app(app)



from app import models