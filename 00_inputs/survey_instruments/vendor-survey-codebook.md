# Vendor Survey - Long Bien 2024 - Survey Codebook

*Survey Instrument Documentation*

**Total Questions:** 46

**Languages:** Vietnamese (vi), English (en)

---

### `Time`

**Type:** `start`

---

### `end`

**Type:** `end`

---

### `deviceid`

**Type:** `deviceid`

---


## General
*Tổng quan*

### `location`

**Question (EN):** IMPORTANT: Please record the GPS LOCATION for this survey before you knock.
**Question (VI):** QUAN TRỌNG: Vui lòng ghi lại VỊ TRÍ GPS cho cuộc khảo sát này trước khi bạn cố gắng liên lạc với người trả lời.

**Type:** `geopoint`

---

### `surveyorname`

**Question (EN):** Who is the surveyor?
**Question (VI):** Người khảo sát là ai?

**Type:** `select_one surveyors`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `analyn` | Analyn | Analyn |
| `angel` | Angel | Angel |
| `emerson` | Emerson | Emerson |
| `duy` | Duy | Duy |
| `hanh` | Hanh | Hanh |
| `mailinh` | Mai Linh | Mai Linh |
| `ha` | Ha | Ha |
| `volunteer` | Volunteer | Volunteer |
| `lisamarie` | Lisa-Marie | Lisa-Marie |

**Appearance:** `quick`

---

### `vendortype`

**Question (EN):** Type of food vendor?
**Question (VI):** Nhà cung cấp thực phẩm loại nào?

**Type:** `select_one vendortype`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `supermarket` | Siêu thị | Supermarket |
| `marketvendor` | Người bán hàng ở chợ | Market stallholder, seller at a fresh produce market |
| `wholesaler` | Người bán buôn | Wholesaler |
| `street vendor` | Người bán hàng rong bán thực phẩm tươi sống (ví dụ như rau/trái cây/thịt) | Street vendor with fresh food (e.g. vegetables/fruit/meat) |
| `retailer` | Nhà bán lẻ (tiệm bánh, cửa hàng thịt, cửa hàng đặc sản, v.v.) | Retailer (bakery, butcher, specialty store, etc.) |
| `restaurant` | Nhà hàng (ăn tại chỗ) | Restaurant (dine-in) |
| `food truck` | Xe tải bán đồ ăn / người bán hàng rong bán đồ ăn chế biến sẵn hoặc đồ ăn nhẹ | Food truck / take-out street vendor that sells prepared meals or snacks |

**Appearance:** `quick`

---

### `GI_I_THI_U_Xin_ch_o_l_i_n_i_c_a_b_n_ch_a`

**Question (EN):** INTRODUCTION: Hello, my name is ${surveyorname} and I am a student at the University of… We are conducting surveys to investigate the food system in Long Bien. We would like to ask you a few questions about your business, the neighborhood, and why you sell food there. We expect this survey to take about 10 minutes of your time. You can choose not to answer one or more questions. Of course, you can also choose to stop the interview at any time. There are no right or wrong answers. This interview is anonymous: we will not ask for your name. We will not share your personal data and this data will be processed mainly at KU Leuven in Belgium. We want to gain a better understanding of the food system: who eats what type of food in Long Bien? Where is this food obtained, nearby or somewhere else? These are our questions for academic research purposes. The survey is conducted digitally. I can also provide you with an extensive information sheet on paper if you wish. Do I have your verbal informed consent?
**Question (VI):** GIỚI THIỆU: Xin chào, tôi tên là ${surveyorname} và tôi là sinh viên tại Đại học… Chúng tôi đang tiến hành khảo sát để tìm hiểu về hệ thống thực phẩm tại Long Biên. Chúng tôi muốn hỏi bạn một vài câu hỏi về doanh nghiệp của bạn, khu phố và lý do bạn bán thực phẩm ở đó. Chúng tôi dự kiến cuộc khảo sát này sẽ mất khoảng 10 phút của bạn. Bạn có thể chọn không trả lời một hoặc nhiều câu hỏi. Tất nhiên, bạn cũng có thể chọn dừng cuộc phỏng vấn bất cứ lúc nào. Không có câu trả lời đúng hay sai. Cuộc phỏng vấn này là ẩn danh: chúng tôi sẽ không hỏi tên của bạn. Chúng tôi sẽ không chia sẻ dữ liệu cá nhân của bạn và dữ liệu này sẽ được xử lý chủ yếu tại KU Leuven ở Bỉ. Chúng tôi muốn hiểu rõ hơn về hệ thống thực phẩm: ai ăn loại thực phẩm nào ở Long Biên? Thực phẩm này được lấy ở đâu, gần đó hay ở nơi nào khác? Đây là những câu hỏi của chúng tôi cho mục đích nghiên cứu học thuật. Cuộc khảo sát được tiến hành dưới dạng kỹ thuật số. Tôi cũng có thể cung cấp cho bạn một tờ thông tin chi tiết trên giấy nếu bạn muốn. Chúng tôi đã có sự đồng ý bằng lời nói của bạn chưa?

**Type:** `note`

---

### `verbalconsent`

**Question (EN):** The respondent gives consent and understands the purpose of the study. Do NOT proceed without consent.
**Question (VI):** Người trả lời đồng ý và hiểu mục đích của nghiên cứu. KHÔNG tiến hành nếu không có sự đồng ý.

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `now` | KHÔNG | No |

**Appearance:** `quick`

---

### `Kh_ng_c_ph_p_D_ng_a_ra_l_do_t_ch_i`

**Question (EN):** No permission. Stop the survey immediately. Note the reason afterwards if relevant.
**Question (VI):** Không được phép. Dừng khảo sát ngay lập tức. Ghi chú lý do sau đó, nếu người trả lời đưa ra lý do từ chối.

**Type:** `note`

**Display Logic:** Only shown if `selected(${verbalconsent}, 'no')`

---

### `refusalreason`

**Question (EN):** Reason for refusal:
**Question (VI):** Lý do từ chối:

**Type:** `select_multiple refuse_reasons or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `not_home` | Họ không có nhà. | They are not home. |
| `responsible_not_home` | Người đưa ra quyết định về thực phẩm không có ở nhà. | The person who makes the decisions about food is not at home. |
| `no_response` | Có lẽ họ đã về nhà nhưng không mở cửa. | They are probably home but did not open the door. |
| `undisclosed` | Không đưa ra lý do. | No reason given. |
| `uncomfortable` | Họ không thoải mái khi trả lời những câu hỏi khảo sát này. | They are not comfortable answering these survey questions. |
| `no_time` | Họ không có thời gian. | They don't have time. |

**Display Logic:** Only shown if `selected(${verbalconsent}, 'no')`

---

### `neighborhood`

**Question (EN):** Ask the respondent: What is the name of this neighborhood where you sell food?
**Question (VI):** Hỏi người trả lời: Tên của khu phố nơi bạn bán đồ ăn là gì?

**Type:** `text`

---


## Vendor characteristics and location
*Đặc điểm và vị trí của nhà cung cấp*

### `resp_gender`

**Question (EN):** Gender of the respondent/seller
**Question (VI):** Giới tính của người trả lời/người bán

**Type:** `select_one gender`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `male` | Nam | Man |
| `female` | Nữ | Woman |
| `X` | Khác | X (Non-binary, Nonconforming, Fluid, prefer not to say) |

---

### `age`

**Question (EN):** What is your age?
**Question (VI):** Bạn bao nhiêu tuổi?

**Type:** `integer`

---

### `resp_owner`

**Question (EN):** Is the respondent the owner/main operator of this business?
**Question (VI):** Người trả lời có phải là chủ sở hữu/người điều hành chính của doanh nghiệp này không?

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `now` | KHÔNG | No |

---

### `staff`

**Question (EN):** How many people work here (including yourself)
**Question (VI):** Có bao nhiêu người làm việc ở đây (bao gồm cả bạn)

**Type:** `integer`

---

### `resp_ethn`

**Question (EN):** What is your ethnicity?
**Question (VI):** Dân tộc của bạn là gì?

**Type:** `select_one ethnicity or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `kinh` | Kinh | Kinh |
| `muong` | Mường | Muong |
| `tay` | Tay | Tay |
| `thai` | Thái | Thai |
| `mixed` | Lai | Mixed |
| `other` | Khác | Other |
| `dontknow` | Tôi không biết | I don't know |

**Appearance:** `quick`

---


## What types of food are sold here?
*Những loại thực phẩm nào được bán ở đây?*

### `foodgroups`

**Question (EN):** Describe the food products (meals and snacks) you sell at this location.
**Question (VI):** Mô tả các sản phẩm thực phẩm (đồ ăn bình thường và đồ ăn nhẹ) mà bạn bán tại địa điểm này.

**Type:** `select_multiple foodgroups`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `cereals` | LƯƠNG THỰC (ngô, gạo, lúa mì, bánh mì, mì, cháo, mì ống, v.v.) | GRAINS (corn, rice, wheat, bread, noodles, porridge, pasta, etc…) |
| `whiterootsandtubers` | RỄ VÀ CỦ TRẮNG (khoai tây, khoai lang, khoai môn, sắn trắng,… hoặc các loại rễ khác) | WHITE ROOTS AND TUBERS (potatoes, white sweet potato, white cassava, kwak, Chinese tayer … or other roots) |
| `veg_vitamina` | RAU CỦ CÓ VITAMIN A (bí ngô, cà rốt, ớt chuông (bất kỳ loại nào có màu cam bên trong)) | VEGETABLES AND TUBERS WITH VITAMIN A (pumpkin, carrot, orange sweet potato, bell pepper (anything orange inside)) |
| `veg_darkgreenleafy` | RAU LÁ XANH ĐẬM (lá cải, lá sắn, rau mồng tơi, rau ngót, bắp cải,...) | DARK GREEN LEAFY VEGETABLES (claroen, cassava leaves, spinach, amsoi, pak choi, cabbage, bitawiri all leaves…) |
| `veg_other` | CÁC LOẠI RAU KHÁC (cà chua, hành tây, hành lá, cà tím, đậu bắp,...) | OTHER VEGETABLES (tomato, onion, eggplant/boulangerie, poe, sopropo, antroea, soekwa, okra, broccoli…) |
| `fruits_vitamina` | TRÁI CÂY CÓ VITAMIN A (xoài, dưa, đu đủ, dưa hấu, chanh dây, bưởi,... hoặc 100% nước ép của chúng) | FRUIT WITH VITAMIN A (mango, melon, papaya, watermelon, passion fruit/makoesa, grapefruit, sapotilla or 100% juices thereof) |
| `fruits_other` | TRÁI CÂY KHÁC (chuối, cam, acai, quả mọng, anh đào, thanh long, vải, chôm chôm, táo, lựu, chanh,... hoặc 100% nước ép của những loại này) | OTHER FRUIT (banana/baking, orange, acai, berries, cherries, dragon fruit, lychee/rambutang, apple, pomeranian, lime ... or 100% juices of these) |
| `meat_organ` | THỊT NỘI TẾ (gan, thận, tim hoặc các loại thịt nội tạng khác) | ORGAN MEATS (liver, kidney, heart or other organ meats or blood based foods) |
| `meat_flesh` | CÁC LOẠI THỊT KHÁC (thịt bò, thịt lợn, thịt cừu, thịt dê, thịt thỏ, thịt thú rừng, thịt gà, côn trùng...) | OTHER MEAT (beef, pork, lamb, goat, rabbit, game, chicken, insects...) |
| `eggs` | TRỨNG (gà, vịt hoặc loại khác) | EGGS (chicken, duck or other) |
| `fish_seafood` | CÁ VÀ HẢI SẢN (cá hoặc động vật có vỏ (tươi hoặc khô)) | FISH AND SEAFOOD (fresh or dried fish or shellfish) |
| `legumes_nuts_seeds` | CÁC LOẠI ĐẬU, HẠT VÀ HẠT GIỐNG (đậu đen, đậu đỏ, đậu xanh, đỗ, đậu Hà Lan, đậu lăng, sim, các loại hạt, hạt dẻ, hạnh nhân, đậu phộng hoặc thực phẩm làm từ những loại này) | LEGUMES, NUTS AND SEEDS (beans, runner beans, peas, lentils, sim, nuts, seeds, peanuts or foods made from these) |
| `milk` | SỮA VÀ CÁC SẢN PHẨM TỪ SỮA (sữa, pho mát, sữa chua hoặc các loại khác) | MILK AND DAIRY PRODUCTS (milk, cheese, yoghurt or other) |
| `oils_fats` | DẦU VÀ CHẤT BÉO (dầu, chất béo hoặc bơ được thêm vào thực phẩm hoặc dùng để nấu ăn) | OILS AND FATS (oil, fats or butter added to food or used for cooking) |
| `sweets` | ĐỒ NGỌT (đường, mật ong, nước ngọt có đường hoặc nước ép trái cây có đường, thực phẩm có đường như sô cô la, kẹo, bánh quy và bánh ngọt) | SWEETS (sugar, honey, sweetened soft drinks or sweetened fruit juices, sugary foods such as chocolate, candy, cookies and cake) |
| `spices_cond_bev` | THẢO MỘC, SỐT, ĐỒ UỐNG (gia vị, hạt tiêu, muối, nước tương, nước sốt cay, cà phê, trà, đồ uống có cồn) | HERBS, SAUCES, DRINKS (spices, pepper, salt, soy sauce, hot sauce, coffee, tea, alcoholic beverages) |

---

### `wholeorprocessed`

**Question (EN):** Surveyor: Do you see mostly unprocessed foods (eg whole vegetables, fruits, meat, etc.) or mostly prepared/processed foods (meals, snacks, sauces, etc.)?
**Question (VI):** Người khảo sát: Bạn thấy chủ yếu là thực phẩm chưa qua chế biến (ví dụ như rau củ, trái cây, thịt, v.v.) hay chủ yếu là thực phẩm đã chế biến/đóng hộp sẵn (đồ ăn nhẹ, nước sốt, v.v.)?

**Type:** `select_one whole_processed`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `whole` | Hầu hết là thực phẩm chưa qua chế biến/"nguyên chất" | Mostly unprocessed/"whole" foods |
| `processed` | Chủ yếu là thực phẩm chế biến/sẵn sàng (bữa ăn, món ăn kèm, đồ ăn nhẹ, nước sốt…) | Mainly processed/prepared foods (meals, side dishes, snacks, sauces…) |

---


## Vendor location
*Vị trí nhà cung cấp*

### `locationtime`

**Question (EN):** How many years have you been active as a food vendor AT THIS LOCATION (specifically here)?
**Question (VI):** Bạn đã hoạt động kinh doanh thực phẩm TẠI ĐỊA ĐIỂM NÀY (cụ thể là ở đây) bao nhiêu năm rồi?

**Type:** `integer`

---

### `previouslocation`

**Question (EN):** Is this your first location selling food? If not, WHERE have you sold food before?
**Question (VI):** Đây có phải là địa điểm đầu tiên bạn bán đồ ăn không? Nếu không, trước đây bạn đã bán đồ ăn ở ĐÂU?

**Type:** `select_one previouslocation`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `none` | Đây là nơi đầu tiên tôi bán đồ ăn, tôi chưa từng bán đồ ăn ở bất kỳ nơi nào khác. | This is the first place I ever sold food, I never sold food anywhere else. |
| `NUA` | Ở một phần khác của Long Biên | In another part of Long Bien |
| `city` | Ở Hà Nội | In Hanoi |
| `country` | Ở một nơi khác trong nước, ngoài Hà Nội/Long Biên | In another part of the country, outside Hanoi/Long Bien |
| `abroad` | Trước đây tôi đã bán thực phẩm ở nước ngoài | Before this I sold food abroad |

---

### `previouslocationNUA`

**Question (EN):** In which neighborhood in Long Bien were you previously active as a food vendor?
**Question (VI):** Trước đây bạn từng hoạt động bán hàng rong ở khu vực nào tại Long Biên?

**Type:** `select_one longbien_neighbourhoods`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `anlac` | An Lac | An Lac |
| `doclap` | Độc Lập | Doc Lap |
| `dongduha` | Dong Du Ha | Dong Du Ha |
| `ducgiang` | Duc Giang | Duc Giang |
| `khutapthe` | Khu Tập Thể 918 | Khu Tap The 918 |
| `langtram` | Làng Trạm | Lang Tram |
| `lamdu` | Lam Du / Bo De | Lam Du/Bo De |
| `pholemat` | Pho Le Mat | Pho Le Mat |
| `phucloi` | Phúc Lợi | Phuc Loi |
| `saidong` | Sài Đồng | Sai Dong |
| `thachban` | Thạch Bàn | Thach Ban |
| `thachcaueast` | Thạch Cầu (Đông) | Thach Cau (East) |
| `thachcauwest` | Thạch Cầu (Tây) | Thach Cau (West) |
| `thongnhat` | Thống Nhất | Thong Nhat |
| `thonngo` | Thôn Ngô | Thôn Ngô |
| `thongvang` | Thôn Vàng | Thôn Vàng |
| `thuonghoi` | Thượng Hội | Thuong Hoi |
| `tudinh` | Tư Đình | Tu Dinh |
| `viethung` | Viet Hung | Viet Hung |
| `vinhomesriverside` | Vinhomes Riverside | Vinhomes Riverside |
| `xombai` | Xóm Bài | Xom Bai |
| `xomle` | Xóm Lẻ | Xom Le |
| `xuandoha` | Xuân Đỗ Hạ | Xuan Do Ha |
| `LongBien_other` | Nơi khác ở Long Biên | Elsewhere in Long Bien |

**Display Logic:** Only shown if `selected(${previouslocation}, 'NUA')`

---

### `homelocation`

**Question (EN):** In which region do you live?
**Question (VI):** Bạn sống ở vùng nào?

**Type:** `select_one foodenvlocation`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `home` | Ở đây (thực phẩm bán tận nhà/tại nhà có doanh nghiệp) | Here (food sold to home/home with business) |
| `street` | Trên con phố này | In this street |
| `neighbourhood` | Trong khu dân cư này | In this residential area |
| `adminunit` | Trong khu nghỉ mát này | In this commune |
| `district` | Nơi khác ở quận Long Biên | Elsewhere in Long Bien district |
| `city` | Ở trung tâm thành phố (Hà Nội) | In the city center (Hanoi) |
| `country` | Nơi khác ở Việt Nam | Elsewhere in Vietnam |
| `abroad` | Ở nước ngoài (ví dụ như Guiana thuộc Pháp) | Abroad (e.g. French Guiana) |

---

### `reason`

**Question (EN):** What was the main reason you started selling food/starting a business here in this location?
**Question (VI):** Lý do chính khiến bạn bắt đầu bán thực phẩm/khởi nghiệp ở địa điểm này là gì?

**Type:** `text`

---


## Think back to when you first started your business here, in ${locationtime}. How important were the following factors to you in selling food at this location?
*Hãy nghĩ lại khi bạn mới bắt đầu kinh doanh tại đây, ở ${locationtime}. Các yếu tố sau đây quan trọng như thế nào đối với bạn khi bán thực phẩm tại địa điểm này?*

### `bridge_city`

**Question (EN):** Distance to the BRUG (the city centre).
**Question (VI):** Khoảng cách đến cầu (trung tâm thành phố).

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / Trung tính | Average / Neutral |
| `1` | Rất quan trọng / ưu tiên | Very important / priority |

**Appearance:** `quick`

---

### `customers_neighb`

**Question (EN):** Many customers live in this area.
**Question (VI):** Có nhiều khách hàng sống ở khu vực này.

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / Trung tính | Average / Neutral |
| `1` | Rất quan trọng / ưu tiên | Very important / priority |

**Appearance:** `quick`

---

### `customers_passersby`

**Question (EN):** Many customers PASS this street, for example because they are on their way to work/home, or work nearby.
**Question (VI):** Nhiều khách hàng ĐI QUA con phố này vì họ đang trên đường đi làm/về nhà hoặc làm việc gần đó.

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / Trung tính | Average / Neutral |
| `1` | Rất quan trọng / ưu tiên | Very important / priority |

**Appearance:** `quick`

---

### `supplychain`

**Question (EN):** Distance to suppliers/wholesalers.
**Question (VI):** Khoảng cách tới nhà cung cấp/nhà bán buôn.

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / Trung tính | Average / Neutral |
| `1` | Rất quan trọng / ưu tiên | Very important / priority |

**Appearance:** `quick`

---

### `safe_reputation`

**Question (EN):** When you decided to sell here, in ${locationtime}, how important was to you: the SAFETY of the neighborhood/good reputation
**Question (VI):** Khi bạn quyết định bán ở đây, tại ${locationtime}, bạn quan tâm đến điều gì: SỰ AN TOÀN của khu phố/uy tín tốt

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / Trung tính | Average / Neutral |
| `1` | Rất quan trọng / ưu tiên | Very important / priority |

**Appearance:** `quick`

---

### `flooding`

**Question (EN):** The sensitivity of this location to FLOODS
**Question (VI):** Vị trí này khó bị LŨ LỤT ngập

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / Trung tính | Average / Neutral |
| `1` | Rất quan trọng / ưu tiên | Very important / priority |

**Appearance:** `quick`

---

### `infrastructure`

**Question (EN):** General INFRASTRUCTURE (electricity, gas, paved road, etc.)
**Question (VI):** CƠ SỞ HẠ TẦNG chung (điện, khí đốt, đường trải nhựa, v.v.)

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / Trung tính | Average / Neutral |
| `1` | Rất quan trọng / ưu tiên | Very important / priority |

**Appearance:** `quick`

---

### `presence`

**Question (EN):** PRESENCE of other food vendors (e.g. if there was already a market here and you could join)
**Question (VI):** Ở đây có những người kinh doanh thực phẩm khác (ví dụ nếu đã có một khu chợ ở đây và bạn có thể tham gia)

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / Trung tính | Average / Neutral |
| `1` | Rất quan trọng / ưu tiên | Very important / priority |

**Appearance:** `quick`

---

### `absence`

**Question (EN):** ABSENCE of other food vendors (lack of supply in this area/gap in the market/wanted to be the only one)
**Question (VI):** KHÔNG CÓ nhà cung cấp thực phẩm khác (thiếu nguồn cung ở khu vực này/trên thị trường ít/bạn là người duy nhất kinh doanh tại đây)

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / Trung tính | Average / Neutral |
| `1` | Rất quan trọng / ưu tiên | Very important / priority |

**Appearance:** `quick`

---

### `schools`

**Question (EN):** Think back to ${locationtime}, when you decided to come and sell here. How important was the: distance to SCHOOLS
**Question (VI):** Hãy nghĩ lại về ${locationtime}, khi bạn quyết định kinh doanh ở đây. Khoảng cách từ vị trí của bạn đến trường quan trọng như thế nào

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / Trung tính | Average / Neutral |
| `1` | Rất quan trọng / ưu tiên | Very important / priority |

**Appearance:** `quick`

---

### `leisure`

**Question (EN):** Distance to RECREATION (sports, music, parks…)
**Question (VI):** Khoảng cách đến các khu vực GIẢI TRÍ (thể thao, phòng tập gym, chỗ xem ca nhạc, công viên…)

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / Trung tính | Average / Neutral |
| `1` | Rất quan trọng / ưu tiên | Very important / priority |

**Appearance:** `quick`

---


## Statements_vendor
*Nhà cung cấp báo cáo*

### `B_n_ng_hay_kh_ng_h_ng_tuy_n_b_sau_y`

**Question (EN):** Do you agree or disagree (or are neutral) with respect to the following statements?
**Question (VI):** Bạn đồng ý hay không đồng ý (hoặc trung lập) với những tuyên bố sau đây?

**Type:** `note`

---

### `customers_wealth`

**Question (EN):** The customers who buy food from me are almost all wealthy/rich.
**Question (VI):** Những khách hàng mua đồ ăn hầu hết đều là người có điều kiện.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | Không đồng ý (hoàn toàn/hoàn toàn không đồng ý) | Disagree (completely/strongly disagree) |
| `-1` | Không đồng ý chút nào | Slightly disagree |
| `0` | Trung lập (như những nơi khác/không quan tâm/không biết gì) | Neutral (as elsewhere/don't care/no idea) |
| `1` | Đồng ý một chút | Somewhat agree |
| `2` | Đồng ý (hoàn toàn/hoàn toàn đồng ý/hoàn toàn đồng ý) | Agree (completely/strongly/completely agree) |

**Appearance:** `quick`

---

### `customers_ethn`

**Question (EN):** The customers who buy food from me mainly come from one particular/specific ethnic group.
**Question (VI):** Những khách hàng mua thực phẩm của tôi chủ yếu từ một nhóm dân tộc cụ thể.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | Không đồng ý (hoàn toàn/hoàn toàn không đồng ý) | Disagree (completely/strongly disagree) |
| `-1` | Không đồng ý chút nào | Slightly disagree |
| `0` | Trung lập (như những nơi khác/không quan tâm/không biết gì) | Neutral (as elsewhere/don't care/no idea) |
| `1` | Đồng ý một chút | Somewhat agree |
| `2` | Đồng ý (hoàn toàn/hoàn toàn đồng ý/hoàn toàn đồng ý) | Agree (completely/strongly/completely agree) |

**Appearance:** `quick`

---

### `rathersomewhereelse`

**Question (EN):** I would rather sell food elsewhere (anywhere else), but this is the best location I can afford/can afford.
**Question (VI):** Tôi muốn kinh doanh đồ ăn ở nơi khác (bất kỳ nơi nào khác), nhưng đây là địa điểm phù hợp vơi điều kiện tài chính của tôi.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | Không đồng ý (hoàn toàn/hoàn toàn không đồng ý) | Disagree (completely/strongly disagree) |
| `-1` | Không đồng ý chút nào | Slightly disagree |
| `0` | Trung lập (như những nơi khác/không quan tâm/không biết gì) | Neutral (as elsewhere/don't care/no idea) |
| `1` | Đồng ý một chút | Somewhat agree |
| `2` | Đồng ý (hoàn toàn/hoàn toàn đồng ý/hoàn toàn đồng ý) | Agree (completely/strongly/completely agree) |

**Appearance:** `quick`

---

### `ratherothersector`

**Question (EN):** I would rather run another business, but selling food is the only realistic/profitable venture for me at this time.
**Question (VI):** Tôi muốn mở một doanh nghiệp khác, nhưng kinh doanh thực phẩm là công việc đem lại lợi nhuận duy nhất đối với tôi hiện tại.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | Không đồng ý (hoàn toàn/hoàn toàn không đồng ý) | Disagree (completely/strongly disagree) |
| `-1` | Không đồng ý chút nào | Slightly disagree |
| `0` | Trung lập (như những nơi khác/không quan tâm/không biết gì) | Neutral (as elsewhere/don't care/no idea) |
| `1` | Đồng ý một chút | Somewhat agree |
| `2` | Đồng ý (hoàn toàn/hoàn toàn đồng ý/hoàn toàn đồng ý) | Agree (completely/strongly/completely agree) |

**Appearance:** `quick`

---

### `_5yr_changesector`

**Question (EN):** I plan to stop selling food in the next five years.
**Question (VI):** có kế hoạch ngừng kinh doanh thực phẩm trong năm năm tới.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | Không đồng ý (hoàn toàn/hoàn toàn không đồng ý) | Disagree (completely/strongly disagree) |
| `-1` | Không đồng ý chút nào | Slightly disagree |
| `0` | Trung lập (như những nơi khác/không quan tâm/không biết gì) | Neutral (as elsewhere/don't care/no idea) |
| `1` | Đồng ý một chút | Somewhat agree |
| `2` | Đồng ý (hoàn toàn/hoàn toàn đồng ý/hoàn toàn đồng ý) | Agree (completely/strongly/completely agree) |

**Appearance:** `quick`

---

### `_5yr_changelocation`

**Question (EN):** I plan to continue selling food for the next five years, but will change my location.
**Question (VI):** Tôi dự định sẽ tiếp tục kinh doanh thực phẩm trong năm năm tới nhưng sẽ thay đổi địa điểm.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | Không đồng ý (hoàn toàn/hoàn toàn không đồng ý) | Disagree (completely/strongly disagree) |
| `-1` | Không đồng ý chút nào | Slightly disagree |
| `0` | Trung lập (như những nơi khác/không quan tâm/không biết gì) | Neutral (as elsewhere/don't care/no idea) |
| `1` | Đồng ý một chút | Somewhat agree |
| `2` | Đồng ý (hoàn toàn/hoàn toàn đồng ý/hoàn toàn đồng ý) | Agree (completely/strongly/completely agree) |

**Appearance:** `quick`

---


## Typhoon_Yagi
*Typhoon_Yagi*

### `B_y_gi_h_y_ngh_n_ng_g_n_y_nh_t_Yagi`

**Question (EN):** Now, please think of the most recent serious Typhoon event (Yagi).
**Question (VI):** Bây giờ, hãy nghĩ đến sự kiện Bão nghiêm trọng gần đây nhất (Yagi).

**Type:** `note`

---

### `typhoon_prepare`

**Question (EN):** Which of the following activities did you undertake in the days leading up to the Typhoon, to prepare? (related to food-selling activities)
**Question (VI):** Bạn đã thực hiện hoạt động nào sau đây trong những ngày trước khi Bão đổ bộ để chuẩn bị? (liên quan đến hoạt động bán thực phẩm)

**Type:** `select_multiple typh_prepare`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `stockpiling` | Dự trữ nhu yếu phẩm: mua và dự trữ thêm thực phẩm, đặc biệt là hàng hóa không dễ hư hỏng như gạo, mì khô và các sản phẩm đóng hộp. | Stockpiling Essentials: purchase and store extra food supplies, especially non-perishable goods like rice, dried noodles, and canned products. |
| `securing` | Đảm bảo hàng tồn kho: Bảo vệ các mặt hàng (dễ hư hỏng) bằng cách lưu trữ chúng ở những nơi được bảo vệ trong cửa hàng này. | Securing Inventory: Safeguarding (perishable) items by storing them in protected places within this shop. |
| `securing_away` | Đảm bảo hàng tồn kho: Bảo vệ các mặt hàng (dễ hư hỏng) bằng cách di chuyển chúng đến những địa điểm an toàn hơn, tránh xa các khu vực dễ bị lũ lụt. | Securing Inventory: Safeguarding (perishable) items by moving them to safer locations away from flood-prone zones. |
| `adjusting_hours` | Điều chỉnh giờ kinh doanh: Đóng cửa tạm thời trước khi bão đến hoặc hoạt động trong thời gian ngắn hơn để đảm bảo an toàn. | Adjusting Business Hours: Temporarily closing before the typhoon's arrival or operating shorter hours to ensure safety. |
| `relocating` | Di dời hoạt động đến những địa điểm an toàn hơn | Relocating operations to safer locations |
| `strengthening_infrastructure` | Tăng cường/gia cố cơ sở hạ tầng để chống chọi với gió mạnh và mưa lớn (sử dụng bạt, bao cát, gỗ hoặc các vật liệu ổn định khác) | Strengthening/reinforcing infrastructure to withstand strong winds and heavy rain (using tarps, sandbags, wood, or other stabilizing materials) |
| `diversifying_products` | Đa dạng hóa sản phẩm cung cấp: bằng cách tập trung vào các mặt hàng có sẵn và dễ dự trữ hoặc vận chuyển sau bão. | Diversifying Product Offering: by focusing on items that are readily available and easy to stock or transport post-typhoon. |
| `collaborating_withs` | Hợp tác với các nhà cung cấp địa phương: Xây dựng mối quan hệ với nông dân và nhà cung cấp địa phương, những người có thể dễ tiếp cận hơn sau cơn bão | Collaborating with Local Suppliers: Building relationships with local farmers and suppliers who may be more accessible after the typhoon |
| `saving_cash` | Tiết kiệm tiền mặt cho các trường hợp khẩn cấp: Giữ tiền mặt dự trữ để trang trải chi phí hoạt động hoặc cung ứng | Saving Cash for Emergencies: Keeping cash reserves to cover operational or supply costs |
| `communicating_customers` | Giao tiếp với khách hàng: Thông báo cho khách hàng thường xuyên về những thay đổi tạm thời trong hoạt động thông qua phương tiện truyền thông xã hội, ứng dụng nhắn tin hoặc truyền miệng. | Communicating with Customers: Informing regular customers about temporary changes in operations via social media, messaging apps, or word of mouth. |
| `contingency_poweroutages` | Lập kế hoạch dự phòng cho tình trạng mất điện: các giải pháp dự phòng như máy phát điện hoặc hộp đá để giữ thực phẩm dễ hỏng tươi nếu mất điện. | Contingency Planning for Power Outages: backup solutions such as generators or ice boxes to keep perishable food fresh if electricity is disrupted. |

---

### `typhoon_cope`

**Question (EN):** Which of the following activities did you undertake in during the Typhoon and subsequent flooding, to cope? (related to food-selling activities)
**Question (VI):** Bạn đã thực hiện hoạt động ứng phó nào sau đây trong thời gian Bão đổ bộ và lũ lụt sau bão? (liên quan đến hoạt động bán thực phẩm)

**Type:** `select_multiple typh_cope`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `close_full` | Đóng cửa hàng/quầy hàng cho đến khi gió/lũ lụt hoàn toàn dừng lại (đóng cửa nhiều ngày) | Close shop/stall until all wind/flooding completely stopped (multiple days closed) |
| `close_typhoon` | Đóng cửa hàng/quầy hàng cho đến khi bão hoàn toàn dừng lại, nhưng vẫn mở cửa trong thời gian lũ lụt (đóng cửa một ngày) | Close shop/stall until typhoon completely stopped, but remained open during floods (one day closed) |
| `inside_home` | Ở trong nhà (ở nhà, không ở gần hoặc gần cửa hàng này) | Stay inside (at home, not attached or close to this shop) |
| `inside_here` | Ở trong nhà (ở nhà, ở đây) | Stay inside (at home, here) |
| `cheaper` | Giảm giá thực phẩm để thu hút nhiều khách hàng hơn. | Make food cheaper to attract more clients. |
| `more_expensive` | Giảm giá thực phẩm, vì cần thiết hoặc vì mọi người sẵn sàng trả nhiều tiền hơn sau cơn bão. | Make food more expensive, out of necessity or becausepeople are willing to pay more after a typhoon. |
| `sharing` | Chia sẻ/trao đổi thực phẩm với những người bán hàng khác | Share/exchange food with other vendors |

---

### `typhoon_financial`

**Question (EN):** Have there been any financial losses, and if so, has your business financially recovered from this Typhoon event?
**Question (VI):** Đã có bất kỳ tổn thất tài chính nào không và nếu có, doanh nghiệp, cửa hàng ăn của bạn đã phục hồi tài chính sau sự kiện Bão này chưa?

**Type:** `select_one typh_financial`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `severe_not` | Tổn thất tài chính nghiêm trọng, không được phục hồi | Severe financial losses, not recovered |
| `severe_partly` | Tổn thất tài chính nghiêm trọng, phục hồi một phần | Severe financial losses, partly recovered |
| `severe_fully` | Tổn thất tài chính nghiêm trọng, phục hồi hoàn toàn | Severe financial losses, fully recovered |
| `moderate_not` | Tổn thất tài chính vừa phải, không được phục hồi | Moderate financial losses, not recovered |
| `moderate_party` | Tổn thất tài chính vừa phải, bên được phục hồi | Moderate financial losses, party recovered |
| `moderate_fully` | Tổn thất tài chính vừa phải, phục hồi hoàn toàn | Moderate financial losses, fully recovered |
| `no_losses` | Không có tổn thất tài chính nào cả | No financial losses at all |
| `better_situation` | Tình hình tài chính tốt hơn trước | Better financial situation than before |

---

### `typhoon_damages`

**Question (EN):** Have there been any physical damages, and if so, has your business physically recovered from this Typhoon event?
**Question (VI):** Đã có bất kỳ thiệt hại vật chất nào không và nếu có, doanh nghiệp của bạn đã phục hồi về vật chất của cải sau trận Bão này chưa?

**Type:** `select_one typh_damages`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `severe_not` | Thiệt hại vật chất nghiêm trọng, không được phục hồi | Severe physical damages, not recovered |
| `severe_partly` | Thiệt hại vật chất nghiêm trọng, phục hồi một phần | Severe physical damages, partly recovered |
| `severe_fully` | Thiệt hại vật chất nghiêm trọng, phục hồi hoàn toàn | Severe physical damages, fully recovered |
| `moderate_not` | Thiệt hại vật chất vừa phải, không được phục hồi | Moderate physical damages, not recovered |
| `moderate_party` | Thiệt hại vật chất vừa phải, bên được phục hồi | Moderate physical damages, party recovered |
| `moderate_fully` | Thiệt hại vật chất vừa phải, phục hồi hoàn toàn | Moderate physical damages, fully recovered |
| `no_damages` | Không có thiệt hại vật chất nào cả | No physical damages at all |

---


## Food waste management
*Quản lý chất thải thực phẩm*

### `foodwaste_amount`

**Question (EN):** Approximately, how much food does your business discard per day/week/month?
**Question (VI):** Khoảng bao nhiêu thực phẩm doanh nghiệp của bạn thải ra mỗi ngày/tuần/tháng?

**Type:** `select_one wastequantities`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `0` | Không |  |
| `0.1` | Dưới 100 g | Less than 100 g |
| `0.5` | Dưới 500 g | Less than 500 g |
| `1` | Dưới 1 kg | Less than 1 kg |
| `3` | Dưới 3 kg | Less than 3 kg |
| `5` | Dưới 5 kg | Less than 5 kg |
| `10` | Trên 5 kg | More than 5 kg |

---

### `foodwaste_amount_unit`

**Question (EN):** That amount is discarded per:
**Question (VI):** Lượng thực phẩm đó được thải ra mỗi:

**Type:** `select_one dayweekmonth`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `day` | Ngày | Day |
| `week` | Tuần | Week |
| `month` | Tháng | Month |

---

### `foodwaste_freq`

**Question (EN):** How often does your business discard food?
**Question (VI):** Doanh nghiệp của bạn thải bỏ thực phẩm thường xuyên như thế nào?

**Type:** `select_one frequency`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `1` | hai lần hoặc nhiều hơn mỗi ngày | twice or more per day |
| `2` | một lần mỗi ngày | once every day |
| `3` | một vài lần một tuần | a few times a week |
| `4` | một vài lần một tháng | a few times a month |
| `5` | một vài lần một năm | a few times a year |
| `6` | hiếm khi | rarely |
| `7` | không biết | do not know |

---

### `foodwaste_mainreason`

**Question (EN):** What are the main reasons your business needs to discard food?
**Question (VI):** Những lý do chính khiến doanh nghiệp của bạn cần thải bỏ thực phẩm là gì?

**Type:** `select_multiple wastereasons`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `deteriorated` | Chất lượng kém (bị giảm sút) | Quality went bad (deteriorated) |
| `usebydate` | Đã qua ngày ‘sử dụng’ | Passed ‘use-by’ date |
| `unappetizing` | Không ngon, không thích mùi vị hoặc không hài lòng với thức ăn sau khi ăn vài miếng | Unappetizing, did not like the taste or dissatisfied with the food after a few bites |
| `toomuch` | Tôi đã làm hoặc gọi quá nhiều thức ăn | I made or ordered too much food |
| `toomanyingredients` | Tôi có quá nhiều nguyên liệu để nấu mà tôi không sử dụng | I had too many ingredients to cook that I did not use |
| `other` | Khác | Other |

---

### `foodwaste_whatdo`

**Question (EN):** What do you usually do with the food that is discarded?
**Question (VI):** Bạn thường làm gì với lượng thực phẩm bị thải bỏ?

**Type:** `select_multiple wasteuses`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `throwaway` | Vứt bỏ (vào thùng rác) | Throw it away (in the bin) |
| `giveaway` | Cho hàng xóm, bạn bè hoặc gia đình | Give it to neighbours, friends or family |
| `foodbank` | Mang đến ngân hàng thực phẩm | Bring it to food bank |
| `composting_community` | Ủ phân cộng đồng | Community composting |
| `composting_hh` | Ủ phân hộ gia đình | Household composting |
| `animalfood` | Sử dụng làm thức ăn cho động vật | Use it as animal food |
| `other` | Khác | Other |

---


## Debriefing
*Tóm tắt*

### `Xin_ch_n_th_nh_c_m_m_t_ng_y_th_t_vui_v`

**Question (EN):** Thank you very much for your cooperation. Your anonymous answers will be important for scientific research and my studies at VNU & KU Leuven (Belgium). If you have any questions, you can always send an e-mail to: [LOCAL CONTACT]. If you wish to receive the results of this research, we kindly request you to provide your e-mail address (we will record this in a document separate from this research). You can decide to withdraw your participation up to one month after this interview. Hereby we end the survey, we wish you a very pleasant day.
**Question (VI):** Xin chân thành cảm ơn sự hợp tác của bạn. Những câu trả lời ẩn danh của bạn sẽ rất quan trọng đối với nghiên cứu khoa học và việc học của tôi tại VNU & KU Leuven (Bỉ). Nếu bạn có bất kỳ câu hỏi nào, bạn luôn có thể gửi email đến: [LIÊN HỆ ĐỊA PHƯƠNG]. Nếu bạn muốn nhận kết quả nghiên cứu này, chúng tôi vui lòng yêu cầu bạn cung cấp địa chỉ email của mình (chúng tôi sẽ ghi lại địa chỉ này trong một tài liệu riêng biệt với nghiên cứu này). Bạn có thể quyết định rút khỏi sự tham gia của mình trong vòng một tháng sau cuộc phỏng vấn này. Chúng tôi xin kết thúc cuộc khảo sát này, chúc bạn một ngày thật vui vẻ.

**Type:** `note`

---


## END
*KẾT THÚC*

### `_y_l_ph_n_k_t_th_c_c_k_t_n_i_internet`

**Question (EN):** This is the end of the survey. Wrap up the conversation. Make sure you SAVE the survey later and forward it once there is an internet connection.
**Question (VI):** Đây là phần kết thúc của cuộc khảo sát. Kết thúc cuộc trò chuyện. Đảm bảo rằng bạn LƯU cuộc khảo sát sau đó và chuyển tiếp khi có kết nối internet.

**Type:** `note`

---

### `picture`

**Question (EN):** PHOTO: If the respondent agrees, take a photo of the outside of the business, preferably WITHOUT the respondent in it, unless the respondent specifically requests this.
**Question (VI):** ẢNH: Nếu người trả lời đồng ý, hãy chụp ảnh bên ngoài doanh nghiệp, tốt nhất là KHÔNG có người trả lời trong ảnh, trừ khi người trả lời yêu cầu cụ thể.

**Type:** `image`

---

### `comments`

**Question (EN):** Do you as a SURVEYOR have any final notes about this survey? Anything interesting, anything strange? If NO location could be recorded, type the address/coordinates here.
**Question (VI):** Bạn là NGƯỜI KHẢO SÁT có ghi chú cuối cùng nào về cuộc khảo sát này không? Có gì thú vị không, có gì lạ không? Nếu KHÔNG ghi được vị trí nào, hãy nhập địa chỉ/tọa độ ở đây.

**Type:** `text`

---
