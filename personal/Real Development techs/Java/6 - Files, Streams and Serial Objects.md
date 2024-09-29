# Topics on this chapter:

- File Stream (Byte and Chars)
- Buffered Stream
- Stream filters
- Scanner
    - Console
- Object Streams
- Serialized Objects
- File Random Access

# Concepts

# Stream

A stream is a type of data which represent a continuous flow of bytes, and is capable of reading and writing files, objects and even normal types. This data type is mostly used to optimize file access, because it can on runtime enter each byte/char from a file and store it on an local allocated memory

## Byte Stream (FileInputStream and FileOutputStream)

A byte stream reads and return an integer value which has the last 8 bits used to store the data. You can, later, input the integer on another data type by using a output byte stream.

- in.read()
- out.write(c)

```Java
public class main {
	// byte stream
	FileInputStream in;
	FileOutputStream out;
	
	public void teste() {
		in = new FileInputStream("FileName.type");
		out = new FileInputStream("FileName.type");	
		int c;
		while ((c = in.read()) != -1{
			out.write(c);
		}
	}
}
```

## Char Stream (FileReader and File Writer)

It works almost identically as the last stream, but, instead, it uses 16 bits from the int.

```Java
public class main {
	// char stream
	FileReader in = new FileReader(fileIn);
	FileWriter out = new FileReader(fileOut);
	
	public void teste() {
		int c;
		while ((c = in.read()) != -1{
			out.write(c);
	}
}
```

# Filters

Method that are capable of converting Stream return type from char to string or vice-versa

- wrappers
- bridges

# Buffered Stream

Existem quatro tipos de buffered streams no Java

- BufferedInputStream (byte)
- BufferedOutputStream (byte)
- BufferedReader (caracteres)
- BufferedWriter (caracteres)

Outra vantagem da classe BufferedReader é a possibilidade de leitura do arquivo linha por linha com `readLine()`

- esse método pode verificar linhas completas sem a necessidade de se olhar char por char

`buffer.flush()` descarrega o buffer
# Scanner

A scanner can read an entry using tokens, which assumes an “ “ as separator for each token. Each returned token can be read as an specific primite type.

`Scanner sc = new Scanner(stream here)`

which leads to the functions → .nextLine(); .nextDouble;

## I/O in CLI

You can use as default the Scanner reading the [System.in](http://System.in) stream or a Console object directly

`Console cli = System.console();`

- cli.read()
- cli.write()
- cli.readPassword()

# Object Streams

Can access and store objects instead of files. Then, you can output it wherever you want.

- ObjectInputStream
    - .readObject()
- ObjectOutputStream
    - writeObject(a)u
## Serialization

An serialized object is represented as an byte sequence and can be store in an other stream

- for an object to be serialized, it must, first, implements the Serializabe class, which has no method an only works as an flag

# FILES

- RandomAccessFile raf = new RandomAccessFile(”File”);
    - raf.seek(position / raf.length())