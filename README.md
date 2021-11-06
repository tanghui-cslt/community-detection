##  *基于里奇流的网络聚类和社区检测*

![左边结果 ](.\img\left_huang.png)
>左边为原始的结果，右边为增加数据之后的结果

### 介绍
这个本项目基于[罗锋老师的工作](https://www.nature.com/articles/s41598-019-46380-9)，主要的是把ricci流应用在社区检测上，
能够从复杂的网络中检测出网络中的社区。相比于之前的方法，
这种方法的稳定性和检测结果都有很大的提高。

听小骨是人体中最小的骨头，而且在人体中属于相对独立的区域，内部比较紧密，与其他的组织联系较少，由此我们可以把听小骨看作是一个社区。所以我们把应用罗老师的算法应用图像上面，通过这种社区检测的算法，实现在图像上的听小骨的分割。

这个仓库主要是介绍整个代码的实现流程。

### 安装

下载整个代码，代码中包含matlab和python的代码，所以首先需要安装matlab 2017b及其 以上版本和python3。
#### 方法一
本代码主要基于[GraphRicciCurvature](https://github.com/saibalmars/GraphRicciCurvature.git)，按照它的安装流程，安装成功之后，才能顺利使用本项目的代码。

方法一比较简单，但是可能会由于作者更新版本的原因，可能会导致各种问题。所以给出手动安装的方法。
#### 方法二 ：手动安装
本人安装的库及其版本信息：
```bash
python     (version=3.6.5)
cvxpy      (version=1.0.31)
networkkit (version=6.0)
networkx   (version=2.1)
pot        (version=20.1)
numpy 
pandas
cython
```
可以使用pip手动安装以上的库。

### 开始

听小骨在人体中有两块，以下以左边的听小骨为例。 在本代码中，可以直接从第二步开始。

1.  第一步:在src目录下，在matlab的执行
step2_compare_region.m ，
选定一个特定的包含听小骨的区域。

2.  第二步:  在src/目录下，在python中运行
```bash

python step3_read_new.py

```
 建立网格，并保存为gml文件。

3.  第三步：
在src/GraphRicciCurvature，在python中运行
```bash

python step4_grid.py num orient

```
其中num为1-18中的一个数字，orient为left或right，例如：
```bash

python step4_grid.py 1 left

```
利用ricci流算法，从上一步得到的数据中得到几个待选的分割的听小骨数据。
4.  第四步：
在src/GraphRicciCurvature/，在python中运行
```bash
step5_subgraph.py 
```
从待选的数据中寻找最合适的数据，作为最终结果。


5. 第五步：
在src/，在matlab中运行step6_show_results.m 去掉像素值小于1000的像素点，作为最终结果。

