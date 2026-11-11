# 微信支付文档更新报告 - 合作伙伴

**文档类型**: 合作伙伴 (partner)
**生成时间**: 20261111_071751
**文档总数**: 908
**数据来源**: https://pay.weixin.qq.com/doc/v3/partner/llms.txt

## 变更概览

- 新增: 0 个页面
- 删除: 2 个页面
- 修改: 6 个页面
- 成功拉取: 6 个页面
- 拉取失败: 0 个页面
- llms.txt 变更: 是

## llms.txt 变更

```diff
--- llms_old.txt
+++ llms.txt
@@ -1,4 +1,4 @@
->更新时间：2026.11.10
+>更新时间：2026.11.11
 
 # 微信支付合作伙伴平台文档中心
 
@@ -809,8 +809,6 @@
 - [删除品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4015783113.md)
 - [暂停门店营业](https://pay.weixin.qq.com/doc/v3/partner/4016756671.md)
 - [恢复门店营业](https://pay.weixin.qq.com/doc/v3/partner/4016756672.md)
-- [绑定收款商户号](https://pay.weixin.qq.com/doc/v3/partner/4015783177.md)
-- [解绑收款商户号](https://pay.weixin.qq.com/doc/v3/partner/4015783188.md)
 ### 附录
 - [品牌经营平台管理品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4016689827.md)
 ## 品牌服务商授权
```

## 删除页面

- **绑定收款商户号** (`4015783177`)
  - 原路径: 品牌门店 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015783177.md
  - 原更新时间: 2025-12-02 11:35:44

- **解绑收款商户号** (`4015783188`)
  - 原路径: 品牌门店 > API列表
  - 原 URL: https://pay.weixin.qq.com/doc/v3/partner/4015783188.md
  - 原更新时间: 2025-12-02 11:35:44

## 修改页面

### 创建会员卡模板
- ID: `4015336970`
- 路径: 商家名片会员 > API列表 > 会员卡模板管理
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015336970.md
- 更新时间变更: 2026-11-04 07:43:44 -> 2026-11-11 06:32:15
- 本地文件: `pages/4015336970.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.11.04
+>更新时间：2026.11.11
 
 通过此接口可以创建一张会员卡模板，创建成功将获得会员卡模板ID
 
@@ -37,7 +37,9 @@
 | card_picture_url | string(256) | false | 【卡图片】 商家自定义会员卡背景图。仅支持通过图片上传API接口获取的图片URL地址。支持JPG/JPEG/PNG格式，建议尺寸716px\*320px，且图片小于1M。查看以下链接后传入： [图片要求示例](https://gtimg.wechatpay.cn/resource/xres/img/202507/7eae51fbdbed8090d41528eda795676e_2733x716.png)， [图片上传API指引](https://pay.weixin.qq.com/doc/v3/partner/4012759802.md)。不传时没有默认卡图。 |
 | code_mode | string | false | 【会员卡code分配类型】 1、会员卡code是会员在一个会员卡模板下唯一身份标识，平台支持2种分配类型：<br>（1）SYSTEM\_ALLOCATE 微信支付系统分配，用户领取会员卡时从微信系统分配24位数字作为会员code，并在「用户开通会员卡」事件通知中返回；<br>（2）MERCHANT\_ALLOCATE 商家分配，商家同步会员开通结果时传入，用户开卡成功或失败都以商家传入的code作为会员卡code。选择商家分配模式时，开通事件通知中不返回 `user_card_code`。<br>2、不传时默认为系统分配（ `SYSTEM_ALLOCATE`）。<br>3、会员卡创建后，code分配模式不支持修改。<br>可选取值<br><ul><li>`SYSTEM_ALLOCATE`:  系统分配</li><li>`MERCHANT_ALLOCATE`:  商家分配</li></ul> |
 | code_type | string | false | 【会员码展示类型】 会员码支持不展示码/二维码／条形码／二维码＋条形码/跳转商家小程序5种设置。当会员码展示类型为跳转商家小程序时，必填 `code_jump_information`。不传时默认为不显示任何码型（ `NONE_CODE`）。<br>可选取值<br><ul><li>`NONE_CODE`:  不显示任何码型</li><li>`BAR_CODE`:  条形码</li><li>`QR_CODE`:  二维码</li><li>`BAR_CODE_AND_QR_CODE`:  条形码和二维码</li><li>`JUMP_MINI_PROGRAM`:  跳转商家小程序</li></ul> |
-| code_jump_information | object | false | 【会员码跳转信息】 会员码跳转的小程序信息，当会员码展示类型为跳转商家小程序时必填。<br>属性<br>jump\_appid 选填  string(32)<br>【会员码跳转AppID】 会员码跳转的小程序AppID<br>* * *<br>jump\_path 选填  string(128)<br>【会员码跳转路径】 会员码跳转的小程序路径 |
+| code_jump_information | object | false | 【会员码跳转信息】 会员码跳转的小程序信息，当会员码展示类型为跳转商家小程序时必填。 |
+| code_jump_information.jump_appid | string(32) | false | 【会员码跳转AppID】 会员码跳转的小程序AppID |
+| code_jump_information.jump_path | string(128) | false | 【会员码跳转路径】 会员码跳转的小程序路径 |
 | benefits | string(32) | false | 【会员权益】 会员权益是指平台、品牌或服务机构为付费会员（或等级会员）提供的专属优惠、服务或特权。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
 | notify_url | string(256) | false | 【回调地址】 商家接收开卡成功回调通知的地址，需按照 [notify\_url填写注意事项](https://pay.weixin.qq.com/doc/v3/partner/4012082570.md#1.-notify_url%E5%A1%AB%E5%86%99%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9) 规范填写。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
 | need_pinned | boolean | false | 【是否置顶】 置顶卡是界面中的一种特殊展示模块，通过人工设置，使其固定在内容列表的顶部位置，确保用户优先看到。默认为false。同一个品牌下允许存在多张置顶卡，按照更新时间倒序排序。 |
@@ -45,12 +47,30 @@
 | init_level | string(10) | false | 【会员初始等级】 展示字段，商家可以自定义填写内容。如果选择了展示会员等级，必填 `init_level`，作为新用户开卡后的初始等级。如因商家业务规则需要变更某会员等级，可通过更新用户会员卡接口更新等级信息。若该值不为空，则会返回该字段。 |
 | service_phone | string(32) | false | 【服务电话】 展示在会员卡详情内，建议填写商家固定电话。若该值不为空，则会返回该字段。 |
 | legal_agreement | string(20480) | false | 【商家法务协议】 指用户与商家之间签订的具有法律效力的合同文件，旨在明确双方在交易、服务提供、权利义务等方面的规则，以保障交易安全、规范商业行为，并在纠纷发生时提供法律依据。不支持链接跳转，支持使用 `\n` 代表换行，只支持纯文本展示。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
-| valid_date_information | object | false | 【会员卡有效期】 会员卡有效期。不传时默认为永久有效。<br>属性<br>type 必填  string<br>【有效期类型】 传入会员卡有效期时必填。1.该有效期为会员卡激活后的有效期 2.支持绝对有效期&相对有效期设置 3.绝对有效期：固定过期时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 4.相对有效期：用户激活后x天后有效，x为天数。最多支持10,957天（30年） 5.永久有效 6.过期后卡状态变为“已过期” 7.过期后不再出现服务项，且无法给用户发送会员服务消息通知<br>可选取值<br>- `FIX_TIME_RANGE`:  必填available\_begin\_time和available\_end\_time，会员卡在此时间\[available\_begin\_time, available\_end\_time)范围内有效<br>- `FIX_TERM`:  必填available\_day\_after\_receive，会员卡在用户领取之后available\_day\_after\_receive天内有效<br>- `PERMANENT`:  会员卡激活后永久有效<br>* * *<br>available\_begin\_time 选填  string<br>【有效期开始时间】 type为FIX\_TIME\_RANGE时专用， 表示有效期开始时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。<br>* * *<br>available\_end\_time 选填  string<br>【有效期结束时间】 type为FIX\_TIME\_RANGE时专用，表示有效期结束时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。<br>* * *<br>available\_day\_after\_receive 选填  integer<br>【领取后N天内有效】 type为FIX\_TERM时专用，表示领取后N个自然天内有效。最长不超过30年（10958 天） |
-| member_information | object | true | 【会员中心信息】 用户点击会员卡卡面的跳转信息<br>属性<br>jump\_appid 必填  string(32)<br>【会员中心跳转AppID】 用户点击会员卡卡面后跳转的小程序AppID<br>* * *<br>jump\_path 必填  string(128)<br>【会员中心跳转路径】 用户点击会员卡卡面后跳转的小程序路径 |
-| points_information | object | false | 【积分信息】 若商家名片会员卡使用该功能，需传入跳转商家小程序的信息。否则不启动该功能。若该值不为空，则会返回该字段。<br>属性<br>jump\_appid 选填  string(32)<br>【积分跳转AppID】 会员积分跳转的小程序AppID<br>* * *<br>jump\_path 选填  string(128)<br>【积分跳转路径】 会员积分跳转的小程序路径 |
-| balance_information | object | false | 【储值信息】 若商家名片会员卡使用该功能，需传入跳转商家小程序的信息。否则不启动该功能。若该值不为空，则会返回该字段。<br>属性<br>jump\_appid 选填  string(32)<br>【储值小程序AppID】 点击储值额跳转的小程序AppID<br>* * *<br>jump\_path 选填  string(128)<br>【储值小程序路径】 点击储值额跳转的小程序页面路径，建议为储值充值页面 |
-| purchase_information | object | false | 【付费会员信息】 若商家名片会员卡使用该功能，需传入跳转商家小程序的信息及会员价格。否则不启动该功能。若该值不为空，则会返回该字段。<br>属性<br>price 选填  integer<br>【付费会员价格】 指用户为获取特定商家提供的会员权益而需支付的费用金额。（单位：分）<br>* * *<br>jump\_appid 选填  string(32)<br>【付费会员跳转AppID】 用户购买付费会员时跳转的付费会员的AppID<br>* * *<br>jump\_path 选填  string(128)<br>【付费会员跳转路径】 用户购买付费会员时购买跳转的路径 |
-| user_information | object | false | 【用户开卡信息】 用户开通会员卡时可填写的信息。用户可以选择不填写，不影响开通会员卡；用户填写的内容会在开卡回调中返回给商家。<br>属性<br>common\_field\_list 选填  array\[string\]<br>【平台提供的通用开卡信息字段】 平台提供的通用开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。<br>可选取值<br>- `USER_FORM_FLAG_SEX`:  用户开卡时需填写性别，字段内容可选男或女。<br>- `USER_FORM_FLAG_NAME`:  用户开卡时需填写姓名<br>- `USER_FORM_FLAG_BIRTHDAY`:  用户开卡时需填写生日，字段内容需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准的 `full-date` 格式：yyyy-MM-DD，表示年月日。年份必须为 4 位数，月份和日期不足两位时需补零。 示例：2015-05-20。<br>- `USER_FORM_FLAG_ADDRESS`:  用户开卡时需填写地址<br>- `USER_FORM_FLAG_EMAIL`:  用户开卡时需填写邮箱，字段内容需为合法邮箱。<br>- `USER_FORM_FLAG_CITY`:  用户开卡时需填写城市，字段格式需为："省份,城市"，第一项省份，第二项城市，用英文逗号分隔。<br>* * *<br>custom\_field\_list 选填  array\[object\]<br>【商家自定义的开卡信息字段】 商家自定义的开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。当前最多只允许传入1项。<br>属性<br>type 选填  string<br>【字段类型】 选择所需的字段类型<br>可选取值<br>- `CHECK_BOX`:  用户可从商家提供的选项中选择多项<br>- `RADIO`:  用户可从商家提供的选项中选择一项<br>* * *<br>name 选填  string(32)<br>【字段名称】 信息项的名称。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。<br>* * *<br>values 选填  array\[string(8)\]<br>【字段值】 信息项的值列表。<br>特殊规则：列表最多支持10个，单个列表限制8个字符。若商户创建会员卡模板时设置该值，则查询结果中会返回给商户。 |
+| valid_date_information | object | false | 【会员卡有效期】 会员卡有效期。不传时默认为永久有效。 |
+| valid_date_information.type | string | true | 【有效期类型】 传入会员卡有效期时必填。1.该有效期为会员卡激活后的有效期 2.支持绝对有效期&相对有效期设置 3.绝对有效期：固定过期时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 4.相对有效期：用户激活后x天后有效，x为天数。最多支持10,957天（30年） 5.永久有效 6.过期后卡状态变为“已过期” 7.过期后不再出现服务项，且无法给用户发送会员服务消息通知<br>可选取值<br><ul><li>`FIX_TIME_RANGE`:  必填available\_begin\_time和available\_end\_time，会员卡在此时间\[available\_begin\_time, available\_end\_time)范围内有效</li><li>`FIX_TERM`:  必填available\_day\_after\_receive，会员卡在用户领取之后available\_day\_after\_receive天内有效</li><li>`PERMANENT`:  会员卡激活后永久有效</li></ul> |
+| valid_date_information.available_begin_time | string | false | 【有效期开始时间】 type为FIX\_TIME\_RANGE时专用， 表示有效期开始时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
+| valid_date_information.available_end_time | string | false | 【有效期结束时间】 type为FIX\_TIME\_RANGE时专用，表示有效期结束时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
+| valid_date_information.available_day_after_receive | integer | false | 【领取后N天内有效】 type为FIX\_TERM时专用，表示领取后N个自然天内有效。最长不超过30年（10958 天） |
+| member_information | object | true | 【会员中心信息】 用户点击会员卡卡面的跳转信息 |
+| member_information.jump_appid | string(32) | true | 【会员中心跳转AppID】 用户点击会员卡卡面后跳转的小程序AppID |
+| member_information.jump_path | string(128) | true | 【会员中心跳转路径】 用户点击会员卡卡面后跳转的小程序路径 |
+| points_information | object | false | 【积分信息】 若商家名片会员卡使用该功能，需传入跳转商家小程序的信息。否则不启动该功能。若该值不为空，则会返回该字段。 |
+| points_information.jump_appid | string(32) | false | 【积分跳转AppID】 会员积分跳转的小程序AppID |
+| points_information.jump_path | string(128) | false | 【积分跳转路径】 会员积分跳转的小程序路径 |
+| balance_information | object | false | 【储值信息】 若商家名片会员卡使用该功能，需传入跳转商家小程序的信息。否则不启动该功能。若该值不为空，则会返回该字段。 |
+| balance_information.jump_appid | string(32) | false | 【储值小程序AppID】 点击储值额跳转的小程序AppID |
+| balance_information.jump_path | string(128) | false | 【储值小程序路径】 点击储值额跳转的小程序页面路径，建议为储值充值页面 |
+| purchase_information | object | false | 【付费会员信息】 若商家名片会员卡使用该功能，需传入跳转商家小程序的信息及会员价格。否则不启动该功能。若该值不为空，则会返回该字段。 |
+| purchase_information.price | integer | false | 【付费会员价格】 指用户为获取特定商家提供的会员权益而需支付的费用金额。（单位：分） |
+| purchase_information.jump_appid | string(32) | false | 【付费会员跳转AppID】 用户购买付费会员时跳转的付费会员的AppID |
+| purchase_information.jump_path | string(128) | false | 【付费会员跳转路径】 用户购买付费会员时购买跳转的路径 |
+| user_information | object | false | 【用户开卡信息】 用户开通会员卡时可填写的信息。用户可以选择不填写，不影响开通会员卡；用户填写的内容会在开卡回调中返回给商家。 |
+| user_information.common_field_list | array[string] | false | 【平台提供的通用开卡信息字段】 平台提供的通用开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。<br>可选取值<br><ul><li>`USER_FORM_FLAG_SEX`:  用户开卡时需填写性别，字段内容可选男或女。</li><li>`USER_FORM_FLAG_NAME`:  用户开卡时需填写姓名</li><li>`USER_FORM_FLAG_BIRTHDAY`:  用户开卡时需填写生日，字段内容需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准的 `full-date` 格式：yyyy-MM-DD，表示年月日。年份必须为 4 位数，月份和日期不足两位时需补零。 示例：2015-05-20。</li><li>`USER_FORM_FLAG_ADDRESS`:  用户开卡时需填写地址</li><li>`USER_FORM_FLAG_EMAIL`:  用户开卡时需填写邮箱，字段内容需为合法邮箱。</li><li>`USER_FORM_FLAG_CITY`:  用户开卡时需填写城市，字段格式需为："省份,城市"，第一项省份，第二项城市，用英文逗号分隔。</li></ul> |
+| user_information.custom_field_list | array[object] | false | 【商家自定义的开卡信息字段】 商家自定义的开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。当前最多只允许传入1项。 |
+| user_information.custom_field_list.type | string | false | 【字段类型】 选择所需的字段类型<br>可选取值<br><ul><li>`CHECK_BOX`:  用户可从商家提供的选项中选择多项</li><li>`RADIO`:  用户可从商家提供的选项中选择一项</li></ul> |
+| user_information.custom_field_list.name | string(32) | false | 【字段名称】 信息项的名称。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。 |
+| user_information.custom_field_list.values | array[string(8)] | false | 【字段值】 信息项的值列表。<br>特殊规则：列表最多支持10个，单个列表限制8个字符。若商户创建会员卡模板时设置该值，则查询结果中会返回给商户。 |
 | support_user_active_join | boolean | false | 【是否支持用户主动入会】 是否允许用户在微信支付内主动开通这张会员卡。不传时默认为 true。为 true 时，用户可以通过商家名片、支付相关入会入口，以及商家小程序或 H5 的入会流程填写开卡信息并开通；会员权益、回调地址、商家法务协议必填。为 false 时，用户不能在微信支付内主动开通，只能由商家通过导入等方式开通。 |
 | purchase_membership | boolean | false | 【是否为付费会员】 标记这张会员卡是否为付费会员。不传时为 false。本字段仅作标记，为 true 不要求填写付费会员价格和跳转信息。 |
 ## 应答参数
@@ -69,7 +89,9 @@
 | card_picture_url | string(256) | false | 【卡图片】 商家自定义会员卡背景图。仅支持通过图片上传API接口获取的图片URL地址。支持JPG/JPEG/PNG格式，建议尺寸716px\*320px，且图片小于1M。查看以下链接后传入： [图片要求示例](https://gtimg.wechatpay.cn/resource/xres/img/202507/7eae51fbdbed8090d41528eda795676e_2733x716.png)， [图片上传API指引](https://pay.weixin.qq.com/doc/v3/partner/4012759802.md)。不传时没有默认卡图。 |
 | code_mode | string | true | 【会员卡code分配类型】 1、会员卡code是会员在一个会员卡模板下唯一身份标识，平台支持2种分配类型：<br>（1）SYSTEM\_ALLOCATE 微信支付系统分配，用户领取会员卡时从微信系统分配24位数字作为会员code，并在「用户开通会员卡」事件通知中返回；<br>（2）MERCHANT\_ALLOCATE 商家分配，商家同步会员开通结果时传入，用户开卡成功或失败都以商家传入的code作为会员卡code。选择商家分配模式时，开通事件通知中不返回 `user_card_code`。<br>2、会员卡创建后，code分配模式不支持修改。<br>可选取值<br><ul><li>`SYSTEM_ALLOCATE`:  系统分配</li><li>`MERCHANT_ALLOCATE`:  商家分配</li></ul> |
 | code_type | string | true | 【会员码展示类型】 会员码支持不展示码/二维码／条形码／二维码＋条形码/跳转商家小程序5种设置。<br>可选取值<br><ul><li>`NONE_CODE`:  不显示任何码型</li><li>`BAR_CODE`:  条形码</li><li>`QR_CODE`:  二维码</li><li>`BAR_CODE_AND_QR_CODE`:  条形码和二维码</li><li>`JUMP_MINI_PROGRAM`:  跳转商家小程序</li></ul> |
-| code_jump_information | object | false | 【会员码跳转信息】 会员码跳转的小程序信息，当会员码展示类型为跳转商家小程序时必填。<br>属性<br>jump\_appid 选填  string(32)<br>【会员码跳转AppID】 会员码跳转的小程序AppID<br>* * *<br>jump\_path 选填  string(128)<br>【会员码跳转路径】 会员码跳转的小程序路径 |
+| code_jump_information | object | false | 【会员码跳转信息】 会员码跳转的小程序信息，当会员码展示类型为跳转商家小程序时必填。 |
+| code_jump_information.jump_appid | string(32) | false | 【会员码跳转AppID】 会员码跳转的小程序AppID |
+| code_jump_information.jump_path | string(128) | false | 【会员码跳转路径】 会员码跳转的小程序路径 |
 | benefits | string(32) | false | 【会员权益】 会员权益是指平台、品牌或服务机构为付费会员（或等级会员）提供的专属优惠、服务或特权。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
 | notify_url | string(256) | false | 【回调地址】 商家接收开卡成功回调通知的地址，需按照 [notify\_url填写注意事项](https://pay.weixin.qq.com/doc/v3/partner/4012082570.md#1.-notify_url%E5%A1%AB%E5%86%99%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9) 规范填写。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
 | need_pinned | boolean | false | 【是否置顶】 置顶卡是界面中的一种特殊展示模块，通过人工设置，使其固定在内容列表的顶部位置，确保用户优先看到。默认为false。同一个品牌下允许存在多张置顶卡，按照更新时间倒序排序。 |
@@ -77,12 +99,30 @@
 | init_level | string(10) | false | 【会员初始等级】 展示字段，商家可以自定义填写内容。如果选择了展示会员等级，必填 `init_level`，作为新用户开卡后的初始等级。如因商家业务规则需要变更某会员等级，可通过更新用户会员卡接口更新等级信息。 |
 | service_phone | string(32) | false | 【服务电话】 展示在会员卡详情内，建议填写商家固定电话 |
 | legal_agreement | string(20480) | false | 【商家法务协议】 指用户与商家之间签订的具有法律效力的合同文件，旨在明确双方在交易、服务提供、权利义务等方面的规则，以保障交易安全、规范商业行为，并在纠纷发生时提供法律依据。不支持链接跳转，支持使用 `\n` 代表换行，只支持纯文本展示。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
-| valid_date_information | object | true | 【会员卡有效期】 会员卡有效期<br>属性<br>type 必填  string<br>【有效期类型】 传入会员卡有效期时必填。1.该有效期为会员卡激活后的有效期 2.支持绝对有效期&相对有效期设置 3.绝对有效期：固定过期时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 4.相对有效期：用户激活后x天后有效，x为天数。最多支持10,957天（30年） 5.永久有效 6.过期后卡状态变为“已过期” 7.过期后不再出现服务项，且无法给用户发送会员服务消息通知<br>可选取值<br>- `FIX_TIME_RANGE`:  必填available\_begin\_time和available\_end\_time，会员卡在此时间\[available\_begin\_time, available\_end\_time)范围内有效<br>- `FIX_TERM`:  必填available\_day\_after\_receive，会员卡在用户领取之后available\_day\_after\_receive天内有效<br>- `PERMANENT`:  会员卡激活后永久有效<br>* * *<br>available\_begin\_time 选填  string<br>【有效期开始时间】 type为FIX\_TIME\_RANGE时专用， 表示有效期开始时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。<br>* * *<br>available\_end\_time 选填  string<br>【有效期结束时间】 type为FIX\_TIME\_RANGE时专用，表示有效期结束时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。<br>* * *<br>available\_day\_after\_receive 选填  integer<br>【领取后N天内有效】 type为FIX\_TERM时专用，表示领取后N个自然天内有效。最长不超过30年（10958 天） |
-| member_information | object | true | 【会员中心信息】 用户点击会员卡卡面的跳转信息<br>属性<br>jump\_appid 必填  string(32)<br>【会员中心跳转AppID】 用户点击会员卡卡面后跳转的小程序AppID<br>* * *<br>jump\_path 必填  string(128)<br>【会员中心跳转路径】 用户点击会员卡卡面后跳转的小程序路径 |
-| points_information | object | false | 【积分信息】 若商家名片会员卡使用该功能，需传入跳转商家小程序的信息。否则不启动该功能。<br>属性<br>jump\_appid 选填  string(32)<br>【积分跳转AppID】 会员积分跳转的小程序AppID<br>* * *<br>jump\_path 选填  string(128)<br>【积分跳转路径】 会员积分跳转的小程序路径 |
-| balance_information | object | false | 【储值信息】 若商家名片会员卡使用该功能，需传入跳转商家小程序的信息。否则不启动该功能。<br>属性<br>jump\_appid 选填  string(32)<br>【储值小程序AppID】 点击储值额跳转的小程序AppID<br>* * *<br>jump\_path 选填  string(128)<br>【储值小程序路径】 点击储值额跳转的小程序页面路径，建议为储值充值页面 |
-| purchase_information | object | false | 【付费会员信息】 若商家名片会员卡使用该功能，需传入跳转商家小程序的信息及会员价格。否则不启动该功能。<br>属性<br>price 选填  integer<br>【付费会员价格】 指用户为获取特定商家提供的会员权益而需支付的费用金额。（单位：分）<br>* * *<br>jump\_appid 选填  string(32)<br>【付费会员跳转AppID】 用户购买付费会员时跳转的付费会员的AppID<br>* * *<br>jump\_path 选填  string(128)<br>【付费会员跳转路径】 用户购买付费会员时购买跳转的路径 |
-| user_information | object | false | 【用户开卡信息】 用户开通会员卡时可填写的信息。用户可以选择不填写，不影响开通会员卡；用户填写的内容会在开卡回调中返回给商家。<br>属性<br>common\_field\_list 选填  array\[string\]<br>【平台提供的通用开卡信息字段】 平台提供的通用开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。<br>可选取值<br>- `USER_FORM_FLAG_SEX`:  用户开卡时需填写性别，字段内容可选男或女。<br>- `USER_FORM_FLAG_NAME`:  用户开卡时需填写姓名<br>- `USER_FORM_FLAG_BIRTHDAY`:  用户开卡时需填写生日，字段内容需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准的 `full-date` 格式：yyyy-MM-DD，表示年月日。年份必须为 4 位数，月份和日期不足两位时需补零。 示例：2015-05-20。<br>- `USER_FORM_FLAG_ADDRESS`:  用户开卡时需填写地址<br>- `USER_FORM_FLAG_EMAIL`:  用户开卡时需填写邮箱，字段内容需为合法邮箱。<br>- `USER_FORM_FLAG_CITY`:  用户开卡时需填写城市，字段格式需为："省份,城市"，第一项省份，第二项城市，用英文逗号分隔。<br>* * *<br>custom\_field\_list 选填  array\[object\]<br>【商家自定义的开卡信息字段】 商家自定义的开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。当前最多只允许传入1项。<br>属性<br>type 选填  string<br>【字段类型】 选择所需的字段类型<br>可选取值<br>- `CHECK_BOX`:  用户可从商家提供的选项中选择多项<br>- `RADIO`:  用户可从商家提供的选项中选择一项<br>* * *<br>name 选填  string(32)<br>【字段名称】 信息项的名称。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。<br>* * *<br>values 选填  array\[string(8)\]<br>【字段值】 信息项的值列表。<br>特殊规则：列表最多支持10个，单个列表限制8个字符。若商户创建会员卡模板时设置该值，则查询结果中会返回给商户。 |
+| valid_date_information | object | true | 【会员卡有效期】 会员卡有效期 |
+| valid_date_information.type | string | true | 【有效期类型】 传入会员卡有效期时必填。1.该有效期为会员卡激活后的有效期 2.支持绝对有效期&相对有效期设置 3.绝对有效期：固定过期时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 4.相对有效期：用户激活后x天后有效，x为天数。最多支持10,957天（30年） 5.永久有效 6.过期后卡状态变为“已过期” 7.过期后不再出现服务项，且无法给用户发送会员服务消息通知<br>可选取值<br><ul><li>`FIX_TIME_RANGE`:  必填available\_begin\_time和available\_end\_time，会员卡在此时间\[available\_begin\_time, available\_end\_time)范围内有效</li><li>`FIX_TERM`:  必填available\_day\_after\_receive，会员卡在用户领取之后available\_day\_after\_receive天内有效</li><li>`PERMANENT`:  会员卡激活后永久有效</li></ul> |
+| valid_date_information.available_begin_time | string | false | 【有效期开始时间】 type为FIX\_TIME\_RANGE时专用， 表示有效期开始时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
+| valid_date_information.available_end_time | string | false | 【有效期结束时间】 type为FIX\_TIME\_RANGE时专用，表示有效期结束时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
+| valid_date_information.available_day_after_receive | integer | false | 【领取后N天内有效】 type为FIX\_TERM时专用，表示领取后N个自然天内有效。最长不超过30年（10958 天） |
+| member_information | object | true | 【会员中心信息】 用户点击会员卡卡面的跳转信息 |
+| member_information.jump_appid | string(32) | true | 【会员中心跳转AppID】 用户点击会员卡卡面后跳转的小程序AppID |
+| member_information.jump_path | string(128) | true | 【会员中心跳转路径】 用户点击会员卡卡面后跳转的小程序路径 |
+| points_information | object | false | 【积分信息】 若商家名片会员卡使用该功能，需传入跳转商家小程序的信息。否则不启动该功能。 |
+| points_information.jump_appid | string(32) | false | 【积分跳转AppID】 会员积分跳转的小程序AppID |
+| points_information.jump_path | string(128) | false | 【积分跳转路径】 会员积分跳转的小程序路径 |
+| balance_information | object | false | 【储值信息】 若商家名片会员卡使用该功能，需传入跳转商家小程序的信息。否则不启动该功能。 |
+| balance_information.jump_appid | string(32) | false | 【储值小程序AppID】 点击储值额跳转的小程序AppID |
+| balance_information.jump_path | string(128) | false | 【储值小程序路径】 点击储值额跳转的小程序页面路径，建议为储值充值页面 |
+| purchase_information | object | false | 【付费会员信息】 若商家名片会员卡使用该功能，需传入跳转商家小程序的信息及会员价格。否则不启动该功能。 |
+| purchase_information.price | integer | false | 【付费会员价格】 指用户为获取特定商家提供的会员权益而需支付的费用金额。（单位：分） |
+| purchase_information.jump_appid | string(32) | false | 【付费会员跳转AppID】 用户购买付费会员时跳转的付费会员的AppID |
+| purchase_information.jump_path | string(128) | false | 【付费会员跳转路径】 用户购买付费会员时购买跳转的路径 |
+| user_information | object | false | 【用户开卡信息】 用户开通会员卡时可填写的信息。用户可以选择不填写，不影响开通会员卡；用户填写的内容会在开卡回调中返回给商家。 |
+| user_information.common_field_list | array[string] | false | 【平台提供的通用开卡信息字段】 平台提供的通用开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。<br>可选取值<br><ul><li>`USER_FORM_FLAG_SEX`:  用户开卡时需填写性别，字段内容可选男或女。</li><li>`USER_FORM_FLAG_NAME`:  用户开卡时需填写姓名</li><li>`USER_FORM_FLAG_BIRTHDAY`:  用户开卡时需填写生日，字段内容需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准的 `full-date` 格式：yyyy-MM-DD，表示年月日。年份必须为 4 位数，月份和日期不足两位时需补零。 示例：2015-05-20。</li><li>`USER_FORM_FLAG_ADDRESS`:  用户开卡时需填写地址</li><li>`USER_FORM_FLAG_EMAIL`:  用户开卡时需填写邮箱，字段内容需为合法邮箱。</li><li>`USER_FORM_FLAG_CITY`:  用户开卡时需填写城市，字段格式需为："省份,城市"，第一项省份，第二项城市，用英文逗号分隔。</li></ul> |
+| user_information.custom_field_list | array[object] | false | 【商家自定义的开卡信息字段】 商家自定义的开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。当前最多只允许传入1项。 |
+| user_information.custom_field_list.type | string | false | 【字段类型】 选择所需的字段类型<br>可选取值<br><ul><li>`CHECK_BOX`:  用户可从商家提供的选项中选择多项</li><li>`RADIO`:  用户可从商家提供的选项中选择一项</li></ul> |
+| user_information.custom_field_list.name | string(32) | false | 【字段名称】 信息项的名称。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。 |
+| user_information.custom_field_list.values | array[string(8)] | false | 【字段值】 信息项的值列表。<br>特殊规则：列表最多支持10个，单个列表限制8个字符。若商户创建会员卡模板时设置该值，则查询结果中会返回给商户。 |
 | state | string | true | 【状态】 会员卡状态信息<br>可选取值<br><ul><li>`CARD_EFFECTIVE`:  生效中</li><li>`CARD_INVALID`:  已失效</li></ul> |
 | create_time | string | true | 【创建时间】 创建会员卡的时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
 | modify_time | string | true | 【更新时间】 更新会员卡的时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
```

### 查询会员卡模板列表
- ID: `4015336976`
- 路径: 商家名片会员 > API列表 > 会员卡模板管理
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015336976.md
- 更新时间变更: 2025-08-01 02:53:26 -> 2026-11-11 06:30:44
- 本地文件: `pages/4015336976.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2025.08.01
+>更新时间：2026.11.11
 
 通过此接口可查询指定某品牌的所有会员卡模板列表
 
@@ -15,7 +15,7 @@
 
 　　　　　【备域名】https://api2.mch.weixin.qq.com 使用该域名将访问异地的接入点，指引[点击查看](https://pay.weixin.qq.com/doc/v3/merchant/4012075113.md)
 
-接口限频：10/秒（商户号维度）
+接口限频：100/秒（商户号维度）
 
 ## 请求参数
 
@@ -45,21 +45,21 @@
 | data.card_type | string | true | 【会员卡类型】 支持付费、普通、储值 3 种类型。目前仅支持普通会员卡，填写付费和储值类型时会返回错误。<br>可选取值<br><ul><li>`PURCHASE`:  付费</li><li>`NORMAL`:  普通</li><li>`BALANCE`:  储值</li></ul> |
 | data.card_title | string(10) | true | 【卡名称】 1.可用于展示在卡面的名称 2.支持最长10个中文字 3.支持中文字、英文字符、标点 |
 | data.card_color | string(7) | true | 【卡背景颜色】 用于卡片正面设计的RGB颜色编码，仅支持十六进制 |
-| data.card_picture_url | string(256) | true | 【卡图片】 商家自定义会员卡背景图。仅支持通过图片上传API接口获取的图片URL地址。支持JPG/JPEG/PNG格式，建议尺寸716px\*320px，且图片小于1M。查看以下链接后传入： [图片要求示例](https://gtimg.wechatpay.cn/resource/xres/img/202507/7eae51fbdbed8090d41528eda795676e_2733x716.png)， [图片上传API指引](https://pay.weixin.qq.com/doc/v3/partner/4012759802.md)。 |
-| data.code_mode | string | true | 【会员卡code分配类型】 1、会员卡code是会员在一个会员卡模板下唯一身份标识，平台支持2种分配类型：（1）SYSTEM\_ALLOCATE 微信支付系统分配，用户领取会员卡时从微信系统分配24位数字作为会员code；（2）MERCHANT\_ALLOCATE 商家分配，商家同步会员开通结果时传入，用户开卡成功或失败都以商家传入的code作为会员卡code 2、会员卡code分配模式若为“系统分配”，不支持修改为“商家分配”。<br>可选取值<br><ul><li>`SYSTEM_ALLOCATE`:  系统分配</li><li>`MERCHANT_ALLOCATE`:  商家分配</li></ul> |
+| data.card_picture_url | string(256) | false | 【卡图片】 商家自定义会员卡背景图。仅支持通过图片上传API接口获取的图片URL地址。支持JPG/JPEG/PNG格式，建议尺寸716px\*320px，且图片小于1M。查看以下链接后传入： [图片要求示例](https://gtimg.wechatpay.cn/resource/xres/img/202507/7eae51fbdbed8090d41528eda795676e_2733x716.png)， [图片上传API指引](https://pay.weixin.qq.com/doc/v3/partner/4012759802.md)。不传时没有默认卡图。 |
+| data.code_mode | string | true | 【会员卡code分配类型】 1、会员卡code是会员在一个会员卡模板下唯一身份标识，平台支持2种分配类型：<br>（1）SYSTEM\_ALLOCATE 微信支付系统分配，用户领取会员卡时从微信系统分配24位数字作为会员code，并在「用户开通会员卡」事件通知中返回；<br>（2）MERCHANT\_ALLOCATE 商家分配，商家同步会员开通结果时传入，用户开卡成功或失败都以商家传入的code作为会员卡code。选择商家分配模式时，开通事件通知中不返回 `user_card_code`。<br>2、会员卡创建后，code分配模式不支持修改。<br>可选取值<br><ul><li>`SYSTEM_ALLOCATE`:  系统分配</li><li>`MERCHANT_ALLOCATE`:  商家分配</li></ul> |
 | data.code_type | string | true | 【会员码展示类型】 会员码支持不展示码/二维码／条形码／二维码＋条形码/跳转商家小程序5种设置。<br>可选取值<br><ul><li>`NONE_CODE`:  不显示任何码型</li><li>`BAR_CODE`:  条形码</li><li>`QR_CODE`:  二维码</li><li>`BAR_CODE_AND_QR_CODE`:  条形码和二维码</li><li>`JUMP_MINI_PROGRAM`:  跳转商家小程序</li></ul> |
 | data.code_jump_information | object | false | 【会员码跳转信息】 会员码跳转的小程序信息，当会员码展示类型为跳转商家小程序时必填。 |
 | data.code_jump_information.jump_appid | string(32) | false | 【会员码跳转AppID】 会员码跳转的小程序AppID |
 | data.code_jump_information.jump_path | string(128) | false | 【会员码跳转路径】 会员码跳转的小程序路径 |
-| data.benefits | string(32) | true | 【会员权益】 会员权益是指平台、品牌或服务机构为付费会员（或等级会员）提供的专属优惠、服务或特权。 |
-| data.notify_url | string(256) | true | 【回调地址】 商家接收开卡成功回调通知的地址，需按照 [notify\_url填写注意事项](https://pay.weixin.qq.com/doc/v3/partner/4012082570.md#1.-notify_url%E5%A1%AB%E5%86%99%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9) 规范填写。 |
+| data.benefits | string(32) | false | 【会员权益】 会员权益是指平台、品牌或服务机构为付费会员（或等级会员）提供的专属优惠、服务或特权。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
+| data.notify_url | string(256) | false | 【回调地址】 商家接收开卡成功回调通知的地址，需按照 [notify\_url填写注意事项](https://pay.weixin.qq.com/doc/v3/partner/4012082570.md#1.-notify_url%E5%A1%AB%E5%86%99%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9) 规范填写。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
 | data.need_pinned | boolean | false | 【是否置顶】 置顶卡是界面中的一种特殊展示模块，通过人工设置，使其固定在内容列表的顶部位置，确保用户优先看到。默认为false。同一个品牌下允许存在多张置顶卡，按照更新时间倒序排序。 |
 | data.need_display_level | boolean | false | 【是否展示会员等级】 是否在会员卡面向用户展示等级信息，默认不展示（false） |
 | data.init_level | string(10) | false | 【会员初始等级】 展示字段，商家可以自定义填写内容。如果选择了展示会员等级，必填 `init_level`，作为新用户开卡后的初始等级。如因商家业务规则需要变更某会员等级，可通过更新用户会员卡接口更新等级信息。 |
 | data.service_phone | string(32) | false | 【服务电话】 展示在会员卡详情内，建议填写商家固定电话 |
-| data.legal_agreement | string(20480) | true | 【商家法务协议】 指用户与商家之间签订的具有法律效力的合同文件，旨在明确双方在交易、服务提供、权利义务等方面的规则，以保障交易安全、规范商业行为，并在纠纷发生时提供法律依据。不支持链接跳转，支持使用 `\n` 代表换行，只支持纯文本展示。 |
+| data.legal_agreement | string(20480) | false | 【商家法务协议】 指用户与商家之间签订的具有法律效力的合同文件，旨在明确双方在交易、服务提供、权利义务等方面的规则，以保障交易安全、规范商业行为，并在纠纷发生时提供法律依据。不支持链接跳转，支持使用 `\n` 代表换行，只支持纯文本展示。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
 | data.valid_date_information | object | true | 【会员卡有效期】 会员卡有效期 |
-| data.valid_date_information.type | string | false | 【有效期类型】 1.该有效期为会员卡激活后的有效期 2.支持绝对有效期&相对有效期设置 3.绝对有效期：固定过期时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 4.相对有效期：用户激活后x天后有效，x为天数。最多支持10,957天（30年） 5.永久有效 6.过期后卡状态变为“已过期” 7.过期后不再出现服务项，且无法给用户发送会员服务消息通知<br>可选取值<br><ul><li>`FIX_TIME_RANGE`:  必填available\_begin\_time和available\_end\_time，会员卡在此时间\[available\_begin\_time, available\_end\_time)范围内有效</li><li>`FIX_TERM`:  必填available\_day\_after\_receive，会员卡在用户领取之后available\_day\_after\_receive天内有效</li><li>`PERMANENT`:  会员卡激活后永久有效</li></ul> |
+| data.valid_date_information.type | string | true | 【有效期类型】 传入会员卡有效期时必填。1.该有效期为会员卡激活后的有效期 2.支持绝对有效期&相对有效期设置 3.绝对有效期：固定过期时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 4.相对有效期：用户激活后x天后有效，x为天数。最多支持10,957天（30年） 5.永久有效 6.过期后卡状态变为“已过期” 7.过期后不再出现服务项，且无法给用户发送会员服务消息通知<br>可选取值<br><ul><li>`FIX_TIME_RANGE`:  必填available\_begin\_time和available\_end\_time，会员卡在此时间\[available\_begin\_time, available\_end\_time)范围内有效</li><li>`FIX_TERM`:  必填available\_day\_after\_receive，会员卡在用户领取之后available\_day\_after\_receive天内有效</li><li>`PERMANENT`:  会员卡激活后永久有效</li></ul> |
 | data.valid_date_information.available_begin_time | string | false | 【有效期开始时间】 type为FIX\_TIME\_RANGE时专用， 表示有效期开始时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
 | data.valid_date_information.available_end_time | string | false | 【有效期结束时间】 type为FIX\_TIME\_RANGE时专用，表示有效期结束时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
 | data.valid_date_information.available_day_after_receive | integer | false | 【领取后N天内有效】 type为FIX\_TERM时专用，表示领取后N个自然天内有效。最长不超过30年（10958 天） |
@@ -76,7 +76,7 @@
 | data.purchase_information.price | integer | false | 【付费会员价格】 指用户为获取特定商家提供的会员权益而需支付的费用金额。（单位：分） |
 | data.purchase_information.jump_appid | string(32) | false | 【付费会员跳转AppID】 用户购买付费会员时跳转的付费会员的AppID |
 | data.purchase_information.jump_path | string(128) | false | 【付费会员跳转路径】 用户购买付费会员时购买跳转的路径 |
-| data.user_information | object | false | 【用户开卡信息】 要求用户在开通会员卡时必须填写的信息。若用户不填写则不允许开通会员卡。 |
+| data.user_information | object | false | 【用户开卡信息】 用户开通会员卡时可填写的信息。用户可以选择不填写，不影响开通会员卡；用户填写的内容会在开卡回调中返回给商家。 |
 | data.user_information.common_field_list | array[string] | false | 【平台提供的通用开卡信息字段】 平台提供的通用开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。<br>可选取值<br><ul><li>`USER_FORM_FLAG_SEX`:  用户开卡时需填写性别，字段内容可选男或女。</li><li>`USER_FORM_FLAG_NAME`:  用户开卡时需填写姓名</li><li>`USER_FORM_FLAG_BIRTHDAY`:  用户开卡时需填写生日，字段内容需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准的 `full-date` 格式：yyyy-MM-DD，表示年月日。年份必须为 4 位数，月份和日期不足两位时需补零。 示例：2015-05-20。</li><li>`USER_FORM_FLAG_ADDRESS`:  用户开卡时需填写地址</li><li>`USER_FORM_FLAG_EMAIL`:  用户开卡时需填写邮箱，字段内容需为合法邮箱。</li><li>`USER_FORM_FLAG_CITY`:  用户开卡时需填写城市，字段格式需为："省份,城市"，第一项省份，第二项城市，用英文逗号分隔。</li></ul> |
 | data.user_information.custom_field_list | array[object] | false | 【商家自定义的开卡信息字段】 商家自定义的开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。当前最多只允许传入1项。 |
 | data.user_information.custom_field_list.type | string | false | 【字段类型】 选择所需的字段类型<br>可选取值<br><ul><li>`CHECK_BOX`:  用户可从商家提供的选项中选择多项</li><li>`RADIO`:  用户可从商家提供的选项中选择一项</li></ul> |
@@ -85,6 +85,8 @@
 | data.state | string | true | 【状态】 会员卡状态信息<br>可选取值<br><ul><li>`CARD_EFFECTIVE`:  生效中</li><li>`CARD_INVALID`:  已失效</li></ul> |
 | data.create_time | string | true | 【创建时间】 创建会员卡的时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
 | data.modify_time | string | true | 【更新时间】 更新会员卡的时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
+| data.support_user_active_join | boolean | false | 【是否支持用户主动入会】 true 表示允许用户在微信支付内主动开通这张会员卡，用户可以通过商家名片、支付相关入会入口，以及商家小程序或 H5 的入会流程填写开卡信息并开通；false 表示用户不能在微信支付内主动开通，只能由商家通过导入等方式开通。 |
+| data.purchase_membership | boolean | false | 【是否为付费会员】 true 表示该会员卡是付费会员，false 表示不是。 |
 | total_count | integer | true | 【总数量】 总数量 |
 | offset | integer | true | 【分页开始位置】 该次请求的分页开始位置，从0开始计数，例如offset=10，表示从第11条记录开始返回。 |
 | limit | integer | true | 【分页大小】 分页大小，范围为1~20 |
@@ -175,7 +177,9 @@
       },
       "state" : "CARD_EFFECTIVE",
       "create_time" : "2020-05-20T13:29:35.120+08:00",
-      "modify_time" : "2020-05-20T13:29:35.120+08:00"
+      "modify_time" : "2020-05-20T13:29:35.120+08:00",
+      "support_user_active_join" : true,
+      "purchase_membership" : false
     }
   ],
   "total_count" : 20,
```

### 查询会员卡模板信息
- ID: `4015336974`
- 路径: 商家名片会员 > API列表 > 会员卡模板管理
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015336974.md
- 更新时间变更: 2025-08-01 02:53:26 -> 2026-11-11 06:34:35
- 本地文件: `pages/4015336974.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2025.08.01
+>更新时间：2026.11.11
 
 通过此接口可查询指定会员卡模板的所有信息
 
@@ -15,7 +15,7 @@
 
 　　　　　【备域名】https://api2.mch.weixin.qq.com 使用该域名将访问异地的接入点，指引[点击查看](https://pay.weixin.qq.com/doc/v3/merchant/4012075113.md)
 
-接口限频：10/秒（商户号维度）
+接口限频：100/秒（商户号维度）
 
 ## 请求参数
 
@@ -45,21 +45,21 @@
 | card_type | string | true | 【会员卡类型】 支持付费、普通、储值 3 种类型。目前仅支持普通会员卡，填写付费和储值类型时会返回错误。<br>可选取值<br><ul><li>`PURCHASE`:  付费</li><li>`NORMAL`:  普通</li><li>`BALANCE`:  储值</li></ul> |
 | card_title | string(10) | true | 【卡名称】 1.可用于展示在卡面的名称 2.支持最长10个中文字 3.支持中文字、英文字符、标点 |
 | card_color | string(7) | true | 【卡背景颜色】 用于卡片正面设计的RGB颜色编码，仅支持十六进制 |
-| card_picture_url | string(256) | true | 【卡图片】 商家自定义会员卡背景图。仅支持通过图片上传API接口获取的图片URL地址。支持JPG/JPEG/PNG格式，建议尺寸716px\*320px，且图片小于1M。查看以下链接后传入： [图片要求示例](https://gtimg.wechatpay.cn/resource/xres/img/202507/7eae51fbdbed8090d41528eda795676e_2733x716.png)， [图片上传API指引](https://pay.weixin.qq.com/doc/v3/partner/4012759802.md)。 |
-| code_mode | string | true | 【会员卡code分配类型】 1、会员卡code是会员在一个会员卡模板下唯一身份标识，平台支持2种分配类型：（1）SYSTEM\_ALLOCATE 微信支付系统分配，用户领取会员卡时从微信系统分配24位数字作为会员code；（2）MERCHANT\_ALLOCATE 商家分配，商家同步会员开通结果时传入，用户开卡成功或失败都以商家传入的code作为会员卡code 2、会员卡code分配模式若为“系统分配”，不支持修改为“商家分配”。<br>可选取值<br><ul><li>`SYSTEM_ALLOCATE`:  系统分配</li><li>`MERCHANT_ALLOCATE`:  商家分配</li></ul> |
+| card_picture_url | string(256) | false | 【卡图片】 商家自定义会员卡背景图。仅支持通过图片上传API接口获取的图片URL地址。支持JPG/JPEG/PNG格式，建议尺寸716px\*320px，且图片小于1M。查看以下链接后传入： [图片要求示例](https://gtimg.wechatpay.cn/resource/xres/img/202507/7eae51fbdbed8090d41528eda795676e_2733x716.png)， [图片上传API指引](https://pay.weixin.qq.com/doc/v3/partner/4012759802.md)。不传时没有默认卡图。 |
+| code_mode | string | true | 【会员卡code分配类型】 1、会员卡code是会员在一个会员卡模板下唯一身份标识，平台支持2种分配类型：<br>（1）SYSTEM\_ALLOCATE 微信支付系统分配，用户领取会员卡时从微信系统分配24位数字作为会员code，并在「用户开通会员卡」事件通知中返回；<br>（2）MERCHANT\_ALLOCATE 商家分配，商家同步会员开通结果时传入，用户开卡成功或失败都以商家传入的code作为会员卡code。选择商家分配模式时，开通事件通知中不返回 `user_card_code`。<br>2、会员卡创建后，code分配模式不支持修改。<br>可选取值<br><ul><li>`SYSTEM_ALLOCATE`:  系统分配</li><li>`MERCHANT_ALLOCATE`:  商家分配</li></ul> |
 | code_type | string | true | 【会员码展示类型】 会员码支持不展示码/二维码／条形码／二维码＋条形码/跳转商家小程序5种设置。<br>可选取值<br><ul><li>`NONE_CODE`:  不显示任何码型</li><li>`BAR_CODE`:  条形码</li><li>`QR_CODE`:  二维码</li><li>`BAR_CODE_AND_QR_CODE`:  条形码和二维码</li><li>`JUMP_MINI_PROGRAM`:  跳转商家小程序</li></ul> |
 | code_jump_information | object | false | 【会员码跳转信息】 会员码跳转的小程序信息，当会员码展示类型为跳转商家小程序时必填。 |
 | code_jump_information.jump_appid | string(32) | false | 【会员码跳转AppID】 会员码跳转的小程序AppID |
 | code_jump_information.jump_path | string(128) | false | 【会员码跳转路径】 会员码跳转的小程序路径 |
-| benefits | string(32) | true | 【会员权益】 会员权益是指平台、品牌或服务机构为付费会员（或等级会员）提供的专属优惠、服务或特权。 |
-| notify_url | string(256) | true | 【回调地址】 商家接收开卡成功回调通知的地址，需按照 [notify\_url填写注意事项](https://pay.weixin.qq.com/doc/v3/partner/4012082570.md#1.-notify_url%E5%A1%AB%E5%86%99%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9) 规范填写。 |
+| benefits | string(32) | false | 【会员权益】 会员权益是指平台、品牌或服务机构为付费会员（或等级会员）提供的专属优惠、服务或特权。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
+| notify_url | string(256) | false | 【回调地址】 商家接收开卡成功回调通知的地址，需按照 [notify\_url填写注意事项](https://pay.weixin.qq.com/doc/v3/partner/4012082570.md#1.-notify_url%E5%A1%AB%E5%86%99%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9) 规范填写。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
 | need_pinned | boolean | false | 【是否置顶】 置顶卡是界面中的一种特殊展示模块，通过人工设置，使其固定在内容列表的顶部位置，确保用户优先看到。默认为false。同一个品牌下允许存在多张置顶卡，按照更新时间倒序排序。 |
 | need_display_level | boolean | false | 【是否展示会员等级】 是否在会员卡面向用户展示等级信息，默认不展示（false） |
 | init_level | string(10) | false | 【会员初始等级】 展示字段，商家可以自定义填写内容。如果选择了展示会员等级，必填 `init_level`，作为新用户开卡后的初始等级。如因商家业务规则需要变更某会员等级，可通过更新用户会员卡接口更新等级信息。 |
 | service_phone | string(32) | false | 【服务电话】 展示在会员卡详情内，建议填写商家固定电话 |
-| legal_agreement | string(20480) | true | 【商家法务协议】 指用户与商家之间签订的具有法律效力的合同文件，旨在明确双方在交易、服务提供、权利义务等方面的规则，以保障交易安全、规范商业行为，并在纠纷发生时提供法律依据。不支持链接跳转，支持使用 `\n` 代表换行，只支持纯文本展示。 |
+| legal_agreement | string(20480) | false | 【商家法务协议】 指用户与商家之间签订的具有法律效力的合同文件，旨在明确双方在交易、服务提供、权利义务等方面的规则，以保障交易安全、规范商业行为，并在纠纷发生时提供法律依据。不支持链接跳转，支持使用 `\n` 代表换行，只支持纯文本展示。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
 | valid_date_information | object | true | 【会员卡有效期】 会员卡有效期 |
-| valid_date_information.type | string | false | 【有效期类型】 1.该有效期为会员卡激活后的有效期 2.支持绝对有效期&相对有效期设置 3.绝对有效期：固定过期时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 4.相对有效期：用户激活后x天后有效，x为天数。最多支持10,957天（30年） 5.永久有效 6.过期后卡状态变为“已过期” 7.过期后不再出现服务项，且无法给用户发送会员服务消息通知<br>可选取值<br><ul><li>`FIX_TIME_RANGE`:  必填available\_begin\_time和available\_end\_time，会员卡在此时间\[available\_begin\_time, available\_end\_time)范围内有效</li><li>`FIX_TERM`:  必填available\_day\_after\_receive，会员卡在用户领取之后available\_day\_after\_receive天内有效</li><li>`PERMANENT`:  会员卡激活后永久有效</li></ul> |
+| valid_date_information.type | string | true | 【有效期类型】 传入会员卡有效期时必填。1.该有效期为会员卡激活后的有效期 2.支持绝对有效期&相对有效期设置 3.绝对有效期：固定过期时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 4.相对有效期：用户激活后x天后有效，x为天数。最多支持10,957天（30年） 5.永久有效 6.过期后卡状态变为“已过期” 7.过期后不再出现服务项，且无法给用户发送会员服务消息通知<br>可选取值<br><ul><li>`FIX_TIME_RANGE`:  必填available\_begin\_time和available\_end\_time，会员卡在此时间\[available\_begin\_time, available\_end\_time)范围内有效</li><li>`FIX_TERM`:  必填available\_day\_after\_receive，会员卡在用户领取之后available\_day\_after\_receive天内有效</li><li>`PERMANENT`:  会员卡激活后永久有效</li></ul> |
 | valid_date_information.available_begin_time | string | false | 【有效期开始时间】 type为FIX\_TIME\_RANGE时专用， 表示有效期开始时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
 | valid_date_information.available_end_time | string | false | 【有效期结束时间】 type为FIX\_TIME\_RANGE时专用，表示有效期结束时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
 | valid_date_information.available_day_after_receive | integer | false | 【领取后N天内有效】 type为FIX\_TERM时专用，表示领取后N个自然天内有效。最长不超过30年（10958 天） |
@@ -76,7 +76,7 @@
 | purchase_information.price | integer | false | 【付费会员价格】 指用户为获取特定商家提供的会员权益而需支付的费用金额。（单位：分） |
 | purchase_information.jump_appid | string(32) | false | 【付费会员跳转AppID】 用户购买付费会员时跳转的付费会员的AppID |
 | purchase_information.jump_path | string(128) | false | 【付费会员跳转路径】 用户购买付费会员时购买跳转的路径 |
-| user_information | object | false | 【用户开卡信息】 要求用户在开通会员卡时必须填写的信息。若用户不填写则不允许开通会员卡。 |
+| user_information | object | false | 【用户开卡信息】 用户开通会员卡时可填写的信息。用户可以选择不填写，不影响开通会员卡；用户填写的内容会在开卡回调中返回给商家。 |
 | user_information.common_field_list | array[string] | false | 【平台提供的通用开卡信息字段】 平台提供的通用开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。<br>可选取值<br><ul><li>`USER_FORM_FLAG_SEX`:  用户开卡时需填写性别，字段内容可选男或女。</li><li>`USER_FORM_FLAG_NAME`:  用户开卡时需填写姓名</li><li>`USER_FORM_FLAG_BIRTHDAY`:  用户开卡时需填写生日，字段内容需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准的 `full-date` 格式：yyyy-MM-DD，表示年月日。年份必须为 4 位数，月份和日期不足两位时需补零。 示例：2015-05-20。</li><li>`USER_FORM_FLAG_ADDRESS`:  用户开卡时需填写地址</li><li>`USER_FORM_FLAG_EMAIL`:  用户开卡时需填写邮箱，字段内容需为合法邮箱。</li><li>`USER_FORM_FLAG_CITY`:  用户开卡时需填写城市，字段格式需为："省份,城市"，第一项省份，第二项城市，用英文逗号分隔。</li></ul> |
 | user_information.custom_field_list | array[object] | false | 【商家自定义的开卡信息字段】 商家自定义的开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。当前最多只允许传入1项。 |
 | user_information.custom_field_list.type | string | false | 【字段类型】 选择所需的字段类型<br>可选取值<br><ul><li>`CHECK_BOX`:  用户可从商家提供的选项中选择多项</li><li>`RADIO`:  用户可从商家提供的选项中选择一项</li></ul> |
@@ -85,6 +85,8 @@
 | state | string | true | 【状态】 会员卡状态信息<br>可选取值<br><ul><li>`CARD_EFFECTIVE`:  生效中</li><li>`CARD_INVALID`:  已失效</li></ul> |
 | create_time | string | true | 【创建时间】 创建会员卡的时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
 | modify_time | string | true | 【更新时间】 更新会员卡的时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
+| support_user_active_join | boolean | false | 【是否支持用户主动入会】 true 表示允许用户在微信支付内主动开通这张会员卡，用户可以通过商家名片、支付相关入会入口，以及商家小程序或 H5 的入会流程填写开卡信息并开通；false 表示用户不能在微信支付内主动开通，只能由商家通过导入等方式开通。 |
+| purchase_membership | boolean | false | 【是否为付费会员】 true 表示该会员卡是付费会员，false 表示不是。 |
 ## 错误码
 
 以下是本接口返回的错误码列表。详细错误码规则，请参考[微信支付接口规则-错误码和错误提示](https://pay.weixin.qq.com/doc/v3/partner/4012081726.md#%E9%94%99%E8%AF%AF%E7%A0%81%E5%92%8C%E9%94%99%E8%AF%AF%E6%8F%90%E7%A4%BA)
@@ -171,7 +173,9 @@
   },
   "state" : "CARD_EFFECTIVE",
   "create_time" : "2020-05-20T13:29:35.120+08:00",
-  "modify_time" : "2020-05-20T13:29:35.120+08:00"
+  "modify_time" : "2020-05-20T13:29:35.120+08:00",
+  "support_user_active_join" : true,
+  "purchase_membership" : false
 }
 
 ```
```

### 修改会员卡模板信息
- ID: `4015336977`
- 路径: 商家名片会员 > API列表 > 会员卡模板管理
- URL: https://pay.weixin.qq.com/doc/v3/partner/4015336977.md
- 更新时间变更: 2025-08-01 02:53:26 -> 2026-11-11 06:35:06
- 本地文件: `pages/4015336977.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2025.08.01
+>更新时间：2026.11.11
 
 更新会员卡的信息，包括基本信息、储值信息、开卡信息等
 
@@ -15,7 +15,7 @@
 
 　　　　　【备域名】https://api2.mch.weixin.qq.com 使用该域名将访问异地的接入点，指引[点击查看](https://pay.weixin.qq.com/doc/v3/merchant/4012075113.md)
 
-接口限频：10/秒（商户号维度）
+接口限频：100/秒（商户号维度）
 
 ## 请求参数
 
@@ -39,13 +39,13 @@
 | code_jump_information | object | false | 【会员码跳转信息】 会员码跳转的小程序信息，当会员码展示类型为跳转商家小程序时必填。 |
 | code_jump_information.jump_appid | string(32) | false | 【会员码跳转AppID】 会员码跳转的小程序AppID |
 | code_jump_information.jump_path | string(128) | false | 【会员码跳转路径】 会员码跳转的小程序路径 |
-| benefits | string(32) | false | 【会员权益】 会员权益是指平台、品牌或服务机构为付费会员（或等级会员）提供的专属优惠、服务或特权。 |
-| notify_url | string(256) | false | 【回调地址】 商家接收开卡成功回调通知的地址，需按照 [notify\_url填写注意事项](https://pay.weixin.qq.com/doc/v3/partner/4012082570.md#1.-notify_url%E5%A1%AB%E5%86%99%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9) 规范填写。 |
+| benefits | string(32) | false | 【会员权益】 会员权益是指平台、品牌或服务机构为付费会员（或等级会员）提供的专属优惠、服务或特权。支持用户主动入会时必须已填写或在本次补齐，不能改成空。不传表示不修改。 |
+| notify_url | string(256) | false | 【回调地址】 商家接收开卡成功回调通知的地址，需按照 [notify\_url填写注意事项](https://pay.weixin.qq.com/doc/v3/partner/4012082570.md#1.-notify_url%E5%A1%AB%E5%86%99%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9) 规范填写。支持用户主动入会时必须已填写或在本次补齐，不能改成空。不传表示不修改。 |
 | need_pinned | boolean | false | 【是否置顶】 置顶卡是界面中的一种特殊展示模块，通过人工设置，使其固定在内容列表的顶部位置，确保用户优先看到。默认为false。同一个品牌下允许存在多张置顶卡，按照更新时间倒序排序。 |
 | need_display_level | boolean | false | 【是否展示会员等级】 是否在会员卡面向用户展示等级信息，默认不展示（false） |
 | service_phone | string(32) | false | 【服务电话】 展示在会员卡详情内，建议填写商家固定电话 |
 | valid_date_information | object | false | 【会员卡有效期】 会员卡有效期 |
-| valid_date_information.type | string | false | 【有效期类型】 1.该有效期为会员卡激活后的有效期 2.支持绝对有效期&相对有效期设置 3.绝对有效期：固定过期时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 4.相对有效期：用户激活后x天后有效，x为天数。最多支持10,957天（30年） 5.永久有效 6.过期后卡状态变为“已过期” 7.过期后不再出现服务项，且无法给用户发送会员服务消息通知<br>可选取值<br><ul><li>`FIX_TIME_RANGE`:  必填available\_begin\_time和available\_end\_time，会员卡在此时间\[available\_begin\_time, available\_end\_time)范围内有效</li><li>`FIX_TERM`:  必填available\_day\_after\_receive，会员卡在用户领取之后available\_day\_after\_receive天内有效</li><li>`PERMANENT`:  会员卡激活后永久有效</li></ul> |
+| valid_date_information.type | string | true | 【有效期类型】 传入会员卡有效期时必填。1.该有效期为会员卡激活后的有效期 2.支持绝对有效期&相对有效期设置 3.绝对有效期：固定过期时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 4.相对有效期：用户激活后x天后有效，x为天数。最多支持10,957天（30年） 5.永久有效 6.过期后卡状态变为“已过期” 7.过期后不再出现服务项，且无法给用户发送会员服务消息通知<br>可选取值<br><ul><li>`FIX_TIME_RANGE`:  必填available\_begin\_time和available\_end\_time，会员卡在此时间\[available\_begin\_time, available\_end\_time)范围内有效</li><li>`FIX_TERM`:  必填available\_day\_after\_receive，会员卡在用户领取之后available\_day\_after\_receive天内有效</li><li>`PERMANENT`:  会员卡激活后永久有效</li></ul> |
 | valid_date_information.available_begin_time | string | false | 【有效期开始时间】 type为FIX\_TIME\_RANGE时专用， 表示有效期开始时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
 | valid_date_information.available_end_time | string | false | 【有效期结束时间】 type为FIX\_TIME\_RANGE时专用，表示有效期结束时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
 | valid_date_information.available_day_after_receive | integer | false | 【领取后N天内有效】 type为FIX\_TERM时专用，表示领取后N个自然天内有效。最长不超过30年（10958 天） |
@@ -62,12 +62,16 @@
 | purchase_information.price | integer | false | 【付费会员价格】 指用户为获取特定商家提供的会员权益而需支付的费用金额。（单位：分） |
 | purchase_information.jump_appid | string(32) | false | 【付费会员跳转AppID】 用户购买付费会员时跳转的付费会员的AppID |
 | purchase_information.jump_path | string(128) | false | 【付费会员跳转路径】 用户购买付费会员时购买跳转的路径 |
-| user_information | object | false | 【用户开卡信息】 设置用户在开通会员卡时必须填写的信息 |
+| user_information | object | false | 【用户开卡信息】 用户开通会员卡时可填写的信息。用户可以选择不填写，不影响开通会员卡；用户填写的内容会在开卡回调中返回给商家。 |
 | user_information.common_field_list | array[string] | false | 【平台提供的通用开卡信息字段】 平台提供的通用开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。<br>可选取值<br><ul><li>`USER_FORM_FLAG_SEX`:  用户开卡时需填写性别，字段内容可选男或女。</li><li>`USER_FORM_FLAG_NAME`:  用户开卡时需填写姓名</li><li>`USER_FORM_FLAG_BIRTHDAY`:  用户开卡时需填写生日，字段内容需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准的 `full-date` 格式：yyyy-MM-DD，表示年月日。年份必须为 4 位数，月份和日期不足两位时需补零。 示例：2015-05-20。</li><li>`USER_FORM_FLAG_ADDRESS`:  用户开卡时需填写地址</li><li>`USER_FORM_FLAG_EMAIL`:  用户开卡时需填写邮箱，字段内容需为合法邮箱。</li><li>`USER_FORM_FLAG_CITY`:  用户开卡时需填写城市，字段格式需为："省份,城市"，第一项省份，第二项城市，用英文逗号分隔。</li></ul> |
 | user_information.custom_field_list | array[object] | false | 【商家自定义的开卡信息字段】 商家自定义的开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。当前最多只允许传入1项。 |
 | user_information.custom_field_list.type | string | false | 【字段类型】 选择所需的字段类型<br>可选取值<br><ul><li>`CHECK_BOX`:  用户可从商家提供的选项中选择多项</li><li>`RADIO`:  用户可从商家提供的选项中选择一项</li></ul> |
 | user_information.custom_field_list.name | string(32) | false | 【字段名称】 信息项的名称。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。 |
 | user_information.custom_field_list.values | array[string(8)] | false | 【字段值】 信息项的值列表。<br>特殊规则：列表最多支持10个，单个列表限制8个字符。若商户创建会员卡模板时设置该值，则查询结果中会返回给商户。 |
+| legal_agreement | string(20480) | false | 【商家法务协议】 指用户与商家之间签订的具有法律效力的合同文件，旨在明确双方在交易、服务提供、权利义务等方面的规则，以保障交易安全、规范商业行为，并在纠纷发生时提供法律依据。不支持链接跳转，支持使用 `\n` 代表换行，只支持纯文本展示。支持用户主动入会时必须已填写或在本次补齐，不能改成空。不传表示不修改。 |
+| init_level | string(10) | false | 【会员初始等级】 展示字段，商家可以自定义填写内容。修改后「是否展示会员等级」为 true 时，必须已有会员初始等级或在本次填写，作为新用户开卡后的初始等级，与是否支持用户主动入会无关。不传表示不修改。 |
+| support_user_active_join | boolean | false | 【是否支持用户主动入会】 是否允许用户在微信支付内主动开通这张会员卡。不传表示不修改当前设置，不会因为创建时的默认值 true 重新打开已关闭的用户主动入会。改为 true 时，用户可以通过商家名片、支付相关入会入口，以及商家小程序或 H5 的入会流程填写开卡信息并开通，会员权益、回调地址、商家法务协议必须已填写或在本次补齐；改为 false 时，用户不能在微信支付内主动开通，只能由商家通过导入等方式开通，已填写的会员权益、回调地址、商家法务协议会保留，不会被清空。 |
+| purchase_membership | boolean | false | 【是否为付费会员】 标记这张会员卡是否为付费会员。不传表示不修改当前设置。本字段仅作标记，改为 true 不要求填写付费会员价格和跳转信息。 |
 ## 应答参数
 
 200 OK
@@ -81,21 +85,21 @@
 | card_type | string | true | 【会员卡类型】 支持付费、普通、储值 3 种类型。目前仅支持普通会员卡，填写付费和储值类型时会返回错误。<br>可选取值<br><ul><li>`PURCHASE`:  付费</li><li>`NORMAL`:  普通</li><li>`BALANCE`:  储值</li></ul> |
 | card_title | string(10) | true | 【卡名称】 1.可用于展示在卡面的名称 2.支持最长10个中文字 3.支持中文字、英文字符、标点 |
 | card_color | string(7) | true | 【卡背景颜色】 用于卡片正面设计的RGB颜色编码，仅支持十六进制 |
-| card_picture_url | string(256) | true | 【卡图片】 商家自定义会员卡背景图。仅支持通过图片上传API接口获取的图片URL地址。支持JPG/JPEG/PNG格式，建议尺寸716px\*320px，且图片小于1M。查看以下链接后传入： [图片要求示例](https://gtimg.wechatpay.cn/resource/xres/img/202507/7eae51fbdbed8090d41528eda795676e_2733x716.png)， [图片上传API指引](https://pay.weixin.qq.com/doc/v3/partner/4012759802.md)。 |
-| code_mode | string | true | 【会员卡code分配类型】 1、会员卡code是会员在一个会员卡模板下唯一身份标识，平台支持2种分配类型：（1）SYSTEM\_ALLOCATE 微信支付系统分配，用户领取会员卡时从微信系统分配24位数字作为会员code；（2）MERCHANT\_ALLOCATE 商家分配，商家同步会员开通结果时传入，用户开卡成功或失败都以商家传入的code作为会员卡code 2、会员卡code分配模式若为“系统分配”，不支持修改为“商家分配”。<br>可选取值<br><ul><li>`SYSTEM_ALLOCATE`:  系统分配</li><li>`MERCHANT_ALLOCATE`:  商家分配</li></ul> |
+| card_picture_url | string(256) | false | 【卡图片】 商家自定义会员卡背景图。仅支持通过图片上传API接口获取的图片URL地址。支持JPG/JPEG/PNG格式，建议尺寸716px\*320px，且图片小于1M。查看以下链接后传入： [图片要求示例](https://gtimg.wechatpay.cn/resource/xres/img/202507/7eae51fbdbed8090d41528eda795676e_2733x716.png)， [图片上传API指引](https://pay.weixin.qq.com/doc/v3/partner/4012759802.md)。不传时没有默认卡图。 |
+| code_mode | string | true | 【会员卡code分配类型】 1、会员卡code是会员在一个会员卡模板下唯一身份标识，平台支持2种分配类型：<br>（1）SYSTEM\_ALLOCATE 微信支付系统分配，用户领取会员卡时从微信系统分配24位数字作为会员code，并在「用户开通会员卡」事件通知中返回；<br>（2）MERCHANT\_ALLOCATE 商家分配，商家同步会员开通结果时传入，用户开卡成功或失败都以商家传入的code作为会员卡code。选择商家分配模式时，开通事件通知中不返回 `user_card_code`。<br>2、会员卡创建后，code分配模式不支持修改。<br>可选取值<br><ul><li>`SYSTEM_ALLOCATE`:  系统分配</li><li>`MERCHANT_ALLOCATE`:  商家分配</li></ul> |
 | code_type | string | true | 【会员码展示类型】 会员码支持不展示码/二维码／条形码／二维码＋条形码/跳转商家小程序5种设置。<br>可选取值<br><ul><li>`NONE_CODE`:  不显示任何码型</li><li>`BAR_CODE`:  条形码</li><li>`QR_CODE`:  二维码</li><li>`BAR_CODE_AND_QR_CODE`:  条形码和二维码</li><li>`JUMP_MINI_PROGRAM`:  跳转商家小程序</li></ul> |
 | code_jump_information | object | false | 【会员码跳转信息】 会员码跳转的小程序信息，当会员码展示类型为跳转商家小程序时必填。 |
 | code_jump_information.jump_appid | string(32) | false | 【会员码跳转AppID】 会员码跳转的小程序AppID |
 | code_jump_information.jump_path | string(128) | false | 【会员码跳转路径】 会员码跳转的小程序路径 |
-| benefits | string(32) | true | 【会员权益】 会员权益是指平台、品牌或服务机构为付费会员（或等级会员）提供的专属优惠、服务或特权。 |
-| notify_url | string(256) | true | 【回调地址】 商家接收开卡成功回调通知的地址，需按照 [notify\_url填写注意事项](https://pay.weixin.qq.com/doc/v3/partner/4012082570.md#1.-notify_url%E5%A1%AB%E5%86%99%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9) 规范填写。 |
+| benefits | string(32) | false | 【会员权益】 会员权益是指平台、品牌或服务机构为付费会员（或等级会员）提供的专属优惠、服务或特权。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
+| notify_url | string(256) | false | 【回调地址】 商家接收开卡成功回调通知的地址，需按照 [notify\_url填写注意事项](https://pay.weixin.qq.com/doc/v3/partner/4012082570.md#1.-notify_url%E5%A1%AB%E5%86%99%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9) 规范填写。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
 | need_pinned | boolean | false | 【是否置顶】 置顶卡是界面中的一种特殊展示模块，通过人工设置，使其固定在内容列表的顶部位置，确保用户优先看到。默认为false。同一个品牌下允许存在多张置顶卡，按照更新时间倒序排序。 |
 | need_display_level | boolean | false | 【是否展示会员等级】 是否在会员卡面向用户展示等级信息，默认不展示（false） |
 | init_level | string(10) | false | 【会员初始等级】 展示字段，商家可以自定义填写内容。如果选择了展示会员等级，必填 `init_level`，作为新用户开卡后的初始等级。如因商家业务规则需要变更某会员等级，可通过更新用户会员卡接口更新等级信息。 |
 | service_phone | string(32) | false | 【服务电话】 展示在会员卡详情内，建议填写商家固定电话 |
-| legal_agreement | string(20480) | true | 【商家法务协议】 指用户与商家之间签订的具有法律效力的合同文件，旨在明确双方在交易、服务提供、权利义务等方面的规则，以保障交易安全、规范商业行为，并在纠纷发生时提供法律依据。不支持链接跳转，支持使用 `\n` 代表换行，只支持纯文本展示。 |
+| legal_agreement | string(20480) | false | 【商家法务协议】 指用户与商家之间签订的具有法律效力的合同文件，旨在明确双方在交易、服务提供、权利义务等方面的规则，以保障交易安全、规范商业行为，并在纠纷发生时提供法律依据。不支持链接跳转，支持使用 `\n` 代表换行，只支持纯文本展示。支持用户主动入会时必填。若该值不为空，则会返回该字段。 |
 | valid_date_information | object | true | 【会员卡有效期】 会员卡有效期 |
-| valid_date_information.type | string | false | 【有效期类型】 1.该有效期为会员卡激活后的有效期 2.支持绝对有效期&相对有效期设置 3.绝对有效期：固定过期时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 4.相对有效期：用户激活后x天后有效，x为天数。最多支持10,957天（30年） 5.永久有效 6.过期后卡状态变为“已过期” 7.过期后不再出现服务项，且无法给用户发送会员服务消息通知<br>可选取值<br><ul><li>`FIX_TIME_RANGE`:  必填available\_begin\_time和available\_end\_time，会员卡在此时间\[available\_begin\_time, available\_end\_time)范围内有效</li><li>`FIX_TERM`:  必填available\_day\_after\_receive，会员卡在用户领取之后available\_day\_after\_receive天内有效</li><li>`PERMANENT`:  会员卡激活后永久有效</li></ul> |
+| valid_date_information.type | string | true | 【有效期类型】 传入会员卡有效期时必填。1.该有效期为会员卡激活后的有效期 2.支持绝对有效期&相对有效期设置 3.绝对有效期：固定过期时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 4.相对有效期：用户激活后x天后有效，x为天数。最多支持10,957天（30年） 5.永久有效 6.过期后卡状态变为“已过期” 7.过期后不再出现服务项，且无法给用户发送会员服务消息通知<br>可选取值<br><ul><li>`FIX_TIME_RANGE`:  必填available\_begin\_time和available\_end\_time，会员卡在此时间\[available\_begin\_time, available\_end\_time)范围内有效</li><li>`FIX_TERM`:  必填available\_day\_after\_receive，会员卡在用户领取之后available\_day\_after\_receive天内有效</li><li>`PERMANENT`:  会员卡激活后永久有效</li></ul> |
 | valid_date_information.available_begin_time | string | false | 【有效期开始时间】 type为FIX\_TIME\_RANGE时专用， 表示有效期开始时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
 | valid_date_information.available_end_time | string | false | 【有效期结束时间】 type为FIX\_TIME\_RANGE时专用，表示有效期结束时间。需需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
 | valid_date_information.available_day_after_receive | integer | false | 【领取后N天内有效】 type为FIX\_TERM时专用，表示领取后N个自然天内有效。最长不超过30年（10958 天） |
@@ -112,7 +116,7 @@
 | purchase_information.price | integer | false | 【付费会员价格】 指用户为获取特定商家提供的会员权益而需支付的费用金额。（单位：分） |
 | purchase_information.jump_appid | string(32) | false | 【付费会员跳转AppID】 用户购买付费会员时跳转的付费会员的AppID |
 | purchase_information.jump_path | string(128) | false | 【付费会员跳转路径】 用户购买付费会员时购买跳转的路径 |
-| user_information | object | false | 【用户开卡信息】 要求用户在开通会员卡时必须填写的信息。若用户不填写则不允许开通会员卡。 |
+| user_information | object | false | 【用户开卡信息】 用户开通会员卡时可填写的信息。用户可以选择不填写，不影响开通会员卡；用户填写的内容会在开卡回调中返回给商家。 |
 | user_information.common_field_list | array[string] | false | 【平台提供的通用开卡信息字段】 平台提供的通用开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。<br>可选取值<br><ul><li>`USER_FORM_FLAG_SEX`:  用户开卡时需填写性别，字段内容可选男或女。</li><li>`USER_FORM_FLAG_NAME`:  用户开卡时需填写姓名</li><li>`USER_FORM_FLAG_BIRTHDAY`:  用户开卡时需填写生日，字段内容需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准的 `full-date` 格式：yyyy-MM-DD，表示年月日。年份必须为 4 位数，月份和日期不足两位时需补零。 示例：2015-05-20。</li><li>`USER_FORM_FLAG_ADDRESS`:  用户开卡时需填写地址</li><li>`USER_FORM_FLAG_EMAIL`:  用户开卡时需填写邮箱，字段内容需为合法邮箱。</li><li>`USER_FORM_FLAG_CITY`:  用户开卡时需填写城市，字段格式需为："省份,城市"，第一项省份，第二项城市，用英文逗号分隔。</li></ul> |
 | user_information.custom_field_list | array[object] | false | 【商家自定义的开卡信息字段】 商家自定义的开卡信息字段。若商户在会员卡模板中设置该值，则查询结果中会返回给商户。当前最多只允许传入1项。 |
 | user_information.custom_field_list.type | string | false | 【字段类型】 选择所需的字段类型<br>可选取值<br><ul><li>`CHECK_BOX`:  用户可从商家提供的选项中选择多项</li><li>`RADIO`:  用户可从商家提供的选项中选择一项</li></ul> |
@@ -121,6 +125,8 @@
 | state | string | true | 【状态】 会员卡状态信息<br>可选取值<br><ul><li>`CARD_EFFECTIVE`:  生效中</li><li>`CARD_INVALID`:  已失效</li></ul> |
 | create_time | string | true | 【创建时间】 创建会员卡的时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
 | modify_time | string | true | 【更新时间】 更新会员卡的时间，需遵循 [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) 标准格式：yyyy-MM-DDTHH:mm:ss+TIMEZONE。yyyy-MM-DD 表示年月日；T 字符用于分隔日期和时间部分；HH:mm:ss 表示具体的时分秒；TIMEZONE 表示时区（例如，+08:00 对应东八区时间，即北京时间）。示例：2015-05-20T13:29:35+08:00 表示北京时间2015年5月20日13点29分35秒。 |
+| support_user_active_join | boolean | false | 【是否支持用户主动入会】 true 表示允许用户在微信支付内主动开通这张会员卡，用户可以通过商家名片、支付相关入会入口，以及商家小程序或 H5 的入会流程填写开卡信息并开通；false 表示用户不能在微信支付内主动开通，只能由商家通过导入等方式开通。 |
+| purchase_membership | boolean | false | 【是否为付费会员】 true 表示该会员卡是付费会员，false 表示不是。 |
 ## 错误码
 
 以下是本接口返回的错误码列表。详细错误码规则，请参考[微信支付接口规则-错误码和错误提示](https://pay.weixin.qq.com/doc/v3/partner/4012081726.md#%E9%94%99%E8%AF%AF%E7%A0%81%E5%92%8C%E9%94%99%E8%AF%AF%E6%8F%90%E7%A4%BA)
@@ -163,6 +169,7 @@
 | 400 | PARAM\_ERROR | 积分跳转 AppID 或路径为空 | 请填写积分跳转所需的AppID和页面路径 |
 | 400 | PARAM\_ERROR | 储值跳转 AppID 或路径为空 | 请填写储值跳转所需的AppID和页面路径 |
 | 400 | PARAM\_ERROR | 付费跳转 AppID 或路径为空 | 请填写付费跳转所需的AppID和页面路径 |
+| 400 | PARAM\_ERROR | 修改后是否支持用户主动入会为 true 时，会员权益、回调地址、商家法务协议必须已填写或在本次补齐 | 请补齐会员权益、回调地址、商家法务协议；若不需要用户在微信支付内主动开通，请将是否支持用户主动入会设为 false |
 | 400 | INVALID\_REQUEST | 商家未开通商家名片会员功能 | 请联系运营为该商家开通商家名片会员功能 |
 
 请求示例
@@ -238,7 +245,9 @@
   },
   "state" : "CARD_EFFECTIVE",
   "create_time" : "2020-05-20T13:29:35.120+08:00",
-  "modify_time" : "2020-05-20T13:29:35.120+08:00"
+  "modify_time" : "2020-05-20T13:29:35.120+08:00",
+  "support_user_active_join" : true,
+  "purchase_membership" : false
 }
 
 ```
```

### 投放计划配置指引
- ID: `4016111064`
- 路径: 摇一摇有优惠 > 附录
- URL: https://pay.weixin.qq.com/doc/v3/partner/4016111064.md
- 更新时间变更: 2026-06-30 09:41:15 -> 2026-11-10 07:21:18
- 本地文件: `pages/4016111064.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.06.30
+>更新时间：2026.11.10
 
 针对服务商模式可通过以下三种方式进行投放计划的配置
 
@@ -33,9 +33,9 @@
 | 价格批次 | 是 | 否 | 商品券优惠批次展示规则：<br>1、选择项，默认展示商品券下的可选优惠，包括优惠价和特价（力度+ 门槛）、券名称、券ID、券库存。<br>2、区分状态：单独失效和到期的不展示，其他展示。<br>3、对于展示的优惠批次，若关联批次券code数量不足，小于10000的特价批次置灰，提示库存不足，需大于10000。<br>选择批次时的校验规则：<br>1、券开始可用，当前系统时间>=批次生效时间<br>2、仅支持核销方式为“线上小程序核销”、“微信支付付款码核销”、“APP核销”的批次 |
 | 投放用户 | 是 | 否 | 当前仅支持“智能通投”，基于用户在微信支付的消费偏好进行投放。 |
 | 投放计划名称 | 否 | 是 | 不超过 11 个中文字符或者 22 个英文字符，该名称会在活动页面对外展示，建议与商品券名称一致。 |
-| 投放时间<br>-开始时间<br>-结束时间 | 否 | 是 | 1、投放计划的开始时间需晚于当前时间；<br>2、投放计划的持续时间不得少于 5 天；<br>3、投放计划的开始时间需晚于批次的开始时间（ `available_begin_time`）<br>4、商品券会随批次结束时间到期而直接失效，因此投放计划的结束时间需早于批次时间，保证用户不会在活动期间领取到一张立即过期的券。调用【[查询商品券指定批次](https://pay.weixin.qq.com/doc/v3/partner/4015781542.md)】接口可查询到批次配置的 `coupon_available_period`（券可核销时间）信息。<br>- 情况1: 若商品券配置了 `wait_days_after_receive`（领券后需等待N天生效）和 `available_days`（券生效后N天内可用），则投放计划的结束时间最长可配置为【 `available_end_time`（批次结束时间）- `wait_days_after_receive`（领券后需等待N天生效）- `available_days`（券生效后N天内可用） -1 】。<br>  <br>- 情况2: 若商品券没有配置了 `wait_days_after_receive`（领券后需等待N天生效）和 `available_days`（券生效后N天内可用），则投放计划的结束时间最长可配置为【 `available_end_time`（批次结束时间） -1】。 |
+| 投放时间<br>-开始时间<br>-结束时间 | 否 | 是 | 1、投放计划的开始时间需晚于当前时间；<br>2、投放计划的持续时间不得少于 5 天；<br>3、投放计划的开始时间需晚于批次的开始时间（ `available_begin_time`）<br>4、商品券会随批次结束时间到期而直接失效，因此投放计划的结束时间需早于批次时间，保证用户不会在活动期间领取到一张立即过期的券。调用【[查询商品券指定批次](https://pay.weixin.qq.com/doc/v3/partner/4015781542.md)】接口可查询到批次配置的 `coupon_available_period`（券可核销时间）信息。<br>- 情况1: 若商品券配置了 `wait_days_after_receive`（领券后需等待N天生效）和 `available_days`（券生效后N天内可用），则投放计划的结束时间最长可配置为【 `available_end_time`（批次结束时间）- `wait_days_after_receive`（领券后需等待N天生效）- `available_days`（券生效后N天内可用） -1 】。<br>  <br>- 情况2: 若商品券没有配置了 `wait_days_after_receive`（领券后需等待N天生效）和 `available_days`（券生效后N天内可用），则投放计划的结束时间最长可配置为【 `available_end_time`（批次结束时间） -1】。<br>  <br>- 情况3: 若商品券只配置了 `wait_days_after_receive`（领券后需等待N天生效）则投放计划的结束时间最长可配置为【 `available_end_time`（批次结束时间）- `wait_days_after_receive`（领券后需等待N天生效） -1 】。<br>  <br>- 情况4: 若商品券配置了 `available_days`（券生效后N天内可用），则投放计划的结束时间最长可配置为【 `available_end_time`（批次结束时间）- `available_days`（券生效后N天内可用） -1 】。 |
 | 投放限领 | 是 |  | 目前提供两种限领方式：<br>- 使用批次限领（默认）：将投放批次剩余的所有库存，单日领取上限、单用户领取上限按批次配置信息进行限领。<br>  <br>- 自定义限领：可自定义“投放库存”、“单日领取上限”、“单用户领取上限”进行限领 |
-| -投放库存 | 是 | 是 | 1、投放批次可用库存需 >=10000<br>2、投放数量需 >= 10000，并<= 券批次剩余库存 |
+| -投放库存 | 是 | 是 | 1、投放批次可用库存需 >=10000<br>2、投放总库存数量需 >= 10000，并<= 券批次剩余库存 |
 | -单日领取上限 | 是 | 是 | 需<=券批次最大发放数 |
 | -单用户领取上限 | 否 | 是 | 需<=券批次单用户领取上限 |
 | 营销标签 | 否 | 是 | 选择运营标签（N 选 1）：<br>枚举值及释义：<br>全网低价：商品价格是所有销售渠道中最低的。<br>新品特惠：新上市的商品（3个月内），价格优惠，至少和其他渠道一样便宜。<br>招牌限量：招牌为商家的最出名、卖的最好、最有特色、最好口碑的有代表性的商品。<br>爆款返场：已上架过的活动，曝光转化效果好（领取率、领取量水位线待定），再次返场。<br>省钱套餐：套餐类、优惠券类组合特惠。<br>全场立减：平台类商家的全场通用立减。<br>节日特惠：在特定节日或购物节期间提供的特别优惠。<br>限时特惠：在规定的时间段内的特别特惠。<br>出行立减：打车、单车、电单车等出行服务立减。 |
@@ -111,23 +111,20 @@
 
 
 ```mermaid
-%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
 stateDiagram-v2
-    direction LR
-    state "创建成功[1]" as S1
-    state "投放中[2]" as S2
-    state "投放暂停[3]" as S3
-    state "已过期[4]" as S4
-    state "已终止[5]" as S5
-
-    [*] --> S1: 创建活动
-    S1 --> S2: 审核通过
-    S2 --> S3: 库存用尽
-    S1 --> S4: 活动已过期
-    S2 --> S4: 活动已过期
-    S3 --> S2: 补仓库存
-    S3 --> S5: 终止活动
-    S3 --> S4: 活动已过期
-    S2 --> S5: 活动终止
-    S5 --> [*]
+  state "创建成功[1]" as S0
+  state "投放中[2]" as S1
+  state "投放暂停[3]" as S2
+  state "已过期[4]" as S3
+  state "已终止[5]" as S4
+  [*] --> S0 : 创建活动
+  S0 --> S1 : 审核通过
+  S1 --> S2 : 库存用尽
+  S1 --> S3 : 活动已过期
+  S2 --> S1 : 补仓库存
+  S2 --> S4 : 终止活动
+  S0 --> S3 : 活动已过期
+  S2 --> S3 : 活动已过期
+  S1 --> S4 : 活动终止
+  S4 --> [*]
 ```
```

### 开发指引
- ID: `4016628135`
- 路径: 品牌门店
- URL: https://pay.weixin.qq.com/doc/v3/partner/4016628135.md
- 更新时间变更: 2026-06-10 07:28:01 -> 2026-11-11 03:58:05
- 本地文件: `pages/4016628135.md`

```diff
--- old.md
+++ new.md
@@ -1,4 +1,4 @@
->更新时间：2026.06.10
+>更新时间：2026.11.11
 
 ## 1、整体业务开发流程概览
 
@@ -8,32 +8,27 @@
 | 1 | 创建门店 | 调用「[创建品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4015783183.md)」API | 商家创建新门店时，首先调用此接口获得系统分配的storeid，作为后续流程识别门店的唯一标识。 |
 | 2 | 查询门店审核状态 | 调用「[查询品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4015783153.md)」API | 1、微信侧采用机审+人审的方式进行审核，机审不确定时将会进入人审，机审效率较高预计在 1天内完成，人审预计在 7天内容完成。<br>2、审核通过门店将立即生效，若审核驳回，将返回驳回原因，请调用「[更新品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4015783158.md)」API更新信息。 |
 | 3 | 更新品牌门店信息 | 调用「[更新品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4015783158.md)」API | 若门店生效后，希望更新修改信息，可调用此接口执行，更新信息将不会影响门店的生效状态。 |
-| 4 | 绑定收款商户号 | 调用「[绑定收款商户号](https://pay.weixin.qq.com/doc/v3/partner/4015783177.md)」API | 此步骤选做，如需建立商户号和门店的关联则需调用此接口，仅支持绑定品牌下已有商户号，请先前往品牌经营平台绑定收款商户号。 |
-| 5 | 解绑收款商户号 | 调用「[解绑收款商户号](https://pay.weixin.qq.com/doc/v3/partner/4015783188.md)」API | 此步骤选做，如需解除商户号和门店的关联则调用此接口。 |
-| 6 | 删除品牌门店 | 调用「[删除品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4015783113.md)」API | 若门店已关闭，请使用此接口删除。 |
+| 4 | 删除品牌门店 | 调用「[删除品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4015783113.md)」API | 若门店已关闭，请使用此接口删除。 |
 | 若品牌方需要在品牌经营平台上管理品牌门店，可参考：[品牌经营平台管理品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4016689827.md) | 若品牌方需要在品牌经营平台上管理品牌门店，可参考：[品牌经营平台管理品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4016689827.md) | 若品牌方需要在品牌经营平台上管理品牌门店，可参考：[品牌经营平台管理品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4016689827.md) | 若品牌方需要在品牌经营平台上管理品牌门店，可参考：[品牌经营平台管理品牌门店](https://pay.weixin.qq.com/doc/v3/partner/4016689827.md) |
 
 ## 2、品牌门店状态流转图
 
 ```mermaid
-%%{init: {'themeVariables':{'edgeLabelBackground':'#ffffff'}}}%%
 stateDiagram-v2
-    direction LR
-    state "门店创建中-审核中[1]" as S1
-    state "门店创建中-审核驳回[2]" as S2
-    state "门店营业中[3]" as S3
-    state "门店营业中-审核中[1]" as S4
-    state "门店营业中-审核驳回[2]" as S5
-
-    [*] --> S1
-    S1 --> S2: 门店信息审核驳回
-    S1 --> S3: 门店信息审核通过
-    S3 --> S4: 更新修改门店信息
-    S4 --> S5: 门店信息审核驳回
-    S3 --> [*]: 删除门店
-    S2 --> S1: 修改信息重新提交
-    S4 --> S3: 门店信息审核通过
-    S5 --> S4: 修改信息重新提交
+  state "门店创建中-审核中[1]" as S0
+  state "门店创建中-审核驳回[2]" as S1
+  state "门店营业中[3]" as S2
+  state "门店营业中-审核中[1]" as S3
+  state "门店营业中-审核驳回[2]" as S4
+  [*] --> S0
+  S0 --> S1 : 门店信息审核驳回
+  S0 --> S2 : 门店信息审核通过
+  S2 --> S3 : 更新修改门店信息
+  S3 --> S4 : 门店信息审核驳回
+  S2 --> [*] : 删除门店
+  S1 --> S0 : 修改信息重新提交
+  S3 --> S2 : 门店信息审核通过
+  S4 --> S3 : 修改信息重新提交
 ```
 
 1、品牌门店有【门店状态】、【审核状态】两个状态字段，分别查询门店的生效状态和门店信息的审核状态。
```

## 附录：所有页面清单

<details>
<summary>点击查看全部 908 个页面</summary>

| 序号 | 标题（链接） | ID | 更新时间 | 完整路径 |
|------|-------------|----|----------|----------|
| 1 | [微信支付接入Skill](pages/4019636341.md) | `4019636341` | 2026-09-18 08:57:51 | Skills |
| 2 | [Go](pages/4015119446.md) | `4015119446` | 2025-05-29 03:20:44 | 示例代码 |
| 3 | [Java](pages/4014985777.md) | `4014985777` | 2025-05-27 08:03:58 | 示例代码 |
| 4 | [付款码支付（V2）](pages/4012851192.md) | `4012851192` | 2025-04-25 07:54:10 | 付款码支付（V2） |
| 5 | [刷脸支付](pages/4012851199.md) | `4012851199` | 2024-10-28 07:53:13 | 刷脸支付 |
| 6 | [产品介绍](pages/4012069852.md) | `4012069852` | 2026-05-21 03:22:54 | JSAPI支付 |
| 7 | [开发接入准备](pages/4012069853.md) | `4012069853` | 2026-10-13 13:00:01 | JSAPI支付 |
| 8 | [开发指引](pages/4012069859.md) | `4012069859` | 2026-11-02 03:09:17 | JSAPI支付 |
| 9 | [接入易错点](pages/4054250946.md) | `4054250946` | 2026-11-05 08:11:23 | JSAPI支付 |
| 10 | [常见问题](pages/4013334850.md) | `4013334850` | 2026-08-05 06:16:19 | JSAPI支付 |
| 11 | [JSAPI下单](pages/4012738519.md) | `4012738519` | 2026-10-11 07:44:07 | JSAPI支付 > API列表 |
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
| 29 | [接入易错点](pages/4054257714.md) | `4054257714` | 2026-10-30 13:29:24 | APP支付 |
| 30 | [常见问题](pages/4013080245.md) | `4013080245` | 2026-05-21 03:25:44 | APP支付 |
| 31 | [APP下单](pages/4013080231.md) | `4013080231` | 2025-03-31 06:14:51 | APP支付 > API列表 |
| 32 | [APP调起支付](pages/4013080233.md) | `4013080233` | 2025-02-18 08:14:07 | APP支付 > API列表 |
| 33 | [微信支付订单号查询订单](pages/4013080234.md) | `4013080234` | 2025-01-16 07:08:59 | APP支付 > API列表 |
| 34 | [商户订单号查询订单](pages/4013080235.md) | `4013080235` | 2025-01-16 07:08:54 | APP支付 > API列表 |
| 35 | [关闭订单](pages/4013080236.md) | `4013080236` | 2025-01-16 07:08:55 | APP支付 > API列表 |
| 36 | [支付成功回调通知](pages/4013080237.md) | `4013080237` | 2025-01-14 02:26:27 | APP支付 > API列表 |
| 37 | [申请退款](pages/4013080238.md) | `4013080238` | 2025-01-16 07:08:56 | APP支付 > API列表 |
| 38 | [查询单笔退款（按商户退款单号）](pages/4013080239.md) | `4013080239` | 2025-01-16 07:08:57 | APP支付 > API列表 |
| 39 | [发起异常退款](pages/4013080240.md) | `4013080240` | 2025-01-16 07:08:52 | APP支付 > API列表 |
| 40 | [退款结果通知](pages/4013080241.md) | `4013080241` | 2024-12-30 07:47:39 | APP支付 > API列表 |
| 41 | [申请所有/单个子商户交易账单](pages/4013080242.md) | `4013080242` | 2025-01-16 07:08:51 | APP支付 > API列表 |
| 42 | [申请服务商资金账单](pages/4013080243.md) | `4013080243` | 2025-01-16 07:08:50 | APP支付 > API列表 |
| 43 | [下载账单](pages/4013080230.md) | `4013080230` | 2024-12-23 03:48:08 | APP支付 > API列表 |
| 44 | [管理商户号绑定的APPID账号](pages/4013357894.md) | `4013357894` | 2024-12-24 02:07:53 | APP支付 > 附录 |
| 45 | [OpenSDK接入指南](pages/4013369798.md) | `4013369798` | 2024-12-25 10:48:19 | APP支付 > 附录 |
| 46 | [产品介绍](pages/4012074916.md) | `4012074916` | 2026-05-21 03:26:43 | H5支付 |
| 47 | [开发接入准备](pages/4012074917.md) | `4012074917` | 2026-05-19 08:36:25 | H5支付 |
| 48 | [开发指引](pages/4012074915.md) | `4012074915` | 2026-06-09 09:46:10 | H5支付 |
| 49 | [接入易错点](pages/4054257717.md) | `4054257717` | 2026-11-05 08:10:31 | H5支付 |
| 50 | [常见问题](pages/4013336079.md) | `4013336079` | 2026-09-01 07:43:14 | H5支付 |
| 51 | [H5下单](pages/4012738604.md) | `4012738604` | 2025-03-31 06:14:50 | H5支付 > API列表 |
| 52 | [H5调起支付](pages/4012085683.md) | `4012085683` | 2024-12-23 02:14:31 | H5支付 > API列表 |
| 53 | [支付成功回调通知](pages/4012085680.md) | `4012085680` | 2025-02-20 03:15:13 | H5支付 > API列表 |
| 54 | [微信支付订单号查询订单](pages/4012738969.md) | `4012738969` | 2025-01-16 07:08:59 | H5支付 > API列表 |
| 55 | [商户订单号查询订单](pages/4012759661.md) | `4012759661` | 2025-01-16 07:08:54 | H5支付 > API列表 |
| 56 | [关闭订单](pages/4012759669.md) | `4012759669` | 2025-01-16 07:08:55 | H5支付 > API列表 |
| 57 | [申请退款](pages/4012759673.md) | `4012759673` | 2025-01-16 07:08:56 | H5支付 > API列表 |
| 58 | [查询单笔退款（通过商户退款单号）](pages/4012759680.md) | `4012759680` | 2025-01-16 07:08:57 | H5支付 > API列表 |
| 59 | [发起异常退款](pages/4013351901.md) | `4013351901` | 2025-01-16 07:08:52 | H5支付 > API列表 |
| 60 | [退款结果通知](pages/4012085681.md) | `4012085681` | 2025-02-20 03:14:52 | H5支付 > API列表 |
| 61 | [申请所有/单个子商户交易账单](pages/4012759683.md) | `4012759683` | 2025-01-16 07:08:51 | H5支付 > API列表 |
| 62 | [申请服务商资金账单](pages/4012759690.md) | `4012759690` | 2025-01-16 07:08:50 | H5支付 > API列表 |
| 63 | [下载账单](pages/4012085682.md) | `4012085682` | 2024-12-23 03:48:08 | H5支付 > API列表 |
| 64 | [管理商户号绑定的APPID账号](pages/4013336007.md) | `4013336007` | 2024-12-23 08:19:20 | H5支付 > 附录 |
| 65 | [配置H5支付域名](pages/4013336019.md) | `4013336019` | 2026-09-18 02:15:50 | H5支付 > 附录 |
| 66 | [H5收银台适老化字体规范](pages/4013358769.md) | `4013358769` | 2024-12-24 03:30:20 | H5支付 > 附录 |
| 67 | [获取用户ip指引](pages/4018675960.md) | `4018675960` | 2026-03-13 07:56:12 | H5支付 > 附录 |
| 68 | [产品介绍](pages/4012076267.md) | `4012076267` | 2026-05-21 03:28:32 | Native支付 |
| 69 | [开发接入准备](pages/4012076268.md) | `4012076268` | 2026-05-19 08:36:38 | Native支付 |
| 70 | [开发指引](pages/4012076269.md) | `4012076269` | 2026-06-09 09:46:06 | Native支付 |
| 71 | [接入易错点](pages/4054257719.md) | `4054257719` | 2026-10-30 14:15:36 | Native支付 |
| 72 | [常见问题](pages/4013352076.md) | `4013352076` | 2026-05-21 03:29:23 | Native支付 |
| 73 | [Native下单](pages/4012738659.md) | `4012738659` | 2025-03-31 06:15:38 | Native支付 > API列表 |
| 74 | [Native调起支付](pages/4012085878.md) | `4012085878` | 2025-03-21 07:41:33 | Native支付 > API列表 |
| 75 | [支付成功回调通知](pages/4012085875.md) | `4012085875` | 2025-02-20 03:15:13 | Native支付 > API列表 |
| 76 | [关闭订单](pages/4012759725.md) | `4012759725` | 2025-01-16 07:08:55 | Native支付 > API列表 |
| 77 | [微信支付订单号查询订单](pages/4012738971.md) | `4012738971` | 2025-01-16 07:08:59 | Native支付 > API列表 |
| 78 | [商户订单号查询订单](pages/4012759714.md) | `4012759714` | 2025-01-16 07:08:54 | Native支付 > API列表 |
| 79 | [申请退款](pages/4012759727.md) | `4012759727` | 2025-01-16 07:08:56 | Native支付 > API列表 |
| 80 | [查询单笔退款（通过商户退款单号）](pages/4012759733.md) | `4012759733` | 2025-01-16 07:08:57 | Native支付 > API列表 |
| 81 | [发起异常退款](pages/4013352066.md) | `4013352066` | 2025-01-16 07:08:52 | Native支付 > API列表 |
| 82 | [退款结果回调通知](pages/4012085876.md) | `4012085876` | 2025-02-20 03:14:52 | Native支付 > API列表 |
| 83 | [申请所有/单个子商户交易账单](pages/4012759737.md) | `4012759737` | 2025-01-16 07:08:51 | Native支付 > API列表 |
| 84 | [申请服务商资金账单](pages/4012759741.md) | `4012759741` | 2025-01-16 07:08:50 | Native支付 > API列表 |
| 85 | [下载账单](pages/4012085877.md) | `4012085877` | 2024-12-23 03:48:08 | Native支付 > API列表 |
| 86 | [管理商户号绑定的APPID账号](pages/4013352075.md) | `4013352075` | 2024-12-23 07:21:48 | Native支付 > 附录 |
| 87 | [产品介绍](pages/4012085810.md) | `4012085810` | 2026-05-21 03:31:05 | 小程序支付 |
| 88 | [开发接入准备](pages/4012076731.md) | `4012076731` | 2026-05-19 08:36:53 | 小程序支付 |
| 89 | [开发指引](pages/4012076732.md) | `4012076732` | 2026-06-09 09:46:05 | 小程序支付 |
| 90 | [接入易错点](pages/4054257720.md) | `4054257720` | 2026-11-05 08:11:04 | 小程序支付 |
| 91 | [常见问题](pages/4013352071.md) | `4013352071` | 2026-08-05 09:20:10 | 小程序支付 |
| 92 | [JSAPI/小程序下单](pages/4012759974.md) | `4012759974` | 2025-03-31 06:14:54 | 小程序支付 > API列表 |
| 93 | [小程序调起支付](pages/4012085827.md) | `4012085827` | 2025-02-26 07:10:30 | 小程序支付 > API列表 |
| 94 | [支付成功回调通知](pages/4012085801.md) | `4012085801` | 2025-02-20 03:15:13 | 小程序支付 > API列表 |
| 95 | [关闭订单](pages/4012760108.md) | `4012760108` | 2025-01-16 07:08:55 | 小程序支付 > API列表 |
| 96 | [微信支付订单号查询订单](pages/4012738973.md) | `4012738973` | 2025-01-16 07:08:59 | 小程序支付 > API列表 |
| 97 | [商户订单号查询订单](pages/4012760115.md) | `4012760115` | 2025-01-16 07:08:54 | 小程序支付 > API列表 |
| 98 | [申请退款](pages/4012760121.md) | `4012760121` | 2025-01-16 07:08:56 | 小程序支付 > API列表 |
| 99 | [查询单笔退款（通过商户退款单号）](pages/4012760128.md) | `4012760128` | 2025-01-16 07:08:57 | 小程序支付 > API列表 |
| 100 | [发起异常退款](pages/4013352278.md) | `4013352278` | 2025-01-16 07:08:52 | 小程序支付 > API列表 |
| 101 | [退款结果回调通知](pages/4012085802.md) | `4012085802` | 2025-02-20 03:14:52 | 小程序支付 > API列表 |
| 102 | [申请所有/单个子商户交易账单](pages/4012760132.md) | `4012760132` | 2025-01-16 07:08:51 | 小程序支付 > API列表 |
| 103 | [申请服务商资金账单](pages/4012760136.md) | `4012760136` | 2025-01-16 07:08:50 | 小程序支付 > API列表 |
| 104 | [下载账单](pages/4012085803.md) | `4012085803` | 2024-12-23 03:48:08 | 小程序支付 > API列表 |
| 105 | [管理商户号绑定的APPID账号](pages/4013352070.md) | `4013352070` | 2024-12-23 07:21:48 | 小程序支付 > 附录 |
| 106 | [产品介绍](pages/4012079332.md) | `4012079332` | 2026-05-21 08:20:51 | JSAPI合单支付 |
| 107 | [开发接入准备](pages/4013461849.md) | `4013461849` | 2026-05-21 08:21:02 | JSAPI合单支付 |
| 108 | [开发指引](pages/4012166834.md) | `4012166834` | 2026-06-09 09:46:02 | JSAPI合单支付 |
| 109 | [接入易错点](pages/4054257619.md) | `4054257619` | 2026-10-30 13:29:40 | JSAPI合单支付 |
| 110 | [常见问题](pages/4013462212.md) | `4013462212` | 2025-01-16 08:45:12 | JSAPI合单支付 |
| 111 | [JSAPI合单下单](pages/4012757938.md) | `4012757938` | 2025-01-16 08:23:18 | JSAPI合单支付 > API列表 |
| 112 | [JSAPI调起支付](pages/4012166844.md) | `4012166844` | 2025-02-19 03:55:15 | JSAPI合单支付 > API列表 |
| 113 | [查询合单订单](pages/4013462164.md) | `4013462164` | 2025-01-17 07:39:30 | JSAPI合单支付 > API列表 |
| 114 | [关闭合单订单](pages/4013462171.md) | `4013462171` | 2025-01-16 08:23:11 | JSAPI合单支付 > API列表 |
| 115 | [合单订单支付成功回调通知](pages/4013462175.md) | `4013462175` | 2025-01-16 06:38:52 | JSAPI合单支付 > API列表 |
| 116 | [申请退款](pages/4013462183.md) | `4013462183` | 2025-01-16 07:08:56 | JSAPI合单支付 > API列表 |
| 117 | [查询单笔退款（按商户退款单号）](pages/4013462188.md) | `4013462188` | 2025-01-16 07:08:57 | JSAPI合单支付 > API列表 |
| 118 | [发起异常退款](pages/4013462191.md) | `4013462191` | 2025-01-16 07:08:52 | JSAPI合单支付 > API列表 |
| 119 | [退款结果通知](pages/4013462195.md) | `4013462195` | 2025-01-16 06:38:47 | JSAPI合单支付 > API列表 |
| 120 | [申请所有/单个子商户交易账单](pages/4013462197.md) | `4013462197` | 2025-01-16 07:08:51 | JSAPI合单支付 > API列表 |
| 121 | [申请服务商资金账单](pages/4013462202.md) | `4013462202` | 2025-01-16 07:08:50 | JSAPI合单支付 > API列表 |
| 122 | [下载账单](pages/4013462207.md) | `4013462207` | 2025-01-16 06:38:43 | JSAPI合单支付 > API列表 |
| 123 | [合单支付-商户号绑定APPID操作说明](pages/4013462628.md) | `4013462628` | 2025-01-16 06:39:56 | JSAPI合单支付 > 附录 |
| 124 | [产品介绍](pages/4012079331.md) | `4012079331` | 2026-05-21 03:36:02 | APP合单支付 |
| 125 | [开发指引](pages/4012166832.md) | `4012166832` | 2026-06-09 09:45:58 | APP合单支付 |
| 126 | [接入易错点](pages/4054257716.md) | `4054257716` | 2026-10-30 13:28:33 | APP合单支付 |
| 127 | [常见问题](pages/4013461863.md) | `4013461863` | 2025-01-16 08:45:12 | APP合单支付 |
| 128 | [APP合单下单](pages/4012758021.md) | `4012758021` | 2025-01-16 08:23:20 | APP合单支付 > API列表 |
| 129 | [APP调起支付](pages/4012166845.md) | `4012166845` | 2025-03-28 10:57:37 | APP合单支付 > API列表 |
| 130 | [查询合单订单](pages/4012761057.md) | `4012761057` | 2025-01-17 07:39:30 | APP合单支付 > API列表 |
| 131 | [关闭合单订单](pages/4012761079.md) | `4012761079` | 2025-01-16 08:23:11 | APP合单支付 > API列表 |
| 132 | [合单订单支付成功回调通知](pages/4012231898.md) | `4012231898` | 2025-01-14 09:59:26 | APP合单支付 > API列表 |
| 133 | [申请退款](pages/4012760207.md) | `4012760207` | 2025-01-16 07:08:56 | APP合单支付 > API列表 |
| 134 | [查询单笔退款（通过商户退款单号）](pages/4012760226.md) | `4012760226` | 2025-01-16 07:08:57 | APP合单支付 > API列表 |
| 135 | [发起异常退款](pages/4013461907.md) | `4013461907` | 2025-01-16 07:08:52 | APP合单支付 > API列表 |
| 136 | [退款结果回调通知](pages/4012231901.md) | `4012231901` | 2025-02-20 03:14:52 | APP合单支付 > API列表 |
| 137 | [申请所有/单个子商户交易账单](pages/4012760228.md) | `4012760228` | 2025-01-16 07:08:51 | APP合单支付 > API列表 |
| 138 | [申请服务商资金账单](pages/4012760229.md) | `4012760229` | 2025-01-16 07:08:50 | APP合单支付 > API列表 |
| 139 | [下载账单](pages/4012231933.md) | `4012231933` | 2025-01-16 06:39:27 | APP合单支付 > API列表 |
| 140 | [产品介绍](pages/4013462080.md) | `4013462080` | 2026-05-21 03:35:18 | H5合单支付 |
| 141 | [开发指引](pages/4012166833.md) | `4012166833` | 2026-06-09 09:45:46 | H5合单支付 |
| 142 | [常见问题](pages/4013462145.md) | `4013462145` | 2025-01-16 08:45:12 | H5合单支付 |
| 143 | [H5合单下单](pages/4012758208.md) | `4012758208` | 2025-01-16 08:23:19 | H5合单支付 > API列表 |
| 144 | [H5调起支付](pages/4012166846.md) | `4012166846` | 2025-01-16 06:38:59 | H5合单支付 > API列表 |
| 145 | [查询合单订单](pages/4013462099.md) | `4013462099` | 2025-01-17 07:39:30 | H5合单支付 > API列表 |
| 146 | [关闭合单订单](pages/4013462102.md) | `4013462102` | 2025-01-16 08:23:11 | H5合单支付 > API列表 |
| 147 | [合单订单支付成功回调通知](pages/4013462105.md) | `4013462105` | 2025-01-16 06:39:18 | H5合单支付 > API列表 |
| 148 | [申请退款](pages/4013462113.md) | `4013462113` | 2025-01-16 07:08:56 | H5合单支付 > API列表 |
| 149 | [查询单笔退款（按商户退款单号）](pages/4013462116.md) | `4013462116` | 2025-01-16 07:08:57 | H5合单支付 > API列表 |
| 150 | [发起异常退款](pages/4013462123.md) | `4013462123` | 2025-01-16 07:08:52 | H5合单支付 > API列表 |
| 151 | [退款结果通知](pages/4013462126.md) | `4013462126` | 2025-01-16 06:39:13 | H5合单支付 > API列表 |
| 152 | [申请所有/单个子商户交易账单](pages/4013462129.md) | `4013462129` | 2025-01-16 07:08:51 | H5合单支付 > API列表 |
| 153 | [申请服务商资金账单](pages/4013462134.md) | `4013462134` | 2025-01-16 07:08:50 | H5合单支付 > API列表 |
| 154 | [下载账单](pages/4013462137.md) | `4013462137` | 2025-01-16 06:39:09 | H5合单支付 > API列表 |
| 155 | [产品介绍](pages/4012079333.md) | `4012079333` | 2026-05-21 03:33:32 | Native合单支付 |
| 156 | [开发指引](pages/4012166835.md) | `4012166835` | 2026-06-09 09:45:53 | Native合单支付 |
| 157 | [常见问题](pages/4013462413.md) | `4013462413` | 2025-01-16 08:45:12 | Native合单支付 |
| 158 | [Native合单下单](pages/4012758240.md) | `4012758240` | 2025-01-16 08:23:16 | Native合单支付 > API列表 |
| 159 | [Native调起支付](pages/4012166843.md) | `4012166843` | 2025-03-21 07:39:13 | Native合单支付 > API列表 |
| 160 | [查询合单订单](pages/4013462240.md) | `4013462240` | 2025-01-17 07:39:30 | Native合单支付 > API列表 |
| 161 | [关闭合单订单](pages/4013462247.md) | `4013462247` | 2025-01-16 08:23:11 | Native合单支付 > API列表 |
| 162 | [合单订单支付成功回调通知](pages/4013462250.md) | `4013462250` | 2025-01-16 06:40:25 | Native合单支付 > API列表 |
| 163 | [申请退款](pages/4013462256.md) | `4013462256` | 2025-01-16 07:08:56 | Native合单支付 > API列表 |
| 164 | [查询单笔退款（按商户退款单号）](pages/4013462260.md) | `4013462260` | 2025-01-16 07:08:57 | Native合单支付 > API列表 |
| 165 | [发起异常退款](pages/4013462286.md) | `4013462286` | 2025-01-16 07:08:52 | Native合单支付 > API列表 |
| 166 | [退款结果回调通知](pages/4013462327.md) | `4013462327` | 2025-01-16 06:40:21 | Native合单支付 > API列表 |
| 167 | [申请所有/单个子商户交易账单](pages/4013462343.md) | `4013462343` | 2025-01-16 07:08:51 | Native合单支付 > API列表 |
| 168 | [申请服务商资金账单](pages/4013462358.md) | `4013462358` | 2025-01-16 07:08:50 | Native合单支付 > API列表 |
| 169 | [下载账单](pages/4013462389.md) | `4013462389` | 2025-01-16 06:40:18 | Native合单支付 > API列表 |
| 170 | [产品介绍](pages/4012079334.md) | `4012079334` | 2026-05-21 03:36:27 | 小程序合单支付 |
| 171 | [开发指引](pages/4012166836.md) | `4012166836` | 2026-06-09 09:45:44 | 小程序合单支付 |
| 172 | [接入易错点](pages/4054257721.md) | `4054257721` | 2026-10-30 13:26:03 | 小程序合单支付 |
| 173 | [常见问题](pages/4013462619.md) | `4013462619` | 2025-09-19 01:41:14 | 小程序合单支付 |
| 174 | [小程序合单下单](pages/4012758246.md) | `4012758246` | 2025-01-16 08:23:15 | 小程序合单支付 > API列表 |
| 175 | [小程序调起支付](pages/4012166847.md) | `4012166847` | 2025-01-16 06:40:11 | 小程序合单支付 > API列表 |
| 176 | [查询合单订单](pages/4013462520.md) | `4013462520` | 2025-01-17 07:39:30 | 小程序合单支付 > API列表 |
| 177 | [关闭合单订单](pages/4013462566.md) | `4013462566` | 2025-01-16 08:23:11 | 小程序合单支付 > API列表 |
| 178 | [合单订单支付成功回调通知](pages/4013462574.md) | `4013462574` | 2025-01-16 06:40:08 | 小程序合单支付 > API列表 |
| 179 | [申请退款](pages/4013462579.md) | `4013462579` | 2025-01-16 07:08:56 | 小程序合单支付 > API列表 |
| 180 | [查询单笔退款（按商户退款单号）](pages/4013462581.md) | `4013462581` | 2025-01-16 07:08:57 | 小程序合单支付 > API列表 |
| 181 | [发起异常退款](pages/4013462582.md) | `4013462582` | 2025-01-16 07:08:52 | 小程序合单支付 > API列表 |
| 182 | [退款结果回调通知](pages/4013462586.md) | `4013462586` | 2025-09-16 08:50:44 | 小程序合单支付 > API列表 |
| 183 | [申请所有/单个子商户交易账单](pages/4013462604.md) | `4013462604` | 2025-01-16 07:08:51 | 小程序合单支付 > API列表 |
| 184 | [申请服务商资金账单](pages/4013462607.md) | `4013462607` | 2025-01-16 07:08:50 | 小程序合单支付 > API列表 |
| 185 | [下载账单](pages/4013462614.md) | `4013462614` | 2025-01-16 06:39:58 | 小程序合单支付 > API列表 |
| 186 | [产品介绍](pages/4016824698.md) | `4016824698` | 2026-06-08 09:46:22 | 医保支付（服务商模式） |
| 187 | [开发接入准备](pages/4016824704.md) | `4016824704` | 2026-10-22 10:23:24 | 医保支付（服务商模式） |
| 188 | [开发指引](pages/4017149893.md) | `4017149893` | 2026-10-22 06:50:31 | 医保支付（服务商模式） |
| 189 | [接入易错点](pages/4054257722.md) | `4054257722` | 2026-10-30 13:25:18 | 医保支付（服务商模式） |
| 190 | [医保自费混合收款下单](pages/4012503131.md) | `4012503131` | 2025-12-05 03:00:28 | 医保支付（服务商模式） > API列表 > 医保自费混合订单 |
| 191 | [使用医保自费混合订单号查看下单结果](pages/4012503155.md) | `4012503155` | 2025-12-05 02:58:26 | 医保支付（服务商模式） > API列表 > 医保自费混合订单 |
| 192 | [使用服务商订单号查看下单结果](pages/4012503286.md) | `4012503286` | 2026-04-17 08:57:34 | 医保支付（服务商模式） > API列表 > 医保自费混合订单 |
| 193 | [小程序调起医保自费混合支付](pages/4012166993.md) | `4012166993` | 2024-10-25 06:46:01 | 医保支付（服务商模式） > API列表 > 医保自费混合订单 |
| 194 | [JSAPI调起医保自费混合支付](pages/4012809233.md) | `4012809233` | 2024-10-25 06:46:01 | 医保支付（服务商模式） > API列表 > 医保自费混合订单 |
| 195 | [医保混合收款成功通知](pages/4012165722.md) | `4012165722` | 2024-10-25 06:46:01 | 医保支付（服务商模式） > API列表 > 医保自费混合订单 |
| 196 | [医保退款通知](pages/4012166534.md) | `4012166534` | 2025-12-05 02:58:45 | 医保支付（服务商模式） > API列表 > 医保退款 |
| 197 | [报错排查指引](pages/4020401184.md) | `4020401184` | 2026-05-14 09:13:41 | 医保支付（服务商模式） > 常见问题 |
| 198 | [业务&接口规则类问题](pages/4017415847.md) | `4017415847` | 2026-05-14 09:14:42 | 医保支付（服务商模式） > 常见问题 |
| 199 | [申请医保支付权限](pages/4016971494.md) | `4016971494` | 2026-10-26 02:49:34 | 医保支付（服务商模式） > 附录 |
| 200 | [接入医保亲情付指引](pages/4016970670.md) | `4016970670` | 2026-05-20 06:23:29 | 医保支付（服务商模式） > 附录 |
| 201 | [UI规范与页面说明](pages/4021595914.md) | `4021595914` | 2026-06-08 09:46:27 | 医保支付（服务商模式） > 附录 |
| 202 | [测试及环境切换](pages/4021773695.md) | `4021773695` | 2026-06-11 08:58:23 | 医保支付（服务商模式） > 附录 |
| 203 | [产品介绍](pages/4018300086.md) | `4018300086` | 2026-06-08 09:46:19 | 医保支付（间连模式） |
| 204 | [开发接入准备](pages/4018300089.md) | `4018300089` | 2026-09-18 08:04:03 | 医保支付（间连模式） |
| 205 | [开发指引](pages/4016824703.md) | `4016824703` | 2026-10-22 06:50:28 | 医保支付（间连模式） |
| 206 | [接入易错点](pages/4054257723.md) | `4054257723` | 2026-10-30 14:15:25 | 医保支付（间连模式） |
| 207 | [医保自费混合收款下单](pages/4018300080.md) | `4018300080` | 2026-03-02 06:55:05 | 医保支付（间连模式） > API列表 > 医保自费混合订单 |
| 208 | [使用医保自费混合订单号查看下单结果](pages/4018300081.md) | `4018300081` | 2026-03-02 06:55:05 | 医保支付（间连模式） > API列表 > 医保自费混合订单 |
| 209 | [使用从业机构订单号查看下单结果](pages/4018300082.md) | `4018300082` | 2026-03-02 06:55:05 | 医保支付（间连模式） > API列表 > 医保自费混合订单 |
| 210 | [小程序调起医保自费混合支付](pages/4018300079.md) | `4018300079` | 2026-03-02 06:55:05 | 医保支付（间连模式） > API列表 > 医保自费混合订单 |
| 211 | [JSAPI调起医保自费混合支付](pages/4018300083.md) | `4018300083` | 2026-03-02 06:55:05 | 医保支付（间连模式） > API列表 > 医保自费混合订单 |
| 212 | [医保混合收款成功通知](pages/4018303231.md) | `4018303231` | 2026-07-03 08:22:01 | 医保支付（间连模式） > API列表 > 医保自费混合订单 |
| 213 | [医保退款通知](pages/4018300085.md) | `4018300085` | 2026-03-02 02:58:27 | 医保支付（间连模式） > API列表 > 医保退款 |
| 214 | [报错排查指引](pages/4020401288.md) | `4020401288` | 2026-05-14 09:14:51 | 医保支付（间连模式） > 常见问题 |
| 215 | [业务&接口规则类问题](pages/4018300095.md) | `4018300095` | 2026-05-14 09:21:12 | 医保支付（间连模式） > 常见问题 |
| 216 | [申请医保支付权限](pages/4016824701.md) | `4016824701` | 2026-10-26 02:50:21 | 医保支付（间连模式） > 附录 |
| 217 | [接入医保亲情付指引](pages/4018300091.md) | `4018300091` | 2026-05-20 06:44:13 | 医保支付（间连模式） > 附录 |
| 218 | [UI规范与页面说明](pages/4021595913.md) | `4021595913` | 2026-06-08 09:46:25 | 医保支付（间连模式） > 附录 |
| 219 | [测试及环境切换](pages/4021774021.md) | `4021774021` | 2026-06-11 08:58:22 | 医保支付（间连模式） > 附录 |
| 220 | [产品介绍](pages/4027117103.md) | `4027117103` | 2026-07-22 08:12:43 | 医保一码付 |
| 221 | [开发接入准备](pages/4027117104.md) | `4027117104` | 2026-07-22 08:14:15 | 医保一码付 |
| 222 | [开发指引](pages/4027117105.md) | `4027117105` | 2026-07-29 07:41:29 | 医保一码付 |
| 223 | [接入易错点](pages/4054257725.md) | `4054257725` | 2026-10-30 13:24:22 | 医保一码付 |
| 224 | [签约入口说明](pages/4027117109.md) | `4027117109` | 2026-07-29 07:26:22 | 医保一码付 > 附录 |
| 225 | [申请一码付权限](pages/4027117107.md) | `4027117107` | 2026-07-22 08:13:31 | 医保一码付 > 附录 |
| 226 | [测试信息准备和验收注意事项](pages/4027117108.md) | `4027117108` | 2026-07-22 08:08:00 | 医保一码付 > 附录 |
| 227 | [产品介绍](pages/4013080622.md) | `4013080622` | 2026-05-21 03:44:04 | 订单退款 |
| 228 | [开发接入准备](pages/4013080630.md) | `4013080630` | 2026-05-19 08:38:56 | 订单退款 |
| 229 | [开发指引](pages/4013080623.md) | `4013080623` | 2026-10-13 13:07:48 | 订单退款 |
| 230 | [业务示例代码](pages/4015217325.md) | `4015217325` | 2026-06-10 07:28:38 | 订单退款 |
| 231 | [接入易错点](pages/4054257729.md) | `4054257729` | 2026-10-30 13:23:43 | 订单退款 |
| 232 | [常见问题](pages/4013080629.md) | `4013080629` | 2026-08-05 06:12:19 | 订单退款 |
| 233 | [申请退款](pages/4013080625.md) | `4013080625` | 2025-01-16 07:08:56 | 订单退款 > API列表 |
| 234 | [查询单笔退款（通过商户退款单号）](pages/4013080626.md) | `4013080626` | 2025-01-16 07:08:57 | 订单退款 > API列表 |
| 235 | [发起异常退款](pages/4013080627.md) | `4013080627` | 2025-01-16 07:08:52 | 订单退款 > API列表 |
| 236 | [退款结果通知](pages/4013080628.md) | `4013080628` | 2024-12-30 07:47:39 | 订单退款 > API列表 |
| 237 | [退款操作指引](pages/4013080632.md) | `4013080632` | 2024-11-26 08:21:24 | 订单退款 > 附录 |
| 238 | [微信支付退款最佳实践](pages/4014960215.md) | `4014960215` | 2026-06-10 07:28:37 | 订单退款 > 附录 |
| 239 | [产品介绍](pages/4013080592.md) | `4013080592` | 2026-07-10 09:13:53 | 下载账单 |
| 240 | [开发指引](pages/4013080593.md) | `4013080593` | 2026-10-13 13:30:23 | 下载账单 |
| 241 | [业务示例代码](pages/4015988147.md) | `4015988147` | 2025-12-03 04:00:07 | 下载账单 |
| 242 | [接入易错点](pages/4054257727.md) | `4054257727` | 2026-10-30 14:14:58 | 下载账单 |
| 243 | [常见问题](pages/4013080602.md) | `4013080602` | 2026-05-09 08:57:11 | 下载账单 |
| 244 | [申请所有/单个特约商户交易账单](pages/4013080595.md) | `4013080595` | 2025-01-16 07:08:51 | 下载账单 > API列表 |
| 245 | [申请服务商资金账单](pages/4013080596.md) | `4013080596` | 2025-01-16 07:08:50 | 下载账单 > API列表 |
| 246 | [申请单个子商户资金账单](pages/4012760249.md) | `4012760249` | 2024-10-21 08:45:00 | 下载账单 > API列表 |
| 247 | [下载账单](pages/4013080597.md) | `4013080597` | 2024-12-23 03:48:08 | 下载账单 > API列表 |
| 248 | [交易账单详细说明](pages/4013080599.md) | `4013080599` | 2026-01-16 03:53:05 | 下载账单 > 附录 |
| 249 | [资金账单详细说明](pages/4013080600.md) | `4013080600` | 2024-11-26 08:21:16 | 下载账单 > 附录 |
| 250 | [平台下载账单操作指引](pages/4013080601.md) | `4013080601` | 2024-11-26 08:21:11 | 下载账单 > 附录 |
| 251 | [产品介绍](pages/4012072582.md) | `4012072582` | 2025-05-13 02:17:34 | 分账 |
| 252 | [开发接入准备](pages/4012072589.md) | `4012072589` | 2026-05-19 09:30:27 | 分账 |
| 253 | [开发指引](pages/4012072601.md) | `4012072601` | 2026-06-09 09:46:15 | 分账 |
| 254 | [接入易错点](pages/4054257730.md) | `4054257730` | 2026-10-30 13:24:12 | 分账 |
| 255 | [常见问题](pages/4014547107.md) | `4014547107` | 2026-08-05 06:16:06 | 分账 |
| 256 | [请求分账](pages/4012690683.md) | `4012690683` | 2025-09-29 01:58:27 | 分账 > API列表 |
| 257 | [查询分账结果](pages/4012466850.md) | `4012466850` | 2025-09-29 03:51:23 | 分账 > API列表 |
| 258 | [请求分账回退](pages/4012466854.md) | `4012466854` | 2025-09-29 03:50:46 | 分账 > API列表 |
| 259 | [查询分账回退结果](pages/4012466858.md) | `4012466858` | 2025-09-29 03:49:39 | 分账 > API列表 |
| 260 | [解冻剩余资金](pages/4012466860.md) | `4012466860` | 2025-09-29 03:49:07 | 分账 > API列表 |
| 261 | [查询剩余待分金额](pages/4012457927.md) | `4012457927` | 2025-09-29 03:48:45 | 分账 > API列表 |
| 262 | [查询最大分账比例](pages/4012466864.md) | `4012466864` | 2025-09-29 03:48:29 | 分账 > API列表 |
| 263 | [添加分账接收方](pages/4012690944.md) | `4012690944` | 2025-09-29 03:48:04 | 分账 > API列表 |
| 264 | [删除分账接收方](pages/4012466868.md) | `4012466868` | 2025-09-29 03:47:32 | 分账 > API列表 |
| 265 | [分账动账通知](pages/4012075216.md) | `4012075216` | 2025-02-19 03:56:03 | 分账 > API列表 |
| 266 | [申请分账账单](pages/4012761140.md) | `4012761140` | 2025-09-29 03:47:03 | 分账 > API列表 |
| 267 | [下载账单](pages/4012075366.md) | `4012075366` | 2024-10-30 06:42:53 | 分账 > API列表 |
| 268 | [分账失败处理指引](pages/4015504885.md) | `4015504885` | 2025-07-04 03:08:11 | 分账 > 附录 |
| 269 | [产品介绍](pages/4019514964.md) | `4019514964` | 2026-06-30 08:50:38 | 停车缴费服务 |
| 270 | [开发接入准备](pages/4019515014.md) | `4019515014` | 2026-07-23 03:49:02 | 停车缴费服务 |
| 271 | [开发指引](pages/4020339052.md) | `4020339052` | 2026-06-30 08:50:38 | 停车缴费服务 |
| 272 | [接入易错点](pages/4054257726.md) | `4054257726` | 2026-10-30 13:24:53 | 停车缴费服务 |
| 273 | [常见问题](pages/4019514982.md) | `4019514982` | 2026-06-30 08:50:38 | 停车缴费服务 |
| 274 | [提交停车场进件申请](pages/4019557780.md) | `4019557780` | 2026-06-29 02:59:56 | 停车缴费服务 > API列表 |
| 275 | [查询停车场进件申请单](pages/4019557794.md) | `4019557794` | 2026-06-29 02:59:56 | 停车缴费服务 > API列表 |
| 276 | [查询停车场进件申请单列表](pages/4019557811.md) | `4019557811` | 2026-06-29 02:59:56 | 停车缴费服务 > API列表 |
| 277 | [撤回停车场进件申请](pages/4019557799.md) | `4019557799` | 2026-06-29 02:59:56 | 停车缴费服务 > API列表 |
| 278 | [同步车辆入场通知](pages/4019557757.md) | `4019557757` | 2026-06-29 02:59:56 | 停车缴费服务 > API列表 |
| 279 | [同步车辆离场通知](pages/4019557725.md) | `4019557725` | 2026-06-29 02:59:56 | 停车缴费服务 > API列表 |
| 280 | [同步支付结果通知](pages/4019557765.md) | `4019557765` | 2026-06-29 02:59:56 | 停车缴费服务 > API列表 |
| 281 | [同步非临停扩展支付](pages/4020338487.md) | `4020338487` | 2026-06-29 02:59:56 | 停车缴费服务 > API列表 |
| 282 | [查询停车场信息](pages/4023070758.md) | `4023070758` | 2026-06-29 02:59:56 | 停车缴费服务 > API列表 |
| 283 | [查询停车费用](pages/4019557825.md) | `4019557825` | 2026-06-29 02:59:56 | 停车缴费服务 > API列表 |
| 284 | [商户查费回调](pages/4024070065.md) | `4024070065` | 2026-08-13 09:05:25 | 停车缴费服务 > API列表 |
| 285 | [产品介绍](pages/4012586132.md) | `4012586132` | 2026-05-26 09:26:57 | 微信支付分 |
| 286 | [开发接入准备](pages/4012586133.md) | `4012586133` | 2026-10-20 02:53:34 | 微信支付分 |
| 287 | [开发指引](pages/4012586134.md) | `4012586134` | 2026-10-20 02:54:40 | 微信支付分 |
| 288 | [接入易错点](pages/4054257731.md) | `4054257731` | 2026-10-30 13:22:44 | 微信支付分 |
| 289 | [常见问题](pages/4012586139.md) | `4012586139` | 2026-05-09 08:57:42 | 微信支付分 |
| 290 | [创建支付分订单](pages/4013138534.md) | `4013138534` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 291 | [查询支付分订单](pages/4013138559.md) | `4013138559` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 292 | [取消支付分订单](pages/4013138589.md) | `4013138589` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 293 | [确认订单回调通知](pages/4012586137.md) | `4012586137` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 294 | [完结支付分订单](pages/4013138598.md) | `4013138598` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 295 | [修改支付分订单金额](pages/4013138819.md) | `4013138819` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 296 | [同步支付分订单状态](pages/4013138975.md) | `4013138975` | 2024-12-06 08:29:39 | 微信支付分 > API列表 |
| 297 | [支付成功回调通知](pages/4012586136.md) | `4012586136` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 298 | [申请退款](pages/4013138987.md) | `4013138987` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 299 | [查询退款](pages/4013139077.md) | `4013139077` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 300 | [退款结果通知](pages/4012586138.md) | `4012586138` | 2024-12-06 08:29:26 | 微信支付分 > API列表 |
| 301 | [JSAPI调起支付分确认订单页](pages/4012607505.md) | `4012607505` | 2024-12-05 07:33:34 | 微信支付分 > API列表 > 拉起支付分小程序确认订单页 |
| 302 | [Android](pages/4012607507.md) | `4012607507` | 2024-12-05 07:31:51 | 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > APP调起支付分确认订单页 |
| 303 | [iOS](pages/4012607508.md) | `4012607508` | 2024-12-05 07:32:18 | 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > APP调起支付分确认订单页 |
| 304 | [鸿蒙](pages/4015271745.md) | `4015271745` | 2025-06-18 06:57:03 | 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > APP调起支付分确认订单页 |
| 305 | [wx.openBusinessView](pages/4012607510.md) | `4012607510` | 2024-12-05 07:32:49 | 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > 小程序调起支付分确认订单页 |
| 306 | [wx.navigateToMiniProgram（停止新增）](pages/4012607511.md) | `4012607511` | 2024-12-05 07:33:11 | 微信支付分 > API列表 > 拉起支付分小程序确认订单页 > 小程序调起支付分确认订单页 |
| 307 | [JSAPI调起支付分订单详情页](pages/4012607518.md) | `4012607518` | 2024-12-05 07:36:11 | 微信支付分 > API列表 > 拉起支付分小程序订单详情页 |
| 308 | [Android](pages/4012607513.md) | `4012607513` | 2024-12-05 07:34:23 | 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > APP调起支付分订单详情页 |
| 309 | [iOS](pages/4012607514.md) | `4012607514` | 2024-12-05 07:34:53 | 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > APP调起支付分订单详情页 |
| 310 | [鸿蒙](pages/4015271776.md) | `4015271776` | 2025-06-18 06:57:00 | 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > APP调起支付分订单详情页 |
| 311 | [wx.openBusinessView](pages/4012607516.md) | `4012607516` | 2024-12-05 07:35:16 | 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > 小程序调起支付分订单详情页 |
| 312 | [wx.navigateToMiniProgram（停止新增）](pages/4012607517.md) | `4012607517` | 2024-12-05 07:35:36 | 微信支付分 > API列表 > 拉起支付分小程序订单详情页 > 小程序调起支付分订单详情页 |
| 313 | [支付分合作品牌线上应用规范](pages/4012586152.md) | `4012586152` | 2025-03-20 07:09:22 | 微信支付分 > 附录 |
| 314 | [支付分权限申请邮件模板](pages/4012586142.md) | `4012586142` | 2024-12-09 02:47:16 | 微信支付分 > 附录 |
| 315 | [测试微信号配置指引](pages/4012586141.md) | `4012586141` | 2024-12-09 10:14:05 | 微信支付分 > 附录 |
| 316 | [服务ID新增绑定邮件流程](pages/4012624851.md) | `4012624851` | 2024-12-09 10:13:56 | 微信支付分 > 附录 |
| 317 | [总览](pages/4013163663.md) | `4013163663` | 2024-12-09 09:41:21 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 318 | [二轮电动车充电桩](pages/4012586150.md) | `4012586150` | 2024-12-09 09:41:03 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 319 | [充电宝](pages/4012586148.md) | `4012586148` | 2024-12-09 09:40:59 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 320 | [共享单车](pages/4012586145.md) | `4012586145` | 2024-12-09 09:40:55 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 321 | [快递行业](pages/4012586144.md) | `4012586144` | 2024-12-09 09:40:52 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 322 | [智慧零售(无人设备)](pages/4012586146.md) | `4012586146` | 2026-08-20 10:19:32 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 323 | [汽车充电桩](pages/4012586149.md) | `4012586149` | 2024-12-09 09:40:46 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 324 | [汽车租赁](pages/4012586151.md) | `4012586151` | 2024-12-09 09:40:42 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 325 | [酒店行业](pages/4012586147.md) | `4012586147` | 2024-12-09 10:14:02 | 微信支付分 > 附录 > post_payments(后付费项目)字段传参说明 |
| 326 | [产品介绍](pages/4012085549.md) | `4012085549` | 2026-06-12 09:58:58 | 微信支付分停车服务 |
| 327 | [开发接入准备](pages/4012085632.md) | `4012085632` | 2026-06-12 09:59:11 | 微信支付分停车服务 |
| 328 | [开发指引](pages/4012085711.md) | `4012085711` | 2026-10-19 08:12:08 | 微信支付分停车服务 |
| 329 | [接入易错点](pages/4054257732.md) | `4054257732` | 2026-10-30 13:22:03 | 微信支付分停车服务 |
| 330 | [常见问题](pages/4016183529.md) | `4016183529` | 2025-12-12 02:16:53 | 微信支付分停车服务 |
| 331 | [创建停车入场](pages/4012533994.md) | `4012533994` | 2025-02-21 08:25:44 | 微信支付分停车服务 > API列表 > 停车入场 |
| 332 | [停车入场状态变更通知](pages/4012085798.md) | `4012085798` | 2025-02-19 07:23:03 | 微信支付分停车服务 > API列表 > 停车入场 |
| 333 | [查询车牌服务开通信息](pages/4012534183.md) | `4012534183` | 2025-02-21 08:25:08 | 微信支付分停车服务 > API列表 > 服务 |
| 334 | [小程序调起微信支付分停车服务开通页](pages/4012085969.md) | `4012085969` | 2024-10-31 07:43:33 | 微信支付分停车服务 > API列表 > 服务 |
| 335 | [H5调起微信支付分停车服务开通页](pages/4012085997.md) | `4012085997` | 2024-10-31 07:46:05 | 微信支付分停车服务 > API列表 > 服务 |
| 336 | [App拉起微信支付分停车服务开通页](pages/4012086028.md) | `4012086028` | 2024-10-22 09:54:33 | 微信支付分停车服务 > API列表 > 服务 |
| 337 | [查询订单](pages/4012534441.md) | `4012534441` | 2025-02-21 08:26:35 | 微信支付分停车服务 > API列表 > 扣费受理 |
| 338 | [扣费受理](pages/4012534427.md) | `4012534427` | 2025-03-11 03:03:56 | 微信支付分停车服务 > API列表 > 扣费受理 |
| 339 | [订单支付结果通知](pages/4012086059.md) | `4012086059` | 2025-02-19 07:20:38 | 微信支付分停车服务 > API列表 > 扣费受理 |
| 340 | [微信垫资还款](pages/4012086207.md) | `4012086207` | 2024-11-04 02:10:45 | 微信支付分停车服务 > API列表 > 还款 |
| 341 | [退款申请](pages/4012760545.md) | `4012760545` | 2025-04-07 01:50:02 | 微信支付分停车服务 > API列表 > 退款 |
| 342 | [退款结果通知](pages/4012086319.md) | `4012086319` | 2025-02-20 03:14:52 | 微信支付分停车服务 > API列表 > 退款 |
| 343 | [查询单笔退款（通过商户退款单号）](pages/4012760554.md) | `4012760554` | 2025-04-07 01:49:56 | 微信支付分停车服务 > API列表 > 退款 |
| 344 | [现金红包（V2）](pages/4012851209.md) | `4012851209` | 2025-04-25 07:53:50 | 现金红包（V2） |
| 345 | [产品介绍](pages/4012087800.md) | `4012087800` | 2025-10-14 07:18:06 | 代金券 |
| 346 | [开发接入准备](pages/4012087801.md) | `4012087801` | 2026-05-19 08:44:06 | 代金券 |
| 347 | [开发指引](pages/4012087802.md) | `4012087802` | 2026-06-09 07:58:19 | 代金券 |
| 348 | [接入易错点](pages/4054257733.md) | `4054257733` | 2026-10-31 09:44:18 | 代金券 |
| 349 | [常见问题](pages/4015880931.md) | `4015880931` | 2025-12-19 02:28:02 | 代金券 |
| 350 | [核销事件回调通知](pages/4012285807.md) | `4012285807` | 2025-02-20 07:10:47 | 代金券 > API列表 |
| 351 | [图片上传（营销专用）](pages/4012759802.md) | `4012759802` | 2024-11-18 09:26:00 | 代金券 > API列表 |
| 352 | [创建代金券批次](pages/4012534537.md) | `4012534537` | 2024-11-18 09:25:53 | 代金券 > API列表 > 批次 |
| 353 | [激活代金券批次](pages/4012460237.md) | `4012460237` | 2024-11-18 09:26:00 | 代金券 > API列表 > 批次 |
| 354 | [暂停代金券批次](pages/4012460340.md) | `4012460340` | 2024-11-18 09:26:00 | 代金券 > API列表 > 批次 |
| 355 | [重启代金券批次](pages/4012460448.md) | `4012460448` | 2024-11-18 09:25:43 | 代金券 > API列表 > 批次 |
| 356 | [条件查询批次列表](pages/4012460518.md) | `4012460518` | 2025-03-25 08:44:52 | 代金券 > API列表 > 批次 |
| 357 | [查询批次详情](pages/4012460606.md) | `4012460606` | 2025-03-25 08:44:50 | 代金券 > API列表 > 批次 |
| 358 | [查询代金券可用商户](pages/4012463409.md) | `4012463409` | 2024-11-18 09:25:45 | 代金券 > API列表 > 批次 |
| 359 | [查询代金券可用单品](pages/4012463475.md) | `4012463475` | 2024-11-18 09:25:55 | 代金券 > API列表 > 批次 |
| 360 | [下载批次退款明细](pages/4012463548.md) | `4012463548` | 2024-11-18 09:25:43 | 代金券 > API列表 > 批次 |
| 361 | [下载批次核销明细](pages/4012463698.md) | `4012463698` | 2024-11-18 09:25:53 | 代金券 > API列表 > 批次 |
| 362 | [根据商户号查用户的券](pages/4012494237.md) | `4012494237` | 2024-11-18 09:25:43 | 代金券 > API列表 > 券 |
| 363 | [发放指定批次的代金券](pages/4012463807.md) | `4012463807` | 2024-11-18 09:25:41 | 代金券 > API列表 > 券 |
| 364 | [查询代金券详情](pages/4012492796.md) | `4012492796` | 2024-11-18 09:26:04 | 代金券 > API列表 > 券 |
| 365 | [查询代金券消息通知地址](pages/4012464155.md) | `4012464155` | 2026-10-14 10:37:21 | 代金券 > API列表 > 消息通知地址 |
| 366 | [设置代金券消息通知地址](pages/4012464176.md) | `4012464176` | 2026-10-14 10:37:20 | 代金券 > API列表 > 消息通知地址 |
| 367 | [产品介绍](pages/4012071996.md) | `4012071996` | 2024-07-23 08:00:45 | 委托营销 |
| 368 | [开发接入准备](pages/4012071997.md) | `4012071997` | 2026-05-19 08:45:58 | 委托营销 |
| 369 | [开发指引](pages/4012071998.md) | `4012071998` | 2026-10-19 08:26:53 | 委托营销 |
| 370 | [建立合作关系](pages/4012381469.md) | `4012381469` | 2026-10-16 01:54:44 | 委托营销 > API列表 |
| 371 | [查询合作关系列表](pages/4012381479.md) | `4012381479` | 2024-11-18 09:25:58 | 委托营销 > API列表 |
| 372 | [产品介绍](pages/4012072117.md) | `4012072117` | 2025-11-11 11:20:38 | 支付有礼 |
| 373 | [开发接入准备](pages/4012072118.md) | `4012072118` | 2026-05-19 08:46:11 | 支付有礼 |
| 374 | [开发指引](pages/4012072119.md) | `4012072119` | 2026-06-09 09:46:59 | 支付有礼 |
| 375 | [接入易错点](pages/4055251397.md) | `4055251397` | 2026-11-05 02:53:52 | 支付有礼 |
| 376 | [图片上传（营销专用）](pages/4012760270.md) | `4012760270` | 2024-11-18 09:26:00 | 支付有礼 > API列表 |
| 377 | [创建全场满额送活动](pages/4012492900.md) | `4012492900` | 2024-11-18 09:25:56 | 支付有礼 > API列表 > 支付有礼活动 |
| 378 | [获取活动详情接口](pages/4012492967.md) | `4012492967` | 2024-11-18 09:25:58 | 支付有礼 > API列表 > 支付有礼活动 |
| 379 | [获取活动发券商户号](pages/4012466191.md) | `4012466191` | 2024-11-18 09:25:52 | 支付有礼 > API列表 > 支付有礼活动 |
| 380 | [获取活动指定商品列表](pages/4012466492.md) | `4012466492` | 2024-11-18 09:25:51 | 支付有礼 > API列表 > 支付有礼活动 |
| 381 | [终止活动](pages/4012466633.md) | `4012466633` | 2024-11-18 09:25:39 | 支付有礼 > API列表 > 支付有礼活动 |
| 382 | [新增活动发券商户号](pages/4012466735.md) | `4012466735` | 2024-11-18 09:25:55 | 支付有礼 > API列表 > 支付有礼活动 |
| 383 | [获取支付有礼活动列表](pages/4012493214.md) | `4012493214` | 2024-11-18 09:25:51 | 支付有礼 > API列表 > 支付有礼活动 |
| 384 | [删除活动发券商户号](pages/4012466827.md) | `4012466827` | 2024-11-18 09:25:40 | 支付有礼 > API列表 > 支付有礼活动 |
| 385 | [产品介绍](pages/4012072233.md) | `4012072233` | 2025-03-21 10:25:07 | 小程序发券插件 |
| 386 | [开发接入准备](pages/4012072234.md) | `4012072234` | 2026-05-19 08:46:25 | 小程序发券插件 |
| 387 | [接入易错点](pages/4054257736.md) | `4054257736` | 2026-10-30 13:21:43 | 小程序发券插件 |
| 388 | [小程序发券插件](pages/4012285878.md) | `4012285878` | 2025-02-19 03:55:31 | 小程序发券插件 > API列表 |
| 389 | [产品介绍](pages/4012075048.md) | `4012075048` | 2025-03-21 07:41:31 | H5发券 |
| 390 | [开发接入准备](pages/4012075086.md) | `4012075086` | 2026-05-19 08:46:39 | H5发券 |
| 391 | [H5发券](pages/4012285900.md) | `4012285900` | 2025-03-21 07:39:58 | H5发券 > API列表 |
| 392 | [产品介绍](pages/4012075220.md) | `4012075220` | 2025-03-21 07:41:21 | 智慧商圈 |
| 393 | [开发接入准备](pages/4012075231.md) | `4012075231` | 2026-05-19 08:46:54 | 智慧商圈 |
| 394 | [开发指引](pages/4012075386.md) | `4012075386` | 2026-06-09 07:58:14 | 智慧商圈 |
| 395 | [接入易错点](pages/4054257737.md) | `4054257737` | 2026-10-30 13:19:25 | 智慧商圈 |
| 396 | [常见问题](pages/4016111726.md) | `4016111726` | 2026-08-07 08:09:47 | 智慧商圈 |
| 397 | [商圈会员积分服务授权结果通知](pages/4012076406.md) | `4012076406` | 2025-02-19 03:56:03 | 智慧商圈 > API列表 |
| 398 | [商圈会员场内支付结果通知](pages/4012076414.md) | `4012076414` | 2025-02-19 03:56:03 | 智慧商圈 > API列表 |
| 399 | [商圈会员积分同步](pages/4012474133.md) | `4012474133` | 2024-11-18 09:25:47 | 智慧商圈 > API列表 |
| 400 | [商圈会员场内退款结果通知](pages/4012076419.md) | `4012076419` | 2025-02-19 03:56:03 | 智慧商圈 > API列表 |
| 401 | [商圈会员积分服务授权查询](pages/4012474135.md) | `4012474135` | 2024-11-18 09:25:40 | 智慧商圈 > API列表 |
| 402 | [商圈会员待积分状态查询](pages/4012474129.md) | `4012474129` | 2024-11-28 06:23:32 | 智慧商圈 > API列表 |
| 403 | [商圈会员停车状态同步](pages/4012474127.md) | `4012474127` | 2024-11-28 06:23:40 | 智慧商圈 > API列表 |
| 404 | [产品介绍](pages/4012076036.md) | `4012076036` | 2026-06-10 07:28:54 | 支付即服务 |
| 405 | [开发接入准备](pages/4012076037.md) | `4012076037` | 2026-05-19 08:47:09 | 支付即服务 |
| 406 | [开发指引](pages/4012076038.md) | `4012076038` | 2026-06-09 09:46:56 | 支付即服务 |
| 407 | [常见问题](pages/4016913657.md) | `4016913657` | 2025-12-19 02:14:14 | 支付即服务 |
| 408 | [服务人员查询](pages/4012688558.md) | `4012688558` | 2025-01-09 03:09:59 | 支付即服务 > API列表 |
| 409 | [服务人员注册](pages/4012688564.md) | `4012688564` | 2025-01-09 03:10:21 | 支付即服务 > API列表 |
| 410 | [服务人员更新](pages/4012688570.md) | `4012688570` | 2025-01-09 03:10:22 | 支付即服务 > API列表 |
| 411 | [服务人员分配](pages/4012474145.md) | `4012474145` | 2024-11-18 09:26:02 | 支付即服务 > API列表 |
| 412 | [服务人员称谓申请指引](pages/4012076039.md) | `4012076039` | 2024-07-24 02:26:28 | 支付即服务 > 附录 |
| 413 | [免开发版本操作指引](pages/4012076040.md) | `4012076040` | 2026-10-20 10:23:28 | 支付即服务 > 附录 |
| 414 | [个人微信服务人员注册](pages/4012076041.md) | `4012076041` | 2024-08-02 07:09:59 | 支付即服务 > 附录 |
| 415 | [产品介绍](pages/4012072130.md) | `4012072130` | 2025-09-04 06:45:36 | 点金计划 |
| 416 | [开发接入准备](pages/4012072158.md) | `4012072158` | 2026-10-20 10:23:07 | 点金计划 |
| 417 | [开发指引](pages/4012072262.md) | `4012072262` | 2026-06-09 09:46:53 | 点金计划 |
| 418 | [常见问题](pages/4016241762.md) | `4016241762` | 2026-01-23 03:27:42 | 点金计划 |
| 419 | [点金计划管理](pages/4012473796.md) | `4012473796` | 2024-11-18 09:26:00 | 点金计划 > API列表 |
| 420 | [商家小票管理](pages/4012473788.md) | `4012473788` | 2024-11-18 09:25:49 | 点金计划 > API列表 |
| 421 | [同业过滤标签管理](pages/4012473784.md) | `4012473784` | 2024-11-18 09:25:53 | 点金计划 > API列表 |
| 422 | [开通广告展示](pages/4012473794.md) | `4012473794` | 2024-11-18 09:25:55 | 点金计划 > API列表 |
| 423 | [关闭广告展示](pages/4012473781.md) | `4012473781` | 2024-11-18 09:25:47 | 点金计划 > API列表 |
| 424 | [小程序左上角返回键管理](pages/4012072514.md) | `4012072514` | 2025-02-19 07:20:53 | 点金计划 > API列表 |
| 425 | [产品介绍](pages/4016433410.md) | `4016433410` | 2026-04-02 14:46:39 | 品牌入驻 |
| 426 | [开发指引](pages/4016985537.md) | `4016985537` | 2026-10-20 08:20:32 | 品牌入驻 |
| 427 | [常见问题](pages/4017027854.md) | `4017027854` | 2026-01-04 03:49:11 | 品牌入驻 |
| 428 | [提交入驻申请](pages/4016249989.md) | `4016249989` | 2025-10-23 06:29:49 | 品牌入驻 > API列表 |
| 429 | [根据业务申请编号查询申请状态](pages/4016257694.md) | `4016257694` | 2025-10-23 06:29:49 | 品牌入驻 > API列表 |
| 430 | [根据申请单ID查询申请状态](pages/4016257685.md) | `4016257685` | 2025-10-23 06:29:49 | 品牌入驻 > API列表 |
| 431 | [撤销申请](pages/4016257700.md) | `4016257700` | 2025-10-23 06:29:49 | 品牌入驻 > API列表 |
| 432 | [图片上传](pages/4016276333.md) | `4016276333` | 2025-10-23 06:29:49 | 品牌入驻 > API列表 |
| 433 | [品牌能力介绍](pages/4016433389.md) | `4016433389` | 2026-04-02 12:48:03 | 品牌入驻 > 附录 |
| 434 | [服务商申请品牌授权流程](pages/4016026183.md) | `4016026183` | 2026-03-11 09:48:51 | 品牌入驻 > 附录 |
| 435 | [产品介绍](pages/4016433952.md) | `4016433952` | 2025-11-12 07:52:53 | 商家名片 |
| 436 | [常见问题](pages/4017027862.md) | `4017027862` | 2026-01-04 03:49:05 | 商家名片 |
| 437 | [商家名片开发指引](pages/4016914463.md) | `4016914463` | 2026-06-10 07:28:50 | 商家名片 > 开发指引 |
| 438 | [交易连接名片开发指引](pages/4016985845.md) | `4016985845` | 2026-06-10 07:28:47 | 商家名片 > 开发指引 |
| 439 | [提交商家名片配置申请](pages/4016468440.md) | `4016468440` | 2025-11-13 06:54:09 | 商家名片 > API列表 > 商家名片配置 |
| 440 | [发布商家名片配置](pages/4016475176.md) | `4016475176` | 2025-11-13 06:54:27 | 商家名片 > API列表 > 商家名片配置 |
| 441 | [撤销商家名片配置申请](pages/4016475172.md) | `4016475172` | 2025-11-13 06:54:39 | 商家名片 > API列表 > 商家名片配置 |
| 442 | [查询商家名片配置申请状态](pages/4016475174.md) | `4016475174` | 2025-11-13 06:54:51 | 商家名片 > API列表 > 商家名片配置 |
| 443 | [获取商家名片预览二维码](pages/4016641998.md) | `4016641998` | 2025-11-20 07:20:12 | 商家名片 > API列表 > 商家名片配置 |
| 444 | [添加交易连接名片规则申请](pages/4016333302.md) | `4016333302` | 2025-10-30 09:56:20 | 商家名片 > API列表 > 交易连接名片 |
| 445 | [解除已生效交易连接名片场景](pages/4016366804.md) | `4016366804` | 2025-10-30 09:56:20 | 商家名片 > API列表 > 交易连接名片 |
| 446 | [撤销交易连接名片配置申请](pages/4016366797.md) | `4016366797` | 2025-10-30 09:56:20 | 商家名片 > API列表 > 交易连接名片 |
| 447 | [查询已生效交易连接名片规则](pages/4016366785.md) | `4016366785` | 2025-10-30 09:56:20 | 商家名片 > API列表 > 交易连接名片 |
| 448 | [根据业务申请编号查询添加申请状态](pages/4016366816.md) | `4016366816` | 2025-10-30 09:56:20 | 商家名片 > API列表 > 交易连接名片 |
| 449 | [商家名片&交易连接名片配置指引](pages/4016433970.md) | `4016433970` | 2026-04-02 12:57:33 | 商家名片 > 附录 |
| 450 | [产品介绍](pages/4015274636.md) | `4015274636` | 2026-11-05 07:18:49 | 商家名片会员 |
| 451 | [开发指引](pages/4015274639.md) | `4015274639` | 2026-10-12 03:08:03 | 商家名片会员 |
| 452 | [常见问题](pages/4017418554.md) | `4017418554` | 2026-01-30 07:18:54 | 商家名片会员 |
| 453 | [图片上传](pages/4015900513.md) | `4015900513` | 2025-11-14 07:32:05 | 商家名片会员 > API列表 |
| 454 | [创建会员卡模板](pages/4015336970.md) | `4015336970` | 2026-11-11 06:32:15 | 商家名片会员 > API列表 > 会员卡模板管理 |
| 455 | [查询会员卡模板列表](pages/4015336976.md) | `4015336976` | 2026-11-11 06:30:44 | 商家名片会员 > API列表 > 会员卡模板管理 |
| 456 | [查询会员卡模板信息](pages/4015336974.md) | `4015336974` | 2026-11-11 06:34:35 | 商家名片会员 > API列表 > 会员卡模板管理 |
| 457 | [修改会员卡模板信息](pages/4015336977.md) | `4015336977` | 2026-11-11 06:35:06 | 商家名片会员 > API列表 > 会员卡模板管理 |
| 458 | [作废会员卡模板](pages/4015336972.md) | `4015336972` | 2025-08-01 02:53:26 | 商家名片会员 > API列表 > 会员卡模板管理 |
| 459 | [查询用户会员卡信息](pages/4015336980.md) | `4015336980` | 2025-07-25 03:00:22 | 商家名片会员 > API列表 > 用户会员卡管理 |
| 460 | [查询用户在品牌下所有会员卡](pages/4015336984.md) | `4015336984` | 2025-07-25 03:00:22 | 商家名片会员 > API列表 > 用户会员卡管理 |
| 461 | [修改用户会员卡信息](pages/4015336985.md) | `4015336985` | 2025-07-25 03:00:22 | 商家名片会员 > API列表 > 用户会员卡管理 |
| 462 | [作废用户会员卡](pages/4015336983.md) | `4015336983` | 2025-07-25 03:00:22 | 商家名片会员 > API列表 > 用户会员卡管理 |
| 463 | [品牌会员入会组件预授权](pages/4015336986.md) | `4015336986` | 2025-11-19 04:10:23 | 商家名片会员 > API列表 > 用户开通会员卡 |
| 464 | [小程序拉起品牌会员入会组件](pages/4015273633.md) | `4015273633` | 2025-06-24 06:51:53 | 商家名片会员 > API列表 > 用户开通会员卡 |
| 465 | [H5拉起品牌会员入会组件](pages/4015331476.md) | `4015331476` | 2025-12-23 08:54:29 | 商家名片会员 > API列表 > 用户开通会员卡 |
| 466 | [根据OPENID导入用户会员卡](pages/4015336981.md) | `4015336981` | 2025-06-22 08:21:27 | 商家名片会员 > API列表 > 商家同步会员身份 |
| 467 | [同步会员开通结果](pages/4015336979.md) | `4015336979` | 2025-06-22 08:22:08 | 商家名片会员 > API列表 > 商家同步会员身份 |
| 468 | [会员卡事件通知](pages/4015283692.md) | `4015283692` | 2026-11-04 07:44:04 | 商家名片会员 > API列表 > 事件通知 |
| 469 | [下单同步用户实时动态](pages/4015534755.md) | `4015534755` | 2026-10-20 11:53:26 | 商家名片会员 > API列表 > 用户动态 |
| 470 | [产品介绍](pages/4015782374.md) | `4015782374` | 2026-03-11 10:24:02 | 摇一摇有优惠 |
| 471 | [开发接入准备](pages/4016060552.md) | `4016060552` | 2026-10-20 08:46:40 | 摇一摇有优惠 |
| 472 | [开发指引](pages/4016110225.md) | `4016110225` | 2025-11-18 03:40:57 | 摇一摇有优惠 |
| 473 | [常见问题](pages/4017418618.md) | `4017418618` | 2026-01-30 07:18:49 | 摇一摇有优惠 |
| 474 | [创建投放计划](pages/4016184554.md) | `4016184554` | 2025-12-31 07:07:29 | 摇一摇有优惠 > API列表 > 投放计划 |
| 475 | [分页查询投放计划列表](pages/4016184563.md) | `4016184563` | 2025-09-27 11:06:05 | 摇一摇有优惠 > API列表 > 投放计划 |
| 476 | [更新投放计划](pages/4016184594.md) | `4016184594` | 2025-09-27 11:06:26 | 摇一摇有优惠 > API列表 > 投放计划 |
| 477 | [终止投放计划](pages/4016184572.md) | `4016184572` | 2025-09-27 11:06:52 | 摇一摇有优惠 > API列表 > 投放计划 |
| 478 | [设置投放计划回调地址](pages/4016184598.md) | `4016184598` | 2025-09-27 11:07:12 | 摇一摇有优惠 > API列表 > 投放计划 |
| 479 | [投放计划状态变更通知](pages/4016168699.md) | `4016168699` | 2026-03-23 07:44:52 | 摇一摇有优惠 > API列表 > 投放计划 |
| 480 | [投放计划功能介绍](pages/4016402231.md) | `4016402231` | 2026-06-10 07:28:14 | 摇一摇有优惠 > 附录 |
| 481 | [投放计划配置指引](pages/4016111064.md) | `4016111064` | 2026-11-10 07:21:18 | 摇一摇有优惠 > 附录 |
| 482 | [品牌信息用户端展示规则](pages/4016110939.md) | `4016110939` | 2025-11-07 03:08:03 | 摇一摇有优惠 > 附录 |
| 483 | [权限申请](pages/4015788437.md) | `4015788437` | 2026-04-08 02:20:15 | 摇一摇有优惠 > 附录 |
| 484 | [运营规则](pages/4017294537.md) | `4017294537` | 2026-01-20 09:27:40 | 摇一摇有优惠 > 附录 |
| 485 | [产品介绍](pages/4015989376.md) | `4015989376` | 2026-05-13 06:51:04 | 商品券（单券） |
| 486 | [开发指引](pages/4015788446.md) | `4015788446` | 2026-07-08 12:14:11 | 商品券（单券） |
| 487 | [常见问题](pages/4016950421.md) | `4016950421` | 2025-12-23 02:29:29 | 商品券（单券） |
| 488 | [图片上传](pages/4015781275.md) | `4015781275` | 2025-11-07 03:39:13 | 商品券（单券） > API列表 |
| 489 | [创建商品券](pages/4015781289.md) | `4015781289` | 2025-12-31 07:51:19 | 商品券（单券） > API列表 > 商品券管理 |
| 490 | [修改商品券](pages/4015781296.md) | `4015781296` | 2025-08-20 03:37:14 | 商品券（单券） > API列表 > 商品券管理 |
| 491 | [查询商品券](pages/4015781292.md) | `4015781292` | 2025-08-20 03:37:35 | 商品券（单券） > API列表 > 商品券管理 |
| 492 | [失效商品券](pages/4015781290.md) | `4015781290` | 2025-08-20 03:38:31 | 商品券（单券） > API列表 > 商品券管理 |
| 493 | [添加商品券批次](pages/4015781304.md) | `4015781304` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 494 | [查询商品券批次列表](pages/4015781553.md) | `4015781553` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 495 | [查询商品券指定批次](pages/4015781542.md) | `4015781542` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 496 | [修改商品券批次](pages/4015781556.md) | `4015781556` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 497 | [修改商品券批次发放预算](pages/4015781561.md) | `4015781561` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 498 | [失效商品券批次](pages/4015781532.md) | `4015781532` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 499 | [批次关联门店](pages/4015781302.md) | `4015781302` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 500 | [查询批次关联门店列表](pages/4015781546.md) | `4015781546` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 501 | [批次取消关联门店](pages/4015781537.md) | `4015781537` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 502 | [预上传券Code](pages/4015781572.md) | `4015781572` | 2025-10-21 09:04:51 | 商品券（单券） > API列表 > 商品券批次管理 |
| 503 | [向用户发放商品券](pages/4015781605.md) | `4015781605` | 2025-11-07 03:28:05 | 商品券（单券） > API列表 > 商品券发放 |
| 504 | [确认发放用户商品券](pages/4015781575.md) | `4015781575` | 2025-11-07 03:28:05 | 商品券（单券） > API列表 > 商品券发放 |
| 505 | [向用户预发放商品券](pages/4016434365.md) | `4016434365` | 2025-11-07 03:23:20 | 商品券（单券） > API列表 > 商品券发放 > 小程序发券组件 |
| 506 | [调起小程序发券组件](pages/4016434346.md) | `4016434346` | 2025-12-23 09:05:06 | 商品券（单券） > API列表 > 商品券发放 > 小程序发券组件 |
| 507 | [核销用户商品券](pages/4015781608.md) | `4015781608` | 2025-10-21 09:05:48 | 商品券（单券） > API列表 > 商品券核销 |
| 508 | [调起小程序核销组件](pages/4016110739.md) | `4016110739` | 2025-11-07 08:58:44 | 商品券（单券） > API列表 > 商品券核销 |
| 509 | [查询用户商品券详情](pages/4015781582.md) | `4015781582` | 2025-10-21 09:05:48 | 商品券（单券） > API列表 > 商品券查询 |
| 510 | [指定券状态查询用户商品券列表](pages/4015781590.md) | `4015781590` | 2025-11-07 03:37:12 | 商品券（单券） > API列表 > 商品券查询 |
| 511 | [失效用户商品券](pages/4015781578.md) | `4015781578` | 2025-10-21 09:05:48 | 商品券（单券） > API列表 > 商品券失效与退券 |
| 512 | [退券](pages/4015781599.md) | `4015781599` | 2025-11-07 03:37:52 | 商品券（单券） > API列表 > 商品券失效与退券 |
| 513 | [获取商品券事件通知地址](pages/4015781284.md) | `4015781284` | 2025-08-28 02:02:45 | 商品券（单券） > API列表 > 商品券回调通知 |
| 514 | [设置商品券事件通知地址](pages/4015781286.md) | `4015781286` | 2025-08-28 02:02:45 | 商品券（单券） > API列表 > 商品券回调通知 |
| 515 | [商品券回调通知](pages/4015780862.md) | `4015780862` | 2026-10-30 02:24:56 | 商品券（单券） > API列表 > 商品券回调通知 |
| 516 | [提交图片生成任务](pages/4017327735.md) | `4017327735` | 2026-01-26 03:27:31 | 商品券（单券） > API列表 > 生成商品券头图 |
| 517 | [查询图片生成任务执行结果](pages/4017327739.md) | `4017327739` | 2026-01-26 03:27:31 | 商品券（单券） > API列表 > 生成商品券头图 |
| 518 | [图片生成回调通知](pages/4017327744.md) | `4017327744` | 2026-01-26 03:27:31 | 商品券（单券） > API列表 > 生成商品券头图 |
| 519 | [小程序发券组件开发指引](pages/4016434329.md) | `4016434329` | 2026-06-10 07:28:10 | 商品券（单券） > 附录 |
| 520 | [小程序核销组件开发指引](pages/4016110741.md) | `4016110741` | 2026-04-02 14:44:14 | 商品券（单券） > 附录 |
| 521 | [品牌、服务商、appid关联关系](pages/4018984107.md) | `4018984107` | 2026-03-26 06:44:08 | 商品券（单券） > 附录 |
| 522 | [商品券可核销时间规则说明（coupon_available_period）](pages/4016675999.md) | `4016675999` | 2025-11-25 03:05:19 | 商品券（单券） > 附录 |
| 523 | [商品券客户端消息推送页面](pages/4019005729.md) | `4019005729` | 2026-03-27 06:57:51 | 商品券（单券） > 附录 |
| 524 | [商品券结构及修改说明](pages/4018984452.md) | `4018984452` | 2026-03-27 02:47:11 | 商品券（单券） > 附录 |
| 525 | [品类券头图设计规范](pages/4043213639.md) | `4043213639` | 2026-09-21 09:21:27 | 商品券（单券） > 附录 |
| 526 | [券类型选型](pages/4043817598.md) | `4043817598` | 2026-09-23 02:56:41 | 商品券（单券） > 附录 |
| 527 | [【单券-全场-折扣券】API请求示例](pages/4016756270.md) | `4016756270` | 2025-12-02 13:12:50 | 商品券（单券） > 附录 > API请求示例-创建商品券 |
| 528 | [【单券-全场-满减券】API请求示例](pages/4016756271.md) | `4016756271` | 2025-12-02 13:13:02 | 商品券（单券） > 附录 > API请求示例-创建商品券 |
| 529 | [【单券-单品-折扣券】API请求示例](pages/4016756272.md) | `4016756272` | 2025-12-25 11:53:38 | 商品券（单券） > 附录 > API请求示例-创建商品券 |
| 530 | [【单券-单品-满减券】API请求示例](pages/4016756273.md) | `4016756273` | 2025-12-25 11:54:13 | 商品券（单券） > 附录 > API请求示例-创建商品券 |
| 531 | [【单券-单品-兑换券】API请求示例](pages/4016756274.md) | `4016756274` | 2025-12-25 11:55:51 | 商品券（单券） > 附录 > API请求示例-创建商品券 |
| 532 | [产品介绍](pages/4016438787.md) | `4016438787` | 2026-05-13 06:51:15 | 商品券（多次优惠） |
| 533 | [开发指引](pages/4016438816.md) | `4016438816` | 2026-06-10 07:28:08 | 商品券（多次优惠） |
| 534 | [常见问题](pages/4016950439.md) | `4016950439` | 2025-12-23 02:29:27 | 商品券（多次优惠） |
| 535 | [图片上传](pages/4016435731.md) | `4016435731` | 2025-11-07 06:33:45 | 商品券（多次优惠） > API列表 |
| 536 | [创建商品券](pages/4016434630.md) | `4016434630` | 2025-12-31 07:51:33 | 商品券（多次优惠） > API列表 > 商品券管理 |
| 537 | [修改商品券](pages/4016434633.md) | `4016434633` | 2025-11-07 03:42:29 | 商品券（多次优惠） > API列表 > 商品券管理 |
| 538 | [查询商品券](pages/4016434632.md) | `4016434632` | 2025-11-07 03:42:29 | 商品券（多次优惠） > API列表 > 商品券管理 |
| 539 | [失效商品券](pages/4016434631.md) | `4016434631` | 2025-11-07 03:42:29 | 商品券（多次优惠） > API列表 > 商品券管理 |
| 540 | [添加商品券批次组](pages/4016280622.md) | `4016280622` | 2025-11-20 03:00:43 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 541 | [查询商品券批次列表](pages/4016434641.md) | `4016434641` | 2025-11-07 03:50:02 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 542 | [查询商品券指定批次](pages/4016434649.md) | `4016434649` | 2025-11-07 03:50:02 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 543 | [修改商品券批次组](pages/4016280633.md) | `4016280633` | 2025-11-20 03:00:41 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 544 | [修改商品券批次组发放预算](pages/4016280642.md) | `4016280642` | 2025-11-20 03:00:40 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 545 | [批次组批量关联门店](pages/4016280620.md) | `4016280620` | 2025-11-20 03:00:37 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 546 | [批次组批量取消关联门店](pages/4016280629.md) | `4016280629` | 2025-11-20 03:00:33 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 547 | [查询批次关联门店列表](pages/4016434665.md) | `4016434665` | 2025-11-07 03:50:02 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 548 | [预上传券Code](pages/4016434668.md) | `4016434668` | 2025-11-07 03:50:02 | 商品券（多次优惠） > API列表 > 商品券批次管理 |
| 549 | [向用户发放商品券批次组](pages/4016280664.md) | `4016280664` | 2025-11-20 03:00:32 | 商品券（多次优惠） > API列表 > 商品券发放 |
| 550 | [确认发放用户商品券](pages/4016435562.md) | `4016435562` | 2025-11-07 06:25:22 | 商品券（多次优惠） > API列表 > 商品券发放 |
| 551 | [向用户预发放商品券批次组](pages/4016280670.md) | `4016280670` | 2025-12-16 08:25:19 | 商品券（多次优惠） > API列表 > 商品券发放 > 小程序发券组件 |
| 552 | [调起小程序发券组件](pages/4016435568.md) | `4016435568` | 2025-12-23 08:54:20 | 商品券（多次优惠） > API列表 > 商品券发放 > 小程序发券组件 |
| 553 | [核销用户商品券](pages/4016435636.md) | `4016435636` | 2025-11-07 06:28:01 | 商品券（多次优惠） > API列表 > 商品券核销 |
| 554 | [调起小程序核销组件](pages/4016435640.md) | `4016435640` | 2025-11-07 08:58:05 | 商品券（多次优惠） > API列表 > 商品券核销 |
| 555 | [查询用户商品券详情](pages/4016435702.md) | `4016435702` | 2025-11-07 06:31:39 | 商品券（多次优惠） > API列表 > 商品券查询 |
| 556 | [指定券状态查询用户商品券列表](pages/4016435703.md) | `4016435703` | 2025-11-07 06:31:39 | 商品券（多次优惠） > API列表 > 商品券查询 |
| 557 | [失效用户商品券组](pages/4016280658.md) | `4016280658` | 2025-11-20 03:00:30 | 商品券（多次优惠） > API列表 > 商品券失效与退券 |
| 558 | [退券](pages/4016435674.md) | `4016435674` | 2025-11-07 06:30:06 | 商品券（多次优惠） > API列表 > 商品券失效与退券 |
| 559 | [获取商品券事件通知地址](pages/4016435718.md) | `4016435718` | 2025-11-07 06:32:46 | 商品券（多次优惠） > API列表 > 商品券回调通知 |
| 560 | [设置商品券事件通知地址](pages/4016435719.md) | `4016435719` | 2025-11-07 06:32:46 | 商品券（多次优惠） > API列表 > 商品券回调通知 |
| 561 | [商品券回调通知](pages/4016435717.md) | `4016435717` | 2026-10-30 02:24:06 | 商品券（多次优惠） > API列表 > 商品券回调通知 |
| 562 | [提交图片生成任务](pages/4017327752.md) | `4017327752` | 2026-01-26 03:27:42 | 商品券（多次优惠） > API列表 > 生成商品券头图 |
| 563 | [查询图片生成任务执行结果](pages/4017327753.md) | `4017327753` | 2026-01-26 03:27:42 | 商品券（多次优惠） > API列表 > 生成商品券头图 |
| 564 | [图片生成回调通知](pages/4017327759.md) | `4017327759` | 2026-01-26 03:27:42 | 商品券（多次优惠） > API列表 > 生成商品券头图 |
| 565 | [小程序发券组件开发指引](pages/4016435566.md) | `4016435566` | 2026-06-10 07:28:07 | 商品券（多次优惠） > 附录 |
| 566 | [小程序核销组件开发指引](pages/4016435642.md) | `4016435642` | 2026-04-02 14:46:11 | 商品券（多次优惠） > 附录 |
| 567 | [品牌、服务商、appid关联关系](pages/4018984192.md) | `4018984192` | 2026-03-26 06:44:07 | 商品券（多次优惠） > 附录 |
| 568 | [商品券可核销时间规则说明（coupon_available_period）](pages/4016676012.md) | `4016676012` | 2025-11-25 11:47:16 | 商品券（多次优惠） > 附录 |
| 569 | [商品券客户端消息推送页面](pages/4019005741.md) | `4019005741` | 2026-03-27 06:57:49 | 商品券（多次优惠） > 附录 |
| 570 | [商品券结构及修改说明](pages/4018984437.md) | `4018984437` | 2026-03-27 02:47:05 | 商品券（多次优惠） > 附录 |
| 571 | [品类券头图设计规范](pages/4043213651.md) | `4043213651` | 2026-09-21 09:21:25 | 商品券（多次优惠） > 附录 |
| 572 | [【多次优惠-全场-折扣券】API请求示例](pages/4016756283.md) | `4016756283` | 2025-12-04 07:57:31 | 商品券（多次优惠） > 附录 > API请求示例-创建商品券 |
| 573 | [【多次优惠-全场-满减券】API请求示例](pages/4016756284.md) | `4016756284` | 2025-12-04 07:59:00 | 商品券（多次优惠） > 附录 > API请求示例-创建商品券 |
| 574 | [【多次优惠-单品-折扣券】API请求示例](pages/4016756285.md) | `4016756285` | 2025-12-04 08:00:48 | 商品券（多次优惠） > 附录 > API请求示例-创建商品券 |
| 575 | [【多次优惠-单品-满减券】API请求示例](pages/4016756286.md) | `4016756286` | 2025-12-04 08:01:18 | 商品券（多次优惠） > 附录 > API请求示例-创建商品券 |
| 576 | [【多次优惠-单品-兑换券】API请求示例](pages/4016756287.md) | `4016756287` | 2025-12-04 08:01:50 | 商品券（多次优惠） > 附录 > API请求示例-创建商品券 |
| 577 | [产品介绍](pages/4016628074.md) | `4016628074` | 2025-11-19 02:54:10 | 品牌门店 |
| 578 | [开发指引](pages/4016628135.md) | `4016628135` | 2026-11-11 03:58:05 | 品牌门店 |
| 579 | [常见问题](pages/4016705104.md) | `4016705104` | 2025-11-27 04:06:48 | 品牌门店 |
| 580 | [创建品牌门店](pages/4015783183.md) | `4015783183` | 2025-12-02 11:35:44 | 品牌门店 > API列表 |
| 581 | [查询品牌门店](pages/4015783153.md) | `4015783153` | 2025-12-02 11:35:44 | 品牌门店 > API列表 |
| 582 | [查询品牌门店列表](pages/4016756674.md) | `4016756674` | 2025-12-16 02:56:33 | 品牌门店 > API列表 |
| 583 | [更新品牌门店](pages/4015783158.md) | `4015783158` | 2025-12-02 11:35:44 | 品牌门店 > API列表 |
| 584 | [删除品牌门店](pages/4015783113.md) | `4015783113` | 2025-12-02 11:35:44 | 品牌门店 > API列表 |
| 585 | [暂停门店营业](pages/4016756671.md) | `4016756671` | 2025-12-16 02:56:33 | 品牌门店 > API列表 |
| 586 | [恢复门店营业](pages/4016756672.md) | `4016756672` | 2025-12-16 02:56:33 | 品牌门店 > API列表 |
| 587 | [品牌经营平台管理品牌门店](pages/4016689827.md) | `4016689827` | 2025-11-25 10:04:14 | 品牌门店 > 附录 |
| 588 | [获得品牌已授权且在生效中的产品权限信息](pages/4017410365.md) | `4017410365` | 2026-01-29 09:12:34 | 品牌服务商授权 > API列表 |
| 589 | [产品介绍](pages/4012072620.md) | `4012072620` | 2024-07-23 08:51:32 | 连锁品牌分账 |
| 590 | [开发接入准备](pages/4012072625.md) | `4012072625` | 2026-05-19 09:30:42 | 连锁品牌分账 |
| 591 | [开发指引](pages/4012072637.md) | `4012072637` | 2026-06-09 09:46:07 | 连锁品牌分账 |
| 592 | [业务示例代码](pages/4015871675.md) | `4015871675` | 2026-06-09 09:46:50 | 连锁品牌分账 |
| 593 | [常见问题](pages/4015981574.md) | `4015981574` | 2026-02-06 03:12:47 | 连锁品牌分账 |
| 594 | [请求分账](pages/4012692975.md) | `4012692975` | 2025-09-29 03:46:37 | 连锁品牌分账 > API列表 |
| 595 | [查询分账结果](pages/4012467002.md) | `4012467002` | 2025-09-29 03:45:52 | 连锁品牌分账 > API列表 |
| 596 | [请求分账回退](pages/4012467097.md) | `4012467097` | 2025-09-29 03:43:29 | 连锁品牌分账 > API列表 |
| 597 | [查询分账回退结果](pages/4012467011.md) | `4012467011` | 2025-09-29 03:43:57 | 连锁品牌分账 > API列表 |
| 598 | [解冻剩余资金](pages/4012467016.md) | `4012467016` | 2025-09-29 03:43:07 | 连锁品牌分账 > API列表 |
| 599 | [查询订单剩余待分金额](pages/4012467021.md) | `4012467021` | 2025-09-29 03:42:34 | 连锁品牌分账 > API列表 |
| 600 | [查询最大分账比例](pages/4012467022.md) | `4012467022` | 2025-09-29 03:42:11 | 连锁品牌分账 > API列表 |
| 601 | [添加分账接收方](pages/4012467100.md) | `4012467100` | 2025-09-29 03:41:51 | 连锁品牌分账 > API列表 |
| 602 | [删除分账接收方](pages/4012467103.md) | `4012467103` | 2025-09-29 02:38:34 | 连锁品牌分账 > API列表 |
| 603 | [分账动账通知](pages/4012075400.md) | `4012075400` | 2025-02-19 03:56:03 | 连锁品牌分账 > API列表 |
| 604 | [申请分账账单](pages/4012715572.md) | `4012715572` | 2025-09-29 02:37:48 | 连锁品牌分账 > API列表 |
| 605 | [下载账单](pages/4012076073.md) | `4012076073` | 2024-10-30 06:42:53 | 连锁品牌分账 > API列表 |
| 606 | [分账失败处理指引](pages/4015504918.md) | `4015504918` | 2025-07-04 03:08:09 | 连锁品牌分账 > 附录 |
| 607 | [清关报关（V2）](pages/4012851220.md) | `4012851220` | 2025-04-25 07:53:42 | 清关报关（V2） |
| 608 | [产品介绍](pages/4012072827.md) | `4012072827` | 2025-08-25 10:00:14 | 消费者投诉2.0 |
| 609 | [开发接入准备](pages/4012072844.md) | `4012072844` | 2026-05-19 09:30:57 | 消费者投诉2.0 |
| 610 | [开发指引](pages/4012072858.md) | `4012072858` | 2026-10-20 03:51:53 | 消费者投诉2.0 |
| 611 | [业务示例代码](pages/4015933338.md) | `4015933338` | 2026-06-09 09:46:01 | 消费者投诉2.0 |
| 612 | [接入易错点](pages/4054257738.md) | `4054257738` | 2026-10-30 14:13:17 | 消费者投诉2.0 |
| 613 | [常见问题](pages/4016111688.md) | `4016111688` | 2026-11-05 09:31:00 | 消费者投诉2.0 |
| 614 | [查询投诉单列表](pages/4012691285.md) | `4012691285` | 2025-09-02 02:28:31 | 消费者投诉2.0 > API列表 > 主动查询投诉信息 |
| 615 | [查询投诉单详情](pages/4012691648.md) | `4012691648` | 2025-08-28 02:43:42 | 消费者投诉2.0 > API列表 > 主动查询投诉信息 |
| 616 | [查询投诉单协商历史](pages/4012691802.md) | `4012691802` | 2025-08-28 02:43:30 | 消费者投诉2.0 > API列表 > 主动查询投诉信息 |
| 617 | [投诉通知回调](pages/4012076174.md) | `4012076174` | 2025-02-19 03:56:03 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 618 | [创建投诉通知回调地址](pages/4012458106.md) | `4012458106` | 2025-08-28 02:43:28 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 619 | [查询投诉通知回调地址](pages/4012459065.md) | `4012459065` | 2025-08-28 02:43:23 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 620 | [更新投诉通知回调地址](pages/4012459287.md) | `4012459287` | 2025-08-28 02:43:25 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 621 | [删除投诉通知回调地址](pages/4012460474.md) | `4012460474` | 2025-08-28 02:43:21 | 消费者投诉2.0 > API列表 > 实时获取投诉信息 |
| 622 | [回复用户](pages/4012467213.md) | `4012467213` | 2025-09-01 02:27:29 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 623 | [反馈处理完成](pages/4012467217.md) | `4012467217` | 2025-09-01 02:25:00 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 624 | [更新退款审批结果](pages/4012467218.md) | `4012467218` | 2025-09-01 02:24:26 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 625 | [回复需要即时服务的投诉单](pages/4017151726.md) | `4017151726` | 2026-01-22 08:02:14 | 消费者投诉2.0 > API列表 > 商户处理用户投诉 |
| 626 | [图片上传接口](pages/4012467222.md) | `4012467222` | 2025-09-01 02:10:00 | 消费者投诉2.0 > API列表 > 商户反馈图片 |
| 627 | [图片请求接口](pages/4012467223.md) | `4012467223` | 2025-09-02 02:43:19 | 消费者投诉2.0 > API列表 > 商户反馈图片 |
| 628 | [产品介绍](pages/4015792553.md) | `4015792553` | 2025-11-28 08:19:11 | 微信电子发票 |
| 629 | [开发接入准备](pages/4015792554.md) | `4015792554` | 2026-10-20 10:23:12 | 微信电子发票 |
| 630 | [开发指引](pages/4015792556.md) | `4015792556` | 2026-07-27 08:21:58 | 微信电子发票 |
| 631 | [业务示例代码](pages/4016078358.md) | `4016078358` | 2026-06-10 07:28:02 | 微信电子发票 |
| 632 | [常见问题](pages/4016960715.md) | `4016960715` | 2026-08-05 06:11:58 | 微信电子发票 |
| 633 | [获取开通服务商电子发票能力邀请链接](pages/4015941495.md) | `4015941495` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 634 | [获取邀请开通的商户信息](pages/4015941524.md) | `4015941524` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 635 | [检查子商户开票功能状态](pages/4015792561.md) | `4015792561` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 636 | [创建电子发票卡券模板](pages/4015792562.md) | `4015792562` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 637 | [配置开发选项](pages/4015792563.md) | `4015792563` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 638 | [获取用户抬头填写链接](pages/4015770776.md) | `4015770776` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 639 | [获取用户填写抬头信息](pages/4015784260.md) | `4015784260` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 640 | [开具通用行业电子发票](pages/4015792574.md) | `4015792574` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 641 | [开具不动产租赁行业电子发票](pages/4015941740.md) | `4015941740` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 642 | [开具成品油行业电子发票](pages/4016760559.md) | `4016760559` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 643 | [开具旅客运输行业电子发票](pages/4025863376.md) | `4025863376` | 2026-07-17 03:57:13 | 微信电子发票 > API列表 |
| 644 | [冲红电子发票](pages/4015792575.md) | `4015792575` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 645 | [查询电子发票](pages/4015792567.md) | `4015792567` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 646 | [获取发票下载信息](pages/4015792576.md) | `4015792576` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 647 | [下载发票文件](pages/4015792569.md) | `4015792569` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 648 | [上传电子发票文件](pages/4015792580.md) | `4015792580` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 649 | [将电子发票插入微信用户卡包](pages/4015792579.md) | `4015792579` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 650 | [用户发票抬头填写完成通知](pages/4015792559.md) | `4015792559` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 651 | [发票开具成功通知](pages/4015792570.md) | `4015792570` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 652 | [发票插入用户卡包成功通知](pages/4015792578.md) | `4015792578` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 653 | [发票冲红成功通知](pages/4015792571.md) | `4015792571` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 654 | [发票卡券作废通知](pages/4015792560.md) | `4015792560` | 2025-12-03 02:09:53 | 微信电子发票 > API列表 |
| 655 | [成品油单位转换公式](pages/4016730844.md) | `4016730844` | 2026-07-27 06:19:53 | 微信电子发票 > 附录 |
| 656 | [产品介绍](pages/4012062365.md) | `4012062365` | 2024-10-16 07:11:49 | 特约商户进件 |
| 657 | [开发接入准备](pages/4012062375.md) | `4012062375` | 2026-10-20 10:21:17 | 特约商户进件 |
| 658 | [开发指引](pages/4012062379.md) | `4012062379` | 2026-06-09 09:45:48 | 特约商户进件 |
| 659 | [常见问题](pages/4016058480.md) | `4016058480` | 2026-08-05 06:17:02 | 特约商户进件 |
| 660 | [提交申请单](pages/4012719997.md) | `4012719997` | 2025-03-26 06:58:27 | 特约商户进件 > API列表 |
| 661 | [申请单号查询申请状态](pages/4012697052.md) | `4012697052` | 2025-03-24 04:07:15 | 特约商户进件 > API列表 |
| 662 | [业务申请编号查询申请状态](pages/4012697168.md) | `4012697168` | 2025-03-24 04:07:17 | 特约商户进件 > API列表 |
| 663 | [修改结算账户](pages/4012761102.md) | `4012761102` | 2025-01-22 01:35:52 | 特约商户进件 > API列表 |
| 664 | [查询结算账户](pages/4012761113.md) | `4012761113` | 2025-01-21 03:41:29 | 特约商户进件 > API列表 |
| 665 | [查询结算账户修改申请状态](pages/4012761120.md) | `4012761120` | 2025-01-21 03:41:31 | 特约商户进件 > API列表 |
| 666 | [文件上传](pages/4012760490.md) | `4012760490` | 2026-05-09 07:01:44 | 特约商户进件 > API列表 |
| 667 | [视频上传](pages/4012761084.md) | `4012761084` | 2024-11-18 09:25:56 | 特约商户进件 > API列表 |
| 668 | [产品介绍](pages/4012064820.md) | `4012064820` | 2024-10-24 08:22:24 | 商户开户意愿确认 |
| 669 | [开发接入准备](pages/4012064824.md) | `4012064824` | 2026-10-22 11:09:03 | 商户开户意愿确认 |
| 670 | [开发指引](pages/4012064832.md) | `4012064832` | 2026-10-20 07:56:31 | 商户开户意愿确认 |
| 671 | [常见问题](pages/4016644196.md) | `4016644196` | 2026-01-16 03:48:52 | 商户开户意愿确认 |
| 672 | [提交申请单](pages/4012722388.md) | `4012722388` | 2025-01-09 03:10:33 | 商户开户意愿确认 > API列表 |
| 673 | [撤销申请单](pages/4012697627.md) | `4012697627` | 2024-12-04 02:03:31 | 商户开户意愿确认 > API列表 |
| 674 | [查询申请单审核结果](pages/4012697715.md) | `4012697715` | 2024-11-04 07:59:30 | 商户开户意愿确认 > API列表 |
| 675 | [获取商户开户意愿确认状态](pages/4012467549.md) | `4012467549` | 2024-10-24 09:20:46 | 商户开户意愿确认 > API列表 |
| 676 | [图片上传](pages/4012760509.md) | `4012760509` | 2024-11-18 09:25:43 | 商户开户意愿确认 > API列表 |
| 677 | [产品介绍](pages/4012064844.md) | `4012064844` | 2026-03-10 07:23:55 | 商户平台处置通知 |
| 678 | [开发接入准备](pages/4012064851.md) | `4012064851` | 2026-05-19 09:33:15 | 商户平台处置通知 |
| 679 | [开发指引](pages/4012064853.md) | `4012064853` | 2026-10-20 08:03:31 | 商户平台处置通知 |
| 680 | [业务示例代码](pages/4015949382.md) | `4015949382` | 2025-09-03 03:01:42 | 商户平台处置通知 |
| 681 | [查询商户违规通知回调地址](pages/4012471327.md) | `4012471327` | 2025-08-28 09:27:26 | 商户平台处置通知 > API列表 > 商户违规通知回调 |
| 682 | [修改商户违规通知回调地址](pages/4012471330.md) | `4012471330` | 2025-08-28 09:27:19 | 商户平台处置通知 > API列表 > 商户违规通知回调 |
| 683 | [创建商户违规通知回调地址](pages/4012471333.md) | `4012471333` | 2025-08-28 09:27:12 | 商户平台处置通知 > API列表 > 商户违规通知回调 |
| 684 | [删除商户违规通知回调地址](pages/4012471334.md) | `4012471334` | 2025-08-28 09:27:05 | 商户平台处置通知 > API列表 > 商户违规通知回调 |
| 685 | [商户平台处置记录回调通知](pages/4012079216.md) | `4012079216` | 2025-02-19 03:56:03 | 商户平台处置通知 > API列表 > 商户违规通知回调 |
| 686 | [产品介绍](pages/4012064898.md) | `4012064898` | 2026-05-25 07:06:33 | 不活跃商户身份核实 |
| 687 | [开发接入准备](pages/4012064902.md) | `4012064902` | 2026-05-19 09:33:57 | 不活跃商户身份核实 |
| 688 | [开发指引](pages/4012064909.md) | `4012064909` | 2026-06-09 09:45:41 | 不活跃商户身份核实 |
| 689 | [常见问题](pages/4012064915.md) | `4012064915` | 2024-07-24 08:05:05 | 不活跃商户身份核实 |
| 690 | [发起不活跃商户身份核实](pages/4012471357.md) | `4012471357` | 2025-08-08 07:33:04 | 不活跃商户身份核实 > API列表 |
| 691 | [查询不活跃商户身份核实结果](pages/4012471359.md) | `4012471359` | 2025-08-08 08:00:48 | 不活跃商户身份核实 > API列表 |
| 692 | [关键概念](pages/4012064904.md) | `4012064904` | 2024-10-25 02:37:34 | 不活跃商户身份核实 > 附录 |
| 693 | [产品介绍](pages/4012165270.md) | `4012165270` | 2026-10-20 08:13:40 | 商户被管控能力及原因查询 |
| 694 | [查询子商户管控情况](pages/4012803072.md) | `4012803072` | 2025-09-26 09:24:32 | 商户被管控能力及原因查询 > API列表 |
| 695 | [产品介绍](pages/4016022264.md) | `4016022264` | 2025-09-17 04:03:07 | 合作伙伴订阅 |
| 696 | [开发指引](pages/4016022266.md) | `4016022266` | 2025-09-16 03:35:57 | 合作伙伴订阅 |
| 697 | [常见问题](pages/4016550707.md) | `4016550707` | 2026-08-05 06:17:27 | 合作伙伴订阅 |
| 698 | [证书密钥概览](pages/4025464285.md) | `4025464285` | 2026-07-21 04:03:55 | 证书密钥概览 |
| 699 | [产品介绍](pages/4057926576.md) | `4057926576` | 2026-11-09 10:05:28 | 商户API证书 |
| 700 | [常见问题](pages/4058384718.md) | `4058384718` | 2026-11-10 03:03:30 | 商户API证书 |
| 701 | [产品介绍](pages/4012925323.md) | `4012925323` | 2026-05-20 03:21:30 | 微信支付公钥 |
| 702 | [接入易错点](pages/4054257740.md) | `4054257740` | 2026-10-30 13:18:21 | 微信支付公钥 |
| 703 | [常见问题](pages/4013038589.md) | `4013038589` | 2025-03-04 07:15:22 | 微信支付公钥 |
| 704 | [商户签名验签／加解密测试](pages/4015139289.md) | `4015139289` | 2026-04-08 03:50:21 | 微信支付公钥 > API列表 |
| 705 | [回调接口](pages/4019605946.md) | `4019605946` | 2026-04-10 08:15:23 | 微信支付公钥 > API列表 |
| 706 | [如何从平台证书切换成微信支付公钥](pages/4012925289.md) | `4012925289` | 2024-12-12 02:59:29 | 微信支付公钥 > 附录 |
| 707 | [如何从微信支付公钥切换成平台证书](pages/4015419376.md) | `4015419376` | 2026-03-17 09:45:27 | 微信支付公钥 > 附录 |
| 708 | [产品介绍](pages/4012073044.md) | `4012073044` | 2026-05-21 07:25:38 | 平台证书 |
| 709 | [接入易错点](pages/4054257739.md) | `4054257739` | 2026-11-05 08:10:05 | 平台证书 |
| 710 | [常见问题](pages/4012073263.md) | `4012073263` | 2024-11-29 09:45:35 | 平台证书 |
| 711 | [下载平台证书](pages/4012715700.md) | `4012715700` | 2024-10-15 08:45:31 | 平台证书 > API列表 |
| 712 | [平台证书更换操作指引](pages/4012073146.md) | `4012073146` | 2024-12-04 06:35:09 | 平台证书 > 附录 |
| 713 | [产品介绍](pages/4057926638.md) | `4057926638` | 2026-11-09 10:05:53 | APIv3密钥 |
| 714 | [产品介绍](pages/4012086891.md) | `4012086891` | 2026-10-20 10:21:01 | 平台收付通-电商交易解决方案 |
| 715 | [开发接入准备](pages/4012086921.md) | `4012086921` | 2026-10-20 10:20:57 | 平台收付通-电商交易解决方案 |
| 716 | [消费者投诉2.0](pages/4016312079.md) | `4016312079` | 2026-07-16 03:40:54 | 平台收付通-电商交易解决方案 |
| 717 | [开发指引](pages/4012087137.md) | `4012087137` | 2026-06-16 07:46:00 | 平台收付通-电商交易解决方案 > 商户进件 |
| 718 | [常见问题](pages/4012525423.md) | `4012525423` | 2026-05-26 08:53:06 | 平台收付通-电商交易解决方案 > 商户进件 |
| 719 | [提交申请单](pages/4012713017.md) | `4012713017` | 2025-02-28 12:07:34 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 720 | [通过业务申请编号查询申请状态](pages/4012691376.md) | `4012691376` | 2024-11-28 06:22:29 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 721 | [通过申请单ID查询申请状态](pages/4012691469.md) | `4012691469` | 2024-11-28 06:22:27 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 722 | [修改结算账户](pages/4012761138.md) | `4012761138` | 2026-01-14 06:27:19 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 723 | [查询结算账户](pages/4012761142.md) | `4012761142` | 2026-01-14 06:27:41 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 724 | [查询结算账户修改申请状态](pages/4012761169.md) | `4012761169` | 2025-01-21 03:41:31 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 725 | [文件上传](pages/4012760432.md) | `4012760432` | 2026-05-09 07:02:14 | 平台收付通-电商交易解决方案 > 商户进件 > API列表 |
| 726 | [产品介绍](pages/4018153750.md) | `4018153750` | 2026-06-11 07:25:17 | 平台收付通-电商交易解决方案 > 商户注销 |
| 727 | [商户注销资格校验](pages/4016420099.md) | `4016420099` | 2025-11-05 09:41:04 | 平台收付通-电商交易解决方案 > 商户注销 > 注销预校验 > API列表 |
| 728 | [提交注销提现申请](pages/4013892756.md) | `4013892756` | 2025-03-13 04:54:44 | 平台收付通-电商交易解决方案 > 商户注销 > 注销提现（新流程） > API列表 |
| 729 | [商户申请单号查询申请单状态](pages/4013892759.md) | `4013892759` | 2025-09-26 02:25:46 | 平台收付通-电商交易解决方案 > 商户注销 > 注销提现（新流程） > API列表 |
| 730 | [微信支付申请单号查询申请单状态](pages/4013892765.md) | `4013892765` | 2025-09-26 02:25:56 | 平台收付通-电商交易解决方案 > 商户注销 > 注销提现（新流程） > API列表 |
| 731 | [常见问题](pages/4015943239.md) | `4015943239` | 2025-11-07 06:48:10 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） |
| 732 | [提交注销申请单](pages/4012476217.md) | `4012476217` | 2025-02-17 10:16:34 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销申请 > 注销申请单 |
| 733 | [查询注销单状态](pages/4012476223.md) | `4012476223` | 2024-11-05 02:04:20 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销申请 > 注销申请单 |
| 734 | [图片上传](pages/4012691710.md) | `4012691710` | 2024-11-05 02:05:52 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销申请 > 图片上传 |
| 735 | [提交已注销商户号可用余额提现申请单](pages/4012488950.md) | `4012488950` | 2025-01-09 03:10:34 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销后提现 > API列表 |
| 736 | [商户提现申请单号查询提现申请单状态](pages/4012476164.md) | `4012476164` | 2024-11-05 02:15:27 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销后提现 > API列表 |
| 737 | [微信支付提现申请单号查询提现申请单状态](pages/4012778400.md) | `4012778400` | 2024-11-05 02:16:19 | 平台收付通-电商交易解决方案 > 商户注销 > 注销申请与提现（旧流程） > 注销后提现 > API列表 |
| 738 | [查询指定主体子商户列表](pages/4033742105.md) | `4033742105` | 2026-08-19 02:04:07 | 平台收付通-电商交易解决方案 > 商户注销 > 商户查询 > API列表 |
| 739 | [开发指引](pages/4012088031.md) | `4012088031` | 2026-06-10 07:28:44 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 |
| 740 | [常见问题](pages/4012525474.md) | `4012525474` | 2026-05-09 08:54:23 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 |
| 741 | [APP下单](pages/4012714669.md) | `4012714669` | 2024-10-24 03:39:28 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > APP支付 |
| 742 | [APP调起支付](pages/4012090168.md) | `4012090168` | 2025-02-20 03:00:52 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > APP支付 |
| 743 | [JSAPI下单](pages/4012714678.md) | `4012714678` | 2024-10-24 03:49:34 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > JSAPI支付 |
| 744 | [JSAPI调起支付](pages/4012090156.md) | `4012090156` | 2025-02-26 07:08:25 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > JSAPI支付 |
| 745 | [Native下单](pages/4012714902.md) | `4012714902` | 2024-10-24 06:18:18 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > Native支付 |
| 746 | [Native调起支付](pages/4012090180.md) | `4012090180` | 2025-03-21 07:41:33 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > Native支付 |
| 747 | [小程序下单](pages/4012714911.md) | `4012714911` | 2024-10-24 03:49:34 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 小程序支付 |
| 748 | [小程序调起支付](pages/4012090181.md) | `4012090181` | 2025-02-26 07:10:30 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 小程序支付 |
| 749 | [H5下单](pages/4012714759.md) | `4012714759` | 2024-10-24 06:27:02 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > H5支付 |
| 750 | [H5调起支付](pages/4012090177.md) | `4012090177` | 2024-12-23 02:14:31 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > H5支付 |
| 751 | [微信支付订单号查询订单](pages/4012760565.md) | `4012760565` | 2025-04-07 01:51:41 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 公共API |
| 752 | [微信支付商户订单号查询订单](pages/4012760568.md) | `4012760568` | 2025-04-07 01:51:51 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 公共API |
| 753 | [关闭订单](pages/4012760574.md) | `4012760574` | 2025-04-07 01:51:49 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 公共API |
| 754 | [支付结果通知](pages/4012090195.md) | `4012090195` | 2025-04-07 01:52:18 | 平台收付通-电商交易解决方案 > 支付下单 > 普通支付 > API列表 > 公共API |
| 755 | [开发指引](pages/4012089542.md) | `4012089542` | 2026-06-10 07:28:43 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 |
| 756 | [常见问题](pages/4012525491.md) | `4012525491` | 2026-05-09 08:54:07 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 |
| 757 | [合单下单-JSAPI](pages/4012760615.md) | `4012760615` | 2024-11-14 08:12:09 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > JSAPI合单支付 |
| 758 | [JSAPI调起支付](pages/4012090843.md) | `4012090843` | 2025-02-19 03:55:15 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > JSAPI合单支付 |
| 759 | [合单下单-APP](pages/4012760622.md) | `4012760622` | 2024-11-14 08:12:11 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > APP合单支付 |
| 760 | [APP调起支付](pages/4012090949.md) | `4012090949` | 2025-03-28 10:57:37 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > APP合单支付 |
| 761 | [合单下单-H5](pages/4012760626.md) | `4012760626` | 2024-11-14 08:12:10 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > H5合单支付 |
| 762 | [H5调起支付](pages/4012091014.md) | `4012091014` | 2024-10-28 02:58:30 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > H5合单支付 |
| 763 | [合单下单-NATIVE](pages/4012760629.md) | `4012760629` | 2024-11-14 08:12:12 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > Native合单支付 |
| 764 | [Native调起支付](pages/4012091224.md) | `4012091224` | 2024-10-28 02:54:47 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > Native合单支付 |
| 765 | [合单下单-小程序](pages/4012760633.md) | `4012760633` | 2024-11-14 08:12:09 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 小程序合单支付 |
| 766 | [小程序调起支付](pages/4012091236.md) | `4012091236` | 2025-02-18 11:41:37 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 小程序合单支付 |
| 767 | [合单查询订单](pages/4012761049.md) | `4012761049` | 2024-10-24 07:08:30 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 公共API |
| 768 | [合单关闭订单](pages/4012761093.md) | `4012761093` | 2024-10-24 07:09:52 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 公共API |
| 769 | [支付通知](pages/4012237246.md) | `4012237246` | 2024-11-18 09:25:58 | 平台收付通-电商交易解决方案 > 支付下单 > 合单支付 > API列表 > 公共API |
| 770 | [开发指引](pages/4012087888.md) | `4012087888` | 2026-06-10 07:27:51 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 |
| 771 | [业务示例代码](pages/4015870957.md) | `4015870957` | 2026-06-09 09:46:47 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 |
| 772 | [常见问题](pages/4012525463.md) | `4012525463` | 2026-05-21 07:43:02 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 |
| 773 | [请求分账](pages/4012691594.md) | `4012691594` | 2025-09-29 06:45:52 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 774 | [查询分账结果](pages/4012477734.md) | `4012477734` | 2025-09-29 02:09:30 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 775 | [请求分账回退](pages/4012477737.md) | `4012477737` | 2025-09-29 02:06:15 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 776 | [查询分账回退结果](pages/4012477740.md) | `4012477740` | 2025-09-29 02:04:34 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 777 | [解冻剩余资金](pages/4012477745.md) | `4012477745` | 2025-09-29 02:03:23 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 778 | [查询订单剩余待分金额](pages/4012477751.md) | `4012477751` | 2025-09-29 02:02:25 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 779 | [添加分账接收方](pages/4012477758.md) | `4012477758` | 2025-09-29 02:01:53 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 780 | [删除分账接收方](pages/4012477759.md) | `4012477759` | 2025-09-29 02:00:58 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 781 | [分账动账通知](pages/4012116672.md) | `4012116672` | 2025-02-19 03:56:03 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > API列表 |
| 782 | [分账失败处理指引](pages/4015504955.md) | `4015504955` | 2025-07-04 03:08:08 | 平台收付通-电商交易解决方案 > 补差与分账 > 分账 > 附录 |
| 783 | [业务示例代码](pages/4015593692.md) | `4015593692` | 2026-06-10 07:27:50 | 平台收付通-电商交易解决方案 > 补差与分账 > 补差 |
| 784 | [常见问题](pages/4015942503.md) | `4015942503` | 2026-01-22 06:48:53 | 平台收付通-电商交易解决方案 > 补差与分账 > 补差 |
| 785 | [请求补差](pages/4012477631.md) | `4012477631` | 2024-11-04 11:30:10 | 平台收付通-电商交易解决方案 > 补差与分账 > 补差 > API列表 |
| 786 | [请求补差回退](pages/4012477636.md) | `4012477636` | 2024-11-04 11:30:36 | 平台收付通-电商交易解决方案 > 补差与分账 > 补差 > API列表 |
| 787 | [取消补差](pages/4012477639.md) | `4012477639` | 2024-10-24 08:47:04 | 平台收付通-电商交易解决方案 > 补差与分账 > 补差 > API列表 |
| 788 | [业务示例代码](pages/4015217874.md) | `4015217874` | 2026-06-10 07:27:49 | 平台收付通-电商交易解决方案 > 交易退款 |
| 789 | [申请退款](pages/4012476892.md) | `4012476892` | 2024-11-04 11:33:40 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 790 | [查询单笔退款（按微信支付退款单号）](pages/4012476908.md) | `4012476908` | 2024-11-04 11:36:44 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 791 | [查询单笔退款（按商户退款单号）](pages/4012476911.md) | `4012476911` | 2024-11-04 11:36:11 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 792 | [退款结果通知](pages/4012124635.md) | `4012124635` | 2024-11-18 09:25:58 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 793 | [查询垫付回补结果](pages/4012476916.md) | `4012476916` | 2024-11-04 11:40:17 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 794 | [垫付退款回补](pages/4012476927.md) | `4012476927` | 2024-11-04 11:41:31 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 795 | [发起异常退款](pages/4015181616.md) | `4015181616` | 2025-06-06 08:23:46 | 平台收付通-电商交易解决方案 > 交易退款 > API列表 |
| 796 | [常见问题](pages/4016644075.md) | `4016644075` | 2025-11-21 03:07:14 | 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 |
| 797 | [查询二级商户账户实时余额](pages/4012476690.md) | `4012476690` | 2024-11-04 11:47:34 | 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 > API列表 |
| 798 | [查询二级商户账户日终余额](pages/4012476693.md) | `4012476693` | 2024-11-04 11:47:25 | 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 > API列表 |
| 799 | [查询平台账户实时余额](pages/4012476700.md) | `4012476700` | 2024-11-04 11:46:09 | 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 > API列表 |
| 800 | [查询平台账户日终余额](pages/4012476702.md) | `4012476702` | 2024-11-04 11:46:15 | 平台收付通-电商交易解决方案 > 账户资金管理 > 余额查询 > API列表 |
| 801 | [业务示例代码](pages/4019899593.md) | `4019899593` | 2026-06-10 07:27:45 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 |
| 802 | [常见问题](pages/4014075940.md) | `4014075940` | 2026-06-29 01:57:55 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 |
| 803 | [二级商户预约提现](pages/4012476652.md) | `4012476652` | 2024-12-19 07:33:30 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 804 | [二级商户查询预约提现状态（根据商户预约提现单号查询）](pages/4012476656.md) | `4012476656` | 2024-12-19 07:33:26 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 805 | [二级商户查询预约提现状态（根据微信支付预约提现单号查询）](pages/4012476665.md) | `4012476665` | 2024-12-19 07:33:24 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 806 | [平台预约提现](pages/4012476670.md) | `4012476670` | 2024-12-19 07:33:21 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 807 | [平台查询预约提现状态（根据商户预约提现单号查询）](pages/4012476672.md) | `4012476672` | 2024-12-19 07:33:18 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 808 | [平台查询预约提现状态（根据微信支付预约提现单号查询）](pages/4012476674.md) | `4012476674` | 2024-12-19 07:33:16 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 809 | [二级商户按日终余额预约提现](pages/4013328143.md) | `4013328143` | 2024-12-19 08:08:05 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 810 | [查询二级商户按日终余额预约提现状态](pages/4013328163.md) | `4013328163` | 2024-12-19 08:08:05 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 811 | [按日下载提现异常文件](pages/4012476678.md) | `4012476678` | 2024-12-19 07:11:13 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 812 | [商户提现状态变更通知](pages/4013049135.md) | `4013049135` | 2025-02-24 09:49:47 | 平台收付通-电商交易解决方案 > 账户资金管理 > 商户提现 > API列表 |
| 813 | [业务示例代码](pages/4016062108.md) | `4016062108` | 2025-12-04 01:55:05 | 平台收付通-电商交易解决方案 > 账单下载 |
| 814 | [申请交易账单](pages/4012760667.md) | `4012760667` | 2025-04-07 01:51:03 | 平台收付通-电商交易解决方案 > 账单下载 > API列表 |
| 815 | [申请资金账单](pages/4012760672.md) | `4012760672` | 2025-04-07 01:50:55 | 平台收付通-电商交易解决方案 > 账单下载 > API列表 |
| 816 | [申请分账账单](pages/4012761131.md) | `4012761131` | 2025-01-20 08:06:16 | 平台收付通-电商交易解决方案 > 账单下载 > API列表 |
| 817 | [下载账单](pages/4012124894.md) | `4012124894` | 2025-04-16 09:44:14 | 平台收付通-电商交易解决方案 > 账单下载 > API列表 |
| 818 | [申请二级商户资金账单](pages/4012760697.md) | `4012760697` | 2024-10-23 08:14:36 | 平台收付通-电商交易解决方案 > 账单下载 > API列表 |
| 819 | [下载单个子商户/二级商户资金账单](pages/4014314390.md) | `4014314390` | 2025-04-16 03:21:56 | 平台收付通-电商交易解决方案 > 账单下载 > API列表 |
| 820 | [业务示例代码](pages/4015593257.md) | `4015593257` | 2026-06-10 07:27:44 | 平台收付通-电商交易解决方案 > 跨境付款 |
| 821 | [查询订单剩余可出境余额](pages/4012476109.md) | `4012476109` | 2024-11-05 02:17:34 | 平台收付通-电商交易解决方案 > 跨境付款 > API列表 |
| 822 | [申请资金出境](pages/4012476113.md) | `4012476113` | 2024-11-05 02:22:26 | 平台收付通-电商交易解决方案 > 跨境付款 > API列表 |
| 823 | [查询出境结果](pages/4012476127.md) | `4012476127` | 2024-11-05 02:23:59 | 平台收付通-电商交易解决方案 > 跨境付款 > API列表 |
| 824 | [获取购付汇账单文件下载链接](pages/4012476132.md) | `4012476132` | 2024-11-05 02:32:27 | 平台收付通-电商交易解决方案 > 跨境付款 > API列表 |
| 825 | [提交申请单](pages/4014090649.md) | `4014090649` | 2025-03-31 06:45:54 | 平台收付通-电商交易解决方案 > 修改主体信息 > API列表 |
| 826 | [撤销申请单](pages/4014090672.md) | `4014090672` | 2025-03-31 06:45:49 | 平台收付通-电商交易解决方案 > 修改主体信息 > API列表 |
| 827 | [查询申请单状态-使用业务单号](pages/4014090667.md) | `4014090667` | 2025-03-31 06:45:50 | 平台收付通-电商交易解决方案 > 修改主体信息 > API列表 |
| 828 | [查询申请单状态-使用申请单号](pages/4014090655.md) | `4014090655` | 2025-03-31 06:45:51 | 平台收付通-电商交易解决方案 > 修改主体信息 > API列表 |
| 829 | [APIv3概述](pages/4012081673.md) | `4012081673` | 2024-11-21 08:19:57 | Optional > 开发须知 |
| 830 | [总述-APIv3如何签名和验签](pages/4012365870.md) | `4012365870` | 2024-11-21 10:50:08 | Optional > 开发须知 |
| 831 | [基本规则](pages/4012081726.md) | `4012081726` | 2024-07-25 02:06:07 | Optional > 开发须知 > 接口规则说明 |
| 832 | [HTTP状态码](pages/4012081727.md) | `4012081727` | 2024-07-25 02:07:36 | Optional > 开发须知 > 接口规则说明 |
| 833 | [开发必要参数说明](pages/4013080340.md) | `4013080340` | 2026-10-13 03:52:59 | Optional > 开发须知 > 开发参数申请和配置 |
| 834 | [mchid与appid申请](pages/4012081990.md) | `4012081990` | 2025-10-28 03:00:48 | Optional > 开发须知 > 开发参数申请和配置 |
| 835 | [管理商户号绑定的APPID账号](pages/4016329059.md) | `4016329059` | 2025-10-28 03:00:48 | Optional > 开发须知 > 开发参数申请和配置 |
| 836 | [配置APIv3密钥](pages/4012081991.md) | `4012081991` | 2025-10-28 03:00:48 | Optional > 开发须知 > 开发参数申请和配置 |
| 837 | [品牌经营API开发必要参数说明](pages/4015981654.md) | `4015981654` | 2025-12-15 01:50:19 | Optional > 开发须知 > 开发参数申请和配置 |
| 838 | [平台员工权限管理](pages/4013080349.md) | `4013080349` | 2025-09-19 01:36:32 | Optional > 开发须知 > 开发参数申请和配置 |
| 839 | [申请商户API证书](pages/4012081992.md) | `4012081992` | 2025-10-28 03:01:36 | Optional > 开发须知 > 开发参数申请和配置 > 商户API证书管理 |
| 840 | [如何更换商户API证书？](pages/4013058943.md) | `4013058943` | 2024-11-20 03:18:41 | Optional > 开发须知 > 开发参数申请和配置 > 商户API证书管理 |
| 841 | [请求参数里带Path参数（路径参数），如何计算签名](pages/4012365862.md) | `4012365862` | 2025-02-18 08:09:32 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 842 | [请求参数里带Body参数(包体参数），如何计算签名](pages/4012365864.md) | `4012365864` | 2025-02-18 09:53:43 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 843 | [请求参数里有Query（查询参数），如何计算签名](pages/4012365865.md) | `4012365865` | 2025-02-18 09:53:41 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 844 | [图片上传接口，如何计算签名](pages/4012365863.md) | `4012365863` | 2025-03-25 03:03:49 | Optional > 开发须知 > 如何签名 > 如何构造接口请求签名 |
| 845 | [APP调起支付签名](pages/4012365868.md) | `4012365868` | 2025-03-26 09:28:08 | Optional > 开发须知 > 如何签名 > 如何构造调起支付签名 |
| 846 | [JSAPI调起支付签名](pages/4012365867.md) | `4012365867` | 2025-03-26 09:28:07 | Optional > 开发须知 > 如何签名 > 如何构造调起支付签名 |
| 847 | [小程序调起支付签名](pages/4012365869.md) | `4012365869` | 2025-03-26 09:28:05 | Optional > 开发须知 > 如何签名 > 如何构造调起支付签名 |
| 848 | [如何使用微信支付公钥验签](pages/4013059017.md) | `4013059017` | 2024-11-20 06:55:05 | Optional > 开发须知 > 如何验签 |
| 849 | [如何使用平台证书验签名](pages/4013059030.md) | `4013059030` | 2024-11-29 09:43:48 | Optional > 开发须知 > 如何验签 > 如何使用平台证书验签 |
| 850 | [如何使用签名/验签工具](pages/4012365880.md) | `4012365880` | 2024-12-27 04:05:13 | Optional > 开发须知 > 如何验签 > 如何使用平台证书验签 |
| 851 | [如何使用微信支付公钥加密敏感字段](pages/4013059044.md) | `4013059044` | 2025-03-19 08:49:11 | Optional > 开发须知 > 如何加解密敏感字段 |
| 852 | [如何使用平台证书加密敏感字段](pages/4013059053.md) | `4013059053` | 2025-03-19 08:49:03 | Optional > 开发须知 > 如何加解密敏感字段 |
| 853 | [如何使用API证书解密敏感字段](pages/4013059060.md) | `4013059060` | 2024-11-20 03:29:55 | Optional > 开发须知 > 如何加解密敏感字段 |
| 854 | [如何解密回调报文和平台证书](pages/4012082320.md) | `4012082320` | 2024-11-29 08:22:52 | Optional > 开发须知 > 如何解密微信支付回调报文 |
| 855 | [报错：HTTP header缺少微信支付平台证书序列号(Wechatpay-Serial)](pages/4012365874.md) | `4012365874` | 2024-11-19 09:07:14 | Optional > 开发须知 > 常见问题 |
| 856 | [报错：Http头Authorization值格式错误，请参考《微信支付商户REST API签名规则》或者“Authorization不合法”](pages/4012365872.md) | `4012365872` | 2026-01-23 03:31:55 | Optional > 开发须知 > 常见问题 |
| 857 | [报错：商户证书序列号有误。请使用签名私钥匹配的证书序列号](pages/4012365873.md) | `4012365873` | 2024-12-12 03:12:16 | Optional > 开发须知 > 常见问题 |
| 858 | [报错：状态码401或者“错误的签名，验签失败”或者“签名错误，请检查后再试”](pages/4012365875.md) | `4012365875` | 2024-12-12 03:12:14 | Optional > 开发须知 > 常见问题 |
| 859 | [调起支付报错：支付验证签名失败](pages/4012365876.md) | `4012365876` | 2025-03-26 09:28:04 | Optional > 开发须知 > 常见问题 |
| 860 | [使用Java加载密钥时，抛出异常InvalidKeyException: Illegal key size](pages/4013059103.md) | `4013059103` | 2024-11-20 03:37:11 | Optional > 开发须知 > 常见问题 |
| 861 | [使用Java解密时，抛出异常AEADBadTagException: Tag mismatch](pages/4013059153.md) | `4013059153` | 2024-11-20 03:38:02 | Optional > 开发须知 > 常见问题 |
| 862 | [请求返回{"code":"PARAM_ERROR","message":"平台证书序列号Wechatpay-Serial错误"}](pages/4013059161.md) | `4013059161` | 2024-11-20 03:38:49 | Optional > 开发须知 > 常见问题 |
| 863 | [为什么微信支付的回调缺少签名的几个HTTP头？](pages/4013059166.md) | `4013059166` | 2024-11-20 03:39:20 | Optional > 开发须知 > 常见问题 |
| 864 | [如何在程序中加载商户API证书私钥](pages/4013059175.md) | `4013059175` | 2025-12-25 06:37:41 | Optional > 开发须知 > 常见问题 |
| 865 | [为什么请求返回401 Unauthorized？](pages/4012082324.md) | `4012082324` | 2024-11-25 08:53:06 | Optional > 开发须知 > 常见问题 |
| 866 | [验证微信支付响应的签名报错：签名验证失败](pages/4016241895.md) | `4016241895` | 2025-10-14 06:39:36 | Optional > 开发须知 > 常见问题 |
| 867 | [调用接口报错：“平台私钥解密失败”](pages/4016913182.md) | `4016913182` | 2025-12-19 02:59:24 | Optional > 开发须知 > 常见问题 |
| 868 | [跨城冗灾升级指引](pages/4012082567.md) | `4012082567` | 2025-03-21 07:37:49 | Optional > 最佳实践 |
| 869 | [支付回调和查单实现指引](pages/4012082568.md) | `4012082568` | 2026-10-13 09:08:37 | Optional > 最佳实践 |
| 870 | [专线商户Notify升级指引](pages/4012082569.md) | `4012082569` | 2024-07-25 03:04:49 | Optional > 最佳实践 |
| 871 | [回调通知注意事项](pages/4012082570.md) | `4012082570` | 2024-07-25 03:04:49 | Optional > 最佳实践 |
| 872 | [最佳安全实践](pages/4012082456.md) | `4012082456` | 2024-11-27 09:15:00 | Optional > 最佳实践 > API安全最佳实践 |
| 873 | [安全漏洞checklist](pages/4013059657.md) | `4013059657` | 2024-11-27 09:14:52 | Optional > 最佳实践 > API安全最佳实践 |
| 874 | [系统漏洞检测及修复](pages/4013059668.md) | `4013059668` | 2025-03-21 07:40:38 | Optional > 最佳实践 > API安全最佳实践 |
| 875 | [Web漏洞检测及修复](pages/4013059740.md) | `4013059740` | 2025-03-21 08:53:52 | Optional > 最佳实践 > API安全最佳实践 |
| 876 | [最新安全漏洞及修复](pages/4013059970.md) | `4013059970` | 2024-11-27 09:14:33 | Optional > 最佳实践 > API安全最佳实践 |
| 877 | [密钥泄漏修复指引](pages/4012082455.md) | `4012082455` | 2024-12-24 01:54:38 | Optional > 最佳实践 > API安全最佳实践 |
| 878 | [国家商用密码简介](pages/4012082627.md) | `4012082627` | 2024-07-25 03:09:50 | Optional > 国家商用密码接入指南 |
| 879 | [获取国家商用密码证书和密钥](pages/4012082628.md) | `4012082628` | 2024-07-25 03:09:50 | Optional > 国家商用密码接入指南 |
| 880 | [APIv3接口使用国家商用密码指引](pages/4012082629.md) | `4012082629` | 2024-07-25 03:09:50 | Optional > 国家商用密码接入指南 |
| 881 | [开户银行全称对照表](pages/4012082812.md) | `4012082812` | 2024-07-25 03:24:06 | Optional > 对照表 |
| 882 | [开户银行对照表](pages/4012082813.md) | `4012082813` | 2025-02-19 07:30:19 | Optional > 对照表 |
| 883 | [银行类型对照表](pages/4012082814.md) | `4012082814` | 2024-07-25 03:24:06 | Optional > 对照表 |
| 884 | [省市区编号对照表](pages/4012082815.md) | `4012082815` | 2024-07-25 03:24:06 | Optional > 对照表 |
| 885 | [优惠费率活动对照表](pages/4012082816.md) | `4012082816` | 2024-12-26 08:48:22 | Optional > 对照表 |
| 886 | [跨境电商二级商户费率对照表](pages/4012082817.md) | `4012082817` | 2024-07-25 03:24:06 | Optional > 对照表 |
| 887 | [商户行业编码](pages/4012082818.md) | `4012082818` | 2024-07-25 03:24:06 | Optional > 对照表 |
| 888 | [特殊行业ID对照表](pages/4012082819.md) | `4012082819` | 2024-07-25 03:24:06 | Optional > 对照表 |
| 889 | [接入模式](pages/4012081931.md) | `4012081931` | 2026-06-01 06:16:40 | Optional > 名词表 |
| 890 | [支付产品](pages/4012081932.md) | `4012081932` | 2024-07-25 02:23:51 | Optional > 名词表 |
| 891 | [业务平台](pages/4012081933.md) | `4012081933` | 2024-07-25 02:23:51 | Optional > 名词表 |
| 892 | [业务系统](pages/4012081934.md) | `4012081934` | 2024-07-25 02:23:51 | Optional > 名词表 |
| 893 | [参数说明](pages/4012081935.md) | `4012081935` | 2026-10-13 09:47:01 | Optional > 名词表 |
| 894 | [常见问题](pages/4016183684.md) | `4016183684` | 2026-08-05 06:15:10 | Optional > 名词表 |
| 895 | [微信支付链路界面与交互规范](pages/4020527499.md) | `4020527499` | 2026-05-19 02:15:32 | Optional > 服务运营规范 |
| 896 | [Postman调试工具](pages/4012083114.md) | `4012083114` | 2024-11-29 09:45:15 | Optional > 开发工具 |
| 897 | [平台证书下载工具](pages/4012083115.md) | `4012083115` | 2024-11-27 09:13:57 | Optional > 开发工具 |
| 898 | [验签工具](pages/4012083116.md) | `4012083116` | 2025-01-03 07:02:48 | Optional > 开发工具 |
| 899 | [产品介绍](pages/4012083118.md) | `4012083118` | 2025-03-21 07:39:41 | Optional > 网络云排查 |
| 900 | [网络问题排查指南](pages/4012083119.md) | `4012083119` | 2025-03-21 07:39:03 | Optional > 网络云排查 |
| 901 | [常见问题](pages/4012083120.md) | `4012083120` | 2024-07-25 03:43:58 | Optional > 网络云排查 |
| 902 | [产品介绍](pages/4012083122.md) | `4012083122` | 2024-07-25 03:43:58 | Optional > 安全医生 |
| 903 | [诊断链接绑定指引](pages/4012083123.md) | `4012083123` | 2024-07-25 03:43:58 | Optional > 安全医生 |
| 904 | [安全联系人设置指引](pages/4012083124.md) | `4012083124` | 2024-07-25 03:43:58 | Optional > 安全医生 |
| 905 | [SDK概述](pages/4012083109.md) | `4012083109` | 2026-04-24 09:22:07 | Optional > SDK |
| 906 | [使用 Java SDK](pages/4012083111.md) | `4012083111` | 2025-05-29 03:32:06 | Optional > SDK |
| 907 | [使用 PHP SDK](pages/4012083112.md) | `4012083112` | 2025-05-29 03:32:04 | Optional > SDK |
| 908 | [使用 Go SDK](pages/4012083113.md) | `4012083113` | 2025-05-29 03:36:58 | Optional > SDK |

</details>