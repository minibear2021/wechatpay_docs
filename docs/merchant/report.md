# 微信支付文档更新报告 - 直连商户

**文档类型**: 直连商户 (merchant)
**生成时间**: 20260526_013422
**文档总数**: 520
**数据来源**: https://pay.weixin.qq.com/doc/v3/merchant/llms.txt

## 变更概览

- 新增: 1 个页面
- 删除: 1 个页面
- 修改: 42 个页面
- 成功拉取: 43 个页面
- 拉取失败: 0 个页面
- llms.txt 变更: 是

## llms.txt 变更

```diff
--- llms_old.txt
+++ llms.txt
@@ -151,16 +151,32 @@
 - [管理商户号绑定的APPID账号](https://pay.weixin.qq.com/doc/v3/merchant/4013287504.md)
 - [申请JSAPI支付权限指引(小程序支付场景)](https://pay.weixin.qq.com/doc/v3/merchant/4012791895.md)
 - [各主体可申请的基础支付权限列表](https://pay.weixin.qq.com/doc/v3/merchant/4015459054.md)
-## 合单支付
-> 合单支付支持将多个子商户订单合并为一笔支付，用户一次性完成付款，资金按规则分入对应商户账户，适用于电商购物车、多商家联合订单等场景，简化支付流程，提升平台与商户结算效率。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/merchant/4012077203.md)
-### APP合单支付
+## JSAPI合单支付
+- [产品介绍](https://pay.weixin.qq.com/doc/v3/merchant/4012077221.md)
+- [开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4015764634.md)
+- [开发指引](https://pay.weixin.qq.com/doc/v3/merchant/4012078634.md)
+- [常见问题](https://pay.weixin.qq.com/doc/v3/merchant/4013421298.md)
+### API列表
+- [JSAPI合单下单](https://pay.weixin.qq.com/doc/v3/merchant/4012556926.md)
+- [JSAPI调起支付](https://pay.weixin.qq.com/doc/v3/merchant/4012266069.md)
+- [查询合单订单](https://pay.weixin.qq.com/doc/v3/merchant/4013421222.md)
+- [关闭合单订单](https://pay.weixin.qq.com/doc/v3/merchant/4013421225.md)
+- [合单订单支付成功回调通知](https://pay.weixin.qq.com/doc/v3/merchant/4013421231.md)
+- [退款申请](https://pay.weixin.qq.com/doc/v3/merchant/4013421249.md)
+- [查询单笔退款（通过商户退款单号）](https://pay.weixin.qq.com/doc/v3/merchant/4013421261.md)
+- [发起异常退款](https://pay.weixin.qq.com/doc/v3/merchant/4013421269.md)
+- [退款结果回调通知](https://pay.weixin.qq.com/doc/v3/merchant/4013421273.md)
+- [申请交易账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421277.md)
+- [申请资金账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421284.md)
+- [下载账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421294.md)
+### 附录
+- [管理商户号绑定的APPID账号](https://pay.weixin.qq.com/doc/v3/merchant/4013426141.md)
+## APP合单支付
 - [产品介绍](https://pay.weixin.qq.com/doc/v3/merchant/4012077215.md)
 - [开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)
 - [开发指引](https://pay.weixin.qq.com/doc/v3/merchant/4012077667.md)
 - [常见问题](https://pay.weixin.qq.com/doc/v3/merchant/4013420906.md)
-#### API列表
+### API列表
 - [App合单下单](https://pay.weixin.qq.com/doc/v3/merchant/4012556944.md)
 - [App调起支付](https://pay.weixin.qq.com/doc/v3/merchant/4012266043.md)
 - [查询合单订单](https://pay.weixin.qq.com/doc/v3/merchant/4012557006.md)
@@ -173,12 +189,12 @@
 - [申请交易账单](https://pay.weixin.qq.com/doc/v3/merchant/4012556692.md)
 - [申请资金账单](https://pay.weixin.qq.com/doc/v3/merchant/4012556748.md)
 - [下载账单](https://pay.weixin.qq.com/doc/v3/merchant/4012085923.md)
-### H5合单支付
+## H5合单支付
 - [产品介绍](https://pay.weixin.qq.com/doc/v3/merchant/4013421104.md)
 - [开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4015764448.md)
 - [开发指引](https://pay.weixin.qq.com/doc/v3/merchant/4012078230.md)
 - [常见问题](https://pay.weixin.qq.com/doc/v3/merchant/4013421196.md)
-#### API列表
+### API列表
 - [H5合单下单](https://pay.weixin.qq.com/doc/v3/merchant/4012556961.md)
 - [H5调起支付](https://pay.weixin.qq.com/doc/v3/merchant/4012266131.md)
 - [查询合单订单](https://pay.weixin.qq.com/doc/v3/merchant/4013421126.md)
@@ -191,30 +207,12 @@
 - [申请交易账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421176.md)
 - [申请资金账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421185.md)
 - [下载账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421189.md)
-### JSAPI合单支付
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/merchant/4012077221.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4015764634.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/merchant/4012078634.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/merchant/4013421298.md)
-#### API列表
-- [JSAPI合单下单](https://pay.weixin.qq.com/doc/v3/merchant/4012556926.md)
-- [JSAPI调起支付](https://pay.weixin.qq.com/doc/v3/merchant/4012266069.md)
-- [查询合单订单](https://pay.weixin.qq.com/doc/v3/merchant/4013421222.md)
-- [关闭合单订单](https://pay.weixin.qq.com/doc/v3/merchant/4013421225.md)
-- [合单订单支付成功回调通知](https://pay.weixin.qq.com/doc/v3/merchant/4013421231.md)
-- [退款申请](https://pay.weixin.qq.com/doc/v3/merchant/4013421249.md)
-- [查询单笔退款（通过商户退款单号）](https://pay.weixin.qq.com/doc/v3/merchant/4013421261.md)
-- [发起异常退款](https://pay.weixin.qq.com/doc/v3/merchant/4013421269.md)
-- [退款结果回调通知](https://pay.weixin.qq.com/doc/v3/merchant/4013421273.md)
-- [申请交易账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421277.md)
-- [申请资金账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421284.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421294.md)
-### Native合单支付
+## Native合单支付
 - [产品介绍](https://pay.weixin.qq.com/doc/v3/merchant/4012077545.md)
 - [开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4015764779.md)
 - [开发指引](https://pay.weixin.qq.com/doc/v3/merchant/4012078926.md)
 - [常见问题](https://pay.weixin.qq.com/doc/v3/merchant/4013421369.md)
-#### API列表
+### API列表
 - [Native合单下单](https://pay.weixin.qq.com/doc/v3/merchant/4012556982.md)
 - [Native调起支付](https://pay.weixin.qq.com/doc/v3/merchant/4012266088.md)
 - [查询合单订单](https://pay.weixin.qq.com/doc/v3/merchant/4013421316.md)
@@ -227,12 +225,12 @@
 - [申请交易账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421361.md)
 - [申请资金账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421365.md)
 - [下载账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421368.md)
-### 小程序合单支付
+## 小程序合单支付
 - [产品介绍](https://pay.weixin.qq.com/doc/v3/merchant/4012077589.md)
 - [开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4015765029.md)
 - [开发指引](https://pay.weixin.qq.com/doc/v3/merchant/4012079115.md)
 - [常见问题](https://pay.weixin.qq.com/doc/v3/merchant/4013421468.md)
-#### API列表
+### API列表
 - [小程序合单下单](https://pay.weixin.qq.com/doc/v3/merchant/4012556931.md)
 - [小程序调起支付](https://pay.weixin.qq.com/doc/v3/merchant/4012266109.md)
 - [查询合单订单](https://pay.weixin.qq.com/doc/v3/merchant/4013421401.md)
@@ -245,8 +243,6 @@
 - [申请交易账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421450.md)
 - [申请资金账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421456.md)
 - [下载账单](https://pay.weixin.qq.com/doc/v3/merchant/4013421461.md)
-### 附录
-- [管理商户号绑定的APPID账号](https://pay.weixin.qq.com/doc/v3/merchant/4013426141.md)
 ## 医保支付
 > 医保支付支持用户在微信激活医保电子凭证后，直接完成挂号、门诊缴费等费用的线上医保支付，无需前往线下窗口排队，有助于提高医疗医保服务效率，改善医患关系，为用户提供更便捷流畅的就医体验。
 
@@ -298,10 +294,27 @@
 - [交易账单详细说明](https://pay.weixin.qq.com/doc/v3/merchant/4013071246.md)
 - [资金账单详细说明](https://pay.weixin.qq.com/doc/v3/merchant/4013071249.md)
 - [下载账单操作指引](https://pay.weixin.qq.com/doc/v3/merchant/4013071252.md)
-## 现金红包（V2）
-> 现金红包是微信支付提供的营销工具，商户可以通过公众号或者服务通知向用户发放现金红包。用户领取红包后，资金到达用户微信支付零钱账户；若用户未领取， 资金将会在24小时后退回商户的微信支付账户中。适用于拉新、促活、福利发放等场景。
-
-- [现金红包（V2）](https://pay.weixin.qq.com/doc/v3/merchant/4012647471.md)
+## 分账
+> 分账是商户用于交易资金分配的工具，支持将资金分给合作伙伴、员工、用户等分润方。资金先冻结，可实时或延时分账，单笔最多分 50 次、每次可分 50 方，支持商户或个人账户接收，需设置最大分账比例，全程免手续费。
+
+- [产品介绍](https://pay.weixin.qq.com/doc/v3/merchant/4012067962.md)
+- [开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4012067989.md)
+- [开发指引](https://pay.weixin.qq.com/doc/v3/merchant/4012068033.md)
+- [常见问题](https://pay.weixin.qq.com/doc/v3/merchant/4014547102.md)
+### API列表
+- [请求分账](https://pay.weixin.qq.com/doc/v3/merchant/4012524936.md)
+- [查询分账结果](https://pay.weixin.qq.com/doc/v3/merchant/4012525210.md)
+- [请求分账回退](https://pay.weixin.qq.com/doc/v3/merchant/4012525287.md)
+- [查询分账回退结果](https://pay.weixin.qq.com/doc/v3/merchant/4012526279.md)
+- [解冻剩余资金](https://pay.weixin.qq.com/doc/v3/merchant/4012526374.md)
+- [查询剩余待分金额](https://pay.weixin.qq.com/doc/v3/merchant/4012457939.md)
+- [添加分账接收方](https://pay.weixin.qq.com/doc/v3/merchant/4012528995.md)
+- [删除分账接收方](https://pay.weixin.qq.com/doc/v3/merchant/4012529590.md)
+- [分账动态通知](https://pay.weixin.qq.com/doc/v3/merchant/4012289679.md)
+- [申请分账账单](https://pay.weixin.qq.com/doc/v3/merchant/4012529628.md)
+- [下载账单](https://pay.weixin.qq.com/doc/v3/merchant/4012289690.md)
+### 附录
+- [分账失败处理指引](https://pay.weixin.qq.com/doc/v3/merchant/4015505684.md)
 ## 商家转账
 > 商家转账是微信支付面向商户推出的免费转账产品，仅支持商户向用户微信零钱转账，资金实时到账且成功后不可退回。需用户在微信官方页面确认收款，支持营销奖励、佣金、赔付、货款、报销等多场景，可实名验权、查询记录并获取电子回单，安全高效。
 
@@ -431,6 +444,10 @@
 - [退款申请](https://pay.weixin.qq.com/doc/v3/merchant/4012557131.md)
 - [退款结果通知](https://pay.weixin.qq.com/doc/v3/merchant/4012083103.md)
 - [查询单笔退款（通过商户退款单号）](https://pay.weixin.qq.com/doc/v3/merchant/4012557161.md)
+## 现金红包（V2）
+> 现金红包是微信支付提供的营销工具，商户可以通过公众号或者服务通知向用户发放现金红包。用户领取红包后，资金到达用户微信支付零钱账户；若用户未领取， 资金将会在24小时后退回商户的微信支付账户中。适用于拉新、促活、福利发放等场景。
+
+- [现金红包（V2）](https://pay.weixin.qq.com/doc/v3/merchant/4012647471.md)
 ## 代金券
 > 微信支付官方营销工具，支持商户配置满减、折扣等券型，可在支付前发放、支付中自动核销。支持线上线下多场景投放，数据实时可查，助力商户拉新、复购与客流提升，适配多行业营销需求。
 
@@ -438,6 +455,7 @@
 - [开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4012084133.md)
 - [开发指引](https://pay.weixin.qq.com/doc/v3/merchant/4012084207.md)
 - [常见问题](https://pay.weixin.qq.com/doc/v3/merchant/4015880636.md)
+- [业务示例代码](https://pay.weixin.qq.com/doc/v3/merchant/4015894256.md)
 ### API列表
 - [核销事件回调通知](https://pay.weixin.qq.com/doc/v3/merchant/4012285250.md)
 - [图片上传（营销专用）](https://pay.weixin.qq.com/doc/v3/merchant/4012557233.md)
@@ -534,27 +552,6 @@
 > 清关报关是微信支付面向跨境商户的自助清关工具，商户可在商户平台开通并配置海关信息，通过接口将支付单推送至海关电子口岸，完成 “三单合一” 申报，助力跨境订单合规通关，提升清关效率，免费使用。
 
 - [清关报关（V2）](https://pay.weixin.qq.com/doc/v3/merchant/4012647500.md)
-## 分账
-> 分账是商户用于交易资金分配的工具，支持将资金分给合作伙伴、员工、用户等分润方。资金先冻结，可实时或延时分账，单笔最多分 50 次、每次可分 50 方，支持商户或个人账户接收，需设置最大分账比例，全程免手续费。
-
-- [产品介绍](https://pay.weixin.qq.com/doc/v3/merchant/4012067962.md)
-- [开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4012067989.md)
-- [开发指引](https://pay.weixin.qq.com/doc/v3/merchant/4012068033.md)
-- [常见问题](https://pay.weixin.qq.com/doc/v3/merchant/4014547102.md)
-### API列表
-- [请求分账](https://pay.weixin.qq.com/doc/v3/merchant/4012524936.md)
-- [查询分账结果](https://pay.weixin.qq.com/doc/v3/merchant/4012525210.md)
-- [请求分账回退](https://pay.weixin.qq.com/doc/v3/merchant/4012525287.md)
-- [查询分账回退结果](https://pay.weixin.qq.com/doc/v3/merchant/4012526279.md)
-- [解冻剩余资金](https://pay.weixin.qq.com/doc/v3/merchant/4012526374.md)
-- [查询剩余待分金额](https://pay.weixin.qq.com/doc/v3/merchant/4012457939.md)
-- [添加分账接收方](https://pay.weixin.qq.com/doc/v3/merchant/4012528995.md)
-- [删除分账接收方](https://pay.weixin.qq.com/doc/v3/merchant/4012529590.md)
-- [分账动态通知](https://pay.weixin.qq.com/doc/v3/merchant/4012289679.md)
-- [申请分账账单](https://pay.weixin.qq.com/doc/v3/merchant/4012529628.md)
-- [下载账单](https://pay.weixin.qq.com/doc/v3/merchant/4012289690.md)
-### 附录
-- [分账失败处理指引](https://pay.weixin.qq.com/doc/v3/merchant/4015505684.md)
 ## 消费者投诉2.0
 > 消费者投诉 2.0 提供商户端线上投诉协同处理能力，支持实时获取投诉信息、在线协商、上传凭证、反馈处理结果，全流程可追溯。帮助商户高效处理交易纠纷，提升用户体验，降低合规与经营风险，适配多行业售后管理。
 
```

## 新增页面

### 业务示例代码
- ID: `4015894256`
- 路径: 代金券
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015894256.md
- 更新时间: 2026-05-19 08:07:01
- 本地文件: `pages/4015894256.md`

## 删除页面

- **产品介绍** (`4012077203`)
  - 原路径: 合单支付
  - 原 URL: https://pay.weixin.qq.com/doc/v3/merchant/4012077203.md
  - 原更新时间: 2025-08-01 02:44:23

## 修改页面

### 开发接入准备
- ID: `4015423216`
- 路径: JSAPI支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015423216.md
- 更新时间变更: 2025-11-20 07:26:41 -> 2026-05-21 07:03:41
- 本地文件: `pages/4015423216.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 开发接入准备
- ID: `4015478291`
- 路径: APP支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015478291.md
- 更新时间变更: 2025-11-20 07:26:22 -> 2026-05-19 07:50:37
- 本地文件: `pages/4015478291.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 开发接入准备
- ID: `4015614193`
- 路径: H5支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015614193.md
- 更新时间变更: 2025-11-20 07:26:05 -> 2026-05-19 07:51:45
- 本地文件: `pages/4015614193.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 开发接入准备
- ID: `4015614538`
- 路径: Native支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015614538.md
- 更新时间变更: 2025-11-20 07:25:41 -> 2026-05-19 07:52:00
- 本地文件: `pages/4015614538.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 常见问题
- ID: `4012791890`
- 路径: Native支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012791890.md
- 更新时间变更: 2025-12-05 02:19:44 -> 2026-05-19 07:39:26
- 本地文件: `pages/4012791890.md`

```diff
--- old.md
+++ new.md
@@ -2,7 +2,7 @@
 
 ### 前端问题
 
-## Q：调用Native支付统一下单成功但是扫描二维码支付时返回系统繁忙，请稍后再试。
+#### Q：调用Native支付统一下单成功但是扫描二维码支付时返回系统繁忙，请稍后再试。
 
 A：可能是由于系统繁忙或参数问题导致的。建议您按照以下步骤进行排查和解决：
 
@@ -11,26 +11,32 @@
 - 检查传入的参数值是否为null，不需要的参数可以不传递，避免以null形式传入。
 
 
-## Q：长按识别Native支付二维码返回：该商户暂不支持通过长按识别二维码完成支付。
+#### Q：长按识别Native支付二维码返回：该商户暂不支持通过长按识别二维码完成支付。
 
 A：微信支付已经不支持通过长按识别二维码的方式完成支付。如果您需要使用微信支付，请尝试使用微信扫一扫功能扫描商家提供的支付二维码。
 
-## Q：通过从相册识别Native支付二维码返回：为保障支付安全，暂不支持通过从相册识别二维码完成支付。
+#### Q：通过从相册识别Native支付二维码返回：为保障支付安全，暂不支持通过从相册识别二维码完成支付。
 
 A：微信支付暂不支持通过从相册识别二维码完成支付。如果您需要使用微信支付，请尝试使用微信扫一扫功能扫描商家提供的支付二维码。
 
-## Q：Native支付和其它的基础支付除了下单接口不一样以外，其余接口都一样吗。
+#### Q：Native支付和其它的基础支付除了下单接口不一样以外，其余接口都一样吗。
 
 A：Native支付和其它的基础支付在接口使用上，除了下单接口和调起支付接口存在差异外，其余接口都是相同的。您可以根据具体的支付场景选择合适的支付方式。
 
-## Q：Native支付，生成二维码后，用户支付的时候报错："商家订单信息有误，请重新下单支付"。
+#### Q：Native支付，生成二维码后，用户支付的时候报错："商家订单信息有误，请重新下单支付"。
 
 A：同一笔订单不允许使用不同的微信号扫码调起支付。商户需要引导用户重新下单，并且提示用户使用同一个微信号扫码拉起支付。
 
-## Q：对于Native支付，如果用户当时没有支付，在微信里可以看到订单并再次进行支付吗？
+#### Q：对于Native支付，如果用户当时没有支付，在微信里可以看到订单并再次进行支付吗？
 
 A：未支付的订单在微信客户端不会显示。通常用户可通过商户系统找到待支付订单主动发起支付操作。
 
-## Q：Native支付，二维码能否实现1分钟刷新？
+#### Q：Native支付，二维码能否实现1分钟刷新？
 
 A：可以通过定时原参数重入下单的方式实现1分钟刷新。重入下单返回的code\_url会改变，同时旧的code\_url将会过期失效。
+
+## 业务常见问题
+
+### Q：境外银行卡是否支持绑定微信支付用于支付？
+
+A：支持的。
```

### 开发接入准备
- ID: `4015459512`
- 路径: 小程序支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015459512.md
- 更新时间变更: 2025-12-08 07:50:09 -> 2026-05-19 07:52:18
- 本地文件: `pages/4015459512.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 开发接入准备
- ID: `4015764634`
- 路径: JSAPI合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015764634.md
- 更新时间变更: 2025-08-06 01:36:46 -> 2026-05-21 08:24:21
- 本地文件: `pages/4015764634.md`

```diff
--- old.md
+++ new.md
@@ -4,7 +4,7 @@
 
 1、阅读[产品介绍文档](https://pay.weixin.qq.com/doc/v3/merchant/4012077221.md)，了解JSAPI合单支付产品特性；
 
-2、合单发起方商户与所有子单参与方商户参考[JSAPI支付-快速开始-步骤1~6](https://pay.weixin.qq.com/doc/v3/merchant/4015423216.md)的指引开通JSAPI支付权限；
+2、合单发起方商户与所有子单参与方商户参考[JSAPI支付-开发接入准备-步骤1~6](https://pay.weixin.qq.com/doc/v3/merchant/4015423216.md)的指引开通JSAPI支付权限；
 
 3、合单发起方商户联系对接的运营人员申请合单支付权限（为合单发起方商户号申请发起合单权限，为所有子单参与方商户号申请接收合单权限）；
 
```

### 开发指引
- ID: `4012078634`
- 路径: JSAPI合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012078634.md
- 更新时间变更: 2025-08-06 01:36:46 -> 2026-05-21 08:24:21
- 本地文件: `pages/4012078634.md`

```diff
--- old.md
+++ new.md
@@ -19,11 +19,11 @@
 
 下单接口关键参数说明：
 
-`combine_mchid`：合单发起方的商户号，需先申请发起合单支付权限，详细参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015764634.md)。
+`combine_mchid`：合单发起方的商户号，需先申请发起合单支付权限，详细参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015764634.md)。
 
-`sub_order.mchid`：子单参与方的商户号，需先申请接收合单支付权限，详细参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015764634.md)。
+`sub_order.mchid`：子单参与方的商户号，需先申请接收合单支付权限，详细参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015764634.md)。
 
-`combine_appid`：公众账号ID，合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细参考：[快速开始-步骤4和5](https://pay.weixin.qq.com/doc/v3/merchant/4015764634.md)。
+`combine_appid`：公众账号ID，合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细参考：[开发接入准备-步骤4和5](https://pay.weixin.qq.com/doc/v3/merchant/4015764634.md)。
 
 `time_expire`：支付结束时间。若传递该参数，则用户只能在订单设置的支付结束时间 `time_expire` 之前进行支付，超过支付结束时间后，用户支付将收到："订单已超过商户设置的最晚支付成功时间，请重新发起支付"的提示，商户需对订单进行关单处理。若不传该参数，默认订单支付有效期为7天，用户可在7天内进行支付，超出7天，订单将被关闭。
 
```

### 常见问题
- ID: `4013421298`
- 路径: JSAPI合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4013421298.md
- 更新时间变更: 2025-08-06 01:36:46 -> 2026-05-21 08:24:21
- 本地文件: `pages/4013421298.md`

```diff
--- old.md
+++ new.md
@@ -24,7 +24,7 @@
 
 ## Q：普通商户模式的合单支付子单列表可以既有普通商户又有特约商户么？
 
-A：普通商户模式的子单列表支持普通商户和特约商户，且需要开通接收合单的权限，参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
+A：普通商户模式的子单列表支持普通商户和特约商户，且需要开通接收合单的权限，参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
 
 注意：小微类型的主体商户号不支持。
 
@@ -50,7 +50,7 @@
 
 ## Q：JSAPI合单支付下单返回报错"appid和mch\_id不匹配，请检查后再试"
 
-A：合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细请参考[快速开始-步骤4~5](https://pay.weixin.qq.com/doc/v3/merchant/4015764634.md)。
+A：合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细请参考[开发接入准备-步骤4~5](https://pay.weixin.qq.com/doc/v3/merchant/4015764634.md)。
 
 ## Q：JSAPI合单下单返回报错"appid与openid不匹配"
 
```

### 开发接入准备
- ID: `4013420660`
- 路径: APP合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md
- 更新时间变更: 2025-08-06 01:36:50 -> 2026-05-20 08:26:06
- 本地文件: `pages/4013420660.md`

```diff
--- old.md
+++ new.md
@@ -4,7 +4,7 @@
 
 1、阅读[产品介绍文档](https://pay.weixin.qq.com/doc/v3/merchant/4012077215.md)，了解APP合单支付产品特性；
 
-2、合单发起方商户与所有子单参与方商户参考[APP支付-快速开始-步骤1~7](https://pay.weixin.qq.com/doc/v3/merchant/4015478291.md)指引开通APP支付权限；
+2、合单发起方商户与所有子单参与方商户参考[APP支付-开发接入准备-步骤1~7](https://pay.weixin.qq.com/doc/v3/merchant/4015478291.md)指引开通APP支付权限；
 
 3、合单发起方商户联系对接的运营人员申请合单支付权限（为合单发起方商户号申请发起合单权限，为所有子单参与方商户号申请接收合单权限）；
 
```

### 开发指引
- ID: `4012077667`
- 路径: APP合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012077667.md
- 更新时间变更: 2025-08-06 01:36:50 -> 2026-05-20 08:31:11
- 本地文件: `pages/4012077667.md`

```diff
--- old.md
+++ new.md
@@ -19,11 +19,11 @@
 
 下单接口关键参数说明：
 
-`combine_mchid`：合单发起方的商户号，需先申请发起合单支付权限，详细参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
+`combine_mchid`：合单发起方的商户号，需先申请发起合单支付权限，详细参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
 
-`sub_order.mchid`：子单参与方的商户号，需先申请接收合单支付权限，详细参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
+`sub_order.mchid`：子单参与方的商户号，需先申请接收合单支付权限，详细参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
 
-`combine_appid`：公众账号ID，合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细参考：[快速开始-步骤4和5](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
+`combine_appid`：公众账号ID，合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细参考：[开发接入准备-步骤4和5](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
 
 `time_expire`：支付结束时间。若传递该参数，则用户只能在订单设置的支付结束时间 `time_expire` 之前进行支付，超过支付结束时间后，用户支付将收到："订单已超过商户设置的最晚支付成功时间，请重新发起支付"的提示，商户需对订单进行关单处理。若不传该参数，默认订单支付有效期为7天，用户可在7天内进行支付，超出7天，订单将被关闭。
 
```

### 常见问题
- ID: `4013420906`
- 路径: APP合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4013420906.md
- 更新时间变更: 2025-08-06 01:36:50 -> 2026-05-20 08:33:17
- 本地文件: `pages/4013420906.md`

```diff
--- old.md
+++ new.md
@@ -24,7 +24,7 @@
 
 ## Q：普通商户模式的合单支付子单列表可以既有普通商户又有特约商户么？
 
-A：普通商户模式的子单列表支持普通商户和特约商户，且需要开通接收合单的权限，参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
+A：普通商户模式的子单列表支持普通商户和特约商户，且需要开通接收合单的权限，参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
 
 注意：小微类型的主体商户号不支持。
 
@@ -50,7 +50,7 @@
 
 ## Q：APP合单支付下单返回报错"appid和mch\_id不匹配，请检查后再试"
 
-A：合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细请参考[快速开始-步骤4~5](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
+A：合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细请参考[开发接入准备-步骤4~5](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
 
 ## Q：App调起支付时前端返回errcode=-1，如何进行排查？
 
```

### 开发接入准备
- ID: `4015764448`
- 路径: H5合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015764448.md
- 更新时间变更: 2025-08-06 01:36:48 -> 2026-05-20 08:27:15
- 本地文件: `pages/4015764448.md`

```diff
--- old.md
+++ new.md
@@ -4,7 +4,7 @@
 
 1、阅读[产品介绍文档](https://pay.weixin.qq.com/doc/v3/merchant/4013421104.md)，了解H5合单支付产品特性；
 
-2、合单发起方商户与所有子单参与方商户参考[H5支付-快速开始-步骤1~6](https://pay.weixin.qq.com/doc/v3/merchant/4015614193.md)指引开通H5支付权限；
+2、合单发起方商户与所有子单参与方商户参考[H5支付-开发接入准备-步骤1~6](https://pay.weixin.qq.com/doc/v3/merchant/4015614193.md)指引开通H5支付权限；
 
 3、合单发起方商户联系对接的运营人员申请合单支付权限（为合单发起方商户号申请发起合单权限，为所有子单参与方商户号申请接收合单权限）；
 
```

### 开发指引
- ID: `4012078230`
- 路径: H5合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012078230.md
- 更新时间变更: 2025-08-06 01:36:48 -> 2026-05-20 09:37:25
- 本地文件: `pages/4012078230.md`

```diff
--- old.md
+++ new.md
@@ -33,11 +33,11 @@
 
 下单接口关键参数说明：
 
-`combine_mchid`：合单发起方的商户号，需先申请发起合单支付权限，详细参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015764448.md)。
+`combine_mchid`：合单发起方的商户号，需先申请发起合单支付权限，详细参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015764448.md)。
 
-`sub_order.mchid`：子单参与方的商户号，需先申请接收合单支付权限，详细参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015764448.md)。
+`sub_order.mchid`：子单参与方的商户号，需先申请接收合单支付权限，详细参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015764448.md)。
 
-`combine_appid`：公众账号ID，合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细参考：[快速开始-步骤4和5](https://pay.weixin.qq.com/doc/v3/merchant/4015764448.md)。
+`combine_appid`：公众账号ID，合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细参考：[开发接入准备-步骤4和5](https://pay.weixin.qq.com/doc/v3/merchant/4015764448.md)。
 
 `time_expire`：支付结束时间。若传递该参数，则用户只能在订单设置的支付结束时间 `time_expire` 之前进行支付，超过支付结束时间后，用户支付将收到："订单已超过商户设置的最晚支付成功时间，请重新发起支付"的提示，商户需对订单进行关单处理。若不传该参数，默认订单支付有效期为7天，用户可在7天内进行支付，超出7天，订单将被关闭。
 
```

### 开发接入准备
- ID: `4015764779`
- 路径: Native合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015764779.md
- 更新时间变更: 2025-08-06 01:36:44 -> 2026-05-20 08:28:07
- 本地文件: `pages/4015764779.md`

```diff
--- old.md
+++ new.md
@@ -4,7 +4,7 @@
 
 1、阅读[产品介绍文档](https://pay.weixin.qq.com/doc/v3/merchant/4012077545.md)，了解Native合单支付产品特性；
 
-2、合单发起方商户与所有子单参与方商户参考[Native支付-快速开始-步骤1~6](https://pay.weixin.qq.com/doc/v3/merchant/4015614538.md)指引开通Native支付权限；
+2、合单发起方商户与所有子单参与方商户参考[Native支付-开发接入准备-步骤1~6](https://pay.weixin.qq.com/doc/v3/merchant/4015614538.md)指引开通Native支付权限；
 
 3、合单发起方商户联系对接的运营人员申请合单支付权限（为合单发起方商户号申请发起合单权限，为所有子单参与方商户号申请接收合单权限）；
 
```

### 开发指引
- ID: `4012078926`
- 路径: Native合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012078926.md
- 更新时间变更: 2025-08-06 01:36:44 -> 2026-05-20 09:52:24
- 本地文件: `pages/4012078926.md`

```diff
--- old.md
+++ new.md
@@ -19,11 +19,11 @@
 
 下单接口关键参数说明：
 
-`combine_mchid`：合单发起方的商户号，需先申请发起合单支付权限，详细参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015764779.md)。
+`combine_mchid`：合单发起方的商户号，需先申请发起合单支付权限，详细参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015764779.md)。
 
-`sub_order.mchid`：子单参与方的商户号，需先申请接收合单支付权限，详细参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015764779.md)。
+`sub_order.mchid`：子单参与方的商户号，需先申请接收合单支付权限，详细参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015764779.md)。
 
-`combine_appid`：公众账号ID，合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细参考：[快速开始-步骤4和5](https://pay.weixin.qq.com/doc/v3/merchant/4015764779.md)。
+`combine_appid`：公众账号ID，合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细参考：[开发接入准备-步骤4和5](https://pay.weixin.qq.com/doc/v3/merchant/4015764779.md)。
 
 `time_expire`：支付结束时间。若传递该参数，则用户只能在订单设置的支付结束时间 `time_expire` 之前进行支付，超过支付结束时间后，用户支付将收到："订单已超过商户设置的最晚支付成功时间，请重新发起支付"的提示，商户需对订单进行关单处理。若不传该参数，默认订单支付有效期为7天，用户可在7天内进行支付，超出7天，订单将被关闭。
 
```

### 常见问题
- ID: `4013421369`
- 路径: Native合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4013421369.md
- 更新时间变更: 2025-08-06 01:36:44 -> 2026-05-20 09:55:27
- 本地文件: `pages/4013421369.md`

```diff
--- old.md
+++ new.md
@@ -24,7 +24,7 @@
 
 ## Q：普通商户模式的合单支付子单列表可以既有普通商户又有特约商户么？
 
-A：普通商户模式的子单列表支持普通商户和特约商户，且需要开通接收合单的权限，参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
+A：普通商户模式的子单列表支持普通商户和特约商户，且需要开通接收合单的权限，参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
 
 注意：小微类型的主体商户号不支持。
 
@@ -50,7 +50,7 @@
 
 ## Q：Native合单支付下单返回报错"appid和mch\_id不匹配，请检查后再试"
 
-A：合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细请参考[快速开始-步骤4~5](https://pay.weixin.qq.com/doc/v3/merchant/4015764779.md)。
+A：合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细请参考[开发接入准备-步骤4~5](https://pay.weixin.qq.com/doc/v3/merchant/4015764779.md)。
 
 ## Q：长按识别Native合单支付二维码返回：该商户暂不支持通过长按识别二维码完成支付。
 
```

### 开发接入准备
- ID: `4015765029`
- 路径: 小程序合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4015765029.md
- 更新时间变更: 2025-08-06 01:36:42 -> 2026-05-20 08:28:58
- 本地文件: `pages/4015765029.md`

```diff
--- old.md
+++ new.md
@@ -4,7 +4,7 @@
 
 1、阅读[产品介绍文档](https://pay.weixin.qq.com/doc/v3/merchant/4012077589.md)，了解小程序合单支付产品特性；
 
-2、合单发起方商户与所有子单参与方商户参考[小程序支付-快速开始-步骤1~6](https://pay.weixin.qq.com/doc/v3/merchant/4015459512.md)指引开通小程序支付权限（小程序支付、JSAPI支付共用一个权限）；
+2、合单发起方商户与所有子单参与方商户参考[小程序支付-开发接入准备-步骤1~6](https://pay.weixin.qq.com/doc/v3/merchant/4015459512.md)指引开通小程序支付权限（小程序支付、JSAPI支付共用一个权限）；
 
 3、合单发起方商户联系对接的运营人员申请合单支付权限（为合单发起方商户号申请发起合单权限，为所有子单参与方商户号申请接收合单权限）；
 
```

### 开发指引
- ID: `4012079115`
- 路径: 小程序合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012079115.md
- 更新时间变更: 2025-08-06 01:36:42 -> 2026-05-20 09:56:45
- 本地文件: `pages/4012079115.md`

```diff
--- old.md
+++ new.md
@@ -19,11 +19,11 @@
 
 下单接口关键参数说明：
 
-`combine_mchid`：合单发起方的商户号，需先申请发起合单支付权限，详细参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015765029.md)。
+`combine_mchid`：合单发起方的商户号，需先申请发起合单支付权限，详细参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015765029.md)。
 
-`sub_order.mchid`：子单参与方的商户号，需先申请接收合单支付权限，详细参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015765029.md)。
+`sub_order.mchid`：子单参与方的商户号，需先申请接收合单支付权限，详细参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4015765029.md)。
 
-`combine_appid`：公众账号ID，合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细参考：[快速开始-步骤4和5](https://pay.weixin.qq.com/doc/v3/merchant/4015765029.md)。
+`combine_appid`：公众账号ID，合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细参考：[开发接入准备-步骤4和5](https://pay.weixin.qq.com/doc/v3/merchant/4015765029.md)。
 
 `time_expire`：支付结束时间。若传递该参数，则用户只能在订单设置的支付结束时间 `time_expire` 之前进行支付，超过支付结束时间后，用户支付将收到："订单已超过商户设置的最晚支付成功时间，请重新发起支付"的提示，商户需对订单进行关单处理。若不传该参数，默认订单支付有效期为7天，用户可在7天内进行支付，超出7天，订单将被关闭。
 
```

### 常见问题
- ID: `4013421468`
- 路径: 小程序合单支付
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4013421468.md
- 更新时间变更: 2025-08-06 01:36:42 -> 2026-05-20 09:57:11
- 本地文件: `pages/4013421468.md`

```diff
--- old.md
+++ new.md
@@ -24,7 +24,7 @@
 
 ## Q：普通商户模式的合单支付子单列表可以既有普通商户又有特约商户么？
 
-A：普通商户模式的子单列表支持普通商户和特约商户，且需要开通接收合单的权限，参考：[快速开始-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
+A：普通商户模式的子单列表支持普通商户和特约商户，且需要开通接收合单的权限，参考：[开发接入准备-步骤3](https://pay.weixin.qq.com/doc/v3/merchant/4013420660.md)。
 
 注意：小微类型的主体商户号不支持。
 
@@ -50,7 +50,7 @@
 
 ## Q：小程序合单支付下单返回报错"appid和mch\_id不匹配，请检查后再试"
 
-A：合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细请参考[快速开始-步骤4~5](https://pay.weixin.qq.com/doc/v3/merchant/4015765029.md)。
+A：合单发起方商户号 `combine_mchid` 和子单参与方商户号 `sub_order.mchid` 都需要绑定同一个 `combine_appid`，详细请参考[开发接入准备-步骤4~5](https://pay.weixin.qq.com/doc/v3/merchant/4015765029.md)。
 
 ## Q：小程序合单下单返回报错"appid与openid不匹配"
 
```

### 常见问题
- ID: `4013071254`
- 路径: 下载账单
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4013071254.md
- 更新时间变更: 2026-05-09 08:56:14 -> 2026-05-19 07:37:47
- 本地文件: `pages/4013071254.md`

```diff
--- old.md
+++ new.md
@@ -39,6 +39,10 @@
 
 A：包含，对账单是以商户号维度来生成的。
 
-### Q：子商户号能否调用服务商接口查询交易订单？
+## Q：子商户号能否调用服务商接口查询交易订单？
 
 A：​ 不支持。该接口仅限服务商调用，服务商可以调用这个接口查询名下子商户的所有交易账单，子商户无权限调用。
+
+## Q：资金账单中是否包含品牌红包产品的交易明细？
+
+A：不包含。资金账单仅展示品牌红包的批次记录，不展示具体的明细单记录。
```

### 开发接入准备
- ID: `4012067989`
- 路径: 分账
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012067989.md
- 更新时间变更: 2024-10-25 08:20:30 -> 2026-05-19 08:32:51
- 本地文件: `pages/4012067989.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 常见问题
- ID: `4014547102`
- 路径: 分账
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4014547102.md
- 更新时间变更: 2026-04-28 06:56:13 -> 2026-05-21 03:14:53
- 本地文件: `pages/4014547102.md`

```diff
--- old.md
+++ new.md
@@ -70,7 +70,7 @@
 
 A：请按照以下几点排查：
 
-1、未开通分账权限，请开通后再调用分账接口，可参考[接入前准备](https://pay.weixin.qq.com/doc/v3/merchant/4012067989.md)
+1、未开通分账权限，请开通后再调用分账接口，可参考[开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4012067989.md)
 
 2、请求参数错误
 
```

### 产品介绍
- ID: `4012711988`
- 路径: 商家转账
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012711988.md
- 更新时间变更: 2026-05-12 02:40:42 -> 2026-05-21 02:45:06
- 本地文件: `pages/4012711988.md`

```diff
--- old.md
+++ new.md
@@ -104,7 +104,7 @@
 
 ### 2.1 开通商家转账
 
-- 申请权限：按照[权限申请](https://pay.weixin.qq.com/doc/v3/merchant/4013740645.md)开通产品权限
+- 申请权限：按照[开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4013740645.md)开通产品权限
 
 - 接入产品能力：按照[开发指引](https://pay.weixin.qq.com/doc/v3/merchant/4012715211.md)进行系统开发
 
```

### 开发接入准备
- ID: `4013740645`
- 路径: 商家转账
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4013740645.md
- 更新时间变更: 2026-04-30 02:47:37 -> 2026-05-20 02:31:49
- 本地文件: `pages/4013740645.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 常见问题
- ID: `4013778940`
- 路径: 商家转账
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4013778940.md
- 更新时间变更: 2026-02-06 03:25:07 -> 2026-05-19 07:42:20
- 本地文件: `pages/4013778940.md`

```diff
--- old.md
+++ new.md
@@ -118,6 +118,10 @@
 
 A：微信不会主动推送消息，需要商户[调起用户确认收款](https://pay.weixin.qq.com/doc/v3/merchant/4012716430.md)页面。
 
+### Q：调用 [发起免确认收款授权](https://pay.weixin.qq.com/doc/v3/merchant/4015901167.md) 接口报错 INVALID\_REQUEST，提示“用户在当前场景下的授权数量达到限制，不支持发起授权”，应如何解决？
+
+A：请复用已有授权单号。若用户此前未完成授权流程，请勿创建新的授权单号，直接使用原授权单号重新拉起授权即可。
+
 ### 前端报错
 
 #### Q：调起用户确认收款提示"package\_info信息有误，请返回联系商家处理"
@@ -233,3 +237,15 @@
 2、openid必须正确；
 
 3、账号无异常（如冻结、违规封禁）。
+
+#### Q：升级商家转账产品后，用户确认收款环节是否为必选流程？
+
+A：取决于所选模式。若采用用户授权免确认模式，首次转账前完成授权或确认收款时完成授权后，后续转账可直接发起，无需再次拉起确认收款界面。
+
+#### Q：调用 [撤销转账](https://pay.weixin.qq.com/doc/v3/merchant/4012716458.md) 接口时返回错误码 FREQUENCY\_LIMIT\_EXCEED，该接口的限频是多少？
+
+A：接口限频为 20 次/秒。
+
+### Q：商家转账免确认授权场景下，同一用户使用不同单号是否可以多次授权，最终授权ID是否以最新为准？
+
+A：同一用户仅需授权一次，请勿更换授权单号进行重复授权。
```

### 开发接入准备
- ID: `4012587112`
- 路径: 微信支付分
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012587112.md
- 更新时间变更: 2024-12-09 10:14:08 -> 2026-05-19 07:59:56
- 本地文件: `pages/4012587112.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 开发接入准备
- ID: `4012077356`
- 路径: 微信支付分停车服务
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012077356.md
- 更新时间变更: 2025-03-21 07:40:24 -> 2026-05-19 08:00:39
- 本地文件: `pages/4012077356.md`

```diff
--- old.md
+++ new.md
@@ -45,7 +45,7 @@
 
 - 在该模式下，存在用户账户资金不足以完成支付服务的情况。垫资能力可保证商户实收款项，避免出现坏账。
 
-- 微信支付分停车相关产品介绍，详见[产品介绍](https://pay.weixin.qq.com/doc/v3/merchant/4012077223.md)
+- 微信支付分停车相关产品介绍，详见[产品介绍](https://pay.weixin.qq.com/docs/merchant/products/wexin-pay-score-parking/introduction.html)
 
 
 #### 4.1.1. 确认是否符合申请要求
```

### 开发接入准备
- ID: `4012084133`
- 路径: 代金券
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012084133.md
- 更新时间变更: 2024-11-21 02:19:59 -> 2026-05-19 08:07:01
- 本地文件: `pages/4012084133.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 开发接入准备
- ID: `4012063130`
- 路径: 委托营销
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012063130.md
- 更新时间变更: 2024-11-18 09:25:34 -> 2026-05-19 08:10:42
- 本地文件: `pages/4012063130.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 开发接入准备
- ID: `4012064330`
- 路径: 支付有礼
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012064330.md
- 更新时间变更: 2024-10-25 08:20:30 -> 2026-05-19 08:10:58
- 本地文件: `pages/4012064330.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 开发接入准备
- ID: `4012064734`
- 路径: 小程序发券插件
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012064734.md
- 更新时间变更: 2024-10-25 08:20:30 -> 2026-05-19 08:11:14
- 本地文件: `pages/4012064734.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 开发接入准备
- ID: `4012067883`
- 路径: H5发券
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012067883.md
- 更新时间变更: 2024-10-25 08:20:30 -> 2026-05-19 08:11:29
- 本地文件: `pages/4012067883.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 开发接入准备
- ID: `4012068068`
- 路径: 智慧商圈
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012068068.md
- 更新时间变更: 2024-10-25 08:20:30 -> 2026-05-19 08:12:05
- 本地文件: `pages/4012068068.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 开发指引
- ID: `4012068086`
- 路径: 智慧商圈
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012068086.md
- 更新时间变更: 2025-03-21 07:44:24 -> 2026-05-21 02:56:02
- 本地文件: `pages/4012068086.md`

```diff
--- old.md
+++ new.md
@@ -1,6 +1,6 @@
 ## 1. 接口规则
 
-为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/doc/v3/merchant/4012081606.md)。
+为了在保证支付安全的前提下，带给商户简单、一致且易用的开发体验，我们推出了全新的微信支付APIv3接口。该版本API的具体规则请参考[APIv3接口规则](https://pay.weixin.qq.com/docs/merchant/development/interface-rules/introduction.html)。
 
 ## 2. 开发准备
 
@@ -16,7 +16,7 @@
 
 重点步骤说明：
 
-智慧商圈接入前需先邮件申请接入权限，申请发放具体可查看[接入前准备](https://pay.weixin.qq.com/doc/v3/merchant/4012068068.md)，小程序插件可参考：[小程序插件开发文档](https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/)。
+智慧商圈接入前需先邮件申请接入权限，申请发放具体可查看[开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4012068068.md)，小程序插件可参考：[小程序插件开发文档](https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/)。
 
 步骤10[商圈会员场内支付结果通知](https://pay.weixin.qq.com/doc/v3/merchant/4012285856.md)（已开通积分功能的用户，在场内发生交易时，会将交易信息返回至开通时提交的回调地址）。
 
```

### 常见问题
- ID: `4016111728`
- 路径: 智慧商圈
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4016111728.md
- 更新时间变更: 2026-03-18 09:13:35 -> 2026-05-19 07:42:04
- 本地文件: `pages/4016111728.md`

```diff
--- old.md
+++ new.md
@@ -204,3 +204,15 @@
 商圈插件常见错误码请查看：[【企微文档】商圈插件常见错误码自查指南](https://doc.weixin.qq.com/sheet/e3_AGUA3QZvAEsCNrUG2g5WsQketTJUz?scode=AJEAIQdfAAo3Y1HPtaAQYADwaSAC4&tab=000001)
 
 如要咨询商圈问题请发邮件到：zhsq@tencent.com
+
+#### Q：智慧商圈小程序进入时，是否默认自动获取用户地理位置信息？
+
+A：不支持默认获取。需在代码内主动调用 wx.getLocation() 接口，并在页面加载时触发该函数以实现获取。
+
+#### Q：已圈店的商家微信支付商户号可以通过哪里导出？
+
+A：支持在“智慧商圈-门店管理”中一键导出已圈店信息，导出文件包含对应商户号。操作路径请参考《[圈店工具使用文档](https://docs.qq.com/doc/DYllDRXZFYld2TW12)》。
+
+#### Q：接口返回“请求失败，商户号下暂无商圈”，这是什么原因？​
+
+A：​ 该错误表示当前调用的商户号（mch\_id）尚未在系统中配置或绑定任何商圈信息。请先在商户后台完成商圈入驻或绑定操作后，再重新发起请求。
```

### 产品介绍
- ID: `4012061135`
- 路径: 支付即服务
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012061135.md
- 更新时间变更: 2024-09-23 02:17:59 -> 2026-05-21 02:57:16
- 本地文件: `pages/4012061135.md`

```diff
--- old.md
+++ new.md
@@ -55,7 +55,7 @@
 
 ![](https://gtimg.wechatpay.cn/resource/xres/mmpaydoc/static/img/0937fd136bbf0809341002302267945d.jpeg)
 
-1. 商家开通支付即服务，并进行产品相关设置，产品相关配置流程参见《[权限配置](https://pay.weixin.qq.com/doc/v3/merchant/4012061536.md)》；
+1. 商家开通支付即服务，并进行产品相关设置，产品相关配置流程参见《[开发接入准备](https://pay.weixin.qq.com/doc/v3/merchant/4012061536.md)》；
 
 2. 注册服务人员，由微信支付为每一位注册成功的服务人员生成一个服务人员ID；
 
```

### 开发接入准备
- ID: `4012061536`
- 路径: 支付即服务
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012061536.md
- 更新时间变更: 2025-03-21 07:46:11 -> 2026-05-19 08:12:18
- 本地文件: `pages/4012061536.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 开发接入准备
- ID: `4012068478`
- 路径: 消费者投诉2.0
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012068478.md
- 更新时间变更: 2024-10-25 08:20:30 -> 2026-05-19 08:33:15
- 本地文件: `pages/4012068478.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 常见问题
- ID: `4016111664`
- 路径: 消费者投诉2.0
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4016111664.md
- 更新时间变更: 2026-05-14 06:06:39 -> 2026-05-19 07:42:36
- 本地文件: `pages/4016111664.md`

```diff
--- old.md
+++ new.md
@@ -77,3 +77,11 @@
 #### Q：当投诉单状态为“待处理”时，调用“反馈处理完成”接口是否会失败？
 
 A：是的，当投诉单状态为“待处理”时，无法调用反馈处理完成接口。
+
+#### Q：调用 [回复投诉](https://pay.weixin.qq.com/doc/v3/merchant/4012467254.md) 接口时返回“当前投诉单已达单次回复上限，请等待用户回复”，具体限制规则是什么？
+
+A：单次限制：在用户下次回复前，商家最多可回复 20 条。累计限制：单笔投诉单双方消息总量达到 2000 条后，将触发总a上限。
+
+#### Q：商户平台展示的“升级投诉单数”是否仅统计用户当日发起投诉且当日升级的工单量？
+
+A：不是。该数据指当日发起升级操作的投诉单量，但涉及的投诉单时间范围包含当日及历史存量。
```

### 产品介绍
- ID: `4012153196`
- 路径: 微信支付公钥
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012153196.md
- 更新时间变更: 2024-11-20 06:52:56 -> 2026-05-20 02:34:36
- 本地文件: `pages/4012153196.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

### 产品介绍
- ID: `4012068814`
- 路径: 平台证书
- URL: https://pay.weixin.qq.com/doc/v3/merchant/4012068814.md
- 更新时间变更: 2024-11-29 09:44:43 -> 2026-05-20 03:19:57
- 本地文件: `pages/4012068814.md`

```diff
无正文差异，可能仅更新时间发生变化。
```

## 附录：所有页面清单

<details>
<summary>点击查看全部 520 个页面</summary>

| 序号 | 标题（链接） | ID | 更新时间 | 完整路径 |
|------|-------------|----|----------|----------|
| 1 | [基础支付接入Skill](pages/4019638116.md) | `4019638116` | 2026-04-09 03:13:23 | Skills |
| 2 | [Go](pages/4015119334.md) | `4015119334` | 2025-05-29 03:20:46 | 示例代码 |
| 3 | [Java](pages/4014931831.md) | `4014931831` | 2025-05-28 02:22:00 | 示例代码 |
| 4 | [付款码支付（V2）](pages/4012647301.md) | `4012647301` | 2025-04-25 07:32:13 | 付款码支付（V2） |
| 5 | [刷脸支付](pages/4012647399.md) | `4012647399` | 2024-10-08 06:20:39 | 刷脸支付 |
| 6 | [产品介绍](pages/4012062524.md) | `4012062524` | 2025-07-15 03:13:07 | JSAPI支付 |
| 7 | [开发接入准备](pages/4015423216.md) | `4015423216` | 2026-05-21 07:03:41 | JSAPI支付 |
| 8 | [开发指引](pages/4012791870.md) | `4012791870` | 2026-02-28 03:34:36 | JSAPI支付 |
| 9 | [常见问题](pages/4012791869.md) | `4012791869` | 2026-03-11 09:00:48 | JSAPI支付 |
| 10 | [JSAPI/小程序下单](pages/4012791856.md) | `4012791856` | 2025-03-31 06:15:06 | JSAPI支付 > API列表 |
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
| 28 | [开发接入准备](pages/4015478291.md) | `4015478291` | 2026-05-19 07:50:37 | APP支付 |
| 29 | [开发指引](pages/4013070176.md) | `4013070176` | 2026-01-16 03:57:24 | APP支付 |
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
| 49 | [开发接入准备](pages/4015614193.md) | `4015614193` | 2026-05-19 07:51:45 | H5支付 |
| 50 | [开发指引](pages/4012791831.md) | `4012791831` | 2025-07-17 08:07:32 | H5支付 |
| 51 | [常见问题](pages/4012791845.md) | `4012791845` | 2025-10-15 08:12:25 | H5支付 |
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
| 66 | [配置H5支付域名](pages/4013287193.md) | `4013287193` | 2026-01-09 08:20:57 | H5支付 > 附录 |
| 67 | [H5收银台适老化字体规范](pages/4013317672.md) | `4013317672` | 2024-12-18 07:41:18 | H5支付 > 附录 |
| 68 | [各主体可申请的基础支付权限列表](pages/4015616699.md) | `4015616699` | 2025-07-17 07:54:58 | H5支付 > 附录 |
| 69 | [申请H5支付权限指引](pages/4012791841.md) | `4012791841` | 2025-07-17 08:07:32 | H5支付 > 附录 |
| 70 | [获取用户ip指引](pages/4018677409.md) | `4018677409` | 2026-03-13 07:56:04 | H5支付 > 附录 |
| 71 | [产品介绍](pages/4012791874.md) | `4012791874` | 2025-07-17 08:07:28 | Native支付 |
| 72 | [开发接入准备](pages/4015614538.md) | `4015614538` | 2026-05-19 07:52:00 | Native支付 |
| 73 | [开发指引](pages/4012791891.md) | `4012791891` | 2025-07-17 08:07:28 | Native支付 |
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
| 92 | [开发接入准备](pages/4015459512.md) | `4015459512` | 2026-05-19 07:52:18 | 小程序支付 |
| 93 | [开发指引](pages/4012791911.md) | `4012791911` | 2026-02-28 08:03:41 | 小程序支付 |
| 94 | [常见问题](pages/4012791910.md) | `4012791910` | 2026-01-23 02:53:52 | 小程序支付 |
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
| 112 | [开发接入准备](pages/4015764634.md) | `4015764634` | 2026-05-21 08:24:21 | JSAPI合单支付 |
| 113 | [开发指引](pages/4012078634.md) | `4012078634` | 2026-05-21 08:24:21 | JSAPI合单支付 |
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
| 129 | [开发接入准备](pages/4013420660.md) | `4013420660` | 2026-05-20 08:26:06 | APP合单支付 |
| 130 | [开发指引](pages/4012077667.md) | `4012077667` | 2026-05-20 08:31:11 | APP合单支付 |
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
| 145 | [开发接入准备](pages/4015764448.md) | `4015764448` | 2026-05-20 08:27:15 | H5合单支付 |
| 146 | [开发指引](pages/4012078230.md) | `4012078230` | 2026-05-20 09:37:25 | H5合单支付 |
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
| 161 | [开发接入准备](pages/4015764779.md) | `4015764779` | 2026-05-20 08:28:07 | Native合单支付 |
| 162 | [开发指引](pages/4012078926.md) | `4012078926` | 2026-05-20 09:52:24 | Native合单支付 |
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
| 177 | [开发接入准备](pages/4015765029.md) | `4015765029` | 2026-05-20 08:28:58 | 小程序合单支付 |
| 178 | [开发指引](pages/4012079115.md) | `4012079115` | 2026-05-20 09:56:45 | 小程序合单支付 |
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
| 192 | [产品介绍](pages/4016824672.md) | `4016824672` | 2026-05-14 08:43:58 | 医保支付 |
| 193 | [开发接入准备](pages/4016824684.md) | `4016824684` | 2026-05-20 03:54:19 | 医保支付 |
| 194 | [开发指引](pages/4016824681.md) | `4016824681` | 2026-05-20 07:06:42 | 医保支付 |
| 195 | [医保自费混合收款下单](pages/4016781466.md) | `4016781466` | 2025-12-04 08:22:16 | 医保支付 > API列表 > 医保自费混合订单 |
| 196 | [使用医保自费混合订单号查看下单结果](pages/4016781479.md) | `4016781479` | 2025-12-04 08:22:16 | 医保支付 > API列表 > 医保自费混合订单 |
| 197 | [使用商户订单号查看下单结果](pages/4016781490.md) | `4016781490` | 2025-12-04 08:22:16 | 医保支付 > API列表 > 医保自费混合订单 |
| 198 | [小程序调起医保自费混合支付](pages/4016781545.md) | `4016781545` | 2025-12-04 08:23:06 | 医保支付 > API列表 > 医保自费混合订单 |
| 199 | [JSAPI调起医保自费混合支付](pages/4016781549.md) | `4016781549` | 2025-12-04 08:23:19 | 医保支付 > API列表 > 医保自费混合订单 |
| 200 | [医保混合收款成功通知](pages/4016781554.md) | `4016781554` | 2025-12-04 08:23:33 | 医保支付 > API列表 > 医保自费混合订单 |
| 201 | [医保退款通知](pages/4016781561.md) | `4016781561` | 2025-12-04 08:17:01 | 医保支付 > API列表 > 医保退款 |
| 202 | [报错排查指引](pages/4020401138.md) | `4020401138` | 2026-05-14 09:21:09 | 医保支付 > 常见问题 |
| 203 | [业务&接口规则类问题](pages/4017415831.md) | `4017415831` | 2026-05-14 09:21:10 | 医保支付 > 常见问题 |
| 204 | [申请医保支付权限](pages/4016824675.md) | `4016824675` | 2026-05-20 03:23:21 | 医保支付 > 附录 |
| 205 | [接入医保亲情付指引](pages/4016975471.md) | `4016975471` | 2026-05-20 03:23:51 | 医保支付 > 附录 |
| 206 | [产品介绍](pages/4013071001.md) | `4013071001` | 2025-06-27 09:49:14 | 订单退款 |
| 207 | [开发指引](pages/4013071031.md) | `4013071031` | 2025-06-20 04:11:54 | 订单退款 |
| 208 | [常见问题](pages/4013071200.md) | `4013071200` | 2026-05-09 08:56:42 | 订单退款 |
| 209 | [业务示例代码](pages/4015217336.md) | `4015217336` | 2025-09-03 03:02:18 | 订单退款 |
| 210 | [申请退款](pages/4013071036.md) | `4013071036` | 2025-01-09 03:18:26 | 订单退款 > API列表 |
| 211 | [查询单笔退款（通过商户退款单号）](pages/4013071041.md) | `4013071041` | 2025-01-09 03:19:47 | 订单退款 > API列表 |
| 212 | [发起异常退款](pages/4013071193.md) | `4013071193` | 2024-12-30 07:50:09 | 订单退款 > API列表 |
| 213 | [退款结果通知](pages/4013071196.md) | `4013071196` | 2025-01-02 08:01:31 | 订单退款 > API列表 |
| 214 | [微信支付退款最佳实践](pages/4014959631.md) | `4014959631` | 2025-09-25 02:50:06 | 订单退款 > 附录 |
| 215 | [产品介绍](pages/4013071215.md) | `4013071215` | 2025-04-24 04:25:36 | 下载账单 |
| 216 | [开发指引](pages/4013071218.md) | `4013071218` | 2024-11-25 10:04:01 | 下载账单 |
| 217 | [业务示例代码](pages/4015945131.md) | `4015945131` | 2025-12-03 04:00:41 | 下载账单 |
| 218 | [常见问题](pages/4013071254.md) | `4013071254` | 2026-05-19 07:37:47 | 下载账单 |
| 219 | [申请交易账单](pages/4013071227.md) | `4013071227` | 2025-01-10 01:36:34 | 下载账单 > API列表 |
| 220 | [申请资金账单](pages/4013071235.md) | `4013071235` | 2025-01-09 03:34:15 | 下载账单 > API列表 |
| 221 | [下载账单](pages/4013071238.md) | `4013071238` | 2024-11-25 10:02:55 | 下载账单 > API列表 |
| 222 | [交易账单详细说明](pages/4013071246.md) | `4013071246` | 2026-01-16 03:52:29 | 下载账单 > 附录 |
| 223 | [资金账单详细说明](pages/4013071249.md) | `4013071249` | 2024-11-25 10:03:56 | 下载账单 > 附录 |
| 224 | [下载账单操作指引](pages/4013071252.md) | `4013071252` | 2024-11-25 10:03:53 | 下载账单 > 附录 |
| 225 | [产品介绍](pages/4012067962.md) | `4012067962` | 2025-05-13 02:17:45 | 分账 |
| 226 | [开发接入准备](pages/4012067989.md) | `4012067989` | 2026-05-19 08:32:51 | 分账 |
| 227 | [开发指引](pages/4012068033.md) | `4012068033` | 2025-08-14 02:20:08 | 分账 |
| 228 | [常见问题](pages/4014547102.md) | `4014547102` | 2026-05-21 03:14:53 | 分账 |
| 229 | [请求分账](pages/4012524936.md) | `4012524936` | 2025-09-29 01:57:06 | 分账 > API列表 |
| 230 | [查询分账结果](pages/4012525210.md) | `4012525210` | 2025-09-29 02:00:15 | 分账 > API列表 |
| 231 | [请求分账回退](pages/4012525287.md) | `4012525287` | 2025-09-29 04:02:15 | 分账 > API列表 |
| 232 | [查询分账回退结果](pages/4012526279.md) | `4012526279` | 2025-09-29 03:55:30 | 分账 > API列表 |
| 233 | [解冻剩余资金](pages/4012526374.md) | `4012526374` | 2025-09-29 03:55:05 | 分账 > API列表 |
| 234 | [查询剩余待分金额](pages/4012457939.md) | `4012457939` | 2025-09-29 03:54:33 | 分账 > API列表 |
| 235 | [添加分账接收方](pages/4012528995.md) | `4012528995` | 2025-09-29 03:53:57 | 分账 > API列表 |
| 236 | [删除分账接收方](pages/4012529590.md) | `4012529590` | 2025-09-29 03:52:35 | 分账 > API列表 |
| 237 | [分账动态通知](pages/4012289679.md) | `4012289679` | 2025-02-19 03:56:03 | 分账 > API列表 |
| 238 | [申请分账账单](pages/4012529628.md) | `4012529628` | 2025-09-29 03:52:05 | 分账 > API列表 |
| 239 | [下载账单](pages/4012289690.md) | `4012289690` | 2024-12-18 03:02:33 | 分账 > API列表 |
| 240 | [分账失败处理指引](pages/4015505684.md) | `4015505684` | 2025-07-04 03:41:52 | 分账 > 附录 |
| 241 | [产品介绍](pages/4012711988.md) | `4012711988` | 2026-05-21 02:45:06 | 商家转账 |
| 242 | [开发接入准备](pages/4013740645.md) | `4013740645` | 2026-05-20 02:31:49 | 商家转账 |
| 243 | [开发指引](pages/4012715211.md) | `4012715211` | 2026-05-07 08:19:54 | 商家转账 |
| 244 | [业务示例代码](pages/4018940876.md) | `4018940876` | 2026-04-23 09:22:55 | 商家转账 |
| 245 | [常见问题](pages/4013778940.md) | `4013778940` | 2026-05-19 07:42:20 | 商家转账 |
| 246 | [发起转账](pages/4012716434.md) | `4012716434` | 2025-03-21 02:52:14 | 商家转账 > API列表 > 发起转账 |
| 247 | [JSAPI调起用户确认收款](pages/4012716430.md) | `4012716430` | 2025-03-07 08:37:28 | 商家转账 > API列表 > 发起转账 |
| 248 | [撤销转账](pages/4012716458.md) | `4012716458` | 2025-03-18 03:21:03 | 商家转账 > API列表 > 发起转账 |
| 249 | [商户单号查询转账单](pages/4012716437.md) | `4012716437` | 2025-03-21 02:52:25 | 商家转账 > API列表 > 发起转账 |
| 250 | [微信单号查询转账单](pages/4012716457.md) | `4012716457` | 2025-03-21 02:52:21 | 商家转账 > API列表 > 发起转账 |
| 251 | [商家转账回调通知](pages/4012712115.md) | `4012712115` | 2025-03-07 10:05:02 | 商家转账 > API列表 > 发起转账 |
| 252 | [Android](pages/4012719576.md) | `4012719576` | 2025-03-07 08:37:15 | 商家转账 > API列表 > 发起转账 > APP调起用户确认收款 |
| 253 | [iOS](pages/4012719578.md) | `4012719578` | 2025-03-07 08:37:06 | 商家转账 > API列表 > 发起转账 > APP调起用户确认收款 |
| 254 | [鸿蒙](pages/4019670774.md) | `4019670774` | 2026-04-14 08:28:51 | 商家转账 > API列表 > 发起转账 > APP调起用户确认收款 |
| 255 | [商户单号申请电子回单](pages/4012716452.md) | `4012716452` | 2025-03-21 02:51:55 | 商家转账 > API列表 > 获取电子回单 |
| 256 | [商户单号查询电子回单](pages/4012716436.md) | `4012716436` | 2025-03-21 02:52:17 | 商家转账 > API列表 > 获取电子回单 |
| 257 | [微信单号申请电子回单](pages/4012716456.md) | `4012716456` | 2025-03-21 02:50:21 | 商家转账 > API列表 > 获取电子回单 |
| 258 | [微信单号查询电子回单](pages/4012716455.md) | `4012716455` | 2025-03-21 02:47:21 | 商家转账 > API列表 > 获取电子回单 |
| 259 | [下载电子回单](pages/4013866774.md) | `4013866774` | 2025-03-10 07:43:13 | 商家转账 > API列表 > 获取电子回单 |
| 260 | [发起转账并完成免确认收款授权](pages/4014399293.md) | `4014399293` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 261 | [发起免确认收款授权](pages/4015901167.md) | `4015901167` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 262 | [JSAPI调起免确认收款授权](pages/4015930512.md) | `4015930512` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 263 | [商户单号查询授权结果](pages/4014399423.md) | `4014399423` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 264 | [用户授权后转账](pages/4014399371.md) | `4014399371` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 265 | [免确认收款授权结果通知](pages/4014512908.md) | `4014512908` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 266 | [解除免确认收款授权](pages/4015653811.md) | `4015653811` | 2026-05-08 02:09:53 | 商家转账 > API列表 > 用户授权免确认模式 |
| 267 | [Android](pages/4020320167.md) | `4020320167` | 2026-05-08 02:23:41 | 商家转账 > API列表 > 用户授权免确认模式 > APP调起用户免确认收款授权 |
| 268 | [iOS](pages/4020320150.md) | `4020320150` | 2026-05-08 02:10:18 | 商家转账 > API列表 > 用户授权免确认模式 > APP调起用户免确认收款授权 |
| 269 | [鸿蒙](pages/4020320137.md) | `4020320137` | 2026-05-08 02:10:04 | 商家转账 > API列表 > 用户授权免确认模式 > APP调起用户免确认收款授权 |
| 270 | [充值](pages/4013747269.md) | `4013747269` | 2025-04-15 02:42:45 | 商家转账 > 附录 |
| 271 | [设置接口安全IP](pages/4013751010.md) | `4013751010` | 2026-01-15 08:16:29 | 商家转账 > 附录 |
| 272 | [设置转账额度](pages/4013747667.md) | `4013747667` | 2026-05-08 02:58:10 | 商家转账 > 附录 |
| 273 | [获取账单和电子回单](pages/4013748430.md) | `4013748430` | 2025-02-26 11:48:22 | 商家转账 > 附录 |
| 274 | [订单失败原因说明](pages/4013774966.md) | `4013774966` | 2025-04-15 02:42:41 | 商家转账 > 附录 |
| 275 | [商家转账到零钱升级说明](pages/4015273741.md) | `4015273741` | 2025-09-04 09:39:27 | 商家转账 > 附录 |
| 276 | [现金营销](pages/4013774588.md) | `4013774588` | 2025-07-15 01:38:23 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 277 | [企业赔付](pages/4013774589.md) | `4013774589` | 2025-07-15 01:38:18 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 278 | [佣金报酬](pages/4013774590.md) | `4013774590` | 2025-07-15 01:38:22 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 279 | [采购货款](pages/4013774591.md) | `4013774591` | 2025-07-15 01:38:16 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 280 | [二手回收](pages/4013774592.md) | `4013774592` | 2025-07-15 01:38:21 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 281 | [公益补助](pages/4013774593.md) | `4013774593` | 2025-07-15 01:38:19 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 282 | [行政补贴](pages/4013774594.md) | `4013774594` | 2025-07-15 01:38:14 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 283 | [保险理赔](pages/4013774595.md) | `4013774595` | 2026-02-05 07:23:07 | 商家转账 > 附录 > 转账场景报备信息字段传参说明 |
| 284 | [产品介绍](pages/4012587050.md) | `4012587050` | 2024-12-09 09:50:51 | 微信支付分 |
| 285 | [开发接入准备](pages/4012587112.md) | `4012587112` | 2026-05-19 07:59:56 | 微信支付分 |
| 286 | [开发指引](pages/4012587166.md) | `4012587166` | 2026-03-09 09:24:40 | 微信支付分 |
| 287 | [常见问题](pages/4012587200.md) | `4012587200` | 2026-05-09 08:57:58 | 微信支付分 |
| 288 | [创建支付分订单](pages/4012587900.md) | `4012587900` | 2025-03-06 08:16:47 | 微信支付分 > API列表 |
| 289 | [查询支付分订单](pages/4012587902.md) | `4012587902` | 2024-12-10 09:27:51 | 微信支付分 > API列表 |
| 290 | [取消支付分订单](pages/4012587905.md) | `4012587905` | 2025-02-13 11:37:12 | 微信支付分 > API列表 |
| 291 | [JSAPI调起支付分确认订单页](pages/4012587945.md) | `4012587945` | 2024-11-21 08:08:28 | 微信支付分 > API列表 |
| 292 | [确认订单回调通知](pages/4012587953.md) | `4012587953` | 2024-12-10 09:27:47 | 微信支付分 > API列表 |
| 293 | [完结支付分订单](pages/4012587955.md) | `4012587955` | 2025-03-06 08:16:29 | 微信支付分 > API列表 |
| 294 | [修改订单金额](pages/4012587957.md) | `4012587957` | 2025-03-06 08:16:32 | 微信支付分 > API列表 |
| 295 | [支付成功回调通知](pages/4012587960.md) | `4012587960` | 2025-09-15 08:16:57 | 微信支付分 > API列表 |
| 296 | [同步订单状态](pages/4012587962.md) | `4012587962` | 2024-12-10 09:27:49 | 微信支付分 > API列表 |
| 297 | [申请退款](pages/4012587971.md) | `4012587971` | 2024-12-18 07:43:20 | 微信支付分 > API列表 |
| 298 | [查询退款](pages/4012587973.md) | `4012587973` | 2024-12-05 03:55:51 | 微信支付分 > API列表 |
| 299 | [退款结果通知](pages/4012587976.md) | `4012587976` | 2024-12-10 09:27:50 | 微信支付分 > API列表 |
| 300 | [JSAPI调起支付分订单详情页](pages/4012587983.md) | `4012587983` | 2024-11-14 08:11:51 | 微信支付分 > API列表 |
| 301 | [Android](pages/4012587909.md) | `4012587909` | 2024-11-14 08:12:02 | 微信支付分 > API列表 > APP调起支付分确认订单页 |
| 302 | [iOS](pages/4012596359.md) | `4012596359` | 2024-11-14 08:12:00 | 微信支付分 > API列表 > APP调起支付分确认订单页 |
| 303 | [鸿蒙](pages/4015271805.md) | `4015271805` | 2025-06-18 07:09:37 | 微信支付分 > API列表 > APP调起支付分确认订单页 |
| 304 | [wx.openBusinessView](pages/4012587949.md) | `4012587949` | 2025-03-05 03:45:12 | 微信支付分 > API列表 > 小程序调起支付分确认订单页 |
| 305 | [wx.navigateToMiniProgram（停止新增）](pages/4012596395.md) | `4012596395` | 2025-03-05 03:45:33 | 微信支付分 > API列表 > 小程序调起支付分确认订单页 |
| 306 | [Android](pages/4012587980.md) | `4012587980` | 2024-11-14 08:11:56 | 微信支付分 > API列表 > APP调起支付分订单详情页 |
| 307 | [iOS](pages/4012596423.md) | `4012596423` | 2024-11-14 08:11:55 | 微信支付分 > API列表 > APP调起支付分订单详情页 |
| 308 | [鸿蒙](pages/4015271812.md) | `4015271812` | 2025-06-18 07:09:34 | 微信支付分 > API列表 > APP调起支付分订单详情页 |
| 309 | [wx.openBusinessView](pages/4012587984.md) | `4012587984` | 2024-11-14 08:11:54 | 微信支付分 > API列表 > 小程序调起支付分订单详情页 |
| 310 | [wx.navigateToMiniProgram（停止新增）](pages/4012596449.md) | `4012596449` | 2024-11-14 08:11:53 | 微信支付分 > API列表 > 小程序调起支付分订单详情页 |
| 311 | [支付分合作品牌线上应用规范](pages/4012587220.md) | `4012587220` | 2025-03-21 07:48:14 | 微信支付分 > 附录 |
| 312 | [支付分权限申请邮件模板](pages/4012587233.md) | `4012587233` | 2024-09-25 02:00:56 | 微信支付分 > 附录 |
| 313 | [测试微信号配置指引](pages/4012587248.md) | `4012587248` | 2024-10-10 07:51:05 | 微信支付分 > 附录 |
| 314 | [微信支付分权限类问题排查指南](pages/4018398339.md) | `4018398339` | 2026-03-09 09:24:11 | 微信支付分 > 附录 |
| 315 | [二轮电动车充电桩](pages/4012587259.md) | `4012587259` | 2024-12-09 09:50:39 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 316 | [充电宝](pages/4012587281.md) | `4012587281` | 2024-12-09 09:50:36 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 317 | [共享单车](pages/4012587294.md) | `4012587294` | 2024-12-09 09:50:33 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 318 | [快递行业](pages/4012587304.md) | `4012587304` | 2024-12-09 09:50:31 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 319 | [智慧零售(无人设备)](pages/4012587317.md) | `4012587317` | 2024-12-09 09:50:28 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 320 | [汽车充电桩](pages/4012587347.md) | `4012587347` | 2024-12-09 10:14:12 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 321 | [汽车租赁](pages/4012587354.md) | `4012587354` | 2024-12-09 09:50:24 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 322 | [酒店行业](pages/4012587370.md) | `4012587370` | 2024-12-09 09:50:22 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 323 | [产品介绍](pages/4012077223.md) | `4012077223` | 2025-12-11 08:47:29 | 微信支付分停车服务 |
| 324 | [开发接入准备](pages/4012077356.md) | `4012077356` | 2026-05-19 08:00:39 | 微信支付分停车服务 |
| 325 | [开发指引](pages/4012077649.md) | `4012077649` | 2025-03-21 07:40:10 | 微信支付分停车服务 |
| 326 | [常见问题](pages/4016183517.md) | `4016183517` | 2025-12-12 02:17:07 | 微信支付分停车服务 |
| 327 | [创建停车入场](pages/4012533937.md) | `4012533937` | 2025-02-21 08:25:25 | 微信支付分停车服务 > API列表 > 停车入场 |
| 328 | [停车入场状态变更通知](pages/4012284177.md) | `4012284177` | 2025-02-20 06:14:47 | 微信支付分停车服务 > API列表 > 停车入场 |
| 329 | [查询车牌服务开通信息](pages/4012534043.md) | `4012534043` | 2025-02-21 08:24:47 | 微信支付分停车服务 > API列表 > 服务 |
| 330 | [小程序调起支付分停车服务开通页](pages/4012284186.md) | `4012284186` | 2025-01-14 03:08:49 | 微信支付分停车服务 > API列表 > 服务 |
| 331 | [H5调起微信支付分停车服务开通页](pages/4012284235.md) | `4012284235` | 2024-09-19 07:11:40 | 微信支付分停车服务 > API列表 > 服务 |
| 332 | [App拉起微信支付分停车服务开通页](pages/4012284257.md) | `4012284257` | 2024-09-19 07:11:40 | 微信支付分停车服务 > API列表 > 服务 |
| 333 | [查询订单](pages/4012534308.md) | `4012534308` | 2025-02-21 08:27:22 | 微信支付分停车服务 > API列表 > 扣费受理 |
| 334 | [扣费受理](pages/4012534352.md) | `4012534352` | 2025-03-11 03:04:13 | 微信支付分停车服务 > API列表 > 扣费受理 |
| 335 | [订单支付结果通知](pages/4012284311.md) | `4012284311` | 2025-02-19 03:53:52 | 微信支付分停车服务 > API列表 > 扣费受理 |
| 336 | [微信垫资还款](pages/4012284369.md) | `4012284369` | 2024-08-14 07:16:13 | 微信支付分停车服务 > API列表 > 还款 |
| 337 | [退款申请](pages/4012557131.md) | `4012557131` | 2025-01-09 03:18:26 | 微信支付分停车服务 > API列表 > 退款 |
| 338 | [退款结果通知](pages/4012083103.md) | `4012083103` | 2025-02-19 03:54:15 | 微信支付分停车服务 > API列表 > 退款 |
| 339 | [查询单笔退款（通过商户退款单号）](pages/4012557161.md) | `4012557161` | 2025-01-09 03:19:47 | 微信支付分停车服务 > API列表 > 退款 |
| 340 | [现金红包（V2）](pages/4012647471.md) | `4012647471` | 2025-04-25 08:11:06 | 现金红包（V2） |
| 341 | [产品介绍](pages/4012084079.md) | `4012084079` | 2025-10-14 07:17:46 | 代金券 |
| 342 | [开发接入准备](pages/4012084133.md) | `4012084133` | 2026-05-19 08:07:01 | 代金券 |
| 343 | [开发指引](pages/4012084207.md) | `4012084207` | 2025-08-14 02:19:53 | 代金券 |
| 344 | [常见问题](pages/4015880636.md) | `4015880636` | 2025-10-14 06:41:01 | 代金券 |
| 345 | [业务示例代码](pages/4015894256.md) | `4015894256` | 2026-05-19 08:07:01 | 代金券 |
| 346 | [核销事件回调通知](pages/4012285250.md) | `4012285250` | 2025-02-19 03:51:54 | 代金券 > API列表 |
| 347 | [图片上传（营销专用）](pages/4012557233.md) | `4012557233` | 2024-09-14 09:09:45 | 代金券 > API列表 |
| 348 | [创建代金券批次](pages/4012534633.md) | `4012534633` | 2024-10-31 03:59:23 | 代金券 > API列表 > 批次 |
| 349 | [激活代金券批次](pages/4012460137.md) | `4012460137` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 350 | [暂停代金券批次](pages/4012460305.md) | `4012460305` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 351 | [重启代金券批次](pages/4012460411.md) | `4012460411` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 352 | [条件查询批次列表](pages/4012460489.md) | `4012460489` | 2025-03-25 08:44:54 | 代金券 > API列表 > 批次 |
| 353 | [查询批次详情](pages/4012460564.md) | `4012460564` | 2025-03-25 08:44:53 | 代金券 > API列表 > 批次 |
| 354 | [查询代金券可用商户](pages/4012463358.md) | `4012463358` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 355 | [查询代金券可用单品](pages/4012463442.md) | `4012463442` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 356 | [下载批次退款明细](pages/4012463523.md) | `4012463523` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 357 | [下载批次核销明细](pages/4012463585.md) | `4012463585` | 2024-09-19 11:44:13 | 代金券 > API列表 > 批次 |
| 358 | [根据商户号查用户的券](pages/4012534690.md) | `4012534690` | 2024-09-19 13:18:56 | 代金券 > API列表 > 券 |
| 359 | [发放指定批次的代金券](pages/4012463767.md) | `4012463767` | 2024-09-19 13:18:56 | 代金券 > API列表 > 券 |
| 360 | [查询代金券详情](pages/4012486942.md) | `4012486942` | 2024-09-19 13:18:56 | 代金券 > API列表 > 券 |
| 361 | [查询代金券消息通知地址](pages/4012464070.md) | `4012464070` | 2024-08-28 03:08:05 | 代金券 > API列表 > 消息通知地址 |
| 362 | [设置代金券消息通知地址](pages/4012464198.md) | `4012464198` | 2024-08-28 03:19:30 | 代金券 > API列表 > 消息通知地址 |
| 363 | [产品介绍](pages/4012063104.md) | `4012063104` | 2024-07-23 07:30:20 | 委托营销 |
| 364 | [开发接入准备](pages/4012063130.md) | `4012063130` | 2026-05-19 08:10:42 | 委托营销 |
| 365 | [开发指引](pages/4012063233.md) | `4012063233` | 2025-08-13 08:51:18 | 委托营销 |
| 366 | [建立合作关系](pages/4012380498.md) | `4012380498` | 2024-08-26 03:01:30 | 委托营销 > API列表 |
| 367 | [查询合作关系列表](pages/4012380536.md) | `4012380536` | 2024-09-02 03:15:51 | 委托营销 > API列表 |
| 368 | [产品介绍](pages/4012064295.md) | `4012064295` | 2025-11-11 11:19:33 | 支付有礼 |
| 369 | [开发接入准备](pages/4012064330.md) | `4012064330` | 2026-05-19 08:10:58 | 支付有礼 |
| 370 | [开发指引](pages/4012064366.md) | `4012064366` | 2025-03-27 08:11:44 | 支付有礼 |
| 371 | [图片上传（营销专用）](pages/4012557248.md) | `4012557248` | 2024-09-20 02:59:58 | 支付有礼 > API列表 |
| 372 | [创建全场满额送活动](pages/4012487898.md) | `4012487898` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 373 | [获取活动详情接口](pages/4012487971.md) | `4012487971` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 374 | [获取活动发券商户号](pages/4012466149.md) | `4012466149` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 375 | [获取活动指定商品列表](pages/4012466448.md) | `4012466448` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 376 | [终止活动](pages/4012466523.md) | `4012466523` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 377 | [新增活动发券商户号](pages/4012466671.md) | `4012466671` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 378 | [获取支付有礼活动列表](pages/4012489126.md) | `4012489126` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 379 | [删除活动发券商户号](pages/4012466787.md) | `4012466787` | 2024-09-02 08:05:47 | 支付有礼 > API列表 > 支付有礼活动 |
| 380 | [产品介绍](pages/4012064617.md) | `4012064617` | 2025-03-21 10:25:03 | 小程序发券插件 |
| 381 | [开发接入准备](pages/4012064734.md) | `4012064734` | 2026-05-19 08:11:14 | 小程序发券插件 |
| 382 | [小程序发券插件](pages/4012285674.md) | `4012285674` | 2025-02-19 02:33:35 | 小程序发券插件 > API列表 |
| 383 | [产品介绍](pages/4012067873.md) | `4012067873` | 2025-03-21 07:44:35 | H5发券 |
| 384 | [开发接入准备](pages/4012067883.md) | `4012067883` | 2026-05-19 08:11:29 | H5发券 |
| 385 | [H5发券](pages/4012285783.md) | `4012285783` | 2025-03-21 07:38:14 | H5发券 > API列表 |
| 386 | [产品介绍](pages/4012068030.md) | `4012068030` | 2025-03-21 07:44:27 | 智慧商圈 |
| 387 | [开发接入准备](pages/4012068068.md) | `4012068068` | 2026-05-19 08:12:05 | 智慧商圈 |
| 388 | [开发指引](pages/4012068086.md) | `4012068086` | 2026-05-21 02:56:02 | 智慧商圈 |
| 389 | [常见问题](pages/4016111728.md) | `4016111728` | 2026-05-19 07:42:04 | 智慧商圈 |
| 390 | [商圈会员积分服务授权结果通知](pages/4012285836.md) | `4012285836` | 2025-02-19 03:56:03 | 智慧商圈 > API列表 |
| 391 | [商圈会员场内支付结果通知](pages/4012285856.md) | `4012285856` | 2025-02-19 03:56:03 | 智慧商圈 > API列表 |
| 392 | [商圈会员积分同步](pages/4012534698.md) | `4012534698` | 2024-09-20 09:22:16 | 智慧商圈 > API列表 |
| 393 | [商圈会员场内退款结果通知](pages/4012285869.md) | `4012285869` | 2025-02-19 03:56:03 | 智慧商圈 > API列表 |
| 394 | [商圈会员积分服务授权查询](pages/4012534848.md) | `4012534848` | 2024-09-20 09:22:16 | 智慧商圈 > API列表 |
| 395 | [商圈会员待积分状态查询](pages/4012534994.md) | `4012534994` | 2024-11-27 07:20:28 | 智慧商圈 > API列表 |
| 396 | [商圈会员停车状态同步](pages/4012535502.md) | `4012535502` | 2024-11-27 07:19:43 | 智慧商圈 > API列表 |
| 397 | [产品介绍](pages/4012061135.md) | `4012061135` | 2026-05-21 02:57:16 | 支付即服务 |
| 398 | [开发接入准备](pages/4012061536.md) | `4012061536` | 2026-05-19 08:12:18 | 支付即服务 |
| 399 | [开发指引](pages/4012062997.md) | `4012062997` | 2025-08-13 08:51:10 | 支付即服务 |
| 400 | [常见问题](pages/4016913581.md) | `4016913581` | 2025-12-19 02:14:30 | 支付即服务 |
| 401 | [服务人员查询](pages/4012535123.md) | `4012535123` | 2025-01-08 09:32:31 | 支付即服务 > API列表 |
| 402 | [服务人员注册](pages/4012535138.md) | `4012535138` | 2025-01-09 03:10:17 | 支付即服务 > API列表 |
| 403 | [服务人员更新](pages/4012535160.md) | `4012535160` | 2025-01-09 03:10:19 | 支付即服务 > API列表 |
| 404 | [服务人员分配](pages/4012535161.md) | `4012535161` | 2024-09-20 11:27:00 | 支付即服务 > API列表 |
| 405 | [服务人员称谓申请指引](pages/4012064662.md) | `4012064662` | 2024-07-22 09:19:24 | 支付即服务 > 附录 |
| 406 | [免开发版本操作指引](pages/4012064678.md) | `4012064678` | 2024-09-20 11:37:23 | 支付即服务 > 附录 |
| 407 | [个人微信服务人员注册](pages/4012064695.md) | `4012064695` | 2024-08-01 08:27:41 | 支付即服务 > 附录 |
| 408 | [清关报关（V2）](pages/4012647500.md) | `4012647500` | 2025-04-25 07:53:32 | 清关报关（V2） |
| 409 | [产品介绍](pages/4012068466.md) | `4012068466` | 2025-08-25 10:00:06 | 消费者投诉2.0 |
| 410 | [开发接入准备](pages/4012068478.md) | `4012068478` | 2026-05-19 08:33:15 | 消费者投诉2.0 |
| 411 | [开发指引](pages/4012068499.md) | `4012068499` | 2026-03-24 07:11:09 | 消费者投诉2.0 |
| 412 | [业务示例代码](pages/4015821404.md) | `4015821404` | 2025-09-11 03:09:04 | 消费者投诉2.0 |
| 413 | [常见问题](pages/4016111664.md) | `4016111664` | 2026-05-19 07:42:36 | 消费者投诉2.0 |
| 414 | [查询投诉单列表](pages/4012533431.md) | `4012533431` | 2025-08-28 02:44:02 | 消费者投诉2.0 > API列表 > 主动查询投诉信息 |
| 415 | [查询投诉单详情](pages/4012533436.md) | `4012533436` | 2025-08-28 02:43:38 | 消费者投诉2.0 > API列表 > 主动查询投诉信息 |
| 416 | [查询投诉单协商历史](pages/4012533439.md) | `4012533439` | 2025-08-28 02:43:34 | 消费者投诉2.0 > API列表 > 主动查询投诉信息 |
| 417 | [投诉通知回调](pages/4012289719.md) | `4012289719` | 2025-02-19 03:56:03 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 418 | [创建投诉通知回调地址](pages/4012458679.md) | `4012458679` | 2025-08-28 02:43:18 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 419 | [查询投诉通知回调地址](pages/4012459014.md) | `4012459014` | 2025-08-28 02:43:16 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 420 | [更新投诉通知回调地址](pages/4012459282.md) | `4012459282` | 2025-08-28 02:43:14 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 421 | [删除投诉通知回调地址](pages/4012460452.md) | `4012460452` | 2025-08-28 02:43:11 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 422 | [回复用户](pages/4012467254.md) | `4012467254` | 2025-09-01 02:26:38 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 423 | [反馈处理完成](pages/4012467255.md) | `4012467255` | 2025-09-01 02:25:34 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 424 | [更新退款审批结果](pages/4012467256.md) | `4012467256` | 2025-09-01 02:23:44 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 425 | [回复需要即时服务的投诉单](pages/4017151596.md) | `4017151596` | 2026-01-22 08:02:05 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 426 | [图片上传接口](pages/4012467250.md) | `4012467250` | 2025-09-01 02:11:47 | 消费者投诉2.0 > API列表 > 商户反馈图片 |
| 427 | [图片请求接口](pages/4012467251.md) | `4012467251` | 2025-09-02 02:42:21 | 消费者投诉2.0 > API列表 > 商户反馈图片 |
| 428 | [产品介绍](pages/4012153196.md) | `4012153196` | 2026-05-20 02:34:36 | 微信支付公钥 |
| 429 | [常见问题](pages/4013038816.md) | `4013038816` | 2025-03-04 07:15:22 | 微信支付公钥 |
| 430 | [商户签名验签／加解密测试](pages/4014551946.md) | `4014551946` | 2025-05-30 07:01:56 | 微信支付公钥 > API列表 |
| 431 | [回调接口](pages/4015164042.md) | `4015164042` | 2026-04-10 08:15:52 | 微信支付公钥 > API列表 |
| 432 | [如何从平台证书切换成微信支付公钥](pages/4012154180.md) | `4012154180` | 2024-12-12 02:59:29 | 微信支付公钥 > 附录 |
| 433 | [如何从微信支付公钥切换成平台证书](pages/4015419357.md) | `4015419357` | 2026-03-17 09:45:41 | 微信支付公钥 > 附录 |
| 434 | [产品介绍](pages/4012068814.md) | `4012068814` | 2026-05-20 03:19:57 | 平台证书 |
| 435 | [常见问题](pages/4012069411.md) | `4012069411` | 2024-11-29 09:45:35 | 平台证书 |
| 436 | [下载平台证书](pages/4012551764.md) | `4012551764` | 2024-09-13 06:16:54 | 平台证书 > API列表 |
| 437 | [平台证书更换操作指引](pages/4012068829.md) | `4012068829` | 2024-12-04 06:35:09 | 平台证书 > 附录 |
| 438 | [APIv3概述](pages/4012081606.md) | `4012081606` | 2024-11-21 08:19:57 | Optional > 开发须知 |
| 439 | [总述-APIv3如何签名和验签](pages/4012365342.md) | `4012365342` | 2024-11-21 10:51:22 | Optional > 开发须知 |
| 440 | [基本规则](pages/4012081709.md) | `4012081709` | 2024-07-25 02:05:20 | Optional > 开发须知 > 接口规则说明 |
| 441 | [HTTP状态码](pages/4012081717.md) | `4012081717` | 2024-07-25 02:05:20 | Optional > 开发须知 > 接口规则说明 |
| 442 | [开发必要参数说明](pages/4013070756.md) | `4013070756` | 2025-10-28 02:58:17 | Optional > 开发须知 > 开发参数申请和配置 |
| 443 | [mchid与appid申请](pages/4012071573.md) | `4012071573` | 2025-10-28 02:58:17 | Optional > 开发须知 > 开发参数申请和配置 |
| 444 | [管理商户号绑定的APPID账号](pages/4016328613.md) | `4016328613` | 2025-10-28 02:58:17 | Optional > 开发须知 > 开发参数申请和配置 |
| 445 | [管理经营场景](pages/4017312501.md) | `4017312501` | 2026-02-05 08:34:20 | Optional > 开发须知 > 开发参数申请和配置 |
| 446 | [配置APIv3密钥](pages/4012072195.md) | `4012072195` | 2025-10-28 02:58:17 | Optional > 开发须知 > 开发参数申请和配置 |
| 447 | [配置技术负责人账号指引](pages/4015423618.md) | `4015423618` | 2025-08-07 07:33:12 | Optional > 开发须知 > 开发参数申请和配置 |
| 448 | [员工权限管理](pages/4013071427.md) | `4013071427` | 2025-09-19 01:36:09 | Optional > 开发须知 > 开发参数申请和配置 |
| 449 | [申请商户API证书](pages/4012072428.md) | `4012072428` | 2025-10-28 02:59:06 | Optional > 开发须知 > 开发参数申请和配置 > 商户API证书管理 |
| 450 | [如何更换商户API证书？](pages/4013053057.md) | `4013053057` | 2024-11-19 10:01:05 | Optional > 开发须知 > 开发参数申请和配置 > 商户API证书管理 |
| 451 | [请求参数里带Path参数（路径参数），如何计算签名](pages/4012365334.md) | `4012365334` | 2025-02-18 08:09:32 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 452 | [请求参数里带Body参数(包体参数），如何计算签名](pages/4012365336.md) | `4012365336` | 2025-02-18 09:53:43 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 453 | [请求参数里有Query（查询参数），如何计算签名](pages/4012365337.md) | `4012365337` | 2025-02-18 09:53:41 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 454 | [图片上传接口，如何计算签名](pages/4012365335.md) | `4012365335` | 2025-03-25 03:03:49 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 455 | [APP调起支付签名](pages/4012365340.md) | `4012365340` | 2025-03-26 09:28:08 | Optional > 开发须知 > 如何签名 > 如何构造调起支付签名 |
| 456 | [JSAPI调起支付签名](pages/4012365339.md) | `4012365339` | 2025-03-26 09:28:07 | Optional > 开发须知 > 如何签名 > 如何构造调起支付签名 |
| 457 | [小程序调起支付签名](pages/4012365341.md) | `4012365341` | 2025-03-26 09:28:05 | Optional > 开发须知 > 如何签名 > 如何构造调起支付签名 |
| 458 | [如何使用微信支付公钥验签](pages/4013053249.md) | `4013053249` | 2024-11-20 06:55:05 | Optional > 开发须知 > 如何验签 |
| 459 | [如何使用平台证书验签名](pages/4013053420.md) | `4013053420` | 2024-11-29 09:43:48 | Optional > 开发须知 > 如何验签 > 如何使用平台证书验签 |
| 460 | [如何使用签名/验签工具](pages/4012365352.md) | `4012365352` | 2024-12-27 04:05:13 | Optional > 开发须知 > 如何验签 > 如何使用平台证书验签 |
| 461 | [如何使用微信支付公钥加密敏感字段](pages/4013053257.md) | `4013053257` | 2025-03-19 08:49:11 | Optional > 开发须知 > 如何加解密敏感字段 |
| 462 | [如何使用平台证书加密敏感字段](pages/4013053264.md) | `4013053264` | 2025-03-19 08:49:03 | Optional > 开发须知 > 如何加解密敏感字段 |
| 463 | [如何使用API证书解密敏感字段](pages/4013053265.md) | `4013053265` | 2024-11-19 09:06:37 | Optional > 开发须知 > 如何加解密敏感字段 |
| 464 | [如何解密回调报文和平台证书](pages/4012071382.md) | `4012071382` | 2024-11-29 08:23:04 | Optional > 开发须知 > 如何解密微信支付回调报文 |
| 465 | [报错：HTTP header缺少微信支付平台证书序列号(Wechatpay-Serial)](pages/4012365346.md) | `4012365346` | 2024-11-19 09:07:14 | Optional > 开发须知 > 常见问题 |
| 466 | [报错：“Http头Authorization值格式错误，请参考《微信支付商户REST API签名规则》”或者“Authorization不合法”](pages/4012365344.md) | `4012365344` | 2026-01-23 03:32:09 | Optional > 开发须知 > 常见问题 |
| 467 | [报错：商户证书序列号有误。请使用签名私钥匹配的证书序列号](pages/4012365345.md) | `4012365345` | 2024-12-12 03:12:16 | Optional > 开发须知 > 常见问题 |
| 468 | [报错：状态码401或者“错误的签名，验签失败”或者“签名错误，请检查后再试”](pages/4012365347.md) | `4012365347` | 2024-12-12 03:12:14 | Optional > 开发须知 > 常见问题 |
| 469 | [调起支付报错：支付验证签名失败](pages/4012365348.md) | `4012365348` | 2025-03-26 09:28:04 | Optional > 开发须知 > 常见问题 |
| 470 | [使用Java加载密钥时，抛出异常InvalidKeyException: Illegal key size](pages/4013053271.md) | `4013053271` | 2024-11-19 09:29:40 | Optional > 开发须知 > 常见问题 |
| 471 | [使用Java解密时，抛出异常AEADBadTagException: Tag mismatch](pages/4013053274.md) | `4013053274` | 2024-11-19 09:29:40 | Optional > 开发须知 > 常见问题 |
| 472 | [请求返回{"code":"PARAM_ERROR","message":"平台证书序列号Wechatpay-Serial错误"}](pages/4013053279.md) | `4013053279` | 2024-11-19 09:29:40 | Optional > 开发须知 > 常见问题 |
| 473 | [为什么微信支付的回调缺少签名的几个HTTP头？](pages/4013053283.md) | `4013053283` | 2024-11-19 09:29:40 | Optional > 开发须知 > 常见问题 |
| 474 | [如何在程序中加载商户API证书私钥](pages/4013053290.md) | `4013053290` | 2025-12-25 06:37:14 | Optional > 开发须知 > 常见问题 |
| 475 | [如何查看商户API证书或平台证书序列号？](pages/4013053294.md) | `4013053294` | 2024-11-26 02:43:03 | Optional > 开发须知 > 常见问题 |
| 476 | [为什么请求返回401 Unauthorized？](pages/4012072670.md) | `4012072670` | 2024-11-25 08:53:00 | Optional > 开发须知 > 常见问题 |
| 477 | [验证微信支付响应的签名报错：签名验证失败](pages/4016241880.md) | `4016241880` | 2025-10-14 06:40:19 | Optional > 开发须知 > 常见问题 |
| 478 | [调用接口报错：“平台私钥解密失败”](pages/4016913151.md) | `4016913151` | 2025-12-19 02:59:35 | Optional > 开发须知 > 常见问题 |
| 479 | [跨城冗灾升级指引](pages/4012075113.md) | `4012075113` | 2025-03-21 07:37:49 | Optional > 最佳实践 |
| 480 | [支付回调和查单实现指引](pages/4012075249.md) | `4012075249` | 2024-12-18 07:43:24 | Optional > 最佳实践 |
| 481 | [专线商户Notify升级指引](pages/4012075393.md) | `4012075393` | 2024-07-25 03:02:50 | Optional > 最佳实践 |
| 482 | [回调通知注意事项](pages/4012075420.md) | `4012075420` | 2024-07-25 03:03:09 | Optional > 最佳实践 |
| 483 | [最佳安全实践](pages/4012073699.md) | `4012073699` | 2024-11-27 09:15:00 | Optional > 最佳实践 > API安全最佳实践 |
| 484 | [安全漏洞checklist](pages/4012578686.md) | `4012578686` | 2024-11-27 09:14:55 | Optional > 最佳实践 > API安全最佳实践 |
| 485 | [系统漏洞检测及修复](pages/4012575013.md) | `4012575013` | 2025-03-21 07:40:38 | Optional > 最佳实践 > API安全最佳实践 |
| 486 | [Web漏洞检测及修复](pages/4012575097.md) | `4012575097` | 2025-03-21 08:53:52 | Optional > 最佳实践 > API安全最佳实践 |
| 487 | [最新安全漏洞及修复](pages/4012575124.md) | `4012575124` | 2024-11-27 09:14:37 | Optional > 最佳实践 > API安全最佳实践 |
| 488 | [密钥泄漏修复指引](pages/4012073693.md) | `4012073693` | 2024-12-24 01:54:34 | Optional > 最佳实践 > API安全最佳实践 |
| 489 | [国家商用密码简介](pages/4012075987.md) | `4012075987` | 2024-07-25 03:08:24 | Optional > 国家商用密码接入指南 |
| 490 | [获取国家商用密码证书和密钥](pages/4012076002.md) | `4012076002` | 2024-07-25 03:08:45 | Optional > 国家商用密码接入指南 |
| 491 | [APIv3接口使用国家商用密码指引](pages/4012076194.md) | `4012076194` | 2024-07-25 03:09:16 | Optional > 国家商用密码接入指南 |
| 492 | [开户银行全称对照表](pages/4012076270.md) | `4012076270` | 2024-07-25 03:13:45 | Optional > 对照表 |
| 493 | [开户银行对照表](pages/4012076294.md) | `4012076294` | 2025-02-19 07:30:19 | Optional > 对照表 |
| 494 | [银行类型对照表](pages/4012076355.md) | `4012076355` | 2024-07-25 03:20:22 | Optional > 对照表 |
| 495 | [省市区编号对照表](pages/4012076371.md) | `4012076371` | 2024-07-25 03:20:53 | Optional > 对照表 |
| 496 | [优惠费率活动对照表](pages/4012076387.md) | `4012076387` | 2024-12-26 08:48:22 | Optional > 对照表 |
| 497 | [跨境电商二级商户费率对照表](pages/4012076403.md) | `4012076403` | 2024-07-25 03:21:53 | Optional > 对照表 |
| 498 | [商户行业编码](pages/4012076423.md) | `4012076423` | 2024-07-25 03:22:26 | Optional > 对照表 |
| 499 | [特殊行业ID对照表](pages/4012076444.md) | `4012076444` | 2024-07-25 03:22:48 | Optional > 对照表 |
| 500 | [接入模式](pages/4012068443.md) | `4012068443` | 2024-07-25 02:20:54 | Optional > 名词表 |
| 501 | [支付产品](pages/4012068590.md) | `4012068590` | 2024-07-25 02:21:10 | Optional > 名词表 |
| 502 | [业务平台](pages/4012068615.md) | `4012068615` | 2024-07-25 02:22:14 | Optional > 名词表 |
| 503 | [业务系统](pages/4012068672.md) | `4012068672` | 2024-07-25 02:22:32 | Optional > 名词表 |
| 504 | [参数说明](pages/4012068676.md) | `4012068676` | 2024-10-29 02:13:52 | Optional > 名词表 |
| 505 | [常见问题](pages/4016179629.md) | `4016179629` | 2026-02-06 03:23:52 | Optional > 名词表 |
| 506 | [交易投诉运营规范](pages/4012587539.md) | `4012587539` | 2024-09-23 06:56:32 | Optional > 服务运营规范 |
| 507 | [微信支付链路界面与交互规范](pages/4020527461.md) | `4020527461` | 2026-05-19 02:15:33 | Optional > 服务运营规范 |
| 508 | [验签工具](pages/4012076525.md) | `4012076525` | 2025-01-03 07:02:48 | Optional > 开发工具 |
| 509 | [平台证书下载工具](pages/4012076524.md) | `4012076524` | 2024-11-27 09:13:57 | Optional > 开发工具 |
| 510 | [Postman调试工具](pages/4012076519.md) | `4012076519` | 2024-11-29 09:45:15 | Optional > 开发工具 |
| 511 | [产品介绍](pages/4012076542.md) | `4012076542` | 2025-03-21 07:39:41 | Optional > 网络云排查 |
| 512 | [网络问题排查指南](pages/4012076543.md) | `4012076543` | 2025-03-21 07:39:03 | Optional > 网络云排查 |
| 513 | [常见问题](pages/4012076544.md) | `4012076544` | 2024-07-25 03:40:39 | Optional > 网络云排查 |
| 514 | [产品介绍](pages/4012076556.md) | `4012076556` | 2024-07-25 03:42:19 | Optional > 安全医生 |
| 515 | [诊断链接绑定指引](pages/4012076558.md) | `4012076558` | 2024-07-25 03:42:41 | Optional > 安全医生 |
| 516 | [安全联系人设置指引](pages/4012076563.md) | `4012076563` | 2024-07-25 03:43:12 | Optional > 安全医生 |
| 517 | [SDK概述](pages/4012076498.md) | `4012076498` | 2026-04-24 09:15:35 | Optional > SDK |
| 518 | [使用 Java SDK](pages/4012076506.md) | `4012076506` | 2025-05-29 03:32:15 | Optional > SDK |
| 519 | [使用 PHP SDK](pages/4012076511.md) | `4012076511` | 2025-05-29 03:32:09 | Optional > SDK |
| 520 | [使用 Go SDK](pages/4012076515.md) | `4012076515` | 2025-05-29 03:37:00 | Optional > SDK |

</details>