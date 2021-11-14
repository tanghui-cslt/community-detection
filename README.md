##  *Community Decection applying to ossicles segmentation on Mesh*

![左边结果 ](./img/left_huang.png)
>Left is the original image ，right is new results

### Introdution
This project is based on [professor Luo's work](https://www.nature.com/articles/s41598-019-46380-9)，
it mainly applies olliver-ricci flow on community detection, deceting each compact community from a complex network by defining curvature on edges of mesh instead of defining on vertices. Comparing previous methodes, both the robustness and accuracy are improved. 

This repository introduces how to implement it.

Ossicles are the smallest bones in the human body, its interior is compact and it rare connect with other organs of our body. In this case, it can be seen as a community of a complex network when we scan our brain as a mesh. Searching for ossicles on our body can be transforms as detecting community on network. 



### Install

You need to install matlab 2017 or higher version and python3 firstly, and  download it.


```bash
git clone --recursive https://github.com/tanghui-cslt/community-detection.git
```
#### Method 1

Download and install [GraphRicciCurvature](https://github.com/saibalmars/GraphRicciCurvature.git)

This methos is very easy, but it will have different issuses when authors update it, so I will give another method to install it.


#### Method 2 ：Manual installation
versions of libraries that we will used：
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

### Start

There are two ossicles in the human body, in this project, I am going to take the left one as an example.


1.  Step 1 :

In `src/` directory，in matlab  :
```bash
step2_compare_region.m ，
``` 
Assgining a specific area including ossicle.


2.  Step2 : 

In `src/` directory，in python :
```bash

python step3_read_new.py

```

Esatablishing mesh, and saving as .gml file.


3.  Step3：

In `src/GraphRicciCurvature` directory, in python :
```bash

python step4_grid.py num orient

```
Where the first parameter is numbe, which ranges from 1 to 18; the second parameter can be set as left or right, for example.

```bash

python step4_grid.py 1 left

```
By utilizing ricci flow algorithm, it generates several different possible results.


4.  Step4：

In `src/GraphRicciCurvature` directory, in python  :
```bash
step5_subgraph.py 
```
Selecting the best result from all of them.



5. Step5：
In `src/` directory, in matlab :
```bash
step6_show_results.m
```


### Reference

Ni, CC., Lin, YY., Luo, F. et al. Community Detection on Networks with Ricci Flow. Sci Rep 9, 9984 (2019). 

#### Olliver-Ricci Curvature Project

<p align="center">
<img src="https://github.com/saibalmars/GraphRicciCurvature/raw/master/doc/_static/rf-manifold.png" title="Manifold Ricci flow" width="300" >
<img src="https://github.com/saibalmars/GraphRicciCurvature/raw/master/doc/_static/karate_demo.png" title="karate club demo" width="500" >
</p>

https://github.com/saibalmars/GraphRicciCurvature

