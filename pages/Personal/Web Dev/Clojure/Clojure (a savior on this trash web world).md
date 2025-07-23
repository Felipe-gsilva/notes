Created by Rich Hickey, who used to work in projects with Lisp.

Clojure uses functions as main data structures, data immutability and runs on JVM. It is a pure functional program language focused on concurrency computing.

Almost all Java functions works on .clj files, since we are running it on JVM.

## Installing clojure

```Shell
curl -L -O https://github.com/clojure/brew-install/releases/latest/download/linux-install.sh
chmod +x linux-install.sh
sudo ./linux-install.sh
```

# Evaluation → types

number, string, java types, objects (also)

# ==Data Seqables==

1. Arrays
2. Lists
3. Sets
4. Maps

### arrays

Some static array functions

- First (get first element of the array)
- Rest (get all except the first)
- Nth (get an element with and index you set)

```Clojure
(nth defined_vector 3)
```

- (defined_vector 3) // prints out all elements
- Count - it counts elements
- Conj - add one more element to the end
- Cons - add one more element to the start

### list

same as above, except you can’t use (defined_list 3)

### Set

- Contains? Returns true or false

```Clojure
 (contanis? set-var “what_you_wanna_seek”)
```

- Disj - remove from set
- Conj - adds an value (in order)

### Maps

Created with keys and values

```Clojure
(def musicas {"a" "b", "c" "d"}
```

- get (get with key)
- assoc - add an association
- dissoc - you know
- contains?
- find - returns key and value
- keys - validate all keys in the hash map
- vals - validate all values in the hash map
- zipmap - generate another map from the original one
- remove (remove an entry with a key)

```Clojure
(zipmap #{"a" "b" "c"} (repeat 1))
```

## doc/dir/source

you can see the documentation, a list of functions in the same dir and the source code of EVERY function existing wherever namespace it is

## **Multi-arity functions**

you can add multiple data inputs as different types

```Clojure
(defn carlos 
	([] (carlos "carlos")
	([msg] (println msg)))
```

## **Variadic functions**

when adding an & for an input, it will be seen as a “array” on different inputs and everything added after it will be added to the arr

```Clojure
(defn carlos [primeiro & resto]
	(println primeiro resto))
```

## Anonymous fn

does not need a name, use only fn, the param and the body or maybe #( %1 and %2)

# Comparison

|   |
|---|
|=|
|>=, >, <=, <|
|and, or, not|

# Conditionals

## If

(if (condition)

(case true)

(case false))

## let

let is used in a specific scope ever.

```Clojure
(let [a 5]
  (if (< a 0)
     (println "Menor que 0")
  (if (= a 0)
     (println "Igual a 0")
     (println "Maior que 0"))))

;;  Retorno:
;;  Maior que 0
;;  nil
```

## when

there is no else, only is activated when something happens

  

## cond

stablish a condition as a conditional function like (cond (= a b) “print auto” :else “saida” )

  

## do

Used for returning more than one function on each flow control point

```Clojure
(if (> 1 2)
    (do
      (println "Epa, recebi seus valores!")
      (println "Pelo que parece 1 é maior que 2!"))
    (do
      (println "Epa, recebi seus valores aqui hein!")
      (println "Pelo que parece 1 não é maior que 2!")))
```

## atom

stores a seqable for the whole running time.

## let

stores on a local scope a seqable var, anything you wish.

# Conversion

Interger/parseInt for example

# deps.edn

**extensible data notation (edn)**

:deps :paths

---

# -> e ->>

- -> Threads the expr through the forms. Inserts x as the
    second item in the first form, making a list of it if it is not a
    list already. If there are more forms, inserts the first form as the
    second item in second form, etc.

- ->> Threads the expr through the forms. Inserts x as the
    last item in the first form, making a list of it if it is not a
    list already. If there are more forms, inserts the first form as the
    last item in second form, etc.

(-> func-1 (func-2 func-3) (func-4 func-5 func-6)) = (func-4 (func2 func-1 func-3) func-5 func-6)

(->> func-1 (func-2 func-3) (func-4 func-5 func-6)) = (func-4 func-y func-6 (func-2 func-3 func-1))

---

# ^ - Metadata

stands for metadata, like

```Clojure
(def ^Integer foo 5) ;; this is a hint which tells foo has Integer set to true
(def ^:num foo 5)    ;; set num to true as meta data 

(meta form) ;; returns the metadata of a form
```

---

# ‘ - quote

tells the compiler not to evaluate what appears, just `quote` it

```Clojure
user=> (1 2 3)
Execution error [...]
user=> '(1 2 3)
(1 2 3)
```

# Defmacro
