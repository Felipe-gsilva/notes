- Server side programming lang
- Hypertext Preprocessor
- Prefer using Docker.
- PHP uses tags for starting a script `<?php [...] ?>`

  

## Basic functions

- `echo()` → return a specified value to the terminal.
- `var_dump()` → return the type and some specific info about a var send in its argument.
- `//` or `/** [..] */`→ comments

## Data types

- `bool` → boolean
- `int` → integer
- `$[var_name] = value` - floats
- `$[var_name] = ' '` or `" "` - strings
- `arrays` →

```PHP
$array1 = array(
    "key1" => "value1",
    "k2" => "v2"
);
//or
$array2 = [
	   "value1",
     "v2"
];
```

### Using var in echoes

```PHP
<?php
$idade = '18 Anos';
echo "Me chamo João e tenho " .$idade . "\n";
$idade = '19 Anos';
echo "Porém fiz aniversário e agora tenho " .$idade;
// Answer
// Me chamo João e tenho 18 Anos
// Porém fiz aniversário e agora tenho 19 Anos
?>
```

## Operators

- Addition `+`
- Subtraction
- Multiplication
- Division `/`
- Modulus (remainder of a division) `%`
- exponential `**`

## BIT WISE OPS

- AND `&`
- OR `|`
- Exclusive OR `^`
- NOT `~`
- Shift left `<<`
- Shift right `>>`

## COMPARISONS

- `==` `!=` convert the values, such as `'123'` == `123`
- `===` `!==` (verify types)
- `<` `>` `<=` `>=`