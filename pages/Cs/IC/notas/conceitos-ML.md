# gradiente desaparcendo  (vanishing gradient)

Os gradientes de uma rede neural com backpropagation passam a ter magnitudes (muito) divergentes entre camadas. Os pesos neste tipo de rede neural são calculados através da derivada parcial da função de perda e entregues para os nós anteriores pelo backpropagation. Quanto mais nós com *forward propagation*  existe na rede, maior a distância entre as camadas e consequente mente maior a chance (sem técnicas de mitigação) dos gradientes de camadas iniciais ser consideravelmente menor (em magnitude) aos gradientes das layers finais. o problema inverso (quando o gradiente inicial é muito maior que o final) é chamado de explosão de gradiente.

# colapso de modo (mode collapse)
Acontece quando o modelo passa a produzir saidas com baixa diversidade do esperado, ou seja, ha pouca ou nenhuma variação as épocas anteriores (diferentemente de over e underfitting, onde o modelo ou aprende caracteristicas locais - over - que não se generalizam ou, o contrário, onde ele sequer os aprende).

Regras de mitigação deste sintoma:

- Regra de atualização de duas escalas de tempo.
- A discriminação de minilotes permite que o discriminador avalie lotes inteiros de amostras, incentivando a diversidade.
- GANs desenrolados otimizam o gerador em relação aos estados futuros do discriminador.
- O Wasserstein GAN usa a distância do Earth Mover para fornecer gradientes mais estáveis.
- Use um conjunto de dados de treinamento grande e equilibrado.
- Métodos de regularização como penalidade de gradiente e normalização espectral.
