# Qualidade da imagem
A qualidade da imagem pode ser avaliada via métricas

Erro Máximo: ME = $max \|f(x,y) - g(x,y)\|$

- quanto menor, mais a nova imagem se aproxima da original

Erro Médio Absoluto: MAE = $\frac{1}{MN} \sum^{M-1}_{x=0} \sum^{N-1}_{y=0} \|h(x, y)\|$

Erro Médio Quadrático: MSE =  $\frac{1}{MN} \sum^{M-1}_{x=0} \sum^{N-1}_{y=0} \|h(x, y) \|^2$


Raiz Erro Médio Quadrático: RMSE =  $\sqrt \text{MSE}$ 

Coeficiente de Jaccard:

$$ J = \frac{1}{MN} \sum^{M-1}_{x=0} \sum^{N-1}_{y=0} \left\{ \begin{aligned} \text{Statement 1} =1, \text{se } f(x,y) = g(x,y) \\ =0, \text{caso contrário} \end{aligned} \right.$$

sendo $h(x, y) = f(x, y) - g(x, y)$

---

