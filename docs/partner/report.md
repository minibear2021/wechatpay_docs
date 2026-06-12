# 微信支付文档更新报告 - 合作伙伴

**文档类型**: 合作伙伴 (partner)
**生成时间**: 20260612_014557
**文档总数**: 862
**数据来源**: https://pay.weixin.qq.com/doc/v3/partner/llms.txt

## 变更概览

- 新增: 0 个页面
- 删除: 0 个页面
- 修改: 53 个页面
- 成功拉取: 52 个页面
- 拉取失败: 1 个页面
- llms.txt 变更: 是

## llms.txt 变更

```diff
--- llms_old.txt
+++ llms.txt
@@ -1,4 +1,4 @@
->更新时间：2026.06.10
+>更新时间：2026.06.11
 
 # 微信支付合作伙伴平台文档中心
 
```

## 修改页面

### 开发指引
- ID: `4012069859`
- 路径: JSAPI支付
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012069859.md
- 更新时间变更: 2026-02-28 08:04:00 -> 2026-06-09 09:46:17
- 本地文件: `pages/4012069859.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1、开发前准备
 
 ### 1.1、设置安全联系人
@@ -33,7 +35,22 @@
 
 服务商通过调用[JSAPI/小程序下单](https://pay.weixin.qq.com/doc/v3/partner/4012738519.md)接口生成订单并获取预支付ID。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/486298bb5b9520462331b35859ef775a.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户前端页面(微信浏览器打开)
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        User->>Mch: 用户下单
+        Mch->>SP: 发送下单请求
+        SP->>WxPay: 调用JSAPI/小程序下单接口
+        WxPay-->>SP: 下单成功返回prepay_id
+        SP-->>Mch: 返回JSAPI拉起支付所需参数
+    end
+```
 
 下单接口关键参数说明：
 
@@ -63,7 +80,19 @@
 
 服务商调起支付前，请确保已在[服务商平台](https://pay.weixin.qq.com/index.php/partner/public/home)配置好JSAPI支付授权目录（只有[配置了JSAPI支付授权目录](https://pay.weixin.qq.com/doc/v3/partner/4013335127.md)的网页才能调起支付），然后通过调用微信浏览器内置对象方法来调起微信收银台，具体请参考[JSAPI调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012069855.md)
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/4c92e4341ed832f2594b6e80a1ccf738.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户前端页面(微信浏览器打开)
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        Mch->>WxPay: 调用微信浏览器内置对象方法拉起微信收银台
+    end
+```
 
 ### 3.3、用户支付
 
@@ -79,7 +108,40 @@
 
 若因特殊原因需在用户可支付时间范围内关闭订单，服务商可通过调用[查询订单API](https://pay.weixin.qq.com/doc/v3/partner/4012739008.md)接口确认订单状态，若订单仍是未支付状态，服务商可以调用[关闭订单API](https://pay.weixin.qq.com/doc/v3/partner/4012739019.md)接口关单，关单后可以将订单当作失败终态处理。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/798377a60223f6c5e463c4bd42145b8f.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户前端页面(微信浏览器打开)
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        WxPay-->>Mch: 用户返回服务商/子商户前端页面(前端会有回调function)
+        Mch->>SP: 查单确认订单状态
+        SP->>WxPay: 调用微信查单接口
+        WxPay-->>SP: 返回订单状态
+        SP-->>Mch: 返回订单状态
+        Mch-->>User: 根据订单状态展示支付结果
+
+        alt 支付成功
+            WxPay->>SP: 支付成功回调通知
+        end
+
+        alt 未收到支付成功回调
+            SP->>WxPay: 调用微信查单接口轮询查单
+            WxPay-->>SP: 返回订单状态
+
+            alt 超过一定时间查单仍是未支付状态
+                SP->>WxPay: 调用微信关单接口
+                WxPay-->>SP: 返回关单结果
+                SP->>SP: 订单当作失败终态处理
+            end
+
+        end
+    end
+```
 
 ### 3.4、商户对账
 
@@ -91,7 +153,25 @@
 
 ## 4、普通支付订单状态流转图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/b7e0affdfc4e2c2baf71cdc952d33c7b.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "trade_state：NOTPAY（未支付）" as S2
+    state "trade_state：SUCCESS（支付成功）" as S3
+    state "trade_state：REFUND（转入退款）" as S4
+    state "trade_state：CLOSED（已关闭）" as S5
+
+    [*] --> S2: 服务商调用JSAPI/小程序支付下单接口生成订单
+    S2 --> S3: 用户支付成功
+    S2 --> S5: 订单超过7天未支付<br/>微信侧进行自动关单
+    S2 --> S5: 7天内服务商可对未支付的订单调用关闭订单接口
+    S3 --> S4: 调用申请退款接口申请成功<br/>(支付成功后1年内可申请退款)
+    note right of S2 : 用户支付失败<br/>常见支付失败原因有：余额不足、用户风控、支付密码错误、超过服务商设置的最晚支付时间（即下单设置的time_expire）等
+    S3 --> [*]
+    S5 --> [*]
+    S4 --> [*]
+```
 
 1、服务商调用[JSAPI/小程序下单](https://pay.weixin.qq.com/doc/v3/partner/4012738519.md)接口下单成功后，服务商可以调用[查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012739008.md)接口来确认订单状态，详情请参考[支付回调和查单实现指引](https://pay.weixin.qq.com/doc/v3/partner/4012082568.md)。
 
```

### 开发指引
- ID: `4013080246`
- 路径: APP支付
- URL: https://pay.weixin.qq.com/doc/v3/partner/4013080246.md
- 更新时间变更: 2026-01-16 02:06:34 -> 2026-06-09 09:46:14
- 本地文件: `pages/4013080246.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1、开发前准备
 
 ### 1.1、设置安全联系人
@@ -33,7 +35,23 @@
 
 服务商需要通过调用[APP支付下单API](https://pay.weixin.qq.com/doc/v3/partner/4013080231.md)接口下单并获取预支付ID（prepay\_id）。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/8bde7309643bafef0cfcb14dd118dc8e.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户APP端
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        User->>Mch: 用户下单
+        Mch->>SP: 发送下单请求
+        SP->>WxPay: 调用APP支付下单接口
+        WxPay-->>SP: 下单成功返回prepay_id
+        SP-->>Mch: 返回APP拉起支付所需参数
+    end
+```
 
 下单接口关键参数说明：
 
@@ -71,7 +89,19 @@
 </activity>
 ```
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/bc290989f392cc4f6b4ba06f0dc63372.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户APP端
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        Mch->>WxPay: 通过opensdk方法拉起支付
+    end
+```
 
 调起支付关键参数说明：
 
@@ -96,7 +126,40 @@
 
 若因特殊原因需在用户可支付时间范围内关闭订单，服务商可通过调用[查询订单API](https://pay.weixin.qq.com/doc/v3/partner/4013080235.md)接口确认订单状态，若订单仍是未支付状态，服务商可以调用[关闭订单API](https://pay.weixin.qq.com/doc/v3/partner/4013080236.md)接口关单，关单后可以将订单当作失败终态处理。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/1b25218c00946fdb679174c4aeba3d6d.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户APP端
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        WxPay-->>Mch: 用户返回商户APP(opensdk发送onResp回调)
+        Mch->>SP: 查单确认订单状态
+        SP->>WxPay: 调用微信查单接口
+        WxPay-->>SP: 返回订单状态
+        SP-->>Mch: 返回订单状态
+        Mch-->>User: 根据订单状态展示支付结果
+
+        alt 支付成功
+            WxPay->>SP: 支付成功回调通知
+        end
+
+        alt 未收到支付成功回调
+            SP->>WxPay: 调用微信查单接口轮询查单
+            WxPay-->>SP: 返回订单状态
+
+            alt 超过一定时间查单仍是未支付状态
+                SP->>WxPay: 调用微信关单接口
+                WxPay-->>SP: 返回关单结果
+                SP->>SP: 订单当作失败终态处理
+            end
+
+        end
+    end
+```
 
 ### 3.4、商户对账
 
@@ -108,7 +171,25 @@
 
 ## 4、普通支付订单状态流转图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/49b5941c3d37dc9e95c38e25a025a20f.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "trade_state：NOTPAY（未支付）" as S2
+    state "trade_state：SUCCESS（支付成功）" as S3
+    state "trade_state：REFUND（转入退款）" as S4
+    state "trade_state：CLOSED（已关闭）" as S5
+
+    [*] --> S2: 服务商调用APP支付下单接口生成订单
+    S2 --> S3: 用户支付成功
+    S2 --> S5: 订单超过7天未支付<br/>微信侧进行自动关单
+    S2 --> S5: 7天内服务商可对未支付的订单调用关闭订单接口
+    S3 --> S4: 调用申请退款接口申请成功<br/>(支付成功后1年内可申请退款)
+    note right of S2: 用户支付失败<br/>常见支付失败原因有：余额不足、用户风控、支付密码错误、超过服务商设置的最晚支付时间（即下单设置的time_expire）等
+    S3 --> [*]
+    S5 --> [*]
+    S4 --> [*]
+```
 
 1、服务商调用[APP支付下单](https://pay.weixin.qq.com/doc/v3/partner/4013080231.md)接口下单成功后，服务商可以调用[查询订单](https://pay.weixin.qq.com/doc/v3/partner/4013080235.md)接口来确认订单状态，详情请参考[支付回调和查单实现指引](https://pay.weixin.qq.com/doc/v3/partner/4012082568.md)。
 
```

### 开发指引
- ID: `4012074915`
- 路径: H5支付
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012074915.md
- 更新时间变更: 2025-11-20 08:44:46 -> 2026-06-09 09:46:10
- 本地文件: `pages/4012074915.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1、开发前准备
 
 ### 1.1、设置安全联系人
@@ -40,7 +42,53 @@
 
 安全标准规范流程图：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/9c7f39d2d7bd092a91837bd583822f17.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商H5前端
+        participant Mch2 as 服务商后端
+        participant WxPay as 微信支付系统
+
+        User->>Mch: 用户操作下单
+        Mch->>Mch2: 请求下单
+
+        alt 浏览器 preflight 请求
+            Mch->>Mch2: options请求
+
+            note right of Mch: OPTIONS /api HTTP/1.1<br/>Access-control-request-headers: x-A,x-B<br/>Access-control-request-method: POST<br/>Origin: https://api.third.com<br/>Referer: https://api.third.com/
+            Mch2->>Mch2: 判断Origin头部是否合法
+
+            alt 判断Origin头部是否合法(是)
+                Mch2-->>Mch: ：options请求正常响应
+                note right of Mch: HTTP/1.1 200 OK<br/>Access-control-allow-credentials: true<br/>Access-control-allow-headers: x-A,x-B<br/>Access-control-allow-methods: POST, GET<br/>Access-control-allow-origin: https://api.third.com
+            else 否
+                Mch2-->>Mch: ：options请求异常响应
+                note right of Mch: HTTP/1.1 403 Forbidden<br/>（no access-control-allow header）<br/>报错信息
+            end
+
+        end
+
+        Mch->>Mch2: get/post请求
+        note right of Mch: GET /api HTTP/1.1<br/>Host: api.shanghu.com<br/>Referer: https://api.third.com/1/2.html<br/>Origin: https://api.third.com<br/>Cookie: shanghu_uid=xxx:...
+
+        Mch2->>Mch2: 判断Origin头部是否合法
+        Mch2->>Mch2: 判断Cookie是否关联到商户站点已注册用户
+
+        alt api.third.com合法且用户登录态有效(是)
+            Mch2->>Mch2: 保存订单
+            Mch2->>WxPay: 调用微信支付接口下单
+            WxPay-->>Mch2: 返回跳转URL
+            Mch2-->>Mch: ：请求下单正常响应（）
+            note right of Mch: Access-Control-Allow-Origin: https://api.third.com<br/>Access-Control-Allow-Credentials: true
+        else 否
+            Mch2-->>Mch: ：请求下单异常响应
+            note right of Mch: HTTP/1.1 403 Forbidden<br/>（no access-control-allow header）<br/>报错信息
+        end
+
+    end
+```
 
 注意：
 
@@ -63,7 +111,19 @@
 
 服务商调起支付前，请确保已在[服务商平台](https://pay.weixin.qq.com/partner/public/home)配置好H5支付域名，只有[配置了H5支付域名](https://pay.weixin.qq.com/doc/v3/partner/4013336019.md)的网页才能跳转H5支付链接（如需在支付后返回至指定页面，可在h5支付链接后面拼接上redirect\_url参数），[调起微信支付页面](https://pay.weixin.qq.com/doc/v3/partner/4012085683.md)。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/c7a44ecb828688e5883fa2da1e3a27e0.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant SP as 服务商H5前端
+        participant SP2 as 服务商后端
+        participant WxPay as 微信支付系统
+
+        SP->>WxPay: 跳转微信h5支付链接(如需支付完成返回指定页面可拼接redirect_url参数)
+    end
+```
 
 ### 3.3、用户支付
 
@@ -79,7 +139,40 @@
 
 若因特殊原因需在用户可支付时间范围内关闭订单，服务商可通过调用[查询订单API](https://pay.weixin.qq.com/doc/v3/partner/4012759661.md)接口确认订单状态，若订单仍是未支付状态，服务商可以调用[关闭订单API](https://pay.weixin.qq.com/doc/v3/partner/4012759669.md)接口关单，关单后可以将订单当作失败终态处理。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/624811a2da291fedb81ab9eec3b01011.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant SP as 服务商H5前端
+        participant SP2 as 服务商后端
+        participant WxPay as 微信支付系统
+
+        WxPay-->>SP: 用户返回商户拉起支付页面或redirect_url页面
+        SP->>SP2: 查单确认订单状态
+        SP2->>WxPay: 调用微信查单接口
+        WxPay-->>SP2: 返回订单状态
+        SP2-->>SP: 返回订单状态
+        SP-->>User: 根据订单状态展示支付结果
+
+        alt 支付成功
+            WxPay->>SP2: 支付成功回调通知
+        end
+
+        alt 未收到支付成功回调
+            SP2->>WxPay: 调用微信查单接口轮询查单
+            WxPay-->>SP2: 返回订单状态
+
+            alt 超过一定时间查单仍是未支付状态
+                SP2->>WxPay: 调用微信关单接口
+                WxPay-->>SP2: 返回关单结果
+                SP2->>SP2: 订单当作失败终态处理
+            end
+
+        end
+    end
+```
 
 ### 3.4、商户对账
 
@@ -91,7 +184,25 @@
 
 ## 4、普通支付订单状态流转图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/d21d37f4bc65e9010a90e5f71f12001d.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "trade_state：NOTPAY（未支付）" as S2
+    state "trade_state：SUCCESS（支付成功）" as S3
+    state "trade_state：REFUND（转入退款）" as S4
+    state "trade_state：CLOSED（已关闭）" as S5
+
+    [*] --> S2: 服务商调用H5支付下单接口生成订单
+    S2 --> S3: 用户支付成功
+    S2 --> S5: 订单超过7天未支付<br/>微信侧进行自动关单
+    S2 --> S5: 7天内服务商可对未支付的订单调用关闭订单接口
+    S3 --> S4: 调用申请退款接口申请成功<br/>(支付成功后1年内可申请退款)
+    note right of S2 : 用户支付失败<br/>常见支付失败原因有：余额不足、用户风控、支付密码错误、超过服务商设置的最晚支付时间（即下单设置的time_expire）等
+    S3 --> [*]
+    S5 --> [*]
+    S4 --> [*]
+```
 
 1、服务商调用[H5支付下单](https://pay.weixin.qq.com/doc/v3/partner/4012738604.md)接口下单成功后，服务商可以调用[查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012759661.md)接口来确认订单状态，详情请参考[支付回调和查单实现指引](https://pay.weixin.qq.com/doc/v3/partner/4012082568.md)。
 
```

### 开发指引
- ID: `4012076269`
- 路径: Native支付
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012076269.md
- 更新时间变更: 2025-11-20 08:44:29 -> 2026-06-09 09:46:06
- 本地文件: `pages/4012076269.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1、开发前准备
 
 ### 1.1、设置安全联系人
@@ -33,7 +35,23 @@
 
 服务商通过调用[Native支付下单API](https://pay.weixin.qq.com/doc/v3/partner/4012738659.md)接口生成订单并获取二维码链接 `code_url`，随后将该 `code_url` 传递至服务商/子商户前端，由前端将其转换为二维码图片展示给用户。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/169f4305d5a9083d393d79d6fbfa4fee.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户前端
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        User->>Mch: 用户下单
+        Mch->>SP: 发送下单请求
+        SP->>WxPay: 调用Native支付下单接口
+        WxPay-->>SP: 下单成功返回code_url
+        SP-->>Mch: 转换为二维码图片前端展示
+    end
+```
 
 下单接口关键参数说明：
 
@@ -53,7 +71,20 @@
 
 二维码不支持通过相册识别或长按识别二维码的方式完成支付
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/6f15ed042942f2e5e0e0a8d7e7f7e921.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户前端
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        User->>WxPay: 用户打开微信扫一扫
+        WxPay->>Mch: 扫描服务商/子商户前端展示的二维码图片
+        Mch->>WxPay: 拉起微信收银台
+    end
+```
 
 ### 3.3、用户支付
 
@@ -69,7 +100,36 @@
 
 若因特殊原因需在用户可支付时间范围内关闭订单，服务商可通过调用[查询订单API](https://pay.weixin.qq.com/doc/v3/partner/4012759714.md)接口确认订单状态，若订单仍是未支付状态，服务商可以调用[关闭订单API](https://pay.weixin.qq.com/doc/v3/partner/4012759725.md)接口关单，关单后可以将订单当作失败终态处理。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/317534bd595ff8d79808709812131e47.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户前端
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        Mch->>SP: 轮询获取订单状态
+        SP-->>Mch: 返回订单状态
+        Mch->>User: 给用户展示订单支付结果
+
+        alt 支付成功
+            WxPay->>SP: 支付成功回调通知
+        end
+
+        alt 未收到支付成功回调
+            SP->>WxPay: 调用微信查单接口轮询查单
+            WxPay-->>SP: 返回订单状态
+
+            alt 超过一定时间查单仍是未支付状态
+                SP->>WxPay: 调用微信关单接口
+                WxPay-->>SP: 返回关单结果
+                SP->>SP: 订单当作失败终态处理
+            end
+
+        end
+    end
+```
 
 ### 3.4、商户对账
 
@@ -81,7 +141,25 @@
 
 ## 4、普通支付订单状态流转图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/4bc2a222b3c59bf6a46abd0b38dd52a9.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "trade state:NOTPAY (未支付)" as S2
+    state "trade_state:SUCCESS (支付成功)" as S3
+    state "trade state:REFUND (转入退款)" as S4
+    state "trade state:CLOSED (已关闭)" as S5
+
+    [*] --> S2: 服务商调用Native支付下单接口生成订单
+    S2 --> S3: 用户支付成功
+    S2 --> S5: 订单超过7天未支付<br/>微信侧进行自动关单
+    S2 --> S5: 7天内服务商可对未支付的订单调用关闭订单接口
+    S3 --> S4: 调用申请退款接口申请成功<br/>(支付成功后1年内可申请退款)
+    note right of S2 : 用户支付失败<br/>常见支付失败原因有：余额不足、用户风控、支付密码错误、超过服务商设置的最晚支付时间（即下单设置的time_expire）等
+    S3 --> [*]
+    S5 --> [*]
+    S4 --> [*]
+```
 
 1、服务商调用[Native支付下单](https://pay.weixin.qq.com/doc/v3/partner/4012738659.md)接口下单成功后，服务商可以调用[查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012759714.md)接口来确认订单状态，详情请参考[支付回调和查单实现指引](https://pay.weixin.qq.com/doc/v3/partner/4012082568.md)。
 
```

### 开发指引
- ID: `4012076732`
- 路径: 小程序支付
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012076732.md
- 更新时间变更: 2026-02-28 08:05:10 -> 2026-06-09 09:46:05
- 本地文件: `pages/4012076732.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1、开发前准备
 
 ### 1.1、设置安全联系人
@@ -33,7 +35,22 @@
 
 服务商通过调用[JSAPI/小程序下单](https://pay.weixin.qq.com/doc/v3/partner/4012759974.md)接口下单并获取预支付ID（prepay\_id）。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/bdbb11ae01f6671da84f649dad4894cc.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户小程序
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        User->>Mch: 用户下单
+        Mch->>SP: 发送下单请求
+        SP->>WxPay: 调用小程序支付下单接口
+        WxPay-->>SP: 下单成功返回prepay_id
+        SP-->>Mch: 返回小程序拉起支付所需参数
+    end
+```
 
 下单接口关键参数说明：
 
@@ -63,7 +80,18 @@
 
 注意：若为交易类小程序，需要满足公众平台的[《交易类小程序运营规范》](https://developers.weixin.qq.com/miniprogram/product/jiaoyilei/yunyingguifan.html)，若不满足，可能被公众平台限制使用小程序进行支付的权限，无法在正式环境下调起小程序支付。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/29c3c51f4b025ff7bf04b78d3e7b0847.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户小程序
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        Mch->>WxPay: 调用小程序方法拉起微信收银台
+    end
+```
 
 调起支付关键参数说明：
 
@@ -88,7 +116,39 @@
 
 若因特殊原因需在用户可支付时间范围内关闭订单，服务商可通过调用[查询订单API](https://pay.weixin.qq.com/doc/v3/partner/4012760115.md)接口确认订单状态，若订单仍是未支付状态，服务商可以调用[关闭订单API](https://pay.weixin.qq.com/doc/v3/partner/4012760108.md)接口关单，关单后可以将订单当作失败终态处理。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/edf5bc035ed864e8fb28c82cc1ce8865.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户小程序
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        WxPay-->>Mch: 用户返回服务商/子商户小程序小程序会有回调
+        Mch->>SP: 查单确认订单状态
+        SP->>WxPay: 调用微信查单接口
+        WxPay-->>SP: 返回订单状态
+        SP-->>Mch: 返回订单状态
+        Mch-->>User: 根据订单状态展示支付结果
+
+        alt 支付成功
+            WxPay->>SP: 支付成功回调通知
+        end
+
+        alt 未收到支付成功回调
+            SP->>WxPay: 调用微信查单接口轮询查单
+            WxPay-->>SP: 返回订单状态
+
+            alt 超过一定时间查单仍是未支付状态
+                SP->>WxPay: 调用微信关单接口
+                WxPay-->>SP: 返回关单结果
+                SP->>SP: 订单当作失败终态处理
+            end
+
+        end
+    end
+```
 
 ### 3.4、商户对账
 
@@ -100,7 +160,25 @@
 
 ## 4、普通支付订单状态流转图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/4e0f80b94531f6d9e722fe91ae06550b.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "trade_state：NOTPAY（未支付）" as S2
+    state "trade_state：SUCCESS（支付成功）" as S3
+    state "trade_state：REFUND（转入退款）" as S4
+    state "trade_state：CLOSED（已关闭）" as S5
+
+    [*] --> S2: 服务商调用JSAPI/小程序支付下单接口生成订单
+    S2 --> S3: 用户支付成功
+    S2 --> S5: 订单超过7天未支付<br/>微信侧进行自动关单
+    S2 --> S5: 7天内服务商可对未支付的订单调用关闭订单接口
+    S3 --> S4: 调用申请退款接口申请成功<br/>(支付成功后1年内可申请退款)
+    note right of S2 : 用户支付失败<br/>常见支付失败原因有：余额不足、用户风控、支付密码错误、超过服务商设置的最晚支付时间（即下单设置的time_expire）等
+    S3 --> [*]
+    S5 --> [*]
+    S4 --> [*]
+```
 
 1、服务商调用[JSAPI/小程序下单](https://pay.weixin.qq.com/doc/v3/partner/4012759974.md)接口下单成功后，服务商可以调用[查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012760115.md)接口来确认订单状态，详情请参考[支付回调和查单实现指引](https://pay.weixin.qq.com/doc/v3/partner/4012082568.md)。
 
```

### 开发指引
- ID: `4012166834`
- 路径: JSAPI合单支付
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012166834.md
- 更新时间变更: 2025-01-16 06:39:05 -> 2026-06-09 09:46:02
- 本地文件: `pages/4012166834.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 开发指引
- ID: `4012166832`
- 路径: APP合单支付
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012166832.md
- 更新时间变更: 2025-06-20 04:11:39 -> 2026-06-09 09:45:58
- 本地文件: `pages/4012166832.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1、开发前准备
 
 ### 1.1、设置安全联系人
@@ -29,7 +31,22 @@
 
 服务商通过调用[APP合单支付下单API](https://pay.weixin.qq.com/doc/v3/partner/4012758021.md)接口下单并获取预支付ID（prepay\_id）。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/da30741464b82b99ffafcb7e950173bc.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant SP as 服务商APP端
+        participant SP2 as 服务商后端
+        participant WxPay as 微信支付系统
+
+        User->>SP: 用户下单
+        SP->>SP2: 发送下单请求
+        SP2->>WxPay: 调用合单APP支付下单接口
+        WxPay-->>SP2: 下单成功返回prepay_id
+        SP2-->>SP: 返回APP拉起支付所需参数
+    end
+```
 
 下单接口关键参数说明：
 
@@ -53,7 +70,19 @@
 
 服务商调起支付前，需根据不同客户端系统接入对应的OpenSDK（推荐使用最新版本，具体请参考[OpenSDK接入指南](https://pay.weixin.qq.com/doc/v3/partner/4013369798.md)），然后通过opensdk的sendReq方法调起微信支付页面，具体请参考[调起APP合单支付](https://pay.weixin.qq.com/doc/v3/partner/4012166845.md)。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/a7cf24d360c4bf71e252f7bb75ea8a7c.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant SP as 服务商APP端
+        participant SP2 as 服务商后端
+        participant WxPay as 微信支付系统
+
+        SP->>WxPay: 通过opensdk方法拉起支付
+    end
+```
 
 ### 3.3、用户支付
 
@@ -69,7 +98,40 @@
 
 若因特殊原因需在用户可支付时间范围内关闭订单，服务商可通过调用[查询合单订单API](https://pay.weixin.qq.com/doc/v3/partner/4012761057.md)接口确认订单状态（请勿使用非合单支付的查单接口查询合单订单），若订单仍是未支付状态，服务商可以调用[关闭合单订单API](https://pay.weixin.qq.com/doc/v3/partner/4012761079.md)接口关单（关闭整个合单订单，而非关闭单个子单），关单后可以将订单当作失败终态处理。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/0b75b5be7b84ba0dfc83b53f04b1326e.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant SP as 服务商APP端
+        participant SP2 as 服务商后端
+        participant WxPay as 微信支付系统
+
+        WxPay-->>SP: 用户返回商户APP(opensdk发送onResp回调)
+        SP->>SP2: 查单确认订单状态
+        SP2->>WxPay: 调用微信合单支付的查单接口
+        WxPay-->>SP2: 返回订单状态
+        SP2-->>SP: 返回订单状态
+        SP-->>User: 根据订单状态展示支付结果
+
+        alt 支付成功
+            WxPay->>SP2: 支付成功回调通知
+        end
+
+        alt 未收到支付成功回调
+            SP2->>WxPay: 调用微信合单支付查单接口轮询查单
+            WxPay-->>SP2: 返回订单状态
+
+            alt 超过一定时间查单仍是未支付状态
+                SP2->>WxPay: 调用微信合单支付关单接口
+                WxPay-->>SP2: 返回关单结果
+                SP2->>SP2: 订单当作失败终态处理
+            end
+
+        end
+    end
+```
 
 ### 3.4、商户对账
 
@@ -81,7 +143,22 @@
 
 ## 4、合单支付订单状态流转图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/11d3992b5f06103137cb8da432854d0b.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "sub_orders.trade_state: NOTPAY (未支付)" as S2
+    state "sub_orders.trade_state:SUCCESS (支付成功)" as S3
+    state "sub_orders.trade state:CLOSED (已关闭)" as S4
+
+    [*] --> S2: 服务商调用APP合单支付下单接口生成订单
+    S2 --> S3: 用户支付成功
+    S2 --> S4: 7天内服务商可对未支付的订单调用关闭合单订单接口
+    S2 --> S4: 订单超过7天未支付，微信侧进行自动关单
+    S3 --> [*]
+    S4 --> [*]
+    note right of S2: 用户支付失败<br/>常见支付失败原因有：余额不足、用户风控、支付密码错误、超过服务商设置的最晚支付时间(即下单设置的time_expire)等
+```
 
 1、服务商调用[APP合单支付下单](https://pay.weixin.qq.com/doc/v3/partner/4012758021.md)接口下单成功后，服务商可以调用[查询合单订单](https://pay.weixin.qq.com/doc/v3/partner/4012761057.md)接口来确认订单状态，详情请参考[支付回调和查单实现指引](https://pay.weixin.qq.com/doc/v3/partner/4012082568.md)。
 
```

### 开发指引
- ID: `4012166833`
- 路径: H5合单支付
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012166833.md
- 更新时间变更: 2025-01-16 06:39:52 -> 2026-06-09 09:45:46
- 本地文件: `pages/4012166833.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1、开发前准备
 
 ### 1.1、设置安全联系人
@@ -36,7 +38,53 @@
 
 安全标准规范流程图：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/f696cf6d47704340a6b22075e1021f95.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant SP as 服务商H5前端
+        participant SP2 as 服务商后端
+        participant WxPay as 微信支付系统
+
+        User->>SP: 用户操作下单
+        SP->>SP2: 请求下单
+
+        alt 浏览器 preflight 请求
+            SP->>SP2: options请求
+
+            note right of SP: OPTIONS /api HTTP/1.1<br/>Access-control-request-headers: x-A,x-B<br/>Access-control-request-method: POST<br/>Origin: https://api.third.com<br/>Referer: https://api.third.com/
+			SP2->>SP2: 判断Origin头部是否合法
+
+            alt 判断Origin头部是否合法(是)
+                SP2-->>SP: ：options请求正常响应
+                note right of SP: HTTP/1.1 200 OK<br/>Access-control-allow-credentials: true<br/>Access-control-allow-headers: x-A,x-B<br/>Access-control-allow-methods: POST, GET<br/>Access-control-allow-origin: https://api.third.com
+            else 否
+                SP2-->>SP: ：options请求异常响应
+                note right of SP: HTTP/1.1 403 Forbidden<br/>（no access-control-allow header）<br/>报错信息
+            end
+
+        end
+
+        SP->>SP2: get/post请求
+        note right of SP: GET /api HTTP/1.1<br/>Host: api.shanghu.com<br/>Referer: https://api.third.com/1/2.html<br/>Origin: https://api.third.com<br/>Cookie: shanghu_uid=xxx:...
+
+        SP2->>SP2: 判断Origin头部是否合法
+        SP2->>SP2: 判断Cookie是否关联到商户站点已注册用户
+
+        alt api.third.com合法且用户登录态有效(是)
+            SP2->>SP2: 保存订单
+            SP2->>WxPay: 调用微信合单支付接口下单
+            WxPay-->>SP2: 返回跳转URL
+            SP2-->>SP: ：请求下单正常响应（）
+            note right of SP: Access-Control-Allow-Origin: https://api.third.com<br/>Access-Control-Allow-Credentials: true
+        else 否
+            SP2-->>SP: ：请求下单异常响应
+            note right of SP: HTTP/1.1 403 Forbidden<br/>（no access-control-allow header）<br/>报错信息
+        end
+
+    end
+```
 
 注意：
 
@@ -67,7 +115,19 @@
 
 服务商调起支付前，请确保已在[服务商平台](https://pay.weixin.qq.com/index.php/partner/public/home)配置好H5支付域名（只能合单服务商商户号配置，子商户号配置无效），只有[配置了H5支付域名](https://pay.weixin.qq.com/doc/v3/partner/4013336019.md)的网页才能跳转H5支付链接（如需在支付后返回至指定页面，可在h5支付链接后面拼接上redirect\_url参数），调起微信支付页面。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/116c678c951002d485dc908d276d3f9e.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant SP as 服务商H5前端
+        participant SP2 as 服务商后端
+        participant WxPay as 微信支付系统
+
+        SP->>WxPay: 跳转微信h5支付链接(如需支付完成返回指定页面可拼接redirect_url参数)
+    end
+```
 
 ### 3.3、用户支付
 
@@ -83,7 +143,40 @@
 
 若因特殊原因需在用户可支付时间范围内关闭订单，服务商可通过调用[查询合单订单API](https://pay.weixin.qq.com/doc/v3/partner/4013462099.md)接口确认订单状态（请勿使用非合单支付的查单接口查询合单订单），若订单仍是未支付状态，服务商可以调用[关闭合单订单API](https://pay.weixin.qq.com/doc/v3/partner/4013462102.md)接口关单（关闭整个合单订单，而非关闭单个子单），关单后可以将订单当作失败终态处理。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/5fa17ba4e1f73dc31826aa4fea5e8e04.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant SP as 服务商H5前端
+        participant SP2 as 服务商后端
+        participant WxPay as 微信支付系统
+
+        WxPay-->>SP: 用户返回服务商拉起支付页面或redirect_url页面
+        SP->>SP2: 查单确认订单状态
+        SP2->>WxPay: 调用微信合单支付查单接口
+        WxPay-->>SP2: 返回订单状态
+        SP2-->>SP: 返回订单状态
+        SP-->>User: 根据订单状态展示支付结果
+
+        alt 支付成功
+            WxPay->>SP2: 支付成功回调通知
+        end
+
+        alt 未收到支付成功回调
+            SP2->>WxPay: 调用微信合单支付查单接口轮询查单
+            WxPay-->>SP2: 返回订单状态
+
+            alt 超过一定时间查单仍是未支付状态
+                SP2->>WxPay: 调用微信合单支付关单接口
+                WxPay-->>SP2: 返回关单结果
+                SP2->>SP2: 订单当作失败终态处理
+            end
+
+        end
+    end
+```
 
 ### 3.4、商户对账
 
@@ -95,7 +188,22 @@
 
 ## 4、合单支付订单状态流转图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/243d94942b9efdfe98d73f8f7cf8916e.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "sub_orders.trade_state：NOTPAY（未支付）" as S2
+    state "sub_orders.trade_state：SUCCESS（支付成功）" as S3
+    state "sub_orders.trade_state：CLOSED（已关闭）" as S4
+
+    [*] --> S2: 服务商调用H5合单支付下单接口生成订单
+    S2 --> S3: 用户支付成功
+    S2 --> S4: 订单超过7天未支付<br/>微信侧进行自动关单
+    S2 --> S4: 7天内服务商可对未支付的订单调用关闭合单订单接口
+    note right of S2:用户支付失败<br/>常见支付失败原因有：余额不足、用户风控、支付密码错误、超过服务商设置的最晚支付时间（即下单设置的time_expire）等
+    S3 --> [*]
+    S4 --> [*]
+```
 
 1、服务商调用[H5合单支付下单](https://pay.weixin.qq.com/doc/v3/partner/4012758208.md)接口下单成功后，服务商可以调用[查询合单订单](https://pay.weixin.qq.com/doc/v3/partner/4013462099.md)接口来确认订单状态，详情请参考[支付回调和查单实现指引](https://pay.weixin.qq.com/doc/v3/partner/4012082568.md)。
 
```

### 开发指引
- ID: `4012166835`
- 路径: Native合单支付
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012166835.md
- 更新时间变更: 2025-06-20 04:11:35 -> 2026-06-09 09:45:53
- 本地文件: `pages/4012166835.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1、开发前准备
 
 ### 1.1、设置安全联系人
@@ -29,7 +31,23 @@
 
 服务商通过调用[Native合单支付下单API](https://pay.weixin.qq.com/doc/v3/partner/4012758240.md)接口生成订单并获取二维码链接 `code_url`，随后将该 `code_url` 传递至前端，由前端将其转换为二维码图片展示给用户。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/04074044faab3f43dd52c982dd9fba36.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant SP as 服务商前端
+        participant SP2 as 服务商后端
+        participant WxPay as 微信支付系统
+
+        User->>SP: 用户下单
+        SP->>SP2: 发送下单请求
+        SP2->>WxPay: 调用Native合单支付下单接口
+        WxPay-->>SP2: 下单成功返回code_url
+        SP2-->>SP: 转换为二维码图片前端展示
+    end
+```
 
 下单接口关键参数说明：
 
@@ -57,7 +75,21 @@
 
 二维码不支持通过相册识别或长按识别二维码的方式完成支付
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/f2ea2a8e75c42eddb0bf399cc2c767f1.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant SP as 服务商前端
+        participant SP2 as 服务商后端
+        participant WxPay as 微信支付系统
+
+        User->>WxPay: 用户打开微信扫一扫
+        WxPay->>SP: 扫描商户前端展示的二维码图片
+        SP->>WxPay: 拉起微信收银台
+    end
+```
 
 ### 3.3、用户支付
 
@@ -73,7 +105,37 @@
 
 若因特殊原因需在用户可支付时间范围内关闭订单，服务商可通过调用[查询合单订单API](https://pay.weixin.qq.com/doc/v3/partner/4013462240.md)接口确认订单状态（请勿使用非合单支付的查单接口查询合单订单），若订单仍是未支付状态，服务商可以调用[关闭合单订单API](https://pay.weixin.qq.com/doc/v3/partner/4013462247.md)接口关单（关闭整个合单订单，而非关闭单个子单），关单后可以将订单当作失败终态处理。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/2b4e5de491375de806fa55108ca14b55.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant SP as 服务商前端
+        participant SP2 as 服务商后端
+        participant WxPay as 微信支付系统
+
+        SP->>SP2: 轮询获取订单状态
+        SP2-->>SP: 返回订单状态
+        SP->>User: 给用户展示订单支付结果
+
+        alt 支付成功
+            WxPay->>SP2: 支付成功回调通知
+        end
+
+        alt 未收到支付成功回调
+            SP2->>WxPay: 调用查询合单订单接口轮询查单
+            WxPay-->>SP2: 返回订单状态
+
+            alt 超过一定时间查单仍是未支付状态
+                SP2->>WxPay: 调用关闭合单订单接口
+                WxPay-->>SP2: 返回关单结果
+                SP2->>SP2: 订单当作失败终态处理
+            end
+
+        end
+    end
+```
 
 ### 3.4、商户对账
 
@@ -85,7 +147,22 @@
 
 ## 4、合单支付订单状态流转图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/2cb3c27f810f9abb9dacf6f4a49d7724.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "sub_orders.trade_state:NOTPAY (未支付)" as S2
+    state "sub_orders.trade_state:SUCCESS (支付成功)" as S3
+    state "sub_orders.trade_state:CLOSED (已关闭)" as S4
+
+    [*] --> S2: 服务商调用Native合单支付下单接口生成订单
+    S2 --> S3: 用户支付成功
+    S2 --> S4: 7天内服务商可对未支付的订单调用关闭合单订单接口
+    S2 --> S4: 订单超过7天未支付，微信侧进行自动关单
+    note right of S2: 用户支付失败<br/>常见支付失败原因有：余额不足、用户风控、支付密码错误、超过服务商设置的最晚支付时间(即下单设置的time_expire)等
+    S3 --> [*]
+    S4 --> [*]
+```
 
 1、服务商调用[Native合单支付下单](https://pay.weixin.qq.com/doc/v3/partner/4012758240.md)接口下单成功后，服务商可以调用[查询合单订单](https://pay.weixin.qq.com/doc/v3/partner/4013462240.md)接口来确认订单状态，详情请参考[支付回调和查单实现指引](https://pay.weixin.qq.com/doc/v3/partner/4012082568.md)。
 
```

### 开发指引
- ID: `4012166836`
- 路径: 小程序合单支付
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012166836.md
- 更新时间变更: 2025-06-20 04:11:31 -> 2026-06-09 09:45:44
- 本地文件: `pages/4012166836.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1、开发前准备
 
 ### 1.1、设置安全联系人
@@ -29,7 +31,23 @@
 
 服务商通过调用[小程序合单支付下单API](https://pay.weixin.qq.com/doc/v3/partner/4012758246.md)接口生成订单并获取预支付ID（prepay\_id）。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/f806a28841dcdf52d874290451ba02d2.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户小程序
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        User->>Mch: 用户下单
+        Mch->>SP: 发送下单请求
+        SP->>WxPay: 调用小程序合单支付下单接口
+        WxPay-->>SP: 下单成功返回prepay_id
+        SP-->>Mch: 返回小程序拉起支付所需参数
+    end
+```
 
 下单接口关键参数说明：
 
@@ -57,7 +75,19 @@
 
 服务商/子商户小程序通过调用小程序提供的[requestPayment](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestPayment.html)方法来拉起微信收银台，详情参考[小程序调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012166847.md)
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/73737ac678a01d1e3b7588ef58b912c8.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户小程序
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        Mch->>WxPay: 调用小程序方法拉起微信收银台
+    end
+```
 
 调起支付关键参数说明：
 
@@ -82,7 +112,40 @@
 
 若因特殊原因需在用户可支付时间范围内关闭订单，服务商可通过调用[查询合单订单API](https://pay.weixin.qq.com/doc/v3/partner/4013462520.md)接口确认订单状态（请勿使用非合单支付的查单接口查询合单订单），若订单仍是未支付状态，服务商可以调用[关闭合单订单API](https://pay.weixin.qq.com/doc/v3/partner/4013462566.md)接口关单（关闭整个合单订单，而非关闭单个子单），关单后可以将订单当作失败终态处理。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/14b25dabb6c35fddca41644bdb0985c4.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 服务商/子商户小程序
+        participant SP as 服务商后端
+        participant WxPay as 微信支付系统
+
+        WxPay-->>Mch: 用户返回商户小程序会有回调
+        Mch->>SP: 查单确认订单状态
+        SP->>WxPay: 调用查询合单订单接口
+        WxPay-->>SP: 返回订单状态
+        SP-->>Mch: 返回订单状态
+        Mch-->>User: 根据订单状态展示支付结果
+
+        alt 支付成功
+            WxPay->>SP: 支付成功回调通知
+        end
+
+        alt 未收到支付成功回调
+            SP->>WxPay: 调用查询合单订单接口轮询查单
+            WxPay-->>SP: 返回订单状态
+
+            alt 超过一定时间查单仍是未支付状态
+                SP->>WxPay: 调用关闭合单订单接口
+                WxPay-->>SP: 返回关单结果
+                SP->>SP: 订单当作失败终态处理
+            end
+
+        end
+    end
+```
 
 ### 3.4、商户对账
 
@@ -94,7 +157,22 @@
 
 ## 4、合单支付订单状态流转图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/6dd36f917e88db280887441397ad3d26.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "sub_orders.trade_state: NOTPAY (未支付)" as S2
+    state "sub_orders.trade_state:SUCCESS (支付成功)" as S3
+    state "sub_orders.trade_state: CLOSED (已关闭)" as S4
+
+    [*] --> S2: 服务商调用小程序合单支付下单接口生成订单
+    S2 --> S3: 用户支付成功
+    S2 --> S4: 7天内服务商可对未支付的订单调用关闭合单订单接口
+    S2 --> S4: 订单超过7天未支付，微信侧进行自动关单
+    note right of S2: 用户支付失败<br/>常见支付失败原因有：余额不足、用户风控、支付密码错误、超过服务商设置的最晚支付时间(即下单设置的time_expire)等
+    S3 --> [*]
+    S4 --> [*]
+```
 
 1、服务商调用[小程序合单支付下单](https://pay.weixin.qq.com/doc/v3/partner/4012758246.md)接口下单成功后，服务商可以调用[查询合单订单](https://pay.weixin.qq.com/doc/v3/partner/4013462520.md)接口来确认订单状态，详情请参考[支付回调和查单实现指引](https://pay.weixin.qq.com/doc/v3/partner/4012082568.md)。
 
```

### 开发指引
- ID: `4013080623`
- 路径: 订单退款
- URL: https://pay.weixin.qq.com/doc/v3/partner/4013080623.md
- 更新时间变更: 2025-06-20 04:11:27 -> 2026-06-10 07:28:39
- 本地文件: `pages/4013080623.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1、整体业务开发流程概览
 
 若存在退款需求，服务商需先调用[查询订单状态](https://pay.weixin.qq.com/doc/v3/partner/4013080235.md)接口以确认订单支付状态为已支付成功，随后调用[申请退款API](https://pay.weixin.qq.com/doc/v3/partner/4013080625.md)创建退款单后，可通过[查询单笔退款信息](https://pay.weixin.qq.com/doc/v3/partner/4013080626.md)或[退款回调通知](https://pay.weixin.qq.com/doc/v3/partner/4013080628.md)以确认最终的退款结果。若退款状态为退款异常，则需调用[发起异常退款API](https://pay.weixin.qq.com/doc/v3/partner/4013080627.md)进行退款操作。
@@ -10,7 +12,19 @@
 
 服务商在退款之前调用[微信支付订单号查询订单API](https://pay.weixin.qq.com/doc/v3/partner/4013080234.md)或[商户订单号查询订单API](https://pay.weixin.qq.com/doc/v3/partner/4013080235.md)，确认订单支付状态，支付成功才可进行退款。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/e57a54ee56f4e2770eb8e4a2c18a6718.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 商户系统
+        participant WxPay as 微信支付系统
+
+        User->>Mch: 用户申请退款
+        Mch->>WxPay: 查询订单信息
+        WxPay-->>Mch: 获取订单信息
+    end
+```
 
 ### 2.2、申请退款
 
@@ -23,7 +37,21 @@
 - 若支付订单为分账订单，存在分账给其他商户号成功情况，退款不会自动回退分账金额，退款出资为子商户基本账户可用余额。
 
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/80ebdb7cf038ab7c682f054dd6caa471.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 商户系统
+        participant WxPay as 微信支付系统
+
+        User->>Mch: 用户申请退款
+        Mch->>Mch: 生成商户退款单号
+        Mch->>WxPay: 申请退款
+        WxPay->>WxPay: 生成微信支付退款单号
+        WxPay-->>Mch: 返回退款受理信息
+    end
+```
 
 申请退款接口需要注意的参数：
 
@@ -39,7 +67,30 @@
 
 若未收到退款回调通知或服务商希望主动获取退款状态时，可调用 [查询单笔退款（按商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4013080626.md)查询退款单信息，推荐申请退款后间隔1分钟调用该接口轮询一次退款状态，若超过5分钟仍是退款处理中状态，建议开始逐步衰减轮询频率(比如之后间隔5分钟、10分钟、20分钟、30分钟……轮询一次)。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/e954363fe18c1d7f5231692f8e305e08.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant P2 as 微信客户端
+        participant Mch as 商户系统
+        participant WxPay as 微信支付系统
+
+        alt 退款回调通知
+            WxPay->>Mch: 异步通知商户退款结果
+            Mch->>Mch: 保存退款通知
+            Mch-->>WxPay: 返回告知接收成功处理
+            WxPay-->>P2: 返回退款结果，并微信消息提醒
+        end
+
+        alt 查询退款单状态（未收到退款回调通知）
+            Mch->>WxPay: 调用查询单笔退款API接口，查询退款结果
+            WxPay-->>Mch: 返回退款结果
+        end
+
+        Mch-->>User: 展示退款结果
+    end
+```
 
 退款状态：
 
@@ -63,7 +114,23 @@
 
 退款至用户时，仅支持以下银行的借记卡：招行、交通银行、农行、建行、工商、中行、平安、浦发、中信、光大、民生、兴业、广发、邮储、宁波银行。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/fb1309fc40b2318f4617afb617fdad0e.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 商户系统
+        participant WxPay as 微信支付系统
+
+        alt 若需退款至用户其他银行卡
+            Mch->>User: 向用户收集接收退款的银行卡信息
+            User-->>Mch: 向商户提供接收退款的银行卡信息
+        end
+
+        Mch->>WxPay: 请求发起异常退款
+        WxPay-->>Mch: 返回受理退款信息
+    end
+```
 
 发起异常退款关键参数：
 
@@ -73,7 +140,23 @@
 
 ## 3、退款单状态流转图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/5226b63f853b2eac765e5f857b93a6dc.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "status：PROCESSING（退款处理中）" as S2
+    state "status：SUCCESS（退款成功）" as S3
+    state "status：ABNORMAL（退款异常）" as S4
+    state "status：CLOSED（退款关闭）" as S5
+
+    [*] --> S2: 支付成功，调用申请退款API
+    S2 --> S3: 退款成功
+    S2 --> S4: 支付账户异常导致无法正常退回
+    S2 --> S5: 退款受理超7天账户资金不足
+    S3 --> [*]
+    S4 --> S3: 调用发起异常退款API成功后或在服务商平台手动处理退款成功后
+    S5 --> [*]
+```
 
 退款单状态流转说明
 
```

### 业务示例代码
- ID: `4015217325`
- 路径: 订单退款
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015217325.md
- 更新时间变更: 2025-09-03 03:02:00 -> 2026-06-10 07:28:38
- 本地文件: `pages/4015217325.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1. 目标
 
 通过本教程的学习，你应该可以：
@@ -179,7 +181,23 @@
 
 退款单的状态机：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/a274a0b9f5ec3aadb6546cd5fb1fc4ff.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "PROCESSING[1]" as S2
+    state "SUCCESS[3]" as S3
+    state "ABNORMAL[2]" as S4
+    state "CLOSED[4]" as S5
+
+    [*] --> S2: 商户申请退款
+    S2 --> S3: 退款到账
+    S2 --> S4: 用户异常
+    S2 --> S5: 系统自动关单[商户余额不足超过期限]
+    S3 --> [*]
+    S4 --> S2: 商户发起异常退款
+    S5 --> [*]
+```
 
 ```
 package com.java.partner.refund;
```

### 微信支付退款最佳实践
- ID: `4014960215`
- 路径: 订单退款 > 附录
- URL: https://pay.weixin.qq.com/doc/v3/partner/4014960215.md
- 更新时间变更: 2025-09-25 02:50:28 -> 2026-06-10 07:28:37
- 本地文件: `pages/4014960215.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 一、概述
 
 对微信支付订单退款，需严格遵循官方文档规范，确保资金安全。商户需通过回调通知和查询单笔退款接口获取退款单的最新状态，再根据获取的状态来做不同的业务逻辑处理。
@@ -48,7 +50,23 @@
 
 退款单状态，可以参考：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/f104291b5890d5fb7b46a38d40fcacb5.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "status:PROCESSING(退款处理中)" as S2
+    state "status:SUCCESS(退款成功)" as S3
+    state "status:ABNORMAL(退款异常)" as S4
+    state "status:CLOSED(退款关闭)" as S5
+
+    [*] --> S2: 支付成功，调用申请退款API
+    S2 --> S3: 退款成功
+    S2 --> S4: 支付账户异常导致无法正常退回
+    S2 --> S5: 退款受理超7天账户资金不足
+    S3 --> [*]
+    S4 --> S3: 调用发起异常退款API成功后或在服务商平台手动处理退款成功后
+    S5 --> [*]
+```
 
 ## 三、 退款异常处理流程
 
```

### 开发指引
- ID: `4013080593`
- 路径: 下载账单
- URL: https://pay.weixin.qq.com/doc/v3/partner/4013080593.md
- 更新时间变更: 2024-11-25 08:53:40 -> 2026-06-09 07:58:24
- 本地文件: `pages/4013080593.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1、整体业务开发流程概览
 
 服务商如有对账需求，可在上午十点后可调用申请账单接口（[交易账单](https://pay.weixin.qq.com/doc/v3/partner/4013080595.md)或[资金账单](https://pay.weixin.qq.com/doc/v3/partner/4013080596.md)），获取前三个月内任一天的账单下载链接（download\_url），并通过该链接下载获取账单文件。
@@ -19,7 +21,17 @@
 
 商户调用申请账单API（[申请交易账单](https://pay.weixin.qq.com/doc/v3/partner/4013080595.md)/[申请资金账单](https://pay.weixin.qq.com/doc/v3/partner/4013080596.md)）获取账单文件下载链接download\_url(5分钟内有效)。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/3d9960fe1bdd44847dc008e449aac603.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        participant Mch as 商户后端
+        participant WxPay as 微信支付系统
+
+        Mch->>WxPay: 调用微信申请账单接口
+        WxPay-->>Mch: 申请账单成功返回下载链接download_url与哈希值
+    end
+```
 
 申请账单关键参数说明：
 
@@ -31,4 +43,15 @@
 
 服务商获得5分钟有效期的下载链接（download\_url）后，需通过GET方式请求并按[apiv3标准生成签名](https://pay.weixin.qq.com/doc/v3/partner/4012365870.md#1.1-%E8%AF%B7%E6%B1%82%E5%BE%AE%E4%BF%A1%E6%94%AF%E4%BB%98%E6%8E%A5%E5%8F%A3)来获取账单文件，不得直接在浏览器中访问。默认返回账单文件内容，服务商需用utf-8编码读取；若申请账单时tar\_type指定了GZIP压缩类型，则返回.gzip格式压缩文件，需先解压再读取账单内容。账单文件下载后服务商应计算哈希值，并与申请账单返回的哈希值对比，以确保账单完整性。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/02c97f57c663f08747dda068039e6ee0.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        participant Mch as 商户后端
+        participant WxPay as 微信支付系统
+
+        Mch->>WxPay: 按照apiv3标准生成签名放请求头，GET请求download_url(5分钟内有效)
+        WxPay-->>Mch: 返回账单文件内容或压缩文件(申请账单时指定GZIP压缩)
+        Mch->>Mch: 商户下载并校验哈希值
+    end
+```
```

### 开发指引
- ID: `4012072601`
- 路径: 分账
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012072601.md
- 更新时间变更: 2025-08-13 10:15:05 -> 2026-06-09 09:46:15
- 本地文件: `pages/4012072601.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -12,17 +14,44 @@
 
 ### 3.1. 业务流程图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/b44eadd582847ee8f44c8f6e562a5d50.png)
+```mermaid
+sequenceDiagram
+rect rgb(255,255,255)
+    autonumber
+    actor 用户
+    participant 商户系统-分账方
+    participant 微信支付系统
+    actor 分账接收方
+
+
+        用户->>商户系统-分账方: 用户在商户侧使用微信支付进行支付
+        商户系统-分账方->>微信支付系统: 待分账标识参数, 请求下单并支付（profit_sharing）
+        微信支付系统->>微信支付系统: 此次省去客户端校验支付流程
+        微信支付系统-->>商户系统-分账方: 回调支付结果给商户系统
+
+        商户系统-分账方->>微信支付系统: 调用接口添加分账接收方
+        note right of 商户系统-分账方: 添加分账接收方需要在申请分账前进行
+        微信支付系统-->>商户系统-分账方: 返回添加结果
+
+        商户系统-分账方->>微信支付系统: 添加分账方成功后请求申请分账
+        微信支付系统->>分账接收方: 按照商户需求分账给分账接收方
+        微信支付系统->>商户系统-分账方: 返回分账申请结果(非最终分账结果)
+
+        alt 查询分账结果（请求申请分账未收到返回或返回状态不明）
+            商户系统-分账方->>微信支付系统: 调用查询分账结果
+        end
+    end
+```
 
 重点步骤说明：
 
-步骤4：服务商发起添加分账接收方请求（[添加分账接收方API](https://pay.weixin.qq.com/doc/v3/partner/4012690944.md)），商户的分账接收方数量上限为2万。若已达到上限，可删除部分未使用的接收方后重新添加；
+步骤5：服务商发起添加分账接收方请求（[添加分账接收方API](https://pay.weixin.qq.com/doc/v3/partner/4012690944.md)），商户的分账接收方数量上限为2万。若已达到上限，可删除部分未使用的接收方后重新添加；
 
-步骤6：在基础支付中上传参数 `profit_sharing`，请求支付。支付完成后，调用[请求分账接口](https://pay.weixin.qq.com/doc/v3/partner/4012690683.md)；
+步骤7：在基础支付中上传参数 `profit_sharing`，请求支付。支付完成后，调用[请求分账接口](https://pay.weixin.qq.com/doc/v3/partner/4012690683.md)；
 
-步骤7：请求分账接口采用异步处理模式，即在接收到商户请求后，会先受理请求（受理请求返回的结果非最终分账结果）再异步处理，最终的分账结果需要通过[查询分账结果接口](https://pay.weixin.qq.com/doc/v3/partner/4012466850.md)获取；
+步骤8：请求分账接口采用异步处理模式，即在接收到商户请求后，会先受理请求（受理请求返回的结果非最终分账结果）再异步处理，最终的分账结果需要通过[查询分账结果接口](https://pay.weixin.qq.com/doc/v3/partner/4012466850.md)获取；
 
-步骤8：调用[查询分账结果接口](https://pay.weixin.qq.com/doc/v3/partner/4012466850.md)，根据 `receivers.result` 判断每个接收方的分账结果，如返回 `CLOSED：已关闭`，可根据返回的 `receivers.fail_reason` 分账失败原因参考[分账失败处理指引](https://pay.weixin.qq.com/doc/v3/partner/4015504885.md)进行处理。
+步骤10：调用[查询分账结果接口](https://pay.weixin.qq.com/doc/v3/partner/4012466850.md)，根据 `receivers.result` 判断每个接收方的分账结果，如返回 `CLOSED：已关闭`，可根据返回的 `receivers.fail_reason` 分账失败原因参考[分账失败处理指引](https://pay.weixin.qq.com/doc/v3/partner/4015504885.md)进行处理。
 
 | 参数名 | 变量 | 类型\[长度限制\] | 必填 | 描述 |
 | --- | --- | --- | --- | --- |
```

### 开发指引
- ID: `4012586134`
- 路径: 微信支付分
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012586134.md
- 更新时间变更: 2025-02-13 11:38:19 -> 2026-06-10 07:28:51
- 本地文件: `pages/4012586134.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1、开发前配置
 
 开发前，开发者需要完成如下两个步骤：配置开发参数和配置产品功能。
@@ -41,7 +43,20 @@
 
 当用户申请使用服务时，商户需调用[创建支付分订单API](https://pay.weixin.qq.com/doc/v3/partner/4013138534.md)接口创建订单。在接口参数中，商户需要通过post\_payments字段，上传本笔订单的预估费用或计费规则等信息，不同的场景有不同的传值要求，详见：[post\_payments(后付费项目)字段传参说明](https://pay.weixin.qq.com/doc/v3/partner/4013163663.md)
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/73a711efab31fc8f04eaef2ee4ad38f1.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 商户系统
+        participant WxPay as 微信支付分小程序
+        participant WxPay2 as 微信支付系统
+
+        User->>Mch: 用户下单
+        Mch->>WxPay2: 创建支付分订单
+        WxPay2-->>Mch: 返回用于拉起微信支付分小程确认订单参数“package”
+    end
+```
 
 下单接口需要注意的参数：下单接口需要注意的参数：
 
@@ -71,7 +86,23 @@
 
 商户调用[创建支付分订单API](https://pay.weixin.qq.com/doc/v3/partner/4013138534.md)接口生成订单后，会获取到用于拉起支付分订单确认页面的关键参数"package"，商户根据自己使用支付分的载体选择对应API接口拉起支付分，移动应用类型使用[APP调起支付分订单确认页面](https://pay.weixin.qq.com/doc/v3/partner/4012607507.md)，公众号类型使用[JSAPI调起支付分订单确认页面](https://pay.weixin.qq.com/doc/v3/partner/4012607505.md)，小程序类型使用[小程序调起支付分订单确认页面](https://pay.weixin.qq.com/doc/v3/partner/4012607510.md)。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/2d73b84cbc4cc8e4674b220c7ed04969.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 商户系统
+        participant WxPay as 微信支付分小程序
+        participant WxPay2 as 微信支付系统
+
+        Mch->>WxPay: 跳转微信支付分小程序确认订单页
+        WxPay->>WxPay2: 判断用户是否有免押权益
+        WxPay2-->>WxPay: 获取综合评估结果
+        WxPay-->>User: 展示页面结果
+        User->>WxPay: 用户确认支付分订单
+        WxPay->>WxPay2: 发送确认请求
+    end
+```
 
 #### 2.2.3、商户提供服务
 
@@ -82,7 +113,35 @@
 - 订单完结后，支付分会持续自动扣款，无需重复调用完结接口。
 
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/1c2eafe8a27ffc4b2c902cb7ddf66fa2.png)
+```mermaid
+%%{init: { "sequence": { "wrap": true, "wrapPadding": 10, "noteAlign": "left" } } }%%
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 商户系统
+        participant WxPay as 微信支付分小程序
+        participant WxPay2 as 微信支付系统
+
+        WxPay2-)Mch: 异步通知商户确认订单回调结果
+        Mch->>Mch: 保存确认订单结果
+        Mch-->>WxPay2: 返回告知成功接收处理
+
+        alt 判断确认订单状态（未收到确认订单回调）
+            Mch->>WxPay2: 主动调用查询支付分订单接口，查询确认订单状态
+            WxPay2->>Mch: 返回确认订单状态结果
+            Mch->>Mch: 订单确认成功，为用户提供服务
+        end
+
+        opt 根据情况选择调用取消订单接口（服务过程中出现异常，商户主动终止服务）
+            Mch->>WxPay2: 调用取消订单接口
+            WxPay2-->>Mch: 返回取消订单结果
+        end
+
+        Mch->>WxPay2: 调用完结订单接口
+        WxPay2-->>Mch: 同步返回完结订单结果
+    end
+```
 
 完结订单接口需要注意的参数：
 
@@ -105,7 +164,33 @@
 - 如果订单在“待支付”状态下（collection.state: USER\_PAYING），用户通过其他方式完成支付，商户可调用[同步支付分订单状态API](https://pay.weixin.qq.com/doc/v3/partner/4013138975.md)将订单支付成功状态同步给微信支付，后续微信支付将不再发起扣款，支付分订单将变成已完成状态。
 
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/050249206eec6bd107ae0ac8bc683220.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 商户系统
+        participant WxPay as 微信支付分小程序
+        participant WxPay2 as 微信支付系统
+
+        WxPay2-)Mch: 订单完结成功，微信支付进行轮询扣款，并在扣款成功后将扣款信息回调通知给商户系统
+
+        alt 判断订单扣款状态（未收到支付回调通知）
+            Mch->>WxPay2: 主动调用查询支付分订单状态接口，查询订单支付状态
+            WxPay2-->>Mch: 返回支付结果
+        end
+
+        opt 根据情况选择调用修改订单金额接口（扣款过程中，发现扣款金额有误且当前订单状态为“待支付”）
+            Mch->>WxPay2: 调用修改订单金额接口
+            WxPay2-->>Mch: 返回修改订单金额结果
+        end
+
+        opt 根据情况选择调用同步订单接口（扣款过程中，用户通过其它方式完成了支付，希望微信支付分停止继续扣款）
+            Mch->>WxPay2: 调用同步订单接口
+            WxPay2-->>Mch: 返回同步订单结果
+        end
+    end
+```
 
 #### 2.2.5、商户对账
 
@@ -128,7 +213,32 @@
 
 ### 2.3、订单状态流转图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/87b227be8c93e8f5623a6f7ee20ee629.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "state：CRATED（已创建）" as S2
+    state "state：DOING（进行中）state_description：USER_CONFIRM（用户已确认订单）" as S3
+    state "state：DOING（进行中）state_description：MCH_COMPLETE（商户已完结订单）collection.state：USER_PAYING（订单待支付）" as S4
+    state "state：DONE（已完成）collection.state：USER_PAID（订单已支付）collection.detail.paid_type：NEWTON<br/>（通过微信支付分收款）" as S5
+    state "state：EXPIRED（服务订单已失效）" as S6
+    state "state：REVOKED（商户取消服务订单）" as S7
+    state "state：DONE（已完成）collection.state：<br/>USER_PAID（订单已支付）collection.detail.paid_type：MCH<br/>（通过商户其他渠道收款）" as S8
+
+    [*] --> S2: 创建支付分订单
+    S2 --> S3: 用户确认订单成功
+    S2 --> S6: 超过30天
+    S2 --> S7: 商户取消订单
+    S3 --> S7: 商户取消订单
+    S3 --> S4: 服务结束商户完结订单
+    S6 --> [*]
+    S7 --> [*]
+    S4 --> S7: 商户取消订单
+    S4 --> S5: 委托代扣或<br/>主动支付成功<br/>collection.detail.<br/>paid_type=NEWTON
+    S4 --> S8: 商户通过其他方式收款，调<br/>用同步订单接口扭转状态，collection.detail.paid_type=<br/>MCH
+    S5 --> [*]
+    S8 --> [*]
+```
 
 1、当支付分订单状态为待支付(collection.state: USER\_PAYING)时，微信侧会定期轮询扣款，扣款失败时状态不变，扣款成功时订单状态才改变。
 
```

### 开发指引
- ID: `4012085711`
- 路径: 微信支付分停车服务
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012085711.md
- 更新时间变更: 2025-03-21 07:38:07 -> 2026-06-09 07:58:23
- 本地文件: `pages/4012085711.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -12,17 +14,68 @@
 
 ### 3.1. 业务流程图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/0b2779cfdc612eca9c921bd4d94d55b8.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant P2 as 刷码器（停车场）
+        participant Mch as 商户
+        participant WxPay as 微信支付分停车服务
+
+        User->>P2: 识别车牌
+        P2->>Mch: 提交车牌信息
+        Mch->>WxPay: 调用创建停车入场
+        WxPay->>WxPay: 检查车牌开通情况、用户欠款信息
+        WxPay->>WxPay: 查询用户当前分数是否可用无感
+        WxPay-->>Mch: 返回车牌状态和入场ID
+
+        alt 支付分停车服务（未开通服务）
+            User->>Mch: 开通无感支付
+            Mch->>WxPay: 跳转至微信支付分停车服务小程序开通页
+            WxPay->>WxPay: 支付分授权，平台代扣开通授权
+
+            alt 授权完成
+                WxPay->>User: 拉起开通成功页
+                WxPay->>Mch: 服务状态变更通知
+                WxPay->>User: 服务开通通知
+            else 授权失败
+                WxPay->>User: 拉起开通失败页
+            end
+
+        else 已开通服务
+            WxPay->>User: 入场通知
+        end
+
+        opt 车主入场后车牌状态发送变更
+            WxPay->>WxPay: 场内车牌状态变化
+            WxPay->>Mch: 处理车主场内状态变更通知
+        end
+
+        User->>P2: 识别车牌
+        P2->>Mch: 提交车牌信息
+        Mch->>WxPay: 申请扣款（车牌信息和入场ID）
+        WxPay->>WxPay: 验证请求，受理扣款请求
+        Mch->>Mch: 处理受理结果
+        Mch->>P2: 放行车辆（受理成功）
+
+        alt 受理失败
+            Mch-->>P2: 现场缴费（受理失败）
+        end
+
+        WxPay->>Mch: 异步通知扣费结果
+    end
+```
 
 重点步骤说明：
 
 步骤3 用户入场时，调用[创建停车入场](https://pay.weixin.qq.com/doc/v3/partner/4012533994.md)接口创建停车入场信息。商户根据返回的车牌状态判断用户是否开通支付分停车服务。
 
-步骤7.2 如果用户未开通支付分服务，可调用[调起微信支付分停车服务开通页](https://pay.weixin.qq.com/doc/v3/partner/4012085969.md)接口为微信支付分开通小程序，引导用户进行服务开通。
+步骤7 如果用户未开通支付分服务，可调用[调起微信支付分停车服务开通页](https://pay.weixin.qq.com/doc/v3/partner/4012085969.md)接口为微信支付分开通小程序，引导用户进行服务开通。
 
-步骤10 场内车牌发送变化后，微信支付通过[停车入场状态变更通知](https://pay.weixin.qq.com/doc/v3/partner/4012085798.md)接口将车主状态变化通知给商户。
+步骤16 场内车牌发送变化后，微信支付通过[停车入场状态变更通知](https://pay.weixin.qq.com/doc/v3/partner/4012085798.md)接口将车主状态变化通知给商户。
 
-步骤13 用户离场时，需调用[扣费受理](https://pay.weixin.qq.com/doc/v3/partner/4012534427.md)接口完成订单受理，微信支付进行异步扣款，支付完成后，会将订单支付结果发送给商户。
+步骤19 用户离场时，需调用[扣费受理](https://pay.weixin.qq.com/doc/v3/partner/4012534427.md)接口完成订单受理，微信支付进行异步扣款，支付完成后，会将订单支付结果发送给商户。
 
 ## 4. 开发注意事项
 
```

### 开发指引
- ID: `4012087802`
- 路径: 代金券
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012087802.md
- 更新时间变更: 2025-08-13 10:21:13 -> 2026-06-09 07:58:19
- 本地文件: `pages/4012087802.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2025.08.13
+>更新时间：2026.06.09
 
 ## 1. 接口规则
 
@@ -16,7 +16,39 @@
 
 #### 业务流程时序图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/f07e1981c994f035f83d12bb9c24eb49.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor Mch as 商户
+        participant Mch2 as 商户系统
+        participant WxPay as 微信支付
+
+        Mch->>Mch2: 1、请求创建代金券
+        Mch2->>WxPay: 2、调用创建代金券批次接口
+        WxPay->>WxPay: 3、校验并产生批次号
+        WxPay-->>Mch2: 4、返回代金券批次
+        Mch2-->>Mch: 5、获得代金券批次号
+        Mch->>Mch2: 6、确认并激活代金券批次
+        Mch2->>WxPay: 7、请求激活代金券批次接口
+        WxPay->>WxPay: 8、校验并更新批次状态
+        WxPay-->>Mch2: 9、返回代金券批次状态
+        Mch2-->>Mch: 10、获得代金券批次状态
+        Mch->>Mch2: 11、请求发放代金券
+        Mch2->>WxPay: 12、请求发放代金券批次接口
+        WxPay->>WxPay: 13、校验并发放代金券
+        WxPay-->>Mch2: 14、返回发放结果
+        Mch2-->>Mch: 15、获取代金券发放结果
+
+        alt 管理券
+            Mch->>Mch2: 16、查询代金券
+            Mch2->>WxPay: 17、调用相应接口
+            WxPay->>WxPay: 18、校验并查询
+            WxPay-->>Mch2: 19、返回结果
+            Mch2-->>Mch: 20、获取结果
+        end
+    end
+```
 
 重点步骤说明：
 
```

### 开发指引
- ID: `4012071998`
- 路径: 委托营销
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012071998.md
- 更新时间变更: 2025-08-13 08:56:31 -> 2026-06-09 09:47:05
- 本地文件: `pages/4012071998.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -12,7 +14,26 @@
 
 #### 3.1. 业务流程图
 
-![](https://gtimg.wechatpay.cn/resource/xres/img/202210/1e406e2687809c83fc7172c5a11c3771_800x617.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        actor P2 as 商家
+        participant P3 as 公众平台
+        participant WxPay as 微信支付
+
+        P2->>P3: 1、开通小程序直播插件()
+        P2->>WxPay: 2、创建商家券(商家券or支付券)
+        WxPay->>WxPay: 3、记录券批次信息()
+        P2->>WxPay: 4、完成批次号与appid之间的合作授权()
+        WxPay->>WxPay: 5、记录appid与批次号授权关系
+        P2->>P3: 6、配置直播间派发券信息(商家券or支付券)
+        User->>P3: 7、*进入指定商家直播间()
+        User->>P3: 8、领取券(商家券or支付券)
+        User->>WxPay: 9、进入卡包，查阅相关券信息()
+    end
+```
 
 重点步骤说明：
 
```

### 开发指引
- ID: `4012072119`
- 路径: 支付有礼
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012072119.md
- 更新时间变更: 2025-03-27 08:11:49 -> 2026-06-09 09:46:59
- 本地文件: `pages/4012072119.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -14,7 +16,45 @@
 
 业务流程时序图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/3a39d6aeb5a45a126a7a57f269b5b877.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        participant Mch as 商户
+        participant WxPay as 微信支付
+        actor User as 用户
+
+        Mch->>WxPay: 1、创建商家券
+        WxPay-->>Mch: 2、返回批次号
+        Mch->>WxPay: 3、上传素材图片
+        WxPay-->>Mch: 4、返回图片CDN地址
+        Mch->>WxPay: 5、创建支付有礼活动
+        WxPay-->>Mch: 6、返回活动ID
+        Mch->>WxPay: 7、设置事件通知地址
+        WxPay-->>Mch: 8、返回结果
+        User->>Mch: 9、发起支付
+        Mch->>WxPay: 10、发起微信支付
+        User->>WxPay: 11、确认支付，输入密码
+
+        par 并行处理
+            WxPay-->>User: 12、展示支付结果
+            WxPay->>Mch: 13、通知支付结果
+            WxPay->>User: 14、发放优惠券
+        end
+
+        User->>WxPay: 15、领取优惠券
+
+        par 并行处理
+            WxPay->>Mch: 16、领券消息通知
+        end
+
+        WxPay-->>User: 16、返回领券结果
+        Mch->>WxPay: 18、查询支付有礼
+        WxPay-->>Mch: 19、返回支付有礼活动信息
+        Mch->>WxPay: 20、终止支付有礼活动
+        WxPay-->>Mch: 21、返回结果
+    end
+```
 
 重点步骤说明：
 
```

### 开发指引
- ID: `4012075386`
- 路径: 智慧商圈
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012075386.md
- 更新时间变更: 2026-05-21 06:45:10 -> 2026-06-09 07:58:14
- 本地文件: `pages/4012075386.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.05.21
+>更新时间：2026.06.09
 
 ## 1. 接口规则
 
@@ -14,7 +14,58 @@
 
 ### 3.1. 业务流程图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/84d82d927c0736939f4979fd7309ca34.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+    participant 商圈OR服务商
+    participant 商圈自有小程序
+    participant 微信支付智慧商圈运营
+    participant 微信支付商家/服务商助手小程序
+    participant 微信开放平台
+    participant 微信支付平台
+
+    %% 1. 提交邮件申请【智慧商圈】
+    商圈OR服务商->>微信支付智慧商圈运营: 1、提交邮件申请【智慧商圈】()
+    %% 2. 自操作审核
+    微信支付智慧商圈运营->>微信支付智慧商圈运营: 2、审核()
+    %% 3. 审核通过通知（虚线返回）
+    微信支付智慧商圈运营-->>商圈OR服务商: 3、审核通过，并成功开通智慧商圈()
+
+    %% 4. 添加圈内门店
+    商圈OR服务商->>微信支付商家/服务商助手小程序: 4、添加圈内门店()
+
+    %% 5. 申请【商圈快速积分】插件
+    商圈OR服务商->>微信开放平台: 5、开放平台、申请【商圈快速积分】插件()
+
+    %% 6. 邮件申请【商圈快速积分】
+    商圈OR服务商->>微信支付智慧商圈运营: 6、邮件申请【商圈快速积分】()
+    %% 7.1 运营审核（指向微信开放平台）
+    微信支付智慧商圈运营->>微信开放平台: 7.1、运营审核()
+    %% 7.2 自操作审核
+    微信支付智慧商圈运营->>微信支付智慧商圈运营: 7.2、审核()
+    %% 8. 审核通过通知（虚线返回）
+    微信支付智慧商圈运营-->>商圈OR服务商: 8、审核通过，成功开通【商圈快速积分】()
+
+    %% 9. 插件开发（商圈自有小程序）
+    商圈OR服务商->>商圈自有小程序: 9、插件开发()
+
+    %% 10. 商圈支付结果通知（微信支付平台 → 商圈OR服务商，实线）
+    微信支付平台->>商圈OR服务商: 10、商圈支付结果通知【申请积分时提供回调地址】(将已开通积分消费者消费记录通知给商户)
+    %% 11. 返回通知接收情况（商圈OR服务商 → 微信支付平台，虚线）
+    商圈OR服务商-->>微信支付平台: 11、返回通知接收情况()
+
+    %% 12. 商圈积分同步（商圈OR服务商 → 微信支付平台，实线）
+    商圈OR服务商->>微信支付平台: 12、商圈积分同步()
+
+    %% 13. 商圈退款通知（微信支付平台 → 商圈OR服务商，实线）
+    微信支付平台->>商圈OR服务商: 13、商圈退款通知【申请积分时提供回调地址】(将已开通积分消费者退款记录通知给商户)
+    %% 14. 返回通知接收情况（商圈OR服务商 → 微信支付平台，实线）
+    商圈OR服务商->>微信支付平台: 14、返回通知接收情况()
+
+    %% 15. 监控退款（微信支付平台自操作）
+    微信支付平台->>微信支付平台: 15、监控30天内已同步积分是否发生退款()
+    end
+```
 
 重点步骤说明：
 
```

### 产品介绍
- ID: `4012076036`
- 路径: 支付即服务
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012076036.md
- 更新时间变更: 2026-05-21 06:53:19 -> 2026-06-10 07:28:54
- 本地文件: `pages/4012076036.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 简介
 
 服务人员，是商家为用户提供服务和转化生意的重要一环。通过支付即服务，商家可在支付完成后为用户推送专属服务人员名片，方便用户快速添加专属服务人员为好友，将线下短时服务转化为线上持续服务，弱联系变为强连接，提升用户体验和商家运营效率。
@@ -53,7 +55,40 @@
 
 支付即服务的接入流程如图所示：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/0937fd136bbf0809341002302267945d.jpeg)
+```mermaid
+sequenceDiagram
+    participant 商家
+    participant 微信支付
+    actor 用户
+
+    %% 步骤1：开通并配置产品
+    rect rgb(255,255,255)
+
+        商家->>微信支付:  ① 开通并配置产品 <br>商家在微信支付商户平台-产品中心，开通“支付即服务”,并进行产品配置
+    end
+
+    %% 步骤2：注册服务人员
+    rect rgb(255,255,255)
+
+        商家->>微信支付: ② 注册<br>商家将服务人员注册在微信支付，微信支付会为每一个人员分配一个服务人员ID
+
+    end
+
+    %% 步骤3：分配人员与订单
+    rect rgb(255,255,255)
+        商家->>微信支付: ③ 分配<br>商家在用户支付前，通过服务人员“分配API”将“服务人员ID+商户订单号”传入
+    end
+
+    %% 步骤4：下单支付
+    rect rgb(255,255,255)
+        商家->>微信支付: ④ 下单<br>使用相同的商家订单号调用微信支付下单API完成支付(下单支付流程不变)
+    end
+
+    %% 展示入口给用户
+    rect rgb(255,255,255)
+        微信支付->>用户: 展示入口<br>根据服务人员ID，在支付账单中展示服务入口
+    end
+```
 
 1. 商家开通支付即服务，并进行产品相关设置，产品相关配置流程参见《[开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012076037.md)》；
 
```

### 开发指引
- ID: `4012076038`
- 路径: 支付即服务
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012076038.md
- 更新时间变更: 2025-08-13 10:09:31 -> 2026-06-09 09:46:56
- 本地文件: `pages/4012076038.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -22,7 +24,39 @@
 
 ### 3.1. 业务流程图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/f36f6c1c92d64f5c6b3bec940e8e7e50.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor SP as 服务商
+        actor P2 as 服务员
+        actor P3 as 商家
+        actor P4 as 顾客
+        participant P5 as 基础支付
+        participant P6 as 支付即服务系统
+
+        P3->>P6: 1、开通支付即服务产品功能
+        P3->>P6: 2、配置支付即服务产品模块及参数
+        SP->>P6: 3、邀请商家授权产品权限
+        P6->>P6: 4、生成授权单
+        P3->>P6: 5、查看授权单，完成授权
+        P3->>P6: 6、注册服务员信息
+        P6->>P6: 7、记录信息，生成并返回服务人员ID
+        P3->>P6: 8、查询服务人员信息
+        P4->>P3: 9、选购商品
+        P3->>P5: 10、下单
+        P3->>P6: 11、分配服务人员ID
+        P4->>P5: 12、支付完成
+        P5->>P6: 13、询问支付凭证cell配置信息
+        P6->>P6: 14、判断下单商家是否开通产品功能
+        P6->>P6: 15、检验服务员ID真实性
+        P6->>P6: 16、储存服务人员ID与用户UIN关联关系
+        P6->>P5: 17、返回是否带服务人员名片入口
+        P5->>P4: 18、推送支付凭证带服务人员名片
+        P4->>P6: 19、通过支付凭证进入专属服务人员名片页面
+        P6->>P6: 20、名片页面按商家配置模块进行展示
+    end
+```
 
 重点步骤说明：
 
```

### 开发指引
- ID: `4012072262`
- 路径: 点金计划
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012072262.md
- 更新时间变更: 2025-08-13 10:11:35 -> 2026-06-09 09:46:53
- 本地文件: `pages/4012072262.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -70,7 +72,56 @@
 
 ### 3.1. 业务流程图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/561ede6841fea4b00b46993f90367af4.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+    actor 用户
+    participant 微信客户端
+    participant 微信支付系统
+    participant 服务商系统
+
+    %% 主流程
+    用户->>微信客户端: 1、确认支付
+    note over 微信客户端,服务商系统: ref 微信支付付款流程
+    微信客户端->>微信客户端: 2、支付成功结果展示
+    用户->>微信客户端: 3、点击“完成”按钮
+
+    %% 第一层分支：是否开启点金计划
+    alt 是否开启点金计划（未开启）
+
+        微信客户端->>微信客户端: 4、关闭支付完成页面
+    else 已开启
+
+        微信客户端->>微信支付系统: 5、拉取点金计划配置
+        微信支付系统->>微信客户端: 返回配置信息
+
+        %% 第二层分支：是否配置商家小票链接
+        alt 是否配置商家小票链接（未配置）
+
+            微信客户端->>微信客户端: 6、展示官方小票
+        else 已配置
+
+            微信客户端->>服务商系统: 7、请求商家小票链接
+            服务商系统->>服务商系统: 8、校验check_code
+            服务商系统-->>微信客户端: 9、返回配置商家小票商户号
+
+            %% 第三层分支：等待onIframeReady事件
+            alt 等待onIframeReady事件（超时）
+                微信客户端->>微信客户端: 10、展示小票错误页面
+            else 未超时
+                服务商系统->>微信客户端: 11、发送onIframeReady事件
+
+                %% 第四层分支：展示的小票类型
+                alt 展示的小票类型（displayStyle = SHOW_CUSTOM_PAGE）
+                    微信客户端->>微信客户端: 12、展示商家小票
+                else displayStyle = SHOW_OFFICIAL_PAGE 或其他
+                    微信客户端->>微信客户端: 13、展示官方小票
+                end
+            end
+        end
+    end
+    end
+```
 
 重点步骤说明：
 
```

### 商家名片开发指引
- ID: `4016914463`
- 路径: 商家名片 > 开发指引
- URL: https://pay.weixin.qq.com/doc/v3/partner/4016914463.md
- 更新时间变更: 2026-04-02 12:54:41 -> 2026-06-10 07:28:50
- 本地文件: `pages/4016914463.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 # 1\. 开发前准备
 
 
@@ -27,7 +29,30 @@
 
 # 3\. 名片配置申请单状态流转图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/0f29b41d123a1519603a393ea859b1bf.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "配置中[1]" as S2
+    state "审核中[2]" as S3
+    state "审核驳回[3]" as S4
+    state "待发布[4]" as S5
+    state "发布完成[5]" as S6
+    state "已撤销[6]" as S8
+
+    [*] --> S2: 提交名片配置
+    S2 --> S3: 发布名片配置
+    S3 --> S4: 审核驳回
+    S3 --> S5: 审核通过
+    S6 --> [*]
+    S4 --> S2: 重新提交名片配置
+    S5 --> S8: 撤销申请
+    S3 --> S8: 撤销申请
+    S4 --> S8: 撤销申请
+    S2 --> S8: 撤销申请
+    S5 --> S6: 定时发布/立即发布条件满足
+    S8 --> [*]
+```
 
 1、服务商调用「[提交商家名片配置申请](https://pay.weixin.qq.com/doc/v3/partner/4016468440.md)」接口提交名片配置后，申请单会流转为“配置中”(applyment\_state: DRAFTING)状态。
 
```

### 交易连接名片开发指引
- ID: `4016985845`
- 路径: 商家名片 > 开发指引
- URL: https://pay.weixin.qq.com/doc/v3/partner/4016985845.md
- 更新时间变更: 2026-04-02 12:54:02 -> 2026-06-10 07:28:47
- 本地文件: `pages/4016985845.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 # 1\. 开发前准备
 
 
@@ -34,7 +36,24 @@
 
 下图展示了普通小程序支付/APP支付/支付分支付场景下申请单的状态流转过程：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/989477f88f83c5a5af9d0059548be9b1.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "审核中[1]" as S2
+    state "生效中[5]" as S3
+    state "审核驳回[2]" as S5
+    state "已撤销[6]" as S6
+
+    [*] --> S2: 提交配置申请
+    S2 --> S3: 审核通过
+    S2 --> S5: 审核驳回
+    S2 --> S6: 申请撤销
+    S3 --> [*]
+    S5 --> S2: 重新提交申请
+    S5 --> S6: 申请撤销
+    S6 --> [*]
+```
 
 1、服务商调用「[添加交易连接名片规则申请](https://pay.weixin.qq.com/doc/v3/partner/4016333302.md)」接口提交配置申请后，申请单会流转为“审核中”(configuration\_state: WAITING\_AUDIT)状态，微信侧进行审批，审批方式为人工审核：
 
@@ -58,7 +77,24 @@
 
 下图展示了收银类小程序支付/付款码支付场景下申请单的状态流转过程：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/4084baeee6b6643e29a4dcfbc4cb77ff.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "待商户超管确认[3]" as S2
+    state "生效中[5]" as S3
+    state "商户号超管已拒绝[4]" as S5
+    state "已撤销[6]" as S6
+
+    [*] --> S2: 提交配置申请
+    S2 --> S3: 超管已确认
+    S2 --> S5: 超管确认已拒绝/超时
+    S2 --> S6: 申请撤销
+    S3 --> [*]
+    S5 --> S2: 重新提交申请
+    S5 --> S6: 申请撤销
+    S6 --> [*]
+```
 
 1、服务商调用「[添加交易连接名片规则申请](https://pay.weixin.qq.com/doc/v3/partner/4016333302.md)」接口提交配置申请后，申请单会先流转为“待商户号超管确认”(configuration\_state: WAITING\_CONFIRMATION)状态，是否需要商户号超管确认，判断条件为：
 
```

### 开发指引
- ID: `4015274639`
- 路径: 商家名片会员
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015274639.md
- 更新时间变更: 2025-11-25 06:22:02 -> 2026-06-10 07:28:41
- 本地文件: `pages/4015274639.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1、开发前准备
 
 ### 1.1、设置安全联系人
@@ -35,9 +37,20 @@
 
 商户系统可以通过API管理会员卡模板：包括[创建](https://pay.weixin.qq.com/doc/v3/partner/4015336970.md)、[查询列表](https://pay.weixin.qq.com/doc/v3/partner/4015336976.md)、[查询详情](https://pay.weixin.qq.com/doc/v3/partner/4015336974.md)、[修改](https://pay.weixin.qq.com/doc/v3/partner/4015336977.md)、[作废](https://pay.weixin.qq.com/doc/v3/partner/4015336972.md)等操作。
 
-时序图中绿色步骤可参考API文档中对应的接口。
-
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/859ea11e9d3b21f6430643d337c26889.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        participant Mch as 商户系统
+        participant WxPay as 微信支付系统
+
+        Mch->>WxPay: 创建会员卡模板
+        Mch->>WxPay: 查询会员卡模板信息
+        Mch->>WxPay: 查询会员卡模板列表
+        Mch->>WxPay: 修改会员卡模板信息
+        Mch->>WxPay: 作废会员卡模板
+    end
+```
 
 ### 3.2、用户入会
 
@@ -47,9 +60,32 @@
 
 包括商户[发起预授权](https://pay.weixin.qq.com/doc/v3/partner/4015336986.md)、[拉起组件](https://pay.weixin.qq.com/doc/v3/partner/4015331476.md)、[接收事件通知](https://pay.weixin.qq.com/doc/v3/partner/4015283692.md)、[同步开通结果](https://pay.weixin.qq.com/doc/v3/partner/4015336979.md)、[查询用户会员卡信息](https://pay.weixin.qq.com/doc/v3/partner/4015336980.md)等操作。
 
-时序图中绿色步骤可参考API文档中对应的接口。
-
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/c21616a41d516a7010bee698c60cd567.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 商户小程序
+        participant Mch2 as 商户系统
+        participant WxPay as 微信支付
+        participant WxPay2 as 微信支付开卡组件
+
+        User->>Mch: 开通会员
+        Mch->>Mch2: 发起开通会员请求
+        Mch2->>WxPay: 发起入户组件预授权请求
+        WxPay-->>Mch2: 返回预授权token
+        Mch2-->>Mch: 返回预授权token
+        Mch->>WxPay2: 拉起品牌会员入会组件
+        User->>WxPay2: 提交开通会员信息
+        WxPay2->>WxPay: 确认开通会员
+        WxPay->>Mch2: 发送会员卡事件通知
+        Mch2->>Mch2: 记录会员信息
+        Mch2->>WxPay: 同步会员开通结果
+        User->>Mch: 查询会员信息
+        Mch->>Mch2: 查询会员信息
+        Mch2-->>WxPay: 查询用户会员卡信息
+    end
+```
 
 #### 3.2.2、【新用户】通过商家名片入会
 
@@ -57,15 +93,27 @@
 
 包括商户[接收事件通知](https://pay.weixin.qq.com/doc/v3/partner/4015283692.md)、[同步开通结果](https://pay.weixin.qq.com/doc/v3/partner/4015336979.md)等操作。
 
-时序图中绿色步骤可参考API文档中对应的接口。
-
 ##### 3.2.2.1 普通会员卡
 
 注意：
 
 普通会员，需完成 “ 会员开通” 闭环。用户在商家名片完成开通，然后由微信支付通知商户系统开通结果，最后由商户系统同步微信支付开通结果后才能结束流程。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/29659bc15ffcff8ad64fe9a54710d278.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant WxPay as 微信支付
+        participant Mch as 商户系统
+
+        User->>WxPay: 开通会员
+        WxPay->>Mch: 发送会员卡事件通知
+        Mch->>Mch: 记录会员信息
+        Mch->>WxPay: 同步会员开通结果
+        User->>WxPay: 查看会员卡信息
+    end
+```
 
 ##### 3.2.2.2 付费会员卡（暂未上线）
 
@@ -76,7 +124,28 @@
 - 付费会员，该功能暂未上线。
 
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/2b5d8787c3ecbe403a959e08174282f8.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant WxPay as 微信支付
+        participant Mch as 商户小程序
+        participant Mch2 as 商户系统
+
+        User->>WxPay: 展示开通会员卡活动
+        User->>WxPay: 购买付费会员
+        WxPay->>Mch: 跳转付费会员页面
+        User->>Mch: 购买付费会员
+        Mch->>Mch2: 购买付费会员
+        Mch2->>Mch2: 记录付费会员信息
+        Mch2-->>Mch: 返回购买结果
+        Mch-->>User: 返回购买结果
+        Mch2->>WxPay: 同步会员开通结果
+        WxPay->>WxPay: 记录付费会员信息
+        User->>WxPay: 展示会员卡信息
+    end
+```
 
 #### 3.2.3、【存量会员】通过API导入
 
@@ -84,8 +153,6 @@
 
 包括[导入用户会员卡](https://pay.weixin.qq.com/doc/v3/partner/4015336981.md)、[修改用户会员卡信息](https://pay.weixin.qq.com/doc/v3/partner/4015336985.md)等操作
 
-时序图中绿色步骤可参考API文档中对应的接口。
-
 注意：
 
 - 通过API导入用户会员卡时，必须传入会员卡code字段（user\_card\_code）。
@@ -93,7 +160,29 @@
 - 根据手机号导入用户会员卡，该功能暂未上线。
 
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/3aee189bc9cca8aab18940caff60ed3e.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        participant Mch as 商户系统
+        participant WxPay as 微信支付
+
+        Mch->>WxPay: 导入用户会员卡
+        WxPay->>WxPay: 记录用户会员卡信息
+
+        alt 用户会员卡已存在(是)
+            WxPay-->>Mch: 返回导入失败
+        else 否
+            WxPay-->>Mch: 返回用户会员卡信息
+        end
+
+        Mch->>Mch: 对比用户会员卡信息
+
+        opt 用户会员信息不一致
+            Mch->>WxPay: 修改用户会员卡信息
+        end
+    end
+```
 
 #### 3.2.4、【存量会员】通过下单同步入会
 
@@ -103,15 +192,38 @@
 
 通过下单同步入会时，必须传入会员卡code字段（user\_card\_code）。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/7b9ac4d1e5112a87d9474bbe76a9e62f.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        participant Mch as 商户系统
+        participant WxPay as 微信支付
+
+        Mch->>WxPay: 下单(attach)
+        alt 检验attach(创建用户会员卡)
+            WxPay->>WxPay: 记录用户会员卡信息
+        end
+    end
+```
 
 ### 3.3、管理用户会员卡
 
 商户系统可以通过API管理用户会员卡：包括[导入](https://pay.weixin.qq.com/doc/v3/partner/4015336981.md)、[查询列表](https://pay.weixin.qq.com/doc/v3/partner/4015336984.md)、[查询详情](https://pay.weixin.qq.com/doc/v3/partner/4015336980.md)、[修改](https://pay.weixin.qq.com/doc/v3/partner/4015336985.md)、[作废](https://pay.weixin.qq.com/doc/v3/partner/4015336983.md)等操作。
 
-时序图中绿色步骤可参考API文档中对应的接口。
-
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/a5ab97fd4ec06bb5a876d81c3c4930f6.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        participant Mch as 商户系统
... 已截断其余 56 行 diff
```

### 投放计划功能介绍
- ID: `4016402231`
- 路径: 摇一摇有优惠 > 附录
- URL: https://pay.weixin.qq.com/doc/v3/partner/4016402231.md
- 更新时间变更: 2026-04-02 12:36:06 -> 2026-06-10 07:28:14
- 本地文件: `pages/4016402231.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1、概览
 
 投放计划是摇一摇有优惠的投放端管理能力，创建投放计划后，优惠会进入微信多个场景进行曝光，用户有机会在支付后摇优惠、支付后领取优惠运营位、微信支付公众号、微信支付 交易凭证、商家名片、摇优惠「今日」、摇优惠「附近」、找商家等场景领取优惠，从而帮助商家实现用户拉新、老客促活等经营目标。
@@ -29,7 +31,51 @@
 
 3.1 状态机
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/43c3641de4feb924412697369f31ca38.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+
+    %% 状态字母映射
+    [*] --> A : 创建投放计划
+    A: 创建成功<br/>CREATED
+    B: 审核中<br/>PROCESSING
+    C: 审核驳回<br/>REJECTED
+    D: 审核通过<br/>PASSED
+    E: 投放中<br/>DELIVERING
+    F: 已暂停<br/>PAUSED
+    G: 已终止/已过期<br/>TERMINATED/EXPIRED
+
+    %% 流转链路
+
+
+
+    P1: 审核状态（草稿数据）
+    state P1 {
+        B --> D : 审核通过
+        D --> B : 修改投放计划
+        B --> C : 审核驳回
+        C --> B : 重新修改投放计划
+    }
+    note left of P1
+      注:
+        1.投放中的投放计划，提交修改后，审核状态扭转为审核中，活动状态和线上数据不改变
+        2.若草稿数据被审核驳回，可再次修改提交审核，活动状态和线上数据均不改变;
+        3.若新的草稿数据被审核通过，则草稿数据覆盖线上数据，线上数据开始生效。
+    end note
+    P2: 活动状态（线上数据）
+    state P2 {
+    E --> F : 库存不足自动暂停
+    F --> E : 补充库存提审恢复
+
+    E --> G : 终止活动/活动过期
+    F --> G : 终止活动/活动过期
+    A --> G : 终止活动/活动过期
+    }
+    A --> B : 1.保存投放计划草稿数据<br/>2.草稿数据自动提交进入审核中状态<br/>3.活动状态为"创建成功"
+    D --> E : 草稿活动数据生效为线上数据，状态为投放中
+    G --> [*]
+```
 
 3.2 状态说明
 
```

### 投放计划配置指引
- ID: `4016111064`
- 路径: 摇一摇有优惠 > 附录
- URL: https://pay.weixin.qq.com/doc/v3/partner/4016111064.md
- 更新时间变更: 2026-03-12 02:21:47 -> 2026-06-10 07:28:12
- 本地文件: `pages/4016111064.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 针对服务商模式可通过以下三种方式进行投放计划的配置
 
 方式一：服务商联系微信支付运营配置；
@@ -106,4 +108,24 @@
 - 状态机
 
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/c8656fcf92a0687817b2d55d233a78f3.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "创建成功[1]" as Activity_579e896e_934f_41e4_bd79_61b57feede67
+    state "投放中[2]" as Activity_52a975af_2951_4926_8f6f_c4ed43f31347
+    state "投放暂停[3]" as Activity_9e4fb138_90b6_4e76_a92d_6fcf2ac161b2
+    state "已过期[4]" as Activity_fcb841c4_fdde_4dd5_aac2_3222a3864edb
+    state "已终止[5]" as Activity_64c0bcb0_f8e9_4ce7_b8bb_fcd6306048e6
+
+    [*] --> Activity_579e896e_934f_41e4_bd79_61b57feede67: 创建活动
+    Activity_579e896e_934f_41e4_bd79_61b57feede67 --> Activity_52a975af_2951_4926_8f6f_c4ed43f31347: 审核通过
+    Activity_52a975af_2951_4926_8f6f_c4ed43f31347 --> Activity_9e4fb138_90b6_4e76_a92d_6fcf2ac161b2: 库存用尽
+    Activity_579e896e_934f_41e4_bd79_61b57feede67 --> Activity_fcb841c4_fdde_4dd5_aac2_3222a3864edb: 活动已过期
+    Activity_52a975af_2951_4926_8f6f_c4ed43f31347 --> Activity_fcb841c4_fdde_4dd5_aac2_3222a3864edb: 活动已过期
+    Activity_9e4fb138_90b6_4e76_a92d_6fcf2ac161b2 --> Activity_52a975af_2951_4926_8f6f_c4ed43f31347: 补仓库存
+    Activity_9e4fb138_90b6_4e76_a92d_6fcf2ac161b2 --> Activity_64c0bcb0_f8e9_4ce7_b8bb_fcd6306048e6: 终止活动
+    Activity_9e4fb138_90b6_4e76_a92d_6fcf2ac161b2 --> Activity_fcb841c4_fdde_4dd5_aac2_3222a3864edb: 活动已过期
+    Activity_52a975af_2951_4926_8f6f_c4ed43f31347 --> Activity_64c0bcb0_f8e9_4ce7_b8bb_fcd6306048e6: 活动终止
+    Activity_64c0bcb0_f8e9_4ce7_b8bb_fcd6306048e6 --> [*]
+```
```

### 开发指引
- ID: `4015788446`
- 路径: 商品券（单券）
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015788446.md
- 更新时间变更: 2026-03-23 13:46:14 -> 2026-06-10 07:28:11
- 本地文件: `pages/4015788446.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1、开发前准备
 
 ### 1.1、熟悉微信支付接口规则
@@ -39,7 +41,24 @@
 
 注意：商品券回调通知地址是以服务商为维度配置的，所有商品券共用，若已有配置，则无需重复调用接口设置。回调地址的设置规范请参考文档：[回调通知注意事项](https://pay.weixin.qq.com/doc/v3/partner/4012082570.md)
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/1938132e6de0895dce95c83b4ff1998b.png)
+```mermaid
+sequenceDiagram
+	rect rgb(255,255,255)
+    actor 用户
+    participant 商户系统
+    participant 微信支付系统
+
+        opt 设置商品券事件通知地址
+            商户系统->>微信支付系统: 1.1 调用「设置商品券事件通知地址」接口
+            微信支付系统-->>商户系统: 1.2 设置成功，返回通知URL地址和更新时间
+        end
+
+        opt 查询商品券事件通知地址
+            商户系统->>微信支付系统: 2.1 调用「获取商品券事件通知地址」接口
+            微信支付系统-->>商户系统: 2.2 返回服务商维度下设置的通知URL地址和更新时间
+        end
+    end
+```
 
 #### 3.2、管理商品券
 
@@ -53,7 +72,34 @@
 
 3、商品券失效时，商品券下所有批次都会失效。并且会同步终止该商品券所有投放渠道和活动，不会有新的用户领券事件，但历史已经通过该商品券对应的批次发放的用户券仍然有效。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/efb6a4e1222677df354f01b7b36250a6.png)
+```mermaid
+sequenceDiagram
+	rect rgb(255,255,255)
+    actor 用户
+    participant 商户系统
+    participant 微信支付系统
+
+        opt 创建商品券
+            商户系统->>微信支付系统: 1.1 调用「创建商品券」接口
+            微信支付系统-->>商户系统: 1.2 返回商品券ID、商品券批次ID、商品券信息
+        end
+
+        opt 修改商品券
+            商户系统->>微信支付系统: 2.1 调用「修改商品券」接口
+            微信支付系统-->>商户系统: 2.2 返回商品券修改结果
+        end
+
+        opt 查询商品券
+            商户系统->>微信支付系统: 3.1 调用「查询商品券」接口
+            微信支付系统-->>商户系统: 3.2 返回查询结果
+        end
+
+        opt 失效商品券
+            商户系统->>微信支付系统: 4.1 调用「失效商品券」接口
+            微信支付系统-->>商户系统: 4.2 返回失效商品券的信息
+        end
+    end
+```
 
 #### 3.3、管理商品券批次
 
@@ -67,7 +113,58 @@
 
 3、「[失效商品券批次](https://pay.weixin.qq.com/doc/v3/partner/4015781532.md)」接口只会使单个商品券批次失效，不会影响到其他批次。失效后，该批次不会有新的用户领券事件，但历史已经通过该批次发放的用户券仍然有效。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/d2d40b7c62e7c00e6565db61e51269e6.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        participant Mch as 商户系统
+        participant WxPay as 微信支付系统
+
+        opt 添加商品券批次
+            Mch->>WxPay: 添加商品券批次
+            WxPay-->>Mch: 此次新增的商品券批次详情
+        end
+
+        opt 查询商品券批次列表
+            Mch->>WxPay: 查询商品券批次列表
+            WxPay-->>Mch: 符合查询条件的批次列表
+        end
+
+        opt 查询商品券指定批次
+            Mch->>WxPay: 查询商品券指定批次
+            WxPay-->>Mch: 商品券批次详情
+        end
+
+        opt 修改商品券批次
+            Mch->>WxPay: 修改商品券批次
+            WxPay-->>Mch: 修改后的商品券批次详情
+        end
+
+        opt 修改商品券批次发放预算
+            Mch->>WxPay: 修改商品券批次发放预算
+            WxPay-->>Mch: 修改后的商品券批次详情
+        end
+
+        opt 失效商品券批次
+            Mch->>WxPay: 失效商品券批次
+            WxPay-->>Mch: 失效后的商品券批次详情
+        end
+
+        opt 批次的 coupon_code_mode 为 UPLOAD 时
+            Mch->>WxPay: 预上传券Code
+            WxPay-->>Mch: 上传结果
+        end
+
+        opt 批次的 store_scope 为 SPECIFIC 时
+            Mch->>WxPay: 批次关联门店
+            WxPay-->>Mch: 关联结果
+            Mch->>WxPay: 批次取消关联门店
+            WxPay-->>Mch: 取消关联结果
+            Mch->>WxPay: 查询批次关联门店列表
+            WxPay-->>Mch: 批次关联门店列表
+        end
+    end
+```
 
 #### 3.4、管理用户的券
 
@@ -77,13 +174,107 @@
 
 商品券有多个发券渠道，可以由微信支付提供的营销渠道（摇一摇有优惠、商家名片等）发券，服务商也可以调用「[向用户发放商品券](https://pay.weixin.qq.com/doc/v3/partner/4015781605.md)」接口主动发券，不论由何渠道发放，微信支付均会发送「[商品券回调通知](https://pay.weixin.qq.com/doc/v3/partner/4015780862.md)」给服务商，服务商需调用「[确认发放用户商品券](https://pay.weixin.qq.com/doc/v3/partner/4015781575.md)」接口确认发放成功，用户的券才会生效。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/2c744b47cef0e90a090995f46049a3df.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 微信用户
+        participant Mch as 商户系统
+        participant WxPay as 微信支付系统
+        participant MiniApp as 小程序发券组件
+        participant MiniApp2 as 小程序核销组件
+
+		opt 领券
+          alt 用户通过“摇一摇摇优惠”领券
+              User->>WxPay: 领取商品券
+              WxPay->>WxPay: 发放商品券，用户券状态为「待确认」
+              WxPay-)Mch: 接收商品券回调通知
+              Mch->>Mch: 商户内部给用户发券
+              Mch->>WxPay: 确认发放用户商品券
+              WxPay->>WxPay: 用户券状态转为「已发放待生效」/「已生效」
+          else 商户通过“向用户发放商品券API”发券
+              Mch->>WxPay: 向用户发放商品券
+              WxPay->>WxPay: 发放商品券，用户券状态为「待确认」
+              WxPay-)Mch: 接收商品券回调通知
+              Mch->>Mch: 商户内部给用户发券
+              Mch->>WxPay: 确认发放用户商品券
+              WxPay->>WxPay: 用户券状态转为「已发放待生效」/「已生效」
+          else 商户通过“小程序发券组件”发券
+              User->>Mch: 展示可领券信息
+              Mch->>WxPay: 预发放商品券
+              Mch->>MiniApp: 拉起组件，展示商品券信息(预发放Token)
+              User->>MiniApp: 领取商品券
+              MiniApp->>WxPay: 领取商品券
+              WxPay->>WxPay: 发放商品券，用户券状态为「待确认」
+              WxPay-)Mch: 接收商品券回调通知
+              Mch->>Mch: 商户内部给用户发券
+              Mch->>WxPay: 确认发放用户商品券
+              WxPay->>WxPay: 用户券状态转为「已发放待生效」/「已生效」
+          end
+        end
+
+        opt 核券
+
+            opt 商户小程序中使用核销组件
+                User->>Mch: 展示可核销券信息
+                Mch->>MiniApp2: 拉起核销组件，展示用户券信息
+            end
+
+            User->>Mch: 用券买单
+            Mch->>Mch: 商户内部核券
+            Mch->>WxPay: 核销用户商品券
+            WxPay->>WxPay: 用户券状态转为「已核销」
+            WxPay-->>User: 接收核销成功通知
+        end
+
+        opt 退券
+            User->>Mch: 用券订单退款
+            Mch->>Mch: 商户内部退券
+            Mch->>WxPay: 退券
+            WxPay->>WxPay: 用户券状态转为「已生效」
+        end
+
+		opt 失效用户商品券
+        	note right of WxPay: 用户状态扭转需要遵守其状态机<br/>「已使用」「已删除」的用户券不会因本操作变为「已失效」
+          alt 单次优惠
+
+              Mch->>WxPay: 失效用户商品券
... 已截断其余 100 行 diff
```

### 小程序发券组件开发指引
- ID: `4016434329`
- 路径: 商品券（单券） > 附录
- URL: https://pay.weixin.qq.com/doc/v3/partner/4016434329.md
- 更新时间变更: 2026-04-02 14:44:14 -> 2026-06-10 07:28:10
- 本地文件: `pages/4016434329.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1、开发前准备
 
 A、商家需先访问[微信支付品牌经营平台](https://pay.weixin.qq.com/xdc/brandhomeweb/brand/home#/)开通品牌，成为微信支付品牌商家。详细流程可见：[【商户版】品牌经营平台介绍](https://doc.weixin.qq.com/doc/w3_AUMA3AbsAKcCNqNE3jV15S96SGeWR?scode=AJEAIQdfAAockxrOtDAcoAmgbgAOI)
@@ -11,7 +13,35 @@
 
 ## 2、整体业务开发流程概览
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/08d74b620bdf37ee6b0d437400156b32.jpeg)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 商户小程序（前端）
+        participant Mch2 as 商户系统（后台）
+        participant MiniApp as 小程序领券组件
+        participant WxPay as 微信支付商品券系统
+
+        User->>Mch: 访问小程序
+        Mch->>Mch2: 请求发券
+        Mch2->>WxPay: 调用“向用户预发放商品券”接口
+        WxPay-->>Mch2: 返回token
+        Mch2->>Mch: 返回token
+        Mch->>MiniApp: 调起领券组件
+        MiniApp->>User: 展示“待领券”页面
+        User->>MiniApp: 点击“领取”
+        MiniApp->>WxPay: 向用户发放商品券
+        WxPay->>WxPay: 向用户发放商品券，状态扭转为“待确认”
+        WxPay-->>MiniApp: 返回发券成功
+        MiniApp->>User: 展示“去使用”页面
+        Mch2->>WxPay: 确认发券
+        WxPay->>WxPay: 券状态扭转为“已发放待生效”或“已生效”
+        User->>MiniApp: 点击“去使用”
+        MiniApp->>Mch: 关闭组件半屏弹层，回调商户
+        Mch->>User: 展示下单页
+    end
+```
 
 步骤说明
 
```

### 开发指引
- ID: `4016438816`
- 路径: 商品券（多次优惠）
- URL: https://pay.weixin.qq.com/doc/v3/partner/4016438816.md
- 更新时间变更: 2026-01-29 07:28:12 -> 2026-06-10 07:28:08
- 本地文件: `pages/4016438816.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1、开发前准备
 
 ### 1.1、熟悉微信支付接口规则
@@ -35,7 +37,24 @@
 
 注意：商品券回调通知地址是以服务商为维度配置的，所有商品券共用，若已有配置，则无需重复调用接口设置。回调地址的设置规范请参考文档：[回调通知注意事项](https://pay.weixin.qq.com/doc/v3/partner/4012082570.md)
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/1938132e6de0895dce95c83b4ff1998b.png)
+```mermaid
+sequenceDiagram
+	rect rgb(255,255,255)
+    actor 用户
+    participant 商户系统
+    participant 微信支付系统
+
+        opt 设置商品券事件通知地址
+            商户系统->>微信支付系统: 1.1 调用「设置商品券事件通知地址」接口
+            微信支付系统-->>商户系统: 1.2 设置成功，返回通知URL地址和更新时间
+        end
+
+        opt 查询商品券事件通知地址
+            商户系统->>微信支付系统: 2.1 调用「获取商品券事件通知地址」接口
+            微信支付系统-->>商户系统: 2.2 返回服务商维度下设置的通知URL地址和更新时间
+        end
+    end
+```
 
 #### 3.2、管理商品券
 
@@ -49,7 +68,34 @@
 
 3、商品券失效时，商品券下所有批次都会失效。并且会同步终止该商品券所有投放渠道和活动，不会有新的用户领券事件，但历史已经通过该商品券对应的批次发放的用户券仍然有效。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/efb6a4e1222677df354f01b7b36250a6.png)
+```mermaid
+sequenceDiagram
+	rect rgb(255,255,255)
+    actor 用户
+    participant 商户系统
+    participant 微信支付系统
+
+        opt 创建商品券
+            商户系统->>微信支付系统: 1.1 调用「创建商品券」接口
+            微信支付系统-->>商户系统: 1.2 返回商品券ID、商品券批次ID、商品券信息
+        end
+
+        opt 修改商品券
+            商户系统->>微信支付系统: 2.1 调用「修改商品券」接口
+            微信支付系统-->>商户系统: 2.2 返回商品券修改结果
+        end
+
+        opt 查询商品券
+            商户系统->>微信支付系统: 3.1 调用「查询商品券」接口
+            微信支付系统-->>商户系统: 3.2 返回查询结果
+        end
+
+        opt 失效商品券
+            商户系统->>微信支付系统: 4.1 调用「失效商品券」接口
+            微信支付系统-->>商户系统: 4.2 返回失效商品券的信息
+        end
+    end
+```
 
 #### 3.3、管理商品券批次
 
@@ -61,7 +107,57 @@
 
 2、「[修改商品券批次组发放预算](https://pay.weixin.qq.com/doc/v3/partner/4016280642.md)」接口每次调用只能调整一个维度的投放预算，如果你需要调整多个维度的预算，请多次调用本接口。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/ff447c444824c4d854adaf492df2ffde.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        participant Mch as 商户系统
+        participant WxPay as 微信支付系统
+
+        opt 添加商品券批次组
+            Mch->>WxPay: 添加商品券批次组
+            WxPay-->>Mch: 此次新增的商品券批次组详情
+        end
+
+        opt 查询商品券批次列表
+            Mch->>WxPay: 查询商品券批次列表
+            WxPay-->>Mch: 符合查询条件的批次列表
+        end
+
+        opt 查询商品券指定批次
+            Mch->>WxPay: 查询商品券指定批次
+            WxPay-->>Mch: 商品券批次详情
+        end
+
+        opt 修改商品券批次组
+            Mch->>WxPay: 修改商品券批次组
+            WxPay-->>Mch: 修改后的商品券批次组详情
+        end
+
+        opt 修改商品券批次组发放预算
+            Mch->>WxPay: 修改商品券批次组发放预算
+            WxPay-->>Mch: 修改后的商品券批次组详情
+        end
+
+        opt 批次组的 coupon_code_mode 为 UPLOAD 时
+
+            loop 对批次组内所有批次依次执行
+                Mch->>WxPay: 预上传券Code
+                WxPay-->>Mch: 上传结果
+            end
+
+        end
+
+        opt 批次组的 store_scope 为 SPECIFIC 时
+            Mch->>WxPay: 批次组关联门店
+            WxPay-->>Mch: 关联结果
+            Mch->>WxPay: 批次组取消关联门店
+            WxPay-->>Mch: 取消关联结果
+            Mch->>WxPay: 查询批次关联门店列表
+            WxPay-->>Mch: 批次关联门店列表
+        end
+    end
+```
 
 #### 3.4、管理用户的券
 
@@ -71,13 +167,107 @@
 
 商品券有多个发券渠道，可以由微信支付提供的营销渠道（摇一摇有优惠、商家名片等）发券，服务商也可以调用「[向用户发放商品券批次组](https://pay.weixin.qq.com/doc/v3/partner/4016280664.md)」接口主动发券，不论由何渠道发放，微信支付均会发送「[商品券回调通知](https://pay.weixin.qq.com/doc/v3/partner/4016435717.md)」给服务商，服务商需调用「[确认发放用户商品券](https://pay.weixin.qq.com/doc/v3/partner/4016435562.md)」接口确认发放成功，用户的券才会生效。
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/2c744b47cef0e90a090995f46049a3df.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 微信用户
+        participant Mch as 商户系统
+        participant WxPay as 微信支付系统
+        participant MiniApp as 小程序发券组件
+        participant MiniApp2 as 小程序核销组件
+
+		opt 领券
+          alt 用户通过“摇一摇摇优惠”领券
+              User->>WxPay: 领取商品券
+              WxPay->>WxPay: 发放商品券，用户券状态为「待确认」
+              WxPay-)Mch: 接收商品券回调通知
+              Mch->>Mch: 商户内部给用户发券
+              Mch->>WxPay: 确认发放用户商品券
+              WxPay->>WxPay: 用户券状态转为「已发放待生效」/「已生效」
+          else 商户通过“向用户发放商品券API”发券
+              Mch->>WxPay: 向用户发放商品券
+              WxPay->>WxPay: 发放商品券，用户券状态为「待确认」
+              WxPay-)Mch: 接收商品券回调通知
+              Mch->>Mch: 商户内部给用户发券
+              Mch->>WxPay: 确认发放用户商品券
+              WxPay->>WxPay: 用户券状态转为「已发放待生效」/「已生效」
+          else 商户通过“小程序发券组件”发券
+              User->>Mch: 展示可领券信息
+              Mch->>WxPay: 预发放商品券
+              Mch->>MiniApp: 拉起组件，展示商品券信息(预发放Token)
+              User->>MiniApp: 领取商品券
+              MiniApp->>WxPay: 领取商品券
+              WxPay->>WxPay: 发放商品券，用户券状态为「待确认」
+              WxPay-)Mch: 接收商品券回调通知
+              Mch->>Mch: 商户内部给用户发券
+              Mch->>WxPay: 确认发放用户商品券
+              WxPay->>WxPay: 用户券状态转为「已发放待生效」/「已生效」
+          end
+        end
+
+        opt 核券
+
+            opt 商户小程序中使用核销组件
+                User->>Mch: 展示可核销券信息
+                Mch->>MiniApp2: 拉起核销组件，展示用户券信息
+            end
+
+            User->>Mch: 用券买单
+            Mch->>Mch: 商户内部核券
+            Mch->>WxPay: 核销用户商品券
+            WxPay->>WxPay: 用户券状态转为「已核销」
+            WxPay-->>User: 接收核销成功通知
+        end
+
+        opt 退券
+            User->>Mch: 用券订单退款
+            Mch->>Mch: 商户内部退券
+            Mch->>WxPay: 退券
+            WxPay->>WxPay: 用户券状态转为「已生效」
+        end
+
+		opt 失效用户商品券
+        	note right of WxPay: 用户状态扭转需要遵守其状态机<br/>「已使用」「已删除」的用户券不会因本操作变为「已失效」
+          alt 单次优惠
+
+              Mch->>WxPay: 失效用户商品券
+              WxPay->>WxPay: 用户券状态转为「已失效」
... 已截断其余 99 行 diff
```

### 小程序发券组件开发指引
- ID: `4016435566`
- 路径: 商品券（多次优惠） > 附录
- URL: https://pay.weixin.qq.com/doc/v3/partner/4016435566.md
- 更新时间变更: 2026-04-02 14:46:11 -> 2026-06-10 07:28:07
- 本地文件: `pages/4016435566.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1、开发前准备
 
 A、商家需先访问[微信支付品牌经营平台](https://pay.weixin.qq.com/xdc/brandhomeweb/brand/home#/)开通品牌，成为微信支付品牌商家。详细流程可见：[【商户版】品牌经营平台介绍](https://doc.weixin.qq.com/doc/w3_AUMA3AbsAKcCNqNE3jV15S96SGeWR?scode=AJEAIQdfAAockxrOtDAcoAmgbgAOI)
@@ -11,7 +13,35 @@
 
 ## 2、整体业务开发流程概览
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/08d74b620bdf37ee6b0d437400156b32.jpeg)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant Mch as 商户小程序（前端）
+        participant Mch2 as 商户系统（后台）
+        participant MiniApp as 小程序领券组件
+        participant WxPay as 微信支付商品券系统
+
+        User->>Mch: 访问小程序
+        Mch->>Mch2: 请求发券
+        Mch2->>WxPay: 调用“向用户预发放商品券”接口
+        WxPay-->>Mch2: 返回token
+        Mch2->>Mch: 返回token
+        Mch->>MiniApp: 调起领券组件
+        MiniApp->>User: 展示“待领券”页面
+        User->>MiniApp: 点击“领取”
+        MiniApp->>WxPay: 向用户发放商品券
+        WxPay->>WxPay: 向用户发放商品券，状态扭转为“待确认”
+        WxPay-->>MiniApp: 返回发券成功
+        MiniApp->>User: 展示“去使用”页面
+        Mch2->>WxPay: 确认发券
+        WxPay->>WxPay: 券状态扭转为“已发放待生效”或“已生效”
+        User->>MiniApp: 点击“去使用”
+        MiniApp->>Mch: 关闭组件半屏弹层，回调商户
+        Mch->>User: 展示下单页
+    end
+```
 
 步骤说明
 
```

### 开发指引
- ID: `4016628135`
- 路径: 品牌门店
- URL: https://pay.weixin.qq.com/doc/v3/partner/4016628135.md
- 更新时间变更: 2025-11-25 10:04:12 -> 2026-06-10 07:28:01
- 本地文件: `pages/4016628135.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1、整体业务开发流程概览
 
 |     |     |     |     |
@@ -13,7 +15,26 @@
 
 ## 2、品牌门店状态流转图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/fdc406d7d31cfff9bcba962243642c6a.jpeg)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "门店创建中-审核中[1]" as Activity_d1ee9f46_4ebc_45c9_92aa_d0ef944fe4b0
+    state "门店创建中-审核驳回[2]" as Activity_cdb5490b_498d_4480_ac10_4e396f12a320
+    state "门店营业中[3]" as Activity_f61cd2a9_f5b7_48b2_a383_d13a51d6325a
+    state "门店营业中-审核中[1]" as Activity_0f2a5465_fc86_4173_aab5_7c692a48e832
+    state "门店营业中-审核驳回[2]" as Activity_603b5464_af14_45e2_a22c_fed65c1db989
+
+    [*] --> Activity_d1ee9f46_4ebc_45c9_92aa_d0ef944fe4b0
+    Activity_d1ee9f46_4ebc_45c9_92aa_d0ef944fe4b0 --> Activity_cdb5490b_498d_4480_ac10_4e396f12a320: 门店信息审核驳回
+    Activity_d1ee9f46_4ebc_45c9_92aa_d0ef944fe4b0 --> Activity_f61cd2a9_f5b7_48b2_a383_d13a51d6325a: 门店信息审核通过
+    Activity_f61cd2a9_f5b7_48b2_a383_d13a51d6325a --> Activity_0f2a5465_fc86_4173_aab5_7c692a48e832: 更新修改门店信息
+    Activity_0f2a5465_fc86_4173_aab5_7c692a48e832 --> Activity_603b5464_af14_45e2_a22c_fed65c1db989: 门店信息审核驳回
+    Activity_f61cd2a9_f5b7_48b2_a383_d13a51d6325a --> [*]: 删除门店
+    Activity_cdb5490b_498d_4480_ac10_4e396f12a320 --> Activity_d1ee9f46_4ebc_45c9_92aa_d0ef944fe4b0: 修改信息重新提交
+    Activity_0f2a5465_fc86_4173_aab5_7c692a48e832 --> Activity_f61cd2a9_f5b7_48b2_a383_d13a51d6325a: 门店信息审核通过
+    Activity_603b5464_af14_45e2_a22c_fed65c1db989 --> Activity_0f2a5465_fc86_4173_aab5_7c692a48e832: 修改信息重新提交
+```
 
 1、品牌门店有【门店状态】、【审核状态】两个状态字段，分别查询门店的生效状态和门店信息的审核状态。
 
```

### 开发指引
- ID: `4012072637`
- 路径: 连锁品牌分账
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012072637.md
- 更新时间变更: 2025-07-04 06:21:01 -> 2026-06-09 09:46:07
- 本地文件: `pages/4012072637.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -26,27 +28,69 @@
 
 ### 3.1. 业务流程图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/7d95907393685fa19eebcf2a9a904738.png)
+```mermaid
+sequenceDiagram
+rect rgb(255,255,255)
+    autonumber
+    actor 用户
+    participant 商户系统-分账方
+    participant 微信支付系统
+    actor 分账接收方
+
+
+        用户->>商户系统-分账方: 用户在商户侧使用微信支付进行支付
+        商户系统-分账方->>微信支付系统: 待分账标识参数, 请求下单并支付（profit_sharing）
+        微信支付系统->>微信支付系统: 此次省去客户端校验支付流程
+        微信支付系统-->>商户系统-分账方: 回调支付结果给商户系统
+
+        商户系统-分账方->>微信支付系统: 调用接口添加分账接收方
+        note right of 商户系统-分账方: 添加分账接收方需要在申请分账前进行
+        微信支付系统-->>商户系统-分账方: 返回添加结果
+
+        商户系统-分账方->>微信支付系统: 添加分账方成功后请求申请分账
+        微信支付系统->>分账接收方: 按照商户需求分账给分账接收方
+        微信支付系统->>商户系统-分账方: 返回分账申请结果(非最终分账结果)
+
+        alt 查询分账结果（请求申请分账未收到返回或返回状态不明）
+            商户系统-分账方->>微信支付系统: 调用查询分账结果
+        end
+        alt 分账后退款
+            用户->>商户系统-分账方: 申请订单退款
+            商户系统-分账方->>微信支付系统: 调用分账回退接口, 请求分账回退
+            微信支付系统->>微信支付系统: 发起分账回退
+            微信支付系统-->>商户系统-分账方: 分账动账通知
+
+            alt 异常处理（未收到分账动账通知）
+                商户系统-分账方->>微信支付系统: 请求查询分账回退接口, 查询分账回退状态
+                微信支付系统-->>商户系统-分账方: 返回分账回退结果
+            end
+
+            分账接收方->>商户系统-分账方: 资金回退
+            note over 用户,分账接收方: ref 退款流程
+        end
+        商户系统-分账方->>微信支付系统: 完结分账
+    end
+```
 
 重点步骤说明：
 
-步骤4：分账前需调用[添加分账接收方](https://pay.weixin.qq.com/doc/v3/partner/4012467100.md)接口添加分账接收方。
-
-步骤6：在基础支付中上传参数 `profit_sharing`，请求支付；支付完成后，调用[请求分账接口](https://pay.weixin.qq.com/doc/v3/partner/4012692975.md)；
-
-步骤7：请求分账接口采用异步处理模式，即在接收到商户请求后，会先受理请求（受理请求返回的结果非最终分账结果）再异步处理，最终的分账结果需要通过[查询分账结果接口](https://pay.weixin.qq.com/doc/v3/partner/4012467002.md)获取；
-
-步骤8：分账完成后，微信会通过[分账动账通知](https://pay.weixin.qq.com/doc/v3/partner/4012075400.md)接口，主动通知分账接收方商户；
-
-步骤9：分账发起方商户调用[查询分账结果接口](https://pay.weixin.qq.com/doc/v3/partner/4012467002.md)，主动查询分账结果，根据 `receivers.result` 判断每个接收方的分账结果，如返回 `CLOSED：已关闭`，可根据返回的 `receivers.fail_reason` 分账失败原因参考[分账失败处理指引](https://pay.weixin.qq.com/doc/v3/partner/4015504918.md)进行处理；
+步骤5：分账前需调用[添加分账接收方](https://pay.weixin.qq.com/doc/v3/partner/4012467100.md)接口添加分账接收方。
+
+步骤7：在基础支付中上传参数 `profit_sharing`，请求支付；支付完成后，调用[请求分账接口](https://pay.weixin.qq.com/doc/v3/partner/4012692975.md)；
+
+步骤8：请求分账接口采用异步处理模式，即在接收到商户请求后，会先受理请求（受理请求返回的结果非最终分账结果）再异步处理，最终的分账结果需要通过[查询分账结果接口](https://pay.weixin.qq.com/doc/v3/partner/4012467002.md)获取；
+
+步骤9：分账完成后，微信会通过[分账动账通知](https://pay.weixin.qq.com/doc/v3/partner/4012075400.md)接口，主动通知分账接收方商户；
+
+步骤10：分账发起方商户调用[查询分账结果接口](https://pay.weixin.qq.com/doc/v3/partner/4012467002.md)，主动查询分账结果，根据 `receivers.result` 判断每个接收方的分账结果，如返回 `CLOSED：已关闭`，可根据返回的 `receivers.fail_reason` 分账失败原因参考[分账失败处理指引](https://pay.weixin.qq.com/doc/v3/partner/4015504918.md)进行处理；
 
 步骤12：分账后若产生退款，则需先调用[请求分账回退](https://pay.weixin.qq.com/doc/v3/partner/4012467097.md)接口，请求将已经分给分账方的资金回退，再处理退款；
 
-步骤13：分账回退完成后，微信同样会通过[分账动账通知](https://pay.weixin.qq.com/doc/v3/partner/4012075400.md)接口，主动通知分账回退方商户；
-
-步骤14：分账发起方商户可以通过[查询分账回退结果](https://pay.weixin.qq.com/doc/v3/partner/4012467011.md)接口，主动查询分账回退结果；
-
-步骤17：分账结束后，商户需调用[完结分账](https://pay.weixin.qq.com/doc/v3/partner/4012467016.md)接口结束分账订单。
+步骤14：分账回退完成后，微信同样会通过[分账动账通知](https://pay.weixin.qq.com/doc/v3/partner/4012075400.md)接口，主动通知分账回退方商户；
+
+步骤15：分账发起方商户可以通过[查询分账回退结果](https://pay.weixin.qq.com/doc/v3/partner/4012467011.md)接口，主动查询分账回退结果；
+
+步骤18：分账结束后，商户需调用[完结分账](https://pay.weixin.qq.com/doc/v3/partner/4012467016.md)接口结束分账订单。
 
 ### 3.2. API接入（含示例代码）
 
```

### 业务示例代码
- ID: `4015871675`
- 路径: 连锁品牌分账
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015871675.md
- 更新时间变更: 2025-09-01 02:04:01 -> 2026-06-09 09:46:50
- 本地文件: `pages/4015871675.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1、分账
 
 ### 1.1、简介
@@ -49,11 +51,34 @@
    分账单状态：
 
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/f5de65ad409c7c250fcf90b8b3d84261.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "PROCESSING(1)" as S1
+    state "FINISHED(2)" as S2
+
+    [*] --> S1
+    S1 --> S2
+    S2 --> [*]
+```
 
 分账接收方分账结果：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/abf8ed58915789e1cc7d2097ec880b66.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "CLOSED(3)" as S2
+    state "SUCCESS(2)" as S3
+    state "PEDDING(1)" as S4
+
+    [*] --> S4
+    S4 --> S3
+    S4 --> S2
+    S3 --> [*]
+    S2 --> [*]
+```
 
 ```
 package com.java.brand.profitsharing;
@@ -486,7 +511,20 @@
 
 分账回退单状态机：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/051e836e42d4e82bdc9cf7cf99fd50c6.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "FAILED(3)" as S2
+    state "SUCCESS(2)" as S3
+    state "PROCESSING(1)" as S4
+
+    [*] --> S4
+    S4 --> S3
+    S4 --> S2
+    S3 --> [*]
+    S2 --> [*]
+```
 
 ```
 package com.java.brand.profitsharing;
```

### 开发指引
- ID: `4012072858`
- 路径: 消费者投诉2.0
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012072858.md
- 更新时间变更: 2026-03-24 07:11:27 -> 2026-06-09 09:46:03
- 本地文件: `pages/4012072858.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -12,17 +14,59 @@
 
 ### 3.1. 业务流程图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/fada548943e400d7f2bf5d22777370e2.png)
+```mermaid
+sequenceDiagram
+    autonumber
+    actor 用户
+    participant 微信客户端
+    participant 微信支付系统
+    participant 商户后台
+
+    rect rgb(255,255,255)
+        用户->>微信客户端: 用户发起投诉
+        微信客户端->>微信支付系统: 创建投诉单
+        微信支付系统->>微信支付系统: 用户投诉次数(=1)
+        微信支付系统->>商户后台: 通知商户投诉待处理
+        商户后台->>微信支付系统: 主动查询投诉单进展
+        微信支付系统-->>商户后台: 返回查询结果
+        商户后台->>商户后台: 投诉受理
+        商户后台->>微信支付系统: 调用提交回复接口，回复投诉处理
+        微信支付系统-->>微信客户端: 更新投诉单进展
+        微信客户端-->>用户: 同步投诉回复
+
+        alt 投诉处理结果（满意投诉处理结果）
+            商户后台->>微信支付系统: 反馈处理完成
+            微信支付系统-->>微信客户端: 更新投诉单进展
+            微信客户端-->>用户: 同步投诉处理完成
+        else 不满意投诉处理结果
+            用户->>微信客户端: 用户继续投诉
+            微信客户端->>微信客户端: 记录用户继续投诉内容
+            微信客户端->>微信支付系统: 投诉单状态转为待处理
+            微信支付系统->>微信支付系统: 用户投诉次数(+1)
+            微信支付系统->>商户后台: 通知商户投诉待处理
+            商户后台->>微信支付系统: 主动查询投诉单进展
+            微信支付系统-->>商户后台: 返回查询结果
+            商户后台->>商户后台: 投诉受理
+        end
+
+        par 并行处理
+            微信支付系统->>商户后台: 通知商户投诉单最新进展
+            商户后台-->>微信支付系统: 返回通知处理结果
+            商户后台->>微信支付系统: 主动查询投诉单进展
+            微信支付系统-->>商户后台: 返回查询结果
+        end
+    end
+```
 
 重点步骤说明：
 
 步骤3： 用户发起投诉后，微信支付通过[投诉通知回调API](https://pay.weixin.qq.com/doc/v3/partner/4012076174.md)通知商户投诉单需处理。
 
-步骤6： 商户接收投诉后，可通过[回复用户API](https://pay.weixin.qq.com/doc/v3/partner/4012467213.md)接口向微信支付提交投诉处理回复。
-
-步骤9： 与用户协商一致后，商户通过[反馈处理完成API](https://pay.weixin.qq.com/doc/v3/partner/4012467217.md)反馈投诉单处理完成。
-
-步骤15： 商户在没有接收到微信投诉通知的情况下可主动调用[查询投诉单详情API](https://pay.weixin.qq.com/doc/v3/partner/4012691648.md)查询投诉单处理结果。
+步骤8： 商户接收投诉后，可通过[回复用户API](https://pay.weixin.qq.com/doc/v3/partner/4012467213.md)接口向微信支付提交投诉处理回复。
+
+步骤11： 与用户协商一致后，商户通过[反馈处理完成API](https://pay.weixin.qq.com/doc/v3/partner/4012467217.md)反馈投诉单处理完成。
+
+步骤19： 商户在没有接收到微信投诉通知的情况下可主动调用[查询投诉单详情API](https://pay.weixin.qq.com/doc/v3/partner/4012691648.md)查询投诉单处理结果。
 
 ### 3.2. API接入（含示例代码）
 
```

### 业务示例代码
- ID: `4015933338`
- 路径: 消费者投诉2.0
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015933338.md
- 更新时间变更: 2025-09-11 03:01:51 -> 2026-06-09 09:46:01
- 本地文件: `pages/4015933338.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 目标
 
 学习本文档的内容，您将清晰掌握对名下子商户的以下操作
@@ -282,11 +284,42 @@
 
 「普通咨询」的投诉单状态机：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/3efd06bb04a2ee0047d95e5933661fd8.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "state：PENDING（商户待处理）" as S2
+    state "state：PROESSING（商户处理中）" as S3
+    state "state：PROCESSED（商户处理完成）" as S4
+
+    [*] --> S2: 用户提交投诉
+    S2 --> S3: 商家提交回复
+    S3 --> S4: 商家提交处理完成
+    S4 --> S3: 用户升级投诉（非全额退款到账）
+    S4 --> [*]: 用户升级投诉（全额退款到账）
+```
 
 「退款申请」的投诉单状态机：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/a824672ca6494c8bc5ba1c77a16e1112.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "state：PENDING（商户待处理）" as S2
+    state "state：PROESSING（商户处理中）" as S3
+    state "state：PROCESSED（商户处理完成）" as S4
+
+    [*] --> S2: 用户提交投诉
+    S2 --> S3: 场景1：商家提交回复；<br/>场景2：商家同意退款（非退款到账且未同意/驳回过）
+    S2 --> S4: 场景1：用户提交投诉（用户提交表单阶段商家存在退款）；<br/>场景2：退款到账事件；<br/>场景3：商家驳回退款（非退款到账且未同意/驳回过）
+    S3 --> S4: 场景1：商家提交处理完成；<br/>场景2：退款到账；<br/>场景3：商家驳回退款（非退款到账且未同意/驳回过）
+    S4 --> S3: 用户升级投诉（非全额退款到账）
+    S4 --> [*]: 用户升级投诉（全额退款到账）
+
+    note right of S3
+    	以下场景保持该状态不变<br/>场景1：商家提交回复；<br/>场景2：商家同意退款（非退款到账且未同意/驳回过）
+    end note
+```
 
 ### 3.1 商户投诉单获取
 
```

### 开发指引
- ID: `4015792556`
- 路径: 微信电子发票
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015792556.md
- 更新时间变更: 2026-05-21 06:56:01 -> 2026-06-09 09:47:17
- 本地文件: `pages/4015792556.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.05.21
+>更新时间：2026.06.09
 
 本开发指引对微信支付电子发票的标准流程、关键场景的开发思路和最佳实践展开介绍。你可以阅读开发指引，并结合【API文档】完成微信支付电子发票的接入流程。
 
@@ -19,7 +19,82 @@
 
 业务时序图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/1d6d7381064a54fc428ef141964c7e50.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+    actor 用户
+    actor 商户超管/法人
+    actor 服务商人员
+    participant 服务商业务系统
+    participant 微信支付发票系统
+
+    %% 配置流程
+    服务商人员->>服务商业务系统: 邀请商户开通
+    服务商业务系统->>微信支付发票系统: 获取开通服务商电子发票能力邀请链接
+    商户超管/法人->>微信支付发票系统: 授权开通服务商电子发票
+
+    服务商人员->>服务商业务系统: 查询邀请商户信息
+    服务商业务系统->>微信支付发票系统: 批量查询邀请商户信息
+    服务商业务系统->>微信支付发票系统: 检查子商户开通状态
+
+    服务商人员->>服务商业务系统: 创建卡券模板
+    服务商业务系统->>微信支付发票系统: 创建卡券模板
+
+    服务商人员->>服务商业务系统: 配置开发选项
+    服务商业务系统->>微信支付发票系统: 配置开发选项
+
+    %% 开票场景分支
+    opt 开票场景
+    	alt 支付账单开票
+          用户->>微信支付发票系统: 通过支付账单页点击开发票
+          微信支付发票系统->>微信支付发票系统: 用户填写开票申请
+          用户->>微信支付发票系统: 填写抬头信息
+          微信支付发票系统->>服务商业务系统: 用户填写抬头完成通知
+          服务商业务系统->>微信支付发票系统: 获取用户填写抬头信息
+        else 扫码/小程序开票
+          用户->>服务商业务系统: 用户申请开票
+          服务商业务系统->>微信支付发票系统: 获取用户填写抬头链接
+          微信支付发票系统->>服务商业务系统: 用户填写抬头完成通知
+          服务商业务系统->>微信支付发票系统: 获取用户填写抬头信息
+        end
+    end
+
+    服务商业务系统->>服务商业务系统: 匹配订单并填写开票信息
+
+    %% 开票模式分支
+    alt 开票模式（腾讯数电发票模式）
+
+        服务商业务系统->>微信支付发票系统: 开具电子发票
+        微信支付发票系统->>用户: 发票插入卡包通知
+        微信支付发票系统->>服务商业务系统: 发票插入用户卡包成功通知
+
+        opt 冲红发票
+            服务商人员->>服务商业务系统: 冲红发票
+            服务商业务系统->>微信支付发票系统: 冲红电子发票
+            微信支付发票系统->>用户: 通知用户发票被冲红
+            微信支付发票系统->>服务商业务系统: 发票核销成功通知
+        end
+
+        opt 查询下载发票信息
+            服务商人员->>服务商业务系统: 查询电子发票信息
+            服务商业务系统->>微信支付发票系统: 查询电子发票信息
+
+            服务商人员->>服务商业务系统: 下载电子发票
+            服务商业务系统->>微信支付发票系统: 获取发票下载信息
+            服务商业务系统->>微信支付发票系统: 下载发票文件
+        end
+
+        else（自建/第三方模式）
+
+        服务商业务系统->>服务商业务系统: 自行开具发票
+        服务商业务系统->>微信支付发票系统: 上传电子发票文件
+        服务商业务系统->>微信支付发票系统: 将电子发票插入微信用户卡包
+        微信支付发票系统->>用户: 发票插入卡包通知
+        微信支付发票系统->>服务商业务系统: 发票插入用户卡包成功通知
+        服务商业务系统->>微信支付发票系统: 查询电子发票信息
+    end
+    end
+```
 
 步骤一 邀请商户开通
 
```

### 业务示例代码
- ID: `4016078358`
- 路径: 微信电子发票
- URL: https://pay.weixin.qq.com/doc/v3/partner/4016078358.md
- 更新时间变更: 2026-01-22 06:49:38 -> 2026-06-10 07:28:02
- 本地文件: `pages/4016078358.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1. 目标
 
 通过本教程的学习，你应该可以：
@@ -236,7 +238,40 @@
 
 数电发票接入状态状态机：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/44d66d9567e7ae02589b22ec99af71b7.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "state:ACCESS_CONFIRMED_PENDING(请商户法定代表人/财务负责人登陆电子税局或者国家税务总局乐企数字开放平台进行确认)" as S2
+    state "state:ABILITY_ CONFIRMED_PENDING(请商户法定代表人/财务负责人登录电子税局进行能力授权确认)" as S3
+    state "State:BILLING_PERSON_ CONFIRMED_PENDING(请<br/>开票员登陆电子税局-乐企进行授权)" as S4
+    state "State:BILLING_PERSON_REGISTER_PENDING(请商户法定代表人/财务负责人登陆电子税局进行开票员设置)" as S5
+    state "state:SECURITY_SETTING_PENDING(请商户法定代表人/财务负责人登陆电子税局进行设置开票安全验证有效期)" as S6
+    state "state:ENABLED(商户数电开票能力，税局接入完成)" as S7
+    state "state:RESOURCE_EXPIRED(商户使用的数电服务商资源过期，请联系数电服务商)" as S8
+    state "state:DISABLED(未接入或商户解除授权，请重新发起力邀请商户确认授权)" as S9
+    state "state:APPROVAL_PENDING(请等待当地税务机关审批)" as S10
+    state "state:APPLY_FAILED(税局申请不通过，请查看接入失败原因)" as S11
+
+    [*] --> S2: 邀请成功税局校验通过
+    [*] --> S10: 邀请成功税局校验不通过
+    S2 --> S3: 商户税局乐企确认
+    S10 --> S2: 税局审批通过
+    S10 --> S11: 税局审批不通过
+    S3 --> S4: 能力授权确认
+    S3 --> S9: 超时未完成
+    S11 --> S10: 重新邀请
+    S4 --> S9: 超时未完成
+    S4 --> S5: 开票员设置完成
+    S9 --> S7: 商户重新申请接入
+    S5 --> S9: 超时未完成
+    S5 --> S6: 开票员确认
+    S7 --> S9: 商户税局乐企解除授权
+    S7 --> S8: 资源过期
+    S6 --> S9: 超时未完成
+    S6 --> S7: 安全过期时间设置
+    S8 --> S7: 付费续期
+```
 
 ### 2.2 设置商户开票配置
 
@@ -371,7 +406,30 @@
 
 ### 2.3 电子发票状态状态机
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/da7f4519eab895b03ab5c4426d8961f3.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "state:ISSUE_ACCEPTED(发票开具中)" as S2
+    state "state:lSSUED(发票开具成功)" as S3
+    state "state:REVERSE_ACCEPTED(冲红申请中)" as S4
+    state "state:REVERSED(冲红成功)" as S5
+    state "state:ISSUE_FAILED(发票开具失败)" as S7
+    state "state:REVERSED_FAILED(冲红失败)" as S8
+
+    [*] --> S2: 申请开具发票
+    S2 --> S3: 发票开具成功
+    S2 --> S7: 发票开具失败
+    S3 --> S4: 申请红冲发票
+    S7 --> S3: 换fapiao_id开票成功
+
+
+
+    S4 --> S5: 发票冲红成功
+    S4 --> S8: 冲红失败
+    S5 --> [*]
+    S8 --> S5: 重试成功
+```
 
 ### 2.4 通过微信支付交易凭证开票
 
```

### 开发指引
- ID: `4012062379`
- 路径: 特约商户进件
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012062379.md
- 更新时间变更: 2025-07-18 10:05:14 -> 2026-06-09 09:45:48
- 本地文件: `pages/4012062379.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -14,11 +16,63 @@
 
 业务流程时序图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/9a92c8ec698f7c71660f15f353200a1d.png)
+```mermaid
+sequenceDiagram
+    autonumber
+    actor 特约商户
+    participant 微信支付服务商
+    participant 微信支付
+
+    rect rgb(255,255,255)
+        %% 进件流程
+        特约商户->>微信支付服务商: 商户提交进件资料
+        微信支付服务商->>微信支付服务商: 审核商户提交资料
+        微信支付服务商->>微信支付: 调用微信支付“提交申请单”接口提交进件资料
+        微信支付-->>微信支付服务商: 返回申请单号
+        微信支付服务商->>微信支付: 调用微信支付“查询申请单状态”接口查询进件状态
+        微信支付-->>微信支付服务商: 返回进件状态
+        微信支付服务商-->>特约商户: 商户获取进件状态
+
+        %% 修改结算账号流程
+        alt 修改结算帐号信息
+            特约商户->>微信支付服务商: 修改商户结算帐号
+            微信支付服务商->>微信支付服务商: 审核过滤帐号信息
+            微信支付服务商->>微信支付: 调用微信支付“修改结算帐号接口”，修改结算信息
+            微信支付-->>微信支付服务商: 返回状态码
+            微信支付服务商-->>特约商户: 获取修改状态
+            特约商户->>微信支付服务商: 查询、核实结算帐号信息
+            微信支付服务商->>微信支付: 调用微信支付“查询结算帐号”接口查询结算帐号
+            微信支付-->>微信支付服务商: 返回查询结果
+            微信支付服务商-->>特约商户: 获取查询结果
+        end
+    end
+```
 
 申请单状态变化如下
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/52cc5c9d54dabb689a91ad2546912400.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "审核中" as S2
+    state "待账户验证" as S3
+    state "待签约" as S4
+    state "开通权限中" as S5
+    state "已完成" as S6
+    state "已驳回" as S8
+
+    [*] --> S2: 提交申请单
+    S2 --> S3: 判断需要账户验证
+    S2 --> S8: 审核驳回
+
+    S3 --> S8: 超时10天未验证
+    S3 --> S4: 完成账号验证
+    S2 --> S4: 判断无需账户验证
+    S8 --> [*]
+    S4 --> S5: 完成签约
+    S5 --> S6: 完成开通权限，可交易
+    S6 --> [*]
+```
 
 重点步骤说明：
 
```

### 开发指引
- ID: `4012064832`
- 路径: 商户开户意愿确认
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012064832.md
- 更新时间变更: 2025-08-13 10:13:13 -> 2026-06-09 09:45:45
- 本地文件: `pages/4012064832.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -14,11 +16,65 @@
 
 #### 业务流程时序图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/44e7cee99bda1ee662dc42f7e56f98f7.png)
+```mermaid
+sequenceDiagram
+    rect rgb(255,255,255)
+        autonumber
+        actor User as 用户
+        participant SP as 服务商后台
+        participant WxPay as 微信支付后台
+
+        User->>SP: 提交商家资料
+        SP->>WxPay: 调用“获取商户开户意愿确认状态”接口查看是否需要认证
+        WxPay->>WxPay: 查验授权状态
+        WxPay-->>SP: 返回授权状态
+
+        alt 商户是否完成开户意愿确认（未授权）
+            SP->>WxPay: 调用“提交申请单”接口提交认证资料
+            WxPay->>WxPay: 生成申请单信息
+            WxPay-->>SP: 返回申请单信息
+            SP->>WxPay: 调用“查询申请单状态”查看认证状态
+            WxPay-->>SP: 返回申请单小程序码
+            SP-->>User: 用户扫码登录微信确认
+            User->>WxPay: 获取微信支付验证码
+            WxPay-->>User: 发送验证码
+            User->>WxPay: 确认验证信息
+
+            loop 用户确认异常
+                User->>WxPay: 确认异常，信息错误
+                WxPay-->>SP: 认证失败，信息有误
+                SP-->>User: 信息错误，需法人授权
+                SP->>WxPay: 撤销申请单
+            end
+
+        end
+    end
+```
 
 申请单状态变化如下：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/df7dcdd09e1e803d65177ed58601cbf8.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "审核中" as S2
+    state "待确认联系信息" as S3
+    state "待账户验证" as S4
+    state "审核通过" as S5
+    state "授权成功" as S6
+    state "已作废" as S8
+
+    [*] --> S2: 平台审核
+    S2 --> S3: 审核通过
+    S2 --> S8: 撤销原申请单
+    S3 --> S8: 撤销原申请单
+    S3 --> S4: 确认无误
+    S8 --> [*]
+    S4 --> S8: 撤销原申请单
+    S4 --> S5: 法人授权
+    S5 --> S6: 门店授权
+    S6 --> [*]
+```
 
 重点步骤说明：
 
```

### 开发指引
- ID: `4012064853`
- 路径: 商户平台处置通知
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012064853.md
- 更新时间变更: 2025-03-21 07:44:39 -> 2026-06-09 09:45:42
- 本地文件: `pages/4012064853.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -12,13 +14,29 @@
 
 ### 3.1. 业务流程图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/5b30496bbf5b1babaeda9a7ef1c51ae9.png)
+```mermaid
+sequenceDiagram
+    autonumber
+    participant 商户
+    participant 微信支付
+
+    rect rgb(255,255,255)
+        %% 设置回调链接
+        商户->>微信支付: 设置回调链接
+        微信支付-->>商户: 设置成功
+
+        %% 回调同步记录
+        微信支付->>商户: 回调: 实时同步商户处置记录
+        微信支付->>商户: 回调: 实时同步商户拦截记录
+        微信支付->>商户: 回调: 实时同步商户申诉记录
+    end
+```
 
 重点步骤说明：
 
-步骤1.1 [创建商户违规通知回调地址](https://pay.weixin.qq.com/doc/v3/partner/4012471333.md) ，调服务商、渠道商、从业机构向微信支付设置回调链接。
+步骤1 [创建商户违规通知回调地址](https://pay.weixin.qq.com/doc/v3/partner/4012471333.md) ，调服务商、渠道商、从业机构向微信支付设置回调链接。
 
-步骤2.1、3.1、4.1 服务商、渠道商、从业机构向微信支付设置回调链接成功后，当有新的违规、拦截（大于10次时）和申诉事件发生申诉单据状态发生变化时，商户会收到实时同步通知回调。
+步骤3、4、5 服务商、渠道商、从业机构向微信支付设置回调链接成功后，当有新的违规、拦截（大于10次时）和申诉事件发生申诉单据状态发生变化时，商户会收到实时同步通知回调。
 
 ## 4. 常见问题
 
```

### 开发指引
- ID: `4012064909`
- 路径: 不活跃商户身份核实
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012064909.md
- 更新时间变更: 2024-12-02 07:22:56 -> 2026-06-09 09:45:41
- 本地文件: `pages/4012064909.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考“[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/partner/4012081673.md)”。
@@ -35,7 +37,34 @@
 
 ### 3.1. 业务序列图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/e86bcb993b4f1c3767012c64c6aa4db7.png)
+```mermaid
+sequenceDiagram
+    autonumber
+    participant 服务商系统
+    participant 微信支付系统
+
+    rect rgb(255,255,255)
+        %% 商户平台处置通知
+        微信支付系统->>服务商系统: 商户平台处置通知
+        服务商系统->>服务商系统: 记录受处置子商户
+        服务商系统-->>微信支付系统: 通知成功
+
+        %% 发起不活跃商户身份核实
+        服务商系统->>服务商系统: 过滤待发起核实商户
+        服务商系统->>微信支付系统: 发起不活跃商户身份核实
+        微信支付系统->>微信支付系统: 生成核实单据
+        微信支付系统-->>服务商系统: 返回核实单单号
+
+        %% 异步执行核实
+        微信支付系统->>微信支付系统: 异步执行核实
+
+        %% 轮询查询核实结果
+        loop 查询结果
+            服务商系统->>微信支付系统: 查询不活跃商户身份核实结果
+            微信支付系统-->>服务商系统: 返回核实单信息
+        end
+    end
+```
 
 ### 3.2. 关键步骤说明
 
```

### 产品介绍
- ID: `4018153750`
- 路径: 平台收付通-电商交易解决方案 > 商户注销
- URL: https://pay.weixin.qq.com/doc/v3/partner/4018153750.md
- 更新时间变更: 2026-02-12 08:25:07 -> 2026-06-11 07:25:17
- 本地文件: `pages/4018153750.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.11
+
 为了提升电商平台二级商户的退出体验，平台收付通对原有的注销及提现流程进行了深度整合，推出了全新的“注销提现”一体化接口。
 
 相较于传统方案，接入新接口的核心价值在于：
@@ -73,7 +75,39 @@
 | `CANCELED` (已注销) | 商户号已注销，如涉及提资，请查看提现状态（withdraw\_state） | 否 |
 | `FINISH` (注销完成) | 如不涉及提资，仅注销商户号，最终会进入此状态；<br>如涉及提资，当银行侧返回成功后，提现成功/提现异常均会走入此状态。如果提现异常，请参考特殊情形3）再次发起提现。 | 是 |
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/543fa9f900eb41b20ad5496196b3f87e.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "已受理-ACCEPTED[1]" as S2
+    state "审核中-REVIEWING[2]" as S3
+    state "审核驳回-REJECTED[3]" as S4
+    state "等待商户确认-WAITING_MERCHANT_CONFIRM[4]" as S6
+    state "已撤销-REVIEWING[5]" as S7
+    state "系统处理中-SYSTEM_PROCESSING[6]" as S8
+    state "已注销-CANCELED[7]" as S9
+    state "资金处理中-WITHDRAW_PROCESS[9]" as S10
+    state "注销完成-FINISH[8]" as S11
+
+    [*] --> S2
+    S2 --> S3
+    S2 --> S6
+    S3 --> S4: 审核驳回
+    S3 --> S10: 审核通过[多次提现场景]
+    S3 --> S8: 审核通过[需注销]
+    S6 --> S8: 商户/平台完成确认
+    S6 --> S7: 超时未确认
+    S4 --> [*]
+    S8 --> S9: 商户号注销
+    note right of S10
+    	涉及提现需查看具体提现状态
+    end note
+    S10 --> S11: 提现异常；提现成功
+    S9 --> S10: [需要提现]
+    S9 --> S11: [仅注销]
+    S11 --> [*]
+    S7 --> [*]
+```
 
 ### 2. 回调通知（强烈建议接入）
 
```

### 开发指引
- ID: `4012088031`
- 路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012088031.md
- 更新时间变更: 2026-03-11 09:00:14 -> 2026-06-10 07:28:44
- 本地文件: `pages/4012088031.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -197,7 +199,54 @@
 
 ### 3.1. 业务流程图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/bb606e8b47edbd271709a7fa93316884.png)
+```mermaid
+sequenceDiagram
+	rect rgb(255,255,255)
+        title sd V3基础支付
+
+        actor 用户
+        participant 微信客户端
+        participant 商户系统后台
+        participant 微信支付系统
+
+        %% 下单与生成支付信息流程
+        用户->>商户系统后台: 1、平台下单, 发起支付()
+        商户系统后台->>商户系统后台: 2、生成平台订单()
+        商户系统后台->>微信支付系统: 3、请求下单接口, 创建订单()
+        微信支付系统->>微信支付系统: 4、生成预付单()
+        微信支付系统-->>商户系统后台: 5、返回预付单标识()
+        商户系统后台->>商户系统后台: 6、生成带签名支付信息()
+
+        %% 拉起支付流程
+        用户->>商户系统后台: 7、发起支付()
+        商户系统后台->>微信客户端: 8、调起微信支付()
+        微信客户端->>微信支付系统: 9、发起支付请求()
+        微信支付系统->>微信支付系统: 10、验证支付授权权限()
+        微信支付系统-->>微信客户端: 11、返回支付授权()
+        用户->>微信客户端: 12、确认支付, 输入密码()
+        微信客户端->>微信支付系统: 13、提交授权()
+        微信支付系统->>微信支付系统: 14、验证授权()
+
+        %% 分支：获取订单支付状态（异步通知）
+        alt 获取订单支付状态
+            微信支付系统->>商户系统后台: 15、异步通知平台支付结果()
+            商户系统后台->>商户系统后台: 16、保存支付通知()
+            商户系统后台-->>微信支付系统: 17、返回告知成功接收处理()
+            微信支付系统-->>微信客户端: 18、返回支付结果, 并发微信信息提醒()
+        end
+
+        %% 支付状态查询流程
+        微信客户端->>商户系统后台: 19、支付状态查询()
+
+        alt 判断支付状态(未收到支付回调通知)
+            商户系统后台->>微信支付系统: 20、调用查单接口, 查询支付结果()
+            微信支付系统-->>商户系统后台: 21、返回支付结果()
+        end
+
+        商户系统后台-->>用户: 22、展示支付消息()
+
+    end
+```
 
 重要步骤说明：
 
```

### 开发指引
- ID: `4012089542`
- 路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012089542.md
- 更新时间变更: 2025-09-26 03:23:41 -> 2026-06-10 07:28:43
- 本地文件: `pages/4012089542.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -199,7 +201,59 @@
 
 ### 3.1. 业务流程图
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/6a2406628b51f4bc9a029cf50541b68c.png)
+```mermaid
+sequenceDiagram
+	rect rgb(255,255,255)
+        title sd 合单支付
+
+        actor 买家
+        participant 微信客户端
+        participant 电商平台
+        participant 电商后台
+        participant 微信支付系统
+
+        %% 1-8 下单与生成支付信息流程
+        买家->>电商平台: 1-(平台下单, 发起支付)
+        电商平台->>电商后台: 2、生成支付订单
+        电商后台->>电商后台: 3-(生成平台订单)
+        电商后台->>微信支付系统: 4-(请求合单下单-APP支付/JS支付接口, 创建订单)
+        微信支付系统->>微信支付系统: 5-(生成预付单)
+        微信支付系统-->>电商后台: 6-(返回预付单标识)
+        电商后台->>电商后台: 7-(生成带签名支付信息)
+        电商后台->>电商平台: 8-(返回支付信息)
+
+        %% 9-16 拉起支付与授权流程
+        买家->>电商平台: 9-(发起支付)
+        电商平台->>微信客户端: 10-(调起微信支付)
+        微信客户端->>微信支付系统: 11-(发起支付请求)
+        微信支付系统->>微信支付系统: 12-(验证支付授权权限)
+        微信支付系统-->>微信客户端: 13-(返回支付授权)
+        买家->>微信客户端: 14-(确认支付, 输入密码)
+        微信客户端->>微信支付系统: 15-(提交授权)
+        微信支付系统->>微信支付系统: 16-(验证授权)
+
+        %% 17-20 异常处理分支
+        alt 异常处理
+            微信支付系统->>电商后台: 17-(异步通知平台支付结果)
+            电商后台->>电商后台: 18-(保存支付通知)
+            电商后台-->>微信支付系统: 19-(返回告知成功接收处理)
+            微信支付系统-->>微信客户端: 20-(返回支付结果, 并发微信信息提醒)
+        end
+
+        %% 21-25 支付状态查询流程
+        微信客户端->>电商平台: 21-(支付状态查询)
+        电商平台->>电商后台: 22-(查询后台商户支付结果)
+
+        alt 查单判断支付结果
+            电商后台->>微信支付系统: 23-(调用合单支付查询, 查询支付结果)
+            微信支付系统-->>电商后台: 24、(返回支付结果)
+        end
+
+        电商后台-->>电商平台: 25-(返回支付结果)
+        电商平台-->>买家: 26-(展示支付消息)
+
+    end
+```
 
 重要步骤说明：
 
```

### 开发指引
- ID: `4012087888`
- 路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账
- URL: https://pay.weixin.qq.com/doc/v3/partner/4012087888.md
- 更新时间变更: 2025-09-26 03:05:59 -> 2026-06-10 07:27:51
- 本地文件: `pages/4012087888.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1. 接口规则
 
 为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
@@ -16,7 +18,48 @@
 
 ### 3.1. 业务流程图-分账
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/4685be72ea23d6aaaa7aab202f0fa302.png)
+```mermaid
+sequenceDiagram
+    autonumber
+    actor 用户
+    participant 电商平台
+    participant 微信支付系统
+    actor 分账接收方
+
+    rect rgb(255,255,255)
+        用户->>电商平台: 用户使用微信支付进行支付
+        电商平台->>微信支付系统: 带上分账标识profit_sharing请求下单并支付
+        微信支付系统->>微信支付系统: 支付交易
+        微信支付系统-->>电商平台: 返回支付结果给电商平台
+
+        电商平台->>微信支付系统: 请求分账
+
+        alt 分账异常
+            微信支付系统->>电商平台: 异步通知平台分账结果
+            电商平台->>微信支付系统: 调用查询分账结果接口，查询分账状态
+            微信支付系统-->>电商平台: 返回查询结果
+        end
+
+        微信支付系统->>分账接收方: 结算资金分给分账接收方
+        微信支付系统-->>电商平台: 分账动账结果通知
+        电商平台->>微信支付系统: 完结分账
+
+        alt 分账后退款
+            用户->>电商平台: 申请订单退款
+            电商平台->>微信支付系统: 调用分账回退接口，请求分账回退
+            微信支付系统->>微信支付系统: 发起分账回退
+
+            alt 异常处理
+                微信支付系统->>电商平台: 异步通知分账回退结果
+                电商平台->>微信支付系统: 请求查询分账回退接口，查询分账回退状态
+                微信支付系统-->>电商平台: 返回分账回退结果
+            end
+
+            分账接收方->>电商平台: 资金回退
+            电商平台->>用户: 退款
+        end
+    end
+```
 
 重要步骤说明：
 
```

### 业务示例代码
- ID: `4015870957`
- 路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015870957.md
- 更新时间变更: 2025-09-26 03:05:59 -> 2026-06-09 09:46:47
- 本地文件: `pages/4015870957.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.09
+
 ## 1. 分账
 
 通过分账接口，根据实际业务场景将交易款项分账到其他业务参与方的账户(如：平台抽取佣金)，目前默认最高分账比例30%；同时通过该接口，实现合单交易冻结资金的解冻，从而实现对二级商户的账期管理和资金分配。
@@ -58,11 +60,34 @@
 
 分账单状态：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/278dcf40f1e200231fefd62b700f2cb3.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "PROCESSING(1)" as S1
+    state "FINISHED(2)" as S2
+
+    [*] --> S1
+    S1 --> S2
+    S2 --> [*]
+```
 
 分账接收方分账结果：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/08b88115ea01ffb7b73b0e7bd7102d70.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "CLOSED(3)" as S2
+    state "SUCCESS(2)" as S3
+    state "PEDDING(1)" as S4
+
+    [*] --> S4
+    S4 --> S3
+    S4 --> S2
+    S3 --> [*]
+    S2 --> [*]
+```
 
 ```
 package com.java.ecommerce.profitsharing;
@@ -475,7 +500,20 @@
 
 分账回退单状态机：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/d5610b2746094c7359f94f9974b4209e.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "FAILED(3)" as S2
+    state "SUCCESS(2)" as S3
+    state "PROCESSING(1)" as S4
+
+    [*] --> S4
+    S4 --> S3
+    S4 --> S2
+    S3 --> [*]
+    S2 --> [*]
+```
 
 ```
 package com.java.ecommerce.profitsharing;
```

### 业务示例代码
- ID: `4015593692`
- 路径: 平台收付通-电商交易解决方案 > 补差与分账 > 补差
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015593692.md
- 更新时间变更: 2025-10-24 06:49:13 -> 2026-06-10 07:27:50
- 本地文件: `pages/4015593692.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1. 目标
 
 通过本教程的学习，你应该可以通过微信支付补差的API完成补差业务，API操作包括：
@@ -30,7 +32,20 @@
 
 补差单的状态机：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/134e4d88d61b7ba3fe7c8fd1409c049a.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "SUCCESS[1]" as S2
+    state "FAIL[2]" as S4
+    state "REFUND[3]" as S5
+
+    [*] --> S2: 补差成功
+    [*] --> S4: 补差失败
+    S2 --> [*]
+    S4 --> S5: 系统自动补差回退成功
+    S5 --> [*]
+```
 
 ```
 package com.java.demo.subsidy;
@@ -236,7 +251,18 @@
 
 补差回退单状态：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/95ebcbe8230008ad88aa6a2f1000d7b1.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "SUCCESS[1]" as S2
+    state "FAIL[2]" as S4
+
+    [*] --> S2: 补差回退成功
+    [*] --> S4: 补差回退失败并且重试超过7天都未成功
+    S2 --> [*]
+    S4 --> [*]
+```
 
 ```
 package com.java.demo.subsidy;
```

### 业务示例代码
- ID: `4015217874`
- 路径: 平台收付通-电商交易解决方案 > 交易退款
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015217874.md
- 更新时间变更: 2025-10-15 07:52:29 -> 2026-06-10 07:27:49
- 本地文件: `pages/4015217874.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1. 目标
 
 通过本教程的学习，你应该可以：
@@ -204,7 +206,23 @@
 
 退款单的状态机：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/a274a0b9f5ec3aadb6546cd5fb1fc4ff.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "PROCESSING[1]" as S2
+    state "ABNORMAL[2]" as S3
+    state "SUCCESS[3]" as S4
+    state "CLOSED[4]" as S6
+
+    [*] --> S2: 商户申请退款
+    S2 --> S3: 商户发起异常退款
+    S2 --> S4: 退款到账
+    S2 --> S6: 系统自动关单[商户余额不足超过期限]
+    S3 --> S2: 用户异常
+    S4 --> [*]
+    S6 --> [*]
+```
 
 ### 2.2.1 按商户退款单号查询单笔退款
 
```

### 业务示例代码
- ID: `4019899593`
- 路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现
- URL: https://pay.weixin.qq.com/doc/v3/partner/4019899593.md
- 更新时间变更: 2026-04-23 06:48:35 -> 2026-06-10 07:27:45
- 本地文件: `pages/4019899593.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1. 目标
 
 通过本教程的学习，你应该可以：
@@ -27,11 +29,46 @@
 
 收付通平台预约提现/二级商户预约提现单状态流转
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/9c3c7af5c0f8468843b091921913e3a4.jpeg)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "status：INIT（已建单）" as S2
+    state "status：CREATE_SUCCESS（已受理）" as S3
+    state "status：CLOSE（关单）" as S4
+    state "status：SUCCESS（成功）" as S5
+    state "status：FAIL（失败）" as S6
+    state "status：REFUND（退票）" as S7
+
+    [*] --> S2: 提交提现
+    S2 --> S3: 受理成功
+    S3 --> S4: 关单
+    S3 --> S5: 提现成功
+    S3 --> S6: 提现失败
+    S4 --> [*]
+    S5 --> S7: 银行退票
+    S6 --> [*]
+    S7 --> [*]
+```
 
 二级商户按日终余额预约提现单状态流转
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/9e39e248ebbcba5431b58f08adcfcafc.jpeg)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "status：CREATED（已建单）" as S2
+    state "status：PROCESSING（处理中）" as S3
+    state "status：FINISHED（提现成功）" as S4
+    state "status：ABNORMAL（提现异常）" as S5
+
+    [*] --> S2: 提交提现
+    S2 --> S3: 受理成功
+    S3 --> S4: 提现成功
+    S3 --> S5: 提现异常（如余额不足、风控拦截、结算银行卡有误等）
+    S4 --> S5: 银行退票
+    S5 --> [*]
+```
 
 #### 平台自身提现
 
```

### 业务示例代码
- ID: `4015593257`
- 路径: 平台收付通-电商交易解决方案 > 跨境付款
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015593257.md
- 更新时间变更: 2025-09-26 03:22:00 -> 2026-06-10 07:27:44
- 本地文件: `pages/4015593257.md`

```diff
--- old.md
+++ new.md
@@ -1,3 +1,5 @@
+>更新时间：2026.06.10
+
 ## 1. 目标
 
 通过本教程的学习，你应该可以通过微信支付跨境付款的API完成跨境付款业务，API操作包括：
@@ -26,7 +28,20 @@
 
 资金出境单据状态机：
 
-![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/f587f0add20b2e88cb7b485e2d09f9ff.png)
+```mermaid
+%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
+stateDiagram-v2
+    direction LR
+    state "ACCEPT[1]" as S2
+    state "SUCCESS[2]" as S3
+    state "FAIL[3]" as S4
+
+    [*] --> S2: 商户申请资金出境
+    S2 --> S3: 资金出境成功
+    S2 --> S4: 资金出境失败[风控拦截、商户被冻结等]
+    S3 --> [*]
+    S4 --> [*]
+```
 
 ```
 package com.java.demo.funds2oversea;
```

## 拉取失败

- 开发指引 (`4012166834`): https://pay.weixin.qq.com/doc/v3/partner/4012166834.md

## 附录：所有页面清单

<details>
<summary>点击查看全部 862 个页面</summary>

| 序号 | 标题（链接） | ID | 更新时间 | 完整路径 |
|------|-------------|----|----------|----------|
| 1 | [商品券接入Skill](pages/4018929846.md) | `4018929846` | 2026-04-09 02:43:55 | Skills |
| 2 | [基础支付接入Skill](pages/4019636341.md) | `4019636341` | 2026-04-09 03:11:59 | Skills |
| 3 | [Go](pages/4015119446.md) | `4015119446` | 2025-05-29 03:20:44 | 示例代码 |
| 4 | [Java](pages/4014985777.md) | `4014985777` | 2025-05-27 08:03:58 | 示例代码 |
| 5 | [付款码支付（V2）](pages/4012851192.md) | `4012851192` | 2025-04-25 07:54:10 | 付款码支付（V2） |
| 6 | [刷脸支付](pages/4012851199.md) | `4012851199` | 2024-10-28 07:53:13 | 刷脸支付 |
| 7 | [产品介绍](pages/4012069852.md) | `4012069852` | 2026-05-21 03:22:54 | JSAPI支付 |
| 8 | [开发接入准备](pages/4012069853.md) | `4012069853` | 2026-05-19 08:35:53 | JSAPI支付 |
| 9 | [开发指引](pages/4012069859.md) | `4012069859` | 2026-06-09 09:46:17 | JSAPI支付 |
| 10 | [常见问题](pages/4013334850.md) | `4013334850` | 2026-05-19 07:37:15 | JSAPI支付 |
| 11 | [JSAPI/小程序下单](pages/4012738519.md) | `4012738519` | 2025-03-31 06:14:54 | JSAPI支付 > API列表 |
| 12 | [JSAPI调起支付](pages/4012069855.md) | `4012069855` | 2025-02-26 07:08:25 | JSAPI支付 > API列表 |
| 13 | [微信支付订单号查询订单](pages/4012738964.md) | `4012738964` | 2025-01-16 07:08:59 | JSAPI支付 > API列表 |
| 14 | [关闭订单](pages/4012739019.md) | `4012739019` | 2025-01-16 07:08:55 | JSAPI支付 > API列表 |
| 15 | [支付成功回调通知](pages/4012085146.md) | `4012085146` | 2025-02-20 03:15:13 | JSAPI支付 > API列表 |
| 16 | [商户订单号查询订单](pages/4012739008.md) | `4012739008` | 2025-01-16 07:08:54 | JSAPI支付 > API列表 |
| 17 | [申请退款](pages/4012739034.md) | `4012739034` | 2025-01-16 07:08:56 | JSAPI支付 > API列表 |
| 18 | [查询单笔退款（按商户退款单号）](pages/4012739043.md) | `4012739043` | 2025-01-16 07:08:57 | JSAPI支付 > API列表 |
| 19 | [发起异常退款](pages/4013335389.md) | `4013335389` | 2025-01-16 07:08:52 | JSAPI支付 > API列表 |
| 20 | [退款结果回调通知](pages/4012085298.md) | `4012085298` | 2025-02-20 03:14:52 | JSAPI支付 > API列表 |
| 21 | [申请所有/单个子商户交易账单](pages/4012739068.md) | `4012739068` | 2025-01-16 07:08:51 | JSAPI支付 > API列表 |
| 22 | [申请服务商资金账单](pages/4012739125.md) | `4012739125` | 2025-01-16 07:08:50 | JSAPI支付 > API列表 |
| 23 | [下载账单](pages/4012085421.md) | `4012085421` | 2024-12-23 03:48:08 | JSAPI支付 > API列表 |
| 24 | [管理商户号绑定的APPID账号](pages/4013335081.md) | `4013335081` | 2024-12-23 08:19:22 | JSAPI支付 > 附录 |
| 25 | [配置JSAPI支付授权目录](pages/4013335127.md) | `4013335127` | 2024-12-20 08:32:45 | JSAPI支付 > 附录 |
| 26 | [产品介绍](pages/4013080227.md) | `4013080227` | 2026-05-21 03:24:50 | APP支付 |
| 27 | [开发接入准备](pages/4013080228.md) | `4013080228` | 2026-05-19 08:36:11 | APP支付 |
| 28 | [开发指引](pages/4013080246.md) | `4013080246` | 2026-06-09 09:46:14 | APP支付 |
| 29 | [常见问题](pages/4013080245.md) | `4013080245` | 2026-05-21 03:25:44 | APP支付 |
| 30 | [APP下单](pages/4013080231.md) | `4013080231` | 2025-03-31 06:14:51 | APP支付 > API列表 |
| 31 | [APP调起支付](pages/4013080233.md) | `4013080233` | 2025-02-18 08:14:07 | APP支付 > API列表 |
| 32 | [微信支付订单号查询订单](pages/4013080234.md) | `4013080234` | 2025-01-16 07:08:59 | APP支付 > API列表 |
| 33 | [商户订单号查询订单](pages/4013080235.md) | `4013080235` | 2025-01-16 07:08:54 | APP支付 > API列表 |
| 34 | [关闭订单](pages/4013080236.md) | `4013080236` | 2025-01-16 07:08:55 | APP支付 > API列表 |
| 35 | [支付成功回调通知](pages/4013080237.md) | `4013080237` | 2025-01-14 02:26:27 | APP支付 > API列表 |
| 36 | [申请退款](pages/4013080238.md) | `4013080238` | 2025-01-16 07:08:56 | APP支付 > API列表 |
| 37 | [查询单笔退款（按商户退款单号）](pages/4013080239.md) | `4013080239` | 2025-01-16 07:08:57 | APP支付 > API列表 |
| 38 | [发起异常退款](pages/4013080240.md) | `4013080240` | 2025-01-16 07:08:52 | APP支付 > API列表 |
| 39 | [退款结果通知](pages/4013080241.md) | `4013080241` | 2024-12-30 07:47:39 | APP支付 > API列表 |
| 40 | [申请所有/单个子商户交易账单](pages/4013080242.md) | `4013080242` | 2025-01-16 07:08:51 | APP支付 > API列表 |
| 41 | [申请服务商资金账单](pages/4013080243.md) | `4013080243` | 2025-01-16 07:08:50 | APP支付 > API列表 |
| 42 | [下载账单](pages/4013080230.md) | `4013080230` | 2024-12-23 03:48:08 | APP支付 > API列表 |
| 43 | [管理商户号绑定的APPID账号](pages/4013357894.md) | `4013357894` | 2024-12-24 02:07:53 | APP支付 > 附录 |
| 44 | [OpenSDK接入指南](pages/4013369798.md) | `4013369798` | 2024-12-25 10:48:19 | APP支付 > 附录 |
| 45 | [产品介绍](pages/4012074916.md) | `4012074916` | 2026-05-21 03:26:43 | H5支付 |
| 46 | [开发接入准备](pages/4012074917.md) | `4012074917` | 2026-05-19 08:36:25 | H5支付 |
| 47 | [开发指引](pages/4012074915.md) | `4012074915` | 2026-06-09 09:46:10 | H5支付 |
| 48 | [常见问题](pages/4013336079.md) | `4013336079` | 2025-10-15 08:12:08 | H5支付 |
| 49 | [H5下单](pages/4012738604.md) | `4012738604` | 2025-03-31 06:14:50 | H5支付 > API列表 |
| 50 | [H5调起支付](pages/4012085683.md) | `4012085683` | 2024-12-23 02:14:31 | H5支付 > API列表 |
| 51 | [支付成功回调通知](pages/4012085680.md) | `4012085680` | 2025-02-20 03:15:13 | H5支付 > API列表 |
| 52 | [微信支付订单号查询订单](pages/4012738969.md) | `4012738969` | 2025-01-16 07:08:59 | H5支付 > API列表 |
| 53 | [商户订单号查询订单](pages/4012759661.md) | `4012759661` | 2025-01-16 07:08:54 | H5支付 > API列表 |
| 54 | [关闭订单](pages/4012759669.md) | `4012759669` | 2025-01-16 07:08:55 | H5支付 > API列表 |
| 55 | [申请退款](pages/4012759673.md) | `4012759673` | 2025-01-16 07:08:56 | H5支付 > API列表 |
| 56 | [查询单笔退款（通过商户退款单号）](pages/4012759680.md) | `4012759680` | 2025-01-16 07:08:57 | H5支付 > API列表 |
| 57 | [发起异常退款](pages/4013351901.md) | `4013351901` | 2025-01-16 07:08:52 | H5支付 > API列表 |
| 58 | [退款结果通知](pages/4012085681.md) | `4012085681` | 2025-02-20 03:14:52 | H5支付 > API列表 |
| 59 | [申请所有/单个子商户交易账单](pages/4012759683.md) | `4012759683` | 2025-01-16 07:08:51 | H5支付 > API列表 |
| 60 | [申请服务商资金账单](pages/4012759690.md) | `4012759690` | 2025-01-16 07:08:50 | H5支付 > API列表 |
| 61 | [下载账单](pages/4012085682.md) | `4012085682` | 2024-12-23 03:48:08 | H5支付 > API列表 |
| 62 | [管理商户号绑定的APPID账号](pages/4013336007.md) | `4013336007` | 2024-12-23 08:19:20 | H5支付 > 附录 |
| 63 | [配置H5支付域名](pages/4013336019.md) | `4013336019` | 2026-01-09 08:20:43 | H5支付 > 附录 |
| 64 | [H5收银台适老化字体规范](pages/4013358769.md) | `4013358769` | 2024-12-24 03:30:20 | H5支付 > 附录 |
| 65 | [获取用户ip指引](pages/4018675960.md) | `4018675960` | 2026-03-13 07:56:12 | H5支付 > 附录 |
| 66 | [产品介绍](pages/4012076267.md) | `4012076267` | 2026-05-21 03:28:32 | Native支付 |
| 67 | [开发接入准备](pages/4012076268.md) | `4012076268` | 2026-05-19 08:36:38 | Native支付 |
| 68 | [开发指引](pages/4012076269.md) | `4012076269` | 2026-06-09 09:46:06 | Native支付 |
| 69 | [常见问题](pages/4013352076.md) | `4013352076` | 2026-05-21 03:29:23 | Native支付 |
| 70 | [Native下单](pages/4012738659.md) | `4012738659` | 2025-03-31 06:15:38 | Native支付 > API列表 |
| 71 | [Native调起支付](pages/4012085878.md) | `4012085878` | 2025-03-21 07:41:33 | Native支付 > API列表 |
| 72 | [支付成功回调通知](pages/4012085875.md) | `4012085875` | 2025-02-20 03:15:13 | Native支付 > API列表 |
| 73 | [关闭订单](pages/4012759725.md) | `4012759725` | 2025-01-16 07:08:55 | Native支付 > API列表 |
| 74 | [微信支付订单号查询订单](pages/4012738971.md) | `4012738971` | 2025-01-16 07:08:59 | Native支付 > API列表 |
| 75 | [商户订单号查询订单](pages/4012759714.md) | `4012759714` | 2025-01-16 07:08:54 | Native支付 > API列表 |
| 76 | [申请退款](pages/4012759727.md) | `4012759727` | 2025-01-16 07:08:56 | Native支付 > API列表 |
| 77 | [查询单笔退款（通过商户退款单号）](pages/4012759733.md) | `4012759733` | 2025-01-16 07:08:57 | Native支付 > API列表 |
| 78 | [发起异常退款](pages/4013352066.md) | `4013352066` | 2025-01-16 07:08:52 | Native支付 > API列表 |
| 79 | [退款结果回调通知](pages/4012085876.md) | `4012085876` | 2025-02-20 03:14:52 | Native支付 > API列表 |
| 80 | [申请所有/单个子商户交易账单](pages/4012759737.md) | `4012759737` | 2025-01-16 07:08:51 | Native支付 > API列表 |
| 81 | [申请服务商资金账单](pages/4012759741.md) | `4012759741` | 2025-01-16 07:08:50 | Native支付 > API列表 |
| 82 | [下载账单](pages/4012085877.md) | `4012085877` | 2024-12-23 03:48:08 | Native支付 > API列表 |
| 83 | [管理商户号绑定的APPID账号](pages/4013352075.md) | `4013352075` | 2024-12-23 07:21:48 | Native支付 > 附录 |
| 84 | [产品介绍](pages/4012085810.md) | `4012085810` | 2026-05-21 03:31:05 | 小程序支付 |
| 85 | [开发接入准备](pages/4012076731.md) | `4012076731` | 2026-05-19 08:36:53 | 小程序支付 |
| 86 | [开发指引](pages/4012076732.md) | `4012076732` | 2026-06-09 09:46:05 | 小程序支付 |
| 87 | [常见问题](pages/4013352071.md) | `4013352071` | 2026-05-09 08:54:44 | 小程序支付 |
| 88 | [JSAPI/小程序下单](pages/4012759974.md) | `4012759974` | 2025-03-31 06:14:54 | 小程序支付 > API列表 |
| 89 | [小程序调起支付](pages/4012085827.md) | `4012085827` | 2025-02-26 07:10:30 | 小程序支付 > API列表 |
| 90 | [支付成功回调通知](pages/4012085801.md) | `4012085801` | 2025-02-20 03:15:13 | 小程序支付 > API列表 |
| 91 | [关闭订单](pages/4012760108.md) | `4012760108` | 2025-01-16 07:08:55 | 小程序支付 > API列表 |
| 92 | [微信支付订单号查询订单](pages/4012738973.md) | `4012738973` | 2025-01-16 07:08:59 | 小程序支付 > API列表 |
| 93 | [商户订单号查询订单](pages/4012760115.md) | `4012760115` | 2025-01-16 07:08:54 | 小程序支付 > API列表 |
| 94 | [申请退款](pages/4012760121.md) | `4012760121` | 2025-01-16 07:08:56 | 小程序支付 > API列表 |
| 95 | [查询单笔退款（通过商户退款单号）](pages/4012760128.md) | `4012760128` | 2025-01-16 07:08:57 | 小程序支付 > API列表 |
| 96 | [发起异常退款](pages/4013352278.md) | `4013352278` | 2025-01-16 07:08:52 | 小程序支付 > API列表 |
| 97 | [退款结果回调通知](pages/4012085802.md) | `4012085802` | 2025-02-20 03:14:52 | 小程序支付 > API列表 |
| 98 | [申请所有/单个子商户交易账单](pages/4012760132.md) | `4012760132` | 2025-01-16 07:08:51 | 小程序支付 > API列表 |
| 99 | [申请服务商资金账单](pages/4012760136.md) | `4012760136` | 2025-01-16 07:08:50 | 小程序支付 > API列表 |
| 100 | [下载账单](pages/4012085803.md) | `4012085803` | 2024-12-23 03:48:08 | 小程序支付 > API列表 |
| 101 | [管理商户号绑定的APPID账号](pages/4013352070.md) | `4013352070` | 2024-12-23 07:21:48 | 小程序支付 > 附录 |
| 102 | [产品介绍](pages/4012079332.md) | `4012079332` | 2026-05-21 08:20:51 | JSAPI合单支付 |
| 103 | [开发指引](pages/4012166834.md) | `4012166834` | 2026-06-09 09:46:02 | JSAPI合单支付 |
| 104 | [开发接入准备](pages/4013461849.md) | `4013461849` | 2026-05-21 08:21:02 | JSAPI合单支付 |
| 105 | [常见问题](pages/4013462212.md) | `4013462212` | 2025-01-16 08:45:12 | JSAPI合单支付 |
| 106 | [JSAPI合单下单](pages/4012757938.md) | `4012757938` | 2025-01-16 08:23:18 | JSAPI合单支付 > API列表 |
| 107 | [JSAPI调起支付](pages/4012166844.md) | `4012166844` | 2025-02-19 03:55:15 | JSAPI合单支付 > API列表 |
| 108 | [查询合单订单](pages/4013462164.md) | `4013462164` | 2025-01-17 07:39:30 | JSAPI合单支付 > API列表 |
| 109 | [关闭合单订单](pages/4013462171.md) | `4013462171` | 2025-01-16 08:23:11 | JSAPI合单支付 > API列表 |
| 110 | [合单订单支付成功回调通知](pages/4013462175.md) | `4013462175` | 2025-01-16 06:38:52 | JSAPI合单支付 > API列表 |
| 111 | [申请退款](pages/4013462183.md) | `4013462183` | 2025-01-16 07:08:56 | JSAPI合单支付 > API列表 |
| 112 | [查询单笔退款（按商户退款单号）](pages/4013462188.md) | `4013462188` | 2025-01-16 07:08:57 | JSAPI合单支付 > API列表 |
| 113 | [发起异常退款](pages/4013462191.md) | `4013462191` | 2025-01-16 07:08:52 | JSAPI合单支付 > API列表 |
| 114 | [退款结果通知](pages/4013462195.md) | `4013462195` | 2025-01-16 06:38:47 | JSAPI合单支付 > API列表 |
| 115 | [申请所有/单个子商户交易账单](pages/4013462197.md) | `4013462197` | 2025-01-16 07:08:51 | JSAPI合单支付 > API列表 |
| 116 | [申请服务商资金账单](pages/4013462202.md) | `4013462202` | 2025-01-16 07:08:50 | JSAPI合单支付 > API列表 |
| 117 | [下载账单](pages/4013462207.md) | `4013462207` | 2025-01-16 06:38:43 | JSAPI合单支付 > API列表 |
| 118 | [合单支付-商户号绑定APPID操作说明](pages/4013462628.md) | `4013462628` | 2025-01-16 06:39:56 | JSAPI合单支付 > 附录 |
| 119 | [产品介绍](pages/4012079331.md) | `4012079331` | 2026-05-21 03:36:02 | APP合单支付 |
| 120 | [开发指引](pages/4012166832.md) | `4012166832` | 2026-06-09 09:45:58 | APP合单支付 |
| 121 | [常见问题](pages/4013461863.md) | `4013461863` | 2025-01-16 08:45:12 | APP合单支付 |
| 122 | [APP合单下单](pages/4012758021.md) | `4012758021` | 2025-01-16 08:23:20 | APP合单支付 > API列表 |
| 123 | [APP调起支付](pages/4012166845.md) | `4012166845` | 2025-03-28 10:57:37 | APP合单支付 > API列表 |
| 124 | [查询合单订单](pages/4012761057.md) | `4012761057` | 2025-01-17 07:39:30 | APP合单支付 > API列表 |
| 125 | [关闭合单订单](pages/4012761079.md) | `4012761079` | 2025-01-16 08:23:11 | APP合单支付 > API列表 |
| 126 | [合单订单支付成功回调通知](pages/4012231898.md) | `4012231898` | 2025-01-14 09:59:26 | APP合单支付 > API列表 |
| 127 | [申请退款](pages/4012760207.md) | `4012760207` | 2025-01-16 07:08:56 | APP合单支付 > API列表 |
| 128 | [查询单笔退款（通过商户退款单号）](pages/4012760226.md) | `4012760226` | 2025-01-16 07:08:57 | APP合单支付 > API列表 |
| 129 | [发起异常退款](pages/4013461907.md) | `4013461907` | 2025-01-16 07:08:52 | APP合单支付 > API列表 |
| 130 | [退款结果回调通知](pages/4012231901.md) | `4012231901` | 2025-02-20 03:14:52 | APP合单支付 > API列表 |
| 131 | [申请所有/单个子商户交易账单](pages/4012760228.md) | `4012760228` | 2025-01-16 07:08:51 | APP合单支付 > API列表 |
| 132 | [申请服务商资金账单](pages/4012760229.md) | `4012760229` | 2025-01-16 07:08:50 | APP合单支付 > API列表 |
| 133 | [下载账单](pages/4012231933.md) | `4012231933` | 2025-01-16 06:39:27 | APP合单支付 > API列表 |
| 134 | [产品介绍](pages/4013462080.md) | `4013462080` | 2026-05-21 03:35:18 | H5合单支付 |
| 135 | [开发指引](pages/4012166833.md) | `4012166833` | 2026-06-09 09:45:46 | H5合单支付 |
| 136 | [常见问题](pages/4013462145.md) | `4013462145` | 2025-01-16 08:45:12 | H5合单支付 |
| 137 | [H5合单下单](pages/4012758208.md) | `4012758208` | 2025-01-16 08:23:19 | H5合单支付 > API列表 |
| 138 | [H5调起支付](pages/4012166846.md) | `4012166846` | 2025-01-16 06:38:59 | H5合单支付 > API列表 |
| 139 | [查询合单订单](pages/4013462099.md) | `4013462099` | 2025-01-17 07:39:30 | H5合单支付 > API列表 |
| 140 | [关闭合单订单](pages/4013462102.md) | `4013462102` | 2025-01-16 08:23:11 | H5合单支付 > API列表 |
| 141 | [合单订单支付成功回调通知](pages/4013462105.md) | `4013462105` | 2025-01-16 06:39:18 | H5合单支付 > API列表 |
| 142 | [申请退款](pages/4013462113.md) | `4013462113` | 2025-01-16 07:08:56 | H5合单支付 > API列表 |
| 143 | [查询单笔退款（按商户退款单号）](pages/4013462116.md) | `4013462116` | 2025-01-16 07:08:57 | H5合单支付 > API列表 |
| 144 | [发起异常退款](pages/4013462123.md) | `4013462123` | 2025-01-16 07:08:52 | H5合单支付 > API列表 |
| 145 | [退款结果通知](pages/4013462126.md) | `4013462126` | 2025-01-16 06:39:13 | H5合单支付 > API列表 |
| 146 | [申请所有/单个子商户交易账单](pages/4013462129.md) | `4013462129` | 2025-01-16 07:08:51 | H5合单支付 > API列表 |
| 147 | [申请服务商资金账单](pages/4013462134.md) | `4013462134` | 2025-01-16 07:08:50 | H5合单支付 > API列表 |
| 148 | [下载账单](pages/4013462137.md) | `4013462137` | 2025-01-16 06:39:09 | H5合单支付 > API列表 |
| 149 | [产品介绍](pages/4012079333.md) | `4012079333` | 2026-05-21 03:33:32 | Native合单支付 |
| 150 | [开发指引](pages/4012166835.md) | `4012166835` | 2026-06-09 09:45:53 | Native合单支付 |
| 151 | [常见问题](pages/4013462413.md) | `4013462413` | 2025-01-16 08:45:12 | Native合单支付 |
| 152 | [Native合单下单](pages/4012758240.md) | `4012758240` | 2025-01-16 08:23:16 | Native合单支付 > API列表 |
| 153 | [Native调起支付](pages/4012166843.md) | `4012166843` | 2025-03-21 07:39:13 | Native合单支付 > API列表 |
| 154 | [查询合单订单](pages/4013462240.md) | `4013462240` | 2025-01-17 07:39:30 | Native合单支付 > API列表 |
| 155 | [关闭合单订单](pages/4013462247.md) | `4013462247` | 2025-01-16 08:23:11 | Native合单支付 > API列表 |
| 156 | [合单订单支付成功回调通知](pages/4013462250.md) | `4013462250` | 2025-01-16 06:40:25 | Native合单支付 > API列表 |
| 157 | [申请退款](pages/4013462256.md) | `4013462256` | 2025-01-16 07:08:56 | Native合单支付 > API列表 |
| 158 | [查询单笔退款（按商户退款单号）](pages/4013462260.md) | `4013462260` | 2025-01-16 07:08:57 | Native合单支付 > API列表 |
| 159 | [发起异常退款](pages/4013462286.md) | `4013462286` | 2025-01-16 07:08:52 | Native合单支付 > API列表 |
| 160 | [退款结果回调通知](pages/4013462327.md) | `4013462327` | 2025-01-16 06:40:21 | Native合单支付 > API列表 |
| 161 | [申请所有/单个子商户交易账单](pages/4013462343.md) | `4013462343` | 2025-01-16 07:08:51 | Native合单支付 > API列表 |
| 162 | [申请服务商资金账单](pages/4013462358.md) | `4013462358` | 2025-01-16 07:08:50 | Native合单支付 > API列表 |
| 163 | [下载账单](pages/4013462389.md) | `4013462389` | 2025-01-16 06:40:18 | Native合单支付 > API列表 |
| 164 | [产品介绍](pages/4012079334.md) | `4012079334` | 2026-05-21 03:36:27 | 小程序合单支付 |
| 165 | [开发指引](pages/4012166836.md) | `4012166836` | 2026-06-09 09:45:44 | 小程序合单支付 |
| 166 | [常见问题](pages/4013462619.md) | `4013462619` | 2025-09-19 01:41:14 | 小程序合单支付 |
| 167 | [小程序合单下单](pages/4012758246.md) | `4012758246` | 2025-01-16 08:23:15 | 小程序合单支付 > API列表 |
| 168 | [小程序调起支付](pages/4012166847.md) | `4012166847` | 2025-01-16 06:40:11 | 小程序合单支付 > API列表 |
| 169 | [查询合单订单](pages/4013462520.md) | `4013462520` | 2025-01-17 07:39:30 | 小程序合单支付 > API列表 |
| 170 | [关闭合单订单](pages/4013462566.md) | `4013462566` | 2025-01-16 08:23:11 | 小程序合单支付 > API列表 |
| 171 | [合单订单支付成功回调通知](pages/4013462574.md) | `4013462574` | 2025-01-16 06:40:08 | 小程序合单支付 > API列表 |
| 172 | [申请退款](pages/4013462579.md) | `4013462579` | 2025-01-16 07:08:56 | 小程序合单支付 > API列表 |
| 173 | [查询单笔退款（按商户退款单号）](pages/4013462581.md) | `4013462581` | 2025-01-16 07:08:57 | 小程序合单支付 > API列表 |
| 174 | [发起异常退款](pages/4013462582.md) | `4013462582` | 2025-01-16 07:08:52 | 小程序合单支付 > API列表 |
| 175 | [退款结果回调通知](pages/4013462586.md) | `4013462586` | 2025-09-16 08:50:44 | 小程序合单支付 > API列表 |
| 176 | [申请所有/单个子商户交易账单](pages/4013462604.md) | `4013462604` | 2025-01-16 07:08:51 | 小程序合单支付 > API列表 |
| 177 | [申请服务商资金账单](pages/4013462607.md) | `4013462607` | 2025-01-16 07:08:50 | 小程序合单支付 > API列表 |
| 178 | [下载账单](pages/4013462614.md) | `4013462614` | 2025-01-16 06:39:58 | 小程序合单支付 > API列表 |
| 179 | [产品介绍](pages/4016824698.md) | `4016824698` | 2026-06-08 09:46:22 | 医保支付（服务商模式） |
| 180 | [开发接入准备](pages/4016824704.md) | `4016824704` | 2026-05-20 06:20:32 | 医保支付（服务商模式） |
| 181 | [开发指引](pages/4017149893.md) | `4017149893` | 2026-05-20 07:14:26 | 医保支付（服务商模式） |
| 182 | [医保自费混合收款下单](pages/4012503131.md) | `4012503131` | 2025-12-05 03:00:28 | 医保支付（服务商模式） > API列表 > 医保自费混合订单 |
| 183 | [使用医保自费混合订单号查看下单结果](pages/4012503155.md) | `4012503155` | 2025-12-05 02:58:26 | 医保支付（服务商模式） > API列表 > 医保自费混合订单 |
| 184 | [使用服务商订单号查看下单结果](pages/4012503286.md) | `4012503286` | 2026-04-17 08:57:34 | 医保支付（服务商模式） > API列表 > 医保自费混合订单 |
| 185 | [小程序调起医保自费混合支付](pages/4012166993.md) | `4012166993` | 2024-10-25 06:46:01 | 医保支付（服务商模式） > API列表 > 医保自费混合订单 |
| 186 | [JSAPI调起医保自费混合支付](pages/4012809233.md) | `4012809233` | 2024-10-25 06:46:01 | 医保支付（服务商模式） > API列表 > 医保自费混合订单 |
| 187 | [医保混合收款成功通知](pages/4012165722.md) | `4012165722` | 2024-10-25 06:46:01 | 医保支付（服务商模式） > API列表 > 医保自费混合订单 |
| 188 | [医保退款通知](pages/4012166534.md) | `4012166534` | 2025-12-05 02:58:45 | 医保支付（服务商模式） > API列表 > 医保退款 |
| 189 | [报错排查指引](pages/4020401184.md) | `4020401184` | 2026-05-14 09:13:41 | 医保支付（服务商模式） > 常见问题 |
| 190 | [业务&接口规则类问题](pages/4017415847.md) | `4017415847` | 2026-05-14 09:14:42 | 医保支付（服务商模式） > 常见问题 |
| 191 | [申请医保支付权限](pages/4016971494.md) | `4016971494` | 2026-05-20 06:32:45 | 医保支付（服务商模式） > 附录 |
| 192 | [接入医保亲情付指引](pages/4016970670.md) | `4016970670` | 2026-05-20 06:23:29 | 医保支付（服务商模式） > 附录 |
| 193 | [UI规范与页面说明](pages/4021595914.md) | `4021595914` | 2026-06-08 09:46:27 | 医保支付（服务商模式） > 附录 |
| 194 | [产品介绍](pages/4018300086.md) | `4018300086` | 2026-06-08 09:46:19 | 医保支付（间连模式） |
| 195 | [开发接入准备](pages/4018300089.md) | `4018300089` | 2026-05-20 07:23:17 | 医保支付（间连模式） |
| 196 | [开发指引](pages/4016824703.md) | `4016824703` | 2026-05-20 07:25:15 | 医保支付（间连模式） |
| 197 | [医保自费混合收款下单](pages/4018300080.md) | `4018300080` | 2026-03-02 06:55:05 | 医保支付（间连模式） > API列表 > 医保自费混合订单 |
| 198 | [使用医保自费混合订单号查看下单结果](pages/4018300081.md) | `4018300081` | 2026-03-02 06:55:05 | 医保支付（间连模式） > API列表 > 医保自费混合订单 |
| 199 | [使用从业机构订单号查看下单结果](pages/4018300082.md) | `4018300082` | 2026-03-02 06:55:05 | 医保支付（间连模式） > API列表 > 医保自费混合订单 |
| 200 | [小程序调起医保自费混合支付](pages/4018300079.md) | `4018300079` | 2026-03-02 06:55:05 | 医保支付（间连模式） > API列表 > 医保自费混合订单 |
| 201 | [JSAPI调起医保自费混合支付](pages/4018300083.md) | `4018300083` | 2026-03-02 06:55:05 | 医保支付（间连模式） > API列表 > 医保自费混合订单 |
| 202 | [医保混合收款成功通知](pages/4018303231.md) | `4018303231` | 2026-03-02 06:56:16 | 医保支付（间连模式） > API列表 > 医保自费混合订单 |
| 203 | [医保退款通知](pages/4018300085.md) | `4018300085` | 2026-03-02 02:58:27 | 医保支付（间连模式） > API列表 > 医保退款 |
| 204 | [报错排查指引](pages/4020401288.md) | `4020401288` | 2026-05-14 09:14:51 | 医保支付（间连模式） > 常见问题 |
| 205 | [业务&接口规则类问题](pages/4018300095.md) | `4018300095` | 2026-05-14 09:21:12 | 医保支付（间连模式） > 常见问题 |
| 206 | [申请医保支付权限](pages/4016824701.md) | `4016824701` | 2026-05-20 06:43:31 | 医保支付（间连模式） > 附录 |
| 207 | [接入医保亲情付指引](pages/4018300091.md) | `4018300091` | 2026-05-20 06:44:13 | 医保支付（间连模式） > 附录 |
| 208 | [UI规范与页面说明](pages/4021595913.md) | `4021595913` | 2026-06-08 09:46:25 | 医保支付（间连模式） > 附录 |
| 209 | [产品介绍](pages/4013080622.md) | `4013080622` | 2026-05-21 03:44:04 | 订单退款 |
| 210 | [开发接入准备](pages/4013080630.md) | `4013080630` | 2026-05-19 08:38:56 | 订单退款 |
| 211 | [开发指引](pages/4013080623.md) | `4013080623` | 2026-06-10 07:28:39 | 订单退款 |
| 212 | [业务示例代码](pages/4015217325.md) | `4015217325` | 2026-06-10 07:28:38 | 订单退款 |
| 213 | [常见问题](pages/4013080629.md) | `4013080629` | 2026-05-09 08:56:56 | 订单退款 |
| 214 | [申请退款](pages/4013080625.md) | `4013080625` | 2025-01-16 07:08:56 | 订单退款 > API列表 |
| 215 | [查询单笔退款（通过商户退款单号）](pages/4013080626.md) | `4013080626` | 2025-01-16 07:08:57 | 订单退款 > API列表 |
| 216 | [发起异常退款](pages/4013080627.md) | `4013080627` | 2025-01-16 07:08:52 | 订单退款 > API列表 |
| 217 | [退款结果通知](pages/4013080628.md) | `4013080628` | 2024-12-30 07:47:39 | 订单退款 > API列表 |
| 218 | [退款操作指引](pages/4013080632.md) | `4013080632` | 2024-11-26 08:21:24 | 订单退款 > 附录 |
| 219 | [微信支付退款最佳实践](pages/4014960215.md) | `4014960215` | 2026-06-10 07:28:37 | 订单退款 > 附录 |
| 220 | [产品介绍](pages/4013080592.md) | `4013080592` | 2025-04-24 06:38:30 | 下载账单 |
| 221 | [开发指引](pages/4013080593.md) | `4013080593` | 2026-06-09 07:58:24 | 下载账单 |
| 222 | [业务示例代码](pages/4015988147.md) | `4015988147` | 2025-12-03 04:00:07 | 下载账单 |
| 223 | [常见问题](pages/4013080602.md) | `4013080602` | 2026-05-09 08:57:11 | 下载账单 |
| 224 | [申请所有/单个特约商户交易账单](pages/4013080595.md) | `4013080595` | 2025-01-16 07:08:51 | 下载账单 > API列表 |
| 225 | [申请服务商资金账单](pages/4013080596.md) | `4013080596` | 2025-01-16 07:08:50 | 下载账单 > API列表 |
| 226 | [下载账单](pages/4013080597.md) | `4013080597` | 2024-12-23 03:48:08 | 下载账单 > API列表 |
| 227 | [交易账单详细说明](pages/4013080599.md) | `4013080599` | 2026-01-16 03:53:05 | 下载账单 > 附录 |
| 228 | [资金账单详细说明](pages/4013080600.md) | `4013080600` | 2024-11-26 08:21:16 | 下载账单 > 附录 |
| 229 | [平台下载账单操作指引](pages/4013080601.md) | `4013080601` | 2024-11-26 08:21:11 | 下载账单 > 附录 |
| 230 | [产品介绍](pages/4012072582.md) | `4012072582` | 2025-05-13 02:17:34 | 分账 |
| 231 | [开发接入准备](pages/4012072589.md) | `4012072589` | 2026-05-19 09:30:27 | 分账 |
| 232 | [开发指引](pages/4012072601.md) | `4012072601` | 2026-06-09 09:46:15 | 分账 |
| 233 | [常见问题](pages/4014547107.md) | `4014547107` | 2026-04-28 06:56:30 | 分账 |
| 234 | [请求分账](pages/4012690683.md) | `4012690683` | 2025-09-29 01:58:27 | 分账 > API列表 |
| 235 | [查询分账结果](pages/4012466850.md) | `4012466850` | 2025-09-29 03:51:23 | 分账 > API列表 |
| 236 | [请求分账回退](pages/4012466854.md) | `4012466854` | 2025-09-29 03:50:46 | 分账 > API列表 |
| 237 | [查询分账回退结果](pages/4012466858.md) | `4012466858` | 2025-09-29 03:49:39 | 分账 > API列表 |
| 238 | [解冻剩余资金](pages/4012466860.md) | `4012466860` | 2025-09-29 03:49:07 | 分账 > API列表 |
| 239 | [查询剩余待分金额](pages/4012457927.md) | `4012457927` | 2025-09-29 03:48:45 | 分账 > API列表 |
| 240 | [查询最大分账比例](pages/4012466864.md) | `4012466864` | 2025-09-29 03:48:29 | 分账 > API列表 |
| 241 | [添加分账接收方](pages/4012690944.md) | `4012690944` | 2025-09-29 03:48:04 | 分账 > API列表 |
| 242 | [删除分账接收方](pages/4012466868.md) | `4012466868` | 2025-09-29 03:47:32 | 分账 > API列表 |
| 243 | [分账动账通知](pages/4012075216.md) | `4012075216` | 2025-02-19 03:56:03 | 分账 > API列表 |
| 244 | [申请分账账单](pages/4012761140.md) | `4012761140` | 2025-09-29 03:47:03 | 分账 > API列表 |
| 245 | [下载账单](pages/4012075366.md) | `4012075366` | 2024-10-30 06:42:53 | 分账 > API列表 |
| 246 | [分账失败处理指引](pages/4015504885.md) | `4015504885` | 2025-07-04 03:08:11 | 分账 > 附录 |
| 247 | [产品介绍](pages/4012586132.md) | `4012586132` | 2026-05-26 09:26:57 | 微信支付分 |
| 248 | [开发接入准备](pages/4012586133.md) | `4012586133` | 2026-05-19 08:42:51 | 微信支付分 |
| 249 | [开发指引](pages/4012586134.md) | `4012586134` | 2026-06-10 07:28:51 | 微信支付分 |
| 250 | [常见问题](pages/4012586139.md) | `4012586139` | 2026-05-09 08:57:42 | 微信支付分 |
| 251 | [创建支付分订单](pages/4013138534.md) | `4013138534` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 252 | [查询支付分订单](pages/4013138559.md) | `4013138559` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 253 | [取消支付分订单](pages/4013138589.md) | `4013138589` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 254 | [确认订单回调通知](pages/4012586137.md) | `4012586137` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 255 | [完结支付分订单](pages/4013138598.md) | `4013138598` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 256 | [修改支付分订单金额](pages/4013138819.md) | `4013138819` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 257 | [同步支付分订单状态](pages/4013138975.md) | `4013138975` | 2024-12-06 08:29:39 | 微信支付分 > API列表 |
| 258 | [支付成功回调通知](pages/4012586136.md) | `4012586136` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 259 | [申请退款](pages/4013138987.md) | `4013138987` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 260 | [查询退款](pages/4013139077.md) | `4013139077` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 261 | [退款结果通知](pages/4012586138.md) | `4012586138` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 262 | [JSAPI调起支付分确认订单页](pages/4012607505.md) | `4012607505` | 2024-12-05 07:33:34 | 微信支付分 > API列表 > 拉起支付分小程序确认订单页 |
| 263 | [Android](pages/4012607507.md) | `4012607507` | 2024-12-05 07:31:51 | 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > APP调起支付分确认订单页 |
| 264 | [iOS](pages/4012607508.md) | `4012607508` | 2024-12-05 07:32:18 | 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > APP调起支付分确认订单页 |
| 265 | [鸿蒙](pages/4015271745.md) | `4015271745` | 2025-06-18 06:57:03 | 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > APP调起支付分确认订单页 |
| 266 | [wx.openBusinessView](pages/4012607510.md) | `4012607510` | 2024-12-05 07:32:49 | 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > 小程序调起支付分确认订单页 |
| 267 | [wx.navigateToMiniProgram（停止新增）](pages/4012607511.md) | `4012607511` | 2024-12-05 07:33:11 | 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > 小程序调起支付分确认订单页 |
| 268 | [JSAPI调起支付分订单详情页](pages/4012607518.md) | `4012607518` | 2024-12-05 07:36:11 | 微信支付分 > API列表 > 拉起支付分小程序订单详情页 |
| 269 | [Android](pages/4012607513.md) | `4012607513` | 2024-12-05 07:34:23 | 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > APP调起支付分订单详情页 |
| 270 | [iOS](pages/4012607514.md) | `4012607514` | 2024-12-05 07:34:53 | 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > APP调起支付分订单详情页 |
| 271 | [鸿蒙](pages/4015271776.md) | `4015271776` | 2025-06-18 06:57:00 | 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > APP调起支付分订单详情页 |
| 272 | [wx.openBusinessView](pages/4012607516.md) | `4012607516` | 2024-12-05 07:35:16 | 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > 小程序调起支付分订单详情页 |
| 273 | [wx.navigateToMiniProgram（停止新增）](pages/4012607517.md) | `4012607517` | 2024-12-05 07:35:36 | 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > 小程序调起支付分订单详情页 |
| 274 | [支付分合作品牌线上应用规范](pages/4012586152.md) | `4012586152` | 2025-03-20 07:09:22 | 微信支付分 > 附录 |
| 275 | [支付分权限申请邮件模板](pages/4012586142.md) | `4012586142` | 2024-12-09 02:47:16 | 微信支付分 > 附录 |
| 276 | [测试微信号配置指引](pages/4012586141.md) | `4012586141` | 2024-12-09 10:14:05 | 微信支付分 > 附录 |
| 277 | [服务ID新增绑定邮件流程](pages/4012624851.md) | `4012624851` | 2024-12-09 10:13:56 | 微信支付分 > 附录 |
| 278 | [总览](pages/4013163663.md) | `4013163663` | 2024-12-09 09:41:21 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 279 | [二轮电动车充电桩](pages/4012586150.md) | `4012586150` | 2024-12-09 09:41:03 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 280 | [充电宝](pages/4012586148.md) | `4012586148` | 2024-12-09 09:40:59 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 281 | [共享单车](pages/4012586145.md) | `4012586145` | 2024-12-09 09:40:55 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 282 | [快递行业](pages/4012586144.md) | `4012586144` | 2024-12-09 09:40:52 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 283 | [智慧零售(无人设备)](pages/4012586146.md) | `4012586146` | 2024-12-09 09:40:50 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 284 | [汽车充电桩](pages/4012586149.md) | `4012586149` | 2024-12-09 09:40:46 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 285 | [汽车租赁](pages/4012586151.md) | `4012586151` | 2024-12-09 09:40:42 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 286 | [酒店行业](pages/4012586147.md) | `4012586147` | 2024-12-09 10:14:02 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 287 | [产品介绍](pages/4012085549.md) | `4012085549` | 2025-03-21 09:21:49 | 微信支付分停车服务 |
| 288 | [开发接入准备](pages/4012085632.md) | `4012085632` | 2026-05-19 08:43:09 | 微信支付分停车服务 |
| 289 | [开发指引](pages/4012085711.md) | `4012085711` | 2026-06-09 07:58:23 | 微信支付分停车服务 |
| 290 | [常见问题](pages/4016183529.md) | `4016183529` | 2025-12-12 02:16:53 | 微信支付分停车服务 |
| 291 | [创建停车入场](pages/4012533994.md) | `4012533994` | 2025-02-21 08:25:44 | 微信支付分停车服务 > API列表 > 停车入场 |
| 292 | [停车入场状态变更通知](pages/4012085798.md) | `4012085798` | 2025-02-19 07:23:03 | 微信支付分停车服务 > API列表 > 停车入场 |
| 293 | [查询车牌服务开通信息](pages/4012534183.md) | `4012534183` | 2025-02-21 08:25:08 | 微信支付分停车服务 > API列表 > 服务 |
| 294 | [小程序调起微信支付分停车服务开通页](pages/4012085969.md) | `4012085969` | 2024-10-31 07:43:33 | 微信支付分停车服务 > API列表 > 服务 |
| 295 | [H5调起微信支付分停车服务开通页](pages/4012085997.md) | `4012085997` | 2024-10-31 07:46:05 | 微信支付分停车服务 > API列表 > 服务 |
| 296 | [App拉起微信支付分停车服务开通页](pages/4012086028.md) | `4012086028` | 2024-10-22 09:54:33 | 微信支付分停车服务 > API列表 > 服务 |
| 297 | [查询订单](pages/4012534441.md) | `4012534441` | 2025-02-21 08:26:35 | 微信支付分停车服务 > API列表 > 扣费受理 |
| 298 | [扣费受理](pages/4012534427.md) | `4012534427` | 2025-03-11 03:03:56 | 微信支付分停车服务 > API列表 > 扣费受理 |
| 299 | [订单支付结果通知](pages/4012086059.md) | `4012086059` | 2025-02-19 07:20:38 | 微信支付分停车服务 > API列表 > 扣费受理 |
| 300 | [微信垫资还款](pages/4012086207.md) | `4012086207` | 2024-11-04 02:10:45 | 微信支付分停车服务 > API列表 > 还款 |
| 301 | [退款申请](pages/4012760545.md) | `4012760545` | 2025-04-07 01:50:02 | 微信支付分停车服务 > API列表 > 退款 |
| 302 | [退款结果通知](pages/4012086319.md) | `4012086319` | 2025-02-20 03:14:52 | 微信支付分停车服务 > API列表 > 退款 |
| 303 | [查询单笔退款（通过商户退款单号）](pages/4012760554.md) | `4012760554` | 2025-04-07 01:49:56 | 微信支付分停车服务 > API列表 > 退款 |
| 304 | [现金红包（V2）](pages/4012851209.md) | `4012851209` | 2025-04-25 07:53:50 | 现金红包（V2） |
| 305 | [产品介绍](pages/4012087800.md) | `4012087800` | 2025-10-14 07:18:06 | 代金券 |
| 306 | [开发接入准备](pages/4012087801.md) | `4012087801` | 2026-05-19 08:44:06 | 代金券 |
| 307 | [开发指引](pages/4012087802.md) | `4012087802` | 2026-06-09 07:58:19 | 代金券 |
| 308 | [常见问题](pages/4015880931.md) | `4015880931` | 2025-12-19 02:28:02 | 代金券 |
| 309 | [核销事件回调通知](pages/4012285807.md) | `4012285807` | 2025-02-20 07:10:47 | 代金券 > API列表 |
| 310 | [图片上传（营销专用）](pages/4012759802.md) | `4012759802` | 2024-11-18 09:26:00 | 代金券 > API列表 |
| 311 | [创建代金券批次](pages/4012534537.md) | `4012534537` | 2024-11-18 09:25:53 | 代金券 > API列表 > 批次 |
| 312 | [激活代金券批次](pages/4012460237.md) | `4012460237` | 2024-11-18 09:26:00 | 代金券 > API列表 > 批次 |
| 313 | [暂停代金券批次](pages/4012460340.md) | `4012460340` | 2024-11-18 09:26:00 | 代金券 > API列表 > 批次 |
| 314 | [重启代金券批次](pages/4012460448.md) | `4012460448` | 2024-11-18 09:25:43 | 代金券 > API列表 > 批次 |
| 315 | [条件查询批次列表](pages/4012460518.md) | `4012460518` | 2025-03-25 08:44:52 | 代金券 > API列表 > 批次 |
| 316 | [查询批次详情](pages/4012460606.md) | `4012460606` | 2025-03-25 08:44:50 | 代金券 > API列表 > 批次 |
| 317 | [查询代金券可用商户](pages/4012463409.md) | `4012463409` | 2024-11-18 09:25:45 | 代金券 > API列表 > 批次 |
| 318 | [查询代金券可用单品](pages/4012463475.md) | `4012463475` | 2024-11-18 09:25:55 | 代金券 > API列表 > 批次 |
| 319 | [下载批次退款明细](pages/4012463548.md) | `4012463548` | 2024-11-18 09:25:43 | 代金券 > API列表 > 批次 |
| 320 | [下载批次核销明细](pages/4012463698.md) | `4012463698` | 2024-11-18 09:25:53 | 代金券 > API列表 > 批次 |
| 321 | [根据商户号查用户的券](pages/4012494237.md) | `4012494237` | 2024-11-18 09:25:43 | 代金券 > API列表 > 券 |
| 322 | [发放指定批次的代金券](pages/4012463807.md) | `4012463807` | 2024-11-18 09:25:41 | 代金券 > API列表 > 券 |
| 323 | [查询代金券详情](pages/4012492796.md) | `4012492796` | 2024-11-18 09:26:04 | 代金券 > API列表 > 券 |
| 324 | [查询代金券消息通知地址](pages/4012464155.md) | `4012464155` | 2024-11-18 09:25:49 | 代金券 > API列表 > 消息通知地址 |
| 325 | [设置代金券消息通知地址](pages/4012464176.md) | `4012464176` | 2024-11-18 09:25:40 | 代金券 > API列表 > 消息通知地址 |
| 326 | [产品介绍](pages/4012071996.md) | `4012071996` | 2024-07-23 08:00:45 | 委托营销 |
| 327 | [开发接入准备](pages/4012071997.md) | `4012071997` | 2026-05-19 08:45:58 | 委托营销 |
| 328 | [开发指引](pages/4012071998.md) | `4012071998` | 2026-06-09 09:47:05 | 委托营销 |
| 329 | [建立合作关系](pages/4012381469.md) | `4012381469` | 2024-11-18 09:25:45 | 委托营销 > API列表 |
| 330 | [查询合作关系列表](pages/4012381479.md) | `4012381479` | 2024-11-18 09:25:58 | 委托营销 > API列表 |
| 331 | [产品介绍](pages/4012072117.md) | `4012072117` | 2025-11-11 11:20:38 | 支付有礼 |
| 332 | [开发接入准备](pages/4012072118.md) | `4012072118` | 2026-05-19 08:46:11 | 支付有礼 |
| 333 | [开发指引](pages/4012072119.md) | `4012072119` | 2026-06-09 09:46:59 | 支付有礼 |
| 334 | [图片上传（营销专用）](pages/4012760270.md) | `4012760270` | 2024-11-18 09:26:00 | 支付有礼 > API列表 |
| 335 | [创建全场满额送活动](pages/4012492900.md) | `4012492900` | 2024-11-18 09:25:56 | 支付有礼 > API列表 > 支付有礼活动 |
| 336 | [获取活动详情接口](pages/4012492967.md) | `4012492967` | 2024-11-18 09:25:58 | 支付有礼 > API列表 > 支付有礼活动 |
| 337 | [获取活动发券商户号](pages/4012466191.md) | `4012466191` | 2024-11-18 09:25:52 | 支付有礼 > API列表 > 支付有礼活动 |
| 338 | [获取活动指定商品列表](pages/4012466492.md) | `4012466492` | 2024-11-18 09:25:51 | 支付有礼 > API列表 > 支付有礼活动 |
| 339 | [终止活动](pages/4012466633.md) | `4012466633` | 2024-11-18 09:25:39 | 支付有礼 > API列表 > 支付有礼活动 |
| 340 | [新增活动发券商户号](pages/4012466735.md) | `4012466735` | 2024-11-18 09:25:55 | 支付有礼 > API列表 > 支付有礼活动 |
| 341 | [获取支付有礼活动列表](pages/4012493214.md) | `4012493214` | 2024-11-18 09:25:51 | 支付有礼 > API列表 > 支付有礼活动 |
| 342 | [删除活动发券商户号](pages/4012466827.md) | `4012466827` | 2024-11-18 09:25:40 | 支付有礼 > API列表 > 支付有礼活动 |
| 343 | [产品介绍](pages/4012072233.md) | `4012072233` | 2025-03-21 10:25:07 | 小程序发券插件 |
| 344 | [开发接入准备](pages/4012072234.md) | `4012072234` | 2026-05-19 08:46:25 | 小程序发券插件 |
| 345 | [小程序发券插件](pages/4012285878.md) | `4012285878` | 2025-02-19 03:55:31 | 小程序发券插件 > API列表 |
| 346 | [产品介绍](pages/4012075048.md) | `4012075048` | 2025-03-21 07:41:31 | H5发券 |
| 347 | [开发接入准备](pages/4012075086.md) | `4012075086` | 2026-05-19 08:46:39 | H5发券 |
| 348 | [H5发券](pages/4012285900.md) | `4012285900` | 2025-03-21 07:39:58 | H5发券 > API列表 |
| 349 | [产品介绍](pages/4012075220.md) | `4012075220` | 2025-03-21 07:41:21 | 智慧商圈 |
| 350 | [开发接入准备](pages/4012075231.md) | `4012075231` | 2026-05-19 08:46:54 | 智慧商圈 |
| 351 | [开发指引](pages/4012075386.md) | `4012075386` | 2026-06-09 07:58:14 | 智慧商圈 |
| 352 | [常见问题](pages/4016111726.md) | `4016111726` | 2026-05-19 07:41:47 | 智慧商圈 |
| 353 | [商圈会员积分服务授权结果通知](pages/4012076406.md) | `4012076406` | 2025-02-19 03:56:03 | 智慧商圈 > API列表 |
| 354 | [商圈会员场内支付结果通知](pages/4012076414.md) | `4012076414` | 2025-02-19 03:56:03 | 智慧商圈 > API列表 |
| 355 | [商圈会员积分同步](pages/4012474133.md) | `4012474133` | 2024-11-18 09:25:47 | 智慧商圈 > API列表 |
| 356 | [商圈会员场内退款结果通知](pages/4012076419.md) | `4012076419` | 2025-02-19 03:56:03 | 智慧商圈 > API列表 |
| 357 | [商圈会员积分服务授权查询](pages/4012474135.md) | `4012474135` | 2024-11-18 09:25:40 | 智慧商圈 > API列表 |
| 358 | [商圈会员待积分状态查询](pages/4012474129.md) | `4012474129` | 2024-11-28 06:23:32 | 智慧商圈 > API列表 |
| 359 | [商圈会员停车状态同步](pages/4012474127.md) | `4012474127` | 2024-11-28 06:23:40 | 智慧商圈 > API列表 |
| 360 | [产品介绍](pages/4012076036.md) | `4012076036` | 2026-06-10 07:28:54 | 支付即服务 |
| 361 | [开发接入准备](pages/4012076037.md) | `4012076037` | 2026-05-19 08:47:09 | 支付即服务 |
| 362 | [开发指引](pages/4012076038.md) | `4012076038` | 2026-06-09 09:46:56 | 支付即服务 |
| 363 | [常见问题](pages/4016913657.md) | `4016913657` | 2025-12-19 02:14:14 | 支付即服务 |
| 364 | [服务人员查询](pages/4012688558.md) | `4012688558` | 2025-01-09 03:09:59 | 支付即服务 > API列表 |
| 365 | [服务人员注册](pages/4012688564.md) | `4012688564` | 2025-01-09 03:10:21 | 支付即服务 > API列表 |
| 366 | [服务人员更新](pages/4012688570.md) | `4012688570` | 2025-01-09 03:10:22 | 支付即服务 > API列表 |
| 367 | [服务人员分配](pages/4012474145.md) | `4012474145` | 2024-11-18 09:26:02 | 支付即服务 > API列表 |
| 368 | [服务人员称谓申请指引](pages/4012076039.md) | `4012076039` | 2024-07-24 02:26:28 | 支付即服务 > 附录 |
| 369 | [免开发版本操作指引](pages/4012076040.md) | `4012076040` | 2024-11-18 09:25:36 | 支付即服务 > 附录 |
| 370 | [个人微信服务人员注册](pages/4012076041.md) | `4012076041` | 2024-08-02 07:09:59 | 支付即服务 > 附录 |
| 371 | [产品介绍](pages/4012072130.md) | `4012072130` | 2025-09-04 06:45:36 | 点金计划 |
| 372 | [开发接入准备](pages/4012072158.md) | `4012072158` | 2026-05-19 08:50:32 | 点金计划 |
| 373 | [开发指引](pages/4012072262.md) | `4012072262` | 2026-06-09 09:46:53 | 点金计划 |
| 374 | [常见问题](pages/4016241762.md) | `4016241762` | 2026-01-23 03:27:42 | 点金计划 |
| 375 | [点金计划管理](pages/4012473796.md) | `4012473796` | 2024-11-18 09:26:00 | 点金计划 > API列表 |
| 376 | [商家小票管理](pages/4012473788.md) | `4012473788` | 2024-11-18 09:25:49 | 点金计划 > API列表 |
| 377 | [同业过滤标签管理](pages/4012473784.md) | `4012473784` | 2024-11-18 09:25:53 | 点金计划 > API列表 |
| 378 | [开通广告展示](pages/4012473794.md) | `4012473794` | 2024-11-18 09:25:55 | 点金计划 > API列表 |
| 379 | [关闭广告展示](pages/4012473781.md) | `4012473781` | 2024-11-18 09:25:47 | 点金计划 > API列表 |
| 380 | [小程序左上角返回键管理](pages/4012072514.md) | `4012072514` | 2025-02-19 07:20:53 | 点金计划 > API列表 |
| 381 | [产品介绍](pages/4016433410.md) | `4016433410` | 2026-04-02 14:46:39 | 品牌入驻 |
| 382 | [开发指引](pages/4016985537.md) | `4016985537` | 2026-03-12 02:43:59 | 品牌入驻 |
| 383 | [常见问题](pages/4017027854.md) | `4017027854` | 2026-01-04 03:49:11 | 品牌入驻 |
| 384 | [提交入驻申请](pages/4016249989.md) | `4016249989` | 2025-10-23 06:29:49 | 品牌入驻 > API列表 |
| 385 | [根据业务申请编号查询申请状态](pages/4016257694.md) | `4016257694` | 2025-10-23 06:29:49 | 品牌入驻 > API列表 |
| 386 | [根据申请单ID查询申请状态](pages/4016257685.md) | `4016257685` | 2025-10-23 06:29:49 | 品牌入驻 > API列表 |
| 387 | [撤销申请](pages/4016257700.md) | `4016257700` | 2025-10-23 06:29:49 | 品牌入驻 > API列表 |
| 388 | [图片上传](pages/4016276333.md) | `4016276333` | 2025-10-23 06:29:49 | 品牌入驻 > API列表 |
| 389 | [品牌能力介绍](pages/4016433389.md) | `4016433389` | 2026-04-02 12:48:03 | 品牌入驻 > 附录 |
| 390 | [服务商申请品牌授权流程](pages/4016026183.md) | `4016026183` | 2026-03-11 09:48:51 | 品牌入驻 > 附录 |
| 391 | [产品介绍](pages/4016433952.md) | `4016433952` | 2025-11-12 07:52:53 | 商家名片 |
| 392 | [常见问题](pages/4017027862.md) | `4017027862` | 2026-01-04 03:49:05 | 商家名片 |
| 393 | [商家名片开发指引](pages/4016914463.md) | `4016914463` | 2026-06-10 07:28:50 | 商家名片 > 开发指引 |
| 394 | [交易连接名片开发指引](pages/4016985845.md) | `4016985845` | 2026-06-10 07:28:47 | 商家名片 > 开发指引 |
| 395 | [提交商家名片配置申请](pages/4016468440.md) | `4016468440` | 2025-11-13 06:54:09 | 商家名片 > API列表 > 商家名片配置 |
| 396 | [发布商家名片配置](pages/4016475176.md) | `4016475176` | 2025-11-13 06:54:27 | 商家名片 > API列表 > 商家名片配置 |
| 397 | [撤销商家名片配置申请](pages/4016475172.md) | `4016475172` | 2025-11-13 06:54:39 | 商家名片 > API列表 > 商家名片配置 |
| 398 | [查询商家名片配置申请状态](pages/4016475174.md) | `4016475174` | 2025-11-13 06:54:51 | 商家名片 > API列表 > 商家名片配置 |
| 399 | [获取商家名片预览二维码](pages/4016641998.md) | `4016641998` | 2025-11-20 07:20:12 | 商家名片 > API列表 > 商家名片配置 |
| 400 | [添加交易连接名片规则申请](pages/4016333302.md) | `4016333302` | 2025-10-30 09:56:20 | 商家名片 > API列表 > 交易连接名片 |
| 401 | [解除已生效交易连接名片场景](pages/4016366804.md) | `4016366804` | 2025-10-30 09:56:20 | 商家名片 > API列表 > 交易连接名片 |
| 402 | [撤销交易连接名片配置申请](pages/4016366797.md) | `4016366797` | 2025-10-30 09:56:20 | 商家名片 > API列表 > 交易连接名片 |
| 403 | [查询已生效交易连接名片规则](pages/4016366785.md) | `4016366785` | 2025-10-30 09:56:20 | 商家名片 > API列表 > 交易连接名片 |
| 404 | [根据业务申请编号查询添加申请状态](pages/4016366816.md) | `4016366816` | 2025-10-30 09:56:20 | 商家名片 > API列表 > 交易连接名片 |
| 405 | [商家名片&交易连接名片配置指引](pages/4016433970.md) | `4016433970` | 2026-04-02 12:57:33 | 商家名片 > 附录 |
| 406 | [产品介绍](pages/4015274636.md) | `4015274636` | 2026-02-10 04:06:43 | 商家名片会员 |
| 407 | [开发指引](pages/4015274639.md) | `4015274639` | 2026-06-10 07:28:41 | 商家名片会员 |
| 408 | [常见问题](pages/4017418554.md) | `4017418554` | 2026-01-30 07:18:54 | 商家名片会员 |
| 409 | [图片上传](pages/4015900513.md) | `4015900513` | 2025-11-14 07:32:05 | 商家名片会员 > API列表 |
| 410 | [创建会员卡模板](pages/4015336970.md) | `4015336970` | 2025-08-01 02:53:26 | 商家名片会员 > API列表 > 会员卡模板管理 |
| 411 | [查询会员卡模板列表](pages/4015336976.md) | `4015336976` | 2025-08-01 02:53:26 | 商家名片会员 > API列表 > 会员卡模板管理 |
| 412 | [查询会员卡模板信息](pages/4015336974.md) | `4015336974` | 2025-08-01 02:53:26 | 商家名片会员 > API列表 > 会员卡模板管理 |
| 413 | [修改会员卡模板信息](pages/4015336977.md) | `4015336977` | 2025-08-01 02:53:26 | 商家名片会员 > API列表 > 会员卡模板管理 |
| 414 | [作废会员卡模板](pages/4015336972.md) | `4015336972` | 2025-08-01 02:53:26 | 商家名片会员 > API列表 > 会员卡模板管理 |
| 415 | [查询用户会员卡信息](pages/4015336980.md) | `4015336980` | 2025-07-25 03:00:22 | 商家名片会员 > API列表 > 用户会员卡管理 |
| 416 | [查询用户在品牌下所有会员卡](pages/4015336984.md) | `4015336984` | 2025-07-25 03:00:22 | 商家名片会员 > API列表 > 用户会员卡管理 |
| 417 | [修改用户会员卡信息](pages/4015336985.md) | `4015336985` | 2025-07-25 03:00:22 | 商家名片会员 > API列表 > 用户会员卡管理 |
| 418 | [作废用户会员卡](pages/4015336983.md) | `4015336983` | 2025-07-25 03:00:22 | 商家名片会员 > API列表 > 用户会员卡管理 |
| 419 | [品牌会员入会组件预授权](pages/4015336986.md) | `4015336986` | 2025-11-19 04:10:23 | 商家名片会员 > API列表 > 用户开通会员卡 |
| 420 | [小程序拉起品牌会员入会组件](pages/4015273633.md) | `4015273633` | 2025-06-24 06:51:53 | 商家名片会员 > API列表 > 用户开通会员卡 |
| 421 | [H5拉起品牌会员入会组件](pages/4015331476.md) | `4015331476` | 2025-12-23 08:54:29 | 商家名片会员 > API列表 > 用户开通会员卡 |
| 422 | [根据OPENID导入用户会员卡](pages/4015336981.md) | `4015336981` | 2025-06-22 08:21:27 | 商家名片会员 > API列表 > 商家同步会员身份 |
| 423 | [同步会员开通结果](pages/4015336979.md) | `4015336979` | 2025-06-22 08:22:08 | 商家名片会员 > API列表 > 商家同步会员身份 |
| 424 | [会员卡事件通知](pages/4015283692.md) | `4015283692` | 2025-08-18 10:08:53 | 商家名片会员 > API列表 > 事件通知 |
| 425 | [用户积分兑券事件通知](pages/4015878622.md) | `4015878622` | 2025-08-18 10:08:53 | 商家名片会员 > API列表 > 事件通知 |
| 426 | [用户积分同步事件通知](pages/4016096820.md) | `4016096820` | 2025-09-17 02:57:14 | 商家名片会员 > API列表 > 事件通知 |
| 427 | [创建用户动态信息](pages/4015336987.md) | `4015336987` | 2025-11-14 07:31:53 | 商家名片会员 > API列表 > 用户动态 |
| 428 | [下单同步用户实时动态](pages/4015534755.md) | `4015534755` | 2025-11-14 07:31:53 | 商家名片会员 > API列表 > 用户动态 |
| 429 | [同步积分余额](pages/4015897280.md) | `4015897280` | 2025-08-20 08:35:05 | 商家名片会员 > API列表 > 会员卡积分兑券 |
| 430 | [同步积分兑券结果](pages/4015897268.md) | `4015897268` | 2025-08-20 08:35:07 | 商家名片会员 > API列表 > 会员卡积分兑券 |
| 431 | [创建品牌会员发券活动](pages/4016464918.md) | `4016464918` | 2025-11-14 07:20:57 | 商家名片会员 > API列表 > 品牌会员发券活动 |
| 432 | [查询品牌会员发券活动](pages/4016588015.md) | `4016588015` | 2025-11-14 07:20:57 | 商家名片会员 > API列表 > 品牌会员发券活动 |
| 433 | [查询品牌会员发券活动列表](pages/4016588039.md) | `4016588039` | 2025-11-14 07:20:57 | 商家名片会员 > API列表 > 品牌会员发券活动 |
| 434 | [修改品牌会员发券活动信息](pages/4016588044.md) | `4016588044` | 2025-11-14 07:20:57 | 商家名片会员 > API列表 > 品牌会员发券活动 |
| 435 | [终止品牌会员发券活动](pages/4016588028.md) | `4016588028` | 2025-11-14 07:20:57 | 商家名片会员 > API列表 > 品牌会员发券活动 |
| 436 | [产品介绍](pages/4015782374.md) | `4015782374` | 2026-03-11 10:24:02 | 摇一摇有优惠 |
| 437 | [开发接入准备](pages/4016060552.md) | `4016060552` | 2026-05-21 07:33:55 | 摇一摇有优惠 |
| 438 | [开发指引](pages/4016110225.md) | `4016110225` | 2025-11-18 03:40:57 | 摇一摇有优惠 |
| 439 | [常见问题](pages/4017418618.md) | `4017418618` | 2026-01-30 07:18:49 | 摇一摇有优惠 |
| 440 | [创建投放计划](pages/4016184554.md) | `4016184554` | 2025-12-31 07:07:29 | 摇一摇有优惠 > API列表 > 投放计划 |
| 441 | [分页查询投放计划列表](pages/4016184563.md) | `4016184563` | 2025-09-27 11:06:05 | 摇一摇有优惠 > API列表 > 投放计划 |
| 442 | [更新投放计划](pages/4016184594.md) | `4016184594` | 2025-09-27 11:06:26 | 摇一摇有优惠 > API列表 > 投放计划 |
| 443 | [终止投放计划](pages/4016184572.md) | `4016184572` | 2025-09-27 11:06:52 | 摇一摇有优惠 > API列表 > 投放计划 |
| 444 | [设置投放计划回调地址](pages/4016184598.md) | `4016184598` | 2025-09-27 11:07:12 | 摇一摇有优惠 > API列表 > 投放计划 |
| 445 | [投放计划状态变更通知](pages/4016168699.md) | `4016168699` | 2026-03-23 07:44:52 | 摇一摇有优惠 > API列表 > 投放计划 |
| 446 | [投放计划功能介绍](pages/4016402231.md) | `4016402231` | 2026-06-10 07:28:14 | 摇一摇有优惠 > 附录 |
| 447 | [投放计划配置指引](pages/4016111064.md) | `4016111064` | 2026-06-10 07:28:12 | 摇一摇有优惠 > 附录 |
| 448 | [品牌信息用户端展示规则](pages/4016110939.md) | `4016110939` | 2025-11-07 03:08:03 | 摇一摇有优惠 > 附录 |
| 449 | [权限申请](pages/4015788437.md) | `4015788437` | 2026-04-08 02:20:15 | 摇一摇有优惠 > 附录 |
| 450 | [运营规则](pages/4017294537.md) | `4017294537` | 2026-01-20 09:27:40 | 摇一摇有优惠 > 附录 |
| 451 | [产品介绍](pages/4015989376.md) | `4015989376` | 2026-05-13 06:51:04 | 商品券（单券） |
| 452 | [开发指引](pages/4015788446.md) | `4015788446` | 2026-06-10 07:28:11 | 商品券（单券） |
| 453 | [常见问题](pages/4016950421.md) | `4016950421` | 2025-12-23 02:29:29 | 商品券（单券） |
| 454 | [图片上传](pages/4015781275.md) | `4015781275` | 2025-11-07 03:39:13 | 商品券（单券） > API列表 |
| 455 | [创建商品券](pages/4015781289.md) | `4015781289` | 2025-12-31 07:51:19 | 商品券（单券） > API列表 > 商品券管理 |
| 456 | [修改商品券](pages/4015781296.md) | `4015781296` | 2025-08-20 03:37:14 | 商品券（单券） > API列表 > 商品券管理 |
| 457 | [查询商品券](pages/4015781292.md) | `4015781292` | 2025-08-20 03:37:35 | 商品券（单券） > API列表 > 商品券管理 |
| 458 | [失效商品券](pages/4015781290.md) | `4015781290` | 2025-08-20 03:38:31 | 商品券（单券） > API列表 > 商品券管理 |
| 459 | [添加商品券批次](pages/4015781304.md) | `4015781304` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 460 | [查询商品券批次列表](pages/4015781553.md) | `4015781553` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 461 | [查询商品券指定批次](pages/4015781542.md) | `4015781542` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 462 | [修改商品券批次](pages/4015781556.md) | `4015781556` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 463 | [修改商品券批次发放预算](pages/4015781561.md) | `4015781561` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 464 | [失效商品券批次](pages/4015781532.md) | `4015781532` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 465 | [批次关联门店](pages/4015781302.md) | `4015781302` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 466 | [查询批次关联门店列表](pages/4015781546.md) | `4015781546` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 467 | [批次取消关联门店](pages/4015781537.md) | `4015781537` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 468 | [预上传券Code](pages/4015781572.md) | `4015781572` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 469 | [向用户发放商品券](pages/4015781605.md) | `4015781605` | 2025-11-07 03:28:05 | 商品券（单券） > API列表 > 商品券发放 |
| 470 | [确认发放用户商品券](pages/4015781575.md) | `4015781575` | 2025-11-07 03:28:05 | 商品券（单券） > API列表 > 商品券发放 |
| 471 | [向用户预发放商品券](pages/4016434365.md) | `4016434365` | 2025-11-07 03:23:20 | 商品券（单券） > API列表 > 商品券发放 > 小程序发券组件 |
| 472 | [调起小程序发券组件](pages/4016434346.md) | `4016434346` | 2025-12-23 09:05:06 | 商品券（单券） > API列表 > 商品券发放 > 小程序发券组件 |
| 473 | [核销用户商品券](pages/4015781608.md) | `4015781608` | 2025-10-21 09:05:48 | 商品券（单券） > API列表 > 商品券核销 |
| 474 | [调起小程序核销组件](pages/4016110739.md) | `4016110739` | 2025-11-07 08:58:44 | 商品券（单券） > API列表 > 商品券核销 |
| 475 | [查询用户商品券详情](pages/4015781582.md) | `4015781582` | 2025-10-21 09:05:48 | 商品券（单券） > API列表 > 商品券查询 |
| 476 | [指定券状态查询用户商品券列表](pages/4015781590.md) | `4015781590` | 2025-11-07 03:37:12 | 商品券（单券） > API列表 > 商品券查询 |
| 477 | [失效用户商品券](pages/4015781578.md) | `4015781578` | 2025-10-21 09:05:48 | 商品券（单券） > API列表 > 商品券失效与退券 |
| 478 | [退券](pages/4015781599.md) | `4015781599` | 2025-11-07 03:37:52 | 商品券（单券） > API列表 > 商品券失效与退券 |
| 479 | [获取商品券事件通知地址](pages/4015781284.md) | `4015781284` | 2025-08-28 02:02:45 | 商品券（单券） > API列表 > 商品券回调通知 |
| 480 | [设置商品券事件通知地址](pages/4015781286.md) | `4015781286` | 2025-08-28 02:02:45 | 商品券（单券） > API列表 > 商品券回调通知 |
| 481 | [商品券回调通知](pages/4015780862.md) | `4015780862` | 2026-05-08 08:05:27 | 商品券（单券） > API列表 > 商品券回调通知 |
| 482 | [提交图片生成任务](pages/4017327735.md) | `4017327735` | 2026-01-26 03:27:31 | 商品券（单券） > API列表 > 生成商品券头图 |
| 483 | [查询图片生成任务执行结果](pages/4017327739.md) | `4017327739` | 2026-01-26 03:27:31 | 商品券（单券） > API列表 > 生成商品券头图 |
| 484 | [图片生成回调通知](pages/4017327744.md) | `4017327744` | 2026-01-26 03:27:31 | 商品券（单券） > API列表 > 生成商品券头图 |
| 485 | [小程序发券组件开发指引](pages/4016434329.md) | `4016434329` | 2026-06-10 07:28:10 | 商品券（单券） > 附录 |
| 486 | [小程序核销组件开发指引](pages/4016110741.md) | `4016110741` | 2026-04-02 14:44:14 | 商品券（单券） > 附录 |
| 487 | [品牌、服务商、appid关联关系](pages/4018984107.md) | `4018984107` | 2026-03-26 06:44:08 | 商品券（单券） > 附录 |
| 488 | [商品券可核销时间规则说明（coupon_available_period）](pages/4016675999.md) | `4016675999` | 2025-11-25 03:05:19 | 商品券（单券） > 附录 |
| 489 | [商品券客户端消息推送页面](pages/4019005729.md) | `4019005729` | 2026-03-27 06:57:51 | 商品券（单券） > 附录 |
| 490 | [商品券结构及修改说明](pages/4018984452.md) | `4018984452` | 2026-03-27 02:47:11 | 商品券（单券） > 附录 |
| 491 | [【单券-全场-折扣券】API请求示例](pages/4016756270.md) | `4016756270` | 2025-12-02 13:12:50 | 商品券（单券） > 附录 > API请求示例-创建商品券 |
| 492 | [【单券-全场-满减券】API请求示例](pages/4016756271.md) | `4016756271` | 2025-12-02 13:13:02 | 商品券（单券） > 附录 > API请求示例-创建商品券 |
| 493 | [【单券-单品-折扣券】API请求示例](pages/4016756272.md) | `4016756272` | 2025-12-25 11:53:38 | 商品券（单券） > 附录 > API请求示例-创建商品券 |
| 494 | [【单券-单品-满减券】API请求示例](pages/4016756273.md) | `4016756273` | 2025-12-25 11:54:13 | 商品券（单券） > 附录 > API请求示例-创建商品券 |
| 495 | [【单券-单品-兑换券】API请求示例](pages/4016756274.md) | `4016756274` | 2025-12-25 11:55:51 | 商品券（单券） > 附录 > API请求示例-创建商品券 |
| 496 | [产品介绍](pages/4016438787.md) | `4016438787` | 2026-05-13 06:51:15 | 商品券（多次优惠） |
| 497 | [开发指引](pages/4016438816.md) | `4016438816` | 2026-06-10 07:28:08 | 商品券（多次优惠） |
| 498 | [常见问题](pages/4016950439.md) | `4016950439` | 2025-12-23 02:29:27 | 商品券（多次优惠） |
| 499 | [图片上传](pages/4016435731.md) | `4016435731` | 2025-11-07 06:33:45 | 商品券（多次优惠） > API列表 |
| 500 | [创建商品券](pages/4016434630.md) | `4016434630` | 2025-12-31 07:51:33 | 商品券（多次优惠） > API列表 > 商品券管理 |
| 501 | [修改商品券](pages/4016434633.md) | `4016434633` | 2025-11-07 03:42:29 | 商品券（多次优惠） > API列表 > 商品券管理 |
| 502 | [查询商品券](pages/4016434632.md) | `4016434632` | 2025-11-07 03:42:29 | 商品券（多次优惠） > API列表 > 商品券管理 |
| 503 | [失效商品券](pages/4016434631.md) | `4016434631` | 2025-11-07 03:42:29 | 商品券（多次优惠） > API列表 > 商品券管理 |
| 504 | [添加商品券批次组](pages/4016280622.md) | `4016280622` | 2025-11-20 03:00:43 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 505 | [查询商品券批次列表](pages/4016434641.md) | `4016434641` | 2025-11-07 03:50:02 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 506 | [查询商品券指定批次](pages/4016434649.md) | `4016434649` | 2025-11-07 03:50:02 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 507 | [修改商品券批次组](pages/4016280633.md) | `4016280633` | 2025-11-20 03:00:41 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 508 | [修改商品券批次组发放预算](pages/4016280642.md) | `4016280642` | 2025-11-20 03:00:40 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 509 | [批次组批量关联门店](pages/4016280620.md) | `4016280620` | 2025-11-20 03:00:37 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 510 | [批次组批量取消关联门店](pages/4016280629.md) | `4016280629` | 2025-11-20 03:00:33 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 511 | [查询批次关联门店列表](pages/4016434665.md) | `4016434665` | 2025-11-07 03:50:02 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 512 | [预上传券Code](pages/4016434668.md) | `4016434668` | 2025-11-07 03:50:02 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 513 | [向用户发放商品券批次组](pages/4016280664.md) | `4016280664` | 2025-11-20 03:00:32 | 商品券（多次优惠） > API列表 > 商品券发放 |
| 514 | [确认发放用户商品券](pages/4016435562.md) | `4016435562` | 2025-11-07 06:25:22 | 商品券（多次优惠） > API列表 > 商品券发放 |
| 515 | [向用户预发放商品券批次组](pages/4016280670.md) | `4016280670` | 2025-12-16 08:25:19 | 商品券（多次优惠） > API列表 > 商品券发放 > 小程序发券组件 |
| 516 | [调起小程序发券组件](pages/4016435568.md) | `4016435568` | 2025-12-23 08:54:20 | 商品券（多次优惠） > API列表 > 商品券发放 > 小程序发券组件 |
| 517 | [核销用户商品券](pages/4016435636.md) | `4016435636` | 2025-11-07 06:28:01 | 商品券（多次优惠） > API列表 > 商品券核销 |
| 518 | [调起小程序核销组件](pages/4016435640.md) | `4016435640` | 2025-11-07 08:58:05 | 商品券（多次优惠） > API列表 > 商品券核销 |
| 519 | [查询用户商品券详情](pages/4016435702.md) | `4016435702` | 2025-11-07 06:31:39 | 商品券（多次优惠） > API列表 > 商品券查询 |
| 520 | [指定券状态查询用户商品券列表](pages/4016435703.md) | `4016435703` | 2025-11-07 06:31:39 | 商品券（多次优惠） > API列表 > 商品券查询 |
| 521 | [失效用户商品券组](pages/4016280658.md) | `4016280658` | 2025-11-20 03:00:30 | 商品券（多次优惠） > API列表 > 商品券失效与退券 |
| 522 | [退券](pages/4016435674.md) | `4016435674` | 2025-11-07 06:30:06 | 商品券（多次优惠） > API列表 > 商品券失效与退券 |
| 523 | [获取商品券事件通知地址](pages/4016435718.md) | `4016435718` | 2025-11-07 06:32:46 | 商品券（多次优惠） > API列表 > 商品券回调通知 |
| 524 | [设置商品券事件通知地址](pages/4016435719.md) | `4016435719` | 2025-11-07 06:32:46 | 商品券（多次优惠） > API列表 > 商品券回调通知 |
| 525 | [商品券回调通知](pages/4016435717.md) | `4016435717` | 2026-05-08 08:05:23 | 商品券（多次优惠） > API列表 > 商品券回调通知 |
| 526 | [提交图片生成任务](pages/4017327752.md) | `4017327752` | 2026-01-26 03:27:42 | 商品券（多次优惠） > API列表 > 生成商品券头图 |
| 527 | [查询图片生成任务执行结果](pages/4017327753.md) | `4017327753` | 2026-01-26 03:27:42 | 商品券（多次优惠） > API列表 > 生成商品券头图 |
| 528 | [图片生成回调通知](pages/4017327759.md) | `4017327759` | 2026-01-26 03:27:42 | 商品券（多次优惠） > API列表 > 生成商品券头图 |
| 529 | [小程序发券组件开发指引](pages/4016435566.md) | `4016435566` | 2026-06-10 07:28:07 | 商品券（多次优惠） > 附录 |
| 530 | [小程序核销组件开发指引](pages/4016435642.md) | `4016435642` | 2026-04-02 14:46:11 | 商品券（多次优惠） > 附录 |
| 531 | [品牌、服务商、appid关联关系](pages/4018984192.md) | `4018984192` | 2026-03-26 06:44:07 | 商品券（多次优惠） > 附录 |
| 532 | [商品券可核销时间规则说明（coupon_available_period）](pages/4016676012.md) | `4016676012` | 2025-11-25 11:47:16 | 商品券（多次优惠） > 附录 |
| 533 | [商品券客户端消息推送页面](pages/4019005741.md) | `4019005741` | 2026-03-27 06:57:49 | 商品券（多次优惠） > 附录 |
| 534 | [商品券结构及修改说明](pages/4018984437.md) | `4018984437` | 2026-03-27 02:47:05 | 商品券（多次优惠） > 附录 |
| 535 | [【多次优惠-全场-折扣券】API请求示例](pages/4016756283.md) | `4016756283` | 2025-12-04 07:57:31 | 商品券（多次优惠） > 附录 > API请求示例-创建商品券 |
| 536 | [【多次优惠-全场-满减券】API请求示例](pages/4016756284.md) | `4016756284` | 2025-12-04 07:59:00 | 商品券（多次优惠） > 附录 > API请求示例-创建商品券 |
| 537 | [【多次优惠-单品-折扣券】API请求示例](pages/4016756285.md) | `4016756285` | 2025-12-04 08:00:48 | 商品券（多次优惠） > 附录 > API请求示例-创建商品券 |
| 538 | [【多次优惠-单品-满减券】API请求示例](pages/4016756286.md) | `4016756286` | 2025-12-04 08:01:18 | 商品券（多次优惠） > 附录 > API请求示例-创建商品券 |
| 539 | [【多次优惠-单品-兑换券】API请求示例](pages/4016756287.md) | `4016756287` | 2025-12-04 08:01:50 | 商品券（多次优惠） > 附录 > API请求示例-创建商品券 |
| 540 | [产品介绍](pages/4016628074.md) | `4016628074` | 2025-11-19 02:54:10 | 品牌门店 |
| 541 | [开发指引](pages/4016628135.md) | `4016628135` | 2026-06-10 07:28:01 | 品牌门店 |
| 542 | [常见问题](pages/4016705104.md) | `4016705104` | 2025-11-27 04:06:48 | 品牌门店 |
| 543 | [创建品牌门店](pages/4015783183.md) | `4015783183` | 2025-12-02 11:35:44 | 品牌门店 > API列表 |
| 544 | [查询品牌门店](pages/4015783153.md) | `4015783153` | 2025-12-02 11:35:44 | 品牌门店 > API列表 |
| 545 | [查询品牌门店列表](pages/4016756674.md) | `4016756674` | 2025-12-16 02:56:33 | 品牌门店 > API列表 |
| 546 | [更新品牌门店](pages/4015783158.md) | `4015783158` | 2025-12-02 11:35:44 | 品牌门店 > API列表 |
| 547 | [删除品牌门店](pages/4015783113.md) | `4015783113` | 2025-12-02 11:35:44 | 品牌门店 > API列表 |
| 548 | [暂停门店营业](pages/4016756671.md) | `4016756671` | 2025-12-16 02:56:33 | 品牌门店 > API列表 |
| 549 | [恢复门店营业](pages/4016756672.md) | `4016756672` | 2025-12-16 02:56:33 | 品牌门店 > API列表 |
| 550 | [绑定收款商户号](pages/4015783177.md) | `4015783177` | 2025-12-02 11:35:44 | 品牌门店 > API列表 |
| 551 | [解绑收款商户号](pages/4015783188.md) | `4015783188` | 2025-12-02 11:35:44 | 品牌门店 > API列表 |
| 552 | [品牌经营平台管理品牌门店](pages/4016689827.md) | `4016689827` | 2025-11-25 10:04:14 | 品牌门店 > 附录 |
| 553 | [获得品牌已授权且在生效中的产品权限信息](pages/4017410365.md) | `4017410365` | 2026-01-29 09:12:34 | 品牌服务商授权 > API列表 |
| 554 | [产品介绍](pages/4012072620.md) | `4012072620` | 2024-07-23 08:51:32 | 连锁品牌分账 |
| 555 | [开发接入准备](pages/4012072625.md) | `4012072625` | 2026-05-19 09:30:42 | 连锁品牌分账 |
| 556 | [开发指引](pages/4012072637.md) | `4012072637` | 2026-06-09 09:46:07 | 连锁品牌分账 |
| 557 | [业务示例代码](pages/4015871675.md) | `4015871675` | 2026-06-09 09:46:50 | 连锁品牌分账 |
| 558 | [常见问题](pages/4015981574.md) | `4015981574` | 2026-02-06 03:12:47 | 连锁品牌分账 |
| 559 | [请求分账](pages/4012692975.md) | `4012692975` | 2025-09-29 03:46:37 | 连锁品牌分账 > API列表 |
| 560 | [查询分账结果](pages/4012467002.md) | `4012467002` | 2025-09-29 03:45:52 | 连锁品牌分账 > API列表 |
| 561 | [请求分账回退](pages/4012467097.md) | `4012467097` | 2025-09-29 03:43:29 | 连锁品牌分账 > API列表 |
| 562 | [查询分账回退结果](pages/4012467011.md) | `4012467011` | 2025-09-29 03:43:57 | 连锁品牌分账 > API列表 |
| 563 | [解冻剩余资金](pages/4012467016.md) | `4012467016` | 2025-09-29 03:43:07 | 连锁品牌分账 > API列表 |
| 564 | [查询订单剩余待分金额](pages/4012467021.md) | `4012467021` | 2025-09-29 03:42:34 | 连锁品牌分账 > API列表 |
| 565 | [查询最大分账比例](pages/4012467022.md) | `4012467022` | 2025-09-29 03:42:11 | 连锁品牌分账 > API列表 |
| 566 | [添加分账接收方](pages/4012467100.md) | `4012467100` | 2025-09-29 03:41:51 | 连锁品牌分账 > API列表 |
| 567 | [删除分账接收方](pages/4012467103.md) | `4012467103` | 2025-09-29 02:38:34 | 连锁品牌分账 > API列表 |
| 568 | [分账动账通知](pages/4012075400.md) | `4012075400` | 2025-02-19 03:56:03 | 连锁品牌分账 > API列表 |
| 569 | [申请分账账单](pages/4012715572.md) | `4012715572` | 2025-09-29 02:37:48 | 连锁品牌分账 > API列表 |
| 570 | [下载账单](pages/4012076073.md) | `4012076073` | 2024-10-30 06:42:53 | 连锁品牌分账 > API列表 |
| 571 | [分账失败处理指引](pages/4015504918.md) | `4015504918` | 2025-07-04 03:08:09 | 连锁品牌分账 > 附录 |
| 572 | [清关报关（V2）](pages/4012851220.md) | `4012851220` | 2025-04-25 07:53:42 | 清关报关（V2） |
| 573 | [产品介绍](pages/4012072827.md) | `4012072827` | 2025-08-25 10:00:14 | 消费者投诉2.0 |
| 574 | [开发接入准备](pages/4012072844.md) | `4012072844` | 2026-05-19 09:30:57 | 消费者投诉2.0 |
| 575 | [开发指引](pages/4012072858.md) | `4012072858` | 2026-06-09 09:46:03 | 消费者投诉2.0 |
| 576 | [业务示例代码](pages/4015933338.md) | `4015933338` | 2026-06-09 09:46:01 | 消费者投诉2.0 |
| 577 | [常见问题](pages/4016111688.md) | `4016111688` | 2026-05-19 07:41:24 | 消费者投诉2.0 |
| 578 | [查询投诉单列表](pages/4012691285.md) | `4012691285` | 2025-09-02 02:28:31 | 消费者投诉2.0 > API列表 > 主动查询投诉信息 |
| 579 | [查询投诉单详情](pages/4012691648.md) | `4012691648` | 2025-08-28 02:43:42 | 消费者投诉2.0 > API列表 > 主动查询投诉信息 |
| 580 | [查询投诉单协商历史](pages/4012691802.md) | `4012691802` | 2025-08-28 02:43:30 | 消费者投诉2.0 > API列表 > 主动查询投诉信息 |
| 581 | [投诉通知回调](pages/4012076174.md) | `4012076174` | 2025-02-19 03:56:03 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 582 | [创建投诉通知回调地址](pages/4012458106.md) | `4012458106` | 2025-08-28 02:43:28 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 583 | [查询投诉通知回调地址](pages/4012459065.md) | `4012459065` | 2025-08-28 02:43:23 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 584 | [更新投诉通知回调地址](pages/4012459287.md) | `4012459287` | 2025-08-28 02:43:25 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 585 | [删除投诉通知回调地址](pages/4012460474.md) | `4012460474` | 2025-08-28 02:43:21 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 586 | [回复用户](pages/4012467213.md) | `4012467213` | 2025-09-01 02:27:29 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 587 | [反馈处理完成](pages/4012467217.md) | `4012467217` | 2025-09-01 02:25:00 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 588 | [更新退款审批结果](pages/4012467218.md) | `4012467218` | 2025-09-01 02:24:26 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 589 | [回复需要即时服务的投诉单](pages/4017151726.md) | `4017151726` | 2026-01-22 08:02:14 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 590 | [图片上传接口](pages/4012467222.md) | `4012467222` | 2025-09-01 02:10:00 | 消费者投诉2.0 > API列表 > 商户反馈图片 |
| 591 | [图片请求接口](pages/4012467223.md) | `4012467223` | 2025-09-02 02:43:19 | 消费者投诉2.0 > API列表 > 商户反馈图片 |
| 592 | [产品介绍](pages/4015792553.md) | `4015792553` | 2025-11-28 08:19:11 | 微信电子发票 |
| 593 | [开发接入准备](pages/4015792554.md) | `4015792554` | 2026-05-20 08:10:24 | 微信电子发票 |
| 594 | [开发指引](pages/4015792556.md) | `4015792556` | 2026-06-09 09:47:17 | 微信电子发票 |
| 595 | [业务示例代码](pages/4016078358.md) | `4016078358` | 2026-06-10 07:28:02 | 微信电子发票 |
| 596 | [常见问题](pages/4016960715.md) | `4016960715` | 2026-05-19 07:40:26 | 微信电子发票 |
| 597 | [获取开通服务商电子发票能力邀请链接](pages/4015941495.md) | `4015941495` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 598 | [获取邀请开通的商户信息](pages/4015941524.md) | `4015941524` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 599 | [检查子商户开票功能状态](pages/4015792561.md) | `4015792561` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 600 | [创建电子发票卡券模板](pages/4015792562.md) | `4015792562` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 601 | [配置开发选项](pages/4015792563.md) | `4015792563` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 602 | [获取用户抬头填写链接](pages/4015770776.md) | `4015770776` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 603 | [获取用户填写抬头信息](pages/4015784260.md) | `4015784260` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 604 | [开具通用行业电子发票](pages/4015792574.md) | `4015792574` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 605 | [开具不动产租赁行业电子发票](pages/4015941740.md) | `4015941740` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 606 | [开具成品油行业电子发票](pages/4016760559.md) | `4016760559` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 607 | [冲红电子发票](pages/4015792575.md) | `4015792575` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 608 | [查询电子发票](pages/4015792567.md) | `4015792567` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 609 | [获取发票下载信息](pages/4015792576.md) | `4015792576` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 610 | [下载发票文件](pages/4015792569.md) | `4015792569` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 611 | [上传电子发票文件](pages/4015792580.md) | `4015792580` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 612 | [将电子发票插入微信用户卡包](pages/4015792579.md) | `4015792579` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 613 | [用户发票抬头填写完成通知](pages/4015792559.md) | `4015792559` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 614 | [发票开具成功通知](pages/4015792570.md) | `4015792570` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 615 | [发票插入用户卡包成功通知](pages/4015792578.md) | `4015792578` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 616 | [发票冲红成功通知](pages/4015792571.md) | `4015792571` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 617 | [发票卡券作废通知](pages/4015792560.md) | `4015792560` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 618 | [成品油单位转换公式](pages/4016730844.md) | `4016730844` | 2025-12-24 06:30:37 | 微信电子发票 > 附录 |
| 619 | [产品介绍](pages/4012062365.md) | `4012062365` | 2024-10-16 07:11:49 | 特约商户进件 |
| 620 | [开发接入准备](pages/4012062375.md) | `4012062375` | 2026-05-19 09:32:37 | 特约商户进件 |
| 621 | [开发指引](pages/4012062379.md) | `4012062379` | 2026-06-09 09:45:48 | 特约商户进件 |
| 622 | [常见问题](pages/4016058480.md) | `4016058480` | 2026-01-23 02:51:54 | 特约商户进件 |
| 623 | [提交申请单](pages/4012719997.md) | `4012719997` | 2025-03-26 06:58:27 | 特约商户进件 > API列表 |
| 624 | [申请单号查询申请状态](pages/4012697052.md) | `4012697052` | 2025-03-24 04:07:15 | 特约商户进件 > API列表 |
| 625 | [业务申请编号查询申请状态](pages/4012697168.md) | `4012697168` | 2025-03-24 04:07:17 | 特约商户进件 > API列表 |
| 626 | [修改结算账户](pages/4012761102.md) | `4012761102` | 2025-01-22 01:35:52 | 特约商户进件 > API列表 |
| 627 | [查询结算账户](pages/4012761113.md) | `4012761113` | 2025-01-21 03:41:29 | 特约商户进件 > API列表 |
| 628 | [查询结算账户修改申请状态](pages/4012761120.md) | `4012761120` | 2025-01-21 03:41:31 | 特约商户进件 > API列表 |
| 629 | [文件上传](pages/4012760490.md) | `4012760490` | 2026-05-09 07:01:44 | 特约商户进件 > API列表 |
| 630 | [视频上传](pages/4012761084.md) | `4012761084` | 2024-11-18 09:25:56 | 特约商户进件 > API列表 |
| 631 | [产品介绍](pages/4012064820.md) | `4012064820` | 2024-10-24 08:22:24 | 商户开户意愿确认 |
| 632 | [开发接入准备](pages/4012064824.md) | `4012064824` | 2026-05-20 08:07:52 | 商户开户意愿确认 |
| 633 | [开发指引](pages/4012064832.md) | `4012064832` | 2026-06-09 09:45:45 | 商户开户意愿确认 |
| 634 | [常见问题](pages/4016644196.md) | `4016644196` | 2026-01-16 03:48:52 | 商户开户意愿确认 |
| 635 | [提交申请单](pages/4012722388.md) | `4012722388` | 2025-01-09 03:10:33 | 商户开户意愿确认 > API列表 |
| 636 | [撤销申请单](pages/4012697627.md) | `4012697627` | 2024-12-04 02:03:31 | 商户开户意愿确认 > API列表 |
| 637 | [查询申请单审核结果](pages/4012697715.md) | `4012697715` | 2024-11-04 07:59:30 | 商户开户意愿确认 > API列表 |
| 638 | [获取商户开户意愿确认状态](pages/4012467549.md) | `4012467549` | 2024-10-24 09:20:46 | 商户开户意愿确认 > API列表 |
| 639 | [图片上传](pages/4012760509.md) | `4012760509` | 2024-11-18 09:25:43 | 商户开户意愿确认 > API列表 |
| 640 | [产品介绍](pages/4012064844.md) | `4012064844` | 2026-03-10 07:23:55 | 商户平台处置通知 |
| 641 | [开发接入准备](pages/4012064851.md) | `4012064851` | 2026-05-19 09:33:15 | 商户平台处置通知 |
| 642 | [开发指引](pages/4012064853.md) | `4012064853` | 2026-06-09 09:45:42 | 商户平台处置通知 |
| 643 | [业务示例代码](pages/4015949382.md) | `4015949382` | 2025-09-03 03:01:42 | 商户平台处置通知 |
| 644 | [查询商户违规通知回调地址](pages/4012471327.md) | `4012471327` | 2025-08-28 09:27:26 | 商户平台处置通知 > API列表 > 商户违规通知回调 |
| 645 | [修改商户违规通知回调地址](pages/4012471330.md) | `4012471330` | 2025-08-28 09:27:19 | 商户平台处置通知 > API列表 > 商户违规通知回调 |
| 646 | [创建商户违规通知回调地址](pages/4012471333.md) | `4012471333` | 2025-08-28 09:27:12 | 商户平台处置通知 > API列表 > 商户违规通知回调 |
| 647 | [删除商户违规通知回调地址](pages/4012471334.md) | `4012471334` | 2025-08-28 09:27:05 | 商户平台处置通知 > API列表 > 商户违规通知回调 |
| 648 | [商户平台处置记录回调通知](pages/4012079216.md) | `4012079216` | 2025-02-19 03:56:03 | 商户平台处置通知 > API列表 > 商户违规通知回调 |
| 649 | [产品介绍](pages/4012064898.md) | `4012064898` | 2026-05-25 07:06:33 | 不活跃商户身份核实 |
| 650 | [开发接入准备](pages/4012064902.md) | `4012064902` | 2026-05-19 09:33:57 | 不活跃商户身份核实 |
| 651 | [开发指引](pages/4012064909.md) | `4012064909` | 2026-06-09 09:45:41 | 不活跃商户身份核实 |
| 652 | [常见问题](pages/4012064915.md) | `4012064915` | 2024-07-24 08:05:05 | 不活跃商户身份核实 |
| 653 | [发起不活跃商户身份核实](pages/4012471357.md) | `4012471357` | 2025-08-08 07:33:04 | 不活跃商户身份核实 > API列表 |
| 654 | [查询不活跃商户身份核实结果](pages/4012471359.md) | `4012471359` | 2025-08-08 08:00:48 | 不活跃商户身份核实 > API列表 |
| 655 | [关键概念](pages/4012064904.md) | `4012064904` | 2024-10-25 02:37:34 | 不活跃商户身份核实 > 附录 |
| 656 | [产品介绍](pages/4012165270.md) | `4012165270` | 2025-11-11 06:26:12 | 商户被管控能力及原因查询 |
| 657 | [查询子商户管控情况](pages/4012803072.md) | `4012803072` | 2025-09-26 09:24:32 | 商户被管控能力及原因查询 > API列表 |
| 658 | [产品介绍](pages/4016022264.md) | `4016022264` | 2025-09-17 04:03:07 | 合作伙伴订阅 |
| 659 | [开发指引](pages/4016022266.md) | `4016022266` | 2025-09-16 03:35:57 | 合作伙伴订阅 |
| 660 | [常见问题](pages/4016550707.md) | `4016550707` | 2025-11-14 07:33:02 | 合作伙伴订阅 |
| 661 | [产品介绍](pages/4012925323.md) | `4012925323` | 2026-05-20 03:21:30 | 微信支付公钥 |
| 662 | [常见问题](pages/4013038589.md) | `4013038589` | 2025-03-04 07:15:22 | 微信支付公钥 |
| 663 | [商户签名验签／加解密测试](pages/4015139289.md) | `4015139289` | 2026-04-08 03:50:21 | 微信支付公钥 > API列表 |
| 664 | [回调接口](pages/4019605946.md) | `4019605946` | 2026-04-10 08:15:23 | 微信支付公钥 > API列表 |
| 665 | [如何从平台证书切换成微信支付公钥](pages/4012925289.md) | `4012925289` | 2024-12-12 02:59:29 | 微信支付公钥 > 附录 |
| 666 | [如何从微信支付公钥切换成平台证书](pages/4015419376.md) | `4015419376` | 2026-03-17 09:45:27 | 微信支付公钥 > 附录 |
| 667 | [产品介绍](pages/4012073044.md) | `4012073044` | 2026-05-21 07:25:38 | 平台证书 |
| 668 | [常见问题](pages/4012073263.md) | `4012073263` | 2024-11-29 09:45:35 | 平台证书 |
| 669 | [下载平台证书](pages/4012715700.md) | `4012715700` | 2024-10-15 08:45:31 | 平台证书 > API列表 |
| 670 | [平台证书更换操作指引](pages/4012073146.md) | `4012073146` | 2024-12-04 06:35:09 | 平台证书 > 附录 |
| 671 | [产品介绍](pages/4012086891.md) | `4012086891` | 2026-02-28 08:04:53 | 平台收付通-电商交易解决方案 |
| 672 | [开发接入准备](pages/4012086921.md) | `4012086921` | 2026-05-19 09:38:35 | 平台收付通-电商交易解决方案 |
| 673 | [消费者投诉2.0](pages/4012072827.md) | `4012072827` | 2025-08-25 10:00:14 | 平台收付通-电商交易解决方案 |
| 674 | [开发指引](pages/4012087137.md) | `4012087137` | 2025-09-26 03:22:56 | 平台收付通-电商交易解决方案 > 商户进件 |
| 675 | [常见问题](pages/4012525423.md) | `4012525423` | 2026-05-26 08:53:06 | 平台收付通-电商交易解决方案 > 商户进件 |
| 676 | [提交申请单](pages/4012713017.md) | `4012713017` | 2025-02-28 12:07:34 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 677 | [通过业务申请编号查询申请状态](pages/4012691376.md) | `4012691376` | 2024-11-28 06:22:29 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 678 | [通过申请单ID查询申请状态](pages/4012691469.md) | `4012691469` | 2024-11-28 06:22:27 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 679 | [修改结算账户](pages/4012761138.md) | `4012761138` | 2026-01-14 06:27:19 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 680 | [查询结算账户](pages/4012761142.md) | `4012761142` | 2026-01-14 06:27:41 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 681 | [查询结算账户修改申请状态](pages/4012761169.md) | `4012761169` | 2025-01-21 03:41:31 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 682 | [文件上传](pages/4012760432.md) | `4012760432` | 2026-05-09 07:02:14 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 683 | [产品介绍](pages/4018153750.md) | `4018153750` | 2026-06-11 07:25:17 | 平台收付通-电商交易解决方案 > 商户注销 |
| 684 | [商户注销资格校验](pages/4016420099.md) | `4016420099` | 2025-11-05 09:41:04 | 平台收付通-电商交易解决方案 > 商户注销 > 注销预校验 > API列表 |
| 685 | [提交注销提现申请](pages/4013892756.md) | `4013892756` | 2025-03-13 04:54:44 | 平台收付通-电商交易解决方案 > 商户注销 > 注销提现（新流程） > API列表 |
| 686 | [商户申请单号查询申请单状态](pages/4013892759.md) | `4013892759` | 2025-09-26 02:25:46 | 平台收付通-电商交易解决方案 > 商户注销 > 注销提现（新流程） > API列表 |
| 687 | [微信支付申请单号查询申请单状态](pages/4013892765.md) | `4013892765` | 2025-09-26 02:25:56 | 平台收付通-电商交易解决方案 > 商户注销 > 注销提现（新流程） > API列表 |
| 688 | [常见问题](pages/4015943239.md) | `4015943239` | 2025-11-07 06:48:10 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） |
| 689 | [提交注销申请单](pages/4012476217.md) | `4012476217` | 2025-02-17 10:16:34 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销申请 > 注销申请单 |
| 690 | [查询注销单状态](pages/4012476223.md) | `4012476223` | 2024-11-05 02:04:20 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销申请 > 注销申请单 |
| 691 | [图片上传](pages/4012691710.md) | `4012691710` | 2024-11-05 02:05:52 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销申请 > 图片上传 |
| 692 | [提交已注销商户号可用余额提现申请单](pages/4012488950.md) | `4012488950` | 2025-01-09 03:10:34 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销后提现 > API列表 |
| 693 | [商户提现申请单号查询提现申请单状态](pages/4012476164.md) | `4012476164` | 2024-11-05 02:15:27 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销后提现 > API列表 |
| 694 | [微信支付提现申请单号查询提现申请单状态](pages/4012778400.md) | `4012778400` | 2024-11-05 02:16:19 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销后提现 > API列表 |
| 695 | [开发指引](pages/4012088031.md) | `4012088031` | 2026-06-10 07:28:44 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 |
| 696 | [常见问题](pages/4012525474.md) | `4012525474` | 2026-05-09 08:54:23 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 |
| 697 | [APP下单](pages/4012714669.md) | `4012714669` | 2024-10-24 03:39:28 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > APP支付 |
| 698 | [APP调起支付](pages/4012090168.md) | `4012090168` | 2025-02-20 03:00:52 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > APP支付 |
| 699 | [JSAPI下单](pages/4012714678.md) | `4012714678` | 2024-10-24 03:49:34 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > JSAPI支付 |
| 700 | [JSAPI调起支付](pages/4012090156.md) | `4012090156` | 2025-02-26 07:08:25 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > JSAPI支付 |
| 701 | [Native下单](pages/4012714902.md) | `4012714902` | 2024-10-24 06:18:18 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > Native支付 |
| 702 | [Native调起支付](pages/4012090180.md) | `4012090180` | 2025-03-21 07:41:33 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > Native支付 |
| 703 | [小程序下单](pages/4012714911.md) | `4012714911` | 2024-10-24 03:49:34 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 小程序支付 |
| 704 | [小程序调起支付](pages/4012090181.md) | `4012090181` | 2025-02-26 07:10:30 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 小程序支付 |
| 705 | [H5下单](pages/4012714759.md) | `4012714759` | 2024-10-24 06:27:02 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > H5支付 |
| 706 | [H5调起支付](pages/4012090177.md) | `4012090177` | 2024-12-23 02:14:31 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > H5支付 |
| 707 | [微信支付订单号查询订单](pages/4012760565.md) | `4012760565` | 2025-04-07 01:51:41 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 公共API |
| 708 | [微信支付商户订单号查询订单](pages/4012760568.md) | `4012760568` | 2025-04-07 01:51:51 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 公共API |
| 709 | [关闭订单](pages/4012760574.md) | `4012760574` | 2025-04-07 01:51:49 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 公共API |
| 710 | [支付结果通知](pages/4012090195.md) | `4012090195` | 2025-04-07 01:52:18 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 公共API |
| 711 | [开发指引](pages/4012089542.md) | `4012089542` | 2026-06-10 07:28:43 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 |
| 712 | [常见问题](pages/4012525491.md) | `4012525491` | 2026-05-09 08:54:07 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 |
| 713 | [合单下单-JSAPI](pages/4012760615.md) | `4012760615` | 2024-11-14 08:12:09 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > JSAPI合单支付 |
| 714 | [JSAPI调起支付](pages/4012090843.md) | `4012090843` | 2025-02-19 03:55:15 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > JSAPI合单支付 |
| 715 | [合单下单-APP](pages/4012760622.md) | `4012760622` | 2024-11-14 08:12:11 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > APP合单支付 |
| 716 | [APP调起支付](pages/4012090949.md) | `4012090949` | 2025-03-28 10:57:37 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > APP合单支付 |
| 717 | [合单下单-H5](pages/4012760626.md) | `4012760626` | 2024-11-14 08:12:10 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > H5合单支付 |
| 718 | [H5调起支付](pages/4012091014.md) | `4012091014` | 2024-10-28 02:58:30 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > H5合单支付 |
| 719 | [合单下单-NATIVE](pages/4012760629.md) | `4012760629` | 2024-11-14 08:12:12 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > Native合单支付 |
| 720 | [Native调起支付](pages/4012091224.md) | `4012091224` | 2024-10-28 02:54:47 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > Native合单支付 |
| 721 | [合单下单-小程序](pages/4012760633.md) | `4012760633` | 2024-11-14 08:12:09 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 小程序合单支付 |
| 722 | [小程序调起支付](pages/4012091236.md) | `4012091236` | 2025-02-18 11:41:37 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 小程序合单支付 |
| 723 | [合单查询订单](pages/4012761049.md) | `4012761049` | 2024-10-24 07:08:30 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 公共API |
| 724 | [合单关闭订单](pages/4012761093.md) | `4012761093` | 2024-10-24 07:09:52 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 公共API |
| 725 | [支付通知](pages/4012237246.md) | `4012237246` | 2024-11-18 09:25:58 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 公共API |
| 726 | [开发指引](pages/4012087888.md) | `4012087888` | 2026-06-10 07:27:51 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 |
| 727 | [业务示例代码](pages/4015870957.md) | `4015870957` | 2026-06-09 09:46:47 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 |
| 728 | [常见问题](pages/4012525463.md) | `4012525463` | 2026-05-21 07:43:02 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 |
| 729 | [请求分账](pages/4012691594.md) | `4012691594` | 2025-09-29 06:45:52 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 730 | [查询分账结果](pages/4012477734.md) | `4012477734` | 2025-09-29 02:09:30 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 731 | [请求分账回退](pages/4012477737.md) | `4012477737` | 2025-09-29 02:06:15 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 732 | [查询分账回退结果](pages/4012477740.md) | `4012477740` | 2025-09-29 02:04:34 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 733 | [解冻剩余资金](pages/4012477745.md) | `4012477745` | 2025-09-29 02:03:23 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 734 | [查询订单剩余待分金额](pages/4012477751.md) | `4012477751` | 2025-09-29 02:02:25 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 735 | [添加分账接收方](pages/4012477758.md) | `4012477758` | 2025-09-29 02:01:53 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 736 | [删除分账接收方](pages/4012477759.md) | `4012477759` | 2025-09-29 02:00:58 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 737 | [分账动账通知](pages/4012116672.md) | `4012116672` | 2025-02-19 03:56:03 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 738 | [分账失败处理指引](pages/4015504955.md) | `4015504955` | 2025-07-04 03:08:08 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > 附录 |
| 739 | [业务示例代码](pages/4015593692.md) | `4015593692` | 2026-06-10 07:27:50 | 平台收付通-电商交易解决方案 > 补差与分账 > 补差 |
| 740 | [常见问题](pages/4015942503.md) | `4015942503` | 2026-01-22 06:48:53 | 平台收付通-电商交易解决方案 > 补差与分账 > 补差 |
| 741 | [请求补差](pages/4012477631.md) | `4012477631` | 2024-11-04 11:30:10 | 平台收付通-电商交易解决方案 > 补差与分账 > 补差 > API列表 |
| 742 | [请求补差回退](pages/4012477636.md) | `4012477636` | 2024-11-04 11:30:36 | 平台收付通-电商交易解决方案 > 补差与分账 > 补差 > API列表 |
| 743 | [取消补差](pages/4012477639.md) | `4012477639` | 2024-10-24 08:47:04 | 平台收付通-电商交易解决方案 > 补差与分账 > 补差 > API列表 |
| 744 | [业务示例代码](pages/4015217874.md) | `4015217874` | 2026-06-10 07:27:49 | 平台收付通-电商交易解决方案 > 交易退款 |
| 745 | [申请退款](pages/4012476892.md) | `4012476892` | 2024-11-04 11:33:40 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 746 | [查询单笔退款（按微信支付退款单号）](pages/4012476908.md) | `4012476908` | 2024-11-04 11:36:44 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 747 | [查询单笔退款（按商户退款单号）](pages/4012476911.md) | `4012476911` | 2024-11-04 11:36:11 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 748 | [退款结果通知](pages/4012124635.md) | `4012124635` | 2024-11-18 09:25:58 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 749 | [查询垫付回补结果](pages/4012476916.md) | `4012476916` | 2024-11-04 11:40:17 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 750 | [垫付退款回补](pages/4012476927.md) | `4012476927` | 2024-11-04 11:41:31 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 751 | [发起异常退款](pages/4015181616.md) | `4015181616` | 2025-06-06 08:23:46 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 752 | [常见问题](pages/4016644075.md) | `4016644075` | 2025-11-21 03:07:14 | 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 |
| 753 | [查询二级商户账户实时余额](pages/4012476690.md) | `4012476690` | 2024-11-04 11:47:34 | 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 > API列表 |
| 754 | [查询二级商户账户日终余额](pages/4012476693.md) | `4012476693` | 2024-11-04 11:47:25 | 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 > API列表 |
| 755 | [查询平台账户实时余额](pages/4012476700.md) | `4012476700` | 2024-11-04 11:46:09 | 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 > API列表 |
| 756 | [查询平台账户日终余额](pages/4012476702.md) | `4012476702` | 2024-11-04 11:46:15 | 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 > API列表 |
| 757 | [业务示例代码](pages/4019899593.md) | `4019899593` | 2026-06-10 07:27:45 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 |
| 758 | [常见问题](pages/4014075940.md) | `4014075940` | 2025-12-19 02:57:09 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 |
| 759 | [二级商户预约提现](pages/4012476652.md) | `4012476652` | 2024-12-19 07:33:30 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 760 | [二级商户查询预约提现状态（根据商户预约提现单号查询）](pages/4012476656.md) | `4012476656` | 2024-12-19 07:33:26 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 761 | [二级商户查询预约提现状态（根据微信支付预约提现单号查询）](pages/4012476665.md) | `4012476665` | 2024-12-19 07:33:24 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 762 | [平台预约提现](pages/4012476670.md) | `4012476670` | 2024-12-19 07:33:21 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 763 | [平台查询预约提现状态（根据商户预约提现单号查询）](pages/4012476672.md) | `4012476672` | 2024-12-19 07:33:18 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 764 | [平台查询预约提现状态（根据微信支付预约提现单号查询）](pages/4012476674.md) | `4012476674` | 2024-12-19 07:33:16 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 765 | [二级商户按日终余额预约提现](pages/4013328143.md) | `4013328143` | 2024-12-19 08:08:05 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 766 | [查询二级商户按日终余额预约提现状态](pages/4013328163.md) | `4013328163` | 2024-12-19 08:08:05 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 767 | [按日下载提现异常文件](pages/4012476678.md) | `4012476678` | 2024-12-19 07:11:13 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 768 | [商户提现状态变更通知](pages/4013049135.md) | `4013049135` | 2025-02-24 09:49:47 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 769 | [业务示例代码](pages/4016062108.md) | `4016062108` | 2025-12-04 01:55:05 | 平台收付通-电商交易解决方案 > 账单下载 |
| 770 | [申请交易账单](pages/4012760667.md) | `4012760667` | 2025-04-07 01:51:03 | 平台收付通-电商交易解决方案 > 账单下载 > API列表 |
| 771 | [申请资金账单](pages/4012760672.md) | `4012760672` | 2025-04-07 01:50:55 | 平台收付通-电商交易解决方案 > 账单下载 > API列表 |
| 772 | [申请分账账单](pages/4012761131.md) | `4012761131` | 2025-01-20 08:06:16 | 平台收付通-电商交易解决方案 > 账单下载 > API列表 |
| 773 | [下载账单](pages/4012124894.md) | `4012124894` | 2025-04-16 09:44:14 | 平台收付通-电商交易解决方案 > 账单下载 > API列表 |
| 774 | [申请二级商户资金账单](pages/4012760697.md) | `4012760697` | 2024-10-23 08:14:36 | 平台收付通-电商交易解决方案 > 账单下载 > API列表 |
| 775 | [申请单个子商户资金账单](pages/4012760249.md) | `4012760249` | 2024-10-21 08:45:00 | 平台收付通-电商交易解决方案 > 账单下载 > API列表 |
| 776 | [下载单个子商户/二级商户资金账单](pages/4014314390.md) | `4014314390` | 2025-04-16 03:21:56 | 平台收付通-电商交易解决方案 > 账单下载 > API列表 |
| 777 | [业务示例代码](pages/4015593257.md) | `4015593257` | 2026-06-10 07:27:44 | 平台收付通-电商交易解决方案 > 跨境付款 |
| 778 | [查询订单剩余可出境余额](pages/4012476109.md) | `4012476109` | 2024-11-05 02:17:34 | 平台收付通-电商交易解决方案 > 跨境付款 > API列表 |
| 779 | [申请资金出境](pages/4012476113.md) | `4012476113` | 2024-11-05 02:22:26 | 平台收付通-电商交易解决方案 > 跨境付款 > API列表 |
| 780 | [查询出境结果](pages/4012476127.md) | `4012476127` | 2024-11-05 02:23:59 | 平台收付通-电商交易解决方案 > 跨境付款 > API列表 |
| 781 | [获取购付汇账单文件下载链接](pages/4012476132.md) | `4012476132` | 2024-11-05 02:32:27 | 平台收付通-电商交易解决方案 > 跨境付款 > API列表 |
| 782 | [APIv3概述](pages/4012081673.md) | `4012081673` | 2024-11-21 08:19:57 | Optional > 开发须知 |
| 783 | [总述-APIv3如何签名和验签](pages/4012365870.md) | `4012365870` | 2024-11-21 10:50:08 | Optional > 开发须知 |
| 784 | [基本规则](pages/4012081726.md) | `4012081726` | 2024-07-25 02:06:07 | Optional > 开发须知 > 接口规则说明 |
| 785 | [HTTP状态码](pages/4012081727.md) | `4012081727` | 2024-07-25 02:07:36 | Optional > 开发须知 > 接口规则说明 |
| 786 | [开发必要参数说明](pages/4013080340.md) | `4013080340` | 2026-06-02 08:22:05 | Optional > 开发须知 > 开发参数申请和配置 |
| 787 | [mchid与appid申请](pages/4012081990.md) | `4012081990` | 2025-10-28 03:00:48 | Optional > 开发须知 > 开发参数申请和配置 |
| 788 | [管理商户号绑定的APPID账号](pages/4016329059.md) | `4016329059` | 2025-10-28 03:00:48 | Optional > 开发须知 > 开发参数申请和配置 |
| 789 | [配置APIv3密钥](pages/4012081991.md) | `4012081991` | 2025-10-28 03:00:48 | Optional > 开发须知 > 开发参数申请和配置 |
| 790 | [品牌经营API开发必要参数说明](pages/4015981654.md) | `4015981654` | 2025-12-15 01:50:19 | Optional > 开发须知 > 开发参数申请和配置 |
| 791 | [平台员工权限管理](pages/4013080349.md) | `4013080349` | 2025-09-19 01:36:32 | Optional > 开发须知 > 开发参数申请和配置 |
| 792 | [申请商户API证书](pages/4012081992.md) | `4012081992` | 2025-10-28 03:01:36 | Optional > 开发须知 > 开发参数申请和配置 > 商户API证书管理 |
| 793 | [如何更换商户API证书？](pages/4013058943.md) | `4013058943` | 2024-11-20 03:18:41 | Optional > 开发须知 > 开发参数申请和配置 > 商户API证书管理 |
| 794 | [请求参数里带Path参数（路径参数），如何计算签名](pages/4012365862.md) | `4012365862` | 2025-02-18 08:09:32 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 795 | [请求参数里带Body参数(包体参数），如何计算签名](pages/4012365864.md) | `4012365864` | 2025-02-18 09:53:43 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 796 | [请求参数里有Query（查询参数），如何计算签名](pages/4012365865.md) | `4012365865` | 2025-02-18 09:53:41 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 797 | [图片上传接口，如何计算签名](pages/4012365863.md) | `4012365863` | 2025-03-25 03:03:49 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 798 | [APP调起支付签名](pages/4012365868.md) | `4012365868` | 2025-03-26 09:28:08 | Optional > 开发须知 > 如何签名 > 如何构造调起支付签名 |
| 799 | [JSAPI调起支付签名](pages/4012365867.md) | `4012365867` | 2025-03-26 09:28:07 | Optional > 开发须知 > 如何签名 > 如何构造调起支付签名 |
| 800 | [小程序调起支付签名](pages/4012365869.md) | `4012365869` | 2025-03-26 09:28:05 | Optional > 开发须知 > 如何签名 > 如何构造调起支付签名 |
| 801 | [如何使用微信支付公钥验签](pages/4013059017.md) | `4013059017` | 2024-11-20 06:55:05 | Optional > 开发须知 > 如何验签 |
| 802 | [如何使用平台证书验签名](pages/4013059030.md) | `4013059030` | 2024-11-29 09:43:48 | Optional > 开发须知 > 如何验签 > 如何使用平台证书验签 |
| 803 | [如何使用签名/验签工具](pages/4012365880.md) | `4012365880` | 2024-12-27 04:05:13 | Optional > 开发须知 > 如何验签 > 如何使用平台证书验签 |
| 804 | [如何使用微信支付公钥加密敏感字段](pages/4013059044.md) | `4013059044` | 2025-03-19 08:49:11 | Optional > 开发须知 > 如何加解密敏感字段 |
| 805 | [如何使用平台证书加密敏感字段](pages/4013059053.md) | `4013059053` | 2025-03-19 08:49:03 | Optional > 开发须知 > 如何加解密敏感字段 |
| 806 | [如何使用API证书解密敏感字段](pages/4013059060.md) | `4013059060` | 2024-11-20 03:29:55 | Optional > 开发须知 > 如何加解密敏感字段 |
| 807 | [如何解密回调报文和平台证书](pages/4012082320.md) | `4012082320` | 2024-11-29 08:22:52 | Optional > 开发须知 > 如何解密微信支付回调报文 |
| 808 | [报错：HTTP header缺少微信支付平台证书序列号(Wechatpay-Serial)](pages/4012365874.md) | `4012365874` | 2024-11-19 09:07:14 | Optional > 开发须知 > 常见问题 |
| 809 | [报错：Http头Authorization值格式错误，请参考《微信支付商户REST API签名规则》或者“Authorization不合法”](pages/4012365872.md) | `4012365872` | 2026-01-23 03:31:55 | Optional > 开发须知 > 常见问题 |
| 810 | [报错：商户证书序列号有误。请使用签名私钥匹配的证书序列号](pages/4012365873.md) | `4012365873` | 2024-12-12 03:12:16 | Optional > 开发须知 > 常见问题 |
| 811 | [报错：状态码401或者“错误的签名，验签失败”或者“签名错误，请检查后再试”](pages/4012365875.md) | `4012365875` | 2024-12-12 03:12:14 | Optional > 开发须知 > 常见问题 |
| 812 | [调起支付报错：支付验证签名失败](pages/4012365876.md) | `4012365876` | 2025-03-26 09:28:04 | Optional > 开发须知 > 常见问题 |
| 813 | [使用Java加载密钥时，抛出异常InvalidKeyException: Illegal key size](pages/4013059103.md) | `4013059103` | 2024-11-20 03:37:11 | Optional > 开发须知 > 常见问题 |
| 814 | [使用Java解密时，抛出异常AEADBadTagException: Tag mismatch](pages/4013059153.md) | `4013059153` | 2024-11-20 03:38:02 | Optional > 开发须知 > 常见问题 |
| 815 | [请求返回{"code":"PARAM_ERROR","message":"平台证书序列号Wechatpay-Serial错误"}](pages/4013059161.md) | `4013059161` | 2024-11-20 03:38:49 | Optional > 开发须知 > 常见问题 |
| 816 | [为什么微信支付的回调缺少签名的几个HTTP头？](pages/4013059166.md) | `4013059166` | 2024-11-20 03:39:20 | Optional > 开发须知 > 常见问题 |
| 817 | [如何在程序中加载商户API证书私钥](pages/4013059175.md) | `4013059175` | 2025-12-25 06:37:41 | Optional > 开发须知 > 常见问题 |
| 818 | [如何查看商户API证书或平台证书序列号？](pages/4013059181.md) | `4013059181` | 2024-11-26 02:43:01 | Optional > 开发须知 > 常见问题 |
| 819 | [为什么请求返回401 Unauthorized？](pages/4012082324.md) | `4012082324` | 2024-11-25 08:53:06 | Optional > 开发须知 > 常见问题 |
| 820 | [验证微信支付响应的签名报错：签名验证失败](pages/4016241895.md) | `4016241895` | 2025-10-14 06:39:36 | Optional > 开发须知 > 常见问题 |
| 821 | [调用接口报错：“平台私钥解密失败”](pages/4016913182.md) | `4016913182` | 2025-12-19 02:59:24 | Optional > 开发须知 > 常见问题 |
| 822 | [跨城冗灾升级指引](pages/4012082567.md) | `4012082567` | 2025-03-21 07:37:49 | Optional > 最佳实践 |
| 823 | [支付回调和查单实现指引](pages/4012082568.md) | `4012082568` | 2024-12-18 07:43:24 | Optional > 最佳实践 |
| 824 | [专线商户Notify升级指引](pages/4012082569.md) | `4012082569` | 2024-07-25 03:04:49 | Optional > 最佳实践 |
| 825 | [回调通知注意事项](pages/4012082570.md) | `4012082570` | 2024-07-25 03:04:49 | Optional > 最佳实践 |
| 826 | [最佳安全实践](pages/4012082456.md) | `4012082456` | 2024-11-27 09:15:00 | Optional > 最佳实践 > API安全最佳实践 |
| 827 | [安全漏洞checklist](pages/4013059657.md) | `4013059657` | 2024-11-27 09:14:52 | Optional > 最佳实践 > API安全最佳实践 |
| 828 | [系统漏洞检测及修复](pages/4013059668.md) | `4013059668` | 2025-03-21 07:40:38 | Optional > 最佳实践 > API安全最佳实践 |
| 829 | [Web漏洞检测及修复](pages/4013059740.md) | `4013059740` | 2025-03-21 08:53:52 | Optional > 最佳实践 > API安全最佳实践 |
| 830 | [最新安全漏洞及修复](pages/4013059970.md) | `4013059970` | 2024-11-27 09:14:33 | Optional > 最佳实践 > API安全最佳实践 |
| 831 | [密钥泄漏修复指引](pages/4012082455.md) | `4012082455` | 2024-12-24 01:54:38 | Optional > 最佳实践 > API安全最佳实践 |
| 832 | [国家商用密码简介](pages/4012082627.md) | `4012082627` | 2024-07-25 03:09:50 | Optional > 国家商用密码接入指南 |
| 833 | [获取国家商用密码证书和密钥](pages/4012082628.md) | `4012082628` | 2024-07-25 03:09:50 | Optional > 国家商用密码接入指南 |
| 834 | [APIv3接口使用国家商用密码指引](pages/4012082629.md) | `4012082629` | 2024-07-25 03:09:50 | Optional > 国家商用密码接入指南 |
| 835 | [开户银行全称对照表](pages/4012082812.md) | `4012082812` | 2024-07-25 03:24:06 | Optional > 对照表 |
| 836 | [开户银行对照表](pages/4012082813.md) | `4012082813` | 2025-02-19 07:30:19 | Optional > 对照表 |
| 837 | [银行类型对照表](pages/4012082814.md) | `4012082814` | 2024-07-25 03:24:06 | Optional > 对照表 |
| 838 | [省市区编号对照表](pages/4012082815.md) | `4012082815` | 2024-07-25 03:24:06 | Optional > 对照表 |
| 839 | [优惠费率活动对照表](pages/4012082816.md) | `4012082816` | 2024-12-26 08:48:22 | Optional > 对照表 |
| 840 | [跨境电商二级商户费率对照表](pages/4012082817.md) | `4012082817` | 2024-07-25 03:24:06 | Optional > 对照表 |
| 841 | [商户行业编码](pages/4012082818.md) | `4012082818` | 2024-07-25 03:24:06 | Optional > 对照表 |
| 842 | [特殊行业ID对照表](pages/4012082819.md) | `4012082819` | 2024-07-25 03:24:06 | Optional > 对照表 |
| 843 | [接入模式](pages/4012081931.md) | `4012081931` | 2026-06-01 06:16:40 | Optional > 名词表 |
| 844 | [支付产品](pages/4012081932.md) | `4012081932` | 2024-07-25 02:23:51 | Optional > 名词表 |
| 845 | [业务平台](pages/4012081933.md) | `4012081933` | 2024-07-25 02:23:51 | Optional > 名词表 |
| 846 | [业务系统](pages/4012081934.md) | `4012081934` | 2024-07-25 02:23:51 | Optional > 名词表 |
| 847 | [参数说明](pages/4012081935.md) | `4012081935` | 2024-10-29 02:13:52 | Optional > 名词表 |
| 848 | [常见问题](pages/4016183684.md) | `4016183684` | 2026-04-28 06:50:12 | Optional > 名词表 |
| 849 | [微信支付链路界面与交互规范](pages/4020527499.md) | `4020527499` | 2026-05-19 02:15:32 | Optional > 服务运营规范 |
| 850 | [Postman调试工具](pages/4012083114.md) | `4012083114` | 2024-11-29 09:45:15 | Optional > 开发工具 |
| 851 | [平台证书下载工具](pages/4012083115.md) | `4012083115` | 2024-11-27 09:13:57 | Optional > 开发工具 |
| 852 | [验签工具](pages/4012083116.md) | `4012083116` | 2025-01-03 07:02:48 | Optional > 开发工具 |
| 853 | [产品介绍](pages/4012083118.md) | `4012083118` | 2025-03-21 07:39:41 | Optional > 网络云排查 |
| 854 | [网络问题排查指南](pages/4012083119.md) | `4012083119` | 2025-03-21 07:39:03 | Optional > 网络云排查 |
| 855 | [常见问题](pages/4012083120.md) | `4012083120` | 2024-07-25 03:43:58 | Optional > 网络云排查 |
| 856 | [产品介绍](pages/4012083122.md) | `4012083122` | 2024-07-25 03:43:58 | Optional > 安全医生 |
| 857 | [诊断链接绑定指引](pages/4012083123.md) | `4012083123` | 2024-07-25 03:43:58 | Optional > 安全医生 |
| 858 | [安全联系人设置指引](pages/4012083124.md) | `4012083124` | 2024-07-25 03:43:58 | Optional > 安全医生 |
| 859 | [SDK概述](pages/4012083109.md) | `4012083109` | 2026-04-24 09:22:07 | Optional > SDK |
| 860 | [使用 Java SDK](pages/4012083111.md) | `4012083111` | 2025-05-29 03:32:06 | Optional > SDK |
| 861 | [使用 PHP SDK](pages/4012083112.md) | `4012083112` | 2025-05-29 03:32:04 | Optional > SDK |
| 862 | [使用 Go SDK](pages/4012083113.md) | `4012083113` | 2025-05-29 03:36:58 | Optional > SDK |

</details>