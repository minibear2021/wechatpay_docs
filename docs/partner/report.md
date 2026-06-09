# 微信支付文档更新报告 - 合作伙伴

**文档类型**: 合作伙伴 (partner)
**生成时间**: 20260609_013357
**文档总数**: 0
**数据来源**: https://pay.weixin.qq.com/doc/v3/partner/llms.txt

## 变更概览

- 新增: 0 个页面
- 删除: 859 个页面
- 修改: 0 个页面
- 成功拉取: 0 个页面
- 拉取失败: 0 个页面
- llms.txt 变更: 是

## llms.txt 变更

```diff
--- llms_old.txt
+++ llms.txt
@@ -1,1219 +1,6 @@
->更新时间：2026.06.05
+>更新时间：2026.06.08
 
 # 微信支付合作伙伴平台文档中心
 
 > 微信支付合作伙伴（服务商）文档中心为服务商提供代特约商户接入微信支付的完整技术文档。支付产品涵盖 JSAPI 支付、APP 支付、H5 支付、Native 支付、小程序支付、合单支付、刷脸支付、医保支付等服务商模式收款方式。运营工具包括微信支付分、代金券、支付有礼、现金红包、智慧商圈、微信电子发票、点金计划等。商户管理提供特约商户进件、开户意愿确认、商户处置通知等能力。品牌经营涵盖商家名片、商家名片会员、摇一摇有优惠、商品券（单券/多次优惠）、品牌门店等。此外提供平台收付通电商交易解决方案、分账、连锁品牌分账、清关报关及消费者投诉处理等扩展能力。文档包含产品介绍、开发指引、API 列表及常见问题
 
-## Skills
-> Skill 为接入微信支付基础支付、商品券的开发者提供了一站式的智能辅助能力，包括支付方式选型、券类型选型、示例代码检索、业务知识查询、接入质量评估和接口报错排查。
-
-- [商品券接入Skill](https://pay.weixin.qq.com/doc/v3/partner/4018929846.md)
-- [基础支付接入Skill](https://pay.weixin.qq.com/doc/v3/partner/4019636341.md)
-
-## 示例代码
-> 为使用 Go、Java 接入微信支付的开发者提供了一系列实用的功能，包括 JSON 处理、密钥加载、加密签名、请求头构建、响应验证等。
-
-- [Go](https://pay.weixin.qq.com/doc/v3/partner/4015119446.md)
-- [Java](https://pay.weixin.qq.com/doc/v3/partner/4014985777.md)
-
-## 付款码支付（V2）
-> 付款码支付是微信支付面向线下商户的面对面收银产品。用户出示微信付款码，商户用扫码设备读取后，收银系统调用接口发起支付。适用于商超、餐饮、医院、景区等实体门店，到账快、操作简便、适配各类收银设备。
-
-- [付款码支付（V2）](https://pay.weixin.qq.com/doc/v3/partner/4012851192.md)
-## 刷脸支付
-> 微信刷脸支付是结合了生物识别、AI人工智能、大数据智能风控、3D摄像头等先进技术打造的创新支付方式。用户在集成微信刷脸支付SDK的线下机具上"刷脸"即可完成支付。
-
-- [刷脸支付](https://pay.weixin.qq.com/doc/v3/partner/4012851199.md)
-## JSAPI支付
-> JSAPI 支付是微信支付面向微信内置浏览器场景的收款产品，支持用户在微信内完成选购、确认支付、验密扣款全流程，支付后可返回商户页面，主要用于公众号、微信内网页收款场景。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012069852.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012069853.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012069859.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4013334850.md)
-### API列表
-- [JSAPI/小程序下单](https://pay.weixin.qq.com/doc/v3/partner/4012738519.md)
-- [JSAPI调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012069855.md)
-- [微信支付订单号查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012738964.md)
-- [关闭订单](https://pay.weixin.qq.com/doc/v3/partner/4012739019.md)
-- [支付成功回调通知](https://pay.weixin.qq.com/doc/v3/partner/4012085146.md)
-- [商户订单号查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012739008.md)
-- [申请退款](https://pay.weixin.qq.com/doc/v3/partner/4012739034.md)
-- [查询单笔退款（按商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4012739043.md)
-- [发起异常退款](https://pay.weixin.qq.com/doc/v3/partner/4013335389.md)
-- [退款结果回调通知](https://pay.weixin.qq.com/doc/v3/partner/4012085298.md)
-- [申请所有/单个子商户交易账单](https://pay.weixin.qq.com/doc/v3/partner/4012739068.md)
-- [申请服务商资金账单](https://pay.weixin.qq.com/doc/v3/partner/4012739125.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4012085421.md)
-### 附录
-- [管理商户号绑定的APPID账号](https://pay.weixin.qq.com/doc/v3/partner/4013335081.md)
-- [配置JSAPI支付授权目录](https://pay.weixin.qq.com/doc/v3/partner/4013335127.md)
-## APP支付
-> APP 支付为商户提供移动端 APP 内的微信支付能力，用户在商户 APP 中唤起微信完成支付后返回该应用，适用于电商、游戏、生活服务等各类独立 APP 的支付场景。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4013080227.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4013080228.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4013080246.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4013080245.md)
-### API列表
-- [APP下单](https://pay.weixin.qq.com/doc/v3/partner/4013080231.md)
-- [APP调起支付](https://pay.weixin.qq.com/doc/v3/partner/4013080233.md)
-- [微信支付订单号查询订单](https://pay.weixin.qq.com/doc/v3/partner/4013080234.md)
-- [商户订单号查询订单](https://pay.weixin.qq.com/doc/v3/partner/4013080235.md)
-- [关闭订单](https://pay.weixin.qq.com/doc/v3/partner/4013080236.md)
-- [支付成功回调通知](https://pay.weixin.qq.com/doc/v3/partner/4013080237.md)
-- [申请退款](https://pay.weixin.qq.com/doc/v3/partner/4013080238.md)
-- [查询单笔退款（按商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4013080239.md)
-- [发起异常退款](https://pay.weixin.qq.com/doc/v3/partner/4013080240.md)
-- [退款结果通知](https://pay.weixin.qq.com/doc/v3/partner/4013080241.md)
-- [申请所有/单个子商户交易账单](https://pay.weixin.qq.com/doc/v3/partner/4013080242.md)
-- [申请服务商资金账单](https://pay.weixin.qq.com/doc/v3/partner/4013080243.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4013080230.md)
-### 附录
-- [管理商户号绑定的APPID账号](https://pay.weixin.qq.com/doc/v3/partner/4013357894.md)
-- [OpenSDK接入指南](https://pay.weixin.qq.com/doc/v3/partner/4013369798.md)
-## H5支付
-> H5 支付为商户提供在手机浏览器网页（非微信客户端内部浏览器）中使用微信支付收款的能力，用户在浏览器发起支付时会跳转到微信内，支付后可返回浏览器中商户的H5页面。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012074916.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012074917.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012074915.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4013336079.md)
-### API列表
-- [H5下单](https://pay.weixin.qq.com/doc/v3/partner/4012738604.md)
-- [H5调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012085683.md)
-- [支付成功回调通知](https://pay.weixin.qq.com/doc/v3/partner/4012085680.md)
-- [微信支付订单号查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012738969.md)
-- [商户订单号查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012759661.md)
-- [关闭订单](https://pay.weixin.qq.com/doc/v3/partner/4012759669.md)
-- [申请退款](https://pay.weixin.qq.com/doc/v3/partner/4012759673.md)
-- [查询单笔退款（通过商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4012759680.md)
-- [发起异常退款](https://pay.weixin.qq.com/doc/v3/partner/4013351901.md)
-- [退款结果通知](https://pay.weixin.qq.com/doc/v3/partner/4012085681.md)
-- [申请所有/单个子商户交易账单](https://pay.weixin.qq.com/doc/v3/partner/4012759683.md)
-- [申请服务商资金账单](https://pay.weixin.qq.com/doc/v3/partner/4012759690.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4012085682.md)
-### 附录
-- [管理商户号绑定的APPID账号](https://pay.weixin.qq.com/doc/v3/partner/4013336007.md)
-- [配置H5支付域名](https://pay.weixin.qq.com/doc/v3/partner/4013336019.md)
-- [H5收银台适老化字体规范](https://pay.weixin.qq.com/doc/v3/partner/4013358769.md)
-- [获取用户ip指引](https://pay.weixin.qq.com/doc/v3/partner/4018675960.md)
-## Native支付
-> Native 支付即扫码支付，商户通过接口生成支付二维码，用户使用微信扫码即可完成付款，适用于门店、线下商超、自助设备等线下场景，接入简单、稳定高效，是线下商户主流收款方式之一。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012076267.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012076268.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012076269.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4013352076.md)
-### API列表
-- [Native下单](https://pay.weixin.qq.com/doc/v3/partner/4012738659.md)
-- [Native调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012085878.md)
-- [支付成功回调通知](https://pay.weixin.qq.com/doc/v3/partner/4012085875.md)
-- [关闭订单](https://pay.weixin.qq.com/doc/v3/partner/4012759725.md)
-- [微信支付订单号查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012738971.md)
-- [商户订单号查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012759714.md)
-- [申请退款](https://pay.weixin.qq.com/doc/v3/partner/4012759727.md)
-- [查询单笔退款（通过商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4012759733.md)
-- [发起异常退款](https://pay.weixin.qq.com/doc/v3/partner/4013352066.md)
-- [退款结果回调通知](https://pay.weixin.qq.com/doc/v3/partner/4012085876.md)
-- [申请所有/单个子商户交易账单](https://pay.weixin.qq.com/doc/v3/partner/4012759737.md)
-- [申请服务商资金账单](https://pay.weixin.qq.com/doc/v3/partner/4012759741.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4012085877.md)
-### 附录
-- [管理商户号绑定的APPID账号](https://pay.weixin.qq.com/doc/v3/partner/4013352075.md)
-## 小程序支付
-> 小程序支付提供了让用户在微信小程序内进行支付的能力，小程序内调起支付无需跳转页面，支付体验流畅，适用于小程序电商、餐饮、本地生活等场景，提升转化与复购。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012085810.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012076731.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012076732.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4013352071.md)
-### API列表
-- [JSAPI/小程序下单](https://pay.weixin.qq.com/doc/v3/partner/4012759974.md)
-- [小程序调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012085827.md)
-- [支付成功回调通知](https://pay.weixin.qq.com/doc/v3/partner/4012085801.md)
-- [关闭订单](https://pay.weixin.qq.com/doc/v3/partner/4012760108.md)
-- [微信支付订单号查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012738973.md)
-- [商户订单号查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012760115.md)
-- [申请退款](https://pay.weixin.qq.com/doc/v3/partner/4012760121.md)
-- [查询单笔退款（通过商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4012760128.md)
-- [发起异常退款](https://pay.weixin.qq.com/doc/v3/partner/4013352278.md)
-- [退款结果回调通知](https://pay.weixin.qq.com/doc/v3/partner/4012085802.md)
-- [申请所有/单个子商户交易账单](https://pay.weixin.qq.com/doc/v3/partner/4012760132.md)
-- [申请服务商资金账单](https://pay.weixin.qq.com/doc/v3/partner/4012760136.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4012085803.md)
-### 附录
-- [管理商户号绑定的APPID账号](https://pay.weixin.qq.com/doc/v3/partner/4013352070.md)
-## JSAPI合单支付
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012079332.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012166834.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4013461849.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4013462212.md)
-### API列表
-- [JSAPI合单下单](https://pay.weixin.qq.com/doc/v3/partner/4012757938.md)
-- [JSAPI调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012166844.md)
-- [查询合单订单](https://pay.weixin.qq.com/doc/v3/partner/4013462164.md)
-- [关闭合单订单](https://pay.weixin.qq.com/doc/v3/partner/4013462171.md)
-- [合单订单支付成功回调通知](https://pay.weixin.qq.com/doc/v3/partner/4013462175.md)
-- [申请退款](https://pay.weixin.qq.com/doc/v3/partner/4013462183.md)
-- [查询单笔退款（按商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4013462188.md)
-- [发起异常退款](https://pay.weixin.qq.com/doc/v3/partner/4013462191.md)
-- [退款结果通知](https://pay.weixin.qq.com/doc/v3/partner/4013462195.md)
-- [申请所有/单个子商户交易账单](https://pay.weixin.qq.com/doc/v3/partner/4013462197.md)
-- [申请服务商资金账单](https://pay.weixin.qq.com/doc/v3/partner/4013462202.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4013462207.md)
-### 附录
-- [合单支付-商户号绑定APPID操作说明](https://pay.weixin.qq.com/doc/v3/partner/4013462628.md)
-## APP合单支付
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012079331.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012166832.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4013461863.md)
-### API列表
-- [APP合单下单](https://pay.weixin.qq.com/doc/v3/partner/4012758021.md)
-- [APP调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012166845.md)
-- [查询合单订单](https://pay.weixin.qq.com/doc/v3/partner/4012761057.md)
-- [关闭合单订单](https://pay.weixin.qq.com/doc/v3/partner/4012761079.md)
-- [合单订单支付成功回调通知](https://pay.weixin.qq.com/doc/v3/partner/4012231898.md)
-- [申请退款](https://pay.weixin.qq.com/doc/v3/partner/4012760207.md)
-- [查询单笔退款（通过商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4012760226.md)
-- [发起异常退款](https://pay.weixin.qq.com/doc/v3/partner/4013461907.md)
-- [退款结果回调通知](https://pay.weixin.qq.com/doc/v3/partner/4012231901.md)
-- [申请所有/单个子商户交易账单](https://pay.weixin.qq.com/doc/v3/partner/4012760228.md)
-- [申请服务商资金账单](https://pay.weixin.qq.com/doc/v3/partner/4012760229.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4012231933.md)
-## H5合单支付
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4013462080.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012166833.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4013462145.md)
-### API列表
-- [H5合单下单](https://pay.weixin.qq.com/doc/v3/partner/4012758208.md)
-- [H5调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012166846.md)
-- [查询合单订单](https://pay.weixin.qq.com/doc/v3/partner/4013462099.md)
-- [关闭合单订单](https://pay.weixin.qq.com/doc/v3/partner/4013462102.md)
-- [合单订单支付成功回调通知](https://pay.weixin.qq.com/doc/v3/partner/4013462105.md)
-- [申请退款](https://pay.weixin.qq.com/doc/v3/partner/4013462113.md)
-- [查询单笔退款（按商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4013462116.md)
-- [发起异常退款](https://pay.weixin.qq.com/doc/v3/partner/4013462123.md)
-- [退款结果通知](https://pay.weixin.qq.com/doc/v3/partner/4013462126.md)
-- [申请所有/单个子商户交易账单](https://pay.weixin.qq.com/doc/v3/partner/4013462129.md)
-- [申请服务商资金账单](https://pay.weixin.qq.com/doc/v3/partner/4013462134.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4013462137.md)
-## Native合单支付
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012079333.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012166835.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4013462413.md)
-### API列表
-- [Native合单下单](https://pay.weixin.qq.com/doc/v3/partner/4012758240.md)
-- [Native调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012166843.md)
-- [查询合单订单](https://pay.weixin.qq.com/doc/v3/partner/4013462240.md)
-- [关闭合单订单](https://pay.weixin.qq.com/doc/v3/partner/4013462247.md)
-- [合单订单支付成功回调通知](https://pay.weixin.qq.com/doc/v3/partner/4013462250.md)
-- [申请退款](https://pay.weixin.qq.com/doc/v3/partner/4013462256.md)
-- [查询单笔退款（按商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4013462260.md)
-- [发起异常退款](https://pay.weixin.qq.com/doc/v3/partner/4013462286.md)
-- [退款结果回调通知](https://pay.weixin.qq.com/doc/v3/partner/4013462327.md)
-- [申请所有/单个子商户交易账单](https://pay.weixin.qq.com/doc/v3/partner/4013462343.md)
-- [申请服务商资金账单](https://pay.weixin.qq.com/doc/v3/partner/4013462358.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4013462389.md)
-## 小程序合单支付
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012079334.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012166836.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4013462619.md)
-### API列表
-- [小程序合单下单](https://pay.weixin.qq.com/doc/v3/partner/4012758246.md)
-- [小程序调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012166847.md)
-- [查询合单订单](https://pay.weixin.qq.com/doc/v3/partner/4013462520.md)
-- [关闭合单订单](https://pay.weixin.qq.com/doc/v3/partner/4013462566.md)
-- [合单订单支付成功回调通知](https://pay.weixin.qq.com/doc/v3/partner/4013462574.md)
-- [申请退款](https://pay.weixin.qq.com/doc/v3/partner/4013462579.md)
-- [查询单笔退款（按商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4013462581.md)
-- [发起异常退款](https://pay.weixin.qq.com/doc/v3/partner/4013462582.md)
-- [退款结果回调通知](https://pay.weixin.qq.com/doc/v3/partner/4013462586.md)
-- [申请所有/单个子商户交易账单](https://pay.weixin.qq.com/doc/v3/partner/4013462604.md)
-- [申请服务商资金账单](https://pay.weixin.qq.com/doc/v3/partner/4013462607.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4013462614.md)
-## 医保支付（服务商模式）
-> 医保支付支持用户在微信激活医保电子凭证后，直接完成挂号、门诊缴费等费用的线上医保支付，无需前往线下窗口排队，有助于提高医疗医保服务效率，改善医患关系，为用户提供更便捷流畅的就医体验。
-
-- [产品介绍 ](https://pay.weixin.qq.com/doc/v3/partner/4016824698.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4016824704.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4017149893.md)
-### API列表
-#### 医保自费混合订单
-- [医保自费混合收款下单](https://pay.weixin.qq.com/doc/v3/partner/4012503131.md)
-- [使用医保自费混合订单号查看下单结果](https://pay.weixin.qq.com/doc/v3/partner/4012503155.md)
-- [使用服务商订单号查看下单结果](https://pay.weixin.qq.com/doc/v3/partner/4012503286.md)
-- [小程序调起医保自费混合支付](https://pay.weixin.qq.com/doc/v3/partner/4012166993.md)
-- [JSAPI调起医保自费混合支付](https://pay.weixin.qq.com/doc/v3/partner/4012809233.md)
-- [医保混合收款成功通知](https://pay.weixin.qq.com/doc/v3/partner/4012165722.md)
-#### 医保退款
-- [医保退款通知](https://pay.weixin.qq.com/doc/v3/partner/4012166534.md)
-### 常见问题
-- [报错排查指引](https://pay.weixin.qq.com/doc/v3/partner/4020401184.md)
-- [业务&接口规则类问题](https://pay.weixin.qq.com/doc/v3/partner/4017415847.md)
-### 附录
-- [申请医保支付权限](https://pay.weixin.qq.com/doc/v3/partner/4016971494.md)
-- [接入医保亲情付指引](https://pay.weixin.qq.com/doc/v3/partner/4016970670.md)
-## 医保支付（间连模式）
-> 医保支付支持用户在微信激活医保电子凭证后，直接完成挂号、门诊缴费等费用的线上医保支付，无需前往线下窗口排队，有助于提高医疗医保服务效率，改善医患关系，为用户提供更便捷流畅的就医体验。
-
-- [产品介绍 ](https://pay.weixin.qq.com/doc/v3/partner/4018300086.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4018300089.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4016824703.md)
-### API列表
-#### 医保自费混合订单
-- [医保自费混合收款下单](https://pay.weixin.qq.com/doc/v3/partner/4018300080.md)
-- [使用医保自费混合订单号查看下单结果](https://pay.weixin.qq.com/doc/v3/partner/4018300081.md)
-- [使用从业机构订单号查看下单结果](https://pay.weixin.qq.com/doc/v3/partner/4018300082.md)
-- [小程序调起医保自费混合支付](https://pay.weixin.qq.com/doc/v3/partner/4018300079.md)
-- [JSAPI调起医保自费混合支付](https://pay.weixin.qq.com/doc/v3/partner/4018300083.md)
-- [医保混合收款成功通知](https://pay.weixin.qq.com/doc/v3/partner/4018303231.md)
-#### 医保退款
-- [医保退款通知](https://pay.weixin.qq.com/doc/v3/partner/4018300085.md)
-### 常见问题
-- [报错排查指引](https://pay.weixin.qq.com/doc/v3/partner/4020401288.md)
-- [业务&接口规则类问题](https://pay.weixin.qq.com/doc/v3/partner/4018300095.md)
-### 附录
-- [申请医保支付权限](https://pay.weixin.qq.com/doc/v3/partner/4016824701.md)
-- [接入医保亲情付指引](https://pay.weixin.qq.com/doc/v3/partner/4018300091.md)
-## 订单退款
-> 订单退款为商户提供交易逆向服务，支持全额与部分退款，可按订单发起退款申请，资金原路退回用户账户，支持状态查询与流程追溯，保障售后资金安全，提升消费体验与商户合规能力。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4013080622.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4013080630.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4013080623.md)
-- [业务示例代码](https://pay.weixin.qq.com/doc/v3/partner/4015217325.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4013080629.md)
-### API列表
-- [申请退款](https://pay.weixin.qq.com/doc/v3/partner/4013080625.md)
-- [查询单笔退款（通过商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4013080626.md)
-- [发起异常退款](https://pay.weixin.qq.com/doc/v3/partner/4013080627.md)
-- [退款结果通知](https://pay.weixin.qq.com/doc/v3/partner/4013080628.md)
-### 附录
-- [退款操作指引](https://pay.weixin.qq.com/doc/v3/partner/4013080632.md)
-- [微信支付退款最佳实践](https://pay.weixin.qq.com/doc/v3/partner/4014960215.md)
-## 下载账单
-> 下载账单提供交易、资金、退款、分账等多维度对账文件，支持按时间筛选获取明细，用于财务核对、结算审计与数据归档，帮助商户清晰管理资金流水，提升账务处理效率与透明度。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4013080592.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4013080593.md)
-- [业务示例代码](https://pay.weixin.qq.com/doc/v3/partner/4015988147.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4013080602.md)
-### API列表
-- [申请所有/单个特约商户交易账单](https://pay.weixin.qq.com/doc/v3/partner/4013080595.md)
-- [申请服务商资金账单](https://pay.weixin.qq.com/doc/v3/partner/4013080596.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4013080597.md)
-### 附录
-- [交易账单详细说明](https://pay.weixin.qq.com/doc/v3/partner/4013080599.md)
-- [资金账单详细说明](https://pay.weixin.qq.com/doc/v3/partner/4013080600.md)
-- [平台下载账单操作指引](https://pay.weixin.qq.com/doc/v3/partner/4013080601.md)
-## 分账
-> 分账是商户用于交易资金分配的工具，支持将资金分给合作伙伴、员工、用户等分润方。资金先冻结，可实时或延时分账，单笔最多分 50 次、每次可分 50 方，支持商户或个人账户接收，需设置最大分账比例，全程免手续费。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012072582.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012072589.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012072601.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4014547107.md)
-### API列表
-- [请求分账](https://pay.weixin.qq.com/doc/v3/partner/4012690683.md)
-- [查询分账结果](https://pay.weixin.qq.com/doc/v3/partner/4012466850.md)
-- [请求分账回退](https://pay.weixin.qq.com/doc/v3/partner/4012466854.md)
-- [查询分账回退结果](https://pay.weixin.qq.com/doc/v3/partner/4012466858.md)
-- [解冻剩余资金](https://pay.weixin.qq.com/doc/v3/partner/4012466860.md)
-- [查询剩余待分金额](https://pay.weixin.qq.com/doc/v3/partner/4012457927.md)
-- [查询最大分账比例](https://pay.weixin.qq.com/doc/v3/partner/4012466864.md)
-- [添加分账接收方](https://pay.weixin.qq.com/doc/v3/partner/4012690944.md)
-- [删除分账接收方](https://pay.weixin.qq.com/doc/v3/partner/4012466868.md)
-- [分账动账通知](https://pay.weixin.qq.com/doc/v3/partner/4012075216.md)
-- [申请分账账单](https://pay.weixin.qq.com/doc/v3/partner/4012761140.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4012075366.md)
-### 附录
-- [分账失败处理指引](https://pay.weixin.qq.com/doc/v3/partner/4015504885.md)
-## 微信支付分
-> 微信支付分是基于用户身份、支付行为等综合评估的信用分值，支持免押租借、先享后付等场景。支持先免、先享两种模式，帮助商户降低门槛、提升转化，订单资金可通过分账完成分配。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012586132.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012586133.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012586134.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4012586139.md)
-### API列表
-- [创建支付分订单](https://pay.weixin.qq.com/doc/v3/partner/4013138534.md)
-- [查询支付分订单](https://pay.weixin.qq.com/doc/v3/partner/4013138559.md)
-- [取消支付分订单](https://pay.weixin.qq.com/doc/v3/partner/4013138589.md)
-- [确认订单回调通知](https://pay.weixin.qq.com/doc/v3/partner/4012586137.md)
-- [完结支付分订单](https://pay.weixin.qq.com/doc/v3/partner/4013138598.md)
-- [修改支付分订单金额](https://pay.weixin.qq.com/doc/v3/partner/4013138819.md)
-- [同步支付分订单状态](https://pay.weixin.qq.com/doc/v3/partner/4013138975.md)
-- [支付成功回调通知](https://pay.weixin.qq.com/doc/v3/partner/4012586136.md)
-- [申请退款](https://pay.weixin.qq.com/doc/v3/partner/4013138987.md)
-- [查询退款](https://pay.weixin.qq.com/doc/v3/partner/4013139077.md)
-- [退款结果通知](https://pay.weixin.qq.com/doc/v3/partner/4012586138.md)
-#### 拉起支付分小程序确认订单页
-- [JSAPI调起支付分确认订单页](https://pay.weixin.qq.com/doc/v3/partner/4012607505.md)
-##### APP调起支付分确认订单页
-- [Android](https://pay.weixin.qq.com/doc/v3/partner/4012607507.md)
-- [iOS](https://pay.weixin.qq.com/doc/v3/partner/4012607508.md)
-- [鸿蒙](https://pay.weixin.qq.com/doc/v3/partner/4015271745.md)
-##### 小程序调起支付分确认订单页
-- [wx.openBusinessView](https://pay.weixin.qq.com/doc/v3/partner/4012607510.md)
-- [wx.navigateToMiniProgram（停止新增）](https://pay.weixin.qq.com/doc/v3/partner/4012607511.md)
-#### 拉起支付分小程序订单详情页
-- [JSAPI调起支付分订单详情页](https://pay.weixin.qq.com/doc/v3/partner/4012607518.md)
-##### APP调起支付分订单详情页
-- [Android](https://pay.weixin.qq.com/doc/v3/partner/4012607513.md)
-- [iOS](https://pay.weixin.qq.com/doc/v3/partner/4012607514.md)
-- [鸿蒙](https://pay.weixin.qq.com/doc/v3/partner/4015271776.md)
-##### 小程序调起支付分订单详情页
-- [wx.openBusinessView](https://pay.weixin.qq.com/doc/v3/partner/4012607516.md)
-- [wx.navigateToMiniProgram（停止新增）](https://pay.weixin.qq.com/doc/v3/partner/4012607517.md)
-### 附录
-- [支付分合作品牌线上应用规范](https://pay.weixin.qq.com/doc/v3/partner/4012586152.md)
-- [支付分权限申请邮件模板](https://pay.weixin.qq.com/doc/v3/partner/4012586142.md)
-- [测试微信号配置指引](https://pay.weixin.qq.com/doc/v3/partner/4012586141.md)
-- [服务ID新增绑定邮件流程](https://pay.weixin.qq.com/doc/v3/partner/4012624851.md)
-#### post_payments(后付费项目)字段传参说明
-- [总览](https://pay.weixin.qq.com/doc/v3/partner/4013163663.md)
-- [二轮电动车充电桩](https://pay.weixin.qq.com/doc/v3/partner/4012586150.md)
-- [充电宝](https://pay.weixin.qq.com/doc/v3/partner/4012586148.md)
-- [共享单车](https://pay.weixin.qq.com/doc/v3/partner/4012586145.md)
-- [快递行业](https://pay.weixin.qq.com/doc/v3/partner/4012586144.md)
-- [智慧零售(无人设备)](https://pay.weixin.qq.com/doc/v3/partner/4012586146.md)
-- [汽车充电桩](https://pay.weixin.qq.com/doc/v3/partner/4012586149.md)
-- [汽车租赁](https://pay.weixin.qq.com/doc/v3/partner/4012586151.md)
-- [酒店行业](https://pay.weixin.qq.com/doc/v3/partner/4012586147.md)
-## 微信支付分停车服务
-> 微信支付分停车服务基于用户微信账户和车牌的绑定关系，依托微信支付分，在车辆离场时对绑定账户自动扣费。用户一次开通，全国支付分停车场均可使用。提升车场通行效率与用户体验，减少离场拥堵。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012085549.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012085632.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012085711.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016183529.md)
-### API列表
-#### 停车入场
-- [创建停车入场](https://pay.weixin.qq.com/doc/v3/partner/4012533994.md)
-- [停车入场状态变更通知](https://pay.weixin.qq.com/doc/v3/partner/4012085798.md)
-#### 服务
-- [查询车牌服务开通信息](https://pay.weixin.qq.com/doc/v3/partner/4012534183.md)
-- [小程序调起微信支付分停车服务开通页](https://pay.weixin.qq.com/doc/v3/partner/4012085969.md)
-- [H5调起微信支付分停车服务开通页](https://pay.weixin.qq.com/doc/v3/partner/4012085997.md)
-- [App拉起微信支付分停车服务开通页](https://pay.weixin.qq.com/doc/v3/partner/4012086028.md)
-#### 扣费受理
-- [查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012534441.md)
-- [扣费受理](https://pay.weixin.qq.com/doc/v3/partner/4012534427.md)
-- [订单支付结果通知](https://pay.weixin.qq.com/doc/v3/partner/4012086059.md)
-#### 还款
-- [微信垫资还款](https://pay.weixin.qq.com/doc/v3/partner/4012086207.md)
-#### 退款
-- [退款申请](https://pay.weixin.qq.com/doc/v3/partner/4012760545.md)
-- [退款结果通知](https://pay.weixin.qq.com/doc/v3/partner/4012086319.md)
-- [查询单笔退款（通过商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4012760554.md)
-## 现金红包（V2）
-> 现金红包是微信支付提供的营销工具，商户可以通过公众号或者服务通知向用户发放现金红包。用户领取红包后，资金到达用户微信支付零钱账户；若用户未领取， 资金将会在24小时后退回商户的微信支付账户中。适用于拉新、促活、福利发放等场景。
-
-- [现金红包（V2）](https://pay.weixin.qq.com/doc/v3/partner/4012851209.md)
-## 代金券
-> 微信支付官方营销工具，支持商户配置满减、折扣等券型，可在支付前发放、支付中自动核销。支持线上线下多场景投放，数据实时可查，助力商户拉新、复购与客流提升，适配多行业营销需求。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012087800.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012087801.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012087802.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4015880931.md)
-### API列表
-- [核销事件回调通知](https://pay.weixin.qq.com/doc/v3/partner/4012285807.md)
-- [图片上传（营销专用）](https://pay.weixin.qq.com/doc/v3/partner/4012759802.md)
-#### 批次
-- [创建代金券批次](https://pay.weixin.qq.com/doc/v3/partner/4012534537.md)
-- [激活代金券批次](https://pay.weixin.qq.com/doc/v3/partner/4012460237.md)
-- [暂停代金券批次](https://pay.weixin.qq.com/doc/v3/partner/4012460340.md)
-- [重启代金券批次](https://pay.weixin.qq.com/doc/v3/partner/4012460448.md)
-- [条件查询批次列表](https://pay.weixin.qq.com/doc/v3/partner/4012460518.md)
-- [查询批次详情](https://pay.weixin.qq.com/doc/v3/partner/4012460606.md)
-- [查询代金券可用商户](https://pay.weixin.qq.com/doc/v3/partner/4012463409.md)
-- [查询代金券可用单品](https://pay.weixin.qq.com/doc/v3/partner/4012463475.md)
-- [下载批次退款明细](https://pay.weixin.qq.com/doc/v3/partner/4012463548.md)
-- [下载批次核销明细](https://pay.weixin.qq.com/doc/v3/partner/4012463698.md)
-#### 券
-- [根据商户号查用户的券](https://pay.weixin.qq.com/doc/v3/partner/4012494237.md)
-- [发放指定批次的代金券](https://pay.weixin.qq.com/doc/v3/partner/4012463807.md)
-- [查询代金券详情](https://pay.weixin.qq.com/doc/v3/partner/4012492796.md)
-#### 消息通知地址
-- [查询代金券消息通知地址](https://pay.weixin.qq.com/doc/v3/partner/4012464155.md)
-- [设置代金券消息通知地址](https://pay.weixin.qq.com/doc/v3/partner/4012464176.md)
-## 委托营销
-> 委托营销是微信支付面向小程序直播等场景推出的授权营销工具，商户在商户平台创建券批次后，可通过接口授权给指定小程序 AppID，用于直播插件内发券，实现券创建与投放权限分离管理。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012071996.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012071997.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012071998.md)
-### API列表
-- [建立合作关系](https://pay.weixin.qq.com/doc/v3/partner/4012381469.md)
-- [查询合作关系列表](https://pay.weixin.qq.com/doc/v3/partner/4012381479.md)
-## 支付有礼
-> 支付有礼是支付后营销工具，用户完成支付即可自动发放优惠券、礼品等权益，帮助商户引导复购、提升客单。支持多种优惠形式与精准投放，打通支付与营销闭环，降低运营成本，提升用户粘性与交易转化。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012072117.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012072118.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012072119.md)
-### API列表
-- [图片上传（营销专用）](https://pay.weixin.qq.com/doc/v3/partner/4012760270.md)
-#### 支付有礼活动
-- [创建全场满额送活动](https://pay.weixin.qq.com/doc/v3/partner/4012492900.md)
-- [获取活动详情接口](https://pay.weixin.qq.com/doc/v3/partner/4012492967.md)
-- [获取活动发券商户号](https://pay.weixin.qq.com/doc/v3/partner/4012466191.md)
-- [获取活动指定商品列表](https://pay.weixin.qq.com/doc/v3/partner/4012466492.md)
-- [终止活动](https://pay.weixin.qq.com/doc/v3/partner/4012466633.md)
-- [新增活动发券商户号](https://pay.weixin.qq.com/doc/v3/partner/4012466735.md)
-- [获取支付有礼活动列表](https://pay.weixin.qq.com/doc/v3/partner/4012493214.md)
-- [删除活动发券商户号](https://pay.weixin.qq.com/doc/v3/partner/4012466827.md)
-## 小程序发券插件
-> 小程序发券插件为微信支付为商户小程序提供官方发券插件，用户通过插件领取的券将自动加入微信卡包，提升用户领券感知及核销率。适配电商、零售、餐饮等场景，简化用户领券路径，提升活动效果与运营效率。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012072233.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012072234.md)
-### API列表
-- [小程序发券插件](https://pay.weixin.qq.com/doc/v3/partner/4012285878.md)
-## H5发券
-> H5发券提供网页端发券能力，商户可在H5页面快速配置并投放优惠券，接入便捷、适配性强。适用于活动推广、拉新促活等场景，缩短领券链路，提升券领取率与活动覆盖面。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012075048.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012075086.md)
-### API列表
-- [H5发券](https://pay.weixin.qq.com/doc/v3/partner/4012285900.md)
-## 智慧商圈
-> 面向商业综合体、商圈的数字化经营工具，整合支付、营销、会员、积分、权益等能力，实现场内商户联动运营。用户在商圈门店消费后可享自动积分及出行服务、门店服务等积分权益。增加用户会员价值感，拉动商圈会员活跃与消费。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012075220.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012075231.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012075386.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016111726.md)
-### API列表
-- [商圈会员积分服务授权结果通知](https://pay.weixin.qq.com/doc/v3/partner/4012076406.md)
-- [商圈会员场内支付结果通知](https://pay.weixin.qq.com/doc/v3/partner/4012076414.md)
-- [商圈会员积分同步](https://pay.weixin.qq.com/doc/v3/partner/4012474133.md)
-- [商圈会员场内退款结果通知](https://pay.weixin.qq.com/doc/v3/partner/4012076419.md)
-- [商圈会员积分服务授权查询](https://pay.weixin.qq.com/doc/v3/partner/4012474135.md)
-- [商圈会员待积分状态查询](https://pay.weixin.qq.com/doc/v3/partner/4012474129.md)
-- [商圈会员停车状态同步](https://pay.weixin.qq.com/doc/v3/partner/4012474127.md)
-## 支付即服务
-> 用户完成微信支付后，自动展示服务入口，快速连接售后、客服等场景。缩短服务路径，提升用户体验与服务效率，降低商户客服成本，适用于零售、餐饮、生活服务等多行业售后链路。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012076036.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012076037.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012076038.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016913657.md)
-### API列表
-- [服务人员查询](https://pay.weixin.qq.com/doc/v3/partner/4012688558.md)
-- [服务人员注册](https://pay.weixin.qq.com/doc/v3/partner/4012688564.md)
-- [服务人员更新](https://pay.weixin.qq.com/doc/v3/partner/4012688570.md)
-- [服务人员分配](https://pay.weixin.qq.com/doc/v3/partner/4012474145.md)
-### 附录
-- [服务人员称谓申请指引](https://pay.weixin.qq.com/doc/v3/partner/4012076039.md)
-- [免开发版本操作指引](https://pay.weixin.qq.com/doc/v3/partner/4012076040.md)
-- [个人微信服务人员注册](https://pay.weixin.qq.com/doc/v3/partner/4012076041.md)
-## 点金计划
-> 帮助商户在支付完成页自动展示官方广告，获取广告分成收入。广告页面无需商户侧额外开发，接入即可变现，支持合规展示与数据透明，在不影响用户体验的前提下，为商户增加额外收益，提升经营附加值。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012072130.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012072158.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012072262.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016241762.md)
-### API列表
-- [点金计划管理](https://pay.weixin.qq.com/doc/v3/partner/4012473796.md)
-- [商家小票管理](https://pay.weixin.qq.com/doc/v3/partner/4012473788.md)
-- [同业过滤标签管理](https://pay.weixin.qq.com/doc/v3/partner/4012473784.md)
-- [开通广告展示](https://pay.weixin.qq.com/doc/v3/partner/4012473794.md)
-- [关闭广告展示](https://pay.weixin.qq.com/doc/v3/partner/4012473781.md)
-- [小程序左上角返回键管理](https://pay.weixin.qq.com/doc/v3/partner/4012072514.md)
-## 品牌入驻
-> 品牌入驻是商户开通微信支付品牌经营能力的前提，商户提交资质经审核通过后，即可获得品牌账号，开展品牌门店、营销活动及商家名片会员管理等相关工作。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4016433410.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4016985537.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4017027854.md)
-### API列表
-- [提交入驻申请](https://pay.weixin.qq.com/doc/v3/partner/4016249989.md)
-- [根据业务申请编号查询申请状态](https://pay.weixin.qq.com/doc/v3/partner/4016257694.md)
-- [根据申请单ID查询申请状态](https://pay.weixin.qq.com/doc/v3/partner/4016257685.md)
-- [撤销申请](https://pay.weixin.qq.com/doc/v3/partner/4016257700.md)
-- [图片上传](https://pay.weixin.qq.com/doc/v3/partner/4016276333.md)
-### 附录
-- [品牌能力介绍](https://pay.weixin.qq.com/doc/v3/partner/4016433389.md)
-- [服务商申请品牌授权流程](https://pay.weixin.qq.com/doc/v3/partner/4016026183.md)
-## 商家名片
-> 商家名片是商户在微信支付的官方展示与服务页面，用户支付后可通过支付凭证进入，商家名片可展示交易详情、优惠活动、商家服务、会员信息及客服渠道等，方便用户标记喜爱商家，是商户与用户建立长效连接、实现持续触达的核心入口。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4016433952.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4017027862.md)
-### 开发指引
-- [商家名片开发指引](https://pay.weixin.qq.com/doc/v3/partner/4016914463.md)
-- [交易连接名片开发指引](https://pay.weixin.qq.com/doc/v3/partner/4016985845.md)
-### API列表
-#### 商家名片配置
-- [提交商家名片配置申请](https://pay.weixin.qq.com/doc/v3/partner/4016468440.md)
-- [发布商家名片配置](https://pay.weixin.qq.com/doc/v3/partner/4016475176.md)
-- [撤销商家名片配置申请](https://pay.weixin.qq.com/doc/v3/partner/4016475172.md)
-- [查询商家名片配置申请状态](https://pay.weixin.qq.com/doc/v3/partner/4016475174.md)
-- [获取商家名片预览二维码](https://pay.weixin.qq.com/doc/v3/partner/4016641998.md)
-#### 交易连接名片
-- [添加交易连接名片规则申请](https://pay.weixin.qq.com/doc/v3/partner/4016333302.md)
-- [解除已生效交易连接名片场景](https://pay.weixin.qq.com/doc/v3/partner/4016366804.md)
-- [撤销交易连接名片配置申请](https://pay.weixin.qq.com/doc/v3/partner/4016366797.md)
-- [查询已生效交易连接名片规则](https://pay.weixin.qq.com/doc/v3/partner/4016366785.md)
-- [根据业务申请编号查询添加申请状态](https://pay.weixin.qq.com/doc/v3/partner/4016366816.md)
-### 附录
-- [商家名片&交易连接名片配置指引](https://pay.weixin.qq.com/doc/v3/partner/4016433970.md)
-## 商家名片会员
-> 商家名片会员是基于商家名片的会员运营工具，需开通名片后使用，可结合支付流程引导用户入会，跳转商家小程序会员相关页面，发放会员券的能力，结合微信生态能力向品牌商家提供更丰富的会员解决方案，帮助商家提升会员运营效率。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4015274636.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4015274639.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4017418554.md)
-### API列表
-- [图片上传](https://pay.weixin.qq.com/doc/v3/partner/4015900513.md)
-#### 会员卡模板管理
-- [创建会员卡模板](https://pay.weixin.qq.com/doc/v3/partner/4015336970.md)
-- [查询会员卡模板列表](https://pay.weixin.qq.com/doc/v3/partner/4015336976.md)
-- [查询会员卡模板信息](https://pay.weixin.qq.com/doc/v3/partner/4015336974.md)
-- [修改会员卡模板信息](https://pay.weixin.qq.com/doc/v3/partner/4015336977.md)
-- [作废会员卡模板](https://pay.weixin.qq.com/doc/v3/partner/4015336972.md)
-#### 用户会员卡管理
-- [查询用户会员卡信息](https://pay.weixin.qq.com/doc/v3/partner/4015336980.md)
-- [查询用户在品牌下所有会员卡](https://pay.weixin.qq.com/doc/v3/partner/4015336984.md)
-- [修改用户会员卡信息](https://pay.weixin.qq.com/doc/v3/partner/4015336985.md)
-- [作废用户会员卡](https://pay.weixin.qq.com/doc/v3/partner/4015336983.md)
-#### 用户开通会员卡
-- [品牌会员入会组件预授权](https://pay.weixin.qq.com/doc/v3/partner/4015336986.md)
-- [小程序拉起品牌会员入会组件](https://pay.weixin.qq.com/doc/v3/partner/4015273633.md)
-- [H5拉起品牌会员入会组件](https://pay.weixin.qq.com/doc/v3/partner/4015331476.md)
-#### 商家同步会员身份
-- [根据OPENID导入用户会员卡](https://pay.weixin.qq.com/doc/v3/partner/4015336981.md)
-- [同步会员开通结果](https://pay.weixin.qq.com/doc/v3/partner/4015336979.md)
-#### 事件通知
-- [会员卡事件通知](https://pay.weixin.qq.com/doc/v3/partner/4015283692.md)
-- [用户积分兑券事件通知](https://pay.weixin.qq.com/doc/v3/partner/4015878622.md)
-- [用户积分同步事件通知](https://pay.weixin.qq.com/doc/v3/partner/4016096820.md)
-#### 用户动态
-- [创建用户动态信息](https://pay.weixin.qq.com/doc/v3/partner/4015336987.md)
-- [下单同步用户实时动态](https://pay.weixin.qq.com/doc/v3/partner/4015534755.md)
-#### 会员卡积分兑券
-- [同步积分余额](https://pay.weixin.qq.com/doc/v3/partner/4015897280.md)
-- [同步积分兑券结果](https://pay.weixin.qq.com/doc/v3/partner/4015897268.md)
-#### 品牌会员发券活动
-- [创建品牌会员发券活动](https://pay.weixin.qq.com/doc/v3/partner/4016464918.md)
-- [查询品牌会员发券活动](https://pay.weixin.qq.com/doc/v3/partner/4016588015.md)
-- [查询品牌会员发券活动列表](https://pay.weixin.qq.com/doc/v3/partner/4016588039.md)
-- [修改品牌会员发券活动信息](https://pay.weixin.qq.com/doc/v3/partner/4016588044.md)
-- [终止品牌会员发券活动](https://pay.weixin.qq.com/doc/v3/partner/4016588028.md)
-## 摇一摇有优惠
-> 摇一摇有优惠是微信支付的支付后互动营销功能，依据用户消费偏好在支付完成页快速发放优惠，简化领券与核销链路，帮助商户提升复购、实现精细化运营，使用前需完成商家名片配置或品牌门店创建。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4015782374.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4016060552.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4016110225.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4017418618.md)
-### API列表
-#### 投放计划
-- [创建投放计划](https://pay.weixin.qq.com/doc/v3/partner/4016184554.md)
-- [分页查询投放计划列表](https://pay.weixin.qq.com/doc/v3/partner/4016184563.md)
-- [更新投放计划](https://pay.weixin.qq.com/doc/v3/partner/4016184594.md)
-- [终止投放计划](https://pay.weixin.qq.com/doc/v3/partner/4016184572.md)
-- [设置投放计划回调地址](https://pay.weixin.qq.com/doc/v3/partner/4016184598.md)
-- [投放计划状态变更通知](https://pay.weixin.qq.com/doc/v3/partner/4016168699.md)
-### 附录
-- [投放计划功能介绍](https://pay.weixin.qq.com/doc/v3/partner/4016402231.md)
-- [投放计划配置指引](https://pay.weixin.qq.com/doc/v3/partner/4016111064.md)
-- [品牌信息用户端展示规则](https://pay.weixin.qq.com/doc/v3/partner/4016110939.md)
-- [权限申请](https://pay.weixin.qq.com/doc/v3/partner/4015788437.md)
-- [运营规则](https://pay.weixin.qq.com/doc/v3/partner/4017294537.md)
-## 商品券（单券）
-> 商品券（单券）为单次使用的优惠券，每次发放只会发放一张券，支持满减、折扣、兑换等类型，可设置全场或单品可用，适合短期促销、新人礼、单品特惠等场景。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4015989376.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4015788446.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016950421.md)
-### API列表
-- [图片上传](https://pay.weixin.qq.com/doc/v3/partner/4015781275.md)
-#### 商品券管理
-- [创建商品券](https://pay.weixin.qq.com/doc/v3/partner/4015781289.md)
-- [修改商品券](https://pay.weixin.qq.com/doc/v3/partner/4015781296.md)
-- [查询商品券](https://pay.weixin.qq.com/doc/v3/partner/4015781292.md)
-- [失效商品券](https://pay.weixin.qq.com/doc/v3/partner/4015781290.md)
-#### 商品券批次管理
-- [添加商品券批次](https://pay.weixin.qq.com/doc/v3/partner/4015781304.md)
-- [查询商品券批次列表](https://pay.weixin.qq.com/doc/v3/partner/4015781553.md)
-- [查询商品券指定批次](https://pay.weixin.qq.com/doc/v3/partner/4015781542.md)
-- [修改商品券批次](https://pay.weixin.qq.com/doc/v3/partner/4015781556.md)
-- [修改商品券批次发放预算](https://pay.weixin.qq.com/doc/v3/partner/4015781561.md)
-- [失效商品券批次](https://pay.weixin.qq.com/doc/v3/partner/4015781532.md)
-- [批次关联门店](https://pay.weixin.qq.com/doc/v3/partner/4015781302.md)
-- [查询批次关联门店列表](https://pay.weixin.qq.com/doc/v3/partner/4015781546.md)
-- [批次取消关联门店](https://pay.weixin.qq.com/doc/v3/partner/4015781537.md)
-- [预上传券Code](https://pay.weixin.qq.com/doc/v3/partner/4015781572.md)
-#### 商品券发放
-- [向用户发放商品券](https://pay.weixin.qq.com/doc/v3/partner/4015781605.md)
-- [确认发放用户商品券](https://pay.weixin.qq.com/doc/v3/partner/4015781575.md)
-##### 小程序发券组件
-- [向用户预发放商品券](https://pay.weixin.qq.com/doc/v3/partner/4016434365.md)
-- [调起小程序发券组件](https://pay.weixin.qq.com/doc/v3/partner/4016434346.md)
-#### 商品券核销
-- [核销用户商品券](https://pay.weixin.qq.com/doc/v3/partner/4015781608.md)
-- [调起小程序核销组件](https://pay.weixin.qq.com/doc/v3/partner/4016110739.md)
-#### 商品券查询
-- [查询用户商品券详情](https://pay.weixin.qq.com/doc/v3/partner/4015781582.md)
-- [指定券状态查询用户商品券列表](https://pay.weixin.qq.com/doc/v3/partner/4015781590.md)
-#### 商品券失效与退券
-- [失效用户商品券](https://pay.weixin.qq.com/doc/v3/partner/4015781578.md)
-- [退券](https://pay.weixin.qq.com/doc/v3/partner/4015781599.md)
-#### 商品券回调通知
-- [获取商品券事件通知地址](https://pay.weixin.qq.com/doc/v3/partner/4015781284.md)
-- [设置商品券事件通知地址](https://pay.weixin.qq.com/doc/v3/partner/4015781286.md)
-- [商品券回调通知](https://pay.weixin.qq.com/doc/v3/partner/4015780862.md)
-#### 生成商品券头图
-- [提交图片生成任务](https://pay.weixin.qq.com/doc/v3/partner/4017327735.md)
-- [查询图片生成任务执行结果](https://pay.weixin.qq.com/doc/v3/partner/4017327739.md)
-- [图片生成回调通知](https://pay.weixin.qq.com/doc/v3/partner/4017327744.md)
-### 附录
-- [小程序发券组件开发指引](https://pay.weixin.qq.com/doc/v3/partner/4016434329.md)
-- [小程序核销组件开发指引](https://pay.weixin.qq.com/doc/v3/partner/4016110741.md)
-- [品牌、服务商、appid关联关系](https://pay.weixin.qq.com/doc/v3/partner/4018984107.md)
-- [商品券可核销时间规则说明（coupon_available_period）](https://pay.weixin.qq.com/doc/v3/partner/4016675999.md)
-- [商品券客户端消息推送页面](https://pay.weixin.qq.com/doc/v3/partner/4019005729.md)
-- [商品券结构及修改说明](https://pay.weixin.qq.com/doc/v3/partner/4018984452.md)
-#### API请求示例-创建商品券
-- [【单券-全场-折扣券】API请求示例](https://pay.weixin.qq.com/doc/v3/partner/4016756270.md)
-- [【单券-全场-满减券】API请求示例](https://pay.weixin.qq.com/doc/v3/partner/4016756271.md)
-- [【单券-单品-折扣券】API请求示例](https://pay.weixin.qq.com/doc/v3/partner/4016756272.md)
-- [【单券-单品-满减券】API请求示例](https://pay.weixin.qq.com/doc/v3/partner/4016756273.md)
-- [【单券-单品-兑换券】API请求示例](https://pay.weixin.qq.com/doc/v3/partner/4016756274.md)
-## 商品券（多次优惠）
-> 商品券（多次优惠）为多轮次阶梯优惠券，由多个批次组成批次组，支持 3-15 次核销并可设置使用间隔，每轮核销后解锁下一优惠，适合次卡、复购激励等长期锁客场景。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4016438787.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4016438816.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016950439.md)
-### API列表
-- [图片上传](https://pay.weixin.qq.com/doc/v3/partner/4016435731.md)
-#### 商品券管理
-- [创建商品券](https://pay.weixin.qq.com/doc/v3/partner/4016434630.md)
-- [修改商品券](https://pay.weixin.qq.com/doc/v3/partner/4016434633.md)
-- [查询商品券](https://pay.weixin.qq.com/doc/v3/partner/4016434632.md)
-- [失效商品券](https://pay.weixin.qq.com/doc/v3/partner/4016434631.md)
-#### 商品券批次管理
-- [添加商品券批次组](https://pay.weixin.qq.com/doc/v3/partner/4016280622.md)
-- [查询商品券批次列表](https://pay.weixin.qq.com/doc/v3/partner/4016434641.md)
-- [查询商品券指定批次](https://pay.weixin.qq.com/doc/v3/partner/4016434649.md)
-- [修改商品券批次组](https://pay.weixin.qq.com/doc/v3/partner/4016280633.md)
-- [修改商品券批次组发放预算](https://pay.weixin.qq.com/doc/v3/partner/4016280642.md)
-- [批次组批量关联门店](https://pay.weixin.qq.com/doc/v3/partner/4016280620.md)
-- [批次组批量取消关联门店](https://pay.weixin.qq.com/doc/v3/partner/4016280629.md)
-- [查询批次关联门店列表](https://pay.weixin.qq.com/doc/v3/partner/4016434665.md)
-- [预上传券Code](https://pay.weixin.qq.com/doc/v3/partner/4016434668.md)
-#### 商品券发放
-- [向用户发放商品券批次组](https://pay.weixin.qq.com/doc/v3/partner/4016280664.md)
-- [确认发放用户商品券](https://pay.weixin.qq.com/doc/v3/partner/4016435562.md)
-##### 小程序发券组件
-- [向用户预发放商品券批次组](https://pay.weixin.qq.com/doc/v3/partner/4016280670.md)
-- [调起小程序发券组件](https://pay.weixin.qq.com/doc/v3/partner/4016435568.md)
-#### 商品券核销
-- [核销用户商品券](https://pay.weixin.qq.com/doc/v3/partner/4016435636.md)
-- [调起小程序核销组件](https://pay.weixin.qq.com/doc/v3/partner/4016435640.md)
-#### 商品券查询
-- [查询用户商品券详情](https://pay.weixin.qq.com/doc/v3/partner/4016435702.md)
-- [指定券状态查询用户商品券列表](https://pay.weixin.qq.com/doc/v3/partner/4016435703.md)
-#### 商品券失效与退券
-- [失效用户商品券组](https://pay.weixin.qq.com/doc/v3/partner/4016280658.md)
-- [退券](https://pay.weixin.qq.com/doc/v3/partner/4016435674.md)
-#### 商品券回调通知
-- [获取商品券事件通知地址](https://pay.weixin.qq.com/doc/v3/partner/4016435718.md)
-- [设置商品券事件通知地址](https://pay.weixin.qq.com/doc/v3/partner/4016435719.md)
-- [商品券回调通知](https://pay.weixin.qq.com/doc/v3/partner/4016435717.md)
-#### 生成商品券头图
-- [提交图片生成任务](https://pay.weixin.qq.com/doc/v3/partner/4017327752.md)
-- [查询图片生成任务执行结果](https://pay.weixin.qq.com/doc/v3/partner/4017327753.md)
-- [图片生成回调通知](https://pay.weixin.qq.com/doc/v3/partner/4017327759.md)
-### 附录
-- [小程序发券组件开发指引](https://pay.weixin.qq.com/doc/v3/partner/4016435566.md)
-- [小程序核销组件开发指引](https://pay.weixin.qq.com/doc/v3/partner/4016435642.md)
-- [品牌、服务商、appid关联关系](https://pay.weixin.qq.com/doc/v3/partner/4018984192.md)
-- [商品券可核销时间规则说明（coupon_available_period）](https://pay.weixin.qq.com/doc/v3/partner/4016676012.md)
-- [商品券客户端消息推送页面](https://pay.weixin.qq.com/doc/v3/partner/4019005741.md)
-- [商品券结构及修改说明](https://pay.weixin.qq.com/doc/v3/partner/4018984437.md)
-#### API请求示例-创建商品券
-- [【多次优惠-全场-折扣券】API请求示例](https://pay.weixin.qq.com/doc/v3/partner/4016756283.md)
-- [【多次优惠-全场-满减券】API请求示例](https://pay.weixin.qq.com/doc/v3/partner/4016756284.md)
-- [【多次优惠-单品-折扣券】API请求示例](https://pay.weixin.qq.com/doc/v3/partner/4016756285.md)
-- [【多次优惠-单品-满减券】API请求示例](https://pay.weixin.qq.com/doc/v3/partner/4016756286.md)
-- [【多次优惠-单品-兑换券】API请求示例](https://pay.weixin.qq.com/doc/v3/partner/4016756287.md)
-## 品牌门店
-> 品牌线下门店信息管理工具，支持地图选点和文件批量上传两种方式录入门店。录入后可在名片展示地址、营业状态等信息，可用于商品券适用门店圈定、摇优惠按位置精准投放，有效提升用户到店转化率。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4016628074.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4016628135.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016705104.md)
-### API列表
-- [创建品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4015783183.md)
-- [查询品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4015783153.md)
-- [查询品牌门店列表](https://pay.weixin.qq.com/doc/v3/partner/4016756674.md)
-- [更新品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4015783158.md)
-- [删除品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4015783113.md)
-- [暂停门店营业](https://pay.weixin.qq.com/doc/v3/partner/4016756671.md)
-- [恢复门店营业](https://pay.weixin.qq.com/doc/v3/partner/4016756672.md)
-- [绑定收款商户号](https://pay.weixin.qq.com/doc/v3/partner/4015783177.md)
-- [解绑收款商户号](https://pay.weixin.qq.com/doc/v3/partner/4015783188.md)
-### 附录
-- [品牌经营平台管理品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4016689827.md)
-## 品牌服务商授权
-> 品牌服务商授权是服务商代品牌运营的权限机制，服务商生成授权码由品牌方扫码授权后，服务商可代替品牌操作商品券、门店、商家名片等相关功能，明确权限边界保障运营安全。API接口可协助服务商查询已获取到的授权信息。
-
-### API列表
-- [获得品牌已授权且在生效中的产品权限信息](https://pay.weixin.qq.com/doc/v3/partner/4017410365.md)
-## 连锁品牌分账
-> 连锁品牌分账提供了品牌对门店、连锁业态其它参与者进行更灵活的资金管理能力，支持实时（支付后30s内）、延时分账，单笔最多分 50 次、每次可分 50 方。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012072620.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012072625.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012072637.md)
-- [业务示例代码](https://pay.weixin.qq.com/doc/v3/partner/4015871675.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4015981574.md)
-### API列表
-- [请求分账](https://pay.weixin.qq.com/doc/v3/partner/4012692975.md)
-- [查询分账结果](https://pay.weixin.qq.com/doc/v3/partner/4012467002.md)
-- [请求分账回退](https://pay.weixin.qq.com/doc/v3/partner/4012467097.md)
-- [查询分账回退结果](https://pay.weixin.qq.com/doc/v3/partner/4012467011.md)
-- [解冻剩余资金](https://pay.weixin.qq.com/doc/v3/partner/4012467016.md)
-- [查询订单剩余待分金额](https://pay.weixin.qq.com/doc/v3/partner/4012467021.md)
-- [查询最大分账比例](https://pay.weixin.qq.com/doc/v3/partner/4012467022.md)
-- [添加分账接收方](https://pay.weixin.qq.com/doc/v3/partner/4012467100.md)
-- [删除分账接收方](https://pay.weixin.qq.com/doc/v3/partner/4012467103.md)
-- [分账动账通知](https://pay.weixin.qq.com/doc/v3/partner/4012075400.md)
-- [申请分账账单](https://pay.weixin.qq.com/doc/v3/partner/4012715572.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4012076073.md)
-### 附录
-- [分账失败处理指引](https://pay.weixin.qq.com/doc/v3/partner/4015504918.md)
-## 清关报关（V2）
-> 清关报关是微信支付面向跨境商户的自助清关工具，商户可在商户平台开通并配置海关信息，通过接口将支付单推送至海关电子口岸，完成 “三单合一” 申报，助力跨境订单合规通关，提升清关效率，免费使用。
-
-- [清关报关（V2）](https://pay.weixin.qq.com/doc/v3/partner/4012851220.md)
-## 消费者投诉2.0
-> 消费者投诉 2.0 提供商户端线上投诉协同处理能力，支持实时获取投诉信息、在线协商、上传凭证、反馈处理结果，全流程可追溯。帮助商户高效处理交易纠纷，提升用户体验，降低合规与经营风险，适配多行业售后管理。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012072827.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012072844.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012072858.md)
-- [业务示例代码](https://pay.weixin.qq.com/doc/v3/partner/4015933338.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016111688.md)
-### API列表
-#### 主动查询投诉信息
-- [查询投诉单列表](https://pay.weixin.qq.com/doc/v3/partner/4012691285.md)
-- [查询投诉单详情](https://pay.weixin.qq.com/doc/v3/partner/4012691648.md)
-- [查询投诉单协商历史](https://pay.weixin.qq.com/doc/v3/partner/4012691802.md)
-#### 实时获取投诉信息
-- [投诉通知回调](https://pay.weixin.qq.com/doc/v3/partner/4012076174.md)
-- [创建投诉通知回调地址](https://pay.weixin.qq.com/doc/v3/partner/4012458106.md)
-- [查询投诉通知回调地址](https://pay.weixin.qq.com/doc/v3/partner/4012459065.md)
-- [更新投诉通知回调地址](https://pay.weixin.qq.com/doc/v3/partner/4012459287.md)
-- [删除投诉通知回调地址](https://pay.weixin.qq.com/doc/v3/partner/4012460474.md)
-#### 商户处理用户投诉
-- [回复用户](https://pay.weixin.qq.com/doc/v3/partner/4012467213.md)
-- [反馈处理完成](https://pay.weixin.qq.com/doc/v3/partner/4012467217.md)
-- [更新退款审批结果](https://pay.weixin.qq.com/doc/v3/partner/4012467218.md)
-- [回复需要即时服务的投诉单](https://pay.weixin.qq.com/doc/v3/partner/4017151726.md)
-#### 商户反馈图片
-- [图片上传接口](https://pay.weixin.qq.com/doc/v3/partner/4012467222.md)
-- [图片请求接口](https://pay.weixin.qq.com/doc/v3/partner/4012467223.md)
-## 微信电子发票
-> 微信电子发票提供从开票、接收到归档的全流程电子化方案，用户支付后可通过微信支付凭证页申请发票，并通过微信卡包接收发票，提升了用户体验，降低了商户开纸质发票的成本，增强了商户与用户的服务连接。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4015792553.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4015792554.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4015792556.md)
-- [业务示例代码](https://pay.weixin.qq.com/doc/v3/partner/4016078358.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016960715.md)
-### API列表
-- [获取开通服务商电子发票能力邀请链接](https://pay.weixin.qq.com/doc/v3/partner/4015941495.md)
-- [获取邀请开通的商户信息](https://pay.weixin.qq.com/doc/v3/partner/4015941524.md)
-- [检查子商户开票功能状态](https://pay.weixin.qq.com/doc/v3/partner/4015792561.md)
-- [创建电子发票卡券模板](https://pay.weixin.qq.com/doc/v3/partner/4015792562.md)
-- [配置开发选项](https://pay.weixin.qq.com/doc/v3/partner/4015792563.md)
-- [获取用户抬头填写链接](https://pay.weixin.qq.com/doc/v3/partner/4015770776.md)
-- [获取用户填写抬头信息](https://pay.weixin.qq.com/doc/v3/partner/4015784260.md)
-- [开具通用行业电子发票](https://pay.weixin.qq.com/doc/v3/partner/4015792574.md)
-- [开具不动产租赁行业电子发票](https://pay.weixin.qq.com/doc/v3/partner/4015941740.md)
-- [开具成品油行业电子发票](https://pay.weixin.qq.com/doc/v3/partner/4016760559.md)
-- [冲红电子发票](https://pay.weixin.qq.com/doc/v3/partner/4015792575.md)
-- [查询电子发票](https://pay.weixin.qq.com/doc/v3/partner/4015792567.md)
-- [获取发票下载信息](https://pay.weixin.qq.com/doc/v3/partner/4015792576.md)
-- [下载发票文件](https://pay.weixin.qq.com/doc/v3/partner/4015792569.md)
-- [上传电子发票文件](https://pay.weixin.qq.com/doc/v3/partner/4015792580.md)
-- [将电子发票插入微信用户卡包](https://pay.weixin.qq.com/doc/v3/partner/4015792579.md)
-- [用户发票抬头填写完成通知](https://pay.weixin.qq.com/doc/v3/partner/4015792559.md)
-- [发票开具成功通知](https://pay.weixin.qq.com/doc/v3/partner/4015792570.md)
-- [发票插入用户卡包成功通知](https://pay.weixin.qq.com/doc/v3/partner/4015792578.md)
-- [发票冲红成功通知](https://pay.weixin.qq.com/doc/v3/partner/4015792571.md)
-- [发票卡券作废通知](https://pay.weixin.qq.com/doc/v3/partner/4015792560.md)
-### 附录
-- [成品油单位转换公式](https://pay.weixin.qq.com/doc/v3/partner/4016730844.md)
-## 特约商户进件
-> 面向普通服务商的高效进件接口，支持个体户、企业、机关事业单位及其他组织快速接入，可对接自有系统提升效率，入驻后自动绑定 AppID 快速交易，支持优惠费率与快捷验证，还可协助修改结算账户，大幅降低人工录入成本，规范商户准入流程。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012062365.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012062375.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012062379.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016058480.md)
-### API列表
-- [提交申请单](https://pay.weixin.qq.com/doc/v3/partner/4012719997.md)
-- [申请单号查询申请状态](https://pay.weixin.qq.com/doc/v3/partner/4012697052.md)
-- [业务申请编号查询申请状态](https://pay.weixin.qq.com/doc/v3/partner/4012697168.md)
-- [修改结算账户](https://pay.weixin.qq.com/doc/v3/partner/4012761102.md)
-- [查询结算账户](https://pay.weixin.qq.com/doc/v3/partner/4012761113.md)
-- [查询结算账户修改申请状态](https://pay.weixin.qq.com/doc/v3/partner/4012761120.md)
-- [文件上传](https://pay.weixin.qq.com/doc/v3/partner/4012760490.md)
-- [视频上传](https://pay.weixin.qq.com/doc/v3/partner/4012761084.md)
-## 商户开户意愿确认
-> 商户开通微信支付的合规确认环节，用于核验商户真实开户意愿与主体身份，通过线上授权、扫码验证等方式完成确认，保障开户合规安全，是商户正常使用支付、结算等功能的必要前提，有效防范虚假开户与冒用开户风险。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012064820.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012064824.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012064832.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016644196.md)
-### API列表
-- [提交申请单](https://pay.weixin.qq.com/doc/v3/partner/4012722388.md)
-- [撤销申请单](https://pay.weixin.qq.com/doc/v3/partner/4012697627.md)
-- [查询申请单审核结果](https://pay.weixin.qq.com/doc/v3/partner/4012697715.md)
-- [获取商户开户意愿确认状态](https://pay.weixin.qq.com/doc/v3/partner/4012467549.md)
-- [图片上传](https://pay.weixin.qq.com/doc/v3/partner/4012760509.md)
-## 商户平台处置通知
-> 为服务商提供子商户风险处置相关的回调通知服务，覆盖处罚、拦截、申诉三种通知类型，便于服务商快速响应处理，避免因逾期处置导致商户功能受限，提升商户风控管理与合规运营效率。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012064844.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012064851.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012064853.md)
-- [业务示例代码](https://pay.weixin.qq.com/doc/v3/partner/4015949382.md)
-### API列表
-#### 商户违规通知回调
-- [查询商户违规通知回调地址](https://pay.weixin.qq.com/doc/v3/partner/4012471327.md)
-- [修改商户违规通知回调地址](https://pay.weixin.qq.com/doc/v3/partner/4012471330.md)
-- [创建商户违规通知回调地址](https://pay.weixin.qq.com/doc/v3/partner/4012471333.md)
-- [删除商户违规通知回调地址](https://pay.weixin.qq.com/doc/v3/partner/4012471334.md)
-- [商户平台处置记录回调通知](https://pay.weixin.qq.com/doc/v3/partner/4012079216.md)
-## 不活跃商户身份核实
-> 针对长期无交易的不活跃商户开展的合规身份核验，用于确认商户经营状态与身份信息有效性，商户按指引完成资料更新与身份验证后可恢复正常功能，满足监管要求，降低沉睡商户带来的合规与资金风险。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012064898.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012064902.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012064909.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4012064915.md)
-### API列表
-- [发起不活跃商户身份核实](https://pay.weixin.qq.com/doc/v3/partner/4012471357.md)
-- [查询不活跃商户身份核实结果](https://pay.weixin.qq.com/doc/v3/partner/4012471359.md)
-### 附录
-- [关键概念](https://pay.weixin.qq.com/doc/v3/partner/4012064904.md)
-## 商户被管控能力及原因查询
-> 服务商可查询子商户支付、提现、退款、分账等功能管控状态，同步获取管控原因、解脱路径与处理指引，快速定位问题并协助商户提交材料办理解除管控，提升商户异常处理效率，保障正常经营与资金流转。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012165270.md)
-### API列表
-- [查询子商户管控情况 ](https://pay.weixin.qq.com/doc/v3/partner/4012803072.md)
-## 合作伙伴订阅
-> 合作伙伴订阅功能为微信支付服务商专属消息推送服务，支持自主订阅商户进件、交易流水、状态变更等各类业务通知，配置接收地址即可实时推送消息，方便服务商及时掌握商户动态，高效开展商户运营与日常管理工作。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4016022264.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4016022266.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016550707.md)
-## 微信支付公钥
-> 微信支付公钥可用于验证微信支付应答与回调消息的真实性与完整性，防止伪造与篡改，同时可对敏感信息进行加解密，保障交易与数据安全。商户在 API 安全页面申请下载，一次申请永久有效。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012925323.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4013038589.md)
-### API列表
-- [商户签名验签／加解密测试](https://pay.weixin.qq.com/doc/v3/partner/4015139289.md)
-- [回调接口](https://pay.weixin.qq.com/doc/v3/partner/4019605946.md)
-### 附录
-- [如何从平台证书切换成微信支付公钥](https://pay.weixin.qq.com/doc/v3/partner/4012925289.md)
-- [如何从微信支付公钥切换成平台证书](https://pay.weixin.qq.com/doc/v3/partner/4015419376.md)
-## 平台证书
-> 平台证书与微信支付公钥作用相同，用于验签与敏感字段加解密，保障交易与数据安全，但每次申请的有效期为5年，即每5年，商户需要更换一次证书，可与微信支付公钥切换使用。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012073044.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4012073263.md)
-### API列表
-- [下载平台证书](https://pay.weixin.qq.com/doc/v3/partner/4012715700.md)
-### 附录
-- [平台证书更换操作指引](https://pay.weixin.qq.com/doc/v3/partner/4012073146.md)
-## 平台收付通-电商交易解决方案
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012086891.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/partner/4012086921.md)
-- [消费者投诉2.0](https://pay.weixin.qq.com/doc/v3/partner/4012072827.md)
-### 商户进件
-> 商户进件是平台收付通为平台型电商提供的二级商户入驻服务，通过接口协助平台下商户快速完成微信支付二级商户入驻，统一管理商户资质与准入流程，为后续合单支付、分账结算、资金管控等核心能力提供合规主体基础，保障平台交易链路顺畅运行。
-
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012087137.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4012525423.md)
-#### API列表
-- [提交申请单](https://pay.weixin.qq.com/doc/v3/partner/4012713017.md)
-- [通过业务申请编号查询申请状态](https://pay.weixin.qq.com/doc/v3/partner/4012691376.md)
-- [通过申请单ID查询申请状态](https://pay.weixin.qq.com/doc/v3/partner/4012691469.md)
-- [修改结算账户](https://pay.weixin.qq.com/doc/v3/partner/4012761138.md)
-- [查询结算账户](https://pay.weixin.qq.com/doc/v3/partner/4012761142.md)
-- [查询结算账户修改申请状态](https://pay.weixin.qq.com/doc/v3/partner/4012761169.md)
-- [文件上传](https://pay.weixin.qq.com/doc/v3/partner/4012760432.md)
-### 商户注销
-> 商户注销为二级商户提供合规退出通道，支持平台协助二级商户发起注销申请，完成账户资金清算与余额提现，规范商户生命周期管理。注销后可按规则将账户可用余额提现至指定账户，保障资金安全结清，避免遗留风险。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4018153750.md)
-#### 注销预校验
-##### API列表
-- [商户注销资格校验](https://pay.weixin.qq.com/doc/v3/partner/4016420099.md)
-#### 注销提现（新流程）
-##### API列表
-- [提交注销提现申请](https://pay.weixin.qq.com/doc/v3/partner/4013892756.md)
-- [商户申请单号查询申请单状态](https://pay.weixin.qq.com/doc/v3/partner/4013892759.md)
-- [微信支付申请单号查询申请单状态](https://pay.weixin.qq.com/doc/v3/partner/4013892765.md)
-#### 注销申请与提现（旧流程）
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4015943239.md)
-##### 注销申请
-###### API列表
-###### 注销申请单
-- [提交注销申请单](https://pay.weixin.qq.com/doc/v3/partner/4012476217.md)
-- [查询注销单状态](https://pay.weixin.qq.com/doc/v3/partner/4012476223.md)
-###### 图片上传
-- [图片上传](https://pay.weixin.qq.com/doc/v3/partner/4012691710.md)
-##### 注销后提现
-###### API列表
-- [提交已注销商户号可用余额提现申请单](https://pay.weixin.qq.com/doc/v3/partner/4012488950.md)
-- [商户提现申请单号查询提现申请单状态](https://pay.weixin.qq.com/doc/v3/partner/4012476164.md)
-- [微信支付提现申请单号查询提现申请单状态](https://pay.weixin.qq.com/doc/v3/partner/4012778400.md)
-### 支付下单
-#### 普通支付
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012088031.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4012525474.md)
-##### API列表
-###### APP支付
-- [APP下单](https://pay.weixin.qq.com/doc/v3/partner/4012714669.md)
-- [APP调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012090168.md)
-###### JSAPI支付
-- [JSAPI下单](https://pay.weixin.qq.com/doc/v3/partner/4012714678.md)
-- [JSAPI调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012090156.md)
-###### Native支付
-- [Native下单](https://pay.weixin.qq.com/doc/v3/partner/4012714902.md)
-- [Native调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012090180.md)
-###### 小程序支付
-- [小程序下单](https://pay.weixin.qq.com/doc/v3/partner/4012714911.md)
-- [小程序调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012090181.md)
-###### H5支付
-- [H5下单](https://pay.weixin.qq.com/doc/v3/partner/4012714759.md)
-- [H5调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012090177.md)
-###### 公共API
-- [微信支付订单号查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012760565.md)
-- [微信支付商户订单号查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012760568.md)
-- [关闭订单](https://pay.weixin.qq.com/doc/v3/partner/4012760574.md)
-- [支付结果通知](https://pay.weixin.qq.com/doc/v3/partner/4012090195.md)
-#### 合单支付
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012089542.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4012525491.md)
-##### API列表
-###### JSAPI合单支付
-- [合单下单-JSAPI](https://pay.weixin.qq.com/doc/v3/partner/4012760615.md)
-- [JSAPI调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012090843.md)
-###### APP合单支付
-- [合单下单-APP](https://pay.weixin.qq.com/doc/v3/partner/4012760622.md)
-- [APP调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012090949.md)
-###### H5合单支付
-- [合单下单-H5](https://pay.weixin.qq.com/doc/v3/partner/4012760626.md)
-- [H5调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012091014.md)
-###### Native合单支付
-- [合单下单-NATIVE](https://pay.weixin.qq.com/doc/v3/partner/4012760629.md)
-- [Native调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012091224.md)
-###### 小程序合单支付
-- [合单下单-小程序](https://pay.weixin.qq.com/doc/v3/partner/4012760633.md)
-- [小程序调起支付](https://pay.weixin.qq.com/doc/v3/partner/4012091236.md)
-###### 公共API
-- [合单查询订单](https://pay.weixin.qq.com/doc/v3/partner/4012761049.md)
-- [合单关闭订单](https://pay.weixin.qq.com/doc/v3/partner/4012761093.md)
-- [支付通知](https://pay.weixin.qq.com/doc/v3/partner/4012237246.md)
-### 补差与分账
-#### 分账
-- [开发指引](https://pay.weixin.qq.com/doc/v3/partner/4012087888.md)
-- [业务示例代码](https://pay.weixin.qq.com/doc/v3/partner/4015870957.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4012525463.md)
-##### API列表
-- [请求分账](https://pay.weixin.qq.com/doc/v3/partner/4012691594.md)
-- [查询分账结果](https://pay.weixin.qq.com/doc/v3/partner/4012477734.md)
-- [请求分账回退](https://pay.weixin.qq.com/doc/v3/partner/4012477737.md)
-- [查询分账回退结果](https://pay.weixin.qq.com/doc/v3/partner/4012477740.md)
-- [解冻剩余资金](https://pay.weixin.qq.com/doc/v3/partner/4012477745.md)
-- [查询订单剩余待分金额](https://pay.weixin.qq.com/doc/v3/partner/4012477751.md)
-- [添加分账接收方](https://pay.weixin.qq.com/doc/v3/partner/4012477758.md)
-- [删除分账接收方](https://pay.weixin.qq.com/doc/v3/partner/4012477759.md)
-- [分账动账通知](https://pay.weixin.qq.com/doc/v3/partner/4012116672.md)
-##### 附录
-- [分账失败处理指引](https://pay.weixin.qq.com/doc/v3/partner/4015504955.md)
-#### 补差
-- [业务示例代码](https://pay.weixin.qq.com/doc/v3/partner/4015593692.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4015942503.md)
-##### API列表
-- [请求补差](https://pay.weixin.qq.com/doc/v3/partner/4012477631.md)
-- [请求补差回退](https://pay.weixin.qq.com/doc/v3/partner/4012477636.md)
-- [取消补差](https://pay.weixin.qq.com/doc/v3/partner/4012477639.md)
-### 交易退款
-> 交易退款提供订单全额或部分退款能力，支持已支付订单按流程退回买家。退款资金可从冻结资金中支出，分账后退款可先执行分账回退再退款，平台可查询退款状态，保障交易逆向流程完整，提升售后资金处理效率与用户消费体验。
-
-- [业务示例代码](https://pay.weixin.qq.com/doc/v3/partner/4015217874.md)
-#### API列表
-- [申请退款](https://pay.weixin.qq.com/doc/v3/partner/4012476892.md)
-- [查询单笔退款（按微信支付退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4012476908.md)
-- [查询单笔退款（按商户退款单号）](https://pay.weixin.qq.com/doc/v3/partner/4012476911.md)
-- [退款结果通知](https://pay.weixin.qq.com/doc/v3/partner/4012124635.md)
-- [查询垫付回补结果](https://pay.weixin.qq.com/doc/v3/partner/4012476916.md)
-- [垫付退款回补](https://pay.weixin.qq.com/doc/v3/partner/4012476927.md)
-- [发起异常退款](https://pay.weixin.qq.com/doc/v3/partner/4015181616.md)
-### 账户资金管理
-#### 余额查询
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016644075.md)
-##### API列表
-- [查询二级商户账户实时余额](https://pay.weixin.qq.com/doc/v3/partner/4012476690.md)
-- [查询二级商户账户日终余额](https://pay.weixin.qq.com/doc/v3/partner/4012476693.md)
-- [查询平台账户实时余额](https://pay.weixin.qq.com/doc/v3/partner/4012476700.md)
-- [查询平台账户日终余额](https://pay.weixin.qq.com/doc/v3/partner/4012476702.md)
-#### 商户提现
-- [业务示例代码](https://pay.weixin.qq.com/doc/v3/partner/4019899593.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4014075940.md)
-##### API列表
-- [二级商户预约提现](https://pay.weixin.qq.com/doc/v3/partner/4012476652.md)
-- [二级商户查询预约提现状态（根据商户预约提现单号查询）](https://pay.weixin.qq.com/doc/v3/partner/4012476656.md)
-- [二级商户查询预约提现状态（根据微信支付预约提现单号查询）](https://pay.weixin.qq.com/doc/v3/partner/4012476665.md)
-- [平台预约提现](https://pay.weixin.qq.com/doc/v3/partner/4012476670.md)
-- [平台查询预约提现状态（根据商户预约提现单号查询）](https://pay.weixin.qq.com/doc/v3/partner/4012476672.md)
-- [平台查询预约提现状态（根据微信支付预约提现单号查询）](https://pay.weixin.qq.com/doc/v3/partner/4012476674.md)
-- [二级商户按日终余额预约提现](https://pay.weixin.qq.com/doc/v3/partner/4013328143.md)
-- [查询二级商户按日终余额预约提现状态](https://pay.weixin.qq.com/doc/v3/partner/4013328163.md)
-- [按日下载提现异常文件](https://pay.weixin.qq.com/doc/v3/partner/4012476678.md)
-- [商户提现状态变更通知](https://pay.weixin.qq.com/doc/v3/partner/4013049135.md)
-### 账单下载
-> 账单下载为平台与二级商户提供标准化对账文件，支持交易、资金、分账等多维度账单获取，清晰记录收支、分润、退款等明细。可按日期筛选下载，用于财务核对、结算审计与数据归档，提升平台资金管理透明度与财务处理效率。
-
-- [业务示例代码](https://pay.weixin.qq.com/doc/v3/partner/4016062108.md)
-#### API列表
-- [申请交易账单](https://pay.weixin.qq.com/doc/v3/partner/4012760667.md)
-- [申请资金账单](https://pay.weixin.qq.com/doc/v3/partner/4012760672.md)
-- [申请分账账单](https://pay.weixin.qq.com/doc/v3/partner/4012761131.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/partner/4012124894.md)
-- [申请二级商户资金账单](https://pay.weixin.qq.com/doc/v3/partner/4012760697.md)
-- [申请单个子商户资金账单](https://pay.weixin.qq.com/doc/v3/partner/4012760249.md)
-- [下载单个子商户/二级商户资金账单](https://pay.weixin.qq.com/doc/v3/partner/4014314390.md)
-### 跨境付款
-> 跨境付款依托境内收付通，解决境内平台向境外供应商结算需求，支持多币种汇兑、全球分发、海关一键推单。手续费率可由平台或二级商户承担，提供合规出境、快速结算、报关一体化服务。
-
-- [业务示例代码](https://pay.weixin.qq.com/doc/v3/partner/4015593257.md)
-#### API列表
-- [查询订单剩余可出境余额](https://pay.weixin.qq.com/doc/v3/partner/4012476109.md)
-- [申请资金出境](https://pay.weixin.qq.com/doc/v3/partner/4012476113.md)
-- [查询出境结果](https://pay.weixin.qq.com/doc/v3/partner/4012476127.md)
-- [获取购付汇账单文件下载链接](https://pay.weixin.qq.com/doc/v3/partner/4012476132.md)
-
-## Optional
-### 开发须知
-- [APIv3概述](https://pay.weixin.qq.com/doc/v3/partner/4012081673.md)
-- [总述-APIv3如何签名和验签](https://pay.weixin.qq.com/doc/v3/partner/4012365870.md)
-#### 接口规则说明
-- [基本规则](https://pay.weixin.qq.com/doc/v3/partner/4012081726.md)
-- [HTTP状态码](https://pay.weixin.qq.com/doc/v3/partner/4012081727.md)
-#### 开发参数申请和配置
-- [开发必要参数说明](https://pay.weixin.qq.com/doc/v3/partner/4013080340.md)
-- [mchid与appid申请](https://pay.weixin.qq.com/doc/v3/partner/4012081990.md)
-- [管理商户号绑定的APPID账号](https://pay.weixin.qq.com/doc/v3/partner/4016329059.md)
-- [配置APIv3密钥](https://pay.weixin.qq.com/doc/v3/partner/4012081991.md)
-- [品牌经营API开发必要参数说明](https://pay.weixin.qq.com/doc/v3/partner/4015981654.md)
-- [平台员工权限管理](https://pay.weixin.qq.com/doc/v3/partner/4013080349.md)
-##### 商户API证书管理
-- [申请商户API证书](https://pay.weixin.qq.com/doc/v3/partner/4012081992.md)
-- [如何更换商户API证书？](https://pay.weixin.qq.com/doc/v3/partner/4013058943.md)
-#### 如何签名
-##### 如何构造接口请求签名
-- [请求参数里带Path参数（路径参数），如何计算签名](https://pay.weixin.qq.com/doc/v3/partner/4012365862.md)
-- [请求参数里带Body参数(包体参数），如何计算签名](https://pay.weixin.qq.com/doc/v3/partner/4012365864.md)
-- [请求参数里有Query（查询参数），如何计算签名](https://pay.weixin.qq.com/doc/v3/partner/4012365865.md)
-- [图片上传接口，如何计算签名](https://pay.weixin.qq.com/doc/v3/partner/4012365863.md)
-##### 如何构造调起支付签名
-- [APP调起支付签名](https://pay.weixin.qq.com/doc/v3/partner/4012365868.md)
-- [JSAPI调起支付签名](https://pay.weixin.qq.com/doc/v3/partner/4012365867.md)
-- [小程序调起支付签名](https://pay.weixin.qq.com/doc/v3/partner/4012365869.md)
-#### 如何验签
-- [如何使用微信支付公钥验签](https://pay.weixin.qq.com/doc/v3/partner/4013059017.md)
-##### 如何使用平台证书验签
-- [如何使用平台证书验签名](https://pay.weixin.qq.com/doc/v3/partner/4013059030.md)
-- [如何使用签名/验签工具](https://pay.weixin.qq.com/doc/v3/partner/4012365880.md)
-#### 如何加解密敏感字段
-- [如何使用微信支付公钥加密敏感字段](https://pay.weixin.qq.com/doc/v3/partner/4013059044.md)
-- [如何使用平台证书加密敏感字段](https://pay.weixin.qq.com/doc/v3/partner/4013059053.md)
-- [如何使用API证书解密敏感字段](https://pay.weixin.qq.com/doc/v3/partner/4013059060.md)
-#### 如何解密微信支付回调报文
-- [如何解密回调报文和平台证书](https://pay.weixin.qq.com/doc/v3/partner/4012082320.md)
-#### 常见问题
-- [报错：HTTP header缺少微信支付平台证书序列号(Wechatpay-Serial)](https://pay.weixin.qq.com/doc/v3/partner/4012365874.md)
-- [报错：Http头Authorization值格式错误，请参考《微信支付商户REST API签名规则》或者“Authorization不合法”](https://pay.weixin.qq.com/doc/v3/partner/4012365872.md)
-- [报错：商户证书序列号有误。请使用签名私钥匹配的证书序列号](https://pay.weixin.qq.com/doc/v3/partner/4012365873.md)
-- [报错：状态码401或者“错误的签名，验签失败”或者“签名错误，请检查后再试”](https://pay.weixin.qq.com/doc/v3/partner/4012365875.md)
-- [调起支付报错：支付验证签名失败](https://pay.weixin.qq.com/doc/v3/partner/4012365876.md)
-- [使用Java加载密钥时，抛出异常InvalidKeyException: Illegal key size](https://pay.weixin.qq.com/doc/v3/partner/4013059103.md)
-- [使用Java解密时，抛出异常AEADBadTagException: Tag mismatch](https://pay.weixin.qq.com/doc/v3/partner/4013059153.md)
-- [请求返回{"code":"PARAM_ERROR","message":"平台证书序列号Wechatpay-Serial错误"}](https://pay.weixin.qq.com/doc/v3/partner/4013059161.md)
-- [为什么微信支付的回调缺少签名的几个HTTP头？](https://pay.weixin.qq.com/doc/v3/partner/4013059166.md)
-- [如何在程序中加载商户API证书私钥](https://pay.weixin.qq.com/doc/v3/partner/4013059175.md)
-- [如何查看商户API证书或平台证书序列号？](https://pay.weixin.qq.com/doc/v3/partner/4013059181.md)
-- [为什么请求返回401 Unauthorized？](https://pay.weixin.qq.com/doc/v3/partner/4012082324.md)
-- [验证微信支付响应的签名报错：签名验证失败](https://pay.weixin.qq.com/doc/v3/partner/4016241895.md)
-- [调用接口报错：“平台私钥解密失败”](https://pay.weixin.qq.com/doc/v3/partner/4016913182.md)
-### 最佳实践
-- [跨城冗灾升级指引](https://pay.weixin.qq.com/doc/v3/partner/4012082567.md)
-- [支付回调和查单实现指引](https://pay.weixin.qq.com/doc/v3/partner/4012082568.md)
-- [专线商户Notify升级指引](https://pay.weixin.qq.com/doc/v3/partner/4012082569.md)
-- [回调通知注意事项](https://pay.weixin.qq.com/doc/v3/partner/4012082570.md)
-#### API安全最佳实践
-- [最佳安全实践](https://pay.weixin.qq.com/doc/v3/partner/4012082456.md)
-- [安全漏洞checklist](https://pay.weixin.qq.com/doc/v3/partner/4013059657.md)
-- [系统漏洞检测及修复](https://pay.weixin.qq.com/doc/v3/partner/4013059668.md)
-- [Web漏洞检测及修复](https://pay.weixin.qq.com/doc/v3/partner/4013059740.md)
-- [最新安全漏洞及修复](https://pay.weixin.qq.com/doc/v3/partner/4013059970.md)
-- [密钥泄漏修复指引](https://pay.weixin.qq.com/doc/v3/partner/4012082455.md)
-### 国家商用密码接入指南
-- [国家商用密码简介](https://pay.weixin.qq.com/doc/v3/partner/4012082627.md)
-- [获取国家商用密码证书和密钥](https://pay.weixin.qq.com/doc/v3/partner/4012082628.md)
-- [APIv3接口使用国家商用密码指引](https://pay.weixin.qq.com/doc/v3/partner/4012082629.md)
-### 对照表
-- [开户银行全称对照表](https://pay.weixin.qq.com/doc/v3/partner/4012082812.md)
-- [开户银行对照表](https://pay.weixin.qq.com/doc/v3/partner/4012082813.md)
-- [银行类型对照表](https://pay.weixin.qq.com/doc/v3/partner/4012082814.md)
-- [省市区编号对照表](https://pay.weixin.qq.com/doc/v3/partner/4012082815.md)
-- [优惠费率活动对照表](https://pay.weixin.qq.com/doc/v3/partner/4012082816.md)
-- [跨境电商二级商户费率对照表](https://pay.weixin.qq.com/doc/v3/partner/4012082817.md)
-- [商户行业编码](https://pay.weixin.qq.com/doc/v3/partner/4012082818.md)
-- [特殊行业ID对照表](https://pay.weixin.qq.com/doc/v3/partner/4012082819.md)
-### 名词表
-- [接入模式](https://pay.weixin.qq.com/doc/v3/partner/4012081931.md)
-- [支付产品](https://pay.weixin.qq.com/doc/v3/partner/4012081932.md)
-- [业务平台](https://pay.weixin.qq.com/doc/v3/partner/4012081933.md)
-- [业务系统](https://pay.weixin.qq.com/doc/v3/partner/4012081934.md)
-- [参数说明](https://pay.weixin.qq.com/doc/v3/partner/4012081935.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4016183684.md)
-### 服务运营规范
-- [微信支付链路界面与交互规范](https://pay.weixin.qq.com/doc/v3/partner/4020527499.md)
-
-### 开发工具
-- [Postman调试工具](https://pay.weixin.qq.com/doc/v3/partner/4012083114.md)
-- [平台证书下载工具](https://pay.weixin.qq.com/doc/v3/partner/4012083115.md)
-- [验签工具](https://pay.weixin.qq.com/doc/v3/partner/4012083116.md)
-### 网络云排查
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012083118.md)
-- [网络问题排查指南](https://pay.weixin.qq.com/doc/v3/partner/4012083119.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/partner/4012083120.md)
-### 安全医生
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/partner/4012083122.md)
-- [诊断链接绑定指引](https://pay.weixin.qq.com/doc/v3/partner/4012083123.md)
-- [安全联系人设置指引](https://pay.weixin.qq.com/doc/v3/partner/4012083124.md)
-### SDK
-- [SDK概述](https://pay.weixin.qq.com/doc/v3/partner/4012083109.md)
-- [使用 Java SDK](https://pay.weixin.qq.com/doc/v3/partner/4012083111.md)
-- [使用 PHP SDK](https://pay.weixin.qq.com/doc/v3/partner/4012083112.md)
-- [使用 Go SDK](https://pay.weixin.qq.com/doc/v3/partner/4012083113.md)
-
```

## 删除页面

- **商品券接入Skill** (`4018929846`)
  - 原路径: Skills
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018929846.md
  - 原更新时间: 2026-04-09 02:43:55

- **基础支付接入Skill** (`4019636341`)
  - 原路径: Skills
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4019636341.md
  - 原更新时间: 2026-04-09 03:11:59

- **Go** (`4015119446`)
  - 原路径: 示例代码
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015119446.md
  - 原更新时间: 2025-05-29 03:20:44

- **Java** (`4014985777`)
  - 原路径: 示例代码
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4014985777.md
  - 原更新时间: 2025-05-27 08:03:58

- **付款码支付（V2）** (`4012851192`)
  - 原路径: 付款码支付（V2）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012851192.md
  - 原更新时间: 2025-04-25 07:54:10

- **刷脸支付** (`4012851199`)
  - 原路径: 刷脸支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012851199.md
  - 原更新时间: 2024-10-28 07:53:13

- **产品介绍** (`4012069852`)
  - 原路径: JSAPI支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012069852.md
  - 原更新时间: 2026-05-21 03:22:54

- **开发接入准备** (`4012069853`)
  - 原路径: JSAPI支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012069853.md
  - 原更新时间: 2026-05-19 08:35:53

- **开发指引** (`4012069859`)
  - 原路径: JSAPI支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012069859.md
  - 原更新时间: 2026-02-28 08:04:00

- **常见问题** (`4013334850`)
  - 原路径: JSAPI支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013334850.md
  - 原更新时间: 2026-05-19 07:37:15

- **JSAPI/小程序下单** (`4012738519`)
  - 原路径: JSAPI支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012738519.md
  - 原更新时间: 2025-03-31 06:14:54

- **JSAPI调起支付** (`4012069855`)
  - 原路径: JSAPI支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012069855.md
  - 原更新时间: 2025-02-26 07:08:25

- **微信支付订单号查询订单** (`4012738964`)
  - 原路径: JSAPI支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012738964.md
  - 原更新时间: 2025-01-16 07:08:59

- **关闭订单** (`4012739019`)
  - 原路径: JSAPI支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012739019.md
  - 原更新时间: 2025-01-16 07:08:55

- **支付成功回调通知** (`4012085146`)
  - 原路径: JSAPI支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085146.md
  - 原更新时间: 2025-02-20 03:15:13

- **商户订单号查询订单** (`4012739008`)
  - 原路径: JSAPI支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012739008.md
  - 原更新时间: 2025-01-16 07:08:54

- **申请退款** (`4012739034`)
  - 原路径: JSAPI支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012739034.md
  - 原更新时间: 2025-01-16 07:08:56

- **查询单笔退款（按商户退款单号）** (`4012739043`)
  - 原路径: JSAPI支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012739043.md
  - 原更新时间: 2025-01-16 07:08:57

- **发起异常退款** (`4013335389`)
  - 原路径: JSAPI支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013335389.md
  - 原更新时间: 2025-01-16 07:08:52

- **退款结果回调通知** (`4012085298`)
  - 原路径: JSAPI支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085298.md
  - 原更新时间: 2025-02-20 03:14:52

- **申请所有/单个子商户交易账单** (`4012739068`)
  - 原路径: JSAPI支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012739068.md
  - 原更新时间: 2025-01-16 07:08:51

- **申请服务商资金账单** (`4012739125`)
  - 原路径: JSAPI支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012739125.md
  - 原更新时间: 2025-01-16 07:08:50

- **下载账单** (`4012085421`)
  - 原路径: JSAPI支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085421.md
  - 原更新时间: 2024-12-23 03:48:08

- **管理商户号绑定的APPID账号** (`4013335081`)
  - 原路径: JSAPI支付 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013335081.md
  - 原更新时间: 2024-12-23 08:19:22

- **配置JSAPI支付授权目录** (`4013335127`)
  - 原路径: JSAPI支付 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013335127.md
  - 原更新时间: 2024-12-20 08:32:45

- **产品介绍** (`4013080227`)
  - 原路径: APP支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080227.md
  - 原更新时间: 2026-05-21 03:24:50

- **开发接入准备** (`4013080228`)
  - 原路径: APP支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080228.md
  - 原更新时间: 2026-05-19 08:36:11

- **开发指引** (`4013080246`)
  - 原路径: APP支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080246.md
  - 原更新时间: 2026-01-16 02:06:34

- **常见问题** (`4013080245`)
  - 原路径: APP支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080245.md
  - 原更新时间: 2026-05-21 03:25:44

- **APP下单** (`4013080231`)
  - 原路径: APP支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080231.md
  - 原更新时间: 2025-03-31 06:14:51

- **APP调起支付** (`4013080233`)
  - 原路径: APP支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080233.md
  - 原更新时间: 2025-02-18 08:14:07

- **微信支付订单号查询订单** (`4013080234`)
  - 原路径: APP支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080234.md
  - 原更新时间: 2025-01-16 07:08:59

- **商户订单号查询订单** (`4013080235`)
  - 原路径: APP支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080235.md
  - 原更新时间: 2025-01-16 07:08:54

- **关闭订单** (`4013080236`)
  - 原路径: APP支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080236.md
  - 原更新时间: 2025-01-16 07:08:55

- **支付成功回调通知** (`4013080237`)
  - 原路径: APP支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080237.md
  - 原更新时间: 2025-01-14 02:26:27

- **申请退款** (`4013080238`)
  - 原路径: APP支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080238.md
  - 原更新时间: 2025-01-16 07:08:56

- **查询单笔退款（按商户退款单号）** (`4013080239`)
  - 原路径: APP支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080239.md
  - 原更新时间: 2025-01-16 07:08:57

- **发起异常退款** (`4013080240`)
  - 原路径: APP支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080240.md
  - 原更新时间: 2025-01-16 07:08:52

- **退款结果通知** (`4013080241`)
  - 原路径: APP支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080241.md
  - 原更新时间: 2024-12-30 07:47:39

- **申请所有/单个子商户交易账单** (`4013080242`)
  - 原路径: APP支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080242.md
  - 原更新时间: 2025-01-16 07:08:51

- **申请服务商资金账单** (`4013080243`)
  - 原路径: APP支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080243.md
  - 原更新时间: 2025-01-16 07:08:50

- **下载账单** (`4013080230`)
  - 原路径: APP支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080230.md
  - 原更新时间: 2024-12-23 03:48:08

- **管理商户号绑定的APPID账号** (`4013357894`)
  - 原路径: APP支付 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013357894.md
  - 原更新时间: 2024-12-24 02:07:53

- **OpenSDK接入指南** (`4013369798`)
  - 原路径: APP支付 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013369798.md
  - 原更新时间: 2024-12-25 10:48:19

- **产品介绍** (`4012074916`)
  - 原路径: H5支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012074916.md
  - 原更新时间: 2026-05-21 03:26:43

- **开发接入准备** (`4012074917`)
  - 原路径: H5支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012074917.md
  - 原更新时间: 2026-05-19 08:36:25

- **开发指引** (`4012074915`)
  - 原路径: H5支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012074915.md
  - 原更新时间: 2025-11-20 08:44:46

- **常见问题** (`4013336079`)
  - 原路径: H5支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013336079.md
  - 原更新时间: 2025-10-15 08:12:08

- **H5下单** (`4012738604`)
  - 原路径: H5支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012738604.md
  - 原更新时间: 2025-03-31 06:14:50

- **H5调起支付** (`4012085683`)
  - 原路径: H5支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085683.md
  - 原更新时间: 2024-12-23 02:14:31

- **支付成功回调通知** (`4012085680`)
  - 原路径: H5支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085680.md
  - 原更新时间: 2025-02-20 03:15:13

- **微信支付订单号查询订单** (`4012738969`)
  - 原路径: H5支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012738969.md
  - 原更新时间: 2025-01-16 07:08:59

- **商户订单号查询订单** (`4012759661`)
  - 原路径: H5支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759661.md
  - 原更新时间: 2025-01-16 07:08:54

- **关闭订单** (`4012759669`)
  - 原路径: H5支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759669.md
  - 原更新时间: 2025-01-16 07:08:55

- **申请退款** (`4012759673`)
  - 原路径: H5支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759673.md
  - 原更新时间: 2025-01-16 07:08:56

- **查询单笔退款（通过商户退款单号）** (`4012759680`)
  - 原路径: H5支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759680.md
  - 原更新时间: 2025-01-16 07:08:57

- **发起异常退款** (`4013351901`)
  - 原路径: H5支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013351901.md
  - 原更新时间: 2025-01-16 07:08:52

- **退款结果通知** (`4012085681`)
  - 原路径: H5支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085681.md
  - 原更新时间: 2025-02-20 03:14:52

- **申请所有/单个子商户交易账单** (`4012759683`)
  - 原路径: H5支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759683.md
  - 原更新时间: 2025-01-16 07:08:51

- **申请服务商资金账单** (`4012759690`)
  - 原路径: H5支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759690.md
  - 原更新时间: 2025-01-16 07:08:50

- **下载账单** (`4012085682`)
  - 原路径: H5支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085682.md
  - 原更新时间: 2024-12-23 03:48:08

- **管理商户号绑定的APPID账号** (`4013336007`)
  - 原路径: H5支付 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013336007.md
  - 原更新时间: 2024-12-23 08:19:20

- **配置H5支付域名** (`4013336019`)
  - 原路径: H5支付 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013336019.md
  - 原更新时间: 2026-01-09 08:20:43

- **H5收银台适老化字体规范** (`4013358769`)
  - 原路径: H5支付 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013358769.md
  - 原更新时间: 2024-12-24 03:30:20

- **获取用户ip指引** (`4018675960`)
  - 原路径: H5支付 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018675960.md
  - 原更新时间: 2026-03-13 07:56:12

- **产品介绍** (`4012076267`)
  - 原路径: Native支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076267.md
  - 原更新时间: 2026-05-21 03:28:32

- **开发接入准备** (`4012076268`)
  - 原路径: Native支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076268.md
  - 原更新时间: 2026-05-19 08:36:38

- **开发指引** (`4012076269`)
  - 原路径: Native支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076269.md
  - 原更新时间: 2025-11-20 08:44:29

- **常见问题** (`4013352076`)
  - 原路径: Native支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013352076.md
  - 原更新时间: 2026-05-21 03:29:23

- **Native下单** (`4012738659`)
  - 原路径: Native支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012738659.md
  - 原更新时间: 2025-03-31 06:15:38

- **Native调起支付** (`4012085878`)
  - 原路径: Native支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085878.md
  - 原更新时间: 2025-03-21 07:41:33

- **支付成功回调通知** (`4012085875`)
  - 原路径: Native支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085875.md
  - 原更新时间: 2025-02-20 03:15:13

- **关闭订单** (`4012759725`)
  - 原路径: Native支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759725.md
  - 原更新时间: 2025-01-16 07:08:55

- **微信支付订单号查询订单** (`4012738971`)
  - 原路径: Native支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012738971.md
  - 原更新时间: 2025-01-16 07:08:59

- **商户订单号查询订单** (`4012759714`)
  - 原路径: Native支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759714.md
  - 原更新时间: 2025-01-16 07:08:54

- **申请退款** (`4012759727`)
  - 原路径: Native支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759727.md
  - 原更新时间: 2025-01-16 07:08:56

- **查询单笔退款（通过商户退款单号）** (`4012759733`)
  - 原路径: Native支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759733.md
  - 原更新时间: 2025-01-16 07:08:57

- **发起异常退款** (`4013352066`)
  - 原路径: Native支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013352066.md
  - 原更新时间: 2025-01-16 07:08:52

- **退款结果回调通知** (`4012085876`)
  - 原路径: Native支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085876.md
  - 原更新时间: 2025-02-20 03:14:52

- **申请所有/单个子商户交易账单** (`4012759737`)
  - 原路径: Native支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759737.md
  - 原更新时间: 2025-01-16 07:08:51

- **申请服务商资金账单** (`4012759741`)
  - 原路径: Native支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759741.md
  - 原更新时间: 2025-01-16 07:08:50

- **下载账单** (`4012085877`)
  - 原路径: Native支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085877.md
  - 原更新时间: 2024-12-23 03:48:08

- **管理商户号绑定的APPID账号** (`4013352075`)
  - 原路径: Native支付 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013352075.md
  - 原更新时间: 2024-12-23 07:21:48

- **产品介绍** (`4012085810`)
  - 原路径: 小程序支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085810.md
  - 原更新时间: 2026-05-21 03:31:05

- **开发接入准备** (`4012076731`)
  - 原路径: 小程序支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076731.md
  - 原更新时间: 2026-05-19 08:36:53

- **开发指引** (`4012076732`)
  - 原路径: 小程序支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076732.md
  - 原更新时间: 2026-02-28 08:05:10

- **常见问题** (`4013352071`)
  - 原路径: 小程序支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013352071.md
  - 原更新时间: 2026-05-09 08:54:44

- **JSAPI/小程序下单** (`4012759974`)
  - 原路径: 小程序支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759974.md
  - 原更新时间: 2025-03-31 06:14:54

- **小程序调起支付** (`4012085827`)
  - 原路径: 小程序支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085827.md
  - 原更新时间: 2025-02-26 07:10:30

- **支付成功回调通知** (`4012085801`)
  - 原路径: 小程序支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085801.md
  - 原更新时间: 2025-02-20 03:15:13

- **关闭订单** (`4012760108`)
  - 原路径: 小程序支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760108.md
  - 原更新时间: 2025-01-16 07:08:55

- **微信支付订单号查询订单** (`4012738973`)
  - 原路径: 小程序支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012738973.md
  - 原更新时间: 2025-01-16 07:08:59

- **商户订单号查询订单** (`4012760115`)
  - 原路径: 小程序支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760115.md
  - 原更新时间: 2025-01-16 07:08:54

- **申请退款** (`4012760121`)
  - 原路径: 小程序支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760121.md
  - 原更新时间: 2025-01-16 07:08:56

- **查询单笔退款（通过商户退款单号）** (`4012760128`)
  - 原路径: 小程序支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760128.md
  - 原更新时间: 2025-01-16 07:08:57

- **发起异常退款** (`4013352278`)
  - 原路径: 小程序支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013352278.md
  - 原更新时间: 2025-01-16 07:08:52

- **退款结果回调通知** (`4012085802`)
  - 原路径: 小程序支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085802.md
  - 原更新时间: 2025-02-20 03:14:52

- **申请所有/单个子商户交易账单** (`4012760132`)
  - 原路径: 小程序支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760132.md
  - 原更新时间: 2025-01-16 07:08:51

- **申请服务商资金账单** (`4012760136`)
  - 原路径: 小程序支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760136.md
  - 原更新时间: 2025-01-16 07:08:50

- **下载账单** (`4012085803`)
  - 原路径: 小程序支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085803.md
  - 原更新时间: 2024-12-23 03:48:08

- **管理商户号绑定的APPID账号** (`4013352070`)
  - 原路径: 小程序支付 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013352070.md
  - 原更新时间: 2024-12-23 07:21:48

- **产品介绍** (`4012079332`)
  - 原路径: JSAPI合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012079332.md
  - 原更新时间: 2026-05-21 08:20:51

- **开发指引** (`4012166834`)
  - 原路径: JSAPI合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012166834.md
  - 原更新时间: 2025-01-16 06:39:05

- **开发接入准备** (`4013461849`)
  - 原路径: JSAPI合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013461849.md
  - 原更新时间: 2026-05-21 08:21:02

- **常见问题** (`4013462212`)
  - 原路径: JSAPI合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462212.md
  - 原更新时间: 2025-01-16 08:45:12

- **JSAPI合单下单** (`4012757938`)
  - 原路径: JSAPI合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012757938.md
  - 原更新时间: 2025-01-16 08:23:18

- **JSAPI调起支付** (`4012166844`)
  - 原路径: JSAPI合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012166844.md
  - 原更新时间: 2025-02-19 03:55:15

- **查询合单订单** (`4013462164`)
  - 原路径: JSAPI合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462164.md
  - 原更新时间: 2025-01-17 07:39:30

- **关闭合单订单** (`4013462171`)
  - 原路径: JSAPI合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462171.md
  - 原更新时间: 2025-01-16 08:23:11

- **合单订单支付成功回调通知** (`4013462175`)
  - 原路径: JSAPI合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462175.md
  - 原更新时间: 2025-01-16 06:38:52

- **申请退款** (`4013462183`)
  - 原路径: JSAPI合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462183.md
  - 原更新时间: 2025-01-16 07:08:56

- **查询单笔退款（按商户退款单号）** (`4013462188`)
  - 原路径: JSAPI合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462188.md
  - 原更新时间: 2025-01-16 07:08:57

- **发起异常退款** (`4013462191`)
  - 原路径: JSAPI合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462191.md
  - 原更新时间: 2025-01-16 07:08:52

- **退款结果通知** (`4013462195`)
  - 原路径: JSAPI合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462195.md
  - 原更新时间: 2025-01-16 06:38:47

- **申请所有/单个子商户交易账单** (`4013462197`)
  - 原路径: JSAPI合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462197.md
  - 原更新时间: 2025-01-16 07:08:51

- **申请服务商资金账单** (`4013462202`)
  - 原路径: JSAPI合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462202.md
  - 原更新时间: 2025-01-16 07:08:50

- **下载账单** (`4013462207`)
  - 原路径: JSAPI合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462207.md
  - 原更新时间: 2025-01-16 06:38:43

- **合单支付-商户号绑定APPID操作说明** (`4013462628`)
  - 原路径: JSAPI合单支付 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462628.md
  - 原更新时间: 2025-01-16 06:39:56

- **产品介绍** (`4012079331`)
  - 原路径: APP合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012079331.md
  - 原更新时间: 2026-05-21 03:36:02

- **开发指引** (`4012166832`)
  - 原路径: APP合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012166832.md
  - 原更新时间: 2025-06-20 04:11:39

- **常见问题** (`4013461863`)
  - 原路径: APP合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013461863.md
  - 原更新时间: 2025-01-16 08:45:12

- **APP合单下单** (`4012758021`)
  - 原路径: APP合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012758021.md
  - 原更新时间: 2025-01-16 08:23:20

- **APP调起支付** (`4012166845`)
  - 原路径: APP合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012166845.md
  - 原更新时间: 2025-03-28 10:57:37

- **查询合单订单** (`4012761057`)
  - 原路径: APP合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012761057.md
  - 原更新时间: 2025-01-17 07:39:30

- **关闭合单订单** (`4012761079`)
  - 原路径: APP合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012761079.md
  - 原更新时间: 2025-01-16 08:23:11

- **合单订单支付成功回调通知** (`4012231898`)
  - 原路径: APP合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012231898.md
  - 原更新时间: 2025-01-14 09:59:26

- **申请退款** (`4012760207`)
  - 原路径: APP合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760207.md
  - 原更新时间: 2025-01-16 07:08:56

- **查询单笔退款（通过商户退款单号）** (`4012760226`)
  - 原路径: APP合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760226.md
  - 原更新时间: 2025-01-16 07:08:57

- **发起异常退款** (`4013461907`)
  - 原路径: APP合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013461907.md
  - 原更新时间: 2025-01-16 07:08:52

- **退款结果回调通知** (`4012231901`)
  - 原路径: APP合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012231901.md
  - 原更新时间: 2025-02-20 03:14:52

- **申请所有/单个子商户交易账单** (`4012760228`)
  - 原路径: APP合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760228.md
  - 原更新时间: 2025-01-16 07:08:51

- **申请服务商资金账单** (`4012760229`)
  - 原路径: APP合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760229.md
  - 原更新时间: 2025-01-16 07:08:50

- **下载账单** (`4012231933`)
  - 原路径: APP合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012231933.md
  - 原更新时间: 2025-01-16 06:39:27

- **产品介绍** (`4013462080`)
  - 原路径: H5合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462080.md
  - 原更新时间: 2026-05-21 03:35:18

- **开发指引** (`4012166833`)
  - 原路径: H5合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012166833.md
  - 原更新时间: 2025-01-16 06:39:52

- **常见问题** (`4013462145`)
  - 原路径: H5合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462145.md
  - 原更新时间: 2025-01-16 08:45:12

- **H5合单下单** (`4012758208`)
  - 原路径: H5合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012758208.md
  - 原更新时间: 2025-01-16 08:23:19

- **H5调起支付** (`4012166846`)
  - 原路径: H5合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012166846.md
  - 原更新时间: 2025-01-16 06:38:59

- **查询合单订单** (`4013462099`)
  - 原路径: H5合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462099.md
  - 原更新时间: 2025-01-17 07:39:30

- **关闭合单订单** (`4013462102`)
  - 原路径: H5合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462102.md
  - 原更新时间: 2025-01-16 08:23:11

- **合单订单支付成功回调通知** (`4013462105`)
  - 原路径: H5合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462105.md
  - 原更新时间: 2025-01-16 06:39:18

- **申请退款** (`4013462113`)
  - 原路径: H5合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462113.md
  - 原更新时间: 2025-01-16 07:08:56

- **查询单笔退款（按商户退款单号）** (`4013462116`)
  - 原路径: H5合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462116.md
  - 原更新时间: 2025-01-16 07:08:57

- **发起异常退款** (`4013462123`)
  - 原路径: H5合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462123.md
  - 原更新时间: 2025-01-16 07:08:52

- **退款结果通知** (`4013462126`)
  - 原路径: H5合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462126.md
  - 原更新时间: 2025-01-16 06:39:13

- **申请所有/单个子商户交易账单** (`4013462129`)
  - 原路径: H5合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462129.md
  - 原更新时间: 2025-01-16 07:08:51

- **申请服务商资金账单** (`4013462134`)
  - 原路径: H5合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462134.md
  - 原更新时间: 2025-01-16 07:08:50

- **下载账单** (`4013462137`)
  - 原路径: H5合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462137.md
  - 原更新时间: 2025-01-16 06:39:09

- **产品介绍** (`4012079333`)
  - 原路径: Native合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012079333.md
  - 原更新时间: 2026-05-21 03:33:32

- **开发指引** (`4012166835`)
  - 原路径: Native合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012166835.md
  - 原更新时间: 2025-06-20 04:11:35

- **常见问题** (`4013462413`)
  - 原路径: Native合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462413.md
  - 原更新时间: 2025-01-16 08:45:12

- **Native合单下单** (`4012758240`)
  - 原路径: Native合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012758240.md
  - 原更新时间: 2025-01-16 08:23:16

- **Native调起支付** (`4012166843`)
  - 原路径: Native合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012166843.md
  - 原更新时间: 2025-03-21 07:39:13

- **查询合单订单** (`4013462240`)
  - 原路径: Native合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462240.md
  - 原更新时间: 2025-01-17 07:39:30

- **关闭合单订单** (`4013462247`)
  - 原路径: Native合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462247.md
  - 原更新时间: 2025-01-16 08:23:11

- **合单订单支付成功回调通知** (`4013462250`)
  - 原路径: Native合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462250.md
  - 原更新时间: 2025-01-16 06:40:25

- **申请退款** (`4013462256`)
  - 原路径: Native合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462256.md
  - 原更新时间: 2025-01-16 07:08:56

- **查询单笔退款（按商户退款单号）** (`4013462260`)
  - 原路径: Native合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462260.md
  - 原更新时间: 2025-01-16 07:08:57

- **发起异常退款** (`4013462286`)
  - 原路径: Native合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462286.md
  - 原更新时间: 2025-01-16 07:08:52

- **退款结果回调通知** (`4013462327`)
  - 原路径: Native合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462327.md
  - 原更新时间: 2025-01-16 06:40:21

- **申请所有/单个子商户交易账单** (`4013462343`)
  - 原路径: Native合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462343.md
  - 原更新时间: 2025-01-16 07:08:51

- **申请服务商资金账单** (`4013462358`)
  - 原路径: Native合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462358.md
  - 原更新时间: 2025-01-16 07:08:50

- **下载账单** (`4013462389`)
  - 原路径: Native合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462389.md
  - 原更新时间: 2025-01-16 06:40:18

- **产品介绍** (`4012079334`)
  - 原路径: 小程序合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012079334.md
  - 原更新时间: 2026-05-21 03:36:27

- **开发指引** (`4012166836`)
  - 原路径: 小程序合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012166836.md
  - 原更新时间: 2025-06-20 04:11:31

- **常见问题** (`4013462619`)
  - 原路径: 小程序合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462619.md
  - 原更新时间: 2025-09-19 01:41:14

- **小程序合单下单** (`4012758246`)
  - 原路径: 小程序合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012758246.md
  - 原更新时间: 2025-01-16 08:23:15

- **小程序调起支付** (`4012166847`)
  - 原路径: 小程序合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012166847.md
  - 原更新时间: 2025-01-16 06:40:11

- **查询合单订单** (`4013462520`)
  - 原路径: 小程序合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462520.md
  - 原更新时间: 2025-01-17 07:39:30

- **关闭合单订单** (`4013462566`)
  - 原路径: 小程序合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462566.md
  - 原更新时间: 2025-01-16 08:23:11

- **合单订单支付成功回调通知** (`4013462574`)
  - 原路径: 小程序合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462574.md
  - 原更新时间: 2025-01-16 06:40:08

- **申请退款** (`4013462579`)
  - 原路径: 小程序合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462579.md
  - 原更新时间: 2025-01-16 07:08:56

- **查询单笔退款（按商户退款单号）** (`4013462581`)
  - 原路径: 小程序合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462581.md
  - 原更新时间: 2025-01-16 07:08:57

- **发起异常退款** (`4013462582`)
  - 原路径: 小程序合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462582.md
  - 原更新时间: 2025-01-16 07:08:52

- **退款结果回调通知** (`4013462586`)
  - 原路径: 小程序合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462586.md
  - 原更新时间: 2025-09-16 08:50:44

- **申请所有/单个子商户交易账单** (`4013462604`)
  - 原路径: 小程序合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462604.md
  - 原更新时间: 2025-01-16 07:08:51

- **申请服务商资金账单** (`4013462607`)
  - 原路径: 小程序合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462607.md
  - 原更新时间: 2025-01-16 07:08:50

- **下载账单** (`4013462614`)
  - 原路径: 小程序合单支付 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013462614.md
  - 原更新时间: 2025-01-16 06:39:58

- **产品介绍** (`4016824698`)
  - 原路径: 医保支付（服务商模式）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016824698.md
  - 原更新时间: 2026-03-02 07:15:14

- **开发接入准备** (`4016824704`)
  - 原路径: 医保支付（服务商模式）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016824704.md
  - 原更新时间: 2026-05-20 06:20:32

- **开发指引** (`4017149893`)
  - 原路径: 医保支付（服务商模式）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017149893.md
  - 原更新时间: 2026-05-20 07:14:26

- **医保自费混合收款下单** (`4012503131`)
  - 原路径: 医保支付（服务商模式） > API列表 > 医保自费混合订单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012503131.md
  - 原更新时间: 2025-12-05 03:00:28

- **使用医保自费混合订单号查看下单结果** (`4012503155`)
  - 原路径: 医保支付（服务商模式） > API列表 > 医保自费混合订单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012503155.md
  - 原更新时间: 2025-12-05 02:58:26

- **使用服务商订单号查看下单结果** (`4012503286`)
  - 原路径: 医保支付（服务商模式） > API列表 > 医保自费混合订单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012503286.md
  - 原更新时间: 2026-04-17 08:57:34

- **小程序调起医保自费混合支付** (`4012166993`)
  - 原路径: 医保支付（服务商模式） > API列表 > 医保自费混合订单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012166993.md
  - 原更新时间: 2024-10-25 06:46:01

- **JSAPI调起医保自费混合支付** (`4012809233`)
  - 原路径: 医保支付（服务商模式） > API列表 > 医保自费混合订单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012809233.md
  - 原更新时间: 2024-10-25 06:46:01

- **医保混合收款成功通知** (`4012165722`)
  - 原路径: 医保支付（服务商模式） > API列表 > 医保自费混合订单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012165722.md
  - 原更新时间: 2024-10-25 06:46:01

- **医保退款通知** (`4012166534`)
  - 原路径: 医保支付（服务商模式） > API列表 > 医保退款
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012166534.md
  - 原更新时间: 2025-12-05 02:58:45

- **报错排查指引** (`4020401184`)
  - 原路径: 医保支付（服务商模式） > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4020401184.md
  - 原更新时间: 2026-05-14 09:13:41

- **业务&接口规则类问题** (`4017415847`)
  - 原路径: 医保支付（服务商模式） > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017415847.md
  - 原更新时间: 2026-05-14 09:14:42

- **申请医保支付权限** (`4016971494`)
  - 原路径: 医保支付（服务商模式） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016971494.md
  - 原更新时间: 2026-05-20 06:32:45

- **接入医保亲情付指引** (`4016970670`)
  - 原路径: 医保支付（服务商模式） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016970670.md
  - 原更新时间: 2026-05-20 06:23:29

- **产品介绍** (`4018300086`)
  - 原路径: 医保支付（间连模式）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018300086.md
  - 原更新时间: 2026-05-14 08:55:13

- **开发接入准备** (`4018300089`)
  - 原路径: 医保支付（间连模式）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018300089.md
  - 原更新时间: 2026-05-20 07:23:17

- **开发指引** (`4016824703`)
  - 原路径: 医保支付（间连模式）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016824703.md
  - 原更新时间: 2026-05-20 07:25:15

- **医保自费混合收款下单** (`4018300080`)
  - 原路径: 医保支付（间连模式） > API列表 > 医保自费混合订单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018300080.md
  - 原更新时间: 2026-03-02 06:55:05

- **使用医保自费混合订单号查看下单结果** (`4018300081`)
  - 原路径: 医保支付（间连模式） > API列表 > 医保自费混合订单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018300081.md
  - 原更新时间: 2026-03-02 06:55:05

- **使用从业机构订单号查看下单结果** (`4018300082`)
  - 原路径: 医保支付（间连模式） > API列表 > 医保自费混合订单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018300082.md
  - 原更新时间: 2026-03-02 06:55:05

- **小程序调起医保自费混合支付** (`4018300079`)
  - 原路径: 医保支付（间连模式） > API列表 > 医保自费混合订单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018300079.md
  - 原更新时间: 2026-03-02 06:55:05

- **JSAPI调起医保自费混合支付** (`4018300083`)
  - 原路径: 医保支付（间连模式） > API列表 > 医保自费混合订单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018300083.md
  - 原更新时间: 2026-03-02 06:55:05

- **医保混合收款成功通知** (`4018303231`)
  - 原路径: 医保支付（间连模式） > API列表 > 医保自费混合订单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018303231.md
  - 原更新时间: 2026-03-02 06:56:16

- **医保退款通知** (`4018300085`)
  - 原路径: 医保支付（间连模式） > API列表 > 医保退款
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018300085.md
  - 原更新时间: 2026-03-02 02:58:27

- **报错排查指引** (`4020401288`)
  - 原路径: 医保支付（间连模式） > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4020401288.md
  - 原更新时间: 2026-05-14 09:14:51

- **业务&接口规则类问题** (`4018300095`)
  - 原路径: 医保支付（间连模式） > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018300095.md
  - 原更新时间: 2026-05-14 09:21:12

- **申请医保支付权限** (`4016824701`)
  - 原路径: 医保支付（间连模式） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016824701.md
  - 原更新时间: 2026-05-20 06:43:31

- **接入医保亲情付指引** (`4018300091`)
  - 原路径: 医保支付（间连模式） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018300091.md
  - 原更新时间: 2026-05-20 06:44:13

- **产品介绍** (`4013080622`)
  - 原路径: 订单退款
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080622.md
  - 原更新时间: 2026-05-21 03:44:04

- **开发接入准备** (`4013080630`)
  - 原路径: 订单退款
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080630.md
  - 原更新时间: 2026-05-19 08:38:56

- **开发指引** (`4013080623`)
  - 原路径: 订单退款
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080623.md
  - 原更新时间: 2025-06-20 04:11:27

- **业务示例代码** (`4015217325`)
  - 原路径: 订单退款
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015217325.md
  - 原更新时间: 2025-09-03 03:02:00

- **常见问题** (`4013080629`)
  - 原路径: 订单退款
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080629.md
  - 原更新时间: 2026-05-09 08:56:56

- **申请退款** (`4013080625`)
  - 原路径: 订单退款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080625.md
  - 原更新时间: 2025-01-16 07:08:56

- **查询单笔退款（通过商户退款单号）** (`4013080626`)
  - 原路径: 订单退款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080626.md
  - 原更新时间: 2025-01-16 07:08:57

- **发起异常退款** (`4013080627`)
  - 原路径: 订单退款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080627.md
  - 原更新时间: 2025-01-16 07:08:52

- **退款结果通知** (`4013080628`)
  - 原路径: 订单退款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080628.md
  - 原更新时间: 2024-12-30 07:47:39

- **退款操作指引** (`4013080632`)
  - 原路径: 订单退款 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080632.md
  - 原更新时间: 2024-11-26 08:21:24

- **微信支付退款最佳实践** (`4014960215`)
  - 原路径: 订单退款 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4014960215.md
  - 原更新时间: 2025-09-25 02:50:28

- **产品介绍** (`4013080592`)
  - 原路径: 下载账单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080592.md
  - 原更新时间: 2025-04-24 06:38:30

- **开发指引** (`4013080593`)
  - 原路径: 下载账单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080593.md
  - 原更新时间: 2024-11-25 08:53:40

- **业务示例代码** (`4015988147`)
  - 原路径: 下载账单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015988147.md
  - 原更新时间: 2025-12-03 04:00:07

- **常见问题** (`4013080602`)
  - 原路径: 下载账单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080602.md
  - 原更新时间: 2026-05-09 08:57:11

- **申请所有/单个特约商户交易账单** (`4013080595`)
  - 原路径: 下载账单 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080595.md
  - 原更新时间: 2025-01-16 07:08:51

- **申请服务商资金账单** (`4013080596`)
  - 原路径: 下载账单 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080596.md
  - 原更新时间: 2025-01-16 07:08:50

- **下载账单** (`4013080597`)
  - 原路径: 下载账单 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080597.md
  - 原更新时间: 2024-12-23 03:48:08

- **交易账单详细说明** (`4013080599`)
  - 原路径: 下载账单 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080599.md
  - 原更新时间: 2026-01-16 03:53:05

- **资金账单详细说明** (`4013080600`)
  - 原路径: 下载账单 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080600.md
  - 原更新时间: 2024-11-26 08:21:16

- **平台下载账单操作指引** (`4013080601`)
  - 原路径: 下载账单 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080601.md
  - 原更新时间: 2024-11-26 08:21:11

- **产品介绍** (`4012072582`)
  - 原路径: 分账
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072582.md
  - 原更新时间: 2025-05-13 02:17:34

- **开发接入准备** (`4012072589`)
  - 原路径: 分账
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072589.md
  - 原更新时间: 2026-05-19 09:30:27

- **开发指引** (`4012072601`)
  - 原路径: 分账
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072601.md
  - 原更新时间: 2025-08-13 10:15:05

- **常见问题** (`4014547107`)
  - 原路径: 分账
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4014547107.md
  - 原更新时间: 2026-04-28 06:56:30

- **请求分账** (`4012690683`)
  - 原路径: 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012690683.md
  - 原更新时间: 2025-09-29 01:58:27

- **查询分账结果** (`4012466850`)
  - 原路径: 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012466850.md
  - 原更新时间: 2025-09-29 03:51:23

- **请求分账回退** (`4012466854`)
  - 原路径: 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012466854.md
  - 原更新时间: 2025-09-29 03:50:46

- **查询分账回退结果** (`4012466858`)
  - 原路径: 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012466858.md
  - 原更新时间: 2025-09-29 03:49:39

- **解冻剩余资金** (`4012466860`)
  - 原路径: 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012466860.md
  - 原更新时间: 2025-09-29 03:49:07

- **查询剩余待分金额** (`4012457927`)
  - 原路径: 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012457927.md
  - 原更新时间: 2025-09-29 03:48:45

- **查询最大分账比例** (`4012466864`)
  - 原路径: 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012466864.md
  - 原更新时间: 2025-09-29 03:48:29

- **添加分账接收方** (`4012690944`)
  - 原路径: 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012690944.md
  - 原更新时间: 2025-09-29 03:48:04

- **删除分账接收方** (`4012466868`)
  - 原路径: 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012466868.md
  - 原更新时间: 2025-09-29 03:47:32

- **分账动账通知** (`4012075216`)
  - 原路径: 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012075216.md
  - 原更新时间: 2025-02-19 03:56:03

- **申请分账账单** (`4012761140`)
  - 原路径: 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012761140.md
  - 原更新时间: 2025-09-29 03:47:03

- **下载账单** (`4012075366`)
  - 原路径: 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012075366.md
  - 原更新时间: 2024-10-30 06:42:53

- **分账失败处理指引** (`4015504885`)
  - 原路径: 分账 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015504885.md
  - 原更新时间: 2025-07-04 03:08:11

- **产品介绍** (`4012586132`)
  - 原路径: 微信支付分
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586132.md
  - 原更新时间: 2026-05-26 09:26:57

- **开发接入准备** (`4012586133`)
  - 原路径: 微信支付分
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586133.md
  - 原更新时间: 2026-05-19 08:42:51

- **开发指引** (`4012586134`)
  - 原路径: 微信支付分
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586134.md
  - 原更新时间: 2025-02-13 11:38:19

- **常见问题** (`4012586139`)
  - 原路径: 微信支付分
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586139.md
  - 原更新时间: 2026-05-09 08:57:42

- **创建支付分订单** (`4013138534`)
  - 原路径: 微信支付分 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013138534.md
  - 原更新时间: 2024-12-06 08:29:26

- **查询支付分订单** (`4013138559`)
  - 原路径: 微信支付分 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013138559.md
  - 原更新时间: 2024-12-06 08:29:26

- **取消支付分订单** (`4013138589`)
  - 原路径: 微信支付分 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013138589.md
  - 原更新时间: 2024-12-06 08:29:26

- **确认订单回调通知** (`4012586137`)
  - 原路径: 微信支付分 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586137.md
  - 原更新时间: 2024-12-06 08:29:26

- **完结支付分订单** (`4013138598`)
  - 原路径: 微信支付分 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013138598.md
  - 原更新时间: 2024-12-06 08:29:26

- **修改支付分订单金额** (`4013138819`)
  - 原路径: 微信支付分 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013138819.md
  - 原更新时间: 2024-12-06 08:29:26

- **同步支付分订单状态** (`4013138975`)
  - 原路径: 微信支付分 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013138975.md
  - 原更新时间: 2024-12-06 08:29:39

- **支付成功回调通知** (`4012586136`)
  - 原路径: 微信支付分 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586136.md
  - 原更新时间: 2024-12-06 08:29:26

- **申请退款** (`4013138987`)
  - 原路径: 微信支付分 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013138987.md
  - 原更新时间: 2024-12-06 08:29:26

- **查询退款** (`4013139077`)
  - 原路径: 微信支付分 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013139077.md
  - 原更新时间: 2024-12-06 08:29:26

- **退款结果通知** (`4012586138`)
  - 原路径: 微信支付分 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586138.md
  - 原更新时间: 2024-12-06 08:29:26

- **JSAPI调起支付分确认订单页** (`4012607505`)
  - 原路径: 微信支付分 > API列表 > 拉起支付分小程序确认订单页
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012607505.md
  - 原更新时间: 2024-12-05 07:33:34

- **Android** (`4012607507`)
  - 原路径: 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > APP调起支付分确认订单页
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012607507.md
  - 原更新时间: 2024-12-05 07:31:51

- **iOS** (`4012607508`)
  - 原路径: 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > APP调起支付分确认订单页
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012607508.md
  - 原更新时间: 2024-12-05 07:32:18

- **鸿蒙** (`4015271745`)
  - 原路径: 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > APP调起支付分确认订单页
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015271745.md
  - 原更新时间: 2025-06-18 06:57:03

- **wx.openBusinessView** (`4012607510`)
  - 原路径: 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > 小程序调起支付分确认订单页
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012607510.md
  - 原更新时间: 2024-12-05 07:32:49

- **wx.navigateToMiniProgram（停止新增）** (`4012607511`)
  - 原路径: 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > 小程序调起支付分确认订单页
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012607511.md
  - 原更新时间: 2024-12-05 07:33:11

- **JSAPI调起支付分订单详情页** (`4012607518`)
  - 原路径: 微信支付分 > API列表 > 拉起支付分小程序订单详情页
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012607518.md
  - 原更新时间: 2024-12-05 07:36:11

- **Android** (`4012607513`)
  - 原路径: 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > APP调起支付分订单详情页
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012607513.md
  - 原更新时间: 2024-12-05 07:34:23

- **iOS** (`4012607514`)
  - 原路径: 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > APP调起支付分订单详情页
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012607514.md
  - 原更新时间: 2024-12-05 07:34:53

- **鸿蒙** (`4015271776`)
  - 原路径: 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > APP调起支付分订单详情页
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015271776.md
  - 原更新时间: 2025-06-18 06:57:00

- **wx.openBusinessView** (`4012607516`)
  - 原路径: 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > 小程序调起支付分订单详情页
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012607516.md
  - 原更新时间: 2024-12-05 07:35:16

- **wx.navigateToMiniProgram（停止新增）** (`4012607517`)
  - 原路径: 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > 小程序调起支付分订单详情页
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012607517.md
  - 原更新时间: 2024-12-05 07:35:36

- **支付分合作品牌线上应用规范** (`4012586152`)
  - 原路径: 微信支付分 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586152.md
  - 原更新时间: 2025-03-20 07:09:22

- **支付分权限申请邮件模板** (`4012586142`)
  - 原路径: 微信支付分 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586142.md
  - 原更新时间: 2024-12-09 02:47:16

- **测试微信号配置指引** (`4012586141`)
  - 原路径: 微信支付分 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586141.md
  - 原更新时间: 2024-12-09 10:14:05

- **服务ID新增绑定邮件流程** (`4012624851`)
  - 原路径: 微信支付分 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012624851.md
  - 原更新时间: 2024-12-09 10:13:56

- **总览** (`4013163663`)
  - 原路径: 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013163663.md
  - 原更新时间: 2024-12-09 09:41:21

- **二轮电动车充电桩** (`4012586150`)
  - 原路径: 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586150.md
  - 原更新时间: 2024-12-09 09:41:03

- **充电宝** (`4012586148`)
  - 原路径: 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586148.md
  - 原更新时间: 2024-12-09 09:40:59

- **共享单车** (`4012586145`)
  - 原路径: 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586145.md
  - 原更新时间: 2024-12-09 09:40:55

- **快递行业** (`4012586144`)
  - 原路径: 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586144.md
  - 原更新时间: 2024-12-09 09:40:52

- **智慧零售(无人设备)** (`4012586146`)
  - 原路径: 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586146.md
  - 原更新时间: 2024-12-09 09:40:50

- **汽车充电桩** (`4012586149`)
  - 原路径: 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586149.md
  - 原更新时间: 2024-12-09 09:40:46

- **汽车租赁** (`4012586151`)
  - 原路径: 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586151.md
  - 原更新时间: 2024-12-09 09:40:42

- **酒店行业** (`4012586147`)
  - 原路径: 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012586147.md
  - 原更新时间: 2024-12-09 10:14:02

- **产品介绍** (`4012085549`)
  - 原路径: 微信支付分停车服务
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085549.md
  - 原更新时间: 2025-03-21 09:21:49

- **开发接入准备** (`4012085632`)
  - 原路径: 微信支付分停车服务
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085632.md
  - 原更新时间: 2026-05-19 08:43:09

- **开发指引** (`4012085711`)
  - 原路径: 微信支付分停车服务
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085711.md
  - 原更新时间: 2025-03-21 07:38:07

- **常见问题** (`4016183529`)
  - 原路径: 微信支付分停车服务
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016183529.md
  - 原更新时间: 2025-12-12 02:16:53

- **创建停车入场** (`4012533994`)
  - 原路径: 微信支付分停车服务 > API列表 > 停车入场
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012533994.md
  - 原更新时间: 2025-02-21 08:25:44

- **停车入场状态变更通知** (`4012085798`)
  - 原路径: 微信支付分停车服务 > API列表 > 停车入场
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085798.md
  - 原更新时间: 2025-02-19 07:23:03

- **查询车牌服务开通信息** (`4012534183`)
  - 原路径: 微信支付分停车服务 > API列表 > 服务
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012534183.md
  - 原更新时间: 2025-02-21 08:25:08

- **小程序调起微信支付分停车服务开通页** (`4012085969`)
  - 原路径: 微信支付分停车服务 > API列表 > 服务
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085969.md
  - 原更新时间: 2024-10-31 07:43:33

- **H5调起微信支付分停车服务开通页** (`4012085997`)
  - 原路径: 微信支付分停车服务 > API列表 > 服务
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012085997.md
  - 原更新时间: 2024-10-31 07:46:05

- **App拉起微信支付分停车服务开通页** (`4012086028`)
  - 原路径: 微信支付分停车服务 > API列表 > 服务
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012086028.md
  - 原更新时间: 2024-10-22 09:54:33

- **查询订单** (`4012534441`)
  - 原路径: 微信支付分停车服务 > API列表 > 扣费受理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012534441.md
  - 原更新时间: 2025-02-21 08:26:35

- **扣费受理** (`4012534427`)
  - 原路径: 微信支付分停车服务 > API列表 > 扣费受理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012534427.md
  - 原更新时间: 2025-03-11 03:03:56

- **订单支付结果通知** (`4012086059`)
  - 原路径: 微信支付分停车服务 > API列表 > 扣费受理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012086059.md
  - 原更新时间: 2025-02-19 07:20:38

- **微信垫资还款** (`4012086207`)
  - 原路径: 微信支付分停车服务 > API列表 > 还款
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012086207.md
  - 原更新时间: 2024-11-04 02:10:45

- **退款申请** (`4012760545`)
  - 原路径: 微信支付分停车服务 > API列表 > 退款
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760545.md
  - 原更新时间: 2025-04-07 01:50:02

- **退款结果通知** (`4012086319`)
  - 原路径: 微信支付分停车服务 > API列表 > 退款
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012086319.md
  - 原更新时间: 2025-02-20 03:14:52

- **查询单笔退款（通过商户退款单号）** (`4012760554`)
  - 原路径: 微信支付分停车服务 > API列表 > 退款
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760554.md
  - 原更新时间: 2025-04-07 01:49:56

- **现金红包（V2）** (`4012851209`)
  - 原路径: 现金红包（V2）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012851209.md
  - 原更新时间: 2025-04-25 07:53:50

- **产品介绍** (`4012087800`)
  - 原路径: 代金券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012087800.md
  - 原更新时间: 2025-10-14 07:18:06

- **开发接入准备** (`4012087801`)
  - 原路径: 代金券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012087801.md
  - 原更新时间: 2026-05-19 08:44:06

- **开发指引** (`4012087802`)
  - 原路径: 代金券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012087802.md
  - 原更新时间: 2025-08-13 10:21:13

- **常见问题** (`4015880931`)
  - 原路径: 代金券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015880931.md
  - 原更新时间: 2025-12-19 02:28:02

- **核销事件回调通知** (`4012285807`)
  - 原路径: 代金券 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012285807.md
  - 原更新时间: 2025-02-20 07:10:47

- **图片上传（营销专用）** (`4012759802`)
  - 原路径: 代金券 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012759802.md
  - 原更新时间: 2024-11-18 09:26:00

- **创建代金券批次** (`4012534537`)
  - 原路径: 代金券 > API列表 > 批次
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012534537.md
  - 原更新时间: 2024-11-18 09:25:53

- **激活代金券批次** (`4012460237`)
  - 原路径: 代金券 > API列表 > 批次
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012460237.md
  - 原更新时间: 2024-11-18 09:26:00

- **暂停代金券批次** (`4012460340`)
  - 原路径: 代金券 > API列表 > 批次
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012460340.md
  - 原更新时间: 2024-11-18 09:26:00

- **重启代金券批次** (`4012460448`)
  - 原路径: 代金券 > API列表 > 批次
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012460448.md
  - 原更新时间: 2024-11-18 09:25:43

- **条件查询批次列表** (`4012460518`)
  - 原路径: 代金券 > API列表 > 批次
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012460518.md
  - 原更新时间: 2025-03-25 08:44:52

- **查询批次详情** (`4012460606`)
  - 原路径: 代金券 > API列表 > 批次
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012460606.md
  - 原更新时间: 2025-03-25 08:44:50

- **查询代金券可用商户** (`4012463409`)
  - 原路径: 代金券 > API列表 > 批次
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012463409.md
  - 原更新时间: 2024-11-18 09:25:45

- **查询代金券可用单品** (`4012463475`)
  - 原路径: 代金券 > API列表 > 批次
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012463475.md
  - 原更新时间: 2024-11-18 09:25:55

- **下载批次退款明细** (`4012463548`)
  - 原路径: 代金券 > API列表 > 批次
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012463548.md
  - 原更新时间: 2024-11-18 09:25:43

- **下载批次核销明细** (`4012463698`)
  - 原路径: 代金券 > API列表 > 批次
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012463698.md
  - 原更新时间: 2024-11-18 09:25:53

- **根据商户号查用户的券** (`4012494237`)
  - 原路径: 代金券 > API列表 > 券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012494237.md
  - 原更新时间: 2024-11-18 09:25:43

- **发放指定批次的代金券** (`4012463807`)
  - 原路径: 代金券 > API列表 > 券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012463807.md
  - 原更新时间: 2024-11-18 09:25:41

- **查询代金券详情** (`4012492796`)
  - 原路径: 代金券 > API列表 > 券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012492796.md
  - 原更新时间: 2024-11-18 09:26:04

- **查询代金券消息通知地址** (`4012464155`)
  - 原路径: 代金券 > API列表 > 消息通知地址
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012464155.md
  - 原更新时间: 2024-11-18 09:25:49

- **设置代金券消息通知地址** (`4012464176`)
  - 原路径: 代金券 > API列表 > 消息通知地址
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012464176.md
  - 原更新时间: 2024-11-18 09:25:40

- **产品介绍** (`4012071996`)
  - 原路径: 委托营销
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012071996.md
  - 原更新时间: 2024-07-23 08:00:45

- **开发接入准备** (`4012071997`)
  - 原路径: 委托营销
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012071997.md
  - 原更新时间: 2026-05-19 08:45:58

- **开发指引** (`4012071998`)
  - 原路径: 委托营销
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012071998.md
  - 原更新时间: 2025-08-13 08:56:31

- **建立合作关系** (`4012381469`)
  - 原路径: 委托营销 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012381469.md
  - 原更新时间: 2024-11-18 09:25:45

- **查询合作关系列表** (`4012381479`)
  - 原路径: 委托营销 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012381479.md
  - 原更新时间: 2024-11-18 09:25:58

- **产品介绍** (`4012072117`)
  - 原路径: 支付有礼
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072117.md
  - 原更新时间: 2025-11-11 11:20:38

- **开发接入准备** (`4012072118`)
  - 原路径: 支付有礼
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072118.md
  - 原更新时间: 2026-05-19 08:46:11

- **开发指引** (`4012072119`)
  - 原路径: 支付有礼
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072119.md
  - 原更新时间: 2025-03-27 08:11:49

- **图片上传（营销专用）** (`4012760270`)
  - 原路径: 支付有礼 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760270.md
  - 原更新时间: 2024-11-18 09:26:00

- **创建全场满额送活动** (`4012492900`)
  - 原路径: 支付有礼 > API列表 > 支付有礼活动
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012492900.md
  - 原更新时间: 2024-11-18 09:25:56

- **获取活动详情接口** (`4012492967`)
  - 原路径: 支付有礼 > API列表 > 支付有礼活动
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012492967.md
  - 原更新时间: 2024-11-18 09:25:58

- **获取活动发券商户号** (`4012466191`)
  - 原路径: 支付有礼 > API列表 > 支付有礼活动
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012466191.md
  - 原更新时间: 2024-11-18 09:25:52

- **获取活动指定商品列表** (`4012466492`)
  - 原路径: 支付有礼 > API列表 > 支付有礼活动
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012466492.md
  - 原更新时间: 2024-11-18 09:25:51

- **终止活动** (`4012466633`)
  - 原路径: 支付有礼 > API列表 > 支付有礼活动
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012466633.md
  - 原更新时间: 2024-11-18 09:25:39

- **新增活动发券商户号** (`4012466735`)
  - 原路径: 支付有礼 > API列表 > 支付有礼活动
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012466735.md
  - 原更新时间: 2024-11-18 09:25:55

- **获取支付有礼活动列表** (`4012493214`)
  - 原路径: 支付有礼 > API列表 > 支付有礼活动
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012493214.md
  - 原更新时间: 2024-11-18 09:25:51

- **删除活动发券商户号** (`4012466827`)
  - 原路径: 支付有礼 > API列表 > 支付有礼活动
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012466827.md
  - 原更新时间: 2024-11-18 09:25:40

- **产品介绍** (`4012072233`)
  - 原路径: 小程序发券插件
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072233.md
  - 原更新时间: 2025-03-21 10:25:07

- **开发接入准备** (`4012072234`)
  - 原路径: 小程序发券插件
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072234.md
  - 原更新时间: 2026-05-19 08:46:25

- **小程序发券插件** (`4012285878`)
  - 原路径: 小程序发券插件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012285878.md
  - 原更新时间: 2025-02-19 03:55:31

- **产品介绍** (`4012075048`)
  - 原路径: H5发券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012075048.md
  - 原更新时间: 2025-03-21 07:41:31

- **开发接入准备** (`4012075086`)
  - 原路径: H5发券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012075086.md
  - 原更新时间: 2026-05-19 08:46:39

- **H5发券** (`4012285900`)
  - 原路径: H5发券 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012285900.md
  - 原更新时间: 2025-03-21 07:39:58

- **产品介绍** (`4012075220`)
  - 原路径: 智慧商圈
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012075220.md
  - 原更新时间: 2025-03-21 07:41:21

- **开发接入准备** (`4012075231`)
  - 原路径: 智慧商圈
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012075231.md
  - 原更新时间: 2026-05-19 08:46:54

- **开发指引** (`4012075386`)
  - 原路径: 智慧商圈
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012075386.md
  - 原更新时间: 2026-05-21 06:45:10

- **常见问题** (`4016111726`)
  - 原路径: 智慧商圈
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016111726.md
  - 原更新时间: 2026-05-19 07:41:47

- **商圈会员积分服务授权结果通知** (`4012076406`)
  - 原路径: 智慧商圈 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076406.md
  - 原更新时间: 2025-02-19 03:56:03

- **商圈会员场内支付结果通知** (`4012076414`)
  - 原路径: 智慧商圈 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076414.md
  - 原更新时间: 2025-02-19 03:56:03

- **商圈会员积分同步** (`4012474133`)
  - 原路径: 智慧商圈 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012474133.md
  - 原更新时间: 2024-11-18 09:25:47

- **商圈会员场内退款结果通知** (`4012076419`)
  - 原路径: 智慧商圈 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076419.md
  - 原更新时间: 2025-02-19 03:56:03

- **商圈会员积分服务授权查询** (`4012474135`)
  - 原路径: 智慧商圈 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012474135.md
  - 原更新时间: 2024-11-18 09:25:40

- **商圈会员待积分状态查询** (`4012474129`)
  - 原路径: 智慧商圈 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012474129.md
  - 原更新时间: 2024-11-28 06:23:32

- **商圈会员停车状态同步** (`4012474127`)
  - 原路径: 智慧商圈 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012474127.md
  - 原更新时间: 2024-11-28 06:23:40

- **产品介绍** (`4012076036`)
  - 原路径: 支付即服务
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076036.md
  - 原更新时间: 2026-05-21 06:53:19

- **开发接入准备** (`4012076037`)
  - 原路径: 支付即服务
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076037.md
  - 原更新时间: 2026-05-19 08:47:09

- **开发指引** (`4012076038`)
  - 原路径: 支付即服务
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076038.md
  - 原更新时间: 2025-08-13 10:09:31

- **常见问题** (`4016913657`)
  - 原路径: 支付即服务
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016913657.md
  - 原更新时间: 2025-12-19 02:14:14

- **服务人员查询** (`4012688558`)
  - 原路径: 支付即服务 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012688558.md
  - 原更新时间: 2025-01-09 03:09:59

- **服务人员注册** (`4012688564`)
  - 原路径: 支付即服务 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012688564.md
  - 原更新时间: 2025-01-09 03:10:21

- **服务人员更新** (`4012688570`)
  - 原路径: 支付即服务 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012688570.md
  - 原更新时间: 2025-01-09 03:10:22

- **服务人员分配** (`4012474145`)
  - 原路径: 支付即服务 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012474145.md
  - 原更新时间: 2024-11-18 09:26:02

- **服务人员称谓申请指引** (`4012076039`)
  - 原路径: 支付即服务 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076039.md
  - 原更新时间: 2024-07-24 02:26:28

- **免开发版本操作指引** (`4012076040`)
  - 原路径: 支付即服务 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076040.md
  - 原更新时间: 2024-11-18 09:25:36

- **个人微信服务人员注册** (`4012076041`)
  - 原路径: 支付即服务 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076041.md
  - 原更新时间: 2024-08-02 07:09:59

- **产品介绍** (`4012072130`)
  - 原路径: 点金计划
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072130.md
  - 原更新时间: 2025-09-04 06:45:36

- **开发接入准备** (`4012072158`)
  - 原路径: 点金计划
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072158.md
  - 原更新时间: 2026-05-19 08:50:32

- **开发指引** (`4012072262`)
  - 原路径: 点金计划
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072262.md
  - 原更新时间: 2025-08-13 10:11:35

- **常见问题** (`4016241762`)
  - 原路径: 点金计划
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016241762.md
  - 原更新时间: 2026-01-23 03:27:42

- **点金计划管理** (`4012473796`)
  - 原路径: 点金计划 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012473796.md
  - 原更新时间: 2024-11-18 09:26:00

- **商家小票管理** (`4012473788`)
  - 原路径: 点金计划 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012473788.md
  - 原更新时间: 2024-11-18 09:25:49

- **同业过滤标签管理** (`4012473784`)
  - 原路径: 点金计划 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012473784.md
  - 原更新时间: 2024-11-18 09:25:53

- **开通广告展示** (`4012473794`)
  - 原路径: 点金计划 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012473794.md
  - 原更新时间: 2024-11-18 09:25:55

- **关闭广告展示** (`4012473781`)
  - 原路径: 点金计划 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012473781.md
  - 原更新时间: 2024-11-18 09:25:47

- **小程序左上角返回键管理** (`4012072514`)
  - 原路径: 点金计划 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072514.md
  - 原更新时间: 2025-02-19 07:20:53

- **产品介绍** (`4016433410`)
  - 原路径: 品牌入驻
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016433410.md
  - 原更新时间: 2026-04-02 14:46:39

- **开发指引** (`4016985537`)
  - 原路径: 品牌入驻
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016985537.md
  - 原更新时间: 2026-03-12 02:43:59

- **常见问题** (`4017027854`)
  - 原路径: 品牌入驻
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017027854.md
  - 原更新时间: 2026-01-04 03:49:11

- **提交入驻申请** (`4016249989`)
  - 原路径: 品牌入驻 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016249989.md
  - 原更新时间: 2025-10-23 06:29:49

- **根据业务申请编号查询申请状态** (`4016257694`)
  - 原路径: 品牌入驻 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016257694.md
  - 原更新时间: 2025-10-23 06:29:49

- **根据申请单ID查询申请状态** (`4016257685`)
  - 原路径: 品牌入驻 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016257685.md
  - 原更新时间: 2025-10-23 06:29:49

- **撤销申请** (`4016257700`)
  - 原路径: 品牌入驻 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016257700.md
  - 原更新时间: 2025-10-23 06:29:49

- **图片上传** (`4016276333`)
  - 原路径: 品牌入驻 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016276333.md
  - 原更新时间: 2025-10-23 06:29:49

- **品牌能力介绍** (`4016433389`)
  - 原路径: 品牌入驻 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016433389.md
  - 原更新时间: 2026-04-02 12:48:03

- **服务商申请品牌授权流程** (`4016026183`)
  - 原路径: 品牌入驻 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016026183.md
  - 原更新时间: 2026-03-11 09:48:51

- **产品介绍** (`4016433952`)
  - 原路径: 商家名片
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016433952.md
  - 原更新时间: 2025-11-12 07:52:53

- **常见问题** (`4017027862`)
  - 原路径: 商家名片
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017027862.md
  - 原更新时间: 2026-01-04 03:49:05

- **商家名片开发指引** (`4016914463`)
  - 原路径: 商家名片 > 开发指引
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016914463.md
  - 原更新时间: 2026-04-02 12:54:41

- **交易连接名片开发指引** (`4016985845`)
  - 原路径: 商家名片 > 开发指引
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016985845.md
  - 原更新时间: 2026-04-02 12:54:02

- **提交商家名片配置申请** (`4016468440`)
  - 原路径: 商家名片 > API列表 > 商家名片配置
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016468440.md
  - 原更新时间: 2025-11-13 06:54:09

- **发布商家名片配置** (`4016475176`)
  - 原路径: 商家名片 > API列表 > 商家名片配置
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016475176.md
  - 原更新时间: 2025-11-13 06:54:27

- **撤销商家名片配置申请** (`4016475172`)
  - 原路径: 商家名片 > API列表 > 商家名片配置
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016475172.md
  - 原更新时间: 2025-11-13 06:54:39

- **查询商家名片配置申请状态** (`4016475174`)
  - 原路径: 商家名片 > API列表 > 商家名片配置
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016475174.md
  - 原更新时间: 2025-11-13 06:54:51

- **获取商家名片预览二维码** (`4016641998`)
  - 原路径: 商家名片 > API列表 > 商家名片配置
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016641998.md
  - 原更新时间: 2025-11-20 07:20:12

- **添加交易连接名片规则申请** (`4016333302`)
  - 原路径: 商家名片 > API列表 > 交易连接名片
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016333302.md
  - 原更新时间: 2025-10-30 09:56:20

- **解除已生效交易连接名片场景** (`4016366804`)
  - 原路径: 商家名片 > API列表 > 交易连接名片
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016366804.md
  - 原更新时间: 2025-10-30 09:56:20

- **撤销交易连接名片配置申请** (`4016366797`)
  - 原路径: 商家名片 > API列表 > 交易连接名片
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016366797.md
  - 原更新时间: 2025-10-30 09:56:20

- **查询已生效交易连接名片规则** (`4016366785`)
  - 原路径: 商家名片 > API列表 > 交易连接名片
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016366785.md
  - 原更新时间: 2025-10-30 09:56:20

- **根据业务申请编号查询添加申请状态** (`4016366816`)
  - 原路径: 商家名片 > API列表 > 交易连接名片
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016366816.md
  - 原更新时间: 2025-10-30 09:56:20

- **商家名片&交易连接名片配置指引** (`4016433970`)
  - 原路径: 商家名片 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016433970.md
  - 原更新时间: 2026-04-02 12:57:33

- **产品介绍** (`4015274636`)
  - 原路径: 商家名片会员
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015274636.md
  - 原更新时间: 2026-02-10 04:06:43

- **开发指引** (`4015274639`)
  - 原路径: 商家名片会员
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015274639.md
  - 原更新时间: 2025-11-25 06:22:02

- **常见问题** (`4017418554`)
  - 原路径: 商家名片会员
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017418554.md
  - 原更新时间: 2026-01-30 07:18:54

- **图片上传** (`4015900513`)
  - 原路径: 商家名片会员 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015900513.md
  - 原更新时间: 2025-11-14 07:32:05

- **创建会员卡模板** (`4015336970`)
  - 原路径: 商家名片会员 > API列表 > 会员卡模板管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015336970.md
  - 原更新时间: 2025-08-01 02:53:26

- **查询会员卡模板列表** (`4015336976`)
  - 原路径: 商家名片会员 > API列表 > 会员卡模板管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015336976.md
  - 原更新时间: 2025-08-01 02:53:26

- **查询会员卡模板信息** (`4015336974`)
  - 原路径: 商家名片会员 > API列表 > 会员卡模板管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015336974.md
  - 原更新时间: 2025-08-01 02:53:26

- **修改会员卡模板信息** (`4015336977`)
  - 原路径: 商家名片会员 > API列表 > 会员卡模板管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015336977.md
  - 原更新时间: 2025-08-01 02:53:26

- **作废会员卡模板** (`4015336972`)
  - 原路径: 商家名片会员 > API列表 > 会员卡模板管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015336972.md
  - 原更新时间: 2025-08-01 02:53:26

- **查询用户会员卡信息** (`4015336980`)
  - 原路径: 商家名片会员 > API列表 > 用户会员卡管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015336980.md
  - 原更新时间: 2025-07-25 03:00:22

- **查询用户在品牌下所有会员卡** (`4015336984`)
  - 原路径: 商家名片会员 > API列表 > 用户会员卡管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015336984.md
  - 原更新时间: 2025-07-25 03:00:22

- **修改用户会员卡信息** (`4015336985`)
  - 原路径: 商家名片会员 > API列表 > 用户会员卡管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015336985.md
  - 原更新时间: 2025-07-25 03:00:22

- **作废用户会员卡** (`4015336983`)
  - 原路径: 商家名片会员 > API列表 > 用户会员卡管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015336983.md
  - 原更新时间: 2025-07-25 03:00:22

- **品牌会员入会组件预授权** (`4015336986`)
  - 原路径: 商家名片会员 > API列表 > 用户开通会员卡
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015336986.md
  - 原更新时间: 2025-11-19 04:10:23

- **小程序拉起品牌会员入会组件** (`4015273633`)
  - 原路径: 商家名片会员 > API列表 > 用户开通会员卡
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015273633.md
  - 原更新时间: 2025-06-24 06:51:53

- **H5拉起品牌会员入会组件** (`4015331476`)
  - 原路径: 商家名片会员 > API列表 > 用户开通会员卡
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015331476.md
  - 原更新时间: 2025-12-23 08:54:29

- **根据OPENID导入用户会员卡** (`4015336981`)
  - 原路径: 商家名片会员 > API列表 > 商家同步会员身份
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015336981.md
  - 原更新时间: 2025-06-22 08:21:27

- **同步会员开通结果** (`4015336979`)
  - 原路径: 商家名片会员 > API列表 > 商家同步会员身份
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015336979.md
  - 原更新时间: 2025-06-22 08:22:08

- **会员卡事件通知** (`4015283692`)
  - 原路径: 商家名片会员 > API列表 > 事件通知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015283692.md
  - 原更新时间: 2025-08-18 10:08:53

- **用户积分兑券事件通知** (`4015878622`)
  - 原路径: 商家名片会员 > API列表 > 事件通知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015878622.md
  - 原更新时间: 2025-08-18 10:08:53

- **用户积分同步事件通知** (`4016096820`)
  - 原路径: 商家名片会员 > API列表 > 事件通知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016096820.md
  - 原更新时间: 2025-09-17 02:57:14

- **创建用户动态信息** (`4015336987`)
  - 原路径: 商家名片会员 > API列表 > 用户动态
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015336987.md
  - 原更新时间: 2025-11-14 07:31:53

- **下单同步用户实时动态** (`4015534755`)
  - 原路径: 商家名片会员 > API列表 > 用户动态
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015534755.md
  - 原更新时间: 2025-11-14 07:31:53

- **同步积分余额** (`4015897280`)
  - 原路径: 商家名片会员 > API列表 > 会员卡积分兑券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015897280.md
  - 原更新时间: 2025-08-20 08:35:05

- **同步积分兑券结果** (`4015897268`)
  - 原路径: 商家名片会员 > API列表 > 会员卡积分兑券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015897268.md
  - 原更新时间: 2025-08-20 08:35:07

- **创建品牌会员发券活动** (`4016464918`)
  - 原路径: 商家名片会员 > API列表 > 品牌会员发券活动
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016464918.md
  - 原更新时间: 2025-11-14 07:20:57

- **查询品牌会员发券活动** (`4016588015`)
  - 原路径: 商家名片会员 > API列表 > 品牌会员发券活动
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016588015.md
  - 原更新时间: 2025-11-14 07:20:57

- **查询品牌会员发券活动列表** (`4016588039`)
  - 原路径: 商家名片会员 > API列表 > 品牌会员发券活动
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016588039.md
  - 原更新时间: 2025-11-14 07:20:57

- **修改品牌会员发券活动信息** (`4016588044`)
  - 原路径: 商家名片会员 > API列表 > 品牌会员发券活动
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016588044.md
  - 原更新时间: 2025-11-14 07:20:57

- **终止品牌会员发券活动** (`4016588028`)
  - 原路径: 商家名片会员 > API列表 > 品牌会员发券活动
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016588028.md
  - 原更新时间: 2025-11-14 07:20:57

- **产品介绍** (`4015782374`)
  - 原路径: 摇一摇有优惠
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015782374.md
  - 原更新时间: 2026-03-11 10:24:02

- **开发接入准备** (`4016060552`)
  - 原路径: 摇一摇有优惠
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016060552.md
  - 原更新时间: 2026-05-21 07:33:55

- **开发指引** (`4016110225`)
  - 原路径: 摇一摇有优惠
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016110225.md
  - 原更新时间: 2025-11-18 03:40:57

- **常见问题** (`4017418618`)
  - 原路径: 摇一摇有优惠
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017418618.md
  - 原更新时间: 2026-01-30 07:18:49

- **创建投放计划** (`4016184554`)
  - 原路径: 摇一摇有优惠 > API列表 > 投放计划
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016184554.md
  - 原更新时间: 2025-12-31 07:07:29

- **分页查询投放计划列表** (`4016184563`)
  - 原路径: 摇一摇有优惠 > API列表 > 投放计划
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016184563.md
  - 原更新时间: 2025-09-27 11:06:05

- **更新投放计划** (`4016184594`)
  - 原路径: 摇一摇有优惠 > API列表 > 投放计划
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016184594.md
  - 原更新时间: 2025-09-27 11:06:26

- **终止投放计划** (`4016184572`)
  - 原路径: 摇一摇有优惠 > API列表 > 投放计划
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016184572.md
  - 原更新时间: 2025-09-27 11:06:52

- **设置投放计划回调地址** (`4016184598`)
  - 原路径: 摇一摇有优惠 > API列表 > 投放计划
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016184598.md
  - 原更新时间: 2025-09-27 11:07:12

- **投放计划状态变更通知** (`4016168699`)
  - 原路径: 摇一摇有优惠 > API列表 > 投放计划
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016168699.md
  - 原更新时间: 2026-03-23 07:44:52

- **投放计划功能介绍** (`4016402231`)
  - 原路径: 摇一摇有优惠 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016402231.md
  - 原更新时间: 2026-04-02 12:36:06

- **投放计划配置指引** (`4016111064`)
  - 原路径: 摇一摇有优惠 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016111064.md
  - 原更新时间: 2026-03-12 02:21:47

- **品牌信息用户端展示规则** (`4016110939`)
  - 原路径: 摇一摇有优惠 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016110939.md
  - 原更新时间: 2025-11-07 03:08:03

- **权限申请** (`4015788437`)
  - 原路径: 摇一摇有优惠 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015788437.md
  - 原更新时间: 2026-04-08 02:20:15

- **运营规则** (`4017294537`)
  - 原路径: 摇一摇有优惠 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017294537.md
  - 原更新时间: 2026-01-20 09:27:40

- **产品介绍** (`4015989376`)
  - 原路径: 商品券（单券）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015989376.md
  - 原更新时间: 2026-05-13 06:51:04

- **开发指引** (`4015788446`)
  - 原路径: 商品券（单券）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015788446.md
  - 原更新时间: 2026-03-23 13:46:14

- **常见问题** (`4016950421`)
  - 原路径: 商品券（单券）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016950421.md
  - 原更新时间: 2025-12-23 02:29:29

- **图片上传** (`4015781275`)
  - 原路径: 商品券（单券） > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781275.md
  - 原更新时间: 2025-11-07 03:39:13

- **创建商品券** (`4015781289`)
  - 原路径: 商品券（单券） > API列表 > 商品券管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781289.md
  - 原更新时间: 2025-12-31 07:51:19

- **修改商品券** (`4015781296`)
  - 原路径: 商品券（单券） > API列表 > 商品券管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781296.md
  - 原更新时间: 2025-08-20 03:37:14

- **查询商品券** (`4015781292`)
  - 原路径: 商品券（单券） > API列表 > 商品券管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781292.md
  - 原更新时间: 2025-08-20 03:37:35

- **失效商品券** (`4015781290`)
  - 原路径: 商品券（单券） > API列表 > 商品券管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781290.md
  - 原更新时间: 2025-08-20 03:38:31

- **添加商品券批次** (`4015781304`)
  - 原路径: 商品券（单券） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781304.md
  - 原更新时间: 2025-10-21 09:04:51

- **查询商品券批次列表** (`4015781553`)
  - 原路径: 商品券（单券） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781553.md
  - 原更新时间: 2025-10-21 09:04:51

- **查询商品券指定批次** (`4015781542`)
  - 原路径: 商品券（单券） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781542.md
  - 原更新时间: 2025-10-21 09:04:51

- **修改商品券批次** (`4015781556`)
  - 原路径: 商品券（单券） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781556.md
  - 原更新时间: 2025-10-21 09:04:51

- **修改商品券批次发放预算** (`4015781561`)
  - 原路径: 商品券（单券） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781561.md
  - 原更新时间: 2025-10-21 09:04:51

- **失效商品券批次** (`4015781532`)
  - 原路径: 商品券（单券） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781532.md
  - 原更新时间: 2025-10-21 09:04:51

- **批次关联门店** (`4015781302`)
  - 原路径: 商品券（单券） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781302.md
  - 原更新时间: 2025-10-21 09:04:51

- **查询批次关联门店列表** (`4015781546`)
  - 原路径: 商品券（单券） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781546.md
  - 原更新时间: 2025-10-21 09:04:51

- **批次取消关联门店** (`4015781537`)
  - 原路径: 商品券（单券） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781537.md
  - 原更新时间: 2025-10-21 09:04:51

- **预上传券Code** (`4015781572`)
  - 原路径: 商品券（单券） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781572.md
  - 原更新时间: 2025-10-21 09:04:51

- **向用户发放商品券** (`4015781605`)
  - 原路径: 商品券（单券） > API列表 > 商品券发放
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781605.md
  - 原更新时间: 2025-11-07 03:28:05

- **确认发放用户商品券** (`4015781575`)
  - 原路径: 商品券（单券） > API列表 > 商品券发放
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781575.md
  - 原更新时间: 2025-11-07 03:28:05

- **向用户预发放商品券** (`4016434365`)
  - 原路径: 商品券（单券） > API列表 > 商品券发放 > 小程序发券组件
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016434365.md
  - 原更新时间: 2025-11-07 03:23:20

- **调起小程序发券组件** (`4016434346`)
  - 原路径: 商品券（单券） > API列表 > 商品券发放 > 小程序发券组件
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016434346.md
  - 原更新时间: 2025-12-23 09:05:06

- **核销用户商品券** (`4015781608`)
  - 原路径: 商品券（单券） > API列表 > 商品券核销
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781608.md
  - 原更新时间: 2025-10-21 09:05:48

- **调起小程序核销组件** (`4016110739`)
  - 原路径: 商品券（单券） > API列表 > 商品券核销
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016110739.md
  - 原更新时间: 2025-11-07 08:58:44

- **查询用户商品券详情** (`4015781582`)
  - 原路径: 商品券（单券） > API列表 > 商品券查询
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781582.md
  - 原更新时间: 2025-10-21 09:05:48

- **指定券状态查询用户商品券列表** (`4015781590`)
  - 原路径: 商品券（单券） > API列表 > 商品券查询
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781590.md
  - 原更新时间: 2025-11-07 03:37:12

- **失效用户商品券** (`4015781578`)
  - 原路径: 商品券（单券） > API列表 > 商品券失效与退券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781578.md
  - 原更新时间: 2025-10-21 09:05:48

- **退券** (`4015781599`)
  - 原路径: 商品券（单券） > API列表 > 商品券失效与退券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781599.md
  - 原更新时间: 2025-11-07 03:37:52

- **获取商品券事件通知地址** (`4015781284`)
  - 原路径: 商品券（单券） > API列表 > 商品券回调通知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781284.md
  - 原更新时间: 2025-08-28 02:02:45

- **设置商品券事件通知地址** (`4015781286`)
  - 原路径: 商品券（单券） > API列表 > 商品券回调通知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015781286.md
  - 原更新时间: 2025-08-28 02:02:45

- **商品券回调通知** (`4015780862`)
  - 原路径: 商品券（单券） > API列表 > 商品券回调通知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015780862.md
  - 原更新时间: 2026-05-08 08:05:27

- **提交图片生成任务** (`4017327735`)
  - 原路径: 商品券（单券） > API列表 > 生成商品券头图
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017327735.md
  - 原更新时间: 2026-01-26 03:27:31

- **查询图片生成任务执行结果** (`4017327739`)
  - 原路径: 商品券（单券） > API列表 > 生成商品券头图
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017327739.md
  - 原更新时间: 2026-01-26 03:27:31

- **图片生成回调通知** (`4017327744`)
  - 原路径: 商品券（单券） > API列表 > 生成商品券头图
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017327744.md
  - 原更新时间: 2026-01-26 03:27:31

- **小程序发券组件开发指引** (`4016434329`)
  - 原路径: 商品券（单券） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016434329.md
  - 原更新时间: 2026-04-02 14:44:14

- **小程序核销组件开发指引** (`4016110741`)
  - 原路径: 商品券（单券） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016110741.md
  - 原更新时间: 2026-04-02 14:44:14

- **品牌、服务商、appid关联关系** (`4018984107`)
  - 原路径: 商品券（单券） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018984107.md
  - 原更新时间: 2026-03-26 06:44:08

- **商品券可核销时间规则说明（coupon_available_period）** (`4016675999`)
  - 原路径: 商品券（单券） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016675999.md
  - 原更新时间: 2025-11-25 03:05:19

- **商品券客户端消息推送页面** (`4019005729`)
  - 原路径: 商品券（单券） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4019005729.md
  - 原更新时间: 2026-03-27 06:57:51

- **商品券结构及修改说明** (`4018984452`)
  - 原路径: 商品券（单券） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018984452.md
  - 原更新时间: 2026-03-27 02:47:11

- **【单券-全场-折扣券】API请求示例** (`4016756270`)
  - 原路径: 商品券（单券） > 附录 > API请求示例-创建商品券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016756270.md
  - 原更新时间: 2025-12-02 13:12:50

- **【单券-全场-满减券】API请求示例** (`4016756271`)
  - 原路径: 商品券（单券） > 附录 > API请求示例-创建商品券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016756271.md
  - 原更新时间: 2025-12-02 13:13:02

- **【单券-单品-折扣券】API请求示例** (`4016756272`)
  - 原路径: 商品券（单券） > 附录 > API请求示例-创建商品券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016756272.md
  - 原更新时间: 2025-12-25 11:53:38

- **【单券-单品-满减券】API请求示例** (`4016756273`)
  - 原路径: 商品券（单券） > 附录 > API请求示例-创建商品券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016756273.md
  - 原更新时间: 2025-12-25 11:54:13

- **【单券-单品-兑换券】API请求示例** (`4016756274`)
  - 原路径: 商品券（单券） > 附录 > API请求示例-创建商品券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016756274.md
  - 原更新时间: 2025-12-25 11:55:51

- **产品介绍** (`4016438787`)
  - 原路径: 商品券（多次优惠）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016438787.md
  - 原更新时间: 2026-05-13 06:51:15

- **开发指引** (`4016438816`)
  - 原路径: 商品券（多次优惠）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016438816.md
  - 原更新时间: 2026-01-29 07:28:12

- **常见问题** (`4016950439`)
  - 原路径: 商品券（多次优惠）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016950439.md
  - 原更新时间: 2025-12-23 02:29:27

- **图片上传** (`4016435731`)
  - 原路径: 商品券（多次优惠） > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016435731.md
  - 原更新时间: 2025-11-07 06:33:45

- **创建商品券** (`4016434630`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016434630.md
  - 原更新时间: 2025-12-31 07:51:33

- **修改商品券** (`4016434633`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016434633.md
  - 原更新时间: 2025-11-07 03:42:29

- **查询商品券** (`4016434632`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016434632.md
  - 原更新时间: 2025-11-07 03:42:29

- **失效商品券** (`4016434631`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016434631.md
  - 原更新时间: 2025-11-07 03:42:29

- **添加商品券批次组** (`4016280622`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016280622.md
  - 原更新时间: 2025-11-20 03:00:43

- **查询商品券批次列表** (`4016434641`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016434641.md
  - 原更新时间: 2025-11-07 03:50:02

- **查询商品券指定批次** (`4016434649`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016434649.md
  - 原更新时间: 2025-11-07 03:50:02

- **修改商品券批次组** (`4016280633`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016280633.md
  - 原更新时间: 2025-11-20 03:00:41

- **修改商品券批次组发放预算** (`4016280642`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016280642.md
  - 原更新时间: 2025-11-20 03:00:40

- **批次组批量关联门店** (`4016280620`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016280620.md
  - 原更新时间: 2025-11-20 03:00:37

- **批次组批量取消关联门店** (`4016280629`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016280629.md
  - 原更新时间: 2025-11-20 03:00:33

- **查询批次关联门店列表** (`4016434665`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016434665.md
  - 原更新时间: 2025-11-07 03:50:02

- **预上传券Code** (`4016434668`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券批次管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016434668.md
  - 原更新时间: 2025-11-07 03:50:02

- **向用户发放商品券批次组** (`4016280664`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券发放
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016280664.md
  - 原更新时间: 2025-11-20 03:00:32

- **确认发放用户商品券** (`4016435562`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券发放
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016435562.md
  - 原更新时间: 2025-11-07 06:25:22

- **向用户预发放商品券批次组** (`4016280670`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券发放 > 小程序发券组件
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016280670.md
  - 原更新时间: 2025-12-16 08:25:19

- **调起小程序发券组件** (`4016435568`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券发放 > 小程序发券组件
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016435568.md
  - 原更新时间: 2025-12-23 08:54:20

- **核销用户商品券** (`4016435636`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券核销
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016435636.md
  - 原更新时间: 2025-11-07 06:28:01

- **调起小程序核销组件** (`4016435640`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券核销
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016435640.md
  - 原更新时间: 2025-11-07 08:58:05

- **查询用户商品券详情** (`4016435702`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券查询
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016435702.md
  - 原更新时间: 2025-11-07 06:31:39

- **指定券状态查询用户商品券列表** (`4016435703`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券查询
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016435703.md
  - 原更新时间: 2025-11-07 06:31:39

- **失效用户商品券组** (`4016280658`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券失效与退券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016280658.md
  - 原更新时间: 2025-11-20 03:00:30

- **退券** (`4016435674`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券失效与退券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016435674.md
  - 原更新时间: 2025-11-07 06:30:06

- **获取商品券事件通知地址** (`4016435718`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券回调通知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016435718.md
  - 原更新时间: 2025-11-07 06:32:46

- **设置商品券事件通知地址** (`4016435719`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券回调通知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016435719.md
  - 原更新时间: 2025-11-07 06:32:46

- **商品券回调通知** (`4016435717`)
  - 原路径: 商品券（多次优惠） > API列表 > 商品券回调通知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016435717.md
  - 原更新时间: 2026-05-08 08:05:23

- **提交图片生成任务** (`4017327752`)
  - 原路径: 商品券（多次优惠） > API列表 > 生成商品券头图
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017327752.md
  - 原更新时间: 2026-01-26 03:27:42

- **查询图片生成任务执行结果** (`4017327753`)
  - 原路径: 商品券（多次优惠） > API列表 > 生成商品券头图
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017327753.md
  - 原更新时间: 2026-01-26 03:27:42

- **图片生成回调通知** (`4017327759`)
  - 原路径: 商品券（多次优惠） > API列表 > 生成商品券头图
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017327759.md
  - 原更新时间: 2026-01-26 03:27:42

- **小程序发券组件开发指引** (`4016435566`)
  - 原路径: 商品券（多次优惠） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016435566.md
  - 原更新时间: 2026-04-02 14:46:11

- **小程序核销组件开发指引** (`4016435642`)
  - 原路径: 商品券（多次优惠） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016435642.md
  - 原更新时间: 2026-04-02 14:46:11

- **品牌、服务商、appid关联关系** (`4018984192`)
  - 原路径: 商品券（多次优惠） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018984192.md
  - 原更新时间: 2026-03-26 06:44:07

- **商品券可核销时间规则说明（coupon_available_period）** (`4016676012`)
  - 原路径: 商品券（多次优惠） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016676012.md
  - 原更新时间: 2025-11-25 11:47:16

- **商品券客户端消息推送页面** (`4019005741`)
  - 原路径: 商品券（多次优惠） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4019005741.md
  - 原更新时间: 2026-03-27 06:57:49

- **商品券结构及修改说明** (`4018984437`)
  - 原路径: 商品券（多次优惠） > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018984437.md
  - 原更新时间: 2026-03-27 02:47:05

- **【多次优惠-全场-折扣券】API请求示例** (`4016756283`)
  - 原路径: 商品券（多次优惠） > 附录 > API请求示例-创建商品券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016756283.md
  - 原更新时间: 2025-12-04 07:57:31

- **【多次优惠-全场-满减券】API请求示例** (`4016756284`)
  - 原路径: 商品券（多次优惠） > 附录 > API请求示例-创建商品券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016756284.md
  - 原更新时间: 2025-12-04 07:59:00

- **【多次优惠-单品-折扣券】API请求示例** (`4016756285`)
  - 原路径: 商品券（多次优惠） > 附录 > API请求示例-创建商品券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016756285.md
  - 原更新时间: 2025-12-04 08:00:48

- **【多次优惠-单品-满减券】API请求示例** (`4016756286`)
  - 原路径: 商品券（多次优惠） > 附录 > API请求示例-创建商品券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016756286.md
  - 原更新时间: 2025-12-04 08:01:18

- **【多次优惠-单品-兑换券】API请求示例** (`4016756287`)
  - 原路径: 商品券（多次优惠） > 附录 > API请求示例-创建商品券
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016756287.md
  - 原更新时间: 2025-12-04 08:01:50

- **产品介绍** (`4016628074`)
  - 原路径: 品牌门店
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016628074.md
  - 原更新时间: 2025-11-19 02:54:10

- **开发指引** (`4016628135`)
  - 原路径: 品牌门店
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016628135.md
  - 原更新时间: 2025-11-25 10:04:12

- **常见问题** (`4016705104`)
  - 原路径: 品牌门店
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016705104.md
  - 原更新时间: 2025-11-27 04:06:48

- **创建品牌门店** (`4015783183`)
  - 原路径: 品牌门店 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015783183.md
  - 原更新时间: 2025-12-02 11:35:44

- **查询品牌门店** (`4015783153`)
  - 原路径: 品牌门店 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015783153.md
  - 原更新时间: 2025-12-02 11:35:44

- **查询品牌门店列表** (`4016756674`)
  - 原路径: 品牌门店 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016756674.md
  - 原更新时间: 2025-12-16 02:56:33

- **更新品牌门店** (`4015783158`)
  - 原路径: 品牌门店 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015783158.md
  - 原更新时间: 2025-12-02 11:35:44

- **删除品牌门店** (`4015783113`)
  - 原路径: 品牌门店 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015783113.md
  - 原更新时间: 2025-12-02 11:35:44

- **暂停门店营业** (`4016756671`)
  - 原路径: 品牌门店 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016756671.md
  - 原更新时间: 2025-12-16 02:56:33

- **恢复门店营业** (`4016756672`)
  - 原路径: 品牌门店 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016756672.md
  - 原更新时间: 2025-12-16 02:56:33

- **绑定收款商户号** (`4015783177`)
  - 原路径: 品牌门店 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015783177.md
  - 原更新时间: 2025-12-02 11:35:44

- **解绑收款商户号** (`4015783188`)
  - 原路径: 品牌门店 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015783188.md
  - 原更新时间: 2025-12-02 11:35:44

- **品牌经营平台管理品牌门店** (`4016689827`)
  - 原路径: 品牌门店 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016689827.md
  - 原更新时间: 2025-11-25 10:04:14

- **获得品牌已授权且在生效中的产品权限信息** (`4017410365`)
  - 原路径: 品牌服务商授权 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017410365.md
  - 原更新时间: 2026-01-29 09:12:34

- **产品介绍** (`4012072620`)
  - 原路径: 连锁品牌分账
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072620.md
  - 原更新时间: 2024-07-23 08:51:32

- **开发接入准备** (`4012072625`)
  - 原路径: 连锁品牌分账
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072625.md
  - 原更新时间: 2026-05-19 09:30:42

- **开发指引** (`4012072637`)
  - 原路径: 连锁品牌分账
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072637.md
  - 原更新时间: 2025-07-04 06:21:01

- **业务示例代码** (`4015871675`)
  - 原路径: 连锁品牌分账
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015871675.md
  - 原更新时间: 2025-09-01 02:04:01

- **常见问题** (`4015981574`)
  - 原路径: 连锁品牌分账
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015981574.md
  - 原更新时间: 2026-02-06 03:12:47

- **请求分账** (`4012692975`)
  - 原路径: 连锁品牌分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012692975.md
  - 原更新时间: 2025-09-29 03:46:37

- **查询分账结果** (`4012467002`)
  - 原路径: 连锁品牌分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467002.md
  - 原更新时间: 2025-09-29 03:45:52

- **请求分账回退** (`4012467097`)
  - 原路径: 连锁品牌分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467097.md
  - 原更新时间: 2025-09-29 03:43:29

- **查询分账回退结果** (`4012467011`)
  - 原路径: 连锁品牌分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467011.md
  - 原更新时间: 2025-09-29 03:43:57

- **解冻剩余资金** (`4012467016`)
  - 原路径: 连锁品牌分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467016.md
  - 原更新时间: 2025-09-29 03:43:07

- **查询订单剩余待分金额** (`4012467021`)
  - 原路径: 连锁品牌分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467021.md
  - 原更新时间: 2025-09-29 03:42:34

- **查询最大分账比例** (`4012467022`)
  - 原路径: 连锁品牌分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467022.md
  - 原更新时间: 2025-09-29 03:42:11

- **添加分账接收方** (`4012467100`)
  - 原路径: 连锁品牌分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467100.md
  - 原更新时间: 2025-09-29 03:41:51

- **删除分账接收方** (`4012467103`)
  - 原路径: 连锁品牌分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467103.md
  - 原更新时间: 2025-09-29 02:38:34

- **分账动账通知** (`4012075400`)
  - 原路径: 连锁品牌分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012075400.md
  - 原更新时间: 2025-02-19 03:56:03

- **申请分账账单** (`4012715572`)
  - 原路径: 连锁品牌分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012715572.md
  - 原更新时间: 2025-09-29 02:37:48

- **下载账单** (`4012076073`)
  - 原路径: 连锁品牌分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076073.md
  - 原更新时间: 2024-10-30 06:42:53

- **分账失败处理指引** (`4015504918`)
  - 原路径: 连锁品牌分账 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015504918.md
  - 原更新时间: 2025-07-04 03:08:09

- **清关报关（V2）** (`4012851220`)
  - 原路径: 清关报关（V2）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012851220.md
  - 原更新时间: 2025-04-25 07:53:42

- **消费者投诉2.0** (`4012072827`)
  - 原路径: 平台收付通-电商交易解决方案
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072827.md
  - 原更新时间: 2025-08-25 10:00:14

- **开发接入准备** (`4012072844`)
  - 原路径: 消费者投诉2.0
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072844.md
  - 原更新时间: 2026-05-19 09:30:57

- **开发指引** (`4012072858`)
  - 原路径: 消费者投诉2.0
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012072858.md
  - 原更新时间: 2026-03-24 07:11:27

- **业务示例代码** (`4015933338`)
  - 原路径: 消费者投诉2.0
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015933338.md
  - 原更新时间: 2025-09-11 03:01:51

- **常见问题** (`4016111688`)
  - 原路径: 消费者投诉2.0
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016111688.md
  - 原更新时间: 2026-05-19 07:41:24

- **查询投诉单列表** (`4012691285`)
  - 原路径: 消费者投诉2.0 > API列表 > 主动查询投诉信息
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012691285.md
  - 原更新时间: 2025-09-02 02:28:31

- **查询投诉单详情** (`4012691648`)
  - 原路径: 消费者投诉2.0 > API列表 > 主动查询投诉信息
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012691648.md
  - 原更新时间: 2025-08-28 02:43:42

- **查询投诉单协商历史** (`4012691802`)
  - 原路径: 消费者投诉2.0 > API列表 > 主动查询投诉信息
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012691802.md
  - 原更新时间: 2025-08-28 02:43:30

- **投诉通知回调** (`4012076174`)
  - 原路径: 消费者投诉2.0 > API列表 > 实时获取投诉信息
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012076174.md
  - 原更新时间: 2025-02-19 03:56:03

- **创建投诉通知回调地址** (`4012458106`)
  - 原路径: 消费者投诉2.0 > API列表 > 实时获取投诉信息
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012458106.md
  - 原更新时间: 2025-08-28 02:43:28

- **查询投诉通知回调地址** (`4012459065`)
  - 原路径: 消费者投诉2.0 > API列表 > 实时获取投诉信息
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012459065.md
  - 原更新时间: 2025-08-28 02:43:23

- **更新投诉通知回调地址** (`4012459287`)
  - 原路径: 消费者投诉2.0 > API列表 > 实时获取投诉信息
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012459287.md
  - 原更新时间: 2025-08-28 02:43:25

- **删除投诉通知回调地址** (`4012460474`)
  - 原路径: 消费者投诉2.0 > API列表 > 实时获取投诉信息
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012460474.md
  - 原更新时间: 2025-08-28 02:43:21

- **回复用户** (`4012467213`)
  - 原路径: 消费者投诉2.0 > API列表 > 商户处理用户投诉
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467213.md
  - 原更新时间: 2025-09-01 02:27:29

- **反馈处理完成** (`4012467217`)
  - 原路径: 消费者投诉2.0 > API列表 > 商户处理用户投诉
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467217.md
  - 原更新时间: 2025-09-01 02:25:00

- **更新退款审批结果** (`4012467218`)
  - 原路径: 消费者投诉2.0 > API列表 > 商户处理用户投诉
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467218.md
  - 原更新时间: 2025-09-01 02:24:26

- **回复需要即时服务的投诉单** (`4017151726`)
  - 原路径: 消费者投诉2.0 > API列表 > 商户处理用户投诉
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4017151726.md
  - 原更新时间: 2026-01-22 08:02:14

- **图片上传接口** (`4012467222`)
  - 原路径: 消费者投诉2.0 > API列表 > 商户反馈图片
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467222.md
  - 原更新时间: 2025-09-01 02:10:00

- **图片请求接口** (`4012467223`)
  - 原路径: 消费者投诉2.0 > API列表 > 商户反馈图片
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467223.md
  - 原更新时间: 2025-09-02 02:43:19

- **产品介绍** (`4015792553`)
  - 原路径: 微信电子发票
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792553.md
  - 原更新时间: 2025-11-28 08:19:11

- **开发接入准备** (`4015792554`)
  - 原路径: 微信电子发票
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792554.md
  - 原更新时间: 2026-05-20 08:10:24

- **开发指引** (`4015792556`)
  - 原路径: 微信电子发票
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792556.md
  - 原更新时间: 2026-05-21 06:56:01

- **业务示例代码** (`4016078358`)
  - 原路径: 微信电子发票
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016078358.md
  - 原更新时间: 2026-01-22 06:49:38

- **常见问题** (`4016960715`)
  - 原路径: 微信电子发票
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016960715.md
  - 原更新时间: 2026-05-19 07:40:26

- **获取开通服务商电子发票能力邀请链接** (`4015941495`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015941495.md
  - 原更新时间: 2025-12-03 02:09:53

- **获取邀请开通的商户信息** (`4015941524`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015941524.md
  - 原更新时间: 2025-12-03 02:09:53

- **检查子商户开票功能状态** (`4015792561`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792561.md
  - 原更新时间: 2025-12-03 02:09:53

- **创建电子发票卡券模板** (`4015792562`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792562.md
  - 原更新时间: 2025-12-03 02:09:53

- **配置开发选项** (`4015792563`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792563.md
  - 原更新时间: 2025-12-03 02:09:53

- **获取用户抬头填写链接** (`4015770776`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015770776.md
  - 原更新时间: 2025-12-03 02:09:53

- **获取用户填写抬头信息** (`4015784260`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015784260.md
  - 原更新时间: 2025-12-03 02:09:53

- **开具通用行业电子发票** (`4015792574`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792574.md
  - 原更新时间: 2025-12-03 02:09:53

- **开具不动产租赁行业电子发票** (`4015941740`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015941740.md
  - 原更新时间: 2025-12-03 02:09:53

- **开具成品油行业电子发票** (`4016760559`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016760559.md
  - 原更新时间: 2025-12-03 02:09:53

- **冲红电子发票** (`4015792575`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792575.md
  - 原更新时间: 2025-12-03 02:09:53

- **查询电子发票** (`4015792567`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792567.md
  - 原更新时间: 2025-12-03 02:09:53

- **获取发票下载信息** (`4015792576`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792576.md
  - 原更新时间: 2025-12-03 02:09:53

- **下载发票文件** (`4015792569`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792569.md
  - 原更新时间: 2025-12-03 02:09:53

- **上传电子发票文件** (`4015792580`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792580.md
  - 原更新时间: 2025-12-03 02:09:53

- **将电子发票插入微信用户卡包** (`4015792579`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792579.md
  - 原更新时间: 2025-12-03 02:09:53

- **用户发票抬头填写完成通知** (`4015792559`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792559.md
  - 原更新时间: 2025-12-03 02:09:53

- **发票开具成功通知** (`4015792570`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792570.md
  - 原更新时间: 2025-12-03 02:09:53

- **发票插入用户卡包成功通知** (`4015792578`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792578.md
  - 原更新时间: 2025-12-03 02:09:53

- **发票冲红成功通知** (`4015792571`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792571.md
  - 原更新时间: 2025-12-03 02:09:53

- **发票卡券作废通知** (`4015792560`)
  - 原路径: 微信电子发票 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015792560.md
  - 原更新时间: 2025-12-03 02:09:53

- **成品油单位转换公式** (`4016730844`)
  - 原路径: 微信电子发票 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016730844.md
  - 原更新时间: 2025-12-24 06:30:37

- **产品介绍** (`4012062365`)
  - 原路径: 特约商户进件
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012062365.md
  - 原更新时间: 2024-10-16 07:11:49

- **开发接入准备** (`4012062375`)
  - 原路径: 特约商户进件
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012062375.md
  - 原更新时间: 2026-05-19 09:32:37

- **开发指引** (`4012062379`)
  - 原路径: 特约商户进件
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012062379.md
  - 原更新时间: 2025-07-18 10:05:14

- **常见问题** (`4016058480`)
  - 原路径: 特约商户进件
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016058480.md
  - 原更新时间: 2026-01-23 02:51:54

- **提交申请单** (`4012719997`)
  - 原路径: 特约商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012719997.md
  - 原更新时间: 2025-03-26 06:58:27

- **申请单号查询申请状态** (`4012697052`)
  - 原路径: 特约商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012697052.md
  - 原更新时间: 2025-03-24 04:07:15

- **业务申请编号查询申请状态** (`4012697168`)
  - 原路径: 特约商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012697168.md
  - 原更新时间: 2025-03-24 04:07:17

- **修改结算账户** (`4012761102`)
  - 原路径: 特约商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012761102.md
  - 原更新时间: 2025-01-22 01:35:52

- **查询结算账户** (`4012761113`)
  - 原路径: 特约商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012761113.md
  - 原更新时间: 2025-01-21 03:41:29

- **查询结算账户修改申请状态** (`4012761120`)
  - 原路径: 特约商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012761120.md
  - 原更新时间: 2025-01-21 03:41:31

- **文件上传** (`4012760490`)
  - 原路径: 特约商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760490.md
  - 原更新时间: 2026-05-09 07:01:44

- **视频上传** (`4012761084`)
  - 原路径: 特约商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012761084.md
  - 原更新时间: 2024-11-18 09:25:56

- **产品介绍** (`4012064820`)
  - 原路径: 商户开户意愿确认
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012064820.md
  - 原更新时间: 2024-10-24 08:22:24

- **开发接入准备** (`4012064824`)
  - 原路径: 商户开户意愿确认
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012064824.md
  - 原更新时间: 2026-05-20 08:07:52

- **开发指引** (`4012064832`)
  - 原路径: 商户开户意愿确认
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012064832.md
  - 原更新时间: 2025-08-13 10:13:13

- **常见问题** (`4016644196`)
  - 原路径: 商户开户意愿确认
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016644196.md
  - 原更新时间: 2026-01-16 03:48:52

- **提交申请单** (`4012722388`)
  - 原路径: 商户开户意愿确认 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012722388.md
  - 原更新时间: 2025-01-09 03:10:33

- **撤销申请单** (`4012697627`)
  - 原路径: 商户开户意愿确认 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012697627.md
  - 原更新时间: 2024-12-04 02:03:31

- **查询申请单审核结果** (`4012697715`)
  - 原路径: 商户开户意愿确认 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012697715.md
  - 原更新时间: 2024-11-04 07:59:30

- **获取商户开户意愿确认状态** (`4012467549`)
  - 原路径: 商户开户意愿确认 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012467549.md
  - 原更新时间: 2024-10-24 09:20:46

- **图片上传** (`4012760509`)
  - 原路径: 商户开户意愿确认 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760509.md
  - 原更新时间: 2024-11-18 09:25:43

- **产品介绍** (`4012064844`)
  - 原路径: 商户平台处置通知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012064844.md
  - 原更新时间: 2026-03-10 07:23:55

- **开发接入准备** (`4012064851`)
  - 原路径: 商户平台处置通知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012064851.md
  - 原更新时间: 2026-05-19 09:33:15

- **开发指引** (`4012064853`)
  - 原路径: 商户平台处置通知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012064853.md
  - 原更新时间: 2025-03-21 07:44:39

- **业务示例代码** (`4015949382`)
  - 原路径: 商户平台处置通知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015949382.md
  - 原更新时间: 2025-09-03 03:01:42

- **查询商户违规通知回调地址** (`4012471327`)
  - 原路径: 商户平台处置通知 > API列表 > 商户违规通知回调
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012471327.md
  - 原更新时间: 2025-08-28 09:27:26

- **修改商户违规通知回调地址** (`4012471330`)
  - 原路径: 商户平台处置通知 > API列表 > 商户违规通知回调
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012471330.md
  - 原更新时间: 2025-08-28 09:27:19

- **创建商户违规通知回调地址** (`4012471333`)
  - 原路径: 商户平台处置通知 > API列表 > 商户违规通知回调
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012471333.md
  - 原更新时间: 2025-08-28 09:27:12

- **删除商户违规通知回调地址** (`4012471334`)
  - 原路径: 商户平台处置通知 > API列表 > 商户违规通知回调
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012471334.md
  - 原更新时间: 2025-08-28 09:27:05

- **商户平台处置记录回调通知** (`4012079216`)
  - 原路径: 商户平台处置通知 > API列表 > 商户违规通知回调
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012079216.md
  - 原更新时间: 2025-02-19 03:56:03

- **产品介绍** (`4012064898`)
  - 原路径: 不活跃商户身份核实
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012064898.md
  - 原更新时间: 2026-05-25 07:06:33

- **开发接入准备** (`4012064902`)
  - 原路径: 不活跃商户身份核实
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012064902.md
  - 原更新时间: 2026-05-19 09:33:57

- **开发指引** (`4012064909`)
  - 原路径: 不活跃商户身份核实
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012064909.md
  - 原更新时间: 2024-12-02 07:22:56

- **常见问题** (`4012064915`)
  - 原路径: 不活跃商户身份核实
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012064915.md
  - 原更新时间: 2024-07-24 08:05:05

- **发起不活跃商户身份核实** (`4012471357`)
  - 原路径: 不活跃商户身份核实 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012471357.md
  - 原更新时间: 2025-08-08 07:33:04

- **查询不活跃商户身份核实结果** (`4012471359`)
  - 原路径: 不活跃商户身份核实 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012471359.md
  - 原更新时间: 2025-08-08 08:00:48

- **关键概念** (`4012064904`)
  - 原路径: 不活跃商户身份核实 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012064904.md
  - 原更新时间: 2024-10-25 02:37:34

- **产品介绍** (`4012165270`)
  - 原路径: 商户被管控能力及原因查询
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012165270.md
  - 原更新时间: 2025-11-11 06:26:12

- **查询子商户管控情况** (`4012803072`)
  - 原路径: 商户被管控能力及原因查询 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012803072.md
  - 原更新时间: 2025-09-26 09:24:32

- **产品介绍** (`4016022264`)
  - 原路径: 合作伙伴订阅
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016022264.md
  - 原更新时间: 2025-09-17 04:03:07

- **开发指引** (`4016022266`)
  - 原路径: 合作伙伴订阅
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016022266.md
  - 原更新时间: 2025-09-16 03:35:57

- **常见问题** (`4016550707`)
  - 原路径: 合作伙伴订阅
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016550707.md
  - 原更新时间: 2025-11-14 07:33:02

- **产品介绍** (`4012925323`)
  - 原路径: 微信支付公钥
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012925323.md
  - 原更新时间: 2026-05-20 03:21:30

- **常见问题** (`4013038589`)
  - 原路径: 微信支付公钥
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013038589.md
  - 原更新时间: 2025-03-04 07:15:22

- **商户签名验签／加解密测试** (`4015139289`)
  - 原路径: 微信支付公钥 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015139289.md
  - 原更新时间: 2026-04-08 03:50:21

- **回调接口** (`4019605946`)
  - 原路径: 微信支付公钥 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4019605946.md
  - 原更新时间: 2026-04-10 08:15:23

- **如何从平台证书切换成微信支付公钥** (`4012925289`)
  - 原路径: 微信支付公钥 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012925289.md
  - 原更新时间: 2024-12-12 02:59:29

- **如何从微信支付公钥切换成平台证书** (`4015419376`)
  - 原路径: 微信支付公钥 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015419376.md
  - 原更新时间: 2026-03-17 09:45:27

- **产品介绍** (`4012073044`)
  - 原路径: 平台证书
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012073044.md
  - 原更新时间: 2026-05-21 07:25:38

- **常见问题** (`4012073263`)
  - 原路径: 平台证书
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012073263.md
  - 原更新时间: 2024-11-29 09:45:35

- **下载平台证书** (`4012715700`)
  - 原路径: 平台证书 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012715700.md
  - 原更新时间: 2024-10-15 08:45:31

- **平台证书更换操作指引** (`4012073146`)
  - 原路径: 平台证书 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012073146.md
  - 原更新时间: 2024-12-04 06:35:09

- **产品介绍** (`4012086891`)
  - 原路径: 平台收付通-电商交易解决方案
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012086891.md
  - 原更新时间: 2026-02-28 08:04:53

- **开发接入准备** (`4012086921`)
  - 原路径: 平台收付通-电商交易解决方案
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012086921.md
  - 原更新时间: 2026-05-19 09:38:35

- **开发指引** (`4012087137`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户进件
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012087137.md
  - 原更新时间: 2025-09-26 03:22:56

- **常见问题** (`4012525423`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户进件
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012525423.md
  - 原更新时间: 2026-05-26 08:53:06

- **提交申请单** (`4012713017`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012713017.md
  - 原更新时间: 2025-02-28 12:07:34

- **通过业务申请编号查询申请状态** (`4012691376`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012691376.md
  - 原更新时间: 2024-11-28 06:22:29

- **通过申请单ID查询申请状态** (`4012691469`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012691469.md
  - 原更新时间: 2024-11-28 06:22:27

- **修改结算账户** (`4012761138`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012761138.md
  - 原更新时间: 2026-01-14 06:27:19

- **查询结算账户** (`4012761142`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012761142.md
  - 原更新时间: 2026-01-14 06:27:41

- **查询结算账户修改申请状态** (`4012761169`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012761169.md
  - 原更新时间: 2025-01-21 03:41:31

- **文件上传** (`4012760432`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户进件 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760432.md
  - 原更新时间: 2026-05-09 07:02:14

- **产品介绍** (`4018153750`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户注销
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4018153750.md
  - 原更新时间: 2026-02-12 08:25:07

- **商户注销资格校验** (`4016420099`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户注销 > 注销预校验 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016420099.md
  - 原更新时间: 2025-11-05 09:41:04

- **提交注销提现申请** (`4013892756`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户注销 > 注销提现（新流程） > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013892756.md
  - 原更新时间: 2025-03-13 04:54:44

- **商户申请单号查询申请单状态** (`4013892759`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户注销 > 注销提现（新流程） > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013892759.md
  - 原更新时间: 2025-09-26 02:25:46

- **微信支付申请单号查询申请单状态** (`4013892765`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户注销 > 注销提现（新流程） > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013892765.md
  - 原更新时间: 2025-09-26 02:25:56

- **常见问题** (`4015943239`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程）
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015943239.md
  - 原更新时间: 2025-11-07 06:48:10

- **提交注销申请单** (`4012476217`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销申请 > 注销申请单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476217.md
  - 原更新时间: 2025-02-17 10:16:34

- **查询注销单状态** (`4012476223`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销申请 > 注销申请单
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476223.md
  - 原更新时间: 2024-11-05 02:04:20

- **图片上传** (`4012691710`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销申请 > 图片上传
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012691710.md
  - 原更新时间: 2024-11-05 02:05:52

- **提交已注销商户号可用余额提现申请单** (`4012488950`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销后提现 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012488950.md
  - 原更新时间: 2025-01-09 03:10:34

- **商户提现申请单号查询提现申请单状态** (`4012476164`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销后提现 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476164.md
  - 原更新时间: 2024-11-05 02:15:27

- **微信支付提现申请单号查询提现申请单状态** (`4012778400`)
  - 原路径: 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销后提现 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012778400.md
  - 原更新时间: 2024-11-05 02:16:19

- **开发指引** (`4012088031`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012088031.md
  - 原更新时间: 2026-03-11 09:00:14

- **常见问题** (`4012525474`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012525474.md
  - 原更新时间: 2026-05-09 08:54:23

- **APP下单** (`4012714669`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > APP支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012714669.md
  - 原更新时间: 2024-10-24 03:39:28

- **APP调起支付** (`4012090168`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > APP支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012090168.md
  - 原更新时间: 2025-02-20 03:00:52

- **JSAPI下单** (`4012714678`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > JSAPI支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012714678.md
  - 原更新时间: 2024-10-24 03:49:34

- **JSAPI调起支付** (`4012090156`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > JSAPI支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012090156.md
  - 原更新时间: 2025-02-26 07:08:25

- **Native下单** (`4012714902`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > Native支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012714902.md
  - 原更新时间: 2024-10-24 06:18:18

- **Native调起支付** (`4012090180`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > Native支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012090180.md
  - 原更新时间: 2025-03-21 07:41:33

- **小程序下单** (`4012714911`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 小程序支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012714911.md
  - 原更新时间: 2024-10-24 03:49:34

- **小程序调起支付** (`4012090181`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 小程序支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012090181.md
  - 原更新时间: 2025-02-26 07:10:30

- **H5下单** (`4012714759`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > H5支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012714759.md
  - 原更新时间: 2024-10-24 06:27:02

- **H5调起支付** (`4012090177`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > H5支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012090177.md
  - 原更新时间: 2024-12-23 02:14:31

- **微信支付订单号查询订单** (`4012760565`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 公共API
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760565.md
  - 原更新时间: 2025-04-07 01:51:41

- **微信支付商户订单号查询订单** (`4012760568`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 公共API
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760568.md
  - 原更新时间: 2025-04-07 01:51:51

- **关闭订单** (`4012760574`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 公共API
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760574.md
  - 原更新时间: 2025-04-07 01:51:49

- **支付结果通知** (`4012090195`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 公共API
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012090195.md
  - 原更新时间: 2025-04-07 01:52:18

- **开发指引** (`4012089542`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012089542.md
  - 原更新时间: 2025-09-26 03:23:41

- **常见问题** (`4012525491`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012525491.md
  - 原更新时间: 2026-05-09 08:54:07

- **合单下单-JSAPI** (`4012760615`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > JSAPI合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760615.md
  - 原更新时间: 2024-11-14 08:12:09

- **JSAPI调起支付** (`4012090843`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > JSAPI合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012090843.md
  - 原更新时间: 2025-02-19 03:55:15

- **合单下单-APP** (`4012760622`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > APP合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760622.md
  - 原更新时间: 2024-11-14 08:12:11

- **APP调起支付** (`4012090949`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > APP合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012090949.md
  - 原更新时间: 2025-03-28 10:57:37

- **合单下单-H5** (`4012760626`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > H5合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760626.md
  - 原更新时间: 2024-11-14 08:12:10

- **H5调起支付** (`4012091014`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > H5合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012091014.md
  - 原更新时间: 2024-10-28 02:58:30

- **合单下单-NATIVE** (`4012760629`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > Native合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760629.md
  - 原更新时间: 2024-11-14 08:12:12

- **Native调起支付** (`4012091224`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > Native合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012091224.md
  - 原更新时间: 2024-10-28 02:54:47

- **合单下单-小程序** (`4012760633`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 小程序合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760633.md
  - 原更新时间: 2024-11-14 08:12:09

- **小程序调起支付** (`4012091236`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 小程序合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012091236.md
  - 原更新时间: 2025-02-18 11:41:37

- **合单查询订单** (`4012761049`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 公共API
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012761049.md
  - 原更新时间: 2024-10-24 07:08:30

- **合单关闭订单** (`4012761093`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 公共API
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012761093.md
  - 原更新时间: 2024-10-24 07:09:52

- **支付通知** (`4012237246`)
  - 原路径: 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 公共API
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012237246.md
  - 原更新时间: 2024-11-18 09:25:58

- **开发指引** (`4012087888`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012087888.md
  - 原更新时间: 2025-09-26 03:05:59

- **业务示例代码** (`4015870957`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015870957.md
  - 原更新时间: 2025-09-26 03:05:59

- **常见问题** (`4012525463`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012525463.md
  - 原更新时间: 2026-05-21 07:43:02

- **请求分账** (`4012691594`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012691594.md
  - 原更新时间: 2025-09-29 06:45:52

- **查询分账结果** (`4012477734`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012477734.md
  - 原更新时间: 2025-09-29 02:09:30

- **请求分账回退** (`4012477737`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012477737.md
  - 原更新时间: 2025-09-29 02:06:15

- **查询分账回退结果** (`4012477740`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012477740.md
  - 原更新时间: 2025-09-29 02:04:34

- **解冻剩余资金** (`4012477745`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012477745.md
  - 原更新时间: 2025-09-29 02:03:23

- **查询订单剩余待分金额** (`4012477751`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012477751.md
  - 原更新时间: 2025-09-29 02:02:25

- **添加分账接收方** (`4012477758`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012477758.md
  - 原更新时间: 2025-09-29 02:01:53

- **删除分账接收方** (`4012477759`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012477759.md
  - 原更新时间: 2025-09-29 02:00:58

- **分账动账通知** (`4012116672`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012116672.md
  - 原更新时间: 2025-02-19 03:56:03

- **分账失败处理指引** (`4015504955`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > 附录
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015504955.md
  - 原更新时间: 2025-07-04 03:08:08

- **业务示例代码** (`4015593692`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 补差
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015593692.md
  - 原更新时间: 2025-10-24 06:49:13

- **常见问题** (`4015942503`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 补差
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015942503.md
  - 原更新时间: 2026-01-22 06:48:53

- **请求补差** (`4012477631`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 补差 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012477631.md
  - 原更新时间: 2024-11-04 11:30:10

- **请求补差回退** (`4012477636`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 补差 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012477636.md
  - 原更新时间: 2024-11-04 11:30:36

- **取消补差** (`4012477639`)
  - 原路径: 平台收付通-电商交易解决方案 > 补差与分账 > 补差 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012477639.md
  - 原更新时间: 2024-10-24 08:47:04

- **业务示例代码** (`4015217874`)
  - 原路径: 平台收付通-电商交易解决方案 > 交易退款
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015217874.md
  - 原更新时间: 2025-10-15 07:52:29

- **申请退款** (`4012476892`)
  - 原路径: 平台收付通-电商交易解决方案 > 交易退款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476892.md
  - 原更新时间: 2024-11-04 11:33:40

- **查询单笔退款（按微信支付退款单号）** (`4012476908`)
  - 原路径: 平台收付通-电商交易解决方案 > 交易退款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476908.md
  - 原更新时间: 2024-11-04 11:36:44

- **查询单笔退款（按商户退款单号）** (`4012476911`)
  - 原路径: 平台收付通-电商交易解决方案 > 交易退款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476911.md
  - 原更新时间: 2024-11-04 11:36:11

- **退款结果通知** (`4012124635`)
  - 原路径: 平台收付通-电商交易解决方案 > 交易退款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012124635.md
  - 原更新时间: 2024-11-18 09:25:58

- **查询垫付回补结果** (`4012476916`)
  - 原路径: 平台收付通-电商交易解决方案 > 交易退款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476916.md
  - 原更新时间: 2024-11-04 11:40:17

- **垫付退款回补** (`4012476927`)
  - 原路径: 平台收付通-电商交易解决方案 > 交易退款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476927.md
  - 原更新时间: 2024-11-04 11:41:31

- **发起异常退款** (`4015181616`)
  - 原路径: 平台收付通-电商交易解决方案 > 交易退款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015181616.md
  - 原更新时间: 2025-06-06 08:23:46

- **常见问题** (`4016644075`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016644075.md
  - 原更新时间: 2025-11-21 03:07:14

- **查询二级商户账户实时余额** (`4012476690`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476690.md
  - 原更新时间: 2024-11-04 11:47:34

- **查询二级商户账户日终余额** (`4012476693`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476693.md
  - 原更新时间: 2024-11-04 11:47:25

- **查询平台账户实时余额** (`4012476700`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476700.md
  - 原更新时间: 2024-11-04 11:46:09

- **查询平台账户日终余额** (`4012476702`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476702.md
  - 原更新时间: 2024-11-04 11:46:15

- **业务示例代码** (`4019899593`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4019899593.md
  - 原更新时间: 2026-04-23 06:48:35

- **常见问题** (`4014075940`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4014075940.md
  - 原更新时间: 2025-12-19 02:57:09

- **二级商户预约提现** (`4012476652`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476652.md
  - 原更新时间: 2024-12-19 07:33:30

- **二级商户查询预约提现状态（根据商户预约提现单号查询）** (`4012476656`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476656.md
  - 原更新时间: 2024-12-19 07:33:26

- **二级商户查询预约提现状态（根据微信支付预约提现单号查询）** (`4012476665`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476665.md
  - 原更新时间: 2024-12-19 07:33:24

- **平台预约提现** (`4012476670`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476670.md
  - 原更新时间: 2024-12-19 07:33:21

- **平台查询预约提现状态（根据商户预约提现单号查询）** (`4012476672`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476672.md
  - 原更新时间: 2024-12-19 07:33:18

- **平台查询预约提现状态（根据微信支付预约提现单号查询）** (`4012476674`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476674.md
  - 原更新时间: 2024-12-19 07:33:16

- **二级商户按日终余额预约提现** (`4013328143`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013328143.md
  - 原更新时间: 2024-12-19 08:08:05

- **查询二级商户按日终余额预约提现状态** (`4013328163`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013328163.md
  - 原更新时间: 2024-12-19 08:08:05

- **按日下载提现异常文件** (`4012476678`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476678.md
  - 原更新时间: 2024-12-19 07:11:13

- **商户提现状态变更通知** (`4013049135`)
  - 原路径: 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013049135.md
  - 原更新时间: 2025-02-24 09:49:47

- **业务示例代码** (`4016062108`)
  - 原路径: 平台收付通-电商交易解决方案 > 账单下载
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016062108.md
  - 原更新时间: 2025-12-04 01:55:05

- **申请交易账单** (`4012760667`)
  - 原路径: 平台收付通-电商交易解决方案 > 账单下载 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760667.md
  - 原更新时间: 2025-04-07 01:51:03

- **申请资金账单** (`4012760672`)
  - 原路径: 平台收付通-电商交易解决方案 > 账单下载 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760672.md
  - 原更新时间: 2025-04-07 01:50:55

- **申请分账账单** (`4012761131`)
  - 原路径: 平台收付通-电商交易解决方案 > 账单下载 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012761131.md
  - 原更新时间: 2025-01-20 08:06:16

- **下载账单** (`4012124894`)
  - 原路径: 平台收付通-电商交易解决方案 > 账单下载 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012124894.md
  - 原更新时间: 2025-04-16 09:44:14

- **申请二级商户资金账单** (`4012760697`)
  - 原路径: 平台收付通-电商交易解决方案 > 账单下载 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760697.md
  - 原更新时间: 2024-10-23 08:14:36

- **申请单个子商户资金账单** (`4012760249`)
  - 原路径: 平台收付通-电商交易解决方案 > 账单下载 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012760249.md
  - 原更新时间: 2024-10-21 08:45:00

- **下载单个子商户/二级商户资金账单** (`4014314390`)
  - 原路径: 平台收付通-电商交易解决方案 > 账单下载 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4014314390.md
  - 原更新时间: 2025-04-16 03:21:56

- **业务示例代码** (`4015593257`)
  - 原路径: 平台收付通-电商交易解决方案 > 跨境付款
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015593257.md
  - 原更新时间: 2025-09-26 03:22:00

- **查询订单剩余可出境余额** (`4012476109`)
  - 原路径: 平台收付通-电商交易解决方案 > 跨境付款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476109.md
  - 原更新时间: 2024-11-05 02:17:34

- **申请资金出境** (`4012476113`)
  - 原路径: 平台收付通-电商交易解决方案 > 跨境付款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476113.md
  - 原更新时间: 2024-11-05 02:22:26

- **查询出境结果** (`4012476127`)
  - 原路径: 平台收付通-电商交易解决方案 > 跨境付款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476127.md
  - 原更新时间: 2024-11-05 02:23:59

- **获取购付汇账单文件下载链接** (`4012476132`)
  - 原路径: 平台收付通-电商交易解决方案 > 跨境付款 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012476132.md
  - 原更新时间: 2024-11-05 02:32:27

- **APIv3概述** (`4012081673`)
  - 原路径: Optional > 开发须知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012081673.md
  - 原更新时间: 2024-11-21 08:19:57

- **总述-APIv3如何签名和验签** (`4012365870`)
  - 原路径: Optional > 开发须知
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365870.md
  - 原更新时间: 2024-11-21 10:50:08

- **基本规则** (`4012081726`)
  - 原路径: Optional > 开发须知 > 接口规则说明
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012081726.md
  - 原更新时间: 2024-07-25 02:06:07

- **HTTP状态码** (`4012081727`)
  - 原路径: Optional > 开发须知 > 接口规则说明
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012081727.md
  - 原更新时间: 2024-07-25 02:07:36

- **开发必要参数说明** (`4013080340`)
  - 原路径: Optional > 开发须知 > 开发参数申请和配置
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080340.md
  - 原更新时间: 2026-06-02 08:22:05

- **mchid与appid申请** (`4012081990`)
  - 原路径: Optional > 开发须知 > 开发参数申请和配置
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012081990.md
  - 原更新时间: 2025-10-28 03:00:48

- **管理商户号绑定的APPID账号** (`4016329059`)
  - 原路径: Optional > 开发须知 > 开发参数申请和配置
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016329059.md
  - 原更新时间: 2025-10-28 03:00:48

- **配置APIv3密钥** (`4012081991`)
  - 原路径: Optional > 开发须知 > 开发参数申请和配置
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012081991.md
  - 原更新时间: 2025-10-28 03:00:48

- **品牌经营API开发必要参数说明** (`4015981654`)
  - 原路径: Optional > 开发须知 > 开发参数申请和配置
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015981654.md
  - 原更新时间: 2025-12-15 01:50:19

- **平台员工权限管理** (`4013080349`)
  - 原路径: Optional > 开发须知 > 开发参数申请和配置
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013080349.md
  - 原更新时间: 2025-09-19 01:36:32

- **申请商户API证书** (`4012081992`)
  - 原路径: Optional > 开发须知 > 开发参数申请和配置 > 商户API证书管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012081992.md
  - 原更新时间: 2025-10-28 03:01:36

- **如何更换商户API证书？** (`4013058943`)
  - 原路径: Optional > 开发须知 > 开发参数申请和配置 > 商户API证书管理
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013058943.md
  - 原更新时间: 2024-11-20 03:18:41

- **请求参数里带Path参数（路径参数），如何计算签名** (`4012365862`)
  - 原路径: Optional > 开发须知 > 如何签名 > 如何构造接口请求签名
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365862.md
  - 原更新时间: 2025-02-18 08:09:32

- **请求参数里带Body参数(包体参数），如何计算签名** (`4012365864`)
  - 原路径: Optional > 开发须知 > 如何签名 > 如何构造接口请求签名
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365864.md
  - 原更新时间: 2025-02-18 09:53:43

- **请求参数里有Query（查询参数），如何计算签名** (`4012365865`)
  - 原路径: Optional > 开发须知 > 如何签名 > 如何构造接口请求签名
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365865.md
  - 原更新时间: 2025-02-18 09:53:41

- **图片上传接口，如何计算签名** (`4012365863`)
  - 原路径: Optional > 开发须知 > 如何签名 > 如何构造接口请求签名
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365863.md
  - 原更新时间: 2025-03-25 03:03:49

- **APP调起支付签名** (`4012365868`)
  - 原路径: Optional > 开发须知 > 如何签名 > 如何构造调起支付签名
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365868.md
  - 原更新时间: 2025-03-26 09:28:08

- **JSAPI调起支付签名** (`4012365867`)
  - 原路径: Optional > 开发须知 > 如何签名 > 如何构造调起支付签名
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365867.md
  - 原更新时间: 2025-03-26 09:28:07

- **小程序调起支付签名** (`4012365869`)
  - 原路径: Optional > 开发须知 > 如何签名 > 如何构造调起支付签名
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365869.md
  - 原更新时间: 2025-03-26 09:28:05

- **如何使用微信支付公钥验签** (`4013059017`)
  - 原路径: Optional > 开发须知 > 如何验签
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059017.md
  - 原更新时间: 2024-11-20 06:55:05

- **如何使用平台证书验签名** (`4013059030`)
  - 原路径: Optional > 开发须知 > 如何验签 > 如何使用平台证书验签
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059030.md
  - 原更新时间: 2024-11-29 09:43:48

- **如何使用签名/验签工具** (`4012365880`)
  - 原路径: Optional > 开发须知 > 如何验签 > 如何使用平台证书验签
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365880.md
  - 原更新时间: 2024-12-27 04:05:13

- **如何使用微信支付公钥加密敏感字段** (`4013059044`)
  - 原路径: Optional > 开发须知 > 如何加解密敏感字段
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059044.md
  - 原更新时间: 2025-03-19 08:49:11

- **如何使用平台证书加密敏感字段** (`4013059053`)
  - 原路径: Optional > 开发须知 > 如何加解密敏感字段
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059053.md
  - 原更新时间: 2025-03-19 08:49:03

- **如何使用API证书解密敏感字段** (`4013059060`)
  - 原路径: Optional > 开发须知 > 如何加解密敏感字段
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059060.md
  - 原更新时间: 2024-11-20 03:29:55

- **如何解密回调报文和平台证书** (`4012082320`)
  - 原路径: Optional > 开发须知 > 如何解密微信支付回调报文
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082320.md
  - 原更新时间: 2024-11-29 08:22:52

- **报错：HTTP header缺少微信支付平台证书序列号(Wechatpay-Serial)** (`4012365874`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365874.md
  - 原更新时间: 2024-11-19 09:07:14

- **报错：Http头Authorization值格式错误，请参考《微信支付商户REST API签名规则》或者“Authorization不合法”** (`4012365872`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365872.md
  - 原更新时间: 2026-01-23 03:31:55

- **报错：商户证书序列号有误。请使用签名私钥匹配的证书序列号** (`4012365873`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365873.md
  - 原更新时间: 2024-12-12 03:12:16

- **报错：状态码401或者“错误的签名，验签失败”或者“签名错误，请检查后再试”** (`4012365875`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365875.md
  - 原更新时间: 2024-12-12 03:12:14

- **调起支付报错：支付验证签名失败** (`4012365876`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012365876.md
  - 原更新时间: 2025-03-26 09:28:04

- **使用Java加载密钥时，抛出异常InvalidKeyException: Illegal key size** (`4013059103`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059103.md
  - 原更新时间: 2024-11-20 03:37:11

- **使用Java解密时，抛出异常AEADBadTagException: Tag mismatch** (`4013059153`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059153.md
  - 原更新时间: 2024-11-20 03:38:02

- **请求返回{"code":"PARAM_ERROR","message":"平台证书序列号Wechatpay-Serial错误"}** (`4013059161`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059161.md
  - 原更新时间: 2024-11-20 03:38:49

- **为什么微信支付的回调缺少签名的几个HTTP头？** (`4013059166`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059166.md
  - 原更新时间: 2024-11-20 03:39:20

- **如何在程序中加载商户API证书私钥** (`4013059175`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059175.md
  - 原更新时间: 2025-12-25 06:37:41

- **如何查看商户API证书或平台证书序列号？** (`4013059181`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059181.md
  - 原更新时间: 2024-11-26 02:43:01

- **为什么请求返回401 Unauthorized？** (`4012082324`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082324.md
  - 原更新时间: 2024-11-25 08:53:06

- **验证微信支付响应的签名报错：签名验证失败** (`4016241895`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016241895.md
  - 原更新时间: 2025-10-14 06:39:36

- **调用接口报错：“平台私钥解密失败”** (`4016913182`)
  - 原路径: Optional > 开发须知 > 常见问题
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016913182.md
  - 原更新时间: 2025-12-19 02:59:24

- **跨城冗灾升级指引** (`4012082567`)
  - 原路径: Optional > 最佳实践
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082567.md
  - 原更新时间: 2025-03-21 07:37:49

- **支付回调和查单实现指引** (`4012082568`)
  - 原路径: Optional > 最佳实践
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082568.md
  - 原更新时间: 2024-12-18 07:43:24

- **专线商户Notify升级指引** (`4012082569`)
  - 原路径: Optional > 最佳实践
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082569.md
  - 原更新时间: 2024-07-25 03:04:49

- **回调通知注意事项** (`4012082570`)
  - 原路径: Optional > 最佳实践
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082570.md
  - 原更新时间: 2024-07-25 03:04:49

- **最佳安全实践** (`4012082456`)
  - 原路径: Optional > 最佳实践 > API安全最佳实践
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082456.md
  - 原更新时间: 2024-11-27 09:15:00

- **安全漏洞checklist** (`4013059657`)
  - 原路径: Optional > 最佳实践 > API安全最佳实践
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059657.md
  - 原更新时间: 2024-11-27 09:14:52

- **系统漏洞检测及修复** (`4013059668`)
  - 原路径: Optional > 最佳实践 > API安全最佳实践
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059668.md
  - 原更新时间: 2025-03-21 07:40:38

- **Web漏洞检测及修复** (`4013059740`)
  - 原路径: Optional > 最佳实践 > API安全最佳实践
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059740.md
  - 原更新时间: 2025-03-21 08:53:52

- **最新安全漏洞及修复** (`4013059970`)
  - 原路径: Optional > 最佳实践 > API安全最佳实践
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4013059970.md
  - 原更新时间: 2024-11-27 09:14:33

- **密钥泄漏修复指引** (`4012082455`)
  - 原路径: Optional > 最佳实践 > API安全最佳实践
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082455.md
  - 原更新时间: 2024-12-24 01:54:38

- **国家商用密码简介** (`4012082627`)
  - 原路径: Optional > 国家商用密码接入指南
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082627.md
  - 原更新时间: 2024-07-25 03:09:50

- **获取国家商用密码证书和密钥** (`4012082628`)
  - 原路径: Optional > 国家商用密码接入指南
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082628.md
  - 原更新时间: 2024-07-25 03:09:50

- **APIv3接口使用国家商用密码指引** (`4012082629`)
  - 原路径: Optional > 国家商用密码接入指南
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082629.md
  - 原更新时间: 2024-07-25 03:09:50

- **开户银行全称对照表** (`4012082812`)
  - 原路径: Optional > 对照表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082812.md
  - 原更新时间: 2024-07-25 03:24:06

- **开户银行对照表** (`4012082813`)
  - 原路径: Optional > 对照表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082813.md
  - 原更新时间: 2025-02-19 07:30:19

- **银行类型对照表** (`4012082814`)
  - 原路径: Optional > 对照表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082814.md
  - 原更新时间: 2024-07-25 03:24:06

- **省市区编号对照表** (`4012082815`)
  - 原路径: Optional > 对照表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082815.md
  - 原更新时间: 2024-07-25 03:24:06

- **优惠费率活动对照表** (`4012082816`)
  - 原路径: Optional > 对照表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082816.md
  - 原更新时间: 2024-12-26 08:48:22

- **跨境电商二级商户费率对照表** (`4012082817`)
  - 原路径: Optional > 对照表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082817.md
  - 原更新时间: 2024-07-25 03:24:06

- **商户行业编码** (`4012082818`)
  - 原路径: Optional > 对照表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082818.md
  - 原更新时间: 2024-07-25 03:24:06

- **特殊行业ID对照表** (`4012082819`)
  - 原路径: Optional > 对照表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012082819.md
  - 原更新时间: 2024-07-25 03:24:06

- **接入模式** (`4012081931`)
  - 原路径: Optional > 名词表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012081931.md
  - 原更新时间: 2026-06-01 06:16:40

- **支付产品** (`4012081932`)
  - 原路径: Optional > 名词表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012081932.md
  - 原更新时间: 2024-07-25 02:23:51

- **业务平台** (`4012081933`)
  - 原路径: Optional > 名词表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012081933.md
  - 原更新时间: 2024-07-25 02:23:51

- **业务系统** (`4012081934`)
  - 原路径: Optional > 名词表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012081934.md
  - 原更新时间: 2024-07-25 02:23:51

- **参数说明** (`4012081935`)
  - 原路径: Optional > 名词表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012081935.md
  - 原更新时间: 2024-10-29 02:13:52

- **常见问题** (`4016183684`)
  - 原路径: Optional > 名词表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4016183684.md
  - 原更新时间: 2026-04-28 06:50:12

- **微信支付链路界面与交互规范** (`4020527499`)
  - 原路径: Optional > 服务运营规范
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4020527499.md
  - 原更新时间: 2026-05-19 02:15:32

- **Postman调试工具** (`4012083114`)
  - 原路径: Optional > 开发工具
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012083114.md
  - 原更新时间: 2024-11-29 09:45:15

- **平台证书下载工具** (`4012083115`)
  - 原路径: Optional > 开发工具
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012083115.md
  - 原更新时间: 2024-11-27 09:13:57

- **验签工具** (`4012083116`)
  - 原路径: Optional > 开发工具
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012083116.md
  - 原更新时间: 2025-01-03 07:02:48

- **产品介绍** (`4012083118`)
  - 原路径: Optional > 网络云排查
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012083118.md
  - 原更新时间: 2025-03-21 07:39:41

- **网络问题排查指南** (`4012083119`)
  - 原路径: Optional > 网络云排查
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012083119.md
  - 原更新时间: 2025-03-21 07:39:03

- **常见问题** (`4012083120`)
  - 原路径: Optional > 网络云排查
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012083120.md
  - 原更新时间: 2024-07-25 03:43:58

- **产品介绍** (`4012083122`)
  - 原路径: Optional > 安全医生
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012083122.md
  - 原更新时间: 2024-07-25 03:43:58

- **诊断链接绑定指引** (`4012083123`)
  - 原路径: Optional > 安全医生
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012083123.md
  - 原更新时间: 2024-07-25 03:43:58

- **安全联系人设置指引** (`4012083124`)
  - 原路径: Optional > 安全医生
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012083124.md
  - 原更新时间: 2024-07-25 03:43:58

- **SDK概述** (`4012083109`)
  - 原路径: Optional > SDK
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012083109.md
  - 原更新时间: 2026-04-24 09:22:07

- **使用 Java SDK** (`4012083111`)
  - 原路径: Optional > SDK
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012083111.md
  - 原更新时间: 2025-05-29 03:32:06

- **使用 PHP SDK** (`4012083112`)
  - 原路径: Optional > SDK
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012083112.md
  - 原更新时间: 2025-05-29 03:32:04

- **使用 Go SDK** (`4012083113`)
  - 原路径: Optional > SDK
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4012083113.md
  - 原更新时间: 2025-05-29 03:36:58

## 附录：所有页面清单

<details>
<summary>点击查看全部 0 个页面</summary>

| 序号 | 标题（链接） | ID | 更新时间 | 完整路径 |
|------|-------------|----|----------|----------|

</details>