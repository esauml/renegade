
from flask import Blueprint
Productos=Blueprint('productos',__name__,url_prefix='/productos')

from . import views