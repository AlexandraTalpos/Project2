CREATE TABLE filme (
    id INTEGER PRIMARY KEY,
    titlu TEXT,
    an INTEGER,
    regizor TEXT
);


INSERT INTO filme (titlu, an, regizor) VALUES
('Red Notice', 2021, 'Rawson Marshall Thurber'),
('The Meg', 2018, 'Ben Wheatley');



SELECT * FROM filme
