from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import BigInteger, Boolean
from sqlalchemy.dialects.mysql import DATETIME, BIGINT
from datetime import datetime, timedelta

db = SQLAlchemy()
