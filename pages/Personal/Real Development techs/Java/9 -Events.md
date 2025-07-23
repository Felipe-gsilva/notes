๏ Eventos

๏ Manipulação de Eventos

- Objeto onde eventos são gerados
- Objeto ouvinte de eventos (listeners)

๏ Tipos de Eventos

๏ Multicast

# Definição

Em Java, um evento é um objeto do tipo java.util.EventObject, ou um subtipo como ActionEventou WindowEvent

- Um `listener` é um objeto o qual recebe as interações da interface através de um objeto origem e envia ao graphical server
- Objetos que são capazes de gerar eventos são chamados de `objeto origem`

  

```Java
public class MyPanel implements ActionListener {
	public void actionPerformed(ActionEvent evt) {
		// event reaction
	}
}
```

  

```Java
MyPanel myPanel = new MyPanel();
JButton jbutton = new JButton("Clean");
button.addActionListener(panel);
```

- O código anterior exige que a classe MyPanel implemente a interface ouvinte apropriada (ActionListener)
- Ao implementar a interface ActionListener, a classe ouvinte precisa definir um método (actionPerformed) que recebe como parâmetro um evento (ActionEvent)

  

## Registrando o evento

podemos registrar o mesmo objeto listener para todos os botões, neste caso, para identificar a fonte do evento usaremos o método `getSource()` do objeto evento

  

```Java
if(evt.getSource == yellowButton) // por exemplo
	// treat it
```

You can add the same listener for all the obj in the panel

![[/Untitled 5.png|Untitled 5.png]]

# Lambda Expression

allows a parameter as a function to be passed into the arguments

# Multicast

adicionar objetos ao mesmo listener, permitindo assim que apenas um evento dispare da origin e acesse todos os listeners