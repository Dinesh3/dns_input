import sqlite3

connection  = sqlite3.connect('dns.db')


def create_dns_request_table(connection_string:sqlite3.Connection):
    cursor = connection_string.cursor()
    sql  = '''CREATE TABLE IF NOT EXISTS dns_request(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                dns_type CHAR(50), 
                action CHAR(50),
                dns_record_type CHAR(50),
                date CHAR(50),
                dns_name CHAR(50),
                ip_address CHAR(50),
                fqdn_name CHAR(150),
                service CHAR(50),
                protocol CHAR(50),
                domain CHAR(50),
                weight CHAR(50),
                port_no CHAR(50),
                priority CHAR(50),
                domain_name CHAR(50),
                c_name CHAR(150),
                service_tier CHAR(50),
                testing_mode CHAR(50),
                description TEXT
                )'''
    result = cursor.execute(sql)
    if (result):
        print('Table dns_request created successfully')
    connection.commit()
    # connection.close()


def create_dns_request(connection_string:sqlite3.Connection, dns_request_data):
    """
    Create a new dns_request into the dns_requests table
    :param connection_string:
    :param dns_request:
    :return: dns_request id
    """
    sql = ''' INSERT INTO dns_request(
                    dns_type,
                    action,
                    dns_record_type,
                    date,
                    dns_name,
                    ip_address,
                    fqdn_name,
                    service,
                    protocol,
                    domain,
                    weight,
                    port_no,
                    priority,
                    domain_name,
                    c_name,
                    service_tier,
                    testing_mode,
                    description)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cursor = connection_string.cursor()
    cursor.execute(sql, dns_request_data)
    connection_string.commit()
    return cursor.lastrowid



create_dns_request_table(connection)

# dns_request_data = ('internal_dns','create','a record','dinesh.com.in','10.10.1.1','system.dinesh.com','production','yes','can you create a A record',None,None,None,None,None,None,None,None)
# print(type(dns_request_data))
# result=create_dns_request(connection, dns_request_data )
# print(result)
