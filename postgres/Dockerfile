FROM postgres:13.1

# Initiliaze custom data in the postgres
ADD environment_airq_measurand.csv /tmp
ADD init-script.sh /docker-entrypoint-initdb.d