# Agenda

---

๏ Introdução

๏ Componentes Swing

๏ Gerenciadores de Layout

๏ Look and Feel

๏ GUI e NetBeans

---

# Introdução

- JFrame
- JDialog
- JApplet
- - Método `.add()` adiciona um child ao parent

  

EDT = é responsável por lidar com os eventos de interface do usuário, garantindo a pipeline de eventos.

---

Todos os components Swing são objetos da classe JComponent

- JLabel
- JTextField
- JButton
- JRadioButton
- JCheckBox
- JCheckBox
- JComboBox
- JList
- JTable
- JPanel
- JFileChooser
- JOptionPane
- JTextArea
- JPasswordField/JFormattedTextField
- JCheckBox
- JComboBox
- JList
    - JScrollPane
    - Lista mutável -> ListModel ( inserção das String estão no ListModel que é inserido no JList());
    - .getSelectedIndex();
- JTable
    - into JScrollPane
    - TableModel
- JPanel -> serve para armazenar outros componentes, podendo alterar seu plano de fundo e borda, p.e;
    - JLayeredPane
    - JScrollPane
    - JTabbedPane
- JMenu -> podem receber outros componentes
    - JMenuBar
    - JMenuItem
- JFileChooser -> serve para abrir uma janela com o file manager padrão
    - save and open
- JOptionPane (E/S)
    - showMessageDialog

---

# **Gerenciadores de layout**

---

Organizam a posição e o tamanho dos componentes dentro de um container. Todo container tem um método `setLayout`. Exemplos:

- FlowLayout
    - Padrão de um JPanel -> insere o componentes em ordem de inserção da esquerda para a direita;
    - pode-se trocar o alinhamento ao centro, esquerda e direita
- BorderLayout
    
    - Organiza os componentes em cinco regiões:
        - NORTH, SOUTH, EAST, WEST, CENTER
    - cada componente (máx 5) pode ser um container com mais componentes dentro
    
    ```Java
    Borderlayout borderLayout = new BorderLayout(5,5); // spacing 5px
    f.setLayout(borderLayout);
    ```
    
- CardLayout
- BoxLayout
- GroupLayout
- GridLayout
    
    - Divide o container em uma grade (x, y)
    - Cada elemento é adicionado em uma posição, todos com tamanhos iguais
    - cima para baixo, esquerda para direita
    
    ```Java
    GridLayout gridLayout = new GridLayout(2,3,5,5); // spacing 5
    || 
    GridLayout gridLayout = new GridLayout(3,2); // no spacing
    f.setLayout(GridLayout);
    ```
    
    ![[/Untitled 4.png|Untitled 4.png]]
    
- GridBagLayout
    
    - Igual ao outro, mas diferente
    - Cada linha ou coluna pode ter tamanhos diferentes
    - É possível especificar quais células (e em qual proporção) deverão ser  
        redimensionadas junto com o redimensionamento do container  
        
    
      
    

---

# Look and Feel

---

  

Permite alterar a aparencia dos componentes de acordo com o SO ou outros critérios

tipos →

- CrossPlatformLookAndFell (Metal),
- SystemLookAndFeel → baseado no sistema atual
- Nimbum → uitliza o java 2D graphics para criar os componentes gráficos
- Motif L&F