from odoo import api, fields, models



class ResPartner(models.Model):
    _inherit = 'res.partner'

    iban_no = fields.Char(
        string='IBAN NO',
        required=False)

    supplying_duration = fields.Char(
        string='Supplying Duration',
        required=False)



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    terms_ar = fields.Text(
        string="الشروط و المعايير",
        required=False, default='لا يمكن إلغاء التراخيص المشتراة بمجرد طلبها من البائعين / المصنعين . يبدأ الالتزام بتاريخ التسليم اعتبارا من تاريخ دفع المستحقات المالية لامر الشراء و تأكيد الشركات المصنعة لتوافر المواد و الاستعداد للشحنات و الإرسال من مراكز التصنيع ، بما فى ذلك مستندات الشحن المطلوبة من قبل الهيئة السعودية للمواصفات و المقاييس و الجودة (SASO)  يعتبر هذا خرقا لالتزامات شركة تقدم العالمية فى عقد الشراء (ان وجد) لشروط التسليم شركة تقدم العالمية لا تخضع للمساءلة ، ولن تتحمل أى عواقب لتأخير التسليم بسبب فترة موافقة وزارة الداخلية السعودية - وحدة التراخيص الأمنية للإفراج عن الشحنات ذات الصلة لأنظمة CCTV / FAS / كشف التسلل من خلال التخليص الجمركى فى المنافذ الجمركية السعودية    الشروط و الاحكام :الأسعار جميع الأسعار بالريال السعودى الصلاحية : هذا العرض صالح لمدة 5 أيام عمل ، ما لم يذكر التسليم : 4-5 أيام لبنود المخزون و 8-12 اسبوعيا للمواد غير المخزنة من امر الشراء المؤكد مقابل شروط الدفع ، مالم يذكر هذه الاسعار مخفضة و حصرية لهذا المشروع فقط هذا الاقتراح عبارة عن وحدة واحدة ، ولا يمكن طلب عناصرها بشكل فردى أو تغييرها ما لم يتم النص على ذلك أو بموافقة شركة تقدم العالمية المسبقة السرية : الاسعار و بيانات البائع سرية ، ولن يكشف المشترى أو يتيح لأى طرف ثالث بيانات البائع أو غيرها من المعلومات السرية و الملكية دون الحصول على إذن كتابى مسبق من الشركة العالمية الضمان: وفقا للقوانين المعمول بها فى المملكة ما لم يذكر تركيب المنتج: التركيب و البرمجة و التثبيت و الاختبار و التدريب و التشغيل غير المشمول بالتسعيرة الا اذا تم تضمينها يجب ان يتأكد الشريك من ان الائحة النهائية للمواد تحتوى على جميع المكونات و الخيارات و الملحقات اللازمة لتوفير الوظائف للمشروع المعين ستخضع مواد المخزون و شروط التوفر للبيع المسبق فى حالة عدم وجود طلب رسمى و اصدار شروط الدفع هناك اضطراب فى التوريد فى جميع انحاء العالم ونقص فى مواد الالكترونيات مثل اشباه الموصلات ورقائق الحاسوب والاسعار المتقلبة بسبب جائحة كوفيد 19 لذلك ينصح بشدة بتوقع حدوث تأخير فى التسليم و يجب على المستخدمين النهائيين تطبيق حالات الطوارئ المناسبة مراجعة و قبول الشروط و الاحكام و الملاحظات الخاصة بمقترح شركة تقدم العالمية التجارى من قبل المشترى هنا تعتبر جزءا من امر الشراء للعميل')

    terms_en = fields.Text(
        string="Terms AND Conditions",
        required=False, default='Purchased license cannot be Canceled Once They Have Been Ordered From Vendors/ Manufacturers Delivery Time Will Be Disclosed In Terms Of Releasing Po Payment Term, Manufacturers Confirmation For Materials Availability and to be ready for shipping / dispatch From Manufacturer / Vendor Hub, including required shipping documents by saudi standards , metrology and quality Organization (SASO) . This will not be considered as breach by AICTEC abligations in the pranch contract (if any) for delivery terms AICTEC is unaccountable , and it will not afford for any consequences for delivery delay due to period of saudi MOI - CLU approval to release the related shipments of CCTV / FAS / intrusion detection systems through customs clearance at saudi customs ports .   Terms And Conditions  Prices All Prices are in SAR Validity This quotation is Valid for 5 Working days , unless stated Payment  100% in advance or as per perior agreement Delivery Time 4-5 days for stock items and 8-12 weeks for non-stock materials from confirmed Po against Payment terms , unless stated these prices are discounted and exclusively for this project only , the same prices might this proposal is one unit , and its items cannot be ordered individually or changed unless stated or prior AICTEC agree Confidentiality prices &amp; seller data are confidential , buyer will not disclose or make available to any third party the sellers data or other propriety and confidential information without sellers prior written authorization from AICTEC Warranty As Per KSA standers unless stated Product Installation installation , configuration, testing &amp; commissioning of the above is not included unless stated the partner should ensure that the ultimate BOM contains all necessary components , options and accessories to provice the functions for the designated project  Stock materials and availability terms will be subjected to prior sale , in the case of not an officialordering material and releasing payment terms there is a worldwide supply chain disruption , electronics material shortage such as semiconductor and computer chips and volatile prices , due to the covid 19 pandemic , thus , it is highly advised to delays in delivery should be applied by the end-users review and accept conditions, terms , and notes of commercial proposal by buyer here are considered part of intended client PO ')

    warranty = fields.Char(
        string='Warranty', 
        required=False)

    payment_id = fields.Many2one('account.payment', string="Payment")

    bank_account = fields.Char(
        string='Bank Account',
        required=False)