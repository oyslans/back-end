from datetime import datetime
from Model import Employee
from flask_restful import Resource
from flask import jsonify, request, Flask
import json
import config

cursor = config.conn.cursor()


# user_id = ""
# name = ""
# bg = ""
# dob = ""
# phone_number = ""
# address = ""
# userPrefix = "OYS00"
# userCount = 1
# response = ''


class AllEmployees(Resource):

    def get(self):
        id_query = f"select * from tblEmployees"
        cursor.execute(id_query)
        results = []
        # data_obj = cursor.fetchall()
        # date = data_obj[0][3]
        # newDate = date.strftime("%d-%m-%y")
        # print(newDate)
        for row in cursor.fetchall():
            date = row.last_attendance.strftime("%d-%m-%y")
            time = row.last_attendance.strftime("%H:%M:%S")
            results.append({
                'emp_id': row.emp_id,
                'emp_name': row.emp_name,
                'status': str(row.att_type),
                'date': date, 'time': time,
                'position': row.position,
                "blood-group": row.emp_bg,
                "address": row.emp_address,
                "phone-number": row.emp_phone_number,
                "dob": row.emp_dob})

        return jsonify(results)

        # emp = Employee.getEmployees(1)
        # # return emp
        # return jsonify({"ids": emp[0], "names": emp[1], "status": emp[2]})

        # query = f"select emp_id, emp_name from tblEmployees"
        # cursor.execute(query)
        # results = cursor.fetchall()
        # newResults = ()
        # for row in results:
        #     newResults = newResults + (tuple(row))
        # idList = []
        # nameList = []
        # for i in range(0, len(newResults)):
        #     if i % 2 == 0:
        #         idList.append(newResults[i])
        #     else:
        #         nameList.append(newResults[i])
        # return jsonify({"id": idList, "names": nameList, "count": len(nameList)})

        # def post(self):
        #     global user_id
        #     global name
        #     global bg
        #     global dob
        #     global phone_number
        #     global address
        #     global response
        #     global userCount
        #     global userPrefix
        #
        #     user_id = userPrefix + str(userCount)
        #     userCount += 1
        #     query2 = f"select emp_id from tblEmployees"
        #     cursor.execute(query2)
        #     request_data = request.data
        #     request_data = json.loads(request_data.decode('utf-8'))
        #     # user_id = request_data['id']
        #     name = request_data['name']
        #     bg = request_data['bg']
        #     address = request_data['address']
        #     phone_number = request_data['phone']
        #     dob = request_data['date']
        #     formattedDate = datetime.strptime(dob, "%d-%m-%Y")
        #     for row in list(cursor.fetchall()):
        #         print(row)
        #     # if user_id =
        #     print(request_data)
        #
        #     query = f"insert into tblEmployees(emp_id,emp_name,emp_bg,emp_dob,emp_phone_number,emp_address) values('{user_id}','{name}' , '{bg}','{formattedDate}','{phone_number}','{address}');"
        #     cursor.execute(query)
        #     cursor.commit()
        #     response = f"hi {name} this is from pythonn"
        #     print("Inserted successfully")
        #     return jsonify({"name": "Hi test"})
