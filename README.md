# 基于卷积神经网络的地震正反演算法
---

本仓库提供了两种不同架构的卷积神经网络分别用于实现不同速度模型的地震正反演。

---
## 概述
我们在前人的神经网络架构基础上进行了部分改进，并分别将其用于实现不同速度模型的地震正反演问题。
* 基于WaveNet架构的卷积神经网络用于实现二维水平层状速度模型地震正演模拟和反演
* 基于Conditional-Encoder-Decoder(CED)架构的卷积神经网络用于实现带有矩形异常体的二维水平层状模型地震正演模拟和反演

## 安装
本仓库需要安装Python(用于深度学习)和Fortran(用于运行[SEISMIC CPML library](https://github.com/geodynamics/seismic_cpml)库提供的FD正演程序)。

我们推荐新建一个工作环境，如下所示：
```bash
conda create -n seismodinv python=3.6  # Use Anaconda package manager
conda activate seismodinv
```
然后安装以下Python依赖包：
```bash
pip install --ignore-installed --upgrade [packageURL]# install tensorflow (get packageURL from https://www.tensorflow.org/install/pip, see tensorflow website for details)
pip install torch==1.5.0 torchvision==0.6.0
pip install scipy matplotlib jupyter
pip install tensorflow==1.14.0
pip install tensorboardX
```
其中，**TensorFlow 版本为 1.14.0** (WaveNet卷积神经网络)， **PyTorch 版本为 1.5.0** (CED卷积神经网络)。

最后，还需要执行如下代码来编译SEISMIC CPML Fortran库：
```bash
git clone https://github.com/kisityan/seismodinv.git
cd seismodinv/CED/generate_data/Seismic_CPML/
make all
cd seismodinv/WaveNet/generate_data/Seismic_CPML/
make all
```
这一步会在`Seismic_CPML`文件夹下创建一个名为`xmodified_seismic_CPML_2D_pressure_second_order`的可执行文件。

鉴于本仓库使用的数据量太大（约4.0G），故将部分数据存储在Google Driver上，在执行程序之前Jupyter Notebook之前先下载相应数据。

## WaveNet网络工作流程
首先，介绍一下`WaveNet`文件夹下各个文件夹的用途：
*  `generate_data`用于生成速度模型、相应的反射率序列和FD正演模拟的地震记录，并将它们整合为一个二进制数据文件，用于训练网络
*  `WaveNet_train`用于定义并训练神经网络
*  `shared_modules`提供了一些共用的Python脚本
*  `plotting`用于绘制并保存相关图片

我们需要按照顺序执行以下脚本来训练网络：
1. `WaveNet/generate_data/velocity/generate_velocity_models.py`：生成随机的速度模型
2. `WaveNet/generate_data/velocity/preprocess_wavenet.py`：生成每个速度模型相应的垂向入射的反射率序列
3. `WaveNet/generate_data/gather/generate_forward_simulations.py`：生成每个速度模型相应的FD正演模拟的地震记录
4. `WaveNet/generate_data/data/convert_to_flat_binary_wavenet.py`：将生成的数据整合并写入一个二进制文件，用于训练网络
5. `WaveNet/WaveNet_train/main.py`：使用生成的数据训练网络并保存模型
6. 最后，`plotting`文件夹中的Jupyter Notebooks 可以使用训练好的模型生成相关图片，有助于对结果进行分析

## CED网络工作流程
`CED`文件夹下各个文件夹的用途：
*  `generate_data`用于生成速度模型和相应的FD正演模拟的地震记录，并将它们整合为一个二进制数据文件，用于训练网络
*  `CED_train`用于定义并训练神经网络
*  `shared_modules`提供了一些共用的Python脚本
*  `plotting`用于绘制并保存相关图片

我们需要按照顺序执行以下脚本来训练网络：
1. `CED/generate_data/velocity/generate_velocity_models.py`：生成随机的速度模型
2. `CED/generate_data/gather/generate_forward_simulations.py`：生成每个速度模型相应的FD正演模拟的地震记录
3. `CED/generate_data/data/convert_to_flat_binary_autoencoder.py`：将生成的数据整合并写入一个二进制文件，用于训练网络
4. `CED/CED_train/main_forward.py`：使用生成的数据训练网络并保存模型(正演)
5. `CED/CED_train/main_inverse.py`：使用生成的数据训练网络并保存模型(反演)
6. 最后，`plotting`文件夹中的Jupyter Notebooks 可以使用训练好的模型生成相关图片，有助于对结果进行分析