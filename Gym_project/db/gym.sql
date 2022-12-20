DROP TABLE bookings;
DROP TABLE members;
DROP TABLE lessons;



CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    dob VARCHAR(255)
);

CREATE TABLE lessons(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    time VARCHAR(255),
    date VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE
);
