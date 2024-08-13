[[SDL2]]

# Static

variavel de classe, n de objeto

# Lambda Expression

```C++
auto soma = [](int n1, int n2) {
	return n1 + n2;
};
```

# Smart Pointers

std::unique_ptr

std::shared_ptr

std::weak_ptr

  

# Template

permite generalizar o tipo de entrada e/ou saida de tipos de dados.

```C++
template <typename T>
T multiplicacao(T a, T b)
{
    return (a * b);
}
```