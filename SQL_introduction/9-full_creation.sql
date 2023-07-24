-- script that creates a table 'second_table' and add multiples row
CREATE TABLE second_table (
    id INT,
    name VARCHAR(50),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);