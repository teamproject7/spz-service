import os
import psycopg2
import psycopg2.extras

from sshtunnel import SSHTunnelForwarder

db_server_ip = os.environ['EGV_DB_SERVER_IP']
ssh_username = os.environ['EGV_DB_SERVER_USERNAME']
ssh_password = os.environ['EGV_DB_SERVER_PASSWORD']

dbname = os.environ['EGV_DB_NAME']
dbuser = os.environ['EGV_DB_USER']
dbpassword = os.environ['EGV_DB_SERVER_PASSWORD']


def get_all_info(spz_string):
    try:
        with SSHTunnelForwarder(
                (db_server_ip, 22),
                ssh_username=ssh_username,
                ssh_password=ssh_password,
                remote_bind_address=('localhost', 5432)) as server:
            server.start()
            print("ssh connection created")

            conn = psycopg2.connect(
                dbname=dbname,
                user=dbuser,
                password=dbpassword,
                host='localhost',
                port=server.local_bind_port
            )
            print("database connected")

            cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cur.execute(
                """
            select
                "Owner"."owner_id",
                "Owner"."identityCardID" as "owner_pid",
                "Owner"."name" as "owner_name",
                "Owner"."surname" as "owner_surname",
                to_char("Owner"."dateOfBirth", 'DD.MM.YYYY') as "dateOfBirth",
                "Car"."car_id",
                "Car"."spz",
                "Car"."model" as "car_model",
                "Car"."company" as "car_company",
                "Car"."color" as "car_color",
                "ServiceCheck"."date" as "service_check_date",
                "ServiceCheck"."type" as "service_check_type",
                "ServiceCheck"."result" as "service_check_result",
                "Insurance"."year" as "insurance_year",
                "Insurance"."type" as "insurance_type",
                "Insurance"."company" as "insurance_company",
                "Insurance"."price" as "insurance_price",
                "HighwayTollDB"."year" as "toll_year",
                "HighwayTollDB"."dateOfPurchase" as "toll_date_purchase",
                "HighwayTollDB"."country" as "toll_country",
                "HighwayTollDB"."price" as "toll_date_purchase",
                "StolenCarsDB"."year" as "stolen_db_year",
                "StolenCarsDB"."place" as "stolen_db_place",
                "StolenCarsDB"."found" as "stolen_db_found"
            from
                "Car"
            left outer join "CarOwner" on
                "Car".car_id = "CarOwner".car_id
            left outer join "Owner" on
                "CarOwner".owner_id = "Owner".owner_id
            left outer join "ServiceCheck" on
                "Car".car_id = "ServiceCheck".card_id
            left outer join "Insurance" on
                "Car".car_id = "Insurance".car_id and "Insurance"."year" = ( select date_part('year', CURRENT_DATE)::integer )
            left outer join "HighwayTollDB" on
                "Car".car_id = "HighwayTollDB".car_id
            left outer join "StolenCarsDB" on
                "Car".car_id = "StolenCarsDB".car_id
                where spz = %(spz)s
                """
                , {
                    'spz': spz_string
                }
            )

            # :DDD
            if cur.rowcount < 1:
                cur.close()
                conn.close()
                return (), [], []

            car_info = cur.fetchone()

            # :DDD
            car_info['insurance_valid'] = False if car_info['insurance_year'] is None else True

            cur.execute(
                """
             select
                "Violations"."violations_id",
                "Violations"."owner_id",
                to_char("Violations"."date", 'DD.MM.YYYY') as "violation_date",
                "Violations"."issueOfficer",
                "Violations"."cost"
            from
                "Violations"
            left outer join "Owner" on
                "Owner".owner_id = "Violations".owner_id
            left outer join "CarOwner" on
                "Owner".owner_id = "CarOwner".owner_id
            where
                "CarOwner".car_id =(
                    select
                        car_id
                    from
                        "Car"
                    where
                        spz = %(spz)s)
                        """
                , {
                    'spz': spz_string
                }
            )

            violations = cur.fetchall()

            cur.execute(
                """
            select
                "Car"."car_id",
                 to_char("ServiceCheck"."date", 'DD.MM.YYYY') as "service_check_date",
                "ServiceCheck"."type" as "service_check_type",
                "ServiceCheck"."result" as "service_check_result"
            from
                "Car"
            left outer join "ServiceCheck" on
                "Car".car_id = "ServiceCheck".card_id
            where
                 spz = %(spz)s
                        """
                , {
                    'spz': spz_string
                }
            )

            checks = cur.fetchall()

            cur.close()
            conn.close()

        return car_info, violations, checks

    except:
        print("Connection Failed")
        return {}, [], []
