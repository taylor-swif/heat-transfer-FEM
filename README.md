# Finite Element Method (FEM) for Heat Transfer Equation

$$
\frac{d}{dx} \left( k(x)  \frac{du(x)}{dx}\right) = -100x
$$

$$
u(2) = 0
$$

$$
\frac{du(0)}{dx} + u(0) = 20
$$

$$
k(x) = \begin{cases}
  1 & \text{for } x \in [0,1] \\
  2x & \text{for } x \in (1,2]
\end{cases}
$$

$$
\text{Where } u \text{ is the function you are looking for}
$$

$$
[0,2] \ni x \mapsto u(x) \in \mathbb{R}
$$

### Requirements

Python, `numpy`, `matplotlib`, and `scipy`.
