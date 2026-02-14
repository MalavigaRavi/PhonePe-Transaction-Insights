----------TABLE1: aggregated_transacion--------------
CREATE TABLE aggregated_transacion (
    state TEXT,
    year INT,
    quarter INT,
    transaction_type TEXT,
    transaction_count BIGINT,
    transaction_amount DOUBLE PRECISION
);
------------TABLE2: aggregated_user-------------------
CREATE TABLE aggregated_user (
    state TEXT,
    year INT,
    quarter INT,
    brand TEXT,
    user_count BIGINT,
    percentage DOUBLE PRECISION,
    registered_users BIGINT,
    app_opens BIDINT
);
------------TABLE3: aggregated_insurance--------------------
CREATE TABLE aggregated_insurance (
    state TEXT,
    year INT,
    quarter INT,
    insurance_type,
    insurance_count BIGINT,
    insurance_amount DOUBLE PRECISION
);
-----------TABLE 4: map_transaction------------------------
CREATE TABLE map_transaction (
    state TEXT,
    year INT,
    quarter INT,
    hover_name TEXT,
    transaction_count BIGINT,
    transaction_amount DOUBLE PRECISION
);
-----------TABLE 5: map_user -------------
CREATE TABLE map_user (
    state TEXT,
    year INT,
    quarter INT,
    hover_name TEXT,
    registered_users BIGINT,
    app_opens BIGINT
);
----------TABLE 6: map_insurance------------
CREATE TABLE map_insurance (
    state TEXT,
    year INT,
    quarter INT,
    hover_name TEXT,
    insurance_count BIGINT,
    insurance_amount DOUBLE PRECISION
);
-----------TABLE 7: top_state_transaction-----------
CREATE TABLE top_state_transaction (
    state TEXT,
    year INT,
    quarter INT,
    level TEXT,
    entity_name TEXT,
    transaction_count BIGINT,
    transaction_amount DOUBLE PRECISION
);
--------------TABLE 8: top_user-------------------
CREATE TABLE top_user (
    state TEXT,
    year INT,
    quarter INT,
    level TEXT,
    entity_name TEXT,
    registered_users BIGINT
);
------------TABLE 9: top_insurance---------------
CREATE TABLE top_insurance (
    state TEXT,
    year INT,
    quarter INT,
    level TEXT,
    entity_name TEXT,
    insurance_count BIGINT,
    insurance_amount DOUBLE PRECISION
);















