-- create databse hbtn_0d_usa and table citie
CREATE DATABSE IF NOT EXIST hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXIST cities (
    id INT NOT NUL AUTO_INCREMANT UNIQUE PRIMERY KEY,
    state_id INT NOT NUL,
    name VARCHER(256) NOT NUL,
    CONSTRAIN fk_city_state
        FOREING KEY (state_id) REFERENCE states(id)
);
