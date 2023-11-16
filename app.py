from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Admin import Admin
from resources.All_Employees import AllEmployees
from resources.SearchEmployees import SearchEmployees
from resources.AddEmployee import AddEmployee
from resources.Login import Login
from resources.EmployeeAttendance import EmployeeAttendance

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(Admin, '/admin')
api.add_resource(AllEmployees, '/getall')
api.add_resource(SearchEmployees, '/search')
api.add_resource(AddEmployee, '/add')
api.add_resource(Login, '/login')
api.add_resource(EmployeeAttendance, '/emp')
