# A-star
A star algorithm

$$
\sum_{k=-\infin}^{\infin} x_1(n-k) \cdot x_2(k) \\
= \sum_{k=-\infin}^{\infin} 2^{n-k} u(k-n) u(k) \\
= \begin{cases}
    \sum_{k=0}^{\infin} 2^{n-k},& \text{if } n < 0\\
    \sum_{k=n}^{\infin} 2^{n-k},& \text{otherwise}
\end{cases} \\
= \begin{cases}
    2^n \sum_{k=0}^{\infin} 2^{-k},& \text{if } n < 0\\
    2^n \sum_{k=n}^{\infin} 2^{-k},& \text{otherwise}
\end{cases} \\
= \begin{cases}
    2^n \frac{1}{1-1/2},& \text{if } n < 0\\
    2^n \frac{2^{-n}}{1-1/2},& \text{otherwise}
\end{cases} \\
= \begin{cases}
    2^{n+1},& \text{if } n < 0\\
    2,& \text{otherwise}
\end{cases} \\
$$
