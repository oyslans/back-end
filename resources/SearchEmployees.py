from datetime import datetime
from Model import Employee
from flask_restful import Resource
from flask import jsonify, request, Flask
import json
import config

cursor = config.conn.cursor()


class SearchEmployees(Resource):

    def get(self):
        # print("hi")
        query = request.args.get('query')
        sql_query = f"SELECT emp_id, emp_name FROM tblEmployees WHERE emp_id LIKE '%{query}' OR emp_name LIKE '%{query}'"
        cursor.execute(sql_query)
        results =[]
        for row in cursor.fetchall():
            results.append({'emp_id': row.emp_id, 'emp_name': row.emp_name})
        # results = [{'emp_id': row.emp_id, 'emp_name': row.emp_name} for row in cursor.fetchall()]

        return jsonify(results)
