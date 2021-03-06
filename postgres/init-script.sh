#!/bin/bash
#
# This script will run before Postgres initdb initlization.
# Will run with postgres user connecting to localhost, so no Auth will be required
#
set -e

# Create specific user and database
psql -v ON_ERROR_STOP=1 <<-EOSQL
    CREATE USER ${POSTGRES_API_USER} PASSWORD '${POSTGRES_API_PASSWORD}';
    CREATE DATABASE ${POSTGRES_API_SCHEMA};
EOSQL

# Create table, load data from CSV and grant permission
psql -v ON_ERROR_STOP=1 --dbname ${POSTGRES_API_SCHEMA} <<-EOSQL
    CREATE TABLE air_quality_measurements (
        time_instant timestamp without time zone,
        id_entity character varying(50),
        so2 double precision,
        no2 double precision,
        co double precision,
        o3 double precision,
        pm10 double precision,
        pm2_5 double precision
    );

    COPY air_quality_measurements
    FROM '/tmp/environment_airq_measurand.csv'
    DELIMITER ','
    CSV HEADER;

    GRANT SELECT ON air_quality_measurements TO ${POSTGRES_API_USER};
EOSQL
