# 金饭碗

### 项目维护

#### 进入项目路径

```
cd /opt/jfw
```

#### 进入虚拟环境

```
source venv/bin/activate
```

#### 查看进程

```
ps auxw | grep python3
```

#### 服务启动

```
nohup python3 manage.py runserver 0.0.0.0:9091 &
```

### 项目安装

#### 进入路径拉取项目代码

```
cd /opt
git clone https://github.com/ginguocun/jfw.git
```

#### 创建虚拟环境 venv

```sh
python3 -m venv venv
```

#### 启动虚拟环境 

```
source venv/bin/activate
```

#### 更新 setuptools pip

```
pip3 install --upgrade setuptools pip
```

#### 安装依赖

```
pip install -r requirements.txt
```

## 用户小程序进入流程

```mermaid
graph TB
A(开始) --> B{用户是否登录}
B --> |否| C[游客模式]
B --> |是| D{判断用户类型}

用户角色 --> 客户
D --> |客户| E[获取菜品列表]
E --> H[进行点餐]
H --> L[订单提交]
L --> M{订单支付}
M --> |支付成功| N[订单取餐]
N --> O[订单评价]

用户角色 --> 商家
D --> |商家| F[获取订单信息]
F --> I[订单确认]
I --> P[订单发货]
P --> Q[订单收款]

用户角色 --> 游客
C --> |游客| G[获取随机菜品列表]
D --> |游客| G
G --> J[请求认证]
J --> K[获取手机号]
K --> R{获取公司信息}
R --> |是公司员工| S[客户]
R --> |获取不到公司信息| T[选择公司]
T --> U[公司管理员审核]
U --> S[客户]
R --> |获取不到公司信息| W[注册商家]
W --> Z[进行审核]
Z --> AA[商家]
```