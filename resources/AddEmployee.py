from datetime import datetime
from flask_restful import Resource
from flask import jsonify, request
import json
import config

cursor = config.conn.cursor()

user_id = ""
name = ""
bg = ""
dob = ""
phone_number = ""
address = ""

userPrefix = "OYS"
userCount = 1
response = ''


class AddEmployee(Resource):

    def post(self):
        global user_id
        global name
        global bg
        global dob
        global phone_number
        global address
        global response
        global userCount
        global userPrefix

        # ===========================
        #   AUTO INCREMENTING ID
        # ===========================
        query2 = f"select count(emp_id) from tblEmployees where emp_id like 'OYS%'"
        cursor.execute(query2)
        userCount = cursor.fetchone()[0]
        userCount += 1
        user_id = userPrefix + str(userCount)

        # ===========================
        #   FETCHING REQUEST
        # ===========================

        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        # user_id = request_data['id']

        name = request_data['name']
        bg = request_data['bg']
        address = request_data['address']
        phone_number = request_data['phone']
        # dob = request_data['date']
        # formattedDate = datetime.strptime(dob, "%d-%m-%Y")
        dateNow = datetime.now()
        for row in list(cursor.fetchall()):
            print(row)
        # if user_id =
        print(request_data)

        # ===========================
        #   ADDING TO DATABASE
        # ===========================

        query = f"insert into tblEmployees(emp_id,emp_name,emp_bg,emp_dob,emp_phone_number,emp_address) values('{user_id}','{name}' , '{bg}','{dateNow}','{phone_number}','{address}');"
        cursor.execute(query)
        cursor.commit()
        print("Inserted successfully")
        return jsonify({"status": "success"})
