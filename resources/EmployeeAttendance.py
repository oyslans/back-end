from flask_restful import Resource
from flask import jsonify, request
from datetime import datetime


import config

cursor = config.conn.cursor()


class EmployeeAttendance(Resource):

    def get(self):
        startDate = request.args.get('start')
        endDate = request.args.get('end')
        id = request.args.get('id')

        sql_query = f"SELECT * FROM tblAttendance WHERE time_stamp between '{startDate}' AND '{endDate}' AND FK_emp_id='{id}'"
        cursor.execute(sql_query)

        results = []

        for row in cursor.fetchall():
            results.append(
                {
                    'emp_id': row.FK_emp_id,
                    'date': row.time_stamp.strftime("%m-%d-%y"),
                    'time': row.time_stamp.strftime("%H:%M:%S"),
                    'type': row.att_type
                })
        return jsonify(results)
