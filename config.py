import pyodbc as odbc_con

conn = odbc_con.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=lavan;"
                        "Database=FAS_DB;"
                        "Trusted_Connection=yes;"
                        )
