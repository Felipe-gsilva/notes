[[Raylib]]
# Cargo

Cargo is the package manager and also a build system for rust, it works as cmake does, but in a truly fashionable way.

list cargo commands:

- ==cargo build== → ./target/debug/_$_binary_$_
- ==cargo run== → build and runs automatically
- ==cargo new== _project_name_ → use `--help` to see details
- ==cargo check== → does not create an binary file, just check its possible failures.
- ==cargo build== `==--release==` → create a /target/realese/binary with some optimizations.

## Imports

use std::io is the standard lib, just as C.

but you can use different ones by adding those to `cargo.toml` and importing it following this structure :

```Rust
use std::io;
use rand::Rng;
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;
```

## User input example

```Rust
io::stdin().read_line(&mut guess).expect("Failed to read line");
```

This code uses `input/output` standard method `stdin` to get user input. The `read_line` function reads the line 👍 and insert it by a referenced version of the guess variable, defined before. If an error occurs, it is handled by `expect` function, which returns the String you inserted there.

This is divided in the `Ok` and `Err` variants from Result type, handled separately.

# Crates

A crate is a collection of Rust source code files. The `rand`  
crate is a  
_library crate_, which contains code that is intended to be used in other programs and can’t be executed on its own.

## add deps to `cargo.toml`

```Rust
// [...]
[dependencies]
rand = "0.8.5"
```

[Crates.io](https://crates.io/) is where people in the Rust ecosystem post their open source Rust projects for others to use.

## Declarations

- fn - function creation word
- fn main () - main

# Variables

- let - defined word for creating a variable.
- let &mut - the only one which is actually mutable
- const - constant

## Numbers

// unsigned integer: u8, u16, i32, i64, u128, usize  
// signed int: i8, i16, i32, i64, i128, isize  

// float: f8, f16, f32, f64, f128, fsize

# Enumaration

==**// TODO**==

# Operators

same as in C, +, -, /, *, %, ‘op’= …

## random numbers

```Rust
let something: i32= rand::thread_rng().gen_range(1..=100);
```

This code generates a random number from 1 to 99 using `thread_rng` method. In this case, we are using `gen_range` set as `1..=100` .

# Conditional

- if, else if and else like normal
- ternary:

```Rust
let my_age: i32 = 47;
    let can_vote: bool = if my_age >= 18{
        true
    } else {
        false
    };
    
    println!("Can Vote: {}", can_vote);
```

- match

```Rust
let age2: i32 = 8;
    match age2 {
        1..=18 => println!("Important"),
        21 | 50 => println!("Important"),
        65..=i32::MAX => println!("Not Important"),
        _ => println!("Not Important"),
    };
```

- match with .cmp

```Rust
use std::cmp::Ordering;
match guess.cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
```

  

  

# lifecycle