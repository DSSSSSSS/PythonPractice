# pandas入门

## 基本概念

`https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=pandas-colab&hl=zh-cn#scrollTo=av6RYOraVG1V`

```python
import pandas as pd
pd.__version__
```

*pandas* 中的主要数据结构被实现为以下两类：

* **`DataFrame`**，您可以将它想象成一个关系型数据表格，其中包含多个行和已命名的列。
* **`Series`**，它是单一列。`DataFrame` 中包含一个或多个 `Series`，每个 `Series` 均有一个名称。

数据框架是用于数据操控的一种常用抽象实现形式。[Spark](https://spark.apache.org/) 和 [R](https://www.r-project.org/about.html) 中也有类似的实现。
