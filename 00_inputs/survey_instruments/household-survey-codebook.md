# Household Survey - Long Bien 2024 - Survey Codebook

*Survey Instrument Documentation*

**Total Questions:** 147

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

**Question (EN):** IMPORTANT: Please register the GPS LOCATION for this survey before you knock.
**Question (VI):** QUAN TRỌNG: Vui lòng đăng ký VỊ TRÍ GPS cho cuộc khảo sát này trước khi bạn đến.

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
| `mai linh` | Mai Linh | Mai Linh |
| `hanh` | Hanh | Hanh |
| `duy` | Duy | Duy |
| `ha` | Ha | Ha |
| `lisamarie` | Lisa-Marie | Lisa-Marie |

**Appearance:** `quick`

---

### `GI_I_THI_U_Xin_ch_o_l_i_n_i_c_a_b_n_ch_a`

**Question (EN):** INTRODUCTION: Hello, my name is ${surveyorname} and I am a student at the University of… We conduct surveys to investigate the food system of Long Bien. We would like to ask you some questions about your household, the neighborhood and why you moved here, the food you have recently eaten and where it comes from. We expect this survey to take approximately 30 minutes of your time. You can choose not to answer one or more questions. You can of course also choose to stop the interview at any time. There are no right or wrong answers. This interview is anonymous: we will not ask for your name. We do not share your personal data and this data is mainly processed at KU Leuven in Belgium. We want to gain a better insight into the food system: who eats what type of food in Long Bien? Where is this food obtained, nearby or elsewhere? These are our questions for academic research purposes. The survey is carried out digitally. I can also provide you with an extensive information sheet on paper if you wish. Do I have your verbal informed consent?
**Question (VI):** GIỚI THIỆU: Xin chào, tôi tên là ${surveyorname} và tôi là sinh viên tại Đại học… Chúng tôi tiến hành khảo sát để tìm hiểu hệ thống thực phẩm của Long Biên. Chúng tôi muốn hỏi bạn một số câu hỏi về hộ gia đình, khu phố và lý do bạn chuyển đến đây, thực phẩm bạn đã ăn gần đây và nguồn gốc của chúng. Chúng tôi dự kiến cuộc khảo sát này sẽ mất khoảng 30 phút của bạn. Bạn có thể chọn không trả lời một hoặc nhiều câu hỏi. Tất nhiên, bạn cũng có thể chọn dừng cuộc phỏng vấn bất cứ lúc nào. Không có câu trả lời đúng hay sai. Cuộc phỏng vấn này là ẩn danh: chúng tôi sẽ không hỏi tên của bạn. Chúng tôi không chia sẻ dữ liệu cá nhân của bạn và dữ liệu này chủ yếu được xử lý tại KU Leuven ở Bỉ. Chúng tôi muốn hiểu rõ hơn về hệ thống thực phẩm: ai ăn loại thực phẩm nào ở Long Biên? Thực phẩm này được lấy ở đâu, gần đó hay ở nơi khác? Đây là những câu hỏi của chúng tôi cho mục đích nghiên cứu học thuật. Cuộc khảo sát được thực hiện dưới dạng kỹ thuật số. Tôi cũng có thể cung cấp cho bạn một tờ thông tin chi tiết trên giấy nếu bạn muốn. Tôi đã có sự đồng ý bằng lời nói của bạn chưa?

**Type:** `note`

---

### `verbalconsent`

**Question (EN):** The respondent gives consent and understands the purpose of the study. DO NOT proceed without permission.
**Question (VI):** Người trả lời đồng ý và hiểu mục đích của nghiên cứu. KHÔNG tiến hành nếu không được phép.

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `no` | KHÔNG | No |

**Appearance:** `quick`

---

### `Kh_ng_c_ph_p_D_ng_a_ra_l_do_t_ch_i`

**Question (EN):** No permission. Stop the survey immediately. Please note the reason afterwards if relevant.
**Question (VI):** Không được phép. Dừng khảo sát ngay lập tức. Vui lòng ghi chú lý do sau đó nếu người trả lời đưa ra lý do từ chối.

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
| `not_home` | Họ không có nhà. | They're not home. |
| `responsible_not_home` | Người đưa ra quyết định về thực phẩm không có ở nhà. | The person making the decisions about food is not at home. |
| `no_response` | Có lẽ họ đã về nhà nhưng không mở cửa. | They are probably home but did not open the door. |
| `undisclosed` | Không đưa ra lý do. | No reason given. |
| `uncomfortable` | Họ không thoải mái khi trả lời những câu hỏi khảo sát này. | They are not comfortable answering these survey questions. |
| `no_time` | Họ không có thời gian. | They don't have time. |

**Display Logic:** Only shown if `selected(${verbalconsent}, 'no')`

---

### `neighborhood`

**Question (EN):** Ask the respondent: what is the name of this neighborhood where you live?
**Question (VI):** Tên khu dân cư mà bạn đang ở ?

**Type:** `text`

---


## Household amount of people
*Số lượng hộ gia đình*

### `total`

**Question (EN):** How many people live in this house?
**Question (VI):** Có bao nhiêu người sống trong ngôi nhà này?

**Type:** `integer`

---

### `men`

**Question (EN):** Number of adult males:
**Question (VI):** Số lượng đàn ông trong gia đình :

**Type:** `integer`

---

### `women`

**Question (EN):** Number of adult women:
**Question (VI):** Số lượng phụ nữ trong gia đình :

**Type:** `integer`

---

### `children`

**Question (EN):** Number of children:
**Question (VI):** Số lượng trẻ em:

**Type:** `integer`

---


## Demographics
*Nhân khẩu học*

### `resp_gender`

**Question (EN):** Gender of the respondent
**Question (VI):** Giới tính của người trả lời

**Type:** `select_one gender`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `male` | Nam | Man |
| `female` | Nữ | Woman |
| `X` | X (khác) | (Non-binary, Nonconforming, Fluid, prefer not to say) |

**Appearance:** `quick`

---

### `resp_edu`

**Question (EN):** What is the highest level of education achieved (of someone living in this house)? OR currently following.
**Question (VI):** Trình độ học vấn cao nhất đạt được (của một người sống trong ngôi nhà này) là gì? HOẶC hiện đang theo học.

**Type:** `select_one education`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `0` | Không đi học | No education |
| `1` | Mẫu giáo | Kindergarten |
| `2` | Trường tiểu học | Primary school |
| `3` | Trường trung học cơ sở | Secondary school |
| `4` | Trung học phổ thông | High school |
| `5` | Giáo dục đại học/cao đẳng: Đại học hoặc Cao đẳng | Higher/Tertiary education: University or College |

**Appearance:** `quick`

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

### `workers`

**Question (EN):** Do people live in the house who work for you (e.g. housekeeper, nanny, security, drivers, gardener)? If so, how much?
**Question (VI):** Có những người sống trong nhà làm việc cho bạn không (ví dụ như người giúp việc, bảo mẫu, an ninh, tài xế, người làm vườn)? Nếu có, bao nhiêu?

**Type:** `integer`

---


## Household location
*Vị trí hộ gia đình*

### `lifelonglocation`

**Question (EN):** Have you lived in this house all your life?
**Question (VI):** Bạn đã sống ở ngôi nhà này cả đời sao?

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `no` | KHÔNG | No |

---

### `locationtime_age`

**Question (EN):** What is your age?
**Question (VI):** Bạn bao nhiêu tuổi?

**Type:** `integer`

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'yes')`

---

### `locationtime`

**Question (EN):** In what year did you move to this house?
**Question (VI):** Bạn chuyển đến ngôi nhà này vào năm nào?

**Type:** `decimal`

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

---


## Location reasons
*Lý do vị trí*

### `previouslocation`

**Question (EN):** Where did your family live before moving to this house?
**Question (VI):** Gia đình bạn sống ở đâu trước khi chuyển đến ngôi nhà này?

**Type:** `select_one previouslocation`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `NUA` | Ở một phần khác của Long Biên | In another part of Long Bien |
| `city` | Ở Hà Nội | In Hanoi |
| `country` | Ở một nơi khác trong nước, ngoài Hà Nội/Long Biên | In another part of the country, outside Hanoi/Long Bien |
| `abroad` | Trước đó chúng tôi sống ở nước ngoài | Before this we lived abroad |

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

**Appearance:** `quick`

---

### `previouslocationNUA`

**Question (EN):** Where in Long Bien did your family live before?
**Question (VI):** Trước đây gia đình bạn sống ở đâu tại Long Biên?

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

**Appearance:** `quick`

---

### `moveaway-reasons`

**Question (EN):** Think back to the last time you moved. What were the reasons your family moved AWAY/from the previous area? Why didn't you want to live there anymore?
**Question (VI):** Hãy nghĩ lại lần cuối cùng bạn chuyển đi. Lý do gia đình bạn chuyển đi/khỏi khu vực trước đó là gì? Tại sao bạn không muốn sống ở đó nữa?

**Type:** `select_multiple moveaway_reasons or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `husband` | Chuyển đi cùng với chồng/vợ/bạn đời | Moved together with husband/wife/partner |
| `family` | Chuyển đi khỏi nhà của một thành viên gia đình. | Moved away from the home of a family member. |
| `inherited` | Thừa hưởng một lô đất ở nơi khác | Inherited a plot somewhere else |
| `own` | Muốn sở hữu một lô đất hoặc ngôi nhà (lớn hơn) (có thể ở chung với một người bạn đời) | Wanted to own a (larger) plot or house (possibly with a partner) |
| `rent` | Muốn thuê một lô đất/ngôi nhà (lớn hơn) (có thể ở chung với một người bạn đời) | Wanted to rent a (larger) plot/house (possibly with a partner) |
| `services` | Dịch vụ kém hoặc quá ít ở khu vực đó (ví dụ siêu thị, cửa hàng, y tế) | Poor or too few services in that neighborhood (e.g. supermarkets, shops, medical) |
| `reputation` | Tiếng xấu của khu phố đó (không an toàn, không sạch sẽ) | Bad reputation of that neighborhood (unsafe, not clean) |
| `flooding` | Khu phố thường xuyên bị ngập lụt | Neighborhood flooded regularly |
| `workdistance` | Nó cách xa nơi làm việc và/hoặc trường học | It was far away from work and/or school |
| `familydistance` | Nó ở rất xa những người trong họ hàng | It was far away from people of the same family/ethnicity |
| `jobloss` | Mất việc, chấm dứt hợp đồng hoặc nghỉ hưu | Job loss, contract terminated or retirement |
| `newjob` | Chuyển việc, công ty mới, công việc mới hoặc học tập mới | Job transfer, new company, new job or new study |
| `allocated` | Một ngôi nhà được giao ở nơi khác (ví dụ như bởi ông chủ) | A home assigned somewhere else (for example by boss) |
| `highrent` | Tiền thuê nhà quá cao | The rents were too high |
| `justcause` | Tôi chỉ muốn thay đổi môi trường | I just wanted to change the environment |
| `refugee` | Người tị nạn từ vùng xung đột | Refugee from a conflict area |
| `forcemajor` | Phải di chuyển vì những lý do ngoài tầm kiểm soát của họ | Had to move due to reasons beyond their control |

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

---

### `movetowards-reasons`

**Question (EN):** You then came to live here. What were the reasons your family moved here TO this neighborhood specifically?
**Question (VI):** Sau đó bạn chuyển đến sống ở đây. Lý do nào khiến gia đình bạn chuyển đến đây ĐẾN khu phố này?

**Type:** `select_multiple movetowards_reasons or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `husband` | Chuyển tới cùng chồng/vợ/đối tác | Withdrawn from husband/wife/partner |
| `family` | Chuyển đến sống cùng gia đình (thành viên) | Moved in with family (member) |
| `inherited` | Tôi thừa kế mảnh đất này | I inherited this plot of land |
| `own` | Đã mua lô đất này với giá tốt và xây nhà | Bought this plot for a good price and built a house |
| `rent` | có thể cho thuê căn nhà này (có thể thuê chung với một người bạn đời) với giá tốt | can rent this house (possibly with a partner) for a good price |
| `house` | Đã mua căn nhà này (có thể là với đối tác) với giá tốt | Bought this house (possibly with partner) for a good price |
| `services` | Dịch vụ tốt hơn trong khu vực | Better services in the area |
| `reputation` | Danh tiếng tốt hơn của khu phố này | Better reputation of this neighborhood |
| `workdistance` | Gần nơi làm việc và/hoặc trường học hơn | Closer to work and/or school |
| `familydistance` | Gần gũi hơn với gia đình và/hoặc những người cùng dân tộc | Closer to family and/or people of the same ethnicity |
| `jobopportunity` | Gần nơi làm việc mới, công việc mới hoặc công ty mới | Closer to a new workplace, new job or new company |
| `allocated` | Ngôi nhà này đã được giao cho tôi/chúng tôi tại địa điểm này (ví dụ: bởi chủ lao động hoặc chính phủ) | This home has been assigned to me/us at this location (e.g. by employer or government) |

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

---


## Localization factors
*Các yếu tố bản địa hóa*

### `M_t_l_n_n_a_h_y_ngh_s_ng_t_i_a_i_m_n_y`

**Question (EN):** Once again, think back to when you moved here in ${locationtime}. How important were the following factors for you to live in this location?
**Question (VI):** Một lần nữa, hãy nghĩ lại thời điểm bạn chuyển đến đây tại ${locationtime}. Các yếu tố sau đây quan trọng như thế nào đối với bạn khi sống tại địa điểm này?

**Type:** `note`

---

### `bridge_city`

**Question (EN):** Distance to the Cau Vinh Tuy + Thanh Tri - BRIDGES
**Question (VI):** Khoảng cách đến Cầu Vĩnh Tuy + Thanh Trì

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / trung tính / khá quan trọng | Average / neutral / somewhat important |
| `1` | Rất quan trọng/ưu tiên | Very important/priority |

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

**Appearance:** `quick`

---

### `waterdistance`

**Question (EN):** Proximity to natural WATER (river, lake, pond, sea, ocean)
**Question (VI):** Khoảng cách đến nguồn nước tự nhiên (sông, hồ, ao, biển, đại dương)

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / trung tính / khá quan trọng | Average / neutral / somewhat important |
| `1` | Rất quan trọng/ưu tiên | Very important/priority |

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

**Appearance:** `quick`

---

### `safe_reputation`

**Question (EN):** When you decided to come and live here in ${locationtime}, how important was it to you: SAFETY of the neighborhood/good REPUTATION
**Question (VI):** Khi bạn quyết định đến và sống ở đây tại ${locationtime}, điều đó quan trọng như thế nào đối với bạn: AN TOÀN của khu phố/UY TÍN tốt

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / trung tính / khá quan trọng | Average / neutral / somewhat important |
| `1` | Rất quan trọng/ưu tiên | Very important/priority |

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

**Appearance:** `quick`

---

### `flooding`

**Question (EN):** The susceptibility of this location to FLOODING
**Question (VI):** Vị trí dễ bị ngập

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / trung tính / khá quan trọng | Average / neutral / somewhat important |
| `1` | Rất quan trọng/ưu tiên | Very important/priority |

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

**Appearance:** `quick`

---

### `infrastructure`

**Question (EN):** General INFRASTRUCTURE (electricity, gas, asphalted road etc.)
**Question (VI):** CƠ SỞ HẠ TẦNG chung (điện, khí đốt, đường nhựa, v.v.)

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / trung tính / khá quan trọng | Average / neutral / somewhat important |
| `1` | Rất quan trọng/ưu tiên | Very important/priority |

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

**Appearance:** `quick`

---

### `foodenvironment`

**Question (EN):** Distance to places where you can buy FOOD
**Question (VI):** Khoảng cách từ nhà đến chợ (siêu thị, nơi cung ứng thực phẩm khác):

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / trung tính / khá quan trọng | Average / neutral / somewhat important |
| `1` | Rất quan trọng/ưu tiên | Very important/priority |

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

**Appearance:** `quick`

---

### `schools`

**Question (EN):** Think back again to ${locationtime}, when you decided to move here. How important was the distance to SCHOOLS then
**Question (VI):** Hãy nghĩ lại về ${locationtime}, khi bạn quyết định chuyển đến đây. Khoảng cách đến TRƯỜNG HỌC quan trọng như thế nào vào thời điểm đó

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / trung tính / khá quan trọng | Average / neutral / somewhat important |
| `1` | Rất quan trọng/ưu tiên | Very important/priority |

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

**Appearance:** `quick`

---

### `medical`

**Question (EN):** Distance to MEDICAL CARE centers/hospital/clinics
**Question (VI):** Khoảng cách đến các trung tâm CHĂM SÓC Y TẾ

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / trung tính / khá quan trọng | Average / neutral / somewhat important |
| `1` | Rất quan trọng/ưu tiên | Very important/priority |

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

**Appearance:** `quick`

---

### `religion`

**Question (EN):** Distance to HOUSES OF PRAYER/Church/religious authorities
**Question (VI):** Khoảng cách đến nơi thờ phụng (nhà thờ, miếu, đền, chùa, đình,vv...)

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / trung tính / khá quan trọng | Average / neutral / somewhat important |
| `1` | Rất quan trọng/ưu tiên | Very important/priority |

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

**Appearance:** `quick`

---

### `leisure`

**Question (EN):** Distance to RECREATION/leisure/entertainment (sports, music, parks…)
**Question (VI):** Khoảng cách đến các khu vực GIẢI TRÍ (thể thao, âm nhạc, công viên…)

**Type:** `select_one importancescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-1` | Không quan trọng / không được tính đến | Not important / not taken into account |
| `0` | Trung bình / trung tính / khá quan trọng | Average / neutral / somewhat important |
| `1` | Rất quan trọng/ưu tiên | Very important/priority |

**Display Logic:** Only shown if `selected(${lifelonglocation}, 'no')`

**Appearance:** `quick`

---


## Neighborhood characteristics
*Đặc điểm khu phố*


## Services
*Dịch vụ*

### `HI_N_T_I_b_n_c_h_i_hu_v_c_c_a_b_n_kh_ng`

**Question (EN):** Are you CURRENTLY satisfied or dissatisfied with the NUMBER and PROXIMITY of the following services in your area?
**Question (VI):** HIỆN TẠI bạn có hài lòng hay không hài lòng về số lượng và và khoảng cách hiện tại tới các dịch vụ sau đây tại khu vực của bạn không?

**Type:** `note`

---

### `primaryschools`

**Question (EN):** Primary/elementary school
**Question (VI):** Trường tiểu học (Độ tuổi: 6-12)

**Type:** `select_multiple satisfaction`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `none` | Không có (không) | There are none (zero) |
| `neg_notenough` | Không hài lòng (dịch vụ này không đủ tốt) | Dissatisfied/unhappy (not enough of this service) |
| `neg_toomany` | Không hài lòng (quá nhiều dịch vụ này) | Dissatisfied/unhappy (too much of this service) |
| `neutral_unimportant` | Trung lập (dịch vụ này không quan trọng với tôi) | Neutral (this service is not important to me) |
| `pos_sufficient` | Hài lòng/tốt (có đủ) | Satisfied/fine/happy (there are enough) |

---

### `secondaryschools`

**Question (EN):** Secondary/middle school (age 12-15)
**Question (VI):** Trường trung học cơ sở (Độ tuổi: 12-15)

**Type:** `select_multiple satisfaction`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `none` | Không có (không) | There are none (zero) |
| `neg_notenough` | Không hài lòng (dịch vụ này không đủ tốt) | Dissatisfied/unhappy (not enough of this service) |
| `neg_toomany` | Không hài lòng (quá nhiều dịch vụ này) | Dissatisfied/unhappy (too much of this service) |
| `neutral_unimportant` | Trung lập (dịch vụ này không quan trọng với tôi) | Neutral (this service is not important to me) |
| `pos_sufficient` | Hài lòng/tốt (có đủ) | Satisfied/fine/happy (there are enough) |

---

### `highschools`

**Question (EN):** High school (age 15-18)
**Question (VI):** Trường trung học phổ thông (Độ tuổi:15-18)

**Type:** `select_multiple satisfaction`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `none` | Không có (không) | There are none (zero) |
| `neg_notenough` | Không hài lòng (dịch vụ này không đủ tốt) | Dissatisfied/unhappy (not enough of this service) |
| `neg_toomany` | Không hài lòng (quá nhiều dịch vụ này) | Dissatisfied/unhappy (too much of this service) |
| `neutral_unimportant` | Trung lập (dịch vụ này không quan trọng với tôi) | Neutral (this service is not important to me) |
| `pos_sufficient` | Hài lòng/tốt (có đủ) | Satisfied/fine/happy (there are enough) |

---

### `medicalcare`

**Question (EN):** Medical care facilities (medical centers/doctors)
**Question (VI):** Chăm sóc y tế (trung tâm)

**Type:** `select_multiple satisfaction`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `none` | Không có (không) | There are none (zero) |
| `neg_notenough` | Không hài lòng (dịch vụ này không đủ tốt) | Dissatisfied/unhappy (not enough of this service) |
| `neg_toomany` | Không hài lòng (quá nhiều dịch vụ này) | Dissatisfied/unhappy (too much of this service) |
| `neutral_unimportant` | Trung lập (dịch vụ này không quan trọng với tôi) | Neutral (this service is not important to me) |
| `pos_sufficient` | Hài lòng/tốt (có đủ) | Satisfied/fine/happy (there are enough) |

---

### `police`

**Question (EN):** Police stations
**Question (VI):** Đồn cảnh sát

**Type:** `select_multiple satisfaction`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `none` | Không có (không) | There are none (zero) |
| `neg_notenough` | Không hài lòng (dịch vụ này không đủ tốt) | Dissatisfied/unhappy (not enough of this service) |
| `neg_toomany` | Không hài lòng (quá nhiều dịch vụ này) | Dissatisfied/unhappy (too much of this service) |
| `neutral_unimportant` | Trung lập (dịch vụ này không quan trọng với tôi) | Neutral (this service is not important to me) |
| `pos_sufficient` | Hài lòng/tốt (có đủ) | Satisfied/fine/happy (there are enough) |

---

### `foodenvironment_001`

**Question (EN):** Places where you can buy food/food
**Question (VI):** Những nơi bạn có thể mua thực phẩm

**Type:** `select_multiple satisfaction`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `none` | Không có (không) | There are none (zero) |
| `neg_notenough` | Không hài lòng (dịch vụ này không đủ tốt) | Dissatisfied/unhappy (not enough of this service) |
| `neg_toomany` | Không hài lòng (quá nhiều dịch vụ này) | Dissatisfied/unhappy (too much of this service) |
| `neutral_unimportant` | Trung lập (dịch vụ này không quan trọng với tôi) | Neutral (this service is not important to me) |
| `pos_sufficient` | Hài lòng/tốt (có đủ) | Satisfied/fine/happy (there are enough) |

---

### `recreation`

**Question (EN):** Recreational activities (leisure, sports, hobbies, entertainment)
**Question (VI):** Các khu vực hoạt động giải trí (gym, hồ bơi, sân bóng, khu vui chơi )

**Type:** `select_multiple satisfaction`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `none` | Không có (không) | There are none (zero) |
| `neg_notenough` | Không hài lòng (dịch vụ này không đủ tốt) | Dissatisfied/unhappy (not enough of this service) |
| `neg_toomany` | Không hài lòng (quá nhiều dịch vụ này) | Dissatisfied/unhappy (too much of this service) |
| `neutral_unimportant` | Trung lập (dịch vụ này không quan trọng với tôi) | Neutral (this service is not important to me) |
| `pos_sufficient` | Hài lòng/tốt (có đủ) | Satisfied/fine/happy (there are enough) |

---

### `worship`

**Question (EN):** Places of worship (church, temple…)
**Question (VI):** Nơi thờ cúng

**Type:** `select_multiple satisfaction`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `none` | Không có (không) | There are none (zero) |
| `neg_notenough` | Không hài lòng (dịch vụ này không đủ tốt) | Dissatisfied/unhappy (not enough of this service) |
| `neg_toomany` | Không hài lòng (quá nhiều dịch vụ này) | Dissatisfied/unhappy (too much of this service) |
| `neutral_unimportant` | Trung lập (dịch vụ này không quan trọng với tôi) | Neutral (this service is not important to me) |
| `pos_sufficient` | Hài lòng/tốt (có đủ) | Satisfied/fine/happy (there are enough) |

---


## Neighborhood statements
*Tuyên bố khu phố*

### `B_n_ng_hay_kh_ng_h_n_i_b_n_ang_s_ng`

**Question (EN):** Do you agree or disagree (or neutral) regarding the following statements about the neighborhood in which you live?
**Question (VI):** Bạn đồng ý hay không đồng ý (hoặc trung lập) về những tuyên bố sau đây về khu phố nơi bạn đang sống?

**Type:** `note`

---

### `clean`

**Question (EN):** This neighborhood is clean.
**Question (VI):** Khu phố này sạch sẽ.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | (Rất) không đồng ý | (Strongly) disagree |
| `-1` | Không đồng ý một chút | Disagree a bit |
| `0` | Trung lập (như những nơi khác/Tôi không quan tâm/Tôi không biết/Chưa nghĩ đến điều đó) | Neutral (as elsewhere/I don't care/I don't know/haven't thought about it) |
| `1` | Đồng ý một chút | Agree a bit |
| `2` | (Hoàn toàn) đồng ý | (Completely) agree |

---

### `safe`

**Question (EN):** This neighborhood is safe.
**Question (VI):** Khu phố này an toàn.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | (Rất) không đồng ý | (Strongly) disagree |
| `-1` | Không đồng ý một chút | Disagree a bit |
| `0` | Trung lập (như những nơi khác/Tôi không quan tâm/Tôi không biết/Chưa nghĩ đến điều đó) | Neutral (as elsewhere/I don't care/I don't know/haven't thought about it) |
| `1` | Đồng ý một chút | Agree a bit |
| `2` | (Hoàn toàn) đồng ý | (Completely) agree |

---

### `floods`

**Question (EN):** This neighborhood experiences flooding when it rains.
**Question (VI):** Khu phố này thường xuyên bị ngập lụt khi trời mưa.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | (Rất) không đồng ý | (Strongly) disagree |
| `-1` | Không đồng ý một chút | Disagree a bit |
| `0` | Trung lập (như những nơi khác/Tôi không quan tâm/Tôi không biết/Chưa nghĩ đến điều đó) | Neutral (as elsewhere/I don't care/I don't know/haven't thought about it) |
| `1` | Đồng ý một chút | Agree a bit |
| `2` | (Hoàn toàn) đồng ý | (Completely) agree |

---

### `reputation`

**Question (EN):** This neighborhood has a good reputation.
**Question (VI):** Khu phố này có uy tín tốt.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | (Rất) không đồng ý | (Strongly) disagree |
| `-1` | Không đồng ý một chút | Disagree a bit |
| `0` | Trung lập (như những nơi khác/Tôi không quan tâm/Tôi không biết/Chưa nghĩ đến điều đó) | Neutral (as elsewhere/I don't care/I don't know/haven't thought about it) |
| `1` | Đồng ý một chút | Agree a bit |
| `2` | (Hoàn toàn) đồng ý | (Completely) agree |

---

### `foodenvironment_002`

**Question (EN):** It is easy to find food in this area.
**Question (VI):** Rất dễ tìm thấy đồ ăn ở khu vực này.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | (Rất) không đồng ý | (Strongly) disagree |
| `-1` | Không đồng ý một chút | Disagree a bit |
| `0` | Trung lập (như những nơi khác/Tôi không quan tâm/Tôi không biết/Chưa nghĩ đến điều đó) | Neutral (as elsewhere/I don't care/I don't know/haven't thought about it) |
| `1` | Đồng ý một chút | Agree a bit |
| `2` | (Hoàn toàn) đồng ý | (Completely) agree |

---

### `happy`

**Question (EN):** Overall I am happy/satisfied to live in this neighborhood.
**Question (VI):** Nhìn chung tôi rất vui/hài lòng khi sống ở khu phố này.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | (Rất) không đồng ý | (Strongly) disagree |
| `-1` | Không đồng ý một chút | Disagree a bit |
| `0` | Trung lập (như những nơi khác/Tôi không quan tâm/Tôi không biết/Chưa nghĩ đến điều đó) | Neutral (as elsewhere/I don't care/I don't know/haven't thought about it) |
| `1` | Đồng ý một chút | Agree a bit |
| `2` | (Hoàn toàn) đồng ý | (Completely) agree |

---


## Social food accessibility
*Social food accessibility*

### `foodsharing_activity`

**Question (EN):** Do you ever receive or give food from/to neighbors, relatives, school, church or other sources?
**Question (VI):** Bạn có bao giờ nhận hoặc tặng thực phẩm (đồ ăn, thức ăn) từ/cho hàng xóm, họ hàng, trường học, nhà thờ hoặc các nguồn khác không?

**Type:** `select_multiple receivegive`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `receive` | Có, đôi khi chúng ta nhận được thức ăn (ví dụ từ gia đình, hàng xóm, bạn bè, nhà thờ, trường học, v.v.) | Yes, we sometimes receive food (e.g. from family, neighbors, friends, church, school, etc.) |
| `give` | Có, đôi khi chúng ta tặng thức ăn (ví dụ cho gia đình, hàng xóm, bạn bè, nhà thờ, trường học, v.v.) | Yes, we sometimes give away food (e.g. to family, neighbors, friends, church, school, etc.) |
| `noexchange` | Không, chúng tôi không chia sẻ thức ăn hoặc nhận thức ăn từ bất kỳ ai | No, we do not share food or receive food from anyone |

---

### `foodsharing_details`

**Question (EN):** Can you tell us more about your food sharing activities? From whom do you receive food, or to whom do you hand out food? What kind of food, and how much?
**Question (VI):** Bạn có thể cho chúng tôi biết thêm về hoạt động chia sẻ thực phẩm của bạn không? Bạn nhận thực phẩm từ ai, hoặc bạn trao thực phẩm cho ai? Loại thực phẩm nào và bao nhiêu?

**Type:** `text`

---


## Home food production
*Sản xuất thực phẩm tại nhà*

### `farms`

**Question (EN):** Does this household produce any food or other agricultural products (whether sold or consumed)?
**Question (VI):** Hộ gia đình này có sản xuất bất kỳ loại thực phẩm hoặc sản phẩm nông nghiệp nào khác (để bán hoặc tiêu thụ) không?

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `no` | KHÔNG | No |

**Appearance:** `quick`

---

### `farmlandtype`

**Question (EN):** On what TYPE OF LAND does your household mainly carry out these gardening or agricultural activities?
**Question (VI):** Hộ gia đình bạn thực hiện các hoạt động làm vườn hoặc nông nghiệp trên loại hình đất gì ?

**Type:** `select_one farmlandtypes or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `farmland` | Đất nông nghiệp (bao gồm đất nông nghiệp thương mại và các doanh nghiệp nhỏ) | Agricultural land (including commercial agricultural land and small businesses) |
| `commonland` | Đất công/bộ lạc | Communal/tribal/family land |
| `backyard` | Sân sau/cánh đồng gắn liền với hộ gia đình | Backyard/fields attached to the household |
| `pots` | Chậu/hộp trong nhà, vườn, ban công, hiên nhà, mái nhà | Pots/boxes within home, garden, balcony, patio, roof |
| `organizationland` | Đất/vườn của trường học/nhà thờ/tổ chức khác | Land/garden of the school/church/other organization |

**Display Logic:** Only shown if `selected(${farms}, 'yes')`

**Appearance:** `quick`

---

### `farmlocation`

**Question (EN):** WHERE does this gardening/farming activity take place?
**Question (VI):** Hoạt động làm vườn/nông trại này diễn ra ở ĐÂU?

**Type:** `select_one agriculturelocations or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `home` | Sân sau/vườn rau gắn liền với ngôi nhà | Backyard/vegetable garden attached to the house |
| `street` | Trên con phố này | On this street |
| `neighbourhood` | Trong khu dân cư này | In this residential area |
| `adminunit` | Trong khu nghỉ mát này | In this resort |
| `district` | Nơi khác ở quận Long Biên | Elsewhere in the Long Bien district |
| `city` | Ở trung tâm thành phố (Hà Nội) | In the city center (Hanoi) |
| `country` | Nơi khác ở Việt Nam | Elsewhere in Vietnam |
| `abroad` | Ở nước ngoài | Abroad |

**Display Logic:** Only shown if `selected(${farms}, 'yes')`

**Appearance:** `quick`

---

### `farmpurpose`

**Question (EN):** What is the most important REASON for doing horticulture/agriculture?
**Question (VI):** Lý do quan trọng nhất để làm vườn/nông nghiệp của bạn là gì ?

**Type:** `select_one agriculturepurpose or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `mainsource_food` | Là nguồn thực phẩm chính | As the main food source |
| `mainsource_income` | Nguồn thu nhập chính/nghề nghiệp chính hoặc công việc chính | Main source of income/main occupation or main job |
| `extrasource_food` | Là nguồn thực phẩm bổ sung | As an additional food source |
| `extrasource_income` | Là nguồn thu nhập bổ sung/nghề phụ/công việc phụ | As an additional source of income/secondary profession/side job |
| `leisure_hobby` | Là một sở thích, thời gian rảnh rỗi, giải trí, kết nối với thiên nhiên | As a hobby, free time, recreation, connection with nature |
| `habit_tradition` | Truyền thống/thói quen gia đình | Family tradition/habit |
| `foodsafety` | Tôi muốn tự trồng thực phẩm an toàn/không có thuốc trừ sâu/hữu cơ/hữu cơ | I want to grow my own food that is safe/pesticide-free/organic/organic |

**Display Logic:** Only shown if `selected(${farms}, 'yes')`

**Appearance:** `quick`

---

### `consumptionpercentage`

**Question (EN):** Can you estimate the PERCENTAGE (%) of your family's food intake that comes from your own garden/farmland?
**Question (VI):** Bạn có thể ước tính TỶ LỆ bao nhiêu (%) lượng thực phẩm mà gia đình bạn tiêu thụ có nguồn gốc từ vườn/đất nông trại do nhà bạn trồng không?

**Type:** `integer`

**Display Logic:** Only shown if `selected(${farms}, 'yes')`

---

### `farmsize`

**Question (EN):** Can you provide an estimated SIZE of the garden/agricultural land you are cultivating in m²?
**Question (VI):** Bạn có thể cung cấp diện tích ước tính của khu vườn/đất nông nghiệp mà bạn đang canh tác theo m² không? (PLOT = X m²)

**Type:** `integer`

**Display Logic:** Only shown if `selected(${farms}, 'yes')`

---

### `accessuncertainty`

**Question (EN):** Are you CONCERNED that you may lose access to this garden/farmland?
**Question (VI):** Bạn có LO LẮNG rằng bạn có thể mất đất trong tương lai không ?

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `no` | KHÔNG | No |

**Display Logic:** Only shown if `selected(${farms}, 'yes')`

**Appearance:** `quick`

---

### `accessuncertaintyreason`

**Question (EN):** If yes, why?
**Question (VI):** Nếu có, tại sao?

**Type:** `select_multiple accessuncertainty`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `urbangrowth_rent` | Đô thị hóa/thiếu đất, nhu cầu quá cao để tiếp tục sử dụng đất (tiền thuê đất trở nên quá đắt) | Urbanization/land shortage, demand is too high to continue using the land (renting becomes too expensive) |
| `urbangrowth_sell` | Đô thị hóa/thiếu đất, nhu cầu quá lớn khiến người được phỏng vấn đang cân nhắc bán đất | Urbanization/land shortage, demand is so great that the interviewee is considering selling the land |
| `landlord` | Người được phỏng vấn thuê đất, chủ nhà có thể tự quyết định sử dụng (không còn cho thuê nữa) | Interviewee rents the land, landlord can decide to use it himself (no longer rent it out) |
| `squatter` | Người được phỏng vấn không phải là chủ sở hữu (hợp pháp) của đất, vì vậy đất có thể được thu hồi | The interviewee is not the (legal) owner of the land, so the land can be reclaimed |
| `landgrab_squatters` | Cướp đất của những người chiếm đất | Land theft by squatters |
| `evictions_govt` | Lý do liên quan đến chính phủ (trục xuất, v.v.) | Government-related reasons (evictions, etc.) |
| `landgrab_companies` | Các tập đoàn thâu tóm đất đai | Land grabbing by corporations |
| `policy` | Các nhà quy hoạch đô thị/nhà hoạch định chính sách có thể cấm nông nghiệp ở địa điểm đó | Urban planners/policymakers could ban agriculture in that location |
| `familyissues` | Đất đai gia đình, tranh chấp với họ hàng | Family land, disputes with relatives |
| `flooding` | Lũ lụt thường xuyên có thể làm cho đất không đủ dinh dưỡng | Frequent flooding might make the soil inadequate |

**Display Logic:** Only shown if `${accessuncertainty} = 'yes' and selected(${farms}, 'yes')`

---


## Home food production persons involved
*Người sản xuất thực phẩm tại nhà tham gia*

### `B_n_s_ng_y_v_i_t_ho_t_ng_n_ng_nghi_p`

**Question (EN):** You live here with ${total} people. Which family member(s) is/are engaged in the agricultural activities?
**Question (VI):** Bạn sống ở đây với ${total} người. Những thành viên nào trong gia đình đang tham gia vào các hoạt động nông nghiệp?

**Type:** `note`

**Display Logic:** Only shown if `selected(${farms}, 'yes')`

---

### `farmersmen`

**Question (EN):** Number of adult males:
**Question (VI):** Số lượng đàn ông trong gia đình:

**Type:** `integer`

**Display Logic:** Only shown if `selected(${farms}, 'yes')`

---

### `farmingwomen`

**Question (EN):** Number of adult women:
**Question (VI):** Số lượng phụ nữ trong gia đình:

**Type:** `integer`

**Display Logic:** Only shown if `selected(${farms}, 'yes')`

---

### `farmingchildren`

**Question (EN):** Number of children:
**Question (VI):** Số lượng trẻ em:

**Type:** `integer`

**Display Logic:** Only shown if `selected(${farms}, 'yes')`

---

### `farmingstaff`

**Question (EN):** Number of employees/staff/helpers:
**Question (VI):** Số lượng người làm thuê/ người hỗ trợ nông nghiệp:

**Type:** `integer`

**Display Logic:** Only shown if `selected(${farms}, 'yes')`

---


## Home food vending
*Bán đồ ăn tại nhà*

### `hh_vendor`

**Question (EN):** Do you sell food at this location (e.g. a stall in the front garden, or house with business attached)?
**Question (VI):** Bạn có bán thực phẩm ngay tại vị trí này không (ví dụ như quầy hàng ở sân trước hoặc nhà có cửa hàng kinh doanh)?

**Type:** `select_multiple vendingoptions`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | Có, tôi (thỉnh thoảng) bán đồ ăn ở địa điểm này | Yes, I (sometimes) sell food at this location |
| `no` | Không, tôi không bán đồ ăn | No, I don't sell food |
| `supplier` | Tôi là nhà cung cấp: Tôi bán thực phẩm cho người bán lại | I am a supplier: I sell food to someone who resells it |

**Appearance:** `quick`

---

### `vendortype`

**Question (EN):** What type of food vendor?
**Question (VI):** Loại hình kinh doanh đồ ăn của bạn là gì ?

**Type:** `select_one vendortype`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `streetvendor` | Quầy hàng rong (người bán hàng rong) bán thực phẩm tươi sống (ví dụ như rau/trái cây/thịt) trong vườn (phía trước) hoặc ở phía đường của ngôi nhà | Stall (street vendor) with fresh food (e.g. vegetables/fruit/meat) in the (front) garden or on the street side of the house |
| `retailer` | Nhà bán lẻ (tiệm bánh, cửa hàng thịt, cửa hàng đặc sản, v.v.) trong hoặc gần/bên cạnh nhà | Retailer (bakery, butcher's shop, specialty store, etc.) in or close to/next to the home |
| `restaurant` | Nhà hàng (ăn tại chỗ) trong hoặc gần/bên cạnh ngôi nhà | Restaurant (dine-in) in or close to/next to the house |
| `foodtruck` | Xe bán đồ ăn lưu động / người bán đồ ăn mang về bán các bữa ăn đã chế biến hoặc đồ ăn nhẹ trong vườn hoặc bên lề đường của ngôi nhà | Food truck / takeaway street vendor who sells prepared meals or snacks in the garden or on the street side of the house |
| `supermarket` | Siêu thị trong hoặc gần/bên cạnh nhà | Supermarket in or close to/next to the house |
| `wholesaler` | Người bán buôn trong hoặc gần/bên cạnh ngôi nhà | Wholesaler in or close to/next to the house |

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

**Appearance:** `quick`

---

### `reason`

**Question (EN):** What was the main reason you started selling food here at this location?
**Question (VI):** Lý do chính khiến bạn bắt đầu bán thực phẩm ở địa điểm này là gì?

**Type:** `select_one homevendingpurpose or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `mainsource_income` | Nguồn thu nhập chính/nghề nghiệp chính hoặc công việc chính | Main source of income/main occupation or main job |
| `extrasource_income` | Là nguồn thu nhập bổ sung/nghề phụ/công việc phụ | As an additional source of income/secondary profession/side job |
| `habit_tradition` | Truyền thống/thói quen gia đình | Family tradition/habit |
| `socialcontact` | Để (nhiều hơn) giao tiếp xã hội với cư dân địa phương và những người khác | For (more) social contact with local residents and others |

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

---

### `foodgroups`

**Question (EN):** What foods do you sell at this location?
**Question (VI):** Bạn bán những loại thực phẩm nào ở địa điểm này?

**Type:** `select_multiple foodgroups`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `cereals` | LƯƠNG THỰC (ngô, gạo, lúa mì, bánh mì, mì, cháo, mì ống, v.v.) | CEREALS (corn, rice, wheat, bread, noodles, porridge, pasta, etc…) |
| `whiterootsandtubers` | RỄ VÀ CỦ TRẮNG (khoai tây, khoai lang, khoai môn, sắn trắng,… hoặc các loại rễ khác) | WHITE ROOTS AND TUBERS (potatoes, white sweet potato, white cassava, quack, Chinese tayer ... or other roots) |
| `veg_vitamina` | RAU CỦ CÓ VITAMIN A (bí ngô, cà rốt, ớt chuông (bất kỳ loại nào có màu cam bên trong)) | VEGETABLES AND TUBERS WITH VITAMIN A (pumpkin, carrot, orange sweet potato, pepper (anything that is orange on the inside)) |
| `veg_darkgreenleafy` | RAU LÁ XANH ĐẬM (lá cải, lá sắn, rau mồng tơi, rau ngót, bắp cải,...) | DARK GREEN LEAFY VEGETABLES (clary, cassava leaves, spinach, amchoi, bok choy, cabbage, bitawiri all leaves…) |
| `veg_other` | CÁC LOẠI RAU KHÁC (cà chua, hành tây, hành lá, cà tím, đậu bắp,...) | OTHER VEGETABLES (tomato, onion, eggplant/boulanger, poe, sopropo, antroea, soekwa, ocher, broccoli…) |
| `fruits_vitamina` | TRÁI CÂY CÓ VITAMIN A (xoài, dưa, đu đủ, dưa hấu, chanh dây, bưởi,... hoặc 100% nước ép của chúng) | FRUIT WITH VITAMIN A (mango, melon, papaya, watermelon, passion fruit/makoesa, grapefruit, sapotille or 100% juices thereof) |
| `fruits_other` | TRÁI CÂY KHÁC (chuối, cam, acai, quả mọng, anh đào, thanh long, vải, chôm chôm, táo, lựu, chanh,... hoặc 100% nước ép của những loại này) | OTHER FRUIT (banana/baking oven, orange, acai, berries, cherries, dragon fruit, lychee/rambutang, apple, pomerak, lime ... or 100% juices thereof) |
| `meat_organ` | THỊT NỘI TẾ (gan, thận, tim hoặc các loại thịt nội tạng khác) | ORGAN MEAT (liver, kidney, heart or other organ meat or blood-based food) |
| `meat_flesh` | CÁC LOẠI THỊT KHÁC (thịt bò, thịt lợn, thịt cừu, thịt dê, thịt thỏ, thịt thú rừng, thịt gà, côn trùng...) | OTHER MEAT (beef, pork, lamb, goat, rabbit, game, chicken, insects...) |
| `eggs` | TRỨNG (gà, vịt hoặc loại khác) | EGGS (chicken, duck or other) |
| `fish_seafood` | CÁ VÀ HẢI SẢN (cá hoặc động vật có vỏ (tươi hoặc khô)) | FISH AND SEAFOOD (fresh or dried fish or shellfish) |
| `legumes_nuts_seeds` | CÁC LOẠI ĐẬU, HẠT VÀ HẠT GIỐNG (đậu đen, đậu đỏ, đậu xanh, đỗ, đậu Hà Lan, đậu lăng, sim, các loại hạt, hạt dẻ, hạnh nhân, đậu phộng hoặc thực phẩm làm từ những loại này) | LEGUMES, NUTS AND SEEDS (beans, long beans, peas, lentils, sim, nuts, seeds, peanuts or food made from these) |
| `milk` | SỮA VÀ CÁC SẢN PHẨM TỪ SỮA (sữa, pho mát, sữa chua hoặc các loại khác) | MILK AND MILK PRODUCTS (milk, cheese, yogurt or others) |
| `oils_fats` | DẦU VÀ CHẤT BÉO (dầu, chất béo hoặc bơ được thêm vào thực phẩm hoặc dùng để nấu ăn) | OILS AND FATS (oil, fats or butter added to food or used for cooking) |
| `sweets` | ĐỒ NGỌT (đường, mật ong, nước ngọt có đường hoặc nước ép trái cây có đường, thực phẩm có đường như sô cô la, kẹo, bánh quy và bánh ngọt) | SWEETS (sugar, honey, sweetened soft drinks or sweetened fruit juices, sugary foods such as chocolate, sweets, cookies and cakes) |
| `spices_cond_bev` | THẢO MỘC, SỐT, ĐỒ UỐNG (gia vị, hạt tiêu, muối, nước tương, nước sốt cay, cà phê, trà, đồ uống có cồn) | SPICES, CONDIMENTS, BEVERAGES (spices, pepper, salt, soy sauce, hot sauce, coffee, tea, alcoholic drinks) |

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

---

### `wholeorprocessed`

**Question (EN):** Is it mainly UNPROCESSED food (eg whole vegetables, fruit, meat, etc.) or mainly prepared/PROCESSED food (meals, snacks, sauces, etc.)?
**Question (VI):** Thực phẩm chủ yếu là thực phẩm KHÔNG CHẾ BIẾN (ví dụ như rau củ, trái cây, thịt, v.v.) hay chủ yếu là thực phẩm đã chế biến/CHẾ BIẾN (bữa ăn, đồ ăn nhẹ, nước sốt, v.v.)?

**Type:** `select_one whole_processed`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `whole` | Đặc biệt là thực phẩm chưa qua chế biến/"nguyên chất" | Especially unprocessed/"whole" foods |
| `processed` | Đặc biệt là thực phẩm chế biến sẵn (món ăn kèm, đồ ăn nhẹ, nước sốt…) | Especially processed/prepared food (meals, side dishes, snacks, sauces…) |

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

---


## Home food vending persons involved
*Người bán hàng rong thực phẩm tại nhà*

### `B_n_s_ng_y_v_i_t_o_ho_t_ng_b_n_h_ng`

**Question (EN):** You live here with ${total} people. Which family member(s) is/are involved in the sales activities?
**Question (VI):** Bạn sống ở đây với ${total} người. Những thành viên gia đình nào tham gia vào hoạt động bán hàng?

**Type:** `note`

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

---

### `farmersmen_001`

**Question (EN):** Number of adult males:
**Question (VI):** Số lượng đàn ông trong gia đình:

**Type:** `integer`

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

---

### `farmingwomen_001`

**Question (EN):** Number of adult women:
**Question (VI):** Số lượng phụ nữ trong gia đình:

**Type:** `integer`

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

---

### `farmingchildren_001`

**Question (EN):** Number of children:
**Question (VI):** Số lượng trẻ em:

**Type:** `integer`

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

---

### `farmingstaff_001`

**Question (EN):** Number of employees/staff/farm aid:
**Question (VI):** Số lượng người làm thuê/ người hỗ trợ nông nghiệp:

**Type:** `integer`

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

---


## Statements_vendor
*Nhà cung cấp báo cáo*

### `B_n_ng_hay_kh_ng_n_th_c_ph_m_c_a_b_n`

**Question (EN):** Do you agree or disagree (or are you neutral) regarding the following statements about your food sales activities?
**Question (VI):** Bạn đồng ý hay không đồng ý (hoặc trung lập) về những tuyên bố sau đây về hoạt động bán thực phẩm của bạn?

**Type:** `note`

---

### `customers_wealth`

**Question (EN):** The customers who buy food from me are almost all wealthy/rich.
**Question (VI):** Những khách hàng mua đồ ăn của tôi hầu hết đều là người giàu có.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | (Rất) không đồng ý | (Strongly) disagree |
| `-1` | Không đồng ý một chút | Disagree a bit |
| `0` | Trung lập (như những nơi khác/Tôi không quan tâm/Tôi không biết/Chưa nghĩ đến điều đó) | Neutral (as elsewhere/I don't care/I don't know/haven't thought about it) |
| `1` | Đồng ý một chút | Agree a bit |
| `2` | (Hoàn toàn) đồng ý | (Completely) agree |

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

**Appearance:** `quick`

---

### `customers_ethn`

**Question (EN):** The customers who buy food from me almost all come from one particular/specific ethnic group.
**Question (VI):** Hầu hết những khách hàng mua thực phẩm của tôi đều đến từ một nhóm dân tộc cụ thể nào đó.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | (Rất) không đồng ý | (Strongly) disagree |
| `-1` | Không đồng ý một chút | Disagree a bit |
| `0` | Trung lập (như những nơi khác/Tôi không quan tâm/Tôi không biết/Chưa nghĩ đến điều đó) | Neutral (as elsewhere/I don't care/I don't know/haven't thought about it) |
| `1` | Đồng ý một chút | Agree a bit |
| `2` | (Hoàn toàn) đồng ý | (Completely) agree |

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

**Appearance:** `quick`

---

### `rathersomewhereelse`

**Question (EN):** I would rather sell food elsewhere (somewhere else), but here (home) is the only location I can afford.
**Question (VI):** Tôi muốn bán đồ ăn ở nơi khác (nơi khác), nhưng đây (nhà) là nơi duy nhất tôi có đủ khả năng chi trả.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | (Rất) không đồng ý | (Strongly) disagree |
| `-1` | Không đồng ý một chút | Disagree a bit |
| `0` | Trung lập (như những nơi khác/Tôi không quan tâm/Tôi không biết/Chưa nghĩ đến điều đó) | Neutral (as elsewhere/I don't care/I don't know/haven't thought about it) |
| `1` | Đồng ý một chút | Agree a bit |
| `2` | (Hoàn toàn) đồng ý | (Completely) agree |

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

**Appearance:** `quick`

---

### `changesector_5yr`

**Question (EN):** I plan to stop selling food in the next five years.
**Question (VI):** Tôi dự định sẽ ngừng bán thực phẩm trong vòng năm năm tới.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | (Rất) không đồng ý | (Strongly) disagree |
| `-1` | Không đồng ý một chút | Disagree a bit |
| `0` | Trung lập (như những nơi khác/Tôi không quan tâm/Tôi không biết/Chưa nghĩ đến điều đó) | Neutral (as elsewhere/I don't care/I don't know/haven't thought about it) |
| `1` | Đồng ý một chút | Agree a bit |
| `2` | (Hoàn toàn) đồng ý | (Completely) agree |

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

**Appearance:** `quick`

---

### `changelocation_5yr`

**Question (EN):** I plan to continue selling food for the next five years, but no longer from home.
**Question (VI):** Tôi dự định sẽ tiếp tục bán thực phẩm trong năm năm tới, nhưng không bán ở nhà nữa.

**Type:** `select_one agreescale`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `-2` | (Rất) không đồng ý | (Strongly) disagree |
| `-1` | Không đồng ý một chút | Disagree a bit |
| `0` | Trung lập (như những nơi khác/Tôi không quan tâm/Tôi không biết/Chưa nghĩ đến điều đó) | Neutral (as elsewhere/I don't care/I don't know/haven't thought about it) |
| `1` | Đồng ý một chút | Agree a bit |
| `2` | (Hoàn toàn) đồng ý | (Completely) agree |

**Display Logic:** Only shown if `selected(${hh_vendor}, 'yes')`

**Appearance:** `quick`

---


## Dwelling information
*Thông tin nhà ở*

### `housingtype`

**Question (EN):** In which type of housing does the interviewee live?
**Question (VI):** Người được phỏng vấn sống ở loại nhà ở nào?

**Type:** `select_one housingtype or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `singlefamily` | Nhà biệt lập | Detached house |
| `semidetached` | Nhà liền kề (nhà liền kề) | Semi-detached house (semi-detached house) |
| `withcorp` | Nhà có kinh doanh | House with business |
| `apartment` | Căn hộ | Apartment |
| `oneroom` | Nhà một phòng | One-room house |
| `shed` | Nhà ở tạm | Barracks, huts, etc. |
| `multiplefamilyhome` | Nhà tập thể | Part of a multi-family home |

**Appearance:** `quick`

---

### `roadtype`

**Question (EN):** What type of road/street is directly outside the house?
**Question (VI):** Loại đường/phố nào nằm ngay bên ngoài ngôi nhà?

**Type:** `select_one roadtype`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `tarmacked` | Nhựa đường | Asphalted/tarmacked |
| `nontarmacked` | Đường cát/đất/bụi bẩn | Sand/soil/dirt road |

**Appearance:** `quick`

---

### `cookingsource`

**Question (EN):** What is the main source of energy for COOKING in this household?
**Question (VI):** Nhà bạn sử dụng loại bếp gì để nấu ăn ?

**Type:** `select_one cookingsource`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `electricity` | Điện | Electricity |
| `gas` | Ga | Gas |
| `biogas` | Ga sinh học | Biogas |
| `solar` | Năng lượng mặt trời | Solar energy |
| `charcoal` | Than | Charcoal |
| `firewood` | Gỗ | Wood |
| `paraffin` | Parafin | Paraffin |

**Appearance:** `quick`

---

### `watersource`

**Question (EN):** Does your household have a tap or water source indoors/in the home?
**Question (VI):** Nhà bạn có vòi nước hoặc nguồn nước trong nhà/trong nhà không?

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `no` | KHÔNG | No |

**Appearance:** `quick`

---

### `waterdistance_001`

**Question (EN):** What is the distance from the door to the main water source used (estimated in meters)?
**Question (VI):** Khoảng cách từ cửa đến nguồn nước chính được sử dụng là bao nhiêu (ước tính bằng mét)?

**Type:** `integer`

**Display Logic:** Only shown if `selected(${watersource}, 'no')`

---

### `utilities`

**Question (EN):** Does your household have access to the following items in working condition?
**Question (VI):** Gia đình bạn có thể tiếp cận những vật dụng sau đây trong tình trạng hoạt động bình thường không?

**Type:** `select_multiple utilities`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `internet` | Internet (cáp/wifi lắp đặt trong nhà) | Internet (cable/wifi installed in the house) |
| `smartphone` | Điện thoại thông minh hoặc máy tính bảng có kết nối internet | Smartphone or tablet with internet access |
| `TV` | Tivi | Television |
| `ac` | Điều hòa không khí | Air conditioning |
| `pc` | Máy tính (PC/laptop/desktop) | Computer (PC/laptop/desktop) |

---


## Food diversity
*Sự đa dạng của thực phẩm*

### `foodgroups_001`

**Question (EN):** Please describe the food (meals and snacks) you ate or drank yesterday during the day and evening, both at home and away from home. Start with the first food or drink of the morning.
**Question (VI):** Vui lòng mô tả các loại thực phẩm (bữa ăn và đồ ăn nhẹ) bạn đã ăn hoặc uống vào ngày hôm qua trong ngày và buổi tối, cả ở nhà và ở ngoài. Bắt đầu với thức ăn hoặc đồ uống đầu tiên vào buổi sáng.

**Type:** `select_multiple foodgroups`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `cereals` | LƯƠNG THỰC (ngô, gạo, lúa mì, bánh mì, mì, cháo, mì ống, v.v.) | CEREALS (corn, rice, wheat, bread, noodles, porridge, pasta, etc…) |
| `whiterootsandtubers` | RỄ VÀ CỦ TRẮNG (khoai tây, khoai lang, khoai môn, sắn trắng,… hoặc các loại rễ khác) | WHITE ROOTS AND TUBERS (potatoes, white sweet potato, white cassava, quack, Chinese tayer ... or other roots) |
| `veg_vitamina` | RAU CỦ CÓ VITAMIN A (bí ngô, cà rốt, ớt chuông (bất kỳ loại nào có màu cam bên trong)) | VEGETABLES AND TUBERS WITH VITAMIN A (pumpkin, carrot, orange sweet potato, pepper (anything that is orange on the inside)) |
| `veg_darkgreenleafy` | RAU LÁ XANH ĐẬM (lá cải, lá sắn, rau mồng tơi, rau ngót, bắp cải,...) | DARK GREEN LEAFY VEGETABLES (clary, cassava leaves, spinach, amchoi, bok choy, cabbage, bitawiri all leaves…) |
| `veg_other` | CÁC LOẠI RAU KHÁC (cà chua, hành tây, hành lá, cà tím, đậu bắp,...) | OTHER VEGETABLES (tomato, onion, eggplant/boulanger, poe, sopropo, antroea, soekwa, ocher, broccoli…) |
| `fruits_vitamina` | TRÁI CÂY CÓ VITAMIN A (xoài, dưa, đu đủ, dưa hấu, chanh dây, bưởi,... hoặc 100% nước ép của chúng) | FRUIT WITH VITAMIN A (mango, melon, papaya, watermelon, passion fruit/makoesa, grapefruit, sapotille or 100% juices thereof) |
| `fruits_other` | TRÁI CÂY KHÁC (chuối, cam, acai, quả mọng, anh đào, thanh long, vải, chôm chôm, táo, lựu, chanh,... hoặc 100% nước ép của những loại này) | OTHER FRUIT (banana/baking oven, orange, acai, berries, cherries, dragon fruit, lychee/rambutang, apple, pomerak, lime ... or 100% juices thereof) |
| `meat_organ` | THỊT NỘI TẾ (gan, thận, tim hoặc các loại thịt nội tạng khác) | ORGAN MEAT (liver, kidney, heart or other organ meat or blood-based food) |
| `meat_flesh` | CÁC LOẠI THỊT KHÁC (thịt bò, thịt lợn, thịt cừu, thịt dê, thịt thỏ, thịt thú rừng, thịt gà, côn trùng...) | OTHER MEAT (beef, pork, lamb, goat, rabbit, game, chicken, insects...) |
| `eggs` | TRỨNG (gà, vịt hoặc loại khác) | EGGS (chicken, duck or other) |
| `fish_seafood` | CÁ VÀ HẢI SẢN (cá hoặc động vật có vỏ (tươi hoặc khô)) | FISH AND SEAFOOD (fresh or dried fish or shellfish) |
| `legumes_nuts_seeds` | CÁC LOẠI ĐẬU, HẠT VÀ HẠT GIỐNG (đậu đen, đậu đỏ, đậu xanh, đỗ, đậu Hà Lan, đậu lăng, sim, các loại hạt, hạt dẻ, hạnh nhân, đậu phộng hoặc thực phẩm làm từ những loại này) | LEGUMES, NUTS AND SEEDS (beans, long beans, peas, lentils, sim, nuts, seeds, peanuts or food made from these) |
| `milk` | SỮA VÀ CÁC SẢN PHẨM TỪ SỮA (sữa, pho mát, sữa chua hoặc các loại khác) | MILK AND MILK PRODUCTS (milk, cheese, yogurt or others) |
| `oils_fats` | DẦU VÀ CHẤT BÉO (dầu, chất béo hoặc bơ được thêm vào thực phẩm hoặc dùng để nấu ăn) | OILS AND FATS (oil, fats or butter added to food or used for cooking) |
| `sweets` | ĐỒ NGỌT (đường, mật ong, nước ngọt có đường hoặc nước ép trái cây có đường, thực phẩm có đường như sô cô la, kẹo, bánh quy và bánh ngọt) | SWEETS (sugar, honey, sweetened soft drinks or sweetened fruit juices, sugary foods such as chocolate, sweets, cookies and cakes) |
| `spices_cond_bev` | THẢO MỘC, SỐT, ĐỒ UỐNG (gia vị, hạt tiêu, muối, nước tương, nước sốt cay, cà phê, trà, đồ uống có cồn) | SPICES, CONDIMENTS, BEVERAGES (spices, pepper, salt, soy sauce, hot sauce, coffee, tea, alcoholic drinks) |

---


## Food environment
*Môi trường thực phẩm*


## (Local/neighborhood/small-to-medium) Supermarket:
*(Siêu thị địa phương/khu phố/vừa và nhỏ):*

### `supermarket_freq`

**Question (EN):** How often do you (your family) go to a local/small/neighborhood SUPERMARKET to access food?
**Question (VI):** Bạn (gia đình bạn) thường xuyên đến cửa hàng tiện lợi/bách hóa ở địa phương/khu phố để mua thực phẩm như thế nào?

**Type:** `select_one foodenvfrequency`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `40` | Nhiều lần trong ngày | Several times a day |
| `30` | 1 lần mỗi ngày | 1x daily |
| `8` | Nhiều lần một tuần | Several times a week |
| `4` | 1 lần/tuần | 1x per week |
| `2` | 2-3 lần/tháng | 2-3x per month |
| `1` | 1 lần hàng tháng | 1x monthly |
| `0` | Hiếm khi/không bao giờ | Rarely/never |

---

### `location_002`

**Question (EN):** Where is the main SUPERMARKET that you visit regularly?
**Question (VI):** SIÊU THỊ chính mà bạn thường xuyên ghé thăm là ở đâu?

**Type:** `select_one foodenvlocation`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `street` | Trên con phố này | On this street |
| `neighbourhood` | Trong khu dân cư này | In this neighbourhood/residential area |
| `adminunit` | Trong khu nghỉ mát này | In this commune |
| `district` | Nơi khác ở quận Long Biên | Elsewhere in the Long Bien district |
| `city` | Ở trung tâm thành phố (Hà Nội) | In the city center (Hanoi) |
| `country` | Nơi khác ở Việt Nam | Elsewhere in Vietnam |
| `abroad` | Ở nước ngoài | Abroad |

**Display Logic:** Only shown if `not(selected(${supermarket_freq}, '0'))`

---

### `reason_001`

**Question (EN):** What is the main reason you buy/gather food at this particular SUPERMARKET?
**Question (VI):** Lí do bạn thường đến cửa hàng tiện lợi/bách hóa này để mua thực phẩm ?

**Type:** `select_one foodenvreason or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `trust` | Tôi biết rõ nhà cung cấp/nguồn này (tin tưởng) | I know this supplier/source personally (trust) |
| `cheap` | Giá rẻ | They are the cheapest |
| `close` | Khoảng cách gần | It's close |
| `healthy` | Họ có những lựa chọn lành mạnh | They have healthy options |
| `quality` | Họ có sản phẩm chất lượng tốt | They have good quality products |
| `assortment` | Họ cung cấp một phạm vi lớn và/hoặc độc đáo | They offer a large and/or unique assortment, variety |

**Display Logic:** Only shown if `not(selected(${supermarket_freq}, '0'))`

---

### `transportation`

**Question (EN):** What means of transport do you usually use to go to this SUPERMARKET?
**Question (VI):** Bạn thường sử dụng phương tiện giao thông nào để đến SIÊU THỊ này?

**Type:** `select_one transport_type`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `home` | Là nhà | Is home |
| `walking` | Đi bộ | On foot |
| `bycicle` | Bằng xe đạp | By bicycle |
| `motorcycle` | Với xe tay ga hoặc xe máy | With a scooter or motorbike |
| `publictransport` | Xe buýt/phương tiện công cộng | Bus/public transport |
| `Taxi` | Taxi/xe công nghệ | Taxi/uber |
| `elevator` | Tôi đang đi nhờ xe của ai đó/ai đó đưa tôi đi | I'm hitching a ride with someone/someone brings me |
| `car_van` | Xe hơi hoặc xe tải nhỏ riêng | Own car or minivan |
| `companyvehicle` | Xe công ty | Company car |

**Display Logic:** Only shown if `not(selected(${supermarket_freq}, '0'))`

---

### `time`

**Question (EN):** Approximately how long does it take you to get to this SUPERMARKET, in minutes? (travel time)
**Question (VI):** Bạn mất khoảng bao lâu để đến được SIÊU THỊ này (tính theo phút)? (thời gian di chuyển)

**Type:** `integer`

**Display Logic:** Only shown if `not(selected(${supermarket_freq}, '0'))`

---


## (Large/chain) Supermarket:
*Siêu thị (lớn/chuỗi):*

### `largesupermarket_freq`

**Question (EN):** How often do you (your family) go to a large/chain SUPERMARKET to access food?
**Question (VI):** Tần suất Bạn (gia đình bạn) đến các SIÊU THỊ lớn/chuỗi siêu thị để mua thực phẩm ?

**Type:** `select_one foodenvfrequency`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `40` | Nhiều lần trong ngày | Several times a day |
| `30` | 1 lần mỗi ngày | 1x daily |
| `8` | Nhiều lần một tuần | Several times a week |
| `4` | 1 lần/tuần | 1x per week |
| `2` | 2-3 lần/tháng | 2-3x per month |
| `1` | 1 lần hàng tháng | 1x monthly |
| `0` | Hiếm khi/không bao giờ | Rarely/never |

---

### `location_003`

**Question (EN):** Where is the most important large/chain SUPERMARKET that you visit regularly?
**Question (VI):** Siêu thị lớn/chuỗi siêu thị quan trọng nhất mà bạn thường xuyên ghé thăm ở đâu?

**Type:** `select_one foodenvlocation`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `street` | Trên con phố này | On this street |
| `neighbourhood` | Trong khu dân cư này | In this neighbourhood/residential area |
| `adminunit` | Trong khu nghỉ mát này | In this commune |
| `district` | Nơi khác ở quận Long Biên | Elsewhere in the Long Bien district |
| `city` | Ở trung tâm thành phố (Hà Nội) | In the city center (Hanoi) |
| `country` | Nơi khác ở Việt Nam | Elsewhere in Vietnam |
| `abroad` | Ở nước ngoài | Abroad |

**Display Logic:** Only shown if `not(selected(${largesupermarket_freq}, '0'))`

---

### `reason_002`

**Question (EN):** What is the main reason you buy/gather food at this specific large/chain SUPERMARKET?
**Question (VI):** Lý do chính khiến bạn mua/thu thập thực phẩm tại SIÊU THỊ lớn/chuỗi siêu thị này là gì?

**Type:** `select_one foodenvreason or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `trust` | Tôi biết rõ nhà cung cấp/nguồn này (tin tưởng) | I know this supplier/source personally (trust) |
| `cheap` | Giá rẻ | They are the cheapest |
| `close` | Khoảng cách gần | It's close |
| `healthy` | Họ có những lựa chọn lành mạnh | They have healthy options |
| `quality` | Họ có sản phẩm chất lượng tốt | They have good quality products |
| `assortment` | Họ cung cấp một phạm vi lớn và/hoặc độc đáo | They offer a large and/or unique assortment, variety |

**Display Logic:** Only shown if `not(selected(${largesupermarket_freq}, '0'))`

---

### `transportation_001`

**Question (EN):** What means of transport do you usually use to go to this large/chain SUPERMARKET?
**Question (VI):** Bạn thường sử dụng phương tiện giao thông nào để đến SIÊU THỊ lớn/chuỗi này?

**Type:** `select_one transport_type`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `home` | Là nhà | Is home |
| `walking` | Đi bộ | On foot |
| `bycicle` | Bằng xe đạp | By bicycle |
| `motorcycle` | Với xe tay ga hoặc xe máy | With a scooter or motorbike |
| `publictransport` | Xe buýt/phương tiện công cộng | Bus/public transport |
| `Taxi` | Taxi/xe công nghệ | Taxi/uber |
| `elevator` | Tôi đang đi nhờ xe của ai đó/ai đó đưa tôi đi | I'm hitching a ride with someone/someone brings me |
| `car_van` | Xe hơi hoặc xe tải nhỏ riêng | Own car or minivan |
| `companyvehicle` | Xe công ty | Company car |

**Display Logic:** Only shown if `not(selected(${largesupermarket_freq}, '0'))`

---

### `time_001`

**Question (EN):** Approximately how long does it take you to get to this large/chain SUPERMARKET, in minutes? (travel time)
**Question (VI):** Bạn mất khoảng bao lâu để đến được SIÊU THỊ lớn/chuỗi này, tính theo phút? (thời gian di chuyển)

**Type:** `integer`

**Display Logic:** Only shown if `not(selected(${largesupermarket_freq}, '0'))`

---


## Market (mainly fresh food, vegetables/fruit, with several market stalls):
*Chợ (chủ yếu là thực phẩm tươi sống, rau/trái cây, có một số gian hàng):*

### `market_freq`

**Question (EN):** How often do you go to a fresh MARKET to access food?
**Question (VI):** Tần suất bạn đến CHỢ để mua thực phẩm tươi sống?

**Type:** `select_one foodenvfrequency`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `40` | Nhiều lần trong ngày | Several times a day |
| `30` | 1 lần mỗi ngày | 1x daily |
| `8` | Nhiều lần một tuần | Several times a week |
| `4` | 1 lần/tuần | 1x per week |
| `2` | 2-3 lần/tháng | 2-3x per month |
| `1` | 1 lần hàng tháng | 1x monthly |
| `0` | Hiếm khi/không bao giờ | Rarely/never |

---

### `location_004`

**Question (EN):** Where is the main fresh MARKET that you visit regularly?
**Question (VI):** CHỢ đồ tươi sống chính mà bạn thường xuyên ghé thăm là ở đâu?

**Type:** `select_one foodenvlocation`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `street` | Trên con phố này | On this street |
| `neighbourhood` | Trong khu dân cư này | In this neighbourhood/residential area |
| `adminunit` | Trong khu nghỉ mát này | In this commune |
| `district` | Nơi khác ở quận Long Biên | Elsewhere in the Long Bien district |
| `city` | Ở trung tâm thành phố (Hà Nội) | In the city center (Hanoi) |
| `country` | Nơi khác ở Việt Nam | Elsewhere in Vietnam |
| `abroad` | Ở nước ngoài | Abroad |

**Display Logic:** Only shown if `not(selected(${market_freq}, '0'))`

---

### `reason_003`

**Question (EN):** What is the main reason you buy/gather food in this particular MARKET?
**Question (VI):** Lý do chính khiến bạn mua/lấy thực phẩm ở CHỢ này là gì?

**Type:** `select_one foodenvreason or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `trust` | Tôi biết rõ nhà cung cấp/nguồn này (tin tưởng) | I know this supplier/source personally (trust) |
| `cheap` | Giá rẻ | They are the cheapest |
| `close` | Khoảng cách gần | It's close |
| `healthy` | Họ có những lựa chọn lành mạnh | They have healthy options |
| `quality` | Họ có sản phẩm chất lượng tốt | They have good quality products |
| `assortment` | Họ cung cấp một phạm vi lớn và/hoặc độc đáo | They offer a large and/or unique assortment, variety |

**Display Logic:** Only shown if `not(selected(${market_freq}, '0'))`

---

### `transportation_002`

**Question (EN):** What means of transport do you usually use to go to this MARKET?
**Question (VI):** Bạn thường sử dụng phương tiện giao thông nào để đến CHỢ này?

**Type:** `select_one transport_type`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `home` | Là nhà | Is home |
| `walking` | Đi bộ | On foot |
| `bycicle` | Bằng xe đạp | By bicycle |
| `motorcycle` | Với xe tay ga hoặc xe máy | With a scooter or motorbike |
| `publictransport` | Xe buýt/phương tiện công cộng | Bus/public transport |
| `Taxi` | Taxi/xe công nghệ | Taxi/uber |
| `elevator` | Tôi đang đi nhờ xe của ai đó/ai đó đưa tôi đi | I'm hitching a ride with someone/someone brings me |
| `car_van` | Xe hơi hoặc xe tải nhỏ riêng | Own car or minivan |
| `companyvehicle` | Xe công ty | Company car |

**Display Logic:** Only shown if `not(selected(${market_freq}, '0'))`

---

### `time_002`

**Question (EN):** Approximately how long does it take you to get to this MARKET, in minutes? (travel time)
**Question (VI):** Bạn mất khoảng bao lâu để đến được CHỢ này, tính theo phút? (thời gian di chuyển)

**Type:** `integer`

**Display Logic:** Only shown if `not(selected(${market_freq}, '0'))`

---


## Street vendor/fresh food stall ("whole" food)
*Người bán hàng rong/quầy hàng thực phẩm tươi sống (thực phẩm "nguyên chất")*

### `streetven_freq`

**Question (EN):** How often do you go to a STREET VENDOR/stall to access food?
**Question (VI):** Tần suất bạn đến quầy hàng rong/quán ăn để mua đồ ăn?

**Type:** `select_one foodenvfrequency`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `40` | Nhiều lần trong ngày | Several times a day |
| `30` | 1 lần mỗi ngày | 1x daily |
| `8` | Nhiều lần một tuần | Several times a week |
| `4` | 1 lần/tuần | 1x per week |
| `2` | 2-3 lần/tháng | 2-3x per month |
| `1` | 1 lần hàng tháng | 1x monthly |
| `0` | Hiếm khi/không bao giờ | Rarely/never |

---

### `location_005`

**Question (EN):** Where is the main STREET VENDOR/stall that you visit regularly?
**Question (VI):** Quầy hàng/cửa hàng bán đồ lưu niệm chính mà bạn thường xuyên ghé thăm là ở đâu?

**Type:** `select_one foodenvlocation`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `street` | Trên con phố này | On this street |
| `neighbourhood` | Trong khu dân cư này | In this neighbourhood/residential area |
| `adminunit` | Trong khu nghỉ mát này | In this commune |
| `district` | Nơi khác ở quận Long Biên | Elsewhere in the Long Bien district |
| `city` | Ở trung tâm thành phố (Hà Nội) | In the city center (Hanoi) |
| `country` | Nơi khác ở Việt Nam | Elsewhere in Vietnam |
| `abroad` | Ở nước ngoài | Abroad |

**Display Logic:** Only shown if `not(selected(${streetven_freq}, '0'))`

---

### `reason_004`

**Question (EN):** What is the main reason you buy/gather food from this particular STREET VENDOR/stall?
**Question (VI):** Lý do chính khiến bạn mua/lấy thực phẩm từ NGƯỜI BÁN HÀNG/quầy hàng rong này là gì?

**Type:** `select_one foodenvreason or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `trust` | Tôi biết rõ nhà cung cấp/nguồn này (tin tưởng) | I know this supplier/source personally (trust) |
| `cheap` | Giá rẻ | They are the cheapest |
| `close` | Khoảng cách gần | It's close |
| `healthy` | Họ có những lựa chọn lành mạnh | They have healthy options |
| `quality` | Họ có sản phẩm chất lượng tốt | They have good quality products |
| `assortment` | Họ cung cấp một phạm vi lớn và/hoặc độc đáo | They offer a large and/or unique assortment, variety |

**Display Logic:** Only shown if `not(selected(${streetven_freq}, '0'))`

---

### `transportation_003`

**Question (EN):** What mode of transport do you usually use to go to this STREET VENDOR/stall?
**Question (VI):** Bạn thường sử dụng phương tiện giao thông nào để đến quầy hàng/người bán hàng rong này?

**Type:** `select_one transport_type`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `home` | Là nhà | Is home |
| `walking` | Đi bộ | On foot |
| `bycicle` | Bằng xe đạp | By bicycle |
| `motorcycle` | Với xe tay ga hoặc xe máy | With a scooter or motorbike |
| `publictransport` | Xe buýt/phương tiện công cộng | Bus/public transport |
| `Taxi` | Taxi/xe công nghệ | Taxi/uber |
| `elevator` | Tôi đang đi nhờ xe của ai đó/ai đó đưa tôi đi | I'm hitching a ride with someone/someone brings me |
| `car_van` | Xe hơi hoặc xe tải nhỏ riêng | Own car or minivan |
| `companyvehicle` | Xe công ty | Company car |

**Display Logic:** Only shown if `not(selected(${streetven_freq}, '0'))`

---

### `time_003`

**Question (EN):** Approximately how long does it take you to get to this STREET VENDOR/stall, in minutes? (travel time)
**Question (VI):** Bạn mất khoảng bao lâu để đến được quầy hàng/cửa hàng bán hàng rong này, tính theo phút? (thời gian di chuyển)

**Type:** `integer`

**Display Logic:** Only shown if `not(selected(${streetven_freq}, '0'))`

---


## Wholesaler (wholesaler) e.g. [local examples]
*Người bán buôn (người bán buôn) ví dụ [ví dụ địa phương]*

### `wholesaler_freq`

**Question (EN):** How often do you go to a WHOLESALER to access food?
**Question (VI):** Tần suất bạn đến NHÀ BÁN BUÔN để mua thực phẩm như thế nào?

**Type:** `select_one foodenvfrequency`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `40` | Nhiều lần trong ngày | Several times a day |
| `30` | 1 lần mỗi ngày | 1x daily |
| `8` | Nhiều lần một tuần | Several times a week |
| `4` | 1 lần/tuần | 1x per week |
| `2` | 2-3 lần/tháng | 2-3x per month |
| `1` | 1 lần hàng tháng | 1x monthly |
| `0` | Hiếm khi/không bao giờ | Rarely/never |

---

### `location_006`

**Question (EN):** Where is the main WHOLESALER that you visit regularly?
**Question (VI):** Nhà bán buôn chính mà bạn thường xuyên ghé thăm là ở đâu?

**Type:** `select_one foodenvlocation`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `street` | Trên con phố này | On this street |
| `neighbourhood` | Trong khu dân cư này | In this neighbourhood/residential area |
| `adminunit` | Trong khu nghỉ mát này | In this commune |
| `district` | Nơi khác ở quận Long Biên | Elsewhere in the Long Bien district |
| `city` | Ở trung tâm thành phố (Hà Nội) | In the city center (Hanoi) |
| `country` | Nơi khác ở Việt Nam | Elsewhere in Vietnam |
| `abroad` | Ở nước ngoài | Abroad |

**Display Logic:** Only shown if `not(selected(${wholesaler_freq}, '0'))`

---

### `reason_005`

**Question (EN):** What is the main reason you buy/gather food from this particular WHOLESALER?
**Question (VI):** Lý do chính khiến bạn mua/thu thập thực phẩm từ NHÀ BÁN BUÔN này là gì?

**Type:** `select_one foodenvreason or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `trust` | Tôi biết rõ nhà cung cấp/nguồn này (tin tưởng) | I know this supplier/source personally (trust) |
| `cheap` | Giá rẻ | They are the cheapest |
| `close` | Khoảng cách gần | It's close |
| `healthy` | Họ có những lựa chọn lành mạnh | They have healthy options |
| `quality` | Họ có sản phẩm chất lượng tốt | They have good quality products |
| `assortment` | Họ cung cấp một phạm vi lớn và/hoặc độc đáo | They offer a large and/or unique assortment, variety |

**Display Logic:** Only shown if `not(selected(${wholesaler_freq}, '0'))`

---

### `transportation_004`

**Question (EN):** What means of transport do you usually use to get to this WHOLESALER?
**Question (VI):** Bạn thường sử dụng phương tiện giao thông nào để đến NHÀ BÁN BUÔN này?

**Type:** `select_one transport_type`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `home` | Là nhà | Is home |
| `walking` | Đi bộ | On foot |
| `bycicle` | Bằng xe đạp | By bicycle |
| `motorcycle` | Với xe tay ga hoặc xe máy | With a scooter or motorbike |
| `publictransport` | Xe buýt/phương tiện công cộng | Bus/public transport |
| `Taxi` | Taxi/xe công nghệ | Taxi/uber |
| `elevator` | Tôi đang đi nhờ xe của ai đó/ai đó đưa tôi đi | I'm hitching a ride with someone/someone brings me |
| `car_van` | Xe hơi hoặc xe tải nhỏ riêng | Own car or minivan |
| `companyvehicle` | Xe công ty | Company car |

**Display Logic:** Only shown if `not(selected(${wholesaler_freq}, '0'))`

---

### `time_004`

**Question (EN):** Approximately how long does it take you to get to this WHOLESALER, in minutes? (travel time)
**Question (VI):** Bạn mất khoảng bao lâu để đến được NHÀ BÁN BUÔN này, tính theo phút? (thời gian di chuyển)

**Type:** `integer`

**Display Logic:** Only shown if `not(selected(${wholesaler_freq}, '0'))`

---


## Retailer/retailer (baker, butcher, specialty store):
*Nhà bán lẻ/bán lẻ (thợ làm bánh, thợ làm thịt, cửa hàng đặc sản):*

### `retail_freq`

**Question (EN):** How often do you go to a RETAILER (bakery, butchery...) to access food?
**Question (VI):** Tần suất bạn đến NHÀ BÁN LẺ (tiệm bánh, cửa hàng thịt...) để mua thực phẩm như thế nào?

**Type:** `select_one foodenvfrequency`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `40` | Nhiều lần trong ngày | Several times a day |
| `30` | 1 lần mỗi ngày | 1x daily |
| `8` | Nhiều lần một tuần | Several times a week |
| `4` | 1 lần/tuần | 1x per week |
| `2` | 2-3 lần/tháng | 2-3x per month |
| `1` | 1 lần hàng tháng | 1x monthly |
| `0` | Hiếm khi/không bao giờ | Rarely/never |

---

### `location_007`

**Question (EN):** Where is the main RETAILER (bakery, butcher's shop, etc.) that you visit regularly?
**Question (VI):** Cửa hàng bán lẻ chính (tiệm bánh, cửa hàng thịt, v.v.) mà bạn thường xuyên ghé thăm là ở đâu?

**Type:** `select_one foodenvlocation`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `street` | Trên con phố này | On this street |
| `neighbourhood` | Trong khu dân cư này | In this neighbourhood/residential area |
| `adminunit` | Trong khu nghỉ mát này | In this commune |
| `district` | Nơi khác ở quận Long Biên | Elsewhere in the Long Bien district |
| `city` | Ở trung tâm thành phố (Hà Nội) | In the city center (Hanoi) |
| `country` | Nơi khác ở Việt Nam | Elsewhere in Vietnam |
| `abroad` | Ở nước ngoài | Abroad |

**Display Logic:** Only shown if `not(selected(${retail_freq}, '0'))`

---

### `reason_006`

**Question (EN):** What is the main reason you buy/gather food in this specific RETAILER (bakery, butchery...)?
**Question (VI):** Lý do chính khiến bạn mua/lấy thực phẩm tại NHÀ BÁN LẺ này (tiệm bánh, cửa hàng thịt...) là gì?

**Type:** `select_one foodenvreason or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `trust` | Tôi biết rõ nhà cung cấp/nguồn này (tin tưởng) | I know this supplier/source personally (trust) |
| `cheap` | Giá rẻ | They are the cheapest |
| `close` | Khoảng cách gần | It's close |
| `healthy` | Họ có những lựa chọn lành mạnh | They have healthy options |
| `quality` | Họ có sản phẩm chất lượng tốt | They have good quality products |
| `assortment` | Họ cung cấp một phạm vi lớn và/hoặc độc đáo | They offer a large and/or unique assortment, variety |

**Display Logic:** Only shown if `not(selected(${retail_freq}, '0'))`

---

### `transportation_005`

**Question (EN):** Which means of transport do you usually use to go to this RETAILER (bakery, butcher's shop...)?
**Question (VI):** Bạn thường sử dụng phương tiện di chuyển nào để đến CỬA HÀNG BÁN LẺ này (tiệm bánh, cửa hàng thịt...)?

**Type:** `select_one transport_type`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `home` | Là nhà | Is home |
| `walking` | Đi bộ | On foot |
| `bycicle` | Bằng xe đạp | By bicycle |
| `motorcycle` | Với xe tay ga hoặc xe máy | With a scooter or motorbike |
| `publictransport` | Xe buýt/phương tiện công cộng | Bus/public transport |
| `Taxi` | Taxi/xe công nghệ | Taxi/uber |
| `elevator` | Tôi đang đi nhờ xe của ai đó/ai đó đưa tôi đi | I'm hitching a ride with someone/someone brings me |
| `car_van` | Xe hơi hoặc xe tải nhỏ riêng | Own car or minivan |
| `companyvehicle` | Xe công ty | Company car |

**Display Logic:** Only shown if `not(selected(${retail_freq}, '0'))`

---

### `time_005`

**Question (EN):** Approximately how long does it take you to get to this RETAILER (bakery, butcher's shop...), in minutes? (travel time)
**Question (VI):** Bạn mất khoảng bao lâu để đến được NHÀ BÁN LẺ này (tiệm bánh, cửa hàng thịt...), tính bằng phút? (thời gian di chuyển)

**Type:** `integer`

**Display Logic:** Only shown if `not(selected(${retail_freq}, '0'))`

---


## Restaurant (DINE-IN)
*Nhà hàng (ĂN TẠI NHÀ)*

### `resto_freq`

**Question (EN):** How often do you go to a RESTAURANT (dine-in) to access food?
**Question (VI):** Tần suất bạn đến NHÀ HÀNG (ăn tại chỗ) để ăn uống ?

**Type:** `select_one foodenvfrequency`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `40` | Nhiều lần trong ngày | Several times a day |
| `30` | 1 lần mỗi ngày | 1x daily |
| `8` | Nhiều lần một tuần | Several times a week |
| `4` | 1 lần/tuần | 1x per week |
| `2` | 2-3 lần/tháng | 2-3x per month |
| `1` | 1 lần hàng tháng | 1x monthly |
| `0` | Hiếm khi/không bao giờ | Rarely/never |

---

### `location_008`

**Question (EN):** Where is the main RESTAURANT (dine-in) that you visit regularly?
**Question (VI):** NHÀ HÀNG chính (ăn tại chỗ) mà bạn thường xuyên ghé thăm là ở đâu?

**Type:** `select_one foodenvlocation`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `street` | Trên con phố này | On this street |
| `neighbourhood` | Trong khu dân cư này | In this neighbourhood/residential area |
| `adminunit` | Trong khu nghỉ mát này | In this commune |
| `district` | Nơi khác ở quận Long Biên | Elsewhere in the Long Bien district |
| `city` | Ở trung tâm thành phố (Hà Nội) | In the city center (Hanoi) |
| `country` | Nơi khác ở Việt Nam | Elsewhere in Vietnam |
| `abroad` | Ở nước ngoài | Abroad |

**Display Logic:** Only shown if `not(selected(${resto_freq}, '0'))`

---

### `reason_007`

**Question (EN):** What is the main reason you purchase/gather food at this particular RESTAURANT (dine-in)?
**Question (VI):** Lý do chính khiến bạn mua/đi ăn tại NHÀ HÀNG này (ăn tại chỗ) là gì?

**Type:** `select_one foodenvreason or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `trust` | Tôi biết rõ nhà cung cấp/nguồn này (tin tưởng) | I know this supplier/source personally (trust) |
| `cheap` | Giá rẻ | They are the cheapest |
| `close` | Khoảng cách gần | It's close |
| `healthy` | Họ có những lựa chọn lành mạnh | They have healthy options |
| `quality` | Họ có sản phẩm chất lượng tốt | They have good quality products |
| `assortment` | Họ cung cấp một phạm vi lớn và/hoặc độc đáo | They offer a large and/or unique assortment, variety |

**Display Logic:** Only shown if `not(selected(${resto_freq}, '0'))`

---

### `transportation_006`

**Question (EN):** What mode of transportation do you usually use to get to this RESTAURANT (dine-in)?
**Question (VI):** Bạn thường sử dụng phương tiện di chuyển nào để đến NHÀ HÀNG này (ăn tại chỗ)?

**Type:** `select_one transport_type`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `home` | Là nhà | Is home |
| `walking` | Đi bộ | On foot |
| `bycicle` | Bằng xe đạp | By bicycle |
| `motorcycle` | Với xe tay ga hoặc xe máy | With a scooter or motorbike |
| `publictransport` | Xe buýt/phương tiện công cộng | Bus/public transport |
| `Taxi` | Taxi/xe công nghệ | Taxi/uber |
| `elevator` | Tôi đang đi nhờ xe của ai đó/ai đó đưa tôi đi | I'm hitching a ride with someone/someone brings me |
| `car_van` | Xe hơi hoặc xe tải nhỏ riêng | Own car or minivan |
| `companyvehicle` | Xe công ty | Company car |

**Display Logic:** Only shown if `not(selected(${resto_freq}, '0'))`

---

### `time_006`

**Question (EN):** Approximately how long does it take you to get to this RESTAURANT (dine-in), in minutes? (travel time)
**Question (VI):** Bạn mất khoảng bao lâu để đến NHÀ HÀNG này (ăn tại chỗ) (tính bằng phút)? (thời gian di chuyển)

**Type:** `integer`

**Display Logic:** Only shown if `not(selected(${resto_freq}, '0'))`

---


## Food trucks or takeaway street vendors selling prepared meals/snacks
*Xe tải thực phẩm hoặc những người bán hàng rong bán đồ ăn chế biến sẵn/đồ ăn nhẹ*

### `foodtruck_freq`

**Question (EN):** How often do you go to a FOOD TRUCK to access food?
**Question (VI):** Bạn thường xuyên đến Xe bán thức ăn để lấy thực phẩm như thế nào?

**Type:** `select_one foodenvfrequency`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `40` | Nhiều lần trong ngày | Several times a day |
| `30` | 1 lần mỗi ngày | 1x daily |
| `8` | Nhiều lần một tuần | Several times a week |
| `4` | 1 lần/tuần | 1x per week |
| `2` | 2-3 lần/tháng | 2-3x per month |
| `1` | 1 lần hàng tháng | 1x monthly |
| `0` | Hiếm khi/không bao giờ | Rarely/never |

---

### `location_009`

**Question (EN):** Where is the main FOOD TRUCK that you visit regularly?
**Question (VI):** Xe bán đồ ăn chính mà bạn thường xuyên ghé thăm là ở đâu?

**Type:** `select_one foodenvlocation`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `street` | Trên con phố này | On this street |
| `neighbourhood` | Trong khu dân cư này | In this neighbourhood/residential area |
| `adminunit` | Trong khu nghỉ mát này | In this commune |
| `district` | Nơi khác ở quận Long Biên | Elsewhere in the Long Bien district |
| `city` | Ở trung tâm thành phố (Hà Nội) | In the city center (Hanoi) |
| `country` | Nơi khác ở Việt Nam | Elsewhere in Vietnam |
| `abroad` | Ở nước ngoài | Abroad |

**Display Logic:** Only shown if `not(selected(${foodtruck_freq}, '0'))`

---

### `reason_008`

**Question (EN):** What is the main reason you buy/gather food in this specific FOODTRUCK?
**Question (VI):** Lý do chính khiến bạn mua/lấy thực phẩm trong Xe bán thức ăn này là gì?

**Type:** `select_one foodenvreason or_other`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `trust` | Tôi biết rõ nhà cung cấp/nguồn này (tin tưởng) | I know this supplier/source personally (trust) |
| `cheap` | Giá rẻ | They are the cheapest |
| `close` | Khoảng cách gần | It's close |
| `healthy` | Họ có những lựa chọn lành mạnh | They have healthy options |
| `quality` | Họ có sản phẩm chất lượng tốt | They have good quality products |
| `assortment` | Họ cung cấp một phạm vi lớn và/hoặc độc đáo | They offer a large and/or unique assortment, variety |

**Display Logic:** Only shown if `not(selected(${foodtruck_freq}, '0'))`

---

### `transportation_007`

**Question (EN):** What mode of transportation do you usually use to get to this FOOD TRUCK?
**Question (VI):** Bạn thường sử dụng phương tiện di chuyển nào để đến XE này?

**Type:** `select_one transport_type`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `home` | Là nhà | Is home |
| `walking` | Đi bộ | On foot |
| `bycicle` | Bằng xe đạp | By bicycle |
| `motorcycle` | Với xe tay ga hoặc xe máy | With a scooter or motorbike |
| `publictransport` | Xe buýt/phương tiện công cộng | Bus/public transport |
| `Taxi` | Taxi/xe công nghệ | Taxi/uber |
| `elevator` | Tôi đang đi nhờ xe của ai đó/ai đó đưa tôi đi | I'm hitching a ride with someone/someone brings me |
| `car_van` | Xe hơi hoặc xe tải nhỏ riêng | Own car or minivan |
| `companyvehicle` | Xe công ty | Company car |

**Display Logic:** Only shown if `not(selected(${foodtruck_freq}, '0'))`

---

### `time_007`

**Question (EN):** Approximately how long does it take you to get to this FOOD TRUCK, in minutes? (travel time)
**Question (VI):** Bạn mất khoảng bao lâu để đến được Xe bán thức ăn này, tính theo phút? (thời gian di chuyển)

**Type:** `integer`

**Display Logic:** Only shown if `not(selected(${foodtruck_freq}, '0'))`

---


## 

### `order_freq`

**Question (EN):** How often do you order food online for delivery at your home, either using an app (for example Grab), or directly from the restaurant (phone, website)?
**Question (VI):** Bạn thường xuyên đặt đồ ăn trực tuyến để giao nhà như thế nào, thông qua ứng dụng (ví dụ Grab) hoặc trực tiếp từ nhà hàng (điện thoại, trang web)?

**Type:** `select_one foodenvfrequency`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `40` | Nhiều lần trong ngày | Several times a day |
| `30` | 1 lần mỗi ngày | 1x daily |
| `8` | Nhiều lần một tuần | Several times a week |
| `4` | 1 lần/tuần | 1x per week |
| `2` | 2-3 lần/tháng | 2-3x per month |
| `1` | 1 lần hàng tháng | 1x monthly |
| `0` | Hiếm khi/không bao giờ | Rarely/never |

---


## Food Security: In the past 12 MONTHS, has it happened that you ___?
*An ninh lương thực: Trong 12 THÁNG qua, bạn có ___ không?*

### `Sau_y_l_v_i_c_u_h_c_khi_n_o_`

**Question (EN):** I am now going to ask you some questions about food security. It is important that you are honest about this. We remind you that this interview is anonymous and for scientific research. In the past 12 MONTHS, has there been a time when you __________? -->
**Question (VI):** Sau đây là vài câu hỏi về thực phẩm. Trong 12 THÁNG qua, có khi nào__________?

**Type:** `note`

---

### `worried`

**Question (EN):** During the last 12 MONTHS (year), was there a time when you were WORRIED you would not have enough food to eat because of a lack of money or other resources
**Question (VI):** Anh/Chị lo lắng Anh/Chị không có đủ thức ăn vì thiếu tiền hay các nguồn lực khác?

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `no` | KHÔNG | No |

**Appearance:** `quick`

---

### `healthy`

**Question (EN):** In the last 12 MONTHS (year), was there a time when you were unable to eat HEALTHY and nutricious food because of a lack of money or other resources?
**Question (VI):** Vẫn nghĩ về thời gian 12 THÁNG trước, có khi nào Anh/Chị không thể ăn uống lành mạnh và đủ dinh dưỡng vì  thiếu tiền hay các nguồn lực khác?

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `no` | KHÔNG | No |

**Appearance:** `quick`

---

### `fewfoods`

**Question (EN):** During the last 12 MONTHS (year), was there a time when you ate only a FEW KINDS of foods because of a lack of money or other resources?
**Question (VI):** Anh/Chị chỉ ăn một vài loại thực phẩm vì thiếu tiền hay các nguồn lực khác.

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `no` | KHÔNG | No |

**Appearance:** `quick`

---

### `skipped`

**Question (EN):** During the last 12 MONTHS (year), was there a time when you had to SKIP A MEAL because there was not enough money or other resources to get food?
**Question (VI):** Anh/Chị đã phải bỏ một bữa vì thiếu tiền hay các nguồn lực khác để có được thực phẩm

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `no` | KHÔNG | No |

**Appearance:** `quick`

---

### `ateless`

**Question (EN):** Still thinking about the last 12 MONTHS (year), was there a time when you ATE LESS than you thought you should because of a lack of money or other resources?
**Question (VI):** Vẫn nghĩ về thời gian 12 THÁNG trước, có khi nào Anh/Chị ăn ít hơn số lượng Anh/Chị nghĩ mình nên được ăn vì thiếu tiền hay các nguồn lực khác.

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `no` | KHÔNG | No |

**Appearance:** `quick`

---

### `ranout`

**Question (EN):** Was there a time in the past 12 MONTHS (year), when your household RAN OUT of food because of a lack of money or other resources?
**Question (VI):** GIa đình Anh/Chị cạn kiệt thực phẩm vì  thiếu tiền hay các nguồn lực khác.

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `no` | KHÔNG | No |

**Appearance:** `quick`

---

### `hungry`

**Question (EN):** Was there a time in the last 12 MONTHS (year) when you were HUNGRY but did not eat because there was not enough money or other resources for food?
**Question (VI):** Trong vòng 12 tháng qua, những việc này xảy ra thường xuyên như thế nào khiến anh/chị bị đói nhưng không ăn vì thiếu tiền hay các nguồn lực khác cho thực phẩm?

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `no` | KHÔNG | No |

**Appearance:** `quick`

---

### `whlday`

**Question (EN):** During the last 12 MONTHS (year), was there a time when you went without eating for a WHOLE DAY because of a lack of money or other resources?
**Question (VI):** Trong vòng 12 tháng qua, những việc này xảy ra thường xuyên như thế nào khiến anh/chị không ăn gì cả ngày vì thiếu tiền hay các nguồn lực khác?

**Type:** `select_one yes_no`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `yes` | CÓ | Yes |
| `no` | KHÔNG | No |

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

**Question (EN):** Which of the following food-related activities did you undertake in the days leading up to the Typhoon, to prepare?
**Question (VI):** Bạn đã lthực hiện hoạt động nào liên quan đến thực phẩm sau đây trong những ngày trước khi Bão đổ bộ để chuẩn bị?

**Type:** `select_multiple typh_prepare`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `stockpiling` | Dự trữ nhu yếu phẩm: Mua và dự trữ thêm thực phẩm, đặc biệt là các loại hàng hóa bảo quản lâu như gạo, mì khô và các sản phẩm đóng hộp. | Stockpiling Essentials: Purchase and store extra food supplies, especially non-perishable goods like rice, dried noodles, and canned products. |
| `securing` | Đảm bảo hàng tồn kho: Bảo quản thực phẩm dễ hỏng bằng cách cất giữ ở những khu vực phù hợp tại nhà. | Securing Inventory: Safeguarding perishable items by storing them in protected areas at home. |
| `securing_away` | Bảo quản hàng: Bảo quản thực phẩm bằng cách di chuyển đến những nơi an toàn hơn, tránh xa các khu vực dễ bị ngập lụt. | Securing Inventory: Safeguarding food by moving it to safer locations away from flood-prone zones. |
| `strengthening_infrastructure` | Tăng cường cơ sở hạ tầng: Gia cố nhà để chống chọi với gió mạnh và mưa lớn, sử dụng bạt, bao cát hoặc các vật liệu để gia cố khác. | Strengthening Infrastructure: Reinforcing the home to withstand strong winds and heavy rain, using tarps, sandbags, or other stabilizing materials. |
| `collaborating_vendors` | Hợp tác với các nhà cung cấp địa phương: Xây dựng quan hệ, hợp tác với những người cung cấp/kinh doanh thực phẩm tại địa phương có thể dễ dàng tiếp cận, liên lạc sau khi bão qua. | Collaborating with Local Suppliers: Building relationships with local food vendors who may be more accessible after the typhoon. |
| `saving_cash` | Tiết kiệm tiền cho các trường hợp khẩn cấp: Dự trữ tiền mặt để trang trải chi phí trong và sau cơn bão. | Saving Cash for Emergencies: Keeping cash reserves to cover costs during and after the typhoon. |
| `communicating_customers` | Liên hệ với những người cung cấp, kinh doanh thực phẩm: cập nhật tình hình qua mạng xã hội, ứng dụng nhắn tin hoặc truyền miệng. | Communicating with food vendors: staying informed via social media, messaging apps, or word of mouth. |
| `contingency_poweroutages` | Lập kế hoạch dự phòng cho tình huống mất điện: Chuẩn bị các giải pháp dự phòng như máy phát điện hoặc hộp giữ lạnh để bảo quản thực phẩm dễ hỏng luôn tươi sống trong trường hợp mất điện. | Contingency Planning for Power Outages: Preparing backup solutions such as generators or ice boxes to keep perishable food fresh if electricity is disrupted. |

---

### `typhoon_cope`

**Question (EN):** Which of the following food-related activities did you undertake in during the Typhoon and subsequent flooding, to cope?
**Question (VI):** Bạn đã thực hiện hoạt động nào liên quan đến thực phẩm sau đây trong thời gian Bão đổ bộ và lũ lụt sau đó để ứng phó?

**Type:** `select_multiple typh_cope`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `lockdown` | Ở trong nhà nhiều ngày (trong thời gian có bão và lũ lụt) | Stay inside the home for multiple days (during typhoon and during flooding) |
| `partial_lockdown` | Chỉ ở trong nhà trong thời gian có bão | Stay inside the home during typhoon only |
| `socialaccess` | Chia sẻ thức ăn với hàng xóm, thành viên gia đình, v.v. | Share food with neighbours, family members etc |
| `financialaccess` | Mua thức ăn cho người nghèo hoặc đến những người bán thức ăn giá cả phải chăng hơn | Purchase chaper food, or go to more afforable food vendors |
| `physicalaccess` | Mua thức ăn ở những nơi gần nhà hơn | Purchase food in places that are closer to home |

---

### `typhoon_financial`

**Question (EN):** Have there been any financial losses, and if so, has your household financially recovered from this Typhoon event?
**Question (VI):** Có bất kỳ tổn thất tài chính nào không và nếu có, hộ gia đình bạn đã phục hồi tài chính sau sự kiện Bão đổ bộ này chưa?

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

**Question (EN):** Have there been any physical damages to your house, and if so, has your house recovered from this Typhoon event?
**Question (VI):** Nhà của bạn có bị thiệt hại vật chất nào không và nếu có, nhà của bạn đã phục hồi sau sự kiện Bão đổ bộ này chưa?

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

**Question (EN):** Approximately, how much food does your household discard (throw away) per day/week/month?
**Question (VI):** Khoảng bao nhiêu thực phẩm mà hộ gia đình bạn vứt bỏ (vứt bỏ) mỗi ngày/tuần/tháng?

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
**Question (VI):** Lượng thực phẩm đó được vứt bỏ theo:

**Type:** `select_one dayweekmonth`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `day` | Ngày | Day |
| `week` | Tuần | Week |
| `month` | Tháng | Month |

---

### `foodwaste_freq`

**Question (EN):** How often do you discard food?
**Question (VI):** Bạn vứt bỏ thực phẩm thường xuyên như thế nào?

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
| `7` | không biết | don't know |

---

### `foodwaste_mainreason`

**Question (EN):** What are the main reasons your household needs to discard food?
**Question (VI):** Những lý do chính khiến bạn vứt bỏ thực phẩm là gì?

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
**Question (VI):** Bạn thường làm gì với thực phẩm bị vứt bỏ?

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


## Other economic indicators/food accessibility
*Các chỉ số kinh tế khác/ khả năng tiếp cận lương thực*

### `foodexpenditure`

**Question (EN):** How much Vietnamese Dong (VND) does your household spend on food on average per day/week/month?
**Question (VI):** Trung bình mỗi ngày/tuần/tháng, hộ gia đình bạn chi bao nhiêu tiền Việt Nam (VND) cho thực phẩm?

**Type:** `text`

---

### `foodexp_timeunit`

**Question (EN):** ${foodexpenditure} Vietnamese Dong (VND) per:
**Question (VI):** ${foodexpenditure} Đồng Việt Nam (đồng) cho mỗi:

**Type:** `select_one dayweekmonth`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `day` | Ngày | Day |
| `week` | Tuần | Week |
| `month` | Tháng | Month |

---

### `income`

**Question (EN):** What is the estimated total monthly family income in Vietnamese Dong (VND)? (i.e. the monthly income of all working household members combined)
**Question (VI):** Tổng thu nhập gia đình hàng tháng ước tính bằng Đồng Việt Nam (VND) là bao nhiêu? (tức là thu nhập hàng tháng của tất cả các thành viên trong gia đình đi làm cộng lại)

**Type:** `select_one income`

**Options:**

| Value | Vietnamese | English |
|-------|-----------|---------|
| `400000` | < 800k đồng | < 800k VND |
| `1150000` | 800k – 1,5 triệu | 800k – 1,5 mil |
| `2000000` | 1,5 triệu – 2,5 triệu | 1,5 mil – 2,5 mil |
| `3000000` | 2,5 triệu – 3,5 triệu | 2,5 mil – 3,5 mil |
| `4250000` | 3,5 triệu – 5 triệu | 3,5 mil – 5 mil |
| `6000000` | 5 triệu – 7 triệu | 5 mil – 7 mil |
| `8500000` | 7 triệu – 10 triệu | 7 mil – 10 mil |
| `11000000` | 10 triệu – 12 triệu | 10 mil – 12 mil |
| `13000000` | 12 triệu – 14 triệu | 12 mil – 14 mil |
| `15000000` | 14 triệu – 16 triệu | 14 mil – 16 mil |
| `17000000` | 16 triệu – 18 triệu | 16 mil – 18 mil |
| `20000000` | 18 triệu – 22 triệu | 18 mil – 22 mil |
| `24000000` | 22 triệu – 26 triệu | 22 mil – 26 mil |
| `30500000` | 26 triệu – 35 triệu | 26 mil – 35 mil |
| `42500000` | 35 triệu – 50 triệu | 35 mil – 50 mil |
| `75000000` | 50 triệu – 100 triệu | 50 mil – 100 mil |
| `100000000` | > 100 triệu đồng | > 100 mil VND |

**Appearance:** `quick`

---


## Number of vehicles
*Số lượng xe*

### `N_u_h_gia_nh_s_h_ng_cho_bi_t_s_l_ng`

**Question (EN):** If the household owns any of the following food items in working condition, please indicate how many.
**Question (VI):** Nếu hộ gia đình sở hữu bất kỳ loại trang thiết bị, vật tư nào sau đây còn sử dụng được, vui lòng cho biết số lượng.

**Type:** `note`

---

### `car`

**Question (EN):** Car/car (including company car):
**Question (VI):** Xe hơi (bao gồm cả xe công ty):

**Type:** `integer`

---

### `motorcycle`

**Question (EN):** Motorcycle/scooter:
**Question (VI):** Xe máy/xe tay ga:

**Type:** `integer`

---

### `van`

**Question (EN):** Van/minivan:
**Question (VI):** Xe tải/xe tải nhỏ:

**Type:** `integer`

---

### `truck`

**Question (EN):** Truck/van/truck:
**Question (VI):** Xe tải/xe van/xe tải:

**Type:** `integer`

---

### `bicycle`

**Question (EN):** Bicycle:
**Question (VI):** Xe đạp:

**Type:** `integer`

---


## Debriefing
*Tóm tắt*

### `Xin_ch_n_th_nh_c_m_m_t_ng_y_th_t_vui_v`

**Question (EN):** Thank you very much for your cooperation. Your anonymous answers will be important for scientific research and my studies at VNU & KU Leuven (Belgium). If you have any questions, you can always send an email to: lisamarie.hemerijckx@kuleuven.be or [EMAIL CHI/HUONG]. If you wish to receive the results of this survey, please provide your email address (we will record this in a separate document from this survey). You can decide to withdraw your participation up to one month after this interview. We hereby end the survey and wish you a very pleasant day.
**Question (VI):** Xin chân thành cảm ơn sự hợp tác của bạn. Những câu trả lời ẩn danh của bạn sẽ rất quan trọng đối với nghiên cứu khoa học và việc học của tôi tại VNU & KU Leuven (Bỉ). Nếu bạn có bất kỳ câu hỏi nào, bạn luôn có thể gửi email đến: lisamarie.hemerijckx@kuleuven.be hoặc [EMAIL CHI/HUONG]. Nếu bạn muốn nhận kết quả của cuộc khảo sát này, vui lòng cung cấp địa chỉ email của bạn (chúng tôi sẽ ghi lại địa chỉ này trong một tài liệu riêng biệt từ cuộc khảo sát này). Bạn có thể quyết định rút trong vòng một tháng sau cuộc phỏng vấn này. Chúng tôi xin kết thúc cuộc khảo sát và chúc bạn một ngày thật vui vẻ.

**Type:** `note`

---


## END
*KẾT THÚC*

### `_y_l_ph_n_k_t_th_c_c_k_t_n_i_internet`

**Question (EN):** This is the end of the survey. Conclude the conversation. Make sure you SAVE the survey and forward it as soon as there is an internet connection.
**Question (VI):** Đây là phần kết thúc của cuộc khảo sát. Kết thúc cuộc trò chuyện. Đảm bảo rằng bạn LƯU cuộc khảo sát và chuyển tiếp ngay khi có kết nối internet.

**Type:** `note`

---

### `picture`

**Question (EN):** PHOTO: If the respondent agrees, take a photo of the outside of the home, preferably WITHOUT the respondent in it, unless the respondent explicitly wishes this.
**Question (VI):** ẢNH: Nếu người trả lời đồng ý, hãy chụp ảnh bên ngoài ngôi nhà, tốt nhất là KHÔNG có người trả lời trong ảnh, trừ khi người trả lời muốn như vậy một cách rõ ràng.

**Type:** `image`

---

### `comments`

**Question (EN):** As a SURVEYOR, do you have any final notes about this survey? Something interesting, something strange? If NO location could be recorded, enter the address/coordinates here.
**Question (VI):** Là một NGƯỜI KHẢO SÁT, bạn có ghi chú cuối cùng nào về cuộc khảo sát này không? Có điều gì thú vị, có điều gì lạ không? Nếu KHÔNG thể ghi lại địa điểm, hãy nhập địa chỉ/tọa độ vào đây.

**Type:** `text`

---
