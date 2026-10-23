# 微信支付文档更新报告 - 直连商户

**文档类型**: 直连商户 (merchant)
**生成时间**: 20261023_053006
**文档总数**: 535
**数据来源**: https://pay.weixin.qq.com/doc/v3/merchant/llms.txt

## 变更概览

- 新增: 0 个页面
- 删除: 0 个页面
- 修改: 19 个页面
- 成功拉取: 19 个页面
- 拉取失败: 0 个页面
- llms.txt 变更: 是

## llms.txt 变更

```diff
--- llms_old.txt
+++ llms.txt
@@ -1,4 +1,4 @@
->更新时间：2026.10.20
+>更新时间：2026.10.23
 
 # 微信支付商户平台文档中心
 
```

## 修改页面

### 开发接入准备
- ID: `4015423216`
- 路径: JSAPI支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015423216.md
- 更新时间变更: 2026-10-14 06:35:25 -> 2026-10-22 10:23:33
- 本地文件: `pages/4015423216.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.10.14
+>更新时间：2026.10.22
 
 ```mermaid
 flowchart LR
```

### 开发接入准备
- ID: `4015478291`
- 路径: APP支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015478291.md
- 更新时间变更: 2026-10-15 09:24:46 -> 2026-10-22 10:23:37
- 本地文件: `pages/4015478291.md`

```diff
--- old.md
+++ new.md
@@ -1,47 +1,10 @@
->更新时间：2026.10.15
+>更新时间：2026.10.22
 
 ## 产品接入流程
 
-```mermaid
-flowchart LR
-    B(["接入APP支付<br/>阅读产品介绍"])
-    A{"是否有开放平台账号"}
-    C{是否已完成开放平台账号认证}
-    D{是否有移动应用appid}
-    E{是否有商户号}
-    F["登录商户平台开通<br/>APP支付权限"]
-    G["登录商户平台<br/>发起APPID授权绑定申请"]
-    H["登录开放平台<br/>确认授权绑定商户号"]
-    I["给技术负责人<br/>配置商户平台账号"]
-    J["获取开发参数<br/>进入开发流程"]
-    K[注册开放平台账号]
-    L[进行开放平台账号认证]
-    M[创建移动应用appid]
-    O["在商户平台申请商户号<br/>（可同时申请APP支付权限）"]
-    B --> A
-    A -->|是| C
-    C -->|是| D
-    D -->|是| E
-    E -->|是| F
-    F --> G
-    G --> H
-    H --> I
-    I --> J
-    A -->|否| K
-    K --> L
-    L --> M
-    C -->|否| L
-    D -->|否| M
-    M --> E
-    E -->|否| O
-    O -->|系统自动对申请权限时填入的APPID发起授权绑定申请| H
-    A@{ w: 254.9, h: 123.8 }
-    C@{ w: 214, h: 111.8 }
-    D@{ w: 200.5, h: 113 }
-    E@{ w: 210, h: 111.4 }
-```
+## ```mermaid flowchart LR     B(["接入APP支付<br/>阅读产品介绍"])     A{"是否有开放平台账号"}     C{是否已完成开放平台账号认证}     D{是否有移动应用appid}     E{是否有商户号}     F["登录商户平台开通<br/>APP支付权限"]     G["登录商户平台<br/>发起APPID授权绑定申请"]     H["登录开放平台<br/>确认授权绑定商户号"]     I["给技术负责人<br/>配置商户平台账号"]     J["获取开发参数<br/>进入开发流程"]     K[注册开放平台账号]     L[进行开放平台账号认证]     M[创建移动应用appid]     O["在商户平台申请商户号<br/>（可同时申请APP支付权限）"]     B --> A     A -->|是| C     C -->|是| D     D -->|是| E     E -->|是| F     F --> G     G --> H     H --> I     I --> J     A -->|否| K     K --> L     L --> M     C -->|否| L     D -->|否| M     M --> E     E -->|否| O     O -->|系统自动对申请权限时填入的APPID发起授权绑定申请| H     A@{ w: 254.9, h: 123.8 }     C@{ w: 214, h: 111.8 }     D@{ w: 200.5, h: 113 }     E@{ w: 210, h: 111.4 } ```
 
-接入流程说明
+## 接入流程说明
 
 1、阅读[产品介绍文档](https://pay.weixin.qq.com/doc/v3/merchant/4013070158.md)，了解APP支付产品特性；
 
```

### 开发接入准备
- ID: `4015614193`
- 路径: H5支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015614193.md
- 更新时间变更: 2026-10-16 04:04:12 -> 2026-10-22 10:23:30
- 本地文件: `pages/4015614193.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.10.16
+>更新时间：2026.10.22
 
 ```mermaid
 flowchart LR
```

### 开发接入准备
- ID: `4015614538`
- 路径: Native支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015614538.md
- 更新时间变更: 2026-10-16 04:03:49 -> 2026-10-22 10:23:28
- 本地文件: `pages/4015614538.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.10.16
+>更新时间：2026.10.22
 
 ```mermaid
 flowchart LR
@@ -26,7 +26,7 @@
     C -->|否| L
     E -->|否| O
     L --> E
-    O -->|"申请时如果填写了服务号/政府或媒体类型的公众号APPID，<br/>申请完成后，系统会自动对该APPID发起授权绑定申请"| H
+    O -->|"申请时如果填写了服务号/政府或媒体类型的公众号APPID，申请完成后，系统会自动对该APPID发起授权绑定申请"| H
     I --> D
     A@{ w: 310.5, h: 266.5 }
     C@{ w: 213.3, h: 132.5 }
```

### 开发接入准备
- ID: `4015764634`
- 路径: JSAPI合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015764634.md
- 更新时间变更: 2026-09-18 02:15:41 -> 2026-10-19 06:20:57
- 本地文件: `pages/4015764634.md`

```diff
--- old.md
+++ new.md
@@ -1,54 +1,37 @@
->更新时间：2026.09.18
+>更新时间：2026.10.19
 
 ```mermaid
 flowchart LR
-    A(["接入JSAPI合单支付
-阅读产品介绍"])
-    B{"合单发起方商户
-与所有子单参与方商户号
-是否开通JSAPI支付权限"}
+    A(["接入JSAPI合单支付<br/>阅读产品介绍"])
+    B{"合单发起方商户<br/>与所有子单参与方商户号<br/>是否开通JSAPI支付权限"}
+    C{"合单发起方商户号<br/>和所有子单参与方商户号<br/>是否开通合单支付权限"}
+    D["参考指引<br/>开通JSAPI支付"]
+    E{"合单发起方商户号<br/>与所有子单参与方商户号<br/>是否都绑定同一个combine_appid"}
+    F["合单发起方商户联系对接的运营人员申请合单支付权限"]
+    G{"合单发起方商户号<br/>是否配置支付授权目录"}
+    H["所有商户号的超管<br/>各自登录商户平台<br/>发起APPID授权绑定申请"]
+    I["APPID的管理员<br/>登录公众平台<br/>确认授权绑定商户号"]
+    J["获取开发参数<br/>进入开发流程<br/>"]
+    K["合单发起方商户号<br/>登录商户平台<br/>配置支付授权目录"]
     A --> B
-    B@{ w: 295, h: 175.1 }
-    C{"合单发起方商户号
-和所有子单参与方商户号
-是否开通合单支付权限"}
     B -->|是| C
-    C@{ w: 294.3, h: 174.3 }
-    D["参考指引
-开通JSAPI支付"]
     B -->|否| D
     D --> C
-    E{"合单发起方商户号
-与所有子单参与方商户号
-是否都绑定同一个combine_appid"}
     C -->|是| E
-    E@{ w: 327.9, h: 179.7 }
-    F["合单发起方商户联系对接的运营人员申请合单支付权限"]
     C -->|否| F
-    F@{ w: 243, h: 62.1 }
     F --> E
-    G{"合单发起方商户号
-是否配置支付授权目录"}
     E -->|是| G
-    G@{ w: 264.4, h: 149.6 }
-    H["所有商户号的超管
-各自登录商户平台
-发起APPID授权绑定申请"]
     E -->|否| H
-    I["APPID的管理员
-登录公众平台
-确认授权绑定商户号"]
     H --> I
     I --> G
-    J["获取开发参数
-进入开发流程
-"]
     G -->|是| J
-    K["合单发起方商户号
-登录商户平台
-配置支付授权目录"]
     G -->|否| K
     K --> J
+    B@{ w: 295, h: 175.1 }
+    C@{ w: 294.3, h: 174.3 }
+    E@{ w: 327.9, h: 179.7 }
+    F@{ w: 243, h: 62.1 }
+    G@{ w: 264.4, h: 149.6 }
 ```
 
 流程说明
```

### 开发接入准备
- ID: `4013420660`
- 路径: APP合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md
- 更新时间变更: 2026-09-18 02:15:37 -> 2026-10-19 06:20:45
- 本地文件: `pages/4013420660.md`

```diff
--- old.md
+++ new.md
@@ -1,53 +1,37 @@
->更新时间：2026.09.18
+>更新时间：2026.10.19
 
 ```mermaid
 flowchart LR
-    A(["接入APP合单支付
-阅读产品介绍"])
-    B{"合单发起方商户
-和所有子单参与方商户号
-是否开通APP支付权限"}
+    A(["接入APP合单支付<br/>阅读产品介绍"])
+    B{"合单发起方商户<br/>和所有子单参与方商户号<br/>是否开通APP支付权限"}
+    C{"合单发起方商户号<br/>和所有子单参与方商户号<br/>是否开通合单支付权限"}
+    D["参考指引<br/>开通APP支付"]
+    E{"合单发起方商户号<br/>和所有子单参与方商户号<br/>是否都绑定同一个combine_appid"}
+    F["合单发起方商户联系对接的运营人员申请合单支付权限"]
+    G{APPID是否配置了移动应用参数}
+    H["所有商户号的超管<br/>各自登录商户平台<br/>发起APPID授权绑定申请"]
+    I["APPID的管理员<br/>登录开放平台<br/>确认授权绑定商户号"]
+    J["获取开发参数<br/>进入开发流程<br/>"]
+    K["APPID的管理员<br/>登录开放平台<br/>配置移动应用参数"]
     A --> B
-    B@{ w: 295, h: 175.1 }
-    C{"合单发起方商户号
-和所有子单参与方商户号
-是否开通合单支付权限"}
     B -->|是| C
-    C@{ w: 294.3, h: 174.3 }
-    D["参考指引
-开通APP支付"]
     B -->|否| D
     D --> C
-    E{"合单发起方商户号
-和所有子单参与方商户号
-是否都绑定同一个combine_appid"}
     C -->|是| E
-    E@{ w: 327.9, h: 179.7 }
-    F["合单发起方商户联系对接的运营人员申请合单支付权限"]
     C -->|否| F
-    F@{ w: 243, h: 62.1 }
     F --> E
-    G{APPID是否配置了移动应用参数}
     E -->|是| G
-    G@{ w: 222.9, h: 138.5 }
-    H["所有商户号的超管
-各自登录商户平台
-发起APPID授权绑定申请"]
     E -->|否| H
-    I["APPID的管理员
-登录开放平台
-确认授权绑定商户号"]
     H --> I
     I --> G
-    J["获取开发参数
-进入开发流程
-"]
     G -->|是| J
-    K["APPID的管理员
-登录开放平台
-配置移动应用参数"]
     G -->|否| K
     K --> J
+    B@{ w: 295, h: 175.1 }
+    C@{ w: 294.3, h: 174.3 }
+    E@{ w: 327.9, h: 179.7 }
+    F@{ w: 243, h: 62.1 }
+    G@{ w: 222.9, h: 138.5 }
 ```
 
 流程说明
```

### 开发接入准备
- ID: `4015764448`
- 路径: H5合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015764448.md
- 更新时间变更: 2026-09-18 02:15:35 -> 2026-10-19 06:20:31
- 本地文件: `pages/4015764448.md`

```diff
--- old.md
+++ new.md
@@ -1,54 +1,37 @@
->更新时间：2026.09.18
+>更新时间：2026.10.19
 
 ```mermaid
 flowchart LR
-    A(["接入H5合单支付
-阅读产品介绍"])
-    B{"合单发起方商户
-与所有子单参与方商户号
-是否开通H5支付权限"}
+    A(["接入H5合单支付<br/>阅读产品介绍"])
+    B{"合单发起方商户<br/>与所有子单参与方商户号<br/>是否开通H5支付权限"}
+    C{"合单发起方商户号<br/>和所有子单参与方商户号<br/>是否开通合单支付权限"}
+    D["参考指引<br/>开通H5支付"]
+    E{"合单发起方商户号<br/>与所有子单参与方商户号<br/>是否都绑定同一个combine_appid"}
+    F["合单发起方商户联系对接的运营人员申请合单支付权限"]
+    G{"合单发起方商户号<br/>是否配置H5支付域名"}
+    H["所有商户号的超管<br/>各自登录商户平台<br/>发起APPID授权绑定申请"]
+    I["APPID的管理员<br/>登录公众平台或开放平台<br/>确认授权绑定商户号"]
+    J["获取开发参数<br/>进入开发流程<br/>"]
+    K["合单发起方商户号<br/>登录商户平台<br/>配置H5支付域名"]
     A --> B
-    B@{ w: 295, h: 175.1 }
-    C{"合单发起方商户号
-和所有子单参与方商户号
-是否开通合单支付权限"}
     B -->|是| C
-    C@{ w: 294.3, h: 174.3 }
-    D["参考指引
-开通H5支付"]
     B -->|否| D
     D --> C
-    E{"合单发起方商户号
-与所有子单参与方商户号
-是否都绑定同一个combine_appid"}
     C -->|是| E
-    E@{ w: 327.9, h: 179.7 }
-    F["合单发起方商户联系对接的运营人员申请合单支付权限"]
     C -->|否| F
-    F@{ w: 243, h: 62.1 }
     F --> E
-    G{"合单发起方商户号
-是否配置H5支付域名"}
     E -->|是| G
-    G@{ w: 264.4, h: 149.6 }
-    H["所有商户号的超管
-各自登录商户平台
-发起APPID授权绑定申请"]
     E -->|否| H
-    I["APPID的管理员
-登录公众平台或开放平台
-确认授权绑定商户号"]
     H --> I
     I --> G
-    J["获取开发参数
-进入开发流程
-"]
     G -->|是| J
-    K["合单发起方商户号
-登录商户平台
-配置H5支付域名"]
     G -->|否| K
     K --> J
+    B@{ w: 295, h: 175.1 }
+    C@{ w: 294.3, h: 174.3 }
+    E@{ w: 327.9, h: 179.7 }
+    F@{ w: 243, h: 62.1 }
+    G@{ w: 264.4, h: 149.6 }
 ```
 
 流程说明
```

### 开发接入准备
- ID: `4015764779`
- 路径: Native合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015764779.md
- 更新时间变更: 2026-09-18 02:15:34 -> 2026-10-19 06:20:28
- 本地文件: `pages/4015764779.md`

```diff
--- old.md
+++ new.md
@@ -1,45 +1,31 @@
->更新时间：2026.09.18
+>更新时间：2026.10.19
 
 ```mermaid
 flowchart LR
-    A(["接入Native合单支付
-阅读产品介绍"])
-    B{"合单发起方商户
-与所有子单参与方商户号
-是否开通Native支付权限"}
+    A(["接入Native合单支付<br/>阅读产品介绍"])
+    B{"合单发起方商户<br/>与所有子单参与方商户号<br/>是否开通Native支付权限"}
+    C{"合单发起方商户号<br/>和所有子单参与方商户号<br/>是否开通合单支付权限"}
+    D["参考指引<br/>开通Native支付"]
+    E{"合单发起方商户号<br/>与所有子单参与方商户号<br/>是否都绑定同一个combine_appid"}
+    F["合单发起方商户联系对接的运营人员申请合单支付权限"]
+    H["所有商户号的超管<br/>各自登录商户平台<br/>发起APPID授权绑定申请"]
+    I["APPID的管理员<br/>登录公众平台或开放平台<br/>确认授权绑定商户号"]
+    J["获取开发参数<br/>进入开发流程<br/>"]
     A --> B
-    B@{ w: 295, h: 175.1 }
-    C{"合单发起方商户号
-和所有子单参与方商户号
-是否开通合单支付权限"}
     B -->|是| C
-    C@{ w: 294.3, h: 174.3 }
-    D["参考指引
-开通Native支付"]
     B -->|否| D
     D --> C
-    E{"合单发起方商户号
-与所有子单参与方商户号
-是否都绑定同一个combine_appid"}
     C -->|是| E
-    E@{ w: 327.9, h: 179.7 }
-    F["合单发起方商户联系对接的运营人员申请合单支付权限"]
     C -->|否| F
-    F@{ w: 243, h: 62.1 }
     F --> E
-    H["所有商户号的超管
-各自登录商户平台
-发起APPID授权绑定申请"]
     E -->|否| H
-    I["APPID的管理员
-登录公众平台或开放平台
-确认授权绑定商户号"]
     H --> I
-    J["获取开发参数
-进入开发流程
-"]
     E -->|是| J
     I --> J
+    B@{ w: 295, h: 175.1 }
+    C@{ w: 294.3, h: 174.3 }
+    E@{ w: 327.9, h: 179.7 }
+    F@{ w: 243, h: 62.1 }
 ```
 
 流程说明
```

### 开发接入准备
- ID: `4015765029`
- 路径: 小程序合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015765029.md
- 更新时间变更: 2026-09-18 02:15:32 -> 2026-10-19 06:19:58
- 本地文件: `pages/4015765029.md`

```diff
--- old.md
+++ new.md
@@ -1,45 +1,31 @@
->更新时间：2026.09.18
+>更新时间：2026.10.19
 
 ```mermaid
 flowchart LR
-    A(["接入小程序合单支付
-阅读产品介绍"])
-    B{"合单发起方商户
-与所有子单参与方商户号
-是否开通JSAPI支付权限"}
+    A(["接入小程序合单支付<br/>阅读产品介绍"])
+    B{"合单发起方商户<br/>与所有子单参与方商户号<br/>是否开通JSAPI支付权限"}
+    C{"合单发起方商户号<br/>和所有子单参与方商户号<br/>是否开通合单支付权限"}
+    D["参考指引<br/>开通JSAPI支付权限"]
+    E{"合单发起方商户号<br/>与所有子单参与方商户号<br/>是否都绑定同一个combine_appid"}
+    F["合单发起方商户联系对接的运营人员申请合单支付权限"]
+    H["所有商户号的超管<br/>各自登录商户平台<br/>发起APPID授权绑定申请"]
+    I["APPID的管理员<br/>登录公众平台<br/>确认授权绑定商户号"]
+    J["获取开发参数<br/>进入开发流程<br/>"]
     A --> B
-    B@{ w: 295, h: 175.1 }
-    C{"合单发起方商户号
-和所有子单参与方商户号
-是否开通合单支付权限"}
     B -->|是| C
-    C@{ w: 294.3, h: 174.3 }
-    D["参考指引
-开通JSAPI支付权限"]
     B -->|否| D
     D --> C
-    E{"合单发起方商户号
-与所有子单参与方商户号
-是否都绑定同一个combine_appid"}
     C -->|是| E
-    E@{ w: 327.9, h: 179.7 }
-    F["合单发起方商户联系对接的运营人员申请合单支付权限"]
     C -->|否| F
-    F@{ w: 243, h: 62.1 }
     F --> E
-    H["所有商户号的超管
-各自登录商户平台
-发起APPID授权绑定申请"]
     E -->|否| H
-    I["APPID的管理员
-登录公众平台
-确认授权绑定商户号"]
     H --> I
-    J["获取开发参数
-进入开发流程
-"]
     E -->|是| J
     I --> J
+    B@{ w: 295, h: 175.1 }
+    C@{ w: 294.3, h: 174.3 }
+    E@{ w: 327.9, h: 179.7 }
+    F@{ w: 243, h: 62.1 }
 ```
 
 流程说明
```

### 开发指引
- ID: `4016824681`
- 路径: 医保支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4016824681.md
- 更新时间变更: 2026-06-12 03:00:17 -> 2026-10-22 06:50:36
- 本地文件: `pages/4016824681.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.06.12
+>更新时间：2026.10.22
 
 微信支付为接入移动医保支付的合作伙伴及商户提供专属技术支持，涵盖全流程接入指引与报错协助排查。
 
@@ -85,7 +85,25 @@
 - 若授权失效或授权状态不明确，应先重新完成授权，再继续医保费用确认，避免出现后续下单失败或医保结算不一致的问题。
 
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/29340709eba6405f23b283662c86f788.png)
+```mermaid
+sequenceDiagram
+  autonumber
+  actor p0 as 患者（缴费者）
+  participant p1 as 医疗机构系统
+  participant p2 as 微信医保应用系统
+  participant p3 as 医保系统
+  p0->>p1: 展示待缴费单据
+  p0->>p1: 缴纳医疗费
+  opt 患者挂号类型不是“自费挂号”
+    p1->>p2: 获取在线医保支付免密授权 pay_auth_no
+    p2->>p3: 获取授权
+    opt 在线医保支付授权不存在或已过期
+      p3->>p0: 授权在线医保免密支付
+    end
+    p1->>p3: 预结算医保费用（pay_auth_no，医疗费用清单）
+    p3-->>p1: 医保结算订单号 payOrdid、医疗费用组合
+  end
+```
 
 ### 2.2、商户下单
 
@@ -101,7 +119,19 @@
 
 `prepay_id`：预支付交易会话标识。调起支付时需要使用的参数， `prepay_id` 有效期为2小时，超过2小时，商户需要使用原下单参数重新请求下单接口，获取新的 `prepay_id`。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/26d9526b89fb47dcba8e9f47ac2c5f2a.png)
+```mermaid
+sequenceDiagram
+  autonumber
+  actor p0 as 用户
+  participant p1 as 商户前端页面（微信浏览器打开）
+  participant p2 as 商户后端
+  participant p3 as 微信支付系统
+  p0->>p1: 用户下单
+  p1->>p2: 发送下单请求
+  p2->>p3: 调用JSAPI/小程序下单接口
+  p3-->>p2: 下单成功返回 prepay_id
+  p2-->>p1: JSAPI拉起支付所需参数
+```
 
 #### 2.2.2、医保自费混合收款下单
 
@@ -137,7 +167,19 @@
 
 `mix_trade_no`：医保自费混合订单号，后续查单时优先使用该字段。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/9af9f79a17778c900551e1c93a140f69.png)
+```mermaid
+sequenceDiagram
+  autonumber
+  actor p0 as 患者（缴费者）
+  participant p1 as 商户小程序或公众号H5
+  participant p2 as 商户后台
+  participant p3 as 微信支付系统
+  p0->>p1: 用户下单
+  p1->>p2: 自费下单请求
+  p2->>p3: 调用JSAPI/小程序下单接口
+  p3->>p2: 下单成功返回prepay_id
+  p2->>p1: 返回JSAPI/小程序拉起医保自费混合支付所需参数
+```
 
 ### 2.3、商户调起医保支付
 
@@ -147,7 +189,15 @@
 
 `mixTradeNo`：混合收款单 ID，来源于医保自费混合收款下单接口返回的 `mix_trade_no`。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/4ee5c6b3f149cd95130e2e7aa2e5b456.png)
+```mermaid
+sequenceDiagram
+  autonumber
+  actor p0 as 用户
+  participant p1 as 商户前端页面（微信浏览器打开）
+  participant p2 as 商户后端
+  participant p3 as 微信支付系统
+  p1->>p3: 调起微信浏览器内置对象方法拉起微信收银台
+```
 
 ### 2.4、用户支付
 
@@ -173,7 +223,34 @@
 
 若因特殊原因需在用户可支付时间范围内关闭订单，自费部分可调用[关闭订单](https://pay.weixin.qq.com/doc/v3/merchant/4012791860.md)接口，医保部分需要在医保局侧进行关单处理。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/8189962f997b472a61226f7d4552d9d3.png)
+```mermaid
+sequenceDiagram
+  autonumber
+  actor p0 as 患者
+  participant p1 as 用户小程序或公众号H5
+  participant p2 as 商户后台
+  participant p3 as 微信医保应用系统
+  participant p4 as 微信支付系统
+  p4->>p1: 用户返回商户前端/小程序（会有回调function）
+  p1->>p2: 请求确认订单状态
+  p2->>p3: 调用查单接口
+  p3-->>p2: 订单状态
+  p2-->>p1: 订单状态
+  p1->>p0: 根据订单状态展示支付结果
+  alt 支付成功
+    p4->>p2: 支付成功回调通知
+  end
+  alt 未收到支付成功回调
+    p2->>p3: 调用查单接口轮询查单
+    p3-->>p2: 订单状态
+    alt 超过一定时间查单还是未支付状态
+      Note over p0: 自费部分调微信支付基础关单接口。医保部分在医保局侧关单
+      p2->>p4: 调用关单接口
+      p4-->>p2: 关单结果
+      p2->>p2: 订单当作失败终态处理
+    end
+  end
+```
 
 ### 2.5、冲正
 
@@ -207,7 +284,24 @@
 
 `refund_time`：医保退款成功时间，格式为 `yyyy-MM-DDTHH:mm:ss+TIMEZONE`。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/52e15fb4c895995902ec7e89e30ef864.png)
+```mermaid
+sequenceDiagram
+  autonumber
+  actor p0 as 患者(缴费者)
+  participant p1 as 医疗机构系统
+  participant p2 as 微信支付系统
+  participant p3 as 微信医保应用系统
+  participant p4 as 医保系统
+  p0->>p1: 申请退款
+  alt 医疗费用组合：纯医保/医保自费混合
+    p1->>p4: 申请医保退款
+    p1->>p4: 查看医保退款结果
+    p1->>p3: 接收医保退款结果
+  end
+  alt 医疗费用组合：纯自费/医保自费混合
+    p1->>p2: 受理商户退款
+  end
+```
 
 ## 3、整体流程时序图
 
@@ -215,7 +309,89 @@
 
 商户接入时，查询混合支付结果要通过微信的查单接口，而不是通过中台的接口，否则可能会导致资损。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/a83c86cba88b37f90aab065873707ae6.png)
+```mermaid
+sequenceDiagram
+  autonumber
+  actor p0 as 患者(缴费者)
+  participant p1 as 医疗机构系统
+  participant p2 as 微信支付系统
+  participant p3 as 微信医保应用系统
+  participant p4 as 医保系统
+  participant p5 as 时间
+  p0->>p1: 展示待缴费单据
+  p0->>p1: 缴纳医疗费
+  opt 患者挂号类型不是“自费挂号”
+    p1->>p3: 获取在线医保支付免密授权pay_auth_no
+    p3->>p4: 获取授权
+    opt 在线医保支付授权不存在或已过期
+      p4->>p0: 授权在线医保免密支付
+    end
+    p1->>p4: 预结算医保费用（pay_auth_no，医疗费用清单)
+    p4-->>p1: 医保结算订单号payOrdid、医疗费用组合
+  end
+  p1->>p0: 确认缴费
+  alt 医疗费用组合：纯医保
+    p1->>p3: 收款（医保订单payOrdid，医疗收费清单）
+    p3->>p4: 查询医保订单信息（payOrdid）
+    p3->>p2: 核实微信支付用户身份
+    p2->>p0: 验证微信支付用户密码
+    p3->>p4: 结算医保费用（payOrdid）
+    loop 医保结算结果为“不确定” 且 当前未超过医保结算时限
+      p3->>p4: 查看医保结算结果
+    end
+    alt 医保结算结果：成功
+      p3->>p3: 记录医保结算结果为“成功”
+      p3->>p1: 接收医保结算收款结果
+    else 失败
+      p3->>p3: 记录医保结算结果为“失败”
+    else 不确定
+      p3->>p3: 记录医保结算结果为“失败”
+      loop 冲正失败
+        p3->>p4: 冲正医保结算结果
... 已截断其余 47 行 diff
```

### 申请医保支付权限
- ID: `4016824675`
- 路径: 医保支付 > 附录
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4016824675.md
- 更新时间变更: 2026-09-18 08:04:05 -> 2026-10-20 10:23:18
- 本地文件: `pages/4016824675.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.09.18
+>更新时间：2026.10.20
 
 ## 概览
 
@@ -12,17 +12,10 @@
 
 ```mermaid
 flowchart LR
-  A["第一步
-医疗结构向省医保局
-申请接入移动医保支付
-历史已完成则跳过"] --> B["第二步
-向微信申请医院立项
-历史已接入旧接口则跳过
-"]
-    C["第三步
-向微信申请开通
-医保支付新接口支付权限"]
+    C["第三步<br/>向微信申请开通<br/>医保支付新接口支付权限"]
+  A["第一步<br/>医疗结构向省医保局申请接入移动医保支付历史已完成则跳过"] --> B["第二步<br/>向微信申请医院立项<br/>历史已接入旧接口则跳过<br/>"]
     B --> C
+    A@{ w: 293.2, h: 102 }
 ```
 
 ## 1、医疗机构申请接入省移动医保支付
```

### 开发指引
- ID: `4012715211`
- 路径: 商家转账
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012715211.md
- 更新时间变更: 2026-06-23 08:13:21 -> 2026-10-20 02:32:12
- 本地文件: `pages/4012715211.md`

```diff
--- old.md
+++ new.md
@@ -1,10 +1,24 @@
->更新时间：2026.06.23
+>更新时间：2026.10.20
 
 ## 1、开发前配置
 
 开发前，开发者需要完成如下两个步骤：配置开发参数和配置产品功能。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/4f62e12e53052bb2f5747cf827378e73.png)
+```mermaid
+flowchart LR
+    subgraph SG1[第一步：配置开发参数]
+        C["开发参数申请与绑定<br/>(appid+mchid)"]
+        D[配置API密钥]
+        E[下载配置商户证书]
+    end
+    subgraph SG2[第二步：配置产品功能]
+        A[设置接口安全IP]
+    end
+    C --> D
+    D --> E
+    SG1 --> SG2
+    C@{ w: 185.9, h: 77.7 }
+```
 
 ### 1.1、设置安全联系人
 
@@ -70,19 +84,15 @@
 
 ```mermaid
 sequenceDiagram
-    rect rgb(255,255,255)
-        autonumber
-        actor User as 用户
-        participant Mch as 商户系统
-        participant WxPay as 微信支付
-
-        User->>Mch: 申请提现
-        Mch->>WxPay: 发起商家转账
-
-        opt 受理转账成功
-            WxPay-->>Mch: 调起用户确认收款页的订单参数“package ”
-        end
-    end
+  autonumber
+  actor p0 as 用户
+  participant p1 as 商户系统
+  participant p2 as 微信支付
+  p0->>p1: 申请提现
+  p1->>p2: 发起商家转账
+  opt 受理转账成功
+    p2-->>p1: 调起用户确认收款页的订单参数“package”
+  end
 ```
 
 注意：
@@ -104,30 +114,22 @@
 
 ```mermaid
 sequenceDiagram
-    rect rgb(255,255,255)
-        autonumber
-        actor User as 用户
-        participant Mch as 商户系统
-        participant WxPay as 微信支付
-
-        Mch->>WxPay: 展示用户确认收款页
-        WxPay->>User: 确认收款
-		Note right of WxPay: 用户微信账户存在异常需要处理时，<br>可闭环在微信内解脱、完成收款
-        opt 用户可收款
-            WxPay->>WxPay: 转账到用户零钱
-        end
-
-        WxPay-->>User: 收款结果
-		Note right of WxPay: 撤销接口返回成功仅表示撤销请求已<br>受理，系统会异步处理退款等操作，<br>以最终查询转账单接口返回的状态为准。
-        opt 用户已通过其他方式收款
-            Mch->>WxPay: 撤销商家转账
-            WxPay-->>Mch: 撤销转账结果
-        end
-
-
-
-
-    end
+  autonumber
+  actor p0 as 用户
+  participant p1 as 商户系统
+  participant p2 as 微信支付
+  p1->>p2: 展示用户确认收款页
+  p2->>p0: 确认收款
+  opt 用户可收款
+    Note over p0: 用户微信账户存在异常需要处理时，可闭环在微信内解脱、完成收款
+    p2->>p2: 转账到用户零钱
+  end
+  p2-->>p0: 收款结果
+  opt 用户已通过其他方式收款
+    p1->>p2: 撤销商家转账
+    p2--)p1: 撤销转账结果
+    Note over p0: 撤销接口返回成功仅表示撤销请求已受理，系统会异步处理退款等操作，以最终查询转账单接口返回的状态为准。
+  end
 ```
 
 下面介绍在转账过程中的异常处理情况：
@@ -147,26 +149,23 @@
 
 ```mermaid
 sequenceDiagram
-    rect rgb(255,255,255)
-        autonumber
-        actor User as 用户
-        participant Mch as 商户系统
-        participant WxPay as 微信支付
-        participant P4 as 时间
-
-        opt 未收到商家转账成功回调通知，且查单结果还没有到达终态
-            Mch->>WxPay: 查询转账单
-            WxPay-->>Mch: 转账结果
-            Note over Mch,WxPay: 转账单状态为SUCCESS，才代表用户<br/>已实际领取了转账<br/><br/>转账单状态为FAIL 代表转账失败，<br/>为CANCELLED 代表已撤销。<br/><br/>以上三种为终态，说明转账单<br/>已处理完成，状态不会再变化。
-        end
-
-
-        opt 用户24小时未确认
-            P4->>WxPay: 退款用户未确认收款的转账单
-        end
-
-
-    end
+  autonumber
+  actor p0 as 用户
+  participant p1 as 商户系统
+  participant p2 as 微信支付
+  participant p3 as 时间
+  opt 未收到商家转账成功回调通知，且查单结果还没有到达终态
+    p1->>p2: 查询转账单
+    p2-->>p1: 转账结果
+  end
+  opt 用户24小时未确认
+    p3->>p2: 退款用户未确认收款的转账单
+  end
+  Note over p0,p1: 转账单状态为SUCCESS，才代表用户已实际领取了转账
+
+转账单状态为FAIL 代表转账失败，为CANCELLED 代表已撤销。
+
+以上三种为终态，说明转账单已处理完成，状态不会再变化。
 ```
 
 注意：
@@ -191,41 +190,31 @@
 ### 2.3、订单状态流转图
 
 ```mermaid
-%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
 stateDiagram-v2
-    direction LR
-    state "state：ACCEPTED（转账已受理）" as S2
-    state "state：PROCESSING（转账锁定资金中）" as S3
-    state "state：WAIT_USER_CONFIRM（待收款用户确认）" as S4
-    state "state：TRANSFERING（转账中）" as S5
-    state "state：SUCCESS（转账成功）" as S6
-    state "state：CANCELING（撤销中）" as S7
-    state "state：CANCELLED:（转账撤销完成）" as S8
-    state "state：FAIL（转账失败）" as S9
-
-    [*] --> S2: 商户调用发起转账接口生成转账单
-    S2 --> S3: 受理成功
-    S3 --> S4: 锁定资金成功
-    S7 --> S8: 撤销成功
-
-    S4 --> S7: 用户确认收款前，商户可主动撤销
-    S3 --> S7: 用户确认收款前，商户可主动撤销
-    S2 --> S7: 用户确认收款前，商户可主动撤销
-
-    S5 --> S6: 转账成功
-
-    S2 --> S9: 网路抖动等内部系统异常
-    S3 --> S9: 出资账户余额不足，商户超过24小时未充值
-    S4 --> S9: 转账单创建成功后，用户未在24小时内确认收款
-
-    S4 --> S5: 用户确认收款
-    S7 --> S5
-
-
-
-    S9 --> [*]
-    S6 --> [*]
-    S8 --> [*]
+  state "state：ACCEPTED （转账已受理）" as S0
+  state "state：PROCESSING （转账锁定资金中）" as S1
+  state "state：WAIT_USER_CONFIRM （待收款用户确认）" as S2
+  state "state：TRANSFERING （转账中）" as S3
+  state "state：SUCCESS （转账成功）" as S4
+  state "state：CANCELING （撤销中）" as S5
+  state "state：CANCELLED （转账撤销完成）" as S6
+  state "state：FAIL （转账失败）" as S7
+  [*] --> S0 : 商户调用发起转账接口生成转账单
+  S0 --> S1 : 受理成功
+  S1 --> S2 : 锁定资金成功
+  S2 --> S3 : 用户确认收款
... 已截断其余 161 行 diff
```

### 开发接入准备
- ID: `4012587112`
- 路径: 微信支付分
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012587112.md
- 更新时间变更: 2026-09-18 02:15:24 -> 2026-10-19 07:05:46
- 本地文件: `pages/4012587112.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.09.18
+>更新时间：2026.10.19
 
 ## 1、 权限申请要求说明
 
@@ -22,29 +22,22 @@
 
 ```mermaid
 flowchart LR
-  A[商户按照模板发送申请邮件] --> B["微信支付审核
-（审核通过后，微信支付会通过邮件回复对接人联系方式和技术支持群二维码）"]
-    C["签署协议
-（审核通过后，商户登录商户平台签署协议）"]
+    C["签署协议<br/>（审核通过后，商户登录商户平台签署协议）"]
+    D["商户侧技术开发<br/>（商户参考“开发指引”开发业务功能）"]
+    E["微信支付验收<br/>（商家按照开发验收要求<br/>提交验收资料）"]
+    F["微信支付上线<br/>（验收通过后，微信支付配置业务上线）"]
+    G["商户对外上线<br/>（商户配置业务上线，正式提供服务）"]
+  A[商户按照模板发送申请邮件] --> B["微信支付审核<br/>（审核通过后，微信支付会通过邮件回复对接人联系方式和技术支持群二维码）"]
     B --> C
+    B --> D
+    C --> E
+    D --> E
+    E --> F
+    F --> G
     B@{ w: 263.7, h: 140.4 }
     C@{ w: 228.9, h: 82.5 }
-    D["商户侧技术开发
-（商户参考“开发指引”开发业务功能）"]
-    B --> D
     D@{ w: 231.1, h: 78.7 }
-    E["微信支付验收
-（商家按照开发验收要求
-提交验收资料）"]
-    C --> E
-    D --> E
-    F["微信支付上线
-（验收通过后，微信支付配置业务上线）"]
-    E --> F
     F@{ w: 216.3, h: 99.5 }
-    G["商户对外上线
-（商户配置业务上线，正式提供服务）"]
-    F --> G
     G@{ w: 239.2, h: 100.9 }
 ```
 
```

### 开发指引
- ID: `4012587166`
- 路径: 微信支付分
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012587166.md
- 更新时间变更: 2026-09-18 02:15:22 -> 2026-10-19 07:07:24
- 本地文件: `pages/4012587166.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.09.18
+>更新时间：2026.10.19
 
 ## 1、开发前配置
 
@@ -7,18 +7,17 @@
 ```mermaid
 flowchart LR
     subgraph SG1[第一步：配置开发参数]
-        A["开发参数申请与绑定
-（appid+mchid）"]
+        A["开发参数申请与绑定<br/>（appid+mchid）"]
         B[配置API密钥]
         C[下载配置商户证书]
     end
-    A --> B
-    B --> C
     subgraph SG2[第二步：配置产品功能]
       direction TD
       D[绑定服务ID]
       E[配置用于开发的微信账号]
     end
+    A --> B
+    B --> C
     SG1 --> SG2
     D --> E
 ```
@@ -66,15 +65,14 @@
 
 ```mermaid
 sequenceDiagram
-
-        actor User as 用户
-        participant Mch as 商户系统
-        participant WxPay as 微信支付分小程序
-        participant WxPay2@{ type: actor, xwattType: secondaryActor } as 微信支付系统
-
-        User->>Mch: 用户下单
-        Mch->>WxPay2: 创建支付分订单
-        WxPay2-->>Mch: 返回用于拉起微信支付分小程确认订单参数“package”
+  autonumber
+  actor p0 as 用户
+  participant p1 as 商户系统
+  participant p2 as 微信支付分小程序
+  participant p3 as 微信支付系统
+  p0->>p1: 用户下单
+  p1->>p3: 创建支付分订单
+  p3-->>p1: 用于拉起微信支付分小程确认订单参数“package”
 ```
 
 下单接口需要注意的参数：
@@ -105,18 +103,17 @@
 
 ```mermaid
 sequenceDiagram
-
-        actor User as 用户
-        participant Mch as 商户系统
-        participant WxPay@{ type: boundary } as 微信支付分小程序
-        participant WxPay2@{ type: actor, xwattType: secondaryActor } as 微信支付系统
-
-        Mch->>WxPay: 跳转微信支付分小程序确认订单页
-        WxPay->>WxPay2: 判断用户是否有免押权益
-        WxPay2-->>WxPay: 获取综合评估结果
-        WxPay-->>User: 展示页面结果
-        User->>WxPay: 用户确认支付分订单
-        WxPay->>WxPay2: 发送确认请求
+  autonumber
+  actor p0 as 用户
+  participant p1 as 商户系统
+  participant p2 as 微信支付分小程序
+  participant p3 as 微信支付系统
+  p1->>p2: 跳转微信支付分小程序确认订单页
+  p2->>p3: 判断用户是否有免押权益
+  p3-->>p2: 获取综合评估结果
+  p2-->>p0: 展示页面结果
+  p0->>p2: 用户确认支付分订单
+  p2->>p3: 发送确认请求
 ```
 
 #### 2.2.3、商户提供服务
@@ -130,30 +127,25 @@
 
 ```mermaid
 sequenceDiagram
-        %% xwatt: autonumber ea
-        autonumber
-        actor User as 用户
-        participant Mch as 商户系统
-        participant WxPay as 微信支付分小程序
-        participant WxPay2 as 微信支付系统
-
-        WxPay2-)Mch: 异步通知商户确认订单回调结果
-        Mch->>Mch: 保存确认订单结果
-        Mch-->>WxPay2: 返回告知成功接收处理
-
-        alt 判断确认订单状态（未收到确认订单回调）
-            Mch->>WxPay2: 主动调用查询支付分订单接口，查询确认订单状态
-            WxPay2->>Mch: 返回确认订单状态结果
-            Mch->>Mch: 订单确认成功，为用户提供服务
-        end
-
-        opt 根据情况选择调用取消订单接口（服务过程中出现异常，商户主动终止服务）
-            Mch->>WxPay2: 调用取消订单接口
-            WxPay2-->>Mch: 返回取消订单结果
-        end
-
-        Mch->>WxPay2: 调用完结订单接口
-        WxPay2-->>Mch: 同步返回完结订单结果
+  autonumber
+  actor p0 as 用户
+  participant p1 as 商户系统
+  participant p2 as 微信支付分小程序
+  participant p3 as 微信支付系统
+  p3-)p1: 异步通知商户确认订单回调结果
+  p1->>p1: 保存确认订单结果
+  p1--)p3: 告知成功接收处理
+  alt 判断确认订单状态：未收到确认订单回调
+    p1->>p3: 主动调用查询支付分订单接口，查询确认订单状态
+    p3->>p1: 确认订单状态结果
+    p1->>p1: 订单确认成功，为用户提供服务
+  end
+  opt 根据情况选择调用取消订单接口：服务过程中出现异常，商户主动终止服务
+    p1->>p3: 调用取消订单接口
+    p3-->>p1: 取消订单结果
+  end
+  p1->>p3: 调用完结订单接口
+  p3-->>p1: 同步返回完结订单结果
 ```
 
 完结订单接口需要注意的参数：
@@ -191,30 +183,24 @@
 
 ```mermaid
 sequenceDiagram
-
-        %% xwatt: autonumber ea
-        autonumber
-        actor User as 用户
-        participant Mch as 商户系统
-        participant WxPay as 微信支付分小程序
-        participant WxPay2 as 微信支付系统
-
-        WxPay2-)Mch: 订单完结成功，微信支付进行轮询扣款，并在扣款成功后将扣款信息回调通知给商户系统
-
-        alt 判断订单扣款状态（未收到支付回调通知）
-            Mch->>WxPay2: 主动调用查询支付分订单状态接口，查询订单支付状态
-            WxPay2-->>Mch: 返回支付结果
-        end
-
-        opt 根据情况选择调用修改订单金额接口（扣款过程中，发现扣款金额有误且当前订单状态为“待支付”）
-            Mch->>WxPay2: 调用修改订单金额接口
-            WxPay2-->>Mch: 返回修改订单金额结果
-        end
-
-        opt 根据情况选择调用同步订单接口（扣款过程中，用户通过其它方式完成了支付，希望微信支付分停止继续扣款）
-            Mch->>WxPay2: 调用同步订单接口
-            WxPay2-->>Mch: 返回同步订单结果
-        end
+  autonumber
+  actor p0 as 用户
+  participant p1 as 商户系统
+  participant p2 as 微信支付分小程序
+  participant p3 as 微信支付系统
+  p3-)p1: 订单完结成功，微信支付进行轮询扣款，并在扣款成功后将扣款信息回调通知给商户系统
+  alt 判断订单扣款状态：未收到支付回调通知
+    p1->>p3: 主动调用查询支付分订单状态接口，查询订单支付状态
+    p3-->>p1: 支付结果
+  end
+  opt 根据情况选择调用修改订单金额接口：扣款过程中，发现扣款金额有误且当前订单状态为“待支付”
+    p1->>p3: 调用修改订单金额接口
+    p3-->>p1: 修改订单金额结果
+  end
+  opt 根据情况选择调用同步订单接口：扣款过程中，用户通过其它方式完成了支付，希望微信支付分停止继续扣款
+    p1->>p3: 调用同步订单接口
+    p3-->>p1: 同步订单结果
+  end
 ```
 
 #### 2.2.5、商户对账
@@ -239,30 +225,27 @@
 ### 2.3、订单状态流转图
 
 ```mermaid
-%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
 stateDiagram-v2
-    direction LR
-    state "state:CREATED(已创建)" as S2
-    state "state:EXPIRED(服务订单已失效)" as S3
-    state "state:DOING (进行中)<br/>state_description:USER_CONFIRM(用户已确认订单)" as S4
-    state "state:REVOKED(商户取消服务订单)" as S5
-    state "state:DOING (进行中)state description:MCH COMPLETE(商户已完结订单)collection.state:USER PAYING (订单待支付)" as S6
-    state "state:DONE(已完成)collection.state:USER_PAID (订单已支付)collection.detail.paid_type:MCH(通过商户其他渠道收款)" as S7
-    state "state:DONE(已完成)collection.state:USER PAID (订单已支付)collection.detail.paid_type:NEWTON (通过微信支付分收款)" as S8
-
-    [*] --> S2: 创建支付分订单
-    S2 --> S3: 超过30天
... 已截断其余 34 行 diff
```

### 开发指引
- ID: `4012077649`
- 路径: 微信支付分停车服务
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012077649.md
- 更新时间变更: 2026-06-09 07:58:42 -> 2026-10-19 08:12:24
- 本地文件: `pages/4012077649.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.06.09
+>更新时间：2026.10.19
 
 ## 1. 接口规则
 
@@ -16,66 +16,56 @@
 
 ```mermaid
 sequenceDiagram
-    rect rgb(255,255,255)
-        autonumber
-        actor User as 用户
-        participant P2 as 刷码器（停车场）
-        participant Mch as 商户
-        participant WxPay as 微信支付分停车服务
-
-        User->>P2: 识别车牌
-        P2->>Mch: 提交车牌信息
-        Mch->>WxPay: 调用创建停车入场
-        WxPay->>WxPay: 检查车牌开通情况、用户欠款信息
-        WxPay->>WxPay: 查询用户当前分数是否可用无感
-        WxPay-->>Mch: 返回车牌状态和入场ID
-
-        alt 支付分停车服务（未开通服务）
-            User->>Mch: 开通无感支付
-            Mch->>WxPay: 跳转至微信支付分停车服务小程序开通页
-            WxPay->>WxPay: 支付分授权，平台代扣开通授权
-
-            alt 授权完成
-                WxPay->>User: 拉起开通成功页
-                WxPay->>Mch: 服务状态变更通知
-                WxPay->>User: 服务开通通知
-            else 授权失败
-                WxPay->>User: 拉起开通失败页
-            end
-
-        else 已开通服务
-            WxPay->>User: 入场通知
-        end
-
-        opt 车主入场后车牌状态发送变更
-            WxPay->>WxPay: 场内车牌状态变化
-            WxPay->>Mch: 处理车主场内状态变更通知
-        end
-
-        User->>P2: 识别车牌
-        P2->>Mch: 提交车牌信息
-        Mch->>WxPay: 申请扣款（车牌信息和入场ID）
-        WxPay->>WxPay: 验证请求，受理扣款请求
-        Mch->>Mch: 处理受理结果
-        Mch->>P2: 放行车辆（受理成功）
-
-        alt 受理失败
-            Mch-->>P2: 现场缴费（受理失败）
-        end
-
-        WxPay->>Mch: 异步通知扣费结果
+  autonumber
+  actor p0 as 用户
+  participant p1 as 刷码器（停车场）
+  participant p2 as 商户
+  participant p3 as 微信支付分停车服务
+  p0->>p1: 识别车牌
+  p1->>p2: 提交车牌信息
+  p2->>p3: 调用创建停车入场
+  p3->>p3: 检查车牌开通情况、用户欠款信息
+  p3->>p3: 查询用户当前分数是否可用无感
+  p3-->>p2: 车牌状态和入场ID
+  alt 支付分停车服务：未开通服务
+    p0->>p2: 开通无感支付
+    p2->>p3: 跳转至微信支付分停车服务小程序开通页
+    p3->>p3: 支付分授权，平台代扣开通授权
+    alt 授权完成
+      p3->>p0: 拉起开通成功页
+      p3->>p2: 服务状态变更通知
+      p3->>p0: 服务开通通知
+    else 授权失败
+      p3->>p0: 拉起开通失败页
     end
+  else 已开通服务
+    p3->>p0: 入场通知
+  end
+  opt 车主入场后车牌状态发送变更
+    p3->>p3: 场内车牌状态变化
+    p3->>p2: 处理车主场内状态变更通知
+  end
+  p0->>p1: 识别车牌
+  p1->>p2: 提交车牌信息
+  p2->>p3: 申请扣款（车牌信息和入场ID）
+  p3->>p3: 验证请求，受理扣款请求
+  p2->>p2: 处理受理结果
+  p2->>p1: 放行车辆（受理成功）
+  alt 受理失败
+    p2-->>p1: 现场缴费（受理失败）
+  end
+  p3->>p2: 异步通知扣费结果
 ```
 
 重点步骤说明：
 
-步骤3 用户入场时，调用[创建停车入场](https://pay.weixin.qq.com/doc/v3/merchant/4012533937.md)接口创建停车入场信息。商户根据返回的车牌状态判断用户是否开通支付分停车服务。
+步骤1.3 用户入场时，调用[创建停车入场](https://pay.weixin.qq.com/doc/v3/merchant/4012533937.md)接口创建停车入场信息。商户根据返回的车牌状态判断用户是否开通支付分停车服务。
 
-步骤7 如果用户未开通支付分服务，可调用[调起微信支付分停车服务开通页](https://pay.weixin.qq.com/doc/v3/merchant/4012284186.md)接口为微信支付分开通小程序，引导用户进行服务开通。
+步骤1.6 如果用户未开通支付分服务，可调用[调起微信支付分停车服务开通页](https://pay.weixin.qq.com/doc/v3/merchant/4012284186.md)接口为微信支付分开通小程序，引导用户进行服务开通。
 
-步骤16 场内车牌发送变化后，微信支付通过[停车入场状态变更通知](https://pay.weixin.qq.com/doc/v3/merchant/4012284177.md)接口将车主状态变化通知给商户。
+步骤1.15 场内车牌发送变化后，微信支付通过[停车入场状态变更通知](https://pay.weixin.qq.com/doc/v3/merchant/4012284177.md)接口将车主状态变化通知给商户。
 
-步骤19 用户离场时，需调用[扣费受理](https://pay.weixin.qq.com/doc/v3/merchant/4012534352.md)接口完成订单受理，微信支付进行异步扣款，支付完成后，会将订单支付结果发送给商户。
+步骤1.18 用户离场时，需调用[扣费受理](https://pay.weixin.qq.com/doc/v3/merchant/4012534352.md)接口完成订单受理，微信支付进行异步扣款，支付完成后，会将订单支付结果发送给商户。
 
 ## 4. 开发注意事项
 
```

### 开发指引
- ID: `4012063233`
- 路径: 委托营销
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012063233.md
- 更新时间变更: 2026-06-09 07:59:03 -> 2026-10-19 08:26:15
- 本地文件: `pages/4012063233.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.06.09
+>更新时间：2026.10.19
 
 ## 1. 接口规则
 
@@ -16,30 +16,27 @@
 
 ```mermaid
 sequenceDiagram
-    rect rgb(255,255,255)
-        autonumber
-        actor User as 用户
-        actor P2 as 商家
-        participant P3 as 公众平台
-        participant WxPay as 微信支付
-
-        P2->>P3: 1、开通小程序直播插件()
-        P2->>WxPay: 2、创建商家券(商家券or支付券)
-        WxPay->>WxPay: 3、记录券批次信息()
-        P2->>WxPay: 4、完成批次号与appid之间的合作授权()
-        WxPay->>WxPay: 5、记录appid与批次号授权关系
-        P2->>P3: 6、配置直播间派发券信息(商家券or支付券)
-        User->>P3: 7、*进入指定商家直播间()
-        User->>P3: 8、领取券(商家券or支付券)
-        User->>WxPay: 9、进入卡包，查阅相关券信息()
-    end
+  autonumber
+  actor p0 as 用户
+  actor p1 as 商家
+  participant p2 as 公众平台
+  participant p3 as 微信支付
+  p1->>p2: 开通小程序直播插件
+  p1->>p3: 创建商家券
+  p3->>p3: 记录券批次信息
+  p1->>p3: 完成批次号与appid之间的合作授权
+  p3->>p3: 记录appid与批次号授权关系
+  p1->>p2: 配置直播间派发券信息
+  p0->>p2: 进入指定商家直播间
+  p0->>p2: 领取券
+  p0->>p3: 进入卡包，查阅相关券信息
 ```
 
 重点步骤说明：
 
-步骤4 商户调用《[建立合作关系](https://pay.weixin.qq.com/doc/v3/merchant/4012380498.md)》接口，将指定优惠券批次（支付券或商家券）授权给指定AppID。
-
-步骤7 用户在商家小程序直播间，可领取对应优惠券；（优惠券领取后，自动插入用户微信卡包）。
+步骤1.4 商户调用《[建立合作关系](https://pay.weixin.qq.com/doc/v3/merchant/4012380498.md)》接口，将指定优惠券批次（支付券或商家券）授权给指定AppID。
+
+步骤2.1 用户在商家小程序直播间，可领取对应优惠券；（优惠券领取后，自动插入用户微信卡包）。
 
 #### 3.2. API接入（含示例代码）
 
```

### 产品介绍
- ID: `4012061135`
- 路径: 支付即服务
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012061135.md
- 更新时间变更: 2026-05-21 02:57:16 -> 2026-10-22 12:18:29
- 本地文件: `pages/4012061135.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.10.22
+
 ## 简介
 
 服务人员，是商家为用户提供服务和转化生意的重要一环。通过支付即服务，商家可在支付完成后为用户推送专属服务人员名片，方便用户快速添加专属服务人员为好友，将线下短时服务转化为线上持续服务，弱联系变为强连接，提升用户体验和商家运营效率。
@@ -53,7 +55,18 @@
 
 支付即服务的接入流程如图所示：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/0937fd136bbf0809341002302267945d.jpeg)
+```mermaid
+sequenceDiagram
+  autonumber
+  participant p0 as 商家
+  participant p1 as 微信支付
+  actor p2 as 用户
+  p0->>p1: 开通并配置产品（商家在微信支付商户平台-产品中心，开通“支付即服务”，并进行产品配置）
+  p0->>p1: 注册（商家将服务人员注册在微信支付，微信支付会为每一个人员分配一个服务人员ID）
+  p0->>p1: 分配（商家在用户支付前，通过服务人员“分配API”将“服务人员ID+商户订单号”传入）
+  p0->>p1: 下单（使用相同的商家订单号调用微信支付下单API完成支付（下单支付流程不变））
+  p1->>p2: 展示入口（根据服务人员ID，在支付账单中展示服务入口）
+```
 
 1. 商家开通支付即服务，并进行产品相关设置，产品相关配置流程参见《[开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4012061536.md)》；
 
```

### 开发指引
- ID: `4012068499`
- 路径: 消费者投诉2.0
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012068499.md
- 更新时间变更: 2026-06-09 09:46:34 -> 2026-10-20 03:51:02
- 本地文件: `pages/4012068499.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.06.09
+>更新时间：2026.10.20
 
 ## 1. 接口规则
 
@@ -16,59 +16,52 @@
 
 ```mermaid
 sequenceDiagram
-    rect rgb(255,255,255)
-    actor 用户
-    participant 微信客户端
-    participant 微信支付系统
-    participant 商户后台
-
-    %% 主流程
-    用户->>微信客户端: 1、用户发起投诉()
-    微信客户端->>微信支付系统: 2、创建投诉单()
-    微信支付系统->>微信支付系统: 用户投诉次数(=1)
-    微信支付系统->>商户后台: 3、通知商户投诉待处理()
-    商户后台->>微信支付系统: 4、主动查询投诉单进展()
-    微信支付系统-->>商户后台: 5、返回查询结果()
-    商户后台->>商户后台: 投诉受理()
-    商户后台->>微信支付系统: 6、调用提交回复接口，回复投诉处理()
-    微信支付系统-->>微信客户端: 7、更新投诉单进展()
-    微信客户端-->>用户: 8、同步投诉回复()
-
-    %% 投诉处理结果分支
-    alt 投诉处理结果（满意投诉处理结果）
-        商户后台->>微信支付系统: 9、反馈处理完成()
-        微信支付系统->>微信客户端: 10、更新投诉单进展()
-        微信客户端-->>用户: 11、同步投诉处理完成()
-    else 不满意投诉处理结果
-        用户->>微信客户端: 12、用户继续投诉()
-        微信客户端->>微信客户端: 记录用户继续投诉内容()
-        微信客户端->>微信支付系统: 13、投诉单状态转为待处理()
-        微信支付系统->>微信支付系统: 用户投诉次数(+1)
-        微信支付系统->>商户后台: 14、通知商户投诉待处理()
-        商户后台->>微信支付系统: 15、主动查询投诉单进展()
-        微信支付系统-->>商户后台: 16、返回查询结果()
-        商户后台->>商户后台: 投诉受理()
-    end
-
-    %% 并行处理par块
-    par 并行处理
-        微信支付系统->>商户后台: 1、通知商户投诉最新进展()
-        商户后台-->>微信支付系统: 2、返回通知处理结果()
-        商户后台->>微信支付系统: 3、主动查询投诉单进展()
-        微信支付系统-->>商户后台: 4、返回查询结果()
-    end
-    end
+  autonumber
+  actor p0 as 用户
+  participant p1 as 微信客户端
+  participant p2 as 微信支付系统
+  participant p3 as 商户后台
+  p0->>p1: 用户发起投诉
+  p1->>p2: 创建投诉单
+  p2->>p2: 用户投诉次数
+  p2->>p3: 通知商户投诉待处理
+  p3->>p2: 主动查询投诉单进展
+  p2-->>p3: 查询结果
+  p3->>p3: 投诉受理
+  p3->>p2: 调用提交回复接口，回复投诉处理
+  p2-->>p1: 更新投诉单进展
+  p1-->>p0: 同步投诉回复
+  alt 投诉处理结果：满意投诉处理结果
+    p3->>p2: 反馈处理完成
+    p2-->>p1: 更新投诉单进展
+    p1-->>p0: 同步投诉处理完成
+  else 不满意投诉处理结果
+    p0->>p1: 用户继续投诉
+    p1->>p1: 记录用户继续投诉内容
+    p1->>p2: 投诉单状态转为待处理
+    p2->>p2: 用户投诉次数
+    p2->>p3: 通知商户投诉待处理
+    p3->>p2: 主动查询投诉单进展
+    p2-->>p3: 查询结果
+    p3->>p3: 投诉受理
+  end
+  par 并行处理
+    p2->>p3: 通知商户投诉最新进展
+    p3-->>p2: 通知处理结果
+    p3->>p2: 主动查询投诉单进展
+    p2-->>p3: 查询结果
+  end
 ```
 
 重点步骤说明：
 
-步骤3： 用户发起投诉后，微信支付通过[投诉通知回调](https://pay.weixin.qq.com/doc/v3/merchant/4012289719.md)通知商户投诉单需处理。
-
-步骤6： 商户接收投诉后，可通过[回复用户API](https://pay.weixin.qq.com/doc/v3/merchant/4012467254.md)接口向微信支付提交投诉处理回复。
-
-步骤9： 与用户协商一致后，商户通过[反馈处理完成API](https://pay.weixin.qq.com/doc/v3/merchant/4012467255.md)反馈投诉单处理完成。
-
-步骤15： 商户在没有接收到微信投诉通知的情况下可主动调用[查询投诉单详情](https://pay.weixin.qq.com/doc/v3/merchant/4012533436.md)查询投诉单处理结果。
+步骤1.4： 用户发起投诉后，微信支付通过[投诉通知回调](https://pay.weixin.qq.com/doc/v3/merchant/4012289719.md)通知商户投诉单需处理。
+
+步骤1.7： 商户接收投诉后，可通过[回复用户API](https://pay.weixin.qq.com/doc/v3/merchant/4012467254.md)接口向微信支付提交投诉处理回复。
+
+步骤1.8： 与用户协商一致后，商户通过[反馈处理完成API](https://pay.weixin.qq.com/doc/v3/merchant/4012467255.md)反馈投诉单处理完成。
+
+步骤3.1： 商户在没有接收到微信投诉通知的情况下可主动调用[查询投诉单详情](https://pay.weixin.qq.com/doc/v3/merchant/4012533436.md)查询投诉单处理结果。
 
 ### 3.2. API接入（含示例代码）
 
```

### 业务示例代码
- ID: `4015821404`
- 路径: 消费者投诉2.0
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015821404.md
- 更新时间变更: 2026-06-10 07:28:20 -> 2026-10-21 08:12:12
- 本地文件: `pages/4015821404.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.06.10
+>更新时间：2026.10.21
 
 ## 1. 目标
 
@@ -290,43 +290,33 @@
 「普通咨询」的投诉单状态机：
 
 ```mermaid
-%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
 stateDiagram-v2
-    direction LR
-    state "state:PENDING(商户待处理)" as S2
-    state "state:PROCESSING(商户处理中)" as S3
-    state "state:PROCESSED(商户处理完成)" as S4
-
-    [*] --> S2: 用户提交投诉
-    S2 --> S3: 商家提交回复
-    S3 --> S4: 商家提交处理完成
-    S4 --> S3: 用户升级投诉(非全额退款到账)
-    note right of S4: 用户升级投诉(全额退款到账)
-    S4--> [*]
+  state "state：PENDING （商户待处理）" as S0
+  state "state：PROESSING （商户处理中）" as S1
+  state "state：PROCESSED （商户处理完成）" as S2
+  [*] --> S0 : 用户提交投诉
+  S0 --> S1 : 商家提交回复
+  S1 --> S2 : 商家提交处理完成
+  S2 --> S1 : 用户升级投诉 （非全额退款到账）
+  S2 --> [*]
+  S1 --> S1 : 商家提交回复
+  S2 --> S2 : 用户升级投诉 （全额退款到账）
 ```
 
 「退款申请」的投诉单状态机：
 
 ```mermaid
-%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
 stateDiagram-v2
-    direction LR
-    state "state:PENDING(商户待处理)" as S2
-    state "state:PROCESSED(商户处理完成)" as S3
-    state "state:PROCESSING(商户处理中)" as S4
-
-    [*] --> S2: 用户提交投诉
-    S2 --> S3: 退款到账事件
-    S2 --> S3: 用户提交投诉(用户提交表单阶段商家存在退款)
-    S2 --> S3: 商家驳回退款(非退款到账且未同意/驳回过)
-    S2 --> S4: 商家同意退款(非退款到账且未同意/驳回过)
-    S2 --> S4: 商家提交回复
-    S3 --> S4: 用户升级投诉(非全额退款到账)
-    S4 --> S3: 商家提交处理完成
-    S4 --> S3: 退款到账
-    S4 --> S3: 商家驳回退款(非退款到账且未同意/驳回过)
-    note right of S4: 用户升级投诉(全额退款到账)
-    S3 --> [*]
+  state "state：PENDING （商户待处理）" as S0
+  state "state：PROESSING （商户处理中）" as S1
+  state "state：PROCESSED （商户处理完成）" as S2
+  [*] --> S0 : 用户提交投诉
+  S0 --> S1 : 场景1：商家提交回复; 场景2：商家同意退款（非退款到账且未同意/驳回过）
+  S1 --> S2 : 场景1：商家提交处理完成； 场景2：退款到账； 场景3：商家驳回退款（非退款到账且未同意/驳回过）
+  S2 --> S1 : 用户升级投诉 （非全额退款到账）
+  S2 --> [*] : 用户升级投诉 （全额退款到账）
+  S0 --> S2 : 场景1：用户提交投诉（用户提交表单阶段商家存在退款）； 场景2：退款到账事件； 场景3：商家驳回退款（非退款到账且未同意/驳回过）
+  S1 --> S1 : 场景1：商家提交回复; 场景2：商家同意退款（非退款到账且未同意/驳回过）
 ```
 
 ### 3.1 商户投诉单获取
```

## 附录：所有页面清单

<details>
<summary>点击查看全部 535 个页面</summary>

| 序号 | 标题（链接） | ID | 更新时间 | 完整路径 |
|------|-------------|----|----------|----------|
| 1 | [微信支付接入Skill](pages/4019638116.md) | `4019638116` | 2026-09-17 08:58:11 | Skills |
| 2 | [Go](pages/4015119334.md) | `4015119334` | 2025-05-29 03:20:46 | 示例代码 |
| 3 | [Java](pages/4014931831.md) | `4014931831` | 2025-05-28 02:22:00 | 示例代码 |
| 4 | [付款码支付（V2）](pages/4012647301.md) | `4012647301` | 2025-04-25 07:32:13 | 付款码支付（V2） |
| 5 | [刷脸支付](pages/4012647399.md) | `4012647399` | 2024-10-08 06:20:39 | 刷脸支付 |
| 6 | [产品介绍](pages/4012062524.md) | `4012062524` | 2025-07-15 03:13:07 | JSAPI支付 |
| 7 | [开发接入准备](pages/4015423216.md) | `4015423216` | 2026-10-22 10:23:33 | JSAPI支付 |
| 8 | [开发指引](pages/4012791870.md) | `4012791870` | 2026-10-13 13:15:22 | JSAPI支付 |
| 9 | [常见问题](pages/4012791869.md) | `4012791869` | 2026-08-05 06:10:48 | JSAPI支付 |
| 10 | [JSAPI下单](pages/4012791856.md) | `4012791856` | 2026-10-11 07:41:55 | JSAPI支付 > API列表 |
| 11 | [JSAPI调起支付](pages/4012791857.md) | `4012791857` | 2025-02-26 09:52:40 | JSAPI支付 > API列表 |
| 12 | [微信支付订单号查询订单](pages/4012791858.md) | `4012791858` | 2024-12-27 04:05:55 | JSAPI支付 > API列表 |
| 13 | [商户订单号查询订单](pages/4012791859.md) | `4012791859` | 2024-12-27 04:16:21 | JSAPI支付 > API列表 |
| 14 | [关闭订单](pages/4012791860.md) | `4012791860` | 2024-12-11 07:29:28 | JSAPI支付 > API列表 |
| 15 | [支付成功回调通知](pages/4012791861.md) | `4012791861` | 2024-12-27 04:11:52 | JSAPI支付 > API列表 |
| 16 | [退款申请](pages/4012791862.md) | `4012791862` | 2025-01-09 03:18:26 | JSAPI支付 > API列表 |
| 17 | [查询单笔退款（通过商户退款单号）](pages/4012791863.md) | `4012791863` | 2025-01-09 03:19:47 | JSAPI支付 > API列表 |
| 18 | [发起异常退款](pages/4012791864.md) | `4012791864` | 2024-12-30 07:50:09 | JSAPI支付 > API列表 |
| 19 | [退款结果回调通知](pages/4012791865.md) | `4012791865` | 2025-01-02 08:01:31 | JSAPI支付 > API列表 |
| 20 | [申请交易账单](pages/4012791866.md) | `4012791866` | 2025-01-10 01:36:34 | JSAPI支付 > API列表 |
| 21 | [申请资金账单](pages/4012791867.md) | `4012791867` | 2025-01-09 03:34:15 | JSAPI支付 > API列表 |
| 22 | [下载账单](pages/4012791868.md) | `4012791868` | 2024-12-11 07:32:33 | JSAPI支付 > API列表 |
| 23 | [管理商户号绑定的APPID账号](pages/4013287010.md) | `4013287010` | 2025-06-27 07:01:07 | JSAPI支付 > 附录 |
| 24 | [配置JSAPI支付授权目录](pages/4013287088.md) | `4013287088` | 2025-07-15 01:34:39 | JSAPI支付 > 附录 |
| 25 | [申请JSAPI支付权限指引](pages/4012791854.md) | `4012791854` | 2025-06-27 09:19:31 | JSAPI支付 > 附录 |
| 26 | [各主体可申请的基础支付权限列表](pages/4015420731.md) | `4015420731` | 2025-06-27 06:54:59 | JSAPI支付 > 附录 |
| 27 | [产品介绍](pages/4013070158.md) | `4013070158` | 2025-11-18 07:10:06 | APP支付 |
| 28 | [开发接入准备](pages/4015478291.md) | `4015478291` | 2026-10-22 10:23:37 | APP支付 |
| 29 | [开发指引](pages/4013070176.md) | `4013070176` | 2026-06-09 07:58:00 | APP支付 |
| 30 | [常见问题](pages/4013070182.md) | `4013070182` | 2026-01-16 03:47:27 | APP支付 |
| 31 | [APP下单](pages/4013070347.md) | `4013070347` | 2025-03-31 06:15:03 | APP支付 > API列表 |
| 32 | [APP调起支付](pages/4013070351.md) | `4013070351` | 2025-02-19 03:53:32 | APP支付 > API列表 |
| 33 | [微信支付订单号查询订单](pages/4013070354.md) | `4013070354` | 2024-12-27 04:05:55 | APP支付 > API列表 |
| 34 | [商户订单号查询订单](pages/4013070356.md) | `4013070356` | 2024-12-27 04:16:21 | APP支付 > API列表 |
| 35 | [关闭订单](pages/4013070360.md) | `4013070360` | 2024-11-25 10:03:33 | APP支付 > API列表 |
| 36 | [支付成功回调通知](pages/4013070368.md) | `4013070368` | 2024-12-27 04:11:30 | APP支付 > API列表 |
| 37 | [退款申请](pages/4013070371.md) | `4013070371` | 2025-01-09 03:18:26 | APP支付 > API列表 |
| 38 | [查询单笔退款（通过商户退款单号）](pages/4013070374.md) | `4013070374` | 2025-01-09 03:19:47 | APP支付 > API列表 |
| 39 | [发起异常退款](pages/4013070379.md) | `4013070379` | 2024-12-30 07:50:09 | APP支付 > API列表 |
| 40 | [退款结果通知](pages/4013070388.md) | `4013070388` | 2025-01-02 08:01:31 | APP支付 > API列表 |
| 41 | [申请交易账单](pages/4013070395.md) | `4013070395` | 2025-01-10 01:36:34 | APP支付 > API列表 |
| 42 | [申请资金账单](pages/4013070400.md) | `4013070400` | 2025-01-09 03:34:15 | APP支付 > API列表 |
| 43 | [下载账单](pages/4013070401.md) | `4013070401` | 2024-11-25 10:03:12 | APP支付 > API列表 |
| 44 | [申请APP支付权限指引](pages/4013070174.md) | `4013070174` | 2025-07-03 08:51:42 | APP支付 > 附录 |
| 45 | [OpenSDK接入指南](pages/4013289321.md) | `4013289321` | 2025-07-03 08:51:42 | APP支付 > 附录 |
| 46 | [管理商户号绑定的APPID账号](pages/4013289251.md) | `4013289251` | 2025-07-03 09:06:29 | APP支付 > 附录 |
| 47 | [各主体可申请的基础支付权限列表](pages/4015477838.md) | `4015477838` | 2025-07-03 08:51:42 | APP支付 > 附录 |
| 48 | [产品介绍](pages/4012791832.md) | `4012791832` | 2025-07-17 08:07:32 | H5支付 |
| 49 | [开发接入准备](pages/4015614193.md) | `4015614193` | 2026-10-22 10:23:30 | H5支付 |
| 50 | [开发指引](pages/4012791831.md) | `4012791831` | 2026-06-09 09:47:23 | H5支付 |
| 51 | [常见问题](pages/4012791845.md) | `4012791845` | 2026-09-01 07:43:28 | H5支付 |
| 52 | [H5下单](pages/4012791834.md) | `4012791834` | 2025-03-31 06:15:01 | H5支付 > API列表 |
| 53 | [H5调起支付](pages/4012791835.md) | `4012791835` | 2024-12-11 07:24:11 | H5支付 > API列表 |
| 54 | [微信支付订单号查询订单](pages/4012791837.md) | `4012791837` | 2024-12-27 04:05:55 | H5支付 > API列表 |
| 55 | [商户订单号查询订单](pages/4012791838.md) | `4012791838` | 2024-12-27 04:16:21 | H5支付 > API列表 |
| 56 | [关闭订单](pages/4012791839.md) | `4012791839` | 2024-12-11 07:07:35 | H5支付 > API列表 |
| 57 | [支付成功回调通知](pages/4012791836.md) | `4012791836` | 2024-12-27 04:11:52 | H5支付 > API列表 |
| 58 | [退款申请](pages/4012810597.md) | `4012810597` | 2025-01-09 03:18:26 | H5支付 > API列表 |
| 59 | [查询单笔退款（按商户退款单号）](pages/4012810601.md) | `4012810601` | 2025-01-09 03:19:47 | H5支付 > API列表 |
| 60 | [发起异常退款](pages/4012810603.md) | `4012810603` | 2024-12-30 07:50:09 | H5支付 > API列表 |
| 61 | [退款结果回调通知](pages/4012810605.md) | `4012810605` | 2025-01-02 08:01:31 | H5支付 > API列表 |
| 62 | [申请交易账单](pages/4012810606.md) | `4012810606` | 2025-01-10 01:36:34 | H5支付 > API列表 |
| 63 | [申请资金账单](pages/4012810609.md) | `4012810609` | 2025-01-09 03:34:15 | H5支付 > API列表 |
| 64 | [下载账单](pages/4012810615.md) | `4012810615` | 2024-12-11 07:12:32 | H5支付 > API列表 |
| 65 | [管理商户号绑定的APPID账号](pages/4013287174.md) | `4013287174` | 2025-07-17 04:03:46 | H5支付 > 附录 |
| 66 | [配置H5支付域名](pages/4013287193.md) | `4013287193` | 2026-09-18 02:15:53 | H5支付 > 附录 |
| 67 | [H5收银台适老化字体规范](pages/4013317672.md) | `4013317672` | 2024-12-18 07:41:18 | H5支付 > 附录 |
| 68 | [各主体可申请的基础支付权限列表](pages/4015616699.md) | `4015616699` | 2025-07-17 07:54:58 | H5支付 > 附录 |
| 69 | [申请H5支付权限指引](pages/4012791841.md) | `4012791841` | 2025-07-17 08:07:32 | H5支付 > 附录 |
| 70 | [获取用户ip指引](pages/4018677409.md) | `4018677409` | 2026-03-13 07:56:04 | H5支付 > 附录 |
| 71 | [产品介绍](pages/4012791874.md) | `4012791874` | 2025-07-17 08:07:28 | Native支付 |
| 72 | [开发接入准备](pages/4015614538.md) | `4015614538` | 2026-10-22 10:23:28 | Native支付 |
| 73 | [开发指引](pages/4012791891.md) | `4012791891` | 2026-06-09 09:47:19 | Native支付 |
| 74 | [常见问题](pages/4012791890.md) | `4012791890` | 2026-05-19 07:39:26 | Native支付 |
| 75 | [Native下单](pages/4012791877.md) | `4012791877` | 2025-03-31 06:14:58 | Native支付 > API列表 |
| 76 | [Native调起支付](pages/4012791878.md) | `4012791878` | 2025-03-21 07:40:26 | Native支付 > API列表 |
| 77 | [微信支付订单号查询订单](pages/4012791879.md) | `4012791879` | 2024-12-27 04:05:55 | Native支付 > API列表 |
| 78 | [商户订单号查询订单](pages/4012791880.md) | `4012791880` | 2024-12-27 04:16:21 | Native支付 > API列表 |
| 79 | [关闭订单](pages/4012791881.md) | `4012791881` | 2024-12-11 02:38:00 | Native支付 > API列表 |
| 80 | [支付成功回调通知](pages/4012791882.md) | `4012791882` | 2024-12-27 04:11:52 | Native支付 > API列表 |
| 81 | [退款申请](pages/4012791883.md) | `4012791883` | 2025-01-09 03:18:26 | Native支付 > API列表 |
| 82 | [查询单笔退款（通过商户退款单号）](pages/4012791884.md) | `4012791884` | 2025-01-09 03:19:47 | Native支付 > API列表 |
| 83 | [发起异常退款](pages/4012791885.md) | `4012791885` | 2024-12-30 07:50:09 | Native支付 > API列表 |
| 84 | [退款结果回调通知](pages/4012791886.md) | `4012791886` | 2025-01-02 08:01:31 | Native支付 > API列表 |
| 85 | [申请交易账单](pages/4012791887.md) | `4012791887` | 2025-01-10 01:36:34 | Native支付 > API列表 |
| 86 | [申请资金账单](pages/4012791888.md) | `4012791888` | 2025-01-09 03:34:15 | Native支付 > API列表 |
| 87 | [下载账单](pages/4012791889.md) | `4012791889` | 2024-12-11 02:41:45 | Native支付 > API列表 |
| 88 | [管理商户号绑定的APPID账号](pages/4013287246.md) | `4013287246` | 2025-07-17 04:03:25 | Native支付 > 附录 |
| 89 | [各主体可申请的基础支付权限列表](pages/4015616698.md) | `4015616698` | 2025-07-17 07:54:27 | Native支付 > 附录 |
| 90 | [申请Native支付权限指引](pages/4012791875.md) | `4012791875` | 2025-07-17 08:07:28 | Native支付 > 附录 |
| 91 | [产品介绍](pages/4012791894.md) | `4012791894` | 2025-07-15 03:13:41 | 小程序支付 |
| 92 | [开发接入准备](pages/4015459512.md) | `4015459512` | 2026-10-16 07:09:29 | 小程序支付 |
| 93 | [开发指引](pages/4012791911.md) | `4012791911` | 2026-06-09 09:47:15 | 小程序支付 |
| 94 | [常见问题](pages/4012791910.md) | `4012791910` | 2026-08-05 09:20:37 | 小程序支付 |
| 95 | [JSAPI/小程序下单](pages/4012791897.md) | `4012791897` | 2025-03-31 06:15:06 | 小程序支付 > API列表 |
| 96 | [小程序调起支付](pages/4012791898.md) | `4012791898` | 2025-02-26 09:51:05 | 小程序支付 > API列表 |
| 97 | [微信支付订单号查询订单](pages/4012791899.md) | `4012791899` | 2024-12-27 04:05:55 | 小程序支付 > API列表 |
| 98 | [商户订单号查询订单](pages/4012791900.md) | `4012791900` | 2024-12-27 04:16:21 | 小程序支付 > API列表 |
| 99 | [关闭订单](pages/4012791901.md) | `4012791901` | 2024-12-11 03:13:31 | 小程序支付 > API列表 |
| 100 | [支付成功回调通知](pages/4012791902.md) | `4012791902` | 2024-12-27 04:11:52 | 小程序支付 > API列表 |
| 101 | [退款申请](pages/4012791903.md) | `4012791903` | 2025-01-09 03:18:26 | 小程序支付 > API列表 |
| 102 | [查询单笔退款（通过商户退款单号）](pages/4012791904.md) | `4012791904` | 2025-01-09 03:19:47 | 小程序支付 > API列表 |
| 103 | [发起异常退款](pages/4012791905.md) | `4012791905` | 2024-12-30 07:50:09 | 小程序支付 > API列表 |
| 104 | [退款结果回调通知](pages/4012791906.md) | `4012791906` | 2025-01-02 08:01:31 | 小程序支付 > API列表 |
| 105 | [申请交易账单](pages/4012791907.md) | `4012791907` | 2025-01-10 01:36:34 | 小程序支付 > API列表 |
| 106 | [申请资金账单](pages/4012791908.md) | `4012791908` | 2025-01-09 03:34:15 | 小程序支付 > API列表 |
| 107 | [下载账单](pages/4012791909.md) | `4012791909` | 2024-12-11 03:16:49 | 小程序支付 > API列表 |
| 108 | [管理商户号绑定的APPID账号](pages/4013287504.md) | `4013287504` | 2025-07-02 06:14:13 | 小程序支付 > 附录 |
| 109 | [申请JSAPI支付权限指引(小程序支付场景)](pages/4012791895.md) | `4012791895` | 2025-07-02 09:14:57 | 小程序支付 > 附录 |
| 110 | [各主体可申请的基础支付权限列表](pages/4015459054.md) | `4015459054` | 2025-07-02 06:14:13 | 小程序支付 > 附录 |
| 111 | [产品介绍](pages/4012077221.md) | `4012077221` | 2025-08-06 01:36:46 | JSAPI合单支付 |
| 112 | [开发接入准备](pages/4015764634.md) | `4015764634` | 2026-10-19 06:20:57 | JSAPI合单支付 |
| 113 | [开发指引](pages/4012078634.md) | `4012078634` | 2026-06-09 09:47:13 | JSAPI合单支付 |
| 114 | [常见问题](pages/4013421298.md) | `4013421298` | 2026-05-21 08:24:21 | JSAPI合单支付 |
| 115 | [JSAPI合单下单](pages/4012556926.md) | `4012556926` | 2025-01-14 02:41:58 | JSAPI合单支付 > API列表 |
| 116 | [JSAPI调起支付](pages/4012266069.md) | `4012266069` | 2025-02-19 03:55:33 | JSAPI合单支付 > API列表 |
| 117 | [查询合单订单](pages/4013421222.md) | `4013421222` | 2025-01-14 02:39:42 | JSAPI合单支付 > API列表 |
| 118 | [关闭合单订单](pages/4013421225.md) | `4013421225` | 2025-01-14 02:27:08 | JSAPI合单支付 > API列表 |
| 119 | [合单订单支付成功回调通知](pages/4013421231.md) | `4013421231` | 2025-01-14 02:40:06 | JSAPI合单支付 > API列表 |
| 120 | [退款申请](pages/4013421249.md) | `4013421249` | 2025-01-09 03:19:51 | JSAPI合单支付 > API列表 |
| 121 | [查询单笔退款（通过商户退款单号）](pages/4013421261.md) | `4013421261` | 2025-01-09 03:19:50 | JSAPI合单支付 > API列表 |
| 122 | [发起异常退款](pages/4013421269.md) | `4013421269` | 2025-01-09 03:19:49 | JSAPI合单支付 > API列表 |
| 123 | [退款结果回调通知](pages/4013421273.md) | `4013421273` | 2025-01-09 03:19:48 | JSAPI合单支付 > API列表 |
| 124 | [申请交易账单](pages/4013421277.md) | `4013421277` | 2025-01-09 03:19:47 | JSAPI合单支付 > API列表 |
| 125 | [申请资金账单](pages/4013421284.md) | `4013421284` | 2025-01-09 03:19:45 | JSAPI合单支付 > API列表 |
| 126 | [下载账单](pages/4013421294.md) | `4013421294` | 2025-01-09 03:19:44 | JSAPI合单支付 > API列表 |
| 127 | [管理商户号绑定的APPID账号](pages/4013426141.md) | `4013426141` | 2025-07-31 09:23:37 | JSAPI合单支付 > 附录 |
| 128 | [产品介绍](pages/4012077215.md) | `4012077215` | 2025-08-06 01:36:50 | APP合单支付 |
| 129 | [开发接入准备](pages/4013420660.md) | `4013420660` | 2026-10-19 06:20:45 | APP合单支付 |
| 130 | [开发指引](pages/4012077667.md) | `4012077667` | 2026-06-09 09:47:09 | APP合单支付 |
| 131 | [常见问题](pages/4013420906.md) | `4013420906` | 2026-05-20 08:33:17 | APP合单支付 |
| 132 | [App合单下单](pages/4012556944.md) | `4012556944` | 2025-01-14 02:41:38 | APP合单支付 > API列表 |
| 133 | [App调起支付](pages/4012266043.md) | `4012266043` | 2025-02-19 03:54:39 | APP合单支付 > API列表 |
| 134 | [查询合单订单](pages/4012557006.md) | `4012557006` | 2025-01-14 02:39:42 | APP合单支付 > API列表 |
| 135 | [关闭合单订单](pages/4012577452.md) | `4012577452` | 2025-01-14 02:27:08 | APP合单支付 > API列表 |
| 136 | [合单订单支付成功回调通知](pages/4012158598.md) | `4012158598` | 2025-01-14 02:40:06 | APP合单支付 > API列表 |
| 137 | [退款申请](pages/4012556524.md) | `4012556524` | 2025-01-09 03:18:26 | APP合单支付 > API列表 |
| 138 | [查询单笔退款（通过商户退款单号）](pages/4012556587.md) | `4012556587` | 2025-01-09 03:19:47 | APP合单支付 > API列表 |
| 139 | [发起异常退款](pages/4013420988.md) | `4013420988` | 2025-01-08 02:59:38 | APP合单支付 > API列表 |
| 140 | [退款结果回调通知](pages/4012085921.md) | `4012085921` | 2025-01-08 03:00:22 | APP合单支付 > API列表 |
| 141 | [申请交易账单](pages/4012556692.md) | `4012556692` | 2025-01-10 01:36:34 | APP合单支付 > API列表 |
| 142 | [申请资金账单](pages/4012556748.md) | `4012556748` | 2025-01-09 03:34:15 | APP合单支付 > API列表 |
| 143 | [下载账单](pages/4012085923.md) | `4012085923` | 2024-12-18 07:42:23 | APP合单支付 > API列表 |
| 144 | [产品介绍](pages/4013421104.md) | `4013421104` | 2025-08-06 01:36:48 | H5合单支付 |
| 145 | [开发接入准备](pages/4015764448.md) | `4015764448` | 2026-10-19 06:20:31 | H5合单支付 |
| 146 | [开发指引](pages/4012078230.md) | `4012078230` | 2026-06-09 09:47:00 | H5合单支付 |
| 147 | [常见问题](pages/4013421196.md) | `4013421196` | 2025-08-06 01:36:48 | H5合单支付 |
| 148 | [H5合单下单](pages/4012556961.md) | `4012556961` | 2025-01-14 02:40:23 | H5合单支付 > API列表 |
| 149 | [H5调起支付](pages/4012266131.md) | `4012266131` | 2025-01-09 03:20:15 | H5合单支付 > API列表 |
| 150 | [查询合单订单](pages/4013421126.md) | `4013421126` | 2025-01-14 02:39:42 | H5合单支付 > API列表 |
| 151 | [关闭合单订单](pages/4013421130.md) | `4013421130` | 2025-01-14 02:27:08 | H5合单支付 > API列表 |
| 152 | [合单订单支付成功回调通知](pages/4013421143.md) | `4013421143` | 2025-01-14 02:40:06 | H5合单支付 > API列表 |
| 153 | [退款申请](pages/4013421148.md) | `4013421148` | 2025-01-09 03:20:10 | H5合单支付 > API列表 |
| 154 | [查询单笔退款（通过商户退款单号）](pages/4013421156.md) | `4013421156` | 2025-01-09 03:20:09 | H5合单支付 > API列表 |
| 155 | [发起异常退款](pages/4013421164.md) | `4013421164` | 2025-01-09 03:20:08 | H5合单支付 > API列表 |
| 156 | [退款结果回调通知](pages/4013421172.md) | `4013421172` | 2025-01-09 03:20:06 | H5合单支付 > API列表 |
| 157 | [申请交易账单](pages/4013421176.md) | `4013421176` | 2025-01-09 03:20:05 | H5合单支付 > API列表 |
| 158 | [申请资金账单](pages/4013421185.md) | `4013421185` | 2025-01-09 03:20:04 | H5合单支付 > API列表 |
| 159 | [下载账单](pages/4013421189.md) | `4013421189` | 2025-01-09 03:20:03 | H5合单支付 > API列表 |
| 160 | [产品介绍](pages/4012077545.md) | `4012077545` | 2025-08-06 01:36:44 | Native合单支付 |
| 161 | [开发接入准备](pages/4015764779.md) | `4015764779` | 2026-10-19 06:20:28 | Native合单支付 |
| 162 | [开发指引](pages/4012078926.md) | `4012078926` | 2026-06-09 09:46:57 | Native合单支付 |
| 163 | [常见问题](pages/4013421369.md) | `4013421369` | 2026-05-20 09:55:27 | Native合单支付 |
| 164 | [Native合单下单](pages/4012556982.md) | `4012556982` | 2025-01-14 02:40:50 | Native合单支付 > API列表 |
| 165 | [Native调起支付](pages/4012266088.md) | `4012266088` | 2025-03-21 07:38:03 | Native合单支付 > API列表 |
| 166 | [查询合单订单](pages/4013421316.md) | `4013421316` | 2025-01-14 02:39:42 | Native合单支付 > API列表 |
| 167 | [关闭合单订单](pages/4013421330.md) | `4013421330` | 2025-01-14 02:27:08 | Native合单支付 > API列表 |
| 168 | [合单订单支付成功回调通知](pages/4013421336.md) | `4013421336` | 2025-01-14 02:40:06 | Native合单支付 > API列表 |
| 169 | [退款申请](pages/4013421340.md) | `4013421340` | 2025-01-09 03:19:34 | Native合单支付 > API列表 |
| 170 | [查询单笔退款（按商户退款单号）](pages/4013421346.md) | `4013421346` | 2025-01-09 03:19:33 | Native合单支付 > API列表 |
| 171 | [发起异常退款](pages/4013421352.md) | `4013421352` | 2025-01-09 03:19:32 | Native合单支付 > API列表 |
| 172 | [退款结果回调通知](pages/4013421356.md) | `4013421356` | 2025-01-09 03:19:31 | Native合单支付 > API列表 |
| 173 | [申请交易账单](pages/4013421361.md) | `4013421361` | 2025-01-09 03:19:29 | Native合单支付 > API列表 |
| 174 | [申请资金账单](pages/4013421365.md) | `4013421365` | 2025-01-09 03:19:28 | Native合单支付 > API列表 |
| 175 | [下载账单](pages/4013421368.md) | `4013421368` | 2025-01-09 03:19:37 | Native合单支付 > API列表 |
| 176 | [产品介绍](pages/4012077589.md) | `4012077589` | 2025-08-06 01:36:42 | 小程序合单支付 |
| 177 | [开发接入准备](pages/4015765029.md) | `4015765029` | 2026-10-19 06:19:58 | 小程序合单支付 |
| 178 | [开发指引](pages/4012079115.md) | `4012079115` | 2026-06-09 09:46:54 | 小程序合单支付 |
| 179 | [常见问题](pages/4013421468.md) | `4013421468` | 2026-05-20 09:57:11 | 小程序合单支付 |
| 180 | [小程序合单下单](pages/4012556931.md) | `4012556931` | 2025-01-14 02:41:58 | 小程序合单支付 > API列表 |
| 181 | [小程序调起支付](pages/4012266109.md) | `4012266109` | 2025-01-09 03:27:32 | 小程序合单支付 > API列表 |
| 182 | [查询合单订单](pages/4013421401.md) | `4013421401` | 2025-01-14 02:39:42 | 小程序合单支付 > API列表 |
| 183 | [关闭合单订单](pages/4013421404.md) | `4013421404` | 2025-01-14 02:27:08 | 小程序合单支付 > API列表 |
| 184 | [合单订单支付成功回调通知](pages/4013421407.md) | `4013421407` | 2025-01-14 02:40:06 | 小程序合单支付 > API列表 |
| 185 | [退款申请](pages/4013421410.md) | `4013421410` | 2025-01-09 03:27:26 | 小程序合单支付 > API列表 |
| 186 | [查询单笔退款（通过商户退款单号）](pages/4013421421.md) | `4013421421` | 2025-01-09 03:27:25 | 小程序合单支付 > API列表 |
| 187 | [发起异常退款](pages/4013421429.md) | `4013421429` | 2025-01-09 03:27:24 | 小程序合单支付 > API列表 |
| 188 | [退款结果回调通知](pages/4013421448.md) | `4013421448` | 2025-01-09 03:27:22 | 小程序合单支付 > API列表 |
| 189 | [申请交易账单](pages/4013421450.md) | `4013421450` | 2025-01-09 03:19:26 | 小程序合单支付 > API列表 |
| 190 | [申请资金账单](pages/4013421456.md) | `4013421456` | 2025-01-09 03:19:25 | 小程序合单支付 > API列表 |
| 191 | [下载账单](pages/4013421461.md) | `4013421461` | 2025-01-09 03:19:23 | 小程序合单支付 > API列表 |
| 192 | [产品介绍](pages/4035576700.md) | `4035576700` | 2026-08-27 07:42:28 | AI支付 |
| 193 | [开发接入准备](pages/4035576711.md) | `4035576711` | 2026-08-27 07:42:28 | AI支付 |
| 194 | [开发指引](pages/4035576716.md) | `4035576716` | 2026-09-01 02:01:16 | AI支付 |
| 195 | [常见问题](pages/4035576771.md) | `4035576771` | 2026-08-27 08:56:16 | AI支付 |
| 196 | [x402预下单](pages/4035576740.md) | `4035576740` | 2026-09-01 07:29:51 | AI支付 > API列表 |
| 197 | [产品介绍](pages/4016824672.md) | `4016824672` | 2026-06-08 09:46:23 | 医保支付 |
| 198 | [开发接入准备](pages/4016824684.md) | `4016824684` | 2026-06-11 09:17:26 | 医保支付 |
| 199 | [开发指引](pages/4016824681.md) | `4016824681` | 2026-10-22 06:50:36 | 医保支付 |
| 200 | [医保自费混合收款下单](pages/4016781466.md) | `4016781466` | 2025-12-04 08:22:16 | 医保支付 > API列表 > 医保自费混合订单 |
| 201 | [使用医保自费混合订单号查看下单结果](pages/4016781479.md) | `4016781479` | 2025-12-04 08:22:16 | 医保支付 > API列表 > 医保自费混合订单 |
| 202 | [使用商户订单号查看下单结果](pages/4016781490.md) | `4016781490` | 2025-12-04 08:22:16 | 医保支付 > API列表 > 医保自费混合订单 |
| 203 | [小程序调起医保自费混合支付](pages/4016781545.md) | `4016781545` | 2025-12-04 08:23:06 | 医保支付 > API列表 > 医保自费混合订单 |
| 204 | [JSAPI调起医保自费混合支付](pages/4016781549.md) | `4016781549` | 2025-12-04 08:23:19 | 医保支付 > API列表 > 医保自费混合订单 |
| 205 | [医保混合收款成功通知](pages/4016781554.md) | `4016781554` | 2025-12-04 08:23:33 | 医保支付 > API列表 > 医保自费混合订单 |
| 206 | [医保退款通知](pages/4016781561.md) | `4016781561` | 2025-12-04 08:17:01 | 医保支付 > API列表 > 医保退款 |
| 207 | [报错排查指引](pages/4020401138.md) | `4020401138` | 2026-05-14 09:21:09 | 医保支付 > 常见问题 |
| 208 | [业务&接口规则类问题](pages/4017415831.md) | `4017415831` | 2026-05-14 09:21:10 | 医保支付 > 常见问题 |
| 209 | [申请医保支付权限](pages/4016824675.md) | `4016824675` | 2026-10-20 10:23:18 | 医保支付 > 附录 |
| 210 | [接入医保亲情付指引](pages/4016975471.md) | `4016975471` | 2026-05-20 03:23:51 | 医保支付 > 附录 |
| 211 | [UI规范与页面说明](pages/4021595091.md) | `4021595091` | 2026-06-08 09:46:28 | 医保支付 > 附录 |
| 212 | [测试及环境切换](pages/4021773498.md) | `4021773498` | 2026-06-11 08:58:20 | 医保支付 > 附录 |
| 213 | [产品介绍](pages/4026275563.md) | `4026275563` | 2026-07-22 08:07:27 | 医保一码付 |
| 214 | [开发接入准备](pages/4026276029.md) | `4026276029` | 2026-07-22 08:13:57 | 医保一码付 |
| 215 | [开发指引](pages/4026276043.md) | `4026276043` | 2026-07-29 07:41:30 | 医保一码付 |
| 216 | [签约入口说明](pages/4026379305.md) | `4026379305` | 2026-07-29 07:26:20 | 医保一码付 > 附录 |
| 217 | [申请一码付权限](pages/4026292912.md) | `4026292912` | 2026-07-22 08:48:05 | 医保一码付 > 附录 |
| 218 | [测试信息准备和验收注意事项](pages/4026303367.md) | `4026303367` | 2026-07-22 08:47:51 | 医保一码付 > 附录 |
| 219 | [产品介绍](pages/4013071001.md) | `4013071001` | 2025-06-27 09:49:14 | 订单退款 |
| 220 | [开发指引](pages/4013071031.md) | `4013071031` | 2026-10-13 13:03:06 | 订单退款 |
| 221 | [常见问题](pages/4013071200.md) | `4013071200` | 2026-08-05 09:21:08 | 订单退款 |
| 222 | [业务示例代码](pages/4015217336.md) | `4015217336` | 2025-09-03 03:02:18 | 订单退款 |
| 223 | [申请退款](pages/4013071036.md) | `4013071036` | 2025-01-09 03:18:26 | 订单退款 > API列表 |
| 224 | [查询单笔退款（通过商户退款单号）](pages/4013071041.md) | `4013071041` | 2025-01-09 03:19:47 | 订单退款 > API列表 |
| 225 | [发起异常退款](pages/4013071193.md) | `4013071193` | 2024-12-30 07:50:09 | 订单退款 > API列表 |
| 226 | [退款结果通知](pages/4013071196.md) | `4013071196` | 2025-01-02 08:01:31 | 订单退款 > API列表 |
| 227 | [微信支付退款最佳实践](pages/4014959631.md) | `4014959631` | 2026-06-10 07:28:35 | 订单退款 > 附录 |
| 228 | [产品介绍](pages/4013071215.md) | `4013071215` | 2025-04-24 04:25:36 | 下载账单 |
| 229 | [开发指引](pages/4013071218.md) | `4013071218` | 2026-10-13 13:03:31 | 下载账单 |
| 230 | [业务示例代码](pages/4015945131.md) | `4015945131` | 2025-12-03 04:00:41 | 下载账单 |
| 231 | [常见问题](pages/4013071254.md) | `4013071254` | 2026-05-19 07:37:47 | 下载账单 |
| 232 | [申请交易账单](pages/4013071227.md) | `4013071227` | 2025-01-10 01:36:34 | 下载账单 > API列表 |
| 233 | [申请资金账单](pages/4013071235.md) | `4013071235` | 2025-01-09 03:34:15 | 下载账单 > API列表 |
| 234 | [下载账单](pages/4013071238.md) | `4013071238` | 2024-11-25 10:02:55 | 下载账单 > API列表 |
| 235 | [交易账单详细说明](pages/4013071246.md) | `4013071246` | 2026-01-16 03:52:29 | 下载账单 > 附录 |
| 236 | [资金账单详细说明](pages/4013071249.md) | `4013071249` | 2024-11-25 10:03:56 | 下载账单 > 附录 |
| 237 | [下载账单操作指引](pages/4013071252.md) | `4013071252` | 2024-11-25 10:03:53 | 下载账单 > 附录 |
| 238 | [产品介绍](pages/4012067962.md) | `4012067962` | 2025-05-13 02:17:45 | 分账 |
| 239 | [开发接入准备](pages/4012067989.md) | `4012067989` | 2026-05-19 08:32:51 | 分账 |
| 240 | [开发指引](pages/4012068033.md) | `4012068033` | 2026-06-09 07:58:27 | 分账 |
| 241 | [常见问题](pages/4014547102.md) | `4014547102` | 2026-08-05 06:11:11 | 分账 |
| 242 | [请求分账](pages/4012524936.md) | `4012524936` | 2025-09-29 01:57:06 | 分账 > API列表 |
| 243 | [查询分账结果](pages/4012525210.md) | `4012525210` | 2025-09-29 02:00:15 | 分账 > API列表 |
| 244 | [请求分账回退](pages/4012525287.md) | `4012525287` | 2025-09-29 04:02:15 | 分账 > API列表 |
| 245 | [查询分账回退结果](pages/4012526279.md) | `4012526279` | 2025-09-29 03:55:30 | 分账 > API列表 |
| 246 | [解冻剩余资金](pages/4012526374.md) | `4012526374` | 2025-09-29 03:55:05 | 分账 > API列表 |
| 247 | [查询剩余待分金额](pages/4012457939.md) | `4012457939` | 2025-09-29 03:54:33 | 分账 > API列表 |
| 248 | [添加分账接收方](pages/4012528995.md) | `4012528995` | 2025-09-29 03:53:57 | 分账 > API列表 |
| 249 | [删除分账接收方](pages/4012529590.md) | `4012529590` | 2025-09-29 03:52:35 | 分账 > API列表 |
| 250 | [分账动态通知](pages/4012289679.md) | `4012289679` | 2025-02-19 03:56:03 | 分账 > API列表 |
| 251 | [申请分账账单](pages/4012529628.md) | `4012529628` | 2025-09-29 03:52:05 | 分账 > API列表 |
| 252 | [下载账单](pages/4012289690.md) | `4012289690` | 2024-12-18 03:02:33 | 分账 > API列表 |
| 253 | [分账失败处理指引](pages/4015505684.md) | `4015505684` | 2025-07-04 03:41:52 | 分账 > 附录 |
| 254 | [产品介绍](pages/4012711988.md) | `4012711988` | 2026-08-07 02:45:50 | 商家转账 |
| 255 | [开发接入准备](pages/4013740645.md) | `4013740645` | 2026-06-01 03:29:49 | 商家转账 |
| 256 | [开发指引](pages/4012715211.md) | `4012715211` | 2026-10-20 02:32:12 | 商家转账 |
| 257 | [业务示例代码](pages/4018940876.md) | `4018940876` | 2026-04-23 09:22:55 | 商家转账 |
| 258 | [常见问题](pages/4013778940.md) | `4013778940` | 2026-08-05 06:11:24 | 商家转账 |
| 259 | [发起转账](pages/4012716434.md) | `4012716434` | 2025-03-21 02:52:14 | 商家转账 > API列表 > 发起转账 |
| 260 | [JSAPI调起用户确认收款](pages/4012716430.md) | `4012716430` | 2025-03-07 08:37:28 | 商家转账 > API列表 > 发起转账 |
| 261 | [撤销转账](pages/4012716458.md) | `4012716458` | 2025-03-18 03:21:03 | 商家转账 > API列表 > 发起转账 |
| 262 | [商户单号查询转账单](pages/4012716437.md) | `4012716437` | 2025-03-21 02:52:25 | 商家转账 > API列表 > 发起转账 |
| 263 | [微信单号查询转账单](pages/4012716457.md) | `4012716457` | 2025-03-21 02:52:21 | 商家转账 > API列表 > 发起转账 |
| 264 | [商家转账回调通知](pages/4012712115.md) | `4012712115` | 2025-03-07 10:05:02 | 商家转账 > API列表 > 发起转账 |
| 265 | [APP调起用户确认收款-Android](pages/4012719576.md) | `4012719576` | 2025-03-07 08:37:15 | 商家转账 > API列表 > 发起转账 > APP调起用户确认收款 |
| 266 | [APP调起用户确认收款-iOS](pages/4012719578.md) | `4012719578` | 2025-03-07 08:37:06 | 商家转账 > API列表 > 发起转账 > APP调起用户确认收款 |
| 267 | [APP调起用户确认收款-鸿蒙](pages/4019670774.md) | `4019670774` | 2026-04-14 08:28:51 | 商家转账 > API列表 > 发起转账 > APP调起用户确认收款 |
| 268 | [商户单号申请电子回单](pages/4012716452.md) | `4012716452` | 2025-03-21 02:51:55 | 商家转账 > API列表 > 获取电子回单 |
| 269 | [商户单号查询电子回单](pages/4012716436.md) | `4012716436` | 2025-03-21 02:52:17 | 商家转账 > API列表 > 获取电子回单 |
| 270 | [微信单号申请电子回单](pages/4012716456.md) | `4012716456` | 2025-03-21 02:50:21 | 商家转账 > API列表 > 获取电子回单 |
| 271 | [微信单号查询电子回单](pages/4012716455.md) | `4012716455` | 2025-03-21 02:47:21 | 商家转账 > API列表 > 获取电子回单 |
| 272 | [下载电子回单](pages/4013866774.md) | `4013866774` | 2025-03-10 07:43:13 | 商家转账 > API列表 > 获取电子回单 |
| 273 | [发起转账并完成免确认收款授权](pages/4014399293.md) | `4014399293` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 274 | [发起免确认收款授权](pages/4015901167.md) | `4015901167` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 275 | [JSAPI调起免确认收款授权](pages/4015930512.md) | `4015930512` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 276 | [商户单号查询授权结果](pages/4014399423.md) | `4014399423` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 277 | [用户授权后转账](pages/4014399371.md) | `4014399371` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 278 | [免确认收款授权结果通知](pages/4014512908.md) | `4014512908` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 279 | [商户单号查询转账单](pages/4024814206.md) | `4024814206` | 2026-07-08 08:25:48 | 商家转账 > API列表 > 用户授权免确认模式 |
| 280 | [微信单号查询转账单](pages/4024819515.md) | `4024819515` | 2026-07-08 08:25:48 | 商家转账 > API列表 > 用户授权免确认模式 |
| 281 | [解除免确认收款授权](pages/4015653811.md) | `4015653811` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 282 | [Android](pages/4020320167.md) | `4020320167` | 2026-05-08 02:23:41 | 商家转账 > API列表 > 用户授权免确认模式 > APP调起用户免确认收款授权 |
| 283 | [iOS](pages/4020320150.md) | `4020320150` | 2026-05-08 02:10:18 | 商家转账 > API列表 > 用户授权免确认模式 > APP调起用户免确认收款授权 |
| 284 | [鸿蒙](pages/4020320137.md) | `4020320137` | 2026-05-08 02:10:04 | 商家转账 > API列表 > 用户授权免确认模式 > APP调起用户免确认收款授权 |
| 285 | [充值](pages/4013747269.md) | `4013747269` | 2025-04-15 02:42:45 | 商家转账 > 附录 |
| 286 | [设置接口安全IP](pages/4013751010.md) | `4013751010` | 2026-01-15 08:16:29 | 商家转账 > 附录 |
| 287 | [设置转账额度](pages/4013747667.md) | `4013747667` | 2026-05-08 02:58:10 | 商家转账 > 附录 |
| 288 | [获取账单和电子回单](pages/4013748430.md) | `4013748430` | 2025-02-26 11:48:22 | 商家转账 > 附录 |
| 289 | [订单失败原因说明](pages/4013774966.md) | `4013774966` | 2025-04-15 02:42:41 | 商家转账 > 附录 |
| 290 | [商家转账到零钱升级说明](pages/4015273741.md) | `4015273741` | 2026-08-12 08:16:31 | 商家转账 > 附录 |
| 291 | [现金营销](pages/4013774588.md) | `4013774588` | 2025-07-15 01:38:23 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 292 | [企业赔付](pages/4013774589.md) | `4013774589` | 2025-07-15 01:38:18 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 293 | [佣金报酬](pages/4013774590.md) | `4013774590` | 2025-07-15 01:38:22 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 294 | [采购货款](pages/4013774591.md) | `4013774591` | 2025-07-15 01:38:16 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 295 | [二手回收](pages/4013774592.md) | `4013774592` | 2025-07-15 01:38:21 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 296 | [公益补助](pages/4013774593.md) | `4013774593` | 2025-07-15 01:38:19 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 297 | [行政补贴](pages/4013774594.md) | `4013774594` | 2025-07-15 01:38:14 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 298 | [保险理赔](pages/4013774595.md) | `4013774595` | 2026-02-05 07:23:07 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 299 | [产品介绍](pages/4012587050.md) | `4012587050` | 2024-12-09 09:50:51 | 微信支付分 |
| 300 | [开发接入准备](pages/4012587112.md) | `4012587112` | 2026-10-19 07:05:46 | 微信支付分 |
| 301 | [开发指引](pages/4012587166.md) | `4012587166` | 2026-10-19 07:07:24 | 微信支付分 |
| 302 | [常见问题](pages/4012587200.md) | `4012587200` | 2026-05-09 08:57:58 | 微信支付分 |
| 303 | [创建支付分订单](pages/4012587900.md) | `4012587900` | 2025-03-06 08:16:47 | 微信支付分 > API列表 |
| 304 | [查询支付分订单](pages/4012587902.md) | `4012587902` | 2024-12-10 09:27:51 | 微信支付分 > API列表 |
| 305 | [取消支付分订单](pages/4012587905.md) | `4012587905` | 2025-02-13 11:37:12 | 微信支付分 > API列表 |
| 306 | [JSAPI调起支付分确认订单页](pages/4012587945.md) | `4012587945` | 2024-11-21 08:08:28 | 微信支付分 > API列表 |
| 307 | [确认订单回调通知](pages/4012587953.md) | `4012587953` | 2024-12-10 09:27:47 | 微信支付分 > API列表 |
| 308 | [完结支付分订单](pages/4012587955.md) | `4012587955` | 2025-03-06 08:16:29 | 微信支付分 > API列表 |
| 309 | [修改订单金额](pages/4012587957.md) | `4012587957` | 2025-03-06 08:16:32 | 微信支付分 > API列表 |
| 310 | [支付成功回调通知](pages/4012587960.md) | `4012587960` | 2025-09-15 08:16:57 | 微信支付分 > API列表 |
| 311 | [同步订单状态](pages/4012587962.md) | `4012587962` | 2024-12-10 09:27:49 | 微信支付分 > API列表 |
| 312 | [申请退款](pages/4012587971.md) | `4012587971` | 2024-12-18 07:43:20 | 微信支付分 > API列表 |
| 313 | [查询退款](pages/4012587973.md) | `4012587973` | 2024-12-05 03:55:51 | 微信支付分 > API列表 |
| 314 | [退款结果通知](pages/4012587976.md) | `4012587976` | 2024-12-10 09:27:50 | 微信支付分 > API列表 |
| 315 | [JSAPI调起支付分订单详情页](pages/4012587983.md) | `4012587983` | 2024-11-14 08:11:51 | 微信支付分 > API列表 |
| 316 | [Android](pages/4012587909.md) | `4012587909` | 2024-11-14 08:12:02 | 微信支付分 > API列表 > APP调起支付分确认订单页 |
| 317 | [iOS](pages/4012596359.md) | `4012596359` | 2024-11-14 08:12:00 | 微信支付分 > API列表 > APP调起支付分确认订单页 |
| 318 | [鸿蒙](pages/4015271805.md) | `4015271805` | 2025-06-18 07:09:37 | 微信支付分 > API列表 > APP调起支付分确认订单页 |
| 319 | [wx.openBusinessView](pages/4012587949.md) | `4012587949` | 2025-03-05 03:45:12 | 微信支付分 > API列表 > 小程序调起支付分确认订单页 |
| 320 | [wx.navigateToMiniProgram（停止新增）](pages/4012596395.md) | `4012596395` | 2025-03-05 03:45:33 | 微信支付分 > API列表 > 小程序调起支付分确认订单页 |
| 321 | [Android](pages/4012587980.md) | `4012587980` | 2024-11-14 08:11:56 | 微信支付分 > API列表 > APP调起支付分订单详情页 |
| 322 | [iOS](pages/4012596423.md) | `4012596423` | 2024-11-14 08:11:55 | 微信支付分 > API列表 > APP调起支付分订单详情页 |
| 323 | [鸿蒙](pages/4015271812.md) | `4015271812` | 2025-06-18 07:09:34 | 微信支付分 > API列表 > APP调起支付分订单详情页 |
| 324 | [wx.openBusinessView](pages/4012587984.md) | `4012587984` | 2024-11-14 08:11:54 | 微信支付分 > API列表 > 小程序调起支付分订单详情页 |
| 325 | [wx.navigateToMiniProgram（停止新增）](pages/4012596449.md) | `4012596449` | 2024-11-14 08:11:53 | 微信支付分 > API列表 > 小程序调起支付分订单详情页 |
| 326 | [支付分合作品牌线上应用规范](pages/4012587220.md) | `4012587220` | 2025-03-21 07:48:14 | 微信支付分 > 附录 |
| 327 | [支付分权限申请邮件模板](pages/4012587233.md) | `4012587233` | 2024-09-25 02:00:56 | 微信支付分 > 附录 |
| 328 | [测试微信号配置指引](pages/4012587248.md) | `4012587248` | 2024-10-10 07:51:05 | 微信支付分 > 附录 |
| 329 | [微信支付分权限类问题排查指南](pages/4018398339.md) | `4018398339` | 2026-03-09 09:24:11 | 微信支付分 > 附录 |
| 330 | [二轮电动车充电桩](pages/4012587259.md) | `4012587259` | 2024-12-09 09:50:39 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 331 | [充电宝](pages/4012587281.md) | `4012587281` | 2024-12-09 09:50:36 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 332 | [共享单车](pages/4012587294.md) | `4012587294` | 2024-12-09 09:50:33 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 333 | [快递行业](pages/4012587304.md) | `4012587304` | 2024-12-09 09:50:31 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 334 | [智慧零售(无人设备)](pages/4012587317.md) | `4012587317` | 2026-08-20 10:20:23 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 335 | [汽车充电桩](pages/4012587347.md) | `4012587347` | 2024-12-09 10:14:12 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 336 | [汽车租赁](pages/4012587354.md) | `4012587354` | 2024-12-09 09:50:24 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 337 | [酒店行业](pages/4012587370.md) | `4012587370` | 2024-12-09 09:50:22 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 338 | [产品介绍](pages/4012077223.md) | `4012077223` | 2026-06-12 09:46:26 | 微信支付分停车服务 |
| 339 | [开发接入准备](pages/4012077356.md) | `4012077356` | 2026-06-12 09:46:10 | 微信支付分停车服务 |
| 340 | [开发指引](pages/4012077649.md) | `4012077649` | 2026-10-19 08:12:24 | 微信支付分停车服务 |
| 341 | [常见问题](pages/4016183517.md) | `4016183517` | 2025-12-12 02:17:07 | 微信支付分停车服务 |
| 342 | [创建停车入场](pages/4012533937.md) | `4012533937` | 2025-02-21 08:25:25 | 微信支付分停车服务 > API列表 > 停车入场 |
| 343 | [停车入场状态变更通知](pages/4012284177.md) | `4012284177` | 2025-02-20 06:14:47 | 微信支付分停车服务 > API列表 > 停车入场 |
| 344 | [查询车牌服务开通信息](pages/4012534043.md) | `4012534043` | 2025-02-21 08:24:47 | 微信支付分停车服务 > API列表 > 服务 |
| 345 | [小程序调起支付分停车服务开通页](pages/4012284186.md) | `4012284186` | 2025-01-14 03:08:49 | 微信支付分停车服务 > API列表 > 服务 |
| 346 | [H5调起微信支付分停车服务开通页](pages/4012284235.md) | `4012284235` | 2024-09-19 07:11:40 | 微信支付分停车服务 > API列表 > 服务 |
| 347 | [App拉起微信支付分停车服务开通页](pages/4012284257.md) | `4012284257` | 2024-09-19 07:11:40 | 微信支付分停车服务 > API列表 > 服务 |
| 348 | [查询订单](pages/4012534308.md) | `4012534308` | 2025-02-21 08:27:22 | 微信支付分停车服务 > API列表 > 扣费受理 |
| 349 | [扣费受理](pages/4012534352.md) | `4012534352` | 2025-03-11 03:04:13 | 微信支付分停车服务 > API列表 > 扣费受理 |
| 350 | [订单支付结果通知](pages/4012284311.md) | `4012284311` | 2025-02-19 03:53:52 | 微信支付分停车服务 > API列表 > 扣费受理 |
| 351 | [微信垫资还款](pages/4012284369.md) | `4012284369` | 2024-08-14 07:16:13 | 微信支付分停车服务 > API列表 > 还款 |
| 352 | [退款申请](pages/4012557131.md) | `4012557131` | 2025-01-09 03:18:26 | 微信支付分停车服务 > API列表 > 退款 |
| 353 | [退款结果通知](pages/4012083103.md) | `4012083103` | 2025-02-19 03:54:15 | 微信支付分停车服务 > API列表 > 退款 |
| 354 | [查询单笔退款（通过商户退款单号）](pages/4012557161.md) | `4012557161` | 2025-01-09 03:19:47 | 微信支付分停车服务 > API列表 > 退款 |
| 355 | [现金红包（V2）](pages/4012647471.md) | `4012647471` | 2025-04-25 08:11:06 | 现金红包（V2） |
| 356 | [产品介绍](pages/4012084079.md) | `4012084079` | 2025-10-14 07:17:46 | 代金券 |
| 357 | [开发接入准备](pages/4012084133.md) | `4012084133` | 2026-05-19 08:07:01 | 代金券 |
| 358 | [开发指引](pages/4012084207.md) | `4012084207` | 2026-06-09 07:59:04 | 代金券 |
| 359 | [常见问题](pages/4015880636.md) | `4015880636` | 2025-10-14 06:41:01 | 代金券 |
| 360 | [业务示例代码](pages/4015894256.md) | `4015894256` | 2026-05-19 08:07:01 | 代金券 |
| 361 | [核销事件回调通知](pages/4012285250.md) | `4012285250` | 2025-02-19 03:51:54 | 代金券 > API列表 |
| 362 | [图片上传（营销专用）](pages/4012557233.md) | `4012557233` | 2024-09-14 09:09:45 | 代金券 > API列表 |
| 363 | [创建代金券批次](pages/4012534633.md) | `4012534633` | 2024-10-31 03:59:23 | 代金券 > API列表 > 批次 |
| 364 | [激活代金券批次](pages/4012460137.md) | `4012460137` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 365 | [暂停代金券批次](pages/4012460305.md) | `4012460305` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 366 | [重启代金券批次](pages/4012460411.md) | `4012460411` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 367 | [条件查询批次列表](pages/4012460489.md) | `4012460489` | 2025-03-25 08:44:54 | 代金券 > API列表 > 批次 |
| 368 | [查询批次详情](pages/4012460564.md) | `4012460564` | 2025-03-25 08:44:53 | 代金券 > API列表 > 批次 |
| 369 | [查询代金券可用商户](pages/4012463358.md) | `4012463358` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 370 | [查询代金券可用单品](pages/4012463442.md) | `4012463442` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 371 | [下载批次退款明细](pages/4012463523.md) | `4012463523` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 372 | [下载批次核销明细](pages/4012463585.md) | `4012463585` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 373 | [根据商户号查用户的券](pages/4012534690.md) | `4012534690` | 2024-09-19 13:18:56 | 代金券 > API列表 > 券 |
| 374 | [发放指定批次的代金券](pages/4012463767.md) | `4012463767` | 2024-09-19 13:18:56 | 代金券 > API列表 > 券 |
| 375 | [查询代金券详情](pages/4012486942.md) | `4012486942` | 2024-09-19 13:18:56 | 代金券 > API列表 > 券 |
| 376 | [查询代金券消息通知地址](pages/4012464070.md) | `4012464070` | 2026-10-14 10:37:23 | 代金券 > API列表 > 消息通知地址 |
| 377 | [设置代金券消息通知地址](pages/4012464198.md) | `4012464198` | 2026-10-14 10:37:09 | 代金券 > API列表 > 消息通知地址 |
| 378 | [产品介绍](pages/4012063104.md) | `4012063104` | 2024-07-23 07:30:20 | 委托营销 |
| 379 | [开发接入准备](pages/4012063130.md) | `4012063130` | 2026-05-19 08:10:42 | 委托营销 |
| 380 | [开发指引](pages/4012063233.md) | `4012063233` | 2026-10-19 08:26:15 | 委托营销 |
| 381 | [建立合作关系](pages/4012380498.md) | `4012380498` | 2024-08-26 03:01:30 | 委托营销 > API列表 |
| 382 | [查询合作关系列表](pages/4012380536.md) | `4012380536` | 2024-09-02 03:15:51 | 委托营销 > API列表 |
| 383 | [产品介绍](pages/4012064295.md) | `4012064295` | 2025-11-11 11:19:33 | 支付有礼 |
| 384 | [开发接入准备](pages/4012064330.md) | `4012064330` | 2026-05-19 08:10:58 | 支付有礼 |
| 385 | [开发指引](pages/4012064366.md) | `4012064366` | 2026-06-09 07:59:01 | 支付有礼 |
| 386 | [图片上传（营销专用）](pages/4012557248.md) | `4012557248` | 2024-09-20 02:59:58 | 支付有礼 > API列表 |
| 387 | [创建全场满额送活动](pages/4012487898.md) | `4012487898` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 388 | [获取活动详情接口](pages/4012487971.md) | `4012487971` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 389 | [获取活动发券商户号](pages/4012466149.md) | `4012466149` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 390 | [获取活动指定商品列表](pages/4012466448.md) | `4012466448` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 391 | [终止活动](pages/4012466523.md) | `4012466523` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 392 | [新增活动发券商户号](pages/4012466671.md) | `4012466671` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 393 | [获取支付有礼活动列表](pages/4012489126.md) | `4012489126` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 394 | [删除活动发券商户号](pages/4012466787.md) | `4012466787` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 395 | [产品介绍](pages/4012064617.md) | `4012064617` | 2025-03-21 10:25:03 | 小程序发券插件 |
| 396 | [开发接入准备](pages/4012064734.md) | `4012064734` | 2026-05-19 08:11:14 | 小程序发券插件 |
| 397 | [小程序发券插件](pages/4012285674.md) | `4012285674` | 2025-02-19 02:33:35 | 小程序发券插件 > API列表 |
| 398 | [产品介绍](pages/4012067873.md) | `4012067873` | 2025-03-21 07:44:35 | H5发券 |
| 399 | [开发接入准备](pages/4012067883.md) | `4012067883` | 2026-05-19 08:11:29 | H5发券 |
| 400 | [H5发券](pages/4012285783.md) | `4012285783` | 2025-03-21 07:38:14 | H5发券 > API列表 |
| 401 | [产品介绍](pages/4012068030.md) | `4012068030` | 2025-03-21 07:44:27 | 智慧商圈 |
| 402 | [开发接入准备](pages/4012068068.md) | `4012068068` | 2026-07-06 03:47:46 | 智慧商圈 |
| 403 | [开发指引](pages/4012068086.md) | `4012068086` | 2026-06-09 07:59:00 | 智慧商圈 |
| 404 | [常见问题](pages/4016111728.md) | `4016111728` | 2026-08-07 08:09:07 | 智慧商圈 |
| 405 | [商圈会员积分服务授权结果通知](pages/4012285836.md) | `4012285836` | 2025-02-19 03:56:03 | 智慧商圈 > API列表 |
| 406 | [商圈会员场内支付结果通知](pages/4012285856.md) | `4012285856` | 2025-02-19 03:56:03 | 智慧商圈 > API列表 |
| 407 | [商圈会员积分同步](pages/4012534698.md) | `4012534698` | 2024-09-20 09:22:16 | 智慧商圈 > API列表 |
| 408 | [商圈会员场内退款结果通知](pages/4012285869.md) | `4012285869` | 2025-02-19 03:56:03 | 智慧商圈 > API列表 |
| 409 | [商圈会员积分服务授权查询](pages/4012534848.md) | `4012534848` | 2024-09-20 09:22:16 | 智慧商圈 > API列表 |
| 410 | [商圈会员待积分状态查询](pages/4012534994.md) | `4012534994` | 2024-11-27 07:20:28 | 智慧商圈 > API列表 |
| 411 | [商圈会员停车状态同步](pages/4012535502.md) | `4012535502` | 2024-11-27 07:19:43 | 智慧商圈 > API列表 |
| 412 | [产品介绍](pages/4012061135.md) | `4012061135` | 2026-10-22 12:18:29 | 支付即服务 |
| 413 | [开发接入准备](pages/4012061536.md) | `4012061536` | 2026-05-19 08:12:18 | 支付即服务 |
| 414 | [开发指引](pages/4012062997.md) | `4012062997` | 2026-06-09 07:58:58 | 支付即服务 |
| 415 | [常见问题](pages/4016913581.md) | `4016913581` | 2025-12-19 02:14:30 | 支付即服务 |
| 416 | [服务人员查询](pages/4012535123.md) | `4012535123` | 2025-01-08 09:32:31 | 支付即服务 > API列表 |
| 417 | [服务人员注册](pages/4012535138.md) | `4012535138` | 2025-01-09 03:10:17 | 支付即服务 > API列表 |
| 418 | [服务人员更新](pages/4012535160.md) | `4012535160` | 2025-01-09 03:10:19 | 支付即服务 > API列表 |
| 419 | [服务人员分配](pages/4012535161.md) | `4012535161` | 2024-09-20 11:27:00 | 支付即服务 > API列表 |
| 420 | [服务人员称谓申请指引](pages/4012064662.md) | `4012064662` | 2024-07-22 09:19:24 | 支付即服务 > 附录 |
| 421 | [免开发版本操作指引](pages/4012064678.md) | `4012064678` | 2024-09-20 11:37:23 | 支付即服务 > 附录 |
| 422 | [个人微信服务人员注册](pages/4012064695.md) | `4012064695` | 2024-08-01 08:27:41 | 支付即服务 > 附录 |
| 423 | [清关报关（V2）](pages/4012647500.md) | `4012647500` | 2025-04-25 07:53:32 | 清关报关（V2） |
| 424 | [产品介绍](pages/4012068466.md) | `4012068466` | 2025-08-25 10:00:06 | 消费者投诉2.0 |
| 425 | [开发接入准备](pages/4012068478.md) | `4012068478` | 2026-05-19 08:33:15 | 消费者投诉2.0 |
| 426 | [开发指引](pages/4012068499.md) | `4012068499` | 2026-10-20 03:51:02 | 消费者投诉2.0 |
| 427 | [业务示例代码](pages/4015821404.md) | `4015821404` | 2026-10-21 08:12:12 | 消费者投诉2.0 |
| 428 | [常见问题](pages/4016111664.md) | `4016111664` | 2026-05-19 07:42:36 | 消费者投诉2.0 |
| 429 | [查询投诉单列表](pages/4012533431.md) | `4012533431` | 2025-08-28 02:44:02 | 消费者投诉2.0 > API列表 > 主动查询投诉信息 |
| 430 | [查询投诉单详情](pages/4012533436.md) | `4012533436` | 2025-08-28 02:43:38 | 消费者投诉2.0 > API列表 > 主动查询投诉信息 |
| 431 | [查询投诉单协商历史](pages/4012533439.md) | `4012533439` | 2025-08-28 02:43:34 | 消费者投诉2.0 > API列表 > 主动查询投诉信息 |
| 432 | [投诉通知回调](pages/4012289719.md) | `4012289719` | 2025-02-19 03:56:03 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 433 | [创建投诉通知回调地址](pages/4012458679.md) | `4012458679` | 2025-08-28 02:43:18 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 434 | [查询投诉通知回调地址](pages/4012459014.md) | `4012459014` | 2025-08-28 02:43:16 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 435 | [更新投诉通知回调地址](pages/4012459282.md) | `4012459282` | 2025-08-28 02:43:14 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 436 | [删除投诉通知回调地址](pages/4012460452.md) | `4012460452` | 2025-08-28 02:43:11 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 437 | [回复用户](pages/4012467254.md) | `4012467254` | 2025-09-01 02:26:38 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 438 | [反馈处理完成](pages/4012467255.md) | `4012467255` | 2025-09-01 02:25:34 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 439 | [更新退款审批结果](pages/4012467256.md) | `4012467256` | 2025-09-01 02:23:44 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 440 | [回复需要即时服务的投诉单](pages/4017151596.md) | `4017151596` | 2026-01-22 08:02:05 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 441 | [图片上传接口](pages/4012467250.md) | `4012467250` | 2025-09-01 02:11:47 | 消费者投诉2.0 > API列表 > 商户反馈图片 |
| 442 | [图片请求接口](pages/4012467251.md) | `4012467251` | 2025-09-02 02:42:21 | 消费者投诉2.0 > API列表 > 商户反馈图片 |
| 443 | [证书密钥概览](pages/4024350132.md) | `4024350132` | 2026-07-21 04:03:41 | 证书密钥概览 |
| 444 | [产品介绍](pages/4012153196.md) | `4012153196` | 2026-05-20 02:34:36 | 微信支付公钥 |
| 445 | [常见问题](pages/4013038816.md) | `4013038816` | 2025-03-04 07:15:22 | 微信支付公钥 |
| 446 | [商户签名验签／加解密测试](pages/4014551946.md) | `4014551946` | 2025-05-30 07:01:56 | 微信支付公钥 > API列表 |
| 447 | [回调接口](pages/4015164042.md) | `4015164042` | 2026-04-10 08:15:52 | 微信支付公钥 > API列表 |
| 448 | [如何从平台证书切换成微信支付公钥](pages/4012154180.md) | `4012154180` | 2024-12-12 02:59:29 | 微信支付公钥 > 附录 |
| 449 | [如何从微信支付公钥切换成平台证书](pages/4015419357.md) | `4015419357` | 2026-03-17 09:45:41 | 微信支付公钥 > 附录 |
| 450 | [产品介绍](pages/4012068814.md) | `4012068814` | 2026-05-20 03:19:57 | 平台证书 |
| 451 | [常见问题](pages/4012069411.md) | `4012069411` | 2024-11-29 09:45:35 | 平台证书 |
| 452 | [下载平台证书](pages/4012551764.md) | `4012551764` | 2024-09-13 06:16:54 | 平台证书 > API列表 |
| 453 | [平台证书更换操作指引](pages/4012068829.md) | `4012068829` | 2024-12-04 06:35:09 | 平台证书 > 附录 |
| 454 | [APIv3概述](pages/4012081606.md) | `4012081606` | 2024-11-21 08:19:57 | Optional > 开发须知 |
| 455 | [总述-APIv3如何签名和验签](pages/4012365342.md) | `4012365342` | 2024-11-21 10:51:22 | Optional > 开发须知 |
| 456 | [基本规则](pages/4012081709.md) | `4012081709` | 2024-07-25 02:05:20 | Optional > 开发须知 > 接口规则说明 |
| 457 | [HTTP状态码](pages/4012081717.md) | `4012081717` | 2024-07-25 02:05:20 | Optional > 开发须知 > 接口规则说明 |
| 458 | [开发必要参数说明](pages/4013070756.md) | `4013070756` | 2026-10-13 03:44:45 | Optional > 开发须知 > 开发参数申请和配置 |
| 459 | [mchid与appid申请](pages/4012071573.md) | `4012071573` | 2025-10-28 02:58:17 | Optional > 开发须知 > 开发参数申请和配置 |
| 460 | [管理商户号绑定的APPID账号](pages/4016328613.md) | `4016328613` | 2025-10-28 02:58:17 | Optional > 开发须知 > 开发参数申请和配置 |
| 461 | [管理经营场景](pages/4017312501.md) | `4017312501` | 2026-02-05 08:34:20 | Optional > 开发须知 > 开发参数申请和配置 |
| 462 | [配置APIv3密钥](pages/4012072195.md) | `4012072195` | 2025-10-28 02:58:17 | Optional > 开发须知 > 开发参数申请和配置 |
| 463 | [配置技术负责人账号指引](pages/4015423618.md) | `4015423618` | 2025-08-07 07:33:12 | Optional > 开发须知 > 开发参数申请和配置 |
| 464 | [员工权限管理](pages/4013071427.md) | `4013071427` | 2025-09-19 01:36:09 | Optional > 开发须知 > 开发参数申请和配置 |
| 465 | [申请商户API证书](pages/4012072428.md) | `4012072428` | 2025-10-28 02:59:06 | Optional > 开发须知 > 开发参数申请和配置 > 商户API证书管理 |
| 466 | [如何更换商户API证书？](pages/4013053057.md) | `4013053057` | 2024-11-19 10:01:05 | Optional > 开发须知 > 开发参数申请和配置 > 商户API证书管理 |
| 467 | [请求参数里带Path参数（路径参数），如何计算签名](pages/4012365334.md) | `4012365334` | 2025-02-18 08:09:32 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 468 | [请求参数里带Body参数(包体参数），如何计算签名](pages/4012365336.md) | `4012365336` | 2025-02-18 09:53:43 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 469 | [请求参数里有Query（查询参数），如何计算签名](pages/4012365337.md) | `4012365337` | 2025-02-18 09:53:41 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 470 | [图片上传接口，如何计算签名](pages/4012365335.md) | `4012365335` | 2025-03-25 03:03:49 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 471 | [APP调起支付签名](pages/4012365340.md) | `4012365340` | 2025-03-26 09:28:08 | Optional > 开发须知 > 如何签名 > 如何构造调起支付签名 |
| 472 | [JSAPI调起支付签名](pages/4012365339.md) | `4012365339` | 2025-03-26 09:28:07 | Optional > 开发须知 > 如何签名 > 如何构造调起支付签名 |
| 473 | [小程序调起支付签名](pages/4012365341.md) | `4012365341` | 2025-03-26 09:28:05 | Optional > 开发须知 > 如何签名 > 如何构造调起支付签名 |
| 474 | [如何使用微信支付公钥验签](pages/4013053249.md) | `4013053249` | 2024-11-20 06:55:05 | Optional > 开发须知 > 如何验签 |
| 475 | [如何使用平台证书验签名](pages/4013053420.md) | `4013053420` | 2024-11-29 09:43:48 | Optional > 开发须知 > 如何验签 > 如何使用平台证书验签 |
| 476 | [如何使用签名/验签工具](pages/4012365352.md) | `4012365352` | 2024-12-27 04:05:13 | Optional > 开发须知 > 如何验签 > 如何使用平台证书验签 |
| 477 | [如何使用微信支付公钥加密敏感字段](pages/4013053257.md) | `4013053257` | 2025-03-19 08:49:11 | Optional > 开发须知 > 如何加解密敏感字段 |
| 478 | [如何使用平台证书加密敏感字段](pages/4013053264.md) | `4013053264` | 2025-03-19 08:49:03 | Optional > 开发须知 > 如何加解密敏感字段 |
| 479 | [如何使用API证书解密敏感字段](pages/4013053265.md) | `4013053265` | 2024-11-19 09:06:37 | Optional > 开发须知 > 如何加解密敏感字段 |
| 480 | [如何解密回调报文和平台证书](pages/4012071382.md) | `4012071382` | 2024-11-29 08:23:04 | Optional > 开发须知 > 如何解密微信支付回调报文 |
| 481 | [报错：HTTP header缺少微信支付平台证书序列号(Wechatpay-Serial)](pages/4012365346.md) | `4012365346` | 2024-11-19 09:07:14 | Optional > 开发须知 > 常见问题 |
| 482 | [报错：“Http头Authorization值格式错误，请参考《微信支付商户REST API签名规则》”或者“Authorization不合法”](pages/4012365344.md) | `4012365344` | 2026-01-23 03:32:09 | Optional > 开发须知 > 常见问题 |
| 483 | [报错：商户证书序列号有误。请使用签名私钥匹配的证书序列号](pages/4012365345.md) | `4012365345` | 2024-12-12 03:12:16 | Optional > 开发须知 > 常见问题 |
| 484 | [报错：状态码401或者“错误的签名，验签失败”或者“签名错误，请检查后再试”](pages/4012365347.md) | `4012365347` | 2024-12-12 03:12:14 | Optional > 开发须知 > 常见问题 |
| 485 | [调起支付报错：支付验证签名失败](pages/4012365348.md) | `4012365348` | 2025-03-26 09:28:04 | Optional > 开发须知 > 常见问题 |
| 486 | [使用Java加载密钥时，抛出异常InvalidKeyException: Illegal key size](pages/4013053271.md) | `4013053271` | 2024-11-19 09:29:40 | Optional > 开发须知 > 常见问题 |
| 487 | [使用Java解密时，抛出异常AEADBadTagException: Tag mismatch](pages/4013053274.md) | `4013053274` | 2024-11-19 09:29:40 | Optional > 开发须知 > 常见问题 |
| 488 | [请求返回{"code":"PARAM_ERROR","message":"平台证书序列号Wechatpay-Serial错误"}](pages/4013053279.md) | `4013053279` | 2024-11-19 09:29:40 | Optional > 开发须知 > 常见问题 |
| 489 | [为什么微信支付的回调缺少签名的几个HTTP头？](pages/4013053283.md) | `4013053283` | 2024-11-19 09:29:40 | Optional > 开发须知 > 常见问题 |
| 490 | [如何在程序中加载商户API证书私钥](pages/4013053290.md) | `4013053290` | 2025-12-25 06:37:14 | Optional > 开发须知 > 常见问题 |
| 491 | [为什么请求返回401 Unauthorized？](pages/4012072670.md) | `4012072670` | 2024-11-25 08:53:00 | Optional > 开发须知 > 常见问题 |
| 492 | [验证微信支付响应的签名报错：签名验证失败](pages/4016241880.md) | `4016241880` | 2025-10-14 06:40:19 | Optional > 开发须知 > 常见问题 |
| 493 | [调用接口报错：“平台私钥解密失败”](pages/4016913151.md) | `4016913151` | 2025-12-19 02:59:35 | Optional > 开发须知 > 常见问题 |
| 494 | [跨城冗灾升级指引](pages/4012075113.md) | `4012075113` | 2025-03-21 07:37:49 | Optional > 最佳实践 |
| 495 | [支付回调和查单实现指引](pages/4012075249.md) | `4012075249` | 2024-12-18 07:43:24 | Optional > 最佳实践 |
| 496 | [专线商户Notify升级指引](pages/4012075393.md) | `4012075393` | 2024-07-25 03:02:50 | Optional > 最佳实践 |
| 497 | [回调通知注意事项](pages/4012075420.md) | `4012075420` | 2024-07-25 03:03:09 | Optional > 最佳实践 |
| 498 | [最佳安全实践](pages/4012073699.md) | `4012073699` | 2024-11-27 09:15:00 | Optional > 最佳实践 > API安全最佳实践 |
| 499 | [安全漏洞checklist](pages/4012578686.md) | `4012578686` | 2024-11-27 09:14:55 | Optional > 最佳实践 > API安全最佳实践 |
| 500 | [系统漏洞检测及修复](pages/4012575013.md) | `4012575013` | 2025-03-21 07:40:38 | Optional > 最佳实践 > API安全最佳实践 |
| 501 | [Web漏洞检测及修复](pages/4012575097.md) | `4012575097` | 2025-03-21 08:53:52 | Optional > 最佳实践 > API安全最佳实践 |
| 502 | [最新安全漏洞及修复](pages/4012575124.md) | `4012575124` | 2024-11-27 09:14:37 | Optional > 最佳实践 > API安全最佳实践 |
| 503 | [密钥泄漏修复指引](pages/4012073693.md) | `4012073693` | 2024-12-24 01:54:34 | Optional > 最佳实践 > API安全最佳实践 |
| 504 | [国家商用密码简介](pages/4012075987.md) | `4012075987` | 2024-07-25 03:08:24 | Optional > 国家商用密码接入指南 |
| 505 | [获取国家商用密码证书和密钥](pages/4012076002.md) | `4012076002` | 2024-07-25 03:08:45 | Optional > 国家商用密码接入指南 |
| 506 | [APIv3接口使用国家商用密码指引](pages/4012076194.md) | `4012076194` | 2024-07-25 03:09:16 | Optional > 国家商用密码接入指南 |
| 507 | [开户银行全称对照表](pages/4012076270.md) | `4012076270` | 2024-07-25 03:13:45 | Optional > 对照表 |
| 508 | [开户银行对照表](pages/4012076294.md) | `4012076294` | 2025-02-19 07:30:19 | Optional > 对照表 |
| 509 | [银行类型对照表](pages/4012076355.md) | `4012076355` | 2024-07-25 03:20:22 | Optional > 对照表 |
| 510 | [省市区编号对照表](pages/4012076371.md) | `4012076371` | 2024-07-25 03:20:53 | Optional > 对照表 |
| 511 | [优惠费率活动对照表](pages/4012076387.md) | `4012076387` | 2024-12-26 08:48:22 | Optional > 对照表 |
| 512 | [跨境电商二级商户费率对照表](pages/4012076403.md) | `4012076403` | 2024-07-25 03:21:53 | Optional > 对照表 |
| 513 | [商户行业编码](pages/4012076423.md) | `4012076423` | 2024-07-25 03:22:26 | Optional > 对照表 |
| 514 | [特殊行业ID对照表](pages/4012076444.md) | `4012076444` | 2024-07-25 03:22:48 | Optional > 对照表 |
| 515 | [接入模式](pages/4012068443.md) | `4012068443` | 2026-06-01 06:16:12 | Optional > 名词表 |
| 516 | [支付产品](pages/4012068590.md) | `4012068590` | 2024-07-25 02:21:10 | Optional > 名词表 |
| 517 | [业务平台](pages/4012068615.md) | `4012068615` | 2024-07-25 02:22:14 | Optional > 名词表 |
| 518 | [业务系统](pages/4012068672.md) | `4012068672` | 2024-07-25 02:22:32 | Optional > 名词表 |
| 519 | [参数说明](pages/4012068676.md) | `4012068676` | 2026-10-12 13:11:22 | Optional > 名词表 |
| 520 | [常见问题](pages/4016179629.md) | `4016179629` | 2026-08-05 06:14:22 | Optional > 名词表 |
| 521 | [交易投诉运营规范](pages/4012587539.md) | `4012587539` | 2024-09-23 06:56:32 | Optional > 服务运营规范 |
| 522 | [微信支付链路界面与交互规范](pages/4020527461.md) | `4020527461` | 2026-05-19 02:15:33 | Optional > 服务运营规范 |
| 523 | [验签工具](pages/4012076525.md) | `4012076525` | 2025-01-03 07:02:48 | Optional > 开发工具 |
| 524 | [平台证书下载工具](pages/4012076524.md) | `4012076524` | 2024-11-27 09:13:57 | Optional > 开发工具 |
| 525 | [Postman调试工具](pages/4012076519.md) | `4012076519` | 2024-11-29 09:45:15 | Optional > 开发工具 |
| 526 | [产品介绍](pages/4012076542.md) | `4012076542` | 2025-03-21 07:39:41 | Optional > 网络云排查 |
| 527 | [网络问题排查指南](pages/4012076543.md) | `4012076543` | 2025-03-21 07:39:03 | Optional > 网络云排查 |
| 528 | [常见问题](pages/4012076544.md) | `4012076544` | 2024-07-25 03:40:39 | Optional > 网络云排查 |
| 529 | [产品介绍](pages/4012076556.md) | `4012076556` | 2024-07-25 03:42:19 | Optional > 安全医生 |
| 530 | [诊断链接绑定指引](pages/4012076558.md) | `4012076558` | 2024-07-25 03:42:41 | Optional > 安全医生 |
| 531 | [安全联系人设置指引](pages/4012076563.md) | `4012076563` | 2024-07-25 03:43:12 | Optional > 安全医生 |
| 532 | [SDK概述](pages/4012076498.md) | `4012076498` | 2026-04-24 09:15:35 | Optional > SDK |
| 533 | [使用 Java SDK](pages/4012076506.md) | `4012076506` | 2025-05-29 03:32:15 | Optional > SDK |
| 534 | [使用 PHP SDK](pages/4012076511.md) | `4012076511` | 2025-05-29 03:32:09 | Optional > SDK |
| 535 | [使用 Go SDK](pages/4012076515.md) | `4012076515` | 2025-05-29 03:37:00 | Optional > SDK |

</details>