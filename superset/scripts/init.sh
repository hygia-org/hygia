#! /bin/bash


docker exec -it superset_app superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password admin

docker exec -it superset_app superset db upgrade

docker exec -it superset_app superset init


docker cp ./data/data.csv superset_db:/

docker exec  superset_db psql -U superset superset -c "CREATE TABLE  superset(CUSTOMER_NUM VARCHAR(300) DEFAULT NULL, COMPANY_NUM VARCHAR(300) DEFAULT NULL, ADDRESS_SEQ_NUM VARCHAR(300) DEFAULT NULL, ADDRESS_TYPE VARCHAR(300) DEFAULT NULL, STREET_ADDRESS_1 VARCHAR(300) DEFAULT NULL, STREET_ADDRESS_2 VARCHAR(300) DEFAULT NULL, CITY VARCHAR(300) DEFAULT NULL, CITY_2 VARCHAR(300) DEFAULT NULL, STATES VARCHAR(300) DEFAULT NULL, STATE_L VARCHAR(300) DEFAULT NULL, ZIP_CODE VARCHAR(300) DEFAULT NULL, COMPANY_NAME_CRYPT VARCHAR(300) DEFAULT NULL, COMPANY_NAME_2_CRYPT VARCHAR(300) DEFAULT NULL, FIRST_NAME_CRYPT VARCHAR(300) DEFAULT NULL, LAST_NAME_CRYPT VARCHAR(300) DEFAULT NULL, MIDDLE_INIT VARCHAR(300) DEFAULT NULL, NAME_PREFIX VARCHAR(300) DEFAULT NULL, AREA_CODE_1 VARCHAR(300), PHONE_NUM_1 VARCHAR(300) DEFAULT NULL, PHONE_EXT_1 VARCHAR(300) DEFAULT NULL, AREA_CODE_2 VARCHAR(300) DEFAULT NULL, PHONE_NUM_2 VARCHAR(300) DEFAULT NULL, PHONE_EXT_2 VARCHAR(300) DEFAULT NULL, SALESREP_NUM VARCHAR(300), ZIP_CODE_L VARCHAR(300) DEFAULT NULL, UPDATE_TIMESTAMP VARCHAR(300), COMPANY_NAME_EXT_CRYPT VARCHAR(300) DEFAULT NULL, STREET_ADDRESS_EXT VARCHAR(300) DEFAULT NULL, UPDATE_TIMESTAMP_EXT VARCHAR(300), adresses_count VARCHAR(300) DEFAULT NULL, update_year VARCHAR(300) DEFAULT NULL, update_ext_year VARCHAR(300) DEFAULT NULL, latitude VARCHAR(300) DEFAULT NULL, longitude VARCHAR(300) DEFAULT NULL, valid_zip_code VARCHAR(300) DEFAULT NULL, valid_area_code_1 VARCHAR(300) DEFAULT NULL, valid_area_code_2 VARCHAR(300) DEFAULT NULL, invalid_phone_number_2 VARCHAR(300) DEFAULT NULL, invalid_phone_number_1 VARCHAR(300) DEFAULT NULL, address_seq_num_missing_data VARCHAR(300) DEFAULT NULL, area_code_1_missing_data VARCHAR(300) DEFAULT NULL, phone_num_1_missing_data VARCHAR(300) DEFAULT NULL, area_code_2_missing_data VARCHAR(300) DEFAULT NULL, phone_num_2_missing_data VARCHAR(300) DEFAULT NULL, salesrep_num_missing_data VARCHAR(300) DEFAULT NULL, zip_code_l_missing_data VARCHAR(300) DEFAULT NULL, company_name_ext_crypt_missing_data VARCHAR(300) DEFAULT NULL, street_address_ext_missing_data VARCHAR(300), update_timestamp_ext_missing_data INTEGER DEFAULT NULL, random_forest_ksmash_result INTEGER DEFAULT 0, address_1_outlier INTEGER DEFAULT NULL);"

docker exec  superset_db psql -U superset superset  -c "\copy superset  FROM './data.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',')"





