DROP TABLE gyms;
DROP TABLE members;
DROP TABLE lessons;



CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE lessons(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE gyms (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE
);
