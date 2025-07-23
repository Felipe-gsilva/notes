# Data Types

==It is what you would expect it to be, types of data, which you write to create data fields==

INT - Name for integer

DECIMAL - Floats

CHAR(size) - Char.

VARCHAR(size) - literally variable chars

STRING - bunch of char inside a memory pointed by a pointer

BOOLEAN - Abstraction for 0s and 1s

DATE - date, but useless

# CONSTRAINTS

==Restrictions inside a table’s data, making some inputs unacceptable==

UNIQUE - Only one value can be inserted on a field with this type

NOT NULL - exactly what it suggests

PRIMARY KEY - The ID of a table insert, mixing UNIQUE and NOT NULL

CHECK - Verifies if the values of some line in the table match some value you specify.

```SQL
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (Age>=18)
);
```

# CREATING A DATABASE

```SQL
CREATE DATABASE DATABASE1;
```

## CREATING A TABLE

```SQL
CREATE TABLE TABE (
	ID int NOT NULL,
	LILCHAR varchar(255),
	MYGOD int
);
```

## INSERTING DATA

```SQL
INSERT INTO TABLE (LILCHAR, MYGOD) VALUES ('AAAAAAAA', 1)
```

## SEARCHING DATA

```SQL
SELECT * FROM TABE
SELECT LILCHAR, MYGOD FROM TABEL
```

## UPDATING DATA

```SQL
UPDATE TABE SET CAMPO1 = 'VALOR ALTERADO';
```

## DELETING DATA

```SQL
DELETE * FROM TABELA;
DELETE FROM TABELA WHERE ID = 1;

// You can also select data using command where

SELECT * FROM TABELA WHERE ID = 1;
```

## AND/OR

```SQL
SELECT * FROM TABELA WHERE ID = 1 OR ID = 2;
SELECT * FROM TABELA WHERE CAMPO1 = 'MYSQL' AND CAMPO2 = '4NOOBS';
```

## LIKE

You can select an similar value on tables, using LIKE.

```SQL
SELECT * FROM TABELA WHERE CAMPO1 LIKE '%MYSQL%'; // ANYTHING WRITTEN AFTER AND BEFORE WILL BE IGNORED, ONLY FOCUSING ON MYSQL APPEARENCES ON EACH FIELDS
```

## JOINS