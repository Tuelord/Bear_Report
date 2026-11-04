# Bear Buddy

Đặc tả người dùng và thiết kế giao diện

Tài liệu trình bày Chương 1, Chương 2 và Chương 5 của báo cáo Bear Buddy. Nội dung nối mục tiêu sản phẩm với hồ sơ năng lực phát triển, cơ sở social story và quyết định UX. Các persona được mô phỏng để phục vụ thiết kế; kết quả khảo sát và thử nghiệm người dùng cần được bổ sung bằng dữ liệu thực tế.

# Chương 1 Introduction

## 1.1 Description Mô tả ứng dụng

Bear Buddy là ứng dụng mobile hỗ trợ trẻ em tự kỷ làm quen với các tình huống xã hội hằng ngày thông qua câu chuyện ngắn, hình ảnh, lời kể và hoạt động tương tác. Ứng dụng được định hướng là công cụ học tập theo tình huống, trong đó trẻ có cơ hội tìm hiểu bối cảnh, dự đoán diễn biến, lựa chọn cách phản hồi và xem lời giải thích trước khi gặp tình huống tương tự ngoài thực tế.

Nội dung của Bear Buddy được chuẩn bị theo định hướng social story và được bổ sung hoạt động tương tác. Những tình huống ban đầu bao gồm chờ đến lượt, làm quen bạn mới, xin tham gia trò chơi và nhờ sự giúp đỡ. Các chủ đề có thể được mở rộng thành những hoàn cảnh cụ thể như đi khám bác sĩ, đi cắt tóc, chuyển lớp hoặc ứng phó khi lời đề nghị chưa được chấp nhận.

Trong một phiên sử dụng, phụ huynh hoặc giáo viên lựa chọn câu chuyện phù hợp, giới thiệu hoạt động và hỗ trợ khi cần. Trẻ trực tiếp xem, nghe và tương tác với câu chuyện. Mỗi lựa chọn quan trọng được nối với phản ứng của nhân vật và lời giải thích đã biên soạn, giúp làm rõ quan hệ giữa hành động, phản ứng và lý do. Lịch sử tương tác được dùng để người lớn xem lại quá trình tham gia, trao đổi cùng trẻ và chuẩn bị hoạt động tiếp theo.

Bear Buddy có hai nhóm người dùng chính. Primary user là trẻ trực tiếp trải nghiệm câu chuyện. Secondary user là phụ huynh hoặc giáo viên lựa chọn nội dung, cấu hình hỗ trợ và xem lại phiên học. Trong báo cáo, caregiver được dùng để gọi chung người lớn đồng hành; quyền truy cập cụ thể của phụ huynh và giáo viên được đặc tả tại Chương 3.

AI được dự kiến sử dụng ở hai phạm vi: hỗ trợ phụ huynh tìm câu chuyện phù hợp với mong muốn hoặc lịch sử tương tác; và hỗ trợ tương tác giọng nói tại tình huống E. Tình huống E là nhãn công việc chưa được đặc tả đầy đủ, vì vậy báo cáo giữ nội dung này trong phạm vi thiết kế dự kiến, cần chốt ở Chương 4 và Chương 6. Luồng học cốt lõi vẫn phải có cách tham gia bằng thao tác chạm và nội dung chuẩn bị sẵn khi chức năng giọng nói không được sử dụng.

## 1.2 Problem Statement Phát biểu bài toán

Một số trẻ tự kỷ gặp khó khăn khi diễn giải những thông tin xã hội không được nói trực tiếp, chẳng hạn ý nghĩa của nét mặt, giọng điệu, lượt hội thoại hoặc lý do một người phản ứng với hành động của mình. Trong các tình huống như chờ đến lượt, làm quen bạn mới, xin tham gia trò chơi hoặc nhờ giúp đỡ, việc biết các từ riêng lẻ chưa chắc đủ để hiểu toàn bộ bối cảnh. Tài liệu của NIH ghi nhận sự đa dạng về giao tiếp và những khó khăn có thể xuất hiện khi hiểu tín hiệu giao tiếp tinh tế. [NIH về tự kỷ](https://health.nih.gov/health-topics-a-z/autism)

Giả thuyết vấn đề của nhóm là trong một số gia đình hoặc lớp học, việc hỗ trợ hiện nay chủ yếu dựa trên lời giải thích tại thời điểm tình huống xảy ra. Những lời giải thích này có thể rời rạc, khác nhau giữa người hỗ trợ và khó xem lại. Người lớn cũng không thể giải thích mọi tín hiệu ngay khi trẻ cần. Đây là giả thuyết để nghiên cứu yêu cầu, chưa phải kết luận từ khảo sát người dùng của Bear Buddy.

Từ giả thuyết đó, nhóm xác định ba khoảng trống cần kiểm chứng. Trẻ cần một cách tìm hiểu tình huống có cấu trúc và có thể xem lại. Người lớn cần nội dung chuẩn bị sẵn để hỗ trợ nhất quán hơn. Đồng thời, phụ huynh hoặc giáo viên cần nhìn thấy quá trình trẻ lựa chọn và tiếp nhận giải thích, thay vì chỉ biết trẻ đã hoàn thành bao nhiêu câu chuyện.

Giải pháp đề xuất là chuyển các tình huống xã hội phổ biến thành câu chuyện tương tác được chuẩn bị trước. Trẻ được tiếp cận từng phần của bối cảnh, quan sát những cách phản hồi có thể xảy ra và thử lại với sự hỗ trợ phù hợp. Các phản ứng trong truyện là diễn biến của kịch bản cụ thể; chúng không đại diện cho quy luật rằng một hành động luôn tạo ra cùng một cảm xúc hoặc phản ứng ở mọi người.

Thách thức thiết kế của Bear Buddy là giúp trẻ tập trung vào nội dung xã hội trong khi vẫn hiểu cách sử dụng giao diện. Nếu thao tác quá phức tạp, lời giải thích quá trừu tượng hoặc âm thanh và chuyển động cạnh tranh với nội dung chính, ứng dụng có thể tạo thêm rào cản. Vì vậy, bài toán bao gồm cả nội dung câu chuyện, trải nghiệm tương tác và cách người lớn hỗ trợ trẻ.

## 1.3 Goal Mục tiêu của đề tài

Mục tiêu tổng quát của Bear Buddy là xây dựng một công cụ giúp trẻ chuẩn bị và khám phá các tình huống xã hội thường ngày trong một trải nghiệm có cấu trúc, dễ dự đoán và có thể lặp lại, đồng thời giúp phụ huynh hoặc giáo viên lựa chọn và xem lại hoạt động.

Các mục tiêu cụ thể gồm:

- Tổ chức thư viện tình huống để người lớn tìm và lựa chọn nội dung theo nhu cầu thực tế.
- Trình bày bối cảnh bằng hình ảnh, câu ngắn và lời kể, có tùy chọn phù hợp với khả năng tiếp nhận của trẻ.
- Làm rõ những tín hiệu xã hội liên quan và mối liên hệ Action → Reaction → Why trong từng kịch bản.
- Cho phép lựa chọn, quan sát, nhận giải thích, nghe lại, thử lại và tạm dừng với mức hỗ trợ phù hợp.
- Ghi nhận diễn biến phiên học để phụ huynh hoặc giáo viên xem lại và lập kế hoạch tiếp theo.
- Tách trải nghiệm học của trẻ khỏi các chức năng quản lý của người lớn.
- Tích hợp onboarding, accessibility, hỗ trợ người dùng, cài đặt, thông báo và xử lý trạng thái hệ thống thành những phần của trải nghiệm sản phẩm.
- Xác định phạm vi AI có ích cho việc chọn truyện hoặc thực hành tình huống, kèm cách tham gia thay thế và quản lý dữ liệu phù hợp.

Trong phạm vi đồ án, mức đạt được được đánh giá trước hết bằng khả năng sử dụng và mức đáp ứng yêu cầu: người dùng có tìm được nội dung, hiểu thao tác, tham gia câu chuyện và xem lại thông tin hay không. Các chỉ số như số lần thử, số câu chuyện hoàn thành hoặc lựa chọn trong app chỉ mô tả tương tác. Chúng không được dùng riêng lẻ để suy ra mức ASD, năng lực tổng thể hoặc hiệu quả can thiệp của sản phẩm.

## 1.4 Subjects and Scope Đối tượng và phạm vi

### 1.4.1 Đối tượng theo hồ sơ năng lực phát triển

Bear Buddy ưu tiên thiết kế cho trẻ có thể nhận biết nhân vật và hoạt động quen thuộc qua hình ảnh; tiếp nhận câu ngắn hoặc hướng dẫn từng bước khi có hỗ trợ; và thể hiện lựa chọn bằng chạm, chỉ hoặc phương thức giao tiếp quen thuộc. Khả năng đọc độc lập và nói câu đầy đủ không phải điều kiện mặc định để tham gia luồng cốt lõi.

Nhóm mô tả mức phù hợp bằng hồ sơ nhiều chiều: hiểu ngôn ngữ, hiểu hình ảnh, biểu đạt nhu cầu, theo dõi chuỗi sự kiện, chú ý, thao tác, cảm giác và mức hỗ trợ. Tuổi theo năm có thể được dùng làm thông tin bối cảnh nếu cần, nhưng không thay thế hồ sơ này. Báo cáo không quy đổi các năng lực đó thành một “tuổi phát triển” chung và không tự gán mức ASD. Persona mô phỏng được trình bày ở mục 2.4.

Phụ huynh và giáo viên là người sử dụng đồng hành. Phụ huynh quản lý hoạt động của trẻ trong phạm vi quyền được cấp; giáo viên hỗ trợ lựa chọn và sử dụng nội dung theo quan hệ truy cập được xác nhận. Việc chuyển giữa hai vai trò không mặc nhiên cho phép chia sẻ hồ sơ trẻ.

### 1.4.2 Phạm vi chức năng dự kiến

Phạm vi dưới đây giữ các nhóm chức năng của đề tài. Mức ưu tiên MoSCoW và acceptance criteria cho từng chức năng cần được thống nhất trong Chương 3 trước khi nghiệm thu hiện thực.

| Nhóm chức năng | Nội dung trong phạm vi |
|---|---|
| Thư viện tình huống | Danh sách, chủ đề, tìm kiếm hoặc lọc, chi tiết truyện và Most popular social stories. “Phổ biến” cần có chỉ số và khoảng thời gian rõ ràng; dữ liệu demo phải được phân biệt với thống kê thực tế. |
| Hình thức tương tác | Trắc nghiệm lựa chọn; kéo thả hoặc sắp xếp hành động; chạm chọn nhân vật hoặc thành phần trong cảnh; tương tác giọng nói; nhận biết cảm xúc; sắp xếp chuỗi tình huống. Đây là các phương án được giữ để so sánh, chưa mặc định phải triển khai đồng thời. |
| Review và kế hoạch | Xem lại lựa chọn và các lần tham gia; chọn câu chuyện tiếp theo; lập lịch hoạt động. |
| AI hỗ trợ phụ huynh | Gợi ý câu chuyện từ thư viện dựa trên mục tiêu phụ huynh cung cấp hoặc lịch sử được phép sử dụng; giải thích lý do gợi ý. |
| AI và giọng nói tại tình huống E | Giữ trong phạm vi dự kiến; cần chốt nội dung, loại phát ngôn, giới hạn phản hồi và phương án thay thế. |
| Tài khoản và liên kết | Đăng nhập, phân quyền, kết nối trẻ với phụ huynh; quyền giáo viên được mô tả riêng nếu triển khai. |
| Lưu trữ | SQLite theo chiến lược cục bộ và trao đổi dữ liệu được đặc tả tại Chương 6; không suy ra rằng SQLite tự giải quyết đồng bộ giữa thiết bị. |
| Onboarding và Introduction | Bắt buộc: giới thiệu sản phẩm, hướng dẫn người lớn, thiết lập hồ sơ và hỗ trợ hoạt động đầu tiên. |
| Accessibility | Bắt buộc: font scaling, màu sắc, tương phản, kích thước thành phần, touch target, ngôn ngữ và điều khiển âm thanh theo phạm vi đã đặc tả. |
| Privacy và Security | Quản lý truy cập, dữ liệu hồ sơ, lịch sử, microphone và thông tin gửi đến dịch vụ ngoài. |
| Feedback và Support | Bắt buộc: Help/FAQ, liên hệ hỗ trợ, báo lỗi và gửi phản hồi. |
| Trạng thái hệ thống | Error, Loading, Empty States; thông báo dễ hiểu, retry và duy trì bối cảnh khi có thể. |
| Settings và Notification | Tùy chọn tài khoản, trải nghiệm và accessibility; các loại nhắc lịch, thông báo và quyền kiểm soát của người lớn. |

### 1.4.3 Phạm vi sử dụng và giới hạn

Bear Buddy được định hướng sử dụng tại nhà hoặc môi trường học tập với người lớn chuẩn bị và hỗ trợ theo nhu cầu. Ứng dụng giúp chuẩn bị tình huống; sự hiện diện của nội dung số không thay thế giám sát cần thiết ngoài đời.

Nền tảng mobile, phiên bản hệ điều hành tối thiểu, mô hình một hoặc nhiều thiết bị và phạm vi nội dung offline chưa được chốt trong phần này. Những quyết định đó phải được ghi thống nhất tại Chương 3 và Chương 6. Bộ nội dung ban đầu được đề xuất bằng tiếng Việt; cấu trúc hỗ trợ thêm ngôn ngữ được thiết kế để có thể mở rộng, còn số ngôn ngữ thực tế thuộc phạm vi triển khai.

## 1.5 User Flow Overview Tổng quan luồng sử dụng

Luồng tổng quan được giữ như định hướng ban đầu: cha mẹ chọn một câu chuyện → trẻ tham gia → nắm bắt context → lựa chọn cách giải quyết tình huống → mỗi lựa chọn nhận một lời giải thích → lặp lại hoặc tiếp tục → cha mẹ review cách trẻ đã tham gia.

Luồng này được cụ thể hóa thành sáu bước:

1. Người lớn hoàn thành onboarding, chọn hồ sơ trẻ và thiết lập hỗ trợ cần thiết.
2. Người lớn xem thư viện hoặc gợi ý, đọc trước mục tiêu và nội dung rồi chọn câu chuyện.
3. Trẻ xem cảnh, nghe lời kể hoặc đọc câu ngắn để biết ai đang tham gia, điều gì đang xảy ra và nhiệm vụ hiện tại.
4. Trẻ dự đoán hoặc chọn một phản hồi bằng hình thức tương tác đã được thiết kế cho hoạt động đó.
5. Ứng dụng thể hiện phản ứng của nhân vật, giải thích lý do và cho phép nghe lại, thử lựa chọn khác, chuyển cảnh hoặc nghỉ. Với tình huống E, AI/voice chỉ tham gia theo giới hạn đã đặc tả.
6. Người lớn xem lại lựa chọn và lời giải thích của đúng phiên học, trao đổi cùng trẻ và điều chỉnh kế hoạch.

Core learning loop của Bear Buddy là Understand → Predict → Choose → Observe → Understand Why → Repeat. Việc lặp lại là tùy chọn học tập; trẻ có thể dừng mà không bị mất điểm hoặc chịu hình phạt tương tác.

## 1.6 Định hướng thiết kế lấy người dùng làm trung tâm

Các quyết định thiết kế được tổ chức theo chuỗi User Characteristics → UX Concerns → UX Principles → Design Decisions. Hồ sơ người dùng và persona ở Chương 2 cung cấp đầu vào; Chương 5 giải thích cách chuyển chúng thành giao diện. Dữ liệu thu thập trong nghiên cứu và thử prototype được dùng để cập nhật cả hồ sơ, yêu cầu và thiết kế, thay vì chỉ xác nhận lựa chọn ban đầu. Cách làm này phù hợp với khuyến nghị đưa người dùng vào quá trình thiết kế từ sớm của W3C. [W3C về sự tham gia của người dùng](https://www.w3.org/WAI/planning/involving-users/)

Trong bản đặc tả hiện tại, các persona và một số nhu cầu sản phẩm là giả định được công khai để kiểm chứng. Kết quả phân tích tài liệu và ứng dụng liên quan được phân biệt với kết quả phỏng vấn hoặc quan sát trực tiếp, nhằm giữ tính truy vết của lập luận thiết kế.


# Chương 2 Background and Related Work

## 2.1 Đặc điểm của nhóm người dùng mục tiêu

### 2.1.1 Trẻ em và sự khác biệt trong phát triển

Bear Buddy phục vụ trẻ đang phát triển về thể chất, nhận thức, ngôn ngữ, cảm xúc và xã hội. Tuy nhiên, “trẻ em” không phải một nhóm người dùng đồng nhất. Một trẻ 3 tuổi và một trẻ 12 tuổi có thể có trải nghiệm, mức tự lập và nhu cầu hỗ trợ rất khác nhau. Ngay trong cùng độ tuổi, khả năng tiếp nhận nội dung và sử dụng thiết bị cũng có thể khác nhau.

Nhóm giữ tám khía cạnh để tìm hiểu: ngôn ngữ và đọc hiểu; chú ý; tư duy trừu tượng; hiểu quan hệ nguyên nhân – kết quả; hiểu tình huống xã hội; thao tác với thiết bị; mức tự lập; và mức phụ thuộc vào phụ huynh hoặc giáo viên. Những khía cạnh này không được gộp thành một mức phát triển duy nhất. Trẻ có thể thao tác tốt nhưng cần hỗ trợ hiểu lời kể, hoặc hiểu bối cảnh quen thuộc nhưng khó chọn trên giao diện có nhiều thành phần.

Vì vậy, độ phù hợp của Bear Buddy được mô tả bằng những việc trẻ có thể làm và những hỗ trợ giúp trẻ tham gia. Nhóm tránh suy luận năng lực còn lại từ một điểm mạnh hoặc khó khăn riêng lẻ. Các điều chỉnh về nội dung và giao diện được xem là giả thuyết cần thử với người dùng phù hợp.

### 2.1.2 Tự kỷ và sự đa dạng của hồ sơ năng lực

Rối loạn phổ tự kỷ, Autism Spectrum Disorder hoặc ASD, là một tình trạng phát triển thần kinh. Theo cách mô tả hiện hành, hai nhóm đặc điểm cốt lõi liên quan đến giao tiếp và tương tác xã hội, cùng các kiểu hành vi hoặc sở thích hạn chế, lặp lại; khác biệt cảm giác có thể thuộc nhóm thứ hai. Khả năng ngôn ngữ, trí tuệ và nhu cầu hỗ trợ đi kèm cần được mô tả riêng. Chẩn đoán và mức hỗ trợ là vấn đề đánh giá chuyên môn. [CDC về tiêu chí chẩn đoán](https://www.cdc.gov/autism/hcp/diagnosis/index.html)

Một số trẻ có thể đồng thời gặp khó khăn về chú ý, tăng hoạt động hoặc học tập; các đặc điểm đi kèm không xuất hiện giống nhau ở mọi trẻ. Báo cáo sử dụng ngôn ngữ mô tả cụ thể thay cho cách gọi gộp như “hành vi bất thường” hoặc “trí tuệ kém”. [CDC về các biểu hiện có thể gặp](https://www.cdc.gov/autism/signs-symptoms/index.html)

Điểm quan trọng là tự kỷ là một phổ. Không có một mẫu “trẻ tự kỷ điển hình” để thiết kế giao diện áp dụng đồng loạt. Trong Bear Buddy, sáu chiều dưới đây được dùng để đặt câu hỏi nghiên cứu và mô tả hỗ trợ, không phải checklist chẩn đoán:

| Chiều xem xét | Khó khăn có thể xuất hiện và ý nghĩa đối với thiết kế |
|---|---|
| Social understanding | Một số trẻ cần hỗ trợ nhận ra nét mặt, giọng điệu, ý định hoặc thời điểm chờ, bắt chuyện, dừng lại và xin phép. Truyện cần cung cấp bối cảnh đủ rõ. |
| Communication | Trẻ có thể cần cách biểu đạt nhu cầu ngoài lời nói; câu mơ hồ, mỉa mai, nghĩa bóng hoặc hội thoại qua lại có thể cần giải thích. |
| Predictability | Việc biết trước bước tiếp theo có thể hữu ích với trẻ gặp khó khăn khi chuyển hoạt động hoặc đối diện thay đổi. |
| Sensory processing | Âm thanh, ánh sáng, chạm hoặc kích thích khác có thể được tiếp nhận khác nhau. Giao diện cần có tùy chọn và tránh mặc định chung. |
| Repetition and focused interests | Hoạt động lặp lại hoặc chủ đề yêu thích có thể là một phần trải nghiệm của trẻ; cần xem xét chúng trong việc lựa chọn nội dung. |
| Executive functioning and emotion regulation | Một số trẻ cần hỗ trợ chuyển hoạt động, theo dõi các bước, lập kế hoạch hoặc diễn đạt trạng thái cảm xúc. Đây là các nhu cầu hỗ trợ riêng, không phải kết luận từ chẩn đoán. |

Các chiều trên được giữ từ định hướng sản phẩm và cần xác nhận cho từng người dùng. Trong báo cáo, “Cảm nhận tín hiệu xã hội” là cách nhóm gọi ngắn mục tiêu hỗ trợ nhận biết và diễn giải thông tin xã hội trong bối cảnh. Thuật ngữ này không thay thế toàn bộ đặc điểm ASD và không hàm ý rằng các khác biệt cảm giác, giao tiếp hay điều chỉnh cảm xúc có cùng nguyên nhân hoặc cùng cách hỗ trợ.

### 2.1.3 Hồ sơ năng lực phát triển được ưu tiên

Thay vì neo sản phẩm vào một độ tuổi cố định, nhóm dùng hồ sơ tham chiếu có khả năng tiếp nhận tình huống cụ thể qua hình ảnh và câu ngắn, thực hiện từng thao tác đơn giản và tham gia với người lớn hỗ trợ khi cần. Hồ sơ này được thể hiện bằng persona Minh ở mục 2.4.

Những năng lực cần xem xét gồm nhận biết hình và hành động quen thuộc; hiểu hướng dẫn một bước; chọn giữa các phương án minh họa; theo dõi một chuỗi sự kiện ngắn khi được trình bày từng cảnh; biểu đạt chọn, dừng hoặc cần giúp; và thao tác chạm trên vùng đủ lớn. Chúng là điểm bắt đầu để thiết kế phiên bản đầu, không phải điều kiện phân loại y khoa hoặc tiêu chuẩn loại trừ trẻ khỏi mọi hình thức hỗ trợ.

## 2.2 Cơ sở của phương pháp social story

### 2.2.1 Nguồn gốc và mục đích

Social Stories do Carol Gray phát triển từ đầu thập niên 1990. Trong phần lịch sử trên website của mình, bà ghi nhận quá trình phát triển vào năm 1990 và cuốn sách đầu tiên được xuất bản năm 1993. [Lịch sử từ Carol Gray](https://carolgraysocialstories.com/social-stories/social-stories-overview/)

Phương pháp này hỗ trợ trao đổi thông tin xã hội theo cách cá nhân hóa, chính xác và tôn trọng trải nghiệm người đọc. Người viết tìm hiểu hoàn cảnh, chọn chủ đề liên quan và chuẩn bị văn bản hoặc hình ảnh phù hợp. Nội dung có thể mô tả một bối cảnh, kỹ năng, khái niệm hoặc thành công của người đọc. [Định nghĩa Social Story](https://carolgraysocialstories.com/social-stories/what-is-a-social-story/)

Trong Bear Buddy, cách tiếp cận này phục vụ ba mục đích dự kiến. Thứ nhất là cung cấp thông tin cụ thể về ai đang tham gia, điều gì diễn ra và vì sao. Thứ hai là hỗ trợ sự chuẩn bị trước tình huống mới, từ đó có thể giảm bối rối trong hoàn cảnh phù hợp. Thứ ba là giúp trẻ khám phá những cách phản hồi như chào hỏi, xếp hàng, nhờ hỗ trợ hoặc chuẩn bị đi khám. Những mục đích đó là định hướng nội dung; kết quả đối với từng trẻ cần được đánh giá, không được mặc định.

### 2.2.2 Cấu trúc và cách sử dụng ngôn ngữ

Một câu chuyện cần có tiêu đề thể hiện chủ đề, mở đầu giới thiệu bối cảnh, phần thân cung cấp thông tin và kết thúc nhắc lại ý chính. Nội dung cần xem xét các câu hỏi ai, ở đâu, khi nào, điều gì, như thế nào và vì sao. Bộ tiêu chí Social Stories 10.4 phân biệt câu mô tả và câu hướng dẫn nhẹ nhàng; số câu mô tả ít nhất gấp bốn lần câu hướng dẫn, với tối đa một câu hướng dẫn người đọc trong mỗi truyện. Tiêu chí còn yêu cầu chú ý đến việc ghi nhận điểm mạnh, rà soát và theo dõi cách sử dụng. [Social Stories 10.4 Criteria](https://carolgraysocialstories.com/wp-content/uploads/2023/11/2023-Social-Stories-10.4-Criteria-1.pdf)

Để giữ cách phân tích nội dung của đề tài, báo cáo sử dụng bốn nhãn chức năng diễn đạt dưới đây. Chúng giúp người biên soạn kiểm tra ý nghĩa câu, không được xem là bốn loại câu chính thức thay thế phân loại của phiên bản 10.4.

| Chức năng diễn đạt | Cách dùng trong nội dung Bear Buddy |
|---|---|
| Mô tả Descriptive | Cung cấp thông tin cụ thể về người, nơi, thời gian và sự kiện; ví dụ lớp có một hoạt động tham quan đã được thông báo. |
| Quan điểm hoặc cảm xúc Perspective | Mô tả cảm xúc của chính nhân vật hoặc khả năng người khác có cảm xúc nào đó khi có căn cứ; tránh khẳng định suy nghĩ không quan sát được như một sự thật. |
| Gợi ý hành động Directive or Coaching | Đề xuất cách phản hồi nhẹ nhàng và phù hợp hoàn cảnh, chẳng hạn nhờ người lớn giúp; không dùng mệnh lệnh ép trẻ thực hiện. |
| Khẳng định hoặc củng cố Affirmative | Nhắc lại một thông tin có căn cứ hoặc ghi nhận điều trẻ đã làm; tránh bảo đảm tuyệt đối rằng mọi trải nghiệm sẽ an toàn, dễ chịu hoặc thành công. |

### 2.2.3 Quy trình chuẩn bị và cá nhân hóa nội dung

Quy trình nội dung đề xuất của Bear Buddy bắt đầu từ một hoàn cảnh thực tế do người lớn cung cấp. Người biên soạn xác định thông tin trẻ đã biết, thông tin còn thiếu, hình thức giao tiếp và hỗ trợ phù hợp. Sau đó, nhóm soạn nội dung, chọn hình và lời kể, kiểm tra tính chính xác của bối cảnh rồi rà soát với người có hiểu biết về trẻ khi có điều kiện.

Các tình huống có thể được cá nhân hóa bằng nhân vật, cách gọi, ảnh địa điểm hoặc vật dụng quen thuộc và cách diễn đạt phù hợp. Nội dung cần cho phép trẻ xem lại trước khi tình huống diễn ra. Khi sử dụng, người lớn quan sát mức phù hợp và có thể dừng hoặc điều chỉnh; sự không phù hợp của truyện không được quy thành lỗi của trẻ.

Mỗi phiên bản cần có người chịu trách nhiệm nội dung, nguồn ảnh và âm thanh, ngày cập nhật và mã phiên bản. Khi lời giải thích hoặc nhánh truyện thay đổi, lịch sử phiên học vẫn cần chỉ ra phiên bản trẻ đã trải nghiệm. Đặc tả dữ liệu và cơ chế lưu được trình bày ở Chương 6.

### 2.2.4 Ví dụ minh họa Khi đi khám bác sĩ

Ví dụ sau do nhóm biên soạn cho một bối cảnh giả định có mẹ đi cùng. Nội dung giữ mục đích chuẩn bị khám, làm quen dụng cụ, diễn đạt cảm xúc, sử dụng đồ chơi quen thuộc và có người lớn hỗ trợ. Câu chuyện cần được điều chỉnh theo lần khám thật và rà soát trước khi sử dụng.

> Thỉnh thoảng, tôi đến phòng khám để bác sĩ kiểm tra sức khỏe.
>
> Trong lần khám này, mẹ đi cùng tôi.
>
> Bác sĩ có thể dùng ống nghe để nghe tim tôi.
>
> Một số dụng cụ có thể có cảm giác mát hoặc lạ khi chạm vào cơ thể.
>
> Tôi có thể cảm thấy tò mò, lo lắng hoặc có cảm giác khác.
>
> Mẹ có thể giúp tôi hỏi về bước khám tiếp theo.
>
> Tôi có thể cầm đồ chơi yêu thích hoặc báo cho mẹ khi tôi cần được giúp.
>
> Những điều diễn ra trong lần khám sẽ được người lớn giải thích thêm khi cần.

Các câu về địa điểm và dụng cụ thực hiện chức năng mô tả; câu về trạng thái của người kể giữ chức năng cảm xúc; câu về đồ chơi và báo nhu cầu là gợi ý hành động. Thông tin mẹ đi cùng được gắn với lần khám cụ thể. Cách viết này giữ tinh thần hỗ trợ của ví dụ và tránh lời bảo đảm tuyệt đối như “bố mẹ sẽ luôn ở bên” hay “mọi chuyện sẽ ổn”. Đây là minh họa cách biên soạn, chưa phải xác nhận truyện đã đáp ứng đầy đủ bộ tiêu chí.

### 2.2.5 Cách Bear Buddy vận dụng và giới hạn bằng chứng

Bear Buddy giữ ba định hướng của nội dung đã đề xuất: cá nhân hóa theo hoàn cảnh, trình bày trực quan để dễ hình dung và xem lại, đồng thời tôn trọng người học. Trẻ được giúp hiểu thông tin và diễn đạt nhu cầu; việc tham gia không bị biến thành yêu cầu phải tuân theo một cách cư xử duy nhất.

Ứng dụng tổ chức hai lớp nội dung: câu chuyện cung cấp thông tin và hoạt động tương tác đi kèm. Câu hỏi, kéo thả, chọn nhân vật, nhận biết cảm xúc, sắp xếp chuỗi và voice là các hình thức luyện tập được nhóm xem xét. Truyện phân nhánh hoặc trò chơi bổ sung không tự động trở thành Social Story đáp ứng bộ tiêu chí gốc. Mỗi nội dung cần được đánh giá theo phạm vi tuyên bố của nó.

Các lợi ích học tập chưa được mặc định cho Bear Buddy. Nghiên cứu ASSSIST2 trên 249 trẻ tự kỷ từ 4 đến 11 tuổi tại 87 trường ở Anh không tìm thấy cải thiện có ý nghĩa thống kê trên kết quả chính về đáp ứng xã hội sau sáu tháng, trong khi ghi nhận lợi ích ở mục tiêu cá nhân hóa. Kết quả của một nghiên cứu ở trường học không trực tiếp chứng minh hiệu quả cho app, nhưng giúp nhóm giới hạn tuyên bố và chú ý đến mục tiêu cụ thể. [Báo cáo nghiên cứu ASSSIST2](https://www.ncbi.nlm.nih.gov/books/NBK606426/)

## 2.3 Học qua hình ảnh lời kể và tương tác

### 2.3.1 Hình ảnh và biểu diễn cụ thể

Trong thiết kế đề xuất, hình ảnh thể hiện nhân vật, đồ vật, hành động và vị trí liên quan đến bối cảnh. Mục đích là giúp người dùng có thêm cách tiếp nhận thông tin khi đọc chữ chưa thuận lợi. Nhóm không giả định mọi trẻ tự kỷ đều là “người học bằng hình ảnh”. Mức độ hữu ích của ảnh chụp, minh họa và biểu tượng cần được thử theo hồ sơ người dùng.

Hình ảnh cần nhất quán giữa các cảnh, có trọng tâm và tránh chi tiết trang trí cạnh tranh với tín hiệu cần hiểu. Những thông tin không thể suy ra chắc chắn từ nét mặt cần được bổ sung bằng bối cảnh hoặc lời kể. W3C cũng khuyến nghị nội dung rõ, hình ảnh dễ hiểu và cách trình bày có phân tách để hỗ trợ khả năng hiểu. [W3C về nội dung dễ hiểu](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o3-clear-content/)

### 2.3.2 Câu ngắn và lời kể

Câu ngắn, từ cụ thể và hướng dẫn từng bước giúp nhóm giảm lượng ngôn ngữ phải xử lý trong một thời điểm. Lời kể cung cấp một kênh tiếp nhận bổ sung; chữ vẫn được giữ để hỗ trợ người cần đọc hoặc không dùng âm thanh. Narration, text-to-speech và AI hội thoại là các chức năng khác nhau, cần được phân biệt trong đặc tả.

Người dùng hoặc caregiver có thể nghe lại, giảm hoặc tắt âm thanh phù hợp. Âm thanh của cảnh cũ phải dừng khi chuyển sang cảnh mới hoặc khi lựa chọn phát lại thay thế nó. Việc nghe lời kể không đồng nghĩa trẻ cần trả lời bằng giọng nói. Bản dịch và lời đọc ở ngôn ngữ khác cần được rà soát về ý nghĩa xã hội, không chỉ chuyển từng từ.

### 2.3.3 Tương tác và quan hệ nguyên nhân kết quả

Tương tác cho phép trẻ lựa chọn và quan sát diễn biến của một kịch bản. Bear Buddy dự kiến làm rõ Action → Reaction → Why: lựa chọn nào được thực hiện, nhân vật phản ứng ra sao và vì sao phản ứng đó có thể xuất hiện trong hoàn cảnh này. Phần giải thích tránh suy đoán tuyệt đối cảm xúc hoặc ý định của người khác.

Các phương án trắc nghiệm, chạm chọn, nhận biết cảm xúc, kéo thả, sắp xếp hành động, sắp xếp tình huống và voice đều được giữ để đánh giá. Với cùng mục tiêu, nhóm ưu tiên phương án ít tạo thêm yêu cầu đọc, vận động hoặc biểu đạt không cần thiết. Kéo thả có thể có cách thay bằng chạm chọn thứ tự; voice có thể đi kèm lựa chọn hình. Hình thức cuối cùng được chốt sau thử nghiệm thiết kế và ghi ở Chương 4.

### 2.3.4 Phối hợp kênh và những giới hạn cần xem xét

Đa phương thức không có nghĩa mọi kênh đều phải phát đồng thời. Một cảnh có thể cung cấp ảnh và câu ngắn, còn âm thanh được điều khiển theo nhu cầu. Hiệu ứng chỉ được dùng khi giúp định hướng, thể hiện trạng thái hoặc giải thích diễn biến.

Việc trẻ chọn một phương án trong app chưa chứng minh trẻ đã hiểu lý do hay có thể vận dụng ngoài đời. Replay, retry và trao đổi với người lớn giúp tạo cơ hội xem lại; đánh giá sự hiểu cần gắn với nhiệm vụ và phương thức giao tiếp phù hợp. Khả năng chuyển kiến thức sang tình huống khác vẫn là điểm cần nghiên cứu, không phải kết quả được khẳng định trong đồ án.

## 2.4 Personas và hồ sơ năng lực phát triển

Ba persona dưới đây là mô phỏng phục vụ thiết kế. Tên, hoàn cảnh và năng lực được xây dựng để kiểm tra tính nhất quán của giải pháp, không đại diện cho người tham gia nghiên cứu thực tế hoặc cho toàn bộ người tự kỷ. Chúng cần được sửa khi có dữ liệu phỏng vấn, quan sát và thử prototype.

### 2.4.1 Persona PERS01 Minh người trải nghiệm câu chuyện

Minh là một trẻ tự kỷ giả định đang hình thành khả năng hiểu các tình huống xã hội cụ thể qua hình ảnh, câu ngắn và người lớn hỗ trợ. Hồ sơ được neo theo năng lực chức năng, không gán tuổi theo năm, tuổi phát triển, IQ hay mức ASD. Minh thích những nhân vật và đồ vật quen thuộc, chủ động chạm để khám phá và thường muốn nghe lại một đoạn mình quan tâm.

| Chiều năng lực | Mô tả của persona mô phỏng | Hỗ trợ thiết kế dự kiến |
|---|---|---|
| Hiểu ngôn ngữ | Hiểu câu ngắn trong hoàn cảnh quen thuộc; thuận lợi hơn khi chỉ có một hướng dẫn mỗi lần. | Tách nhiệm vụ thành từng bước, có hình minh họa và phát lại lời kể. |
| Biểu đạt và giao tiếp | Có thể chỉ hoặc chạm lựa chọn; đôi khi dùng từ hoặc cụm ngắn; không phải lúc nào cũng muốn nói. | Lựa chọn hình luôn khả dụng; không dùng voice như điều kiện duy nhất. |
| Hiểu hình ảnh | Nhận ra một số đồ vật, người và hoạt động quen thuộc; biểu tượng trừu tượng có thể chưa rõ nghĩa. | Dùng biểu diễn trực tiếp, icon có nhãn hoặc hướng dẫn khi cần. |
| Đọc hiểu | Chưa dựa ổn định vào việc đọc độc lập để thực hiện toàn bộ hoạt động. | Câu ngắn, lời kể tùy chọn, không nhúng chữ quan trọng vào ảnh. |
| Theo dõi câu chuyện | Theo dõi được một chuỗi ngắn khi trình bày từng cảnh; có thể cần nhắc lại cảnh trước. | Giữ nhân vật và bố cục nhất quán, có Back và Replay. |
| Dự đoán và hiểu nguyên nhân | Có thể nối hành động với kết quả cụ thể khi được minh họa; cần hỗ trợ với suy nghĩ hoặc lý do ngầm. | Thể hiện phản ứng rồi giải thích bằng bối cảnh, không chỉ chấm đáp án. |
| Chú ý và chuyển hoạt động | Dễ rời nhiệm vụ khi có nhiều chi tiết cạnh tranh; có thể cần báo trước bước tiếp theo. | Một mục tiêu chính mỗi màn hình, progress dễ hiểu và chuyển cảnh chủ động. |
| Thao tác vận động | Chạm được mục tiêu lớn; thao tác giữ và kéo chính xác chưa ổn định. | Vùng chạm lớn, khoảng cách rõ và phương án chạm thay kéo thả. |
| Tiếp nhận cảm giác | Trong mô phỏng, âm thanh chồng nhau và chuyển động bất ngờ làm Minh khó tiếp tục. | Điều khiển âm thanh, ngăn chồng tiếng và tùy chọn giảm chuyển động. |
| Điều chỉnh và diễn đạt nhu cầu | Có thể rời màn hình hoặc tìm người lớn khi khó chịu; cần một cách rõ ràng để báo nghỉ hoặc cần giúp. | Nút Nghỉ và Cần giúp ở vị trí ổn định; hỗ trợ tiếp tục sau đó. |
| Mức hỗ trợ | Người lớn giúp chọn truyện, giới thiệu buổi đầu và hỗ trợ khi Minh yêu cầu. | Child mode đơn giản, caregiver mode đảm nhiệm quản lý. |

Mục tiêu của Minh là biết chuyện gì sắp xảy ra, chọn cách tham gia, hiểu diễn biến và có thể yêu cầu trợ giúp. Khó khăn giả định của Minh gồm quá nhiều chữ, icon khó đoán, phản hồi không rõ và thao tác vô tình bị lưu như một quyết định có chủ đích. Thành công thiết kế được quan sát bằng việc Minh nhận ra bước tiếp theo, thể hiện được lựa chọn hoặc nhu cầu nghỉ và sử dụng hỗ trợ phù hợp; không đặt tốc độ hoàn thành làm mục tiêu duy nhất.

Kịch bản mô phỏng: trước một hoạt động chơi cùng bạn, người lớn chọn truyện “Xin tham gia trò chơi”. Minh xem ai đang chơi và trò chơi đang diễn ra thế nào, chọn một cách đề nghị, quan sát phản ứng trong truyện rồi nghe lý do. Minh có thể chọn lại hoặc nhờ người lớn giúp mà không bị mất điểm. Diễn biến này là kịch bản thiết kế, chưa phải kết quả sử dụng.

### 2.4.2 Persona PERS02 chị An phụ huynh đồng hành

Chị An là phụ huynh giả định muốn chuẩn bị cho con những tình huống cụ thể ở nhà và ngoài cộng đồng. Chị sử dụng điện thoại hằng ngày nhưng không muốn đọc tài liệu dài để bắt đầu một buổi học. Chị cần nội dung rõ mục tiêu, có thể xem trước và phù hợp với cách con giao tiếp.

Mục tiêu của chị là tìm truyện theo nhu cầu sắp tới, thiết lập hỗ trợ một lần rồi dùng lại, biết con đã thấy lời giải thích nào và chọn hoạt động tiếp theo. Những trở ngại giả định gồm thư viện khó tìm, không biết AI dựa vào đâu, biểu đồ quá trừu tượng và phải quản lý tài khoản trong khi trẻ đang cầm thiết bị.

Thiết kế cần cung cấp chi tiết truyện trước khi bắt đầu, phân biệt hồ sơ trẻ rõ ràng, lịch sử theo phiên và gợi ý AI có lý do. Chị quyết định câu chuyện nào được sử dụng; hệ thống không tự suy ra chẩn đoán hoặc tự lập kế hoạch bắt buộc từ lịch sử lựa chọn. Tiêu chí đánh giá gồm việc chị tìm và giải thích được lý do chọn truyện, hiểu bản ghi phiên và quản lý quyền dữ liệu.

### 2.4.3 Persona PERS03 cô Mai giáo viên hỗ trợ

Cô Mai là giáo viên giả định dùng câu chuyện để chuẩn bị một hoạt động trong lớp hoặc hỗ trợ một trẻ trước hoàn cảnh mới. Cô cần biết mục tiêu, phiên bản nội dung và cách giải thích mà gia đình đang sử dụng. Cô ưu tiên cách triển khai ngắn, rõ và có thể lặp lại.

Mục tiêu của cô là chọn nội dung đúng hoàn cảnh, hỗ trợ giao tiếp trong buổi học và trao đổi những quan sát cụ thể với phụ huynh. Trở ngại giả định gồm nhiều hồ sơ dễ nhầm, ngôn ngữ không thống nhất và quyền xem dữ liệu chưa rõ.

Nếu chức năng giáo viên được triển khai, hệ thống chỉ hiển thị hồ sơ được cấp quyền, ghi rõ trẻ đang được hỗ trợ và cho phép xem nội dung trong phạm vi đã xác nhận. Chức năng quản lý lớp hoặc chia sẻ liên tổ chức không được mặc nhiên suy ra từ persona này; phạm vi tài khoản giáo viên cần chốt ở Chương 3.

### 2.4.4 Giả định cần kiểm chứng từ personas

Nhóm cần kiểm tra liệu trẻ nhận ra các nút chính; số phương án minh họa phù hợp trong một cảnh; cách trẻ hiểu lời giải thích; cách yêu cầu nghỉ; và tác động của phát lại âm thanh. Với người lớn, cần xác nhận cách tìm truyện, mức chi tiết cần trong review và điều kiện chia sẻ hồ sơ. Persona giúp đặt những câu hỏi đó, không thay thế bằng chứng nghiên cứu.

## 2.5 Related Work Phân tích các giải pháp liên quan

### 2.5.1 Phương pháp đối chiếu

Phân tích dưới đây là desk research từ trang sản phẩm của nhà phát triển, kiểm tra ngày 03 tháng 11 năm 2026. Nó phản ánh chức năng được công bố, không phải kết quả thử app trực tiếp hay so sánh hiệu quả can thiệp. Tính năng không được đề cập trong nguồn được xem là chưa có đủ thông tin, không được kết luận là không tồn tại.

### 2.5.2 Pictello

Pictello của AssistiveWare cho phép tạo và chia sẻ truyện trực quan với ảnh, video, bản ghi âm và text-to-speech. Công cụ tổ chức câu chuyện theo từng trang và có những lựa chọn hỗ trợ truy cập. Bài học cho Bear Buddy là nội dung cá nhân hóa và sự liên kết giữa ảnh, chữ và lời kể có thể được tổ chức thành cấu trúc lặp lại dễ kiểm soát. Thông tin này không chứng minh mọi lựa chọn giao diện của Pictello phù hợp với persona Minh. [Trang sản phẩm Pictello](https://www.assistiveware.com/products/pictello)

### 2.5.3 Social Stories Creator and Library

Ứng dụng của Touch Autism cung cấp công cụ tạo truyện bằng ảnh, chữ và âm thanh, đồng thời có thư viện nội dung và chức năng chia sẻ theo phiên bản sản phẩm. Cách giới thiệu nội dung trước khi chọn và khả năng phát lại là điểm tham khảo cho trải nghiệm caregiver. Bear Buddy cần đặc tả riêng việc ghi nhận lựa chọn và lời giải thích trong truyện tương tác; nguồn sản phẩm chưa đủ để kết luận các tính năng đó có hay không ở giải pháp đối chiếu. [Trang sản phẩm Touch Autism](https://touchautism.com/app/social-stories-creator-library/)

### 2.5.4 Choiceworks

Choiceworks của Bee Visual là công cụ trực quan hỗ trợ các hoạt động thường ngày, chờ đợi, cảm xúc và lựa chọn. Bài học thiết kế là cách biểu diễn một hoạt động thành những bước có thể theo dõi và cách người lớn chuẩn bị nội dung cho trẻ. Bear Buddy tập trung thêm vào việc khám phá một kịch bản xã hội và lý do của các phản ứng; đây là định hướng đề tài, không phải kết luận rằng Choiceworks thiếu toàn bộ khả năng đó. [Trang sản phẩm Bee Visual](https://www.beevisual.com/)

### 2.5.5 Tổng hợp định hướng từ related work

| Giải pháp | Chức năng được nguồn chính thức mô tả | Điều Bear Buddy cần nghiên cứu tiếp |
|---|---|---|
| Pictello | Tạo truyện trực quan, thêm ảnh/video/giọng nói, text-to-speech và chia sẻ. | Cách kết hợp bối cảnh cá nhân với lựa chọn, phản ứng và giải thích theo kịch bản. |
| Social Stories Creator and Library | Tạo, lưu, phát lại, dùng thư viện và chia sẻ truyện theo gói tính năng. | Cách caregiver tìm, xem trước và review chính xác phiên tương tác. |
| Choiceworks | Hỗ trợ trực quan cho hoạt động thường ngày, chờ, cảm xúc và lựa chọn. | Cách thể hiện tiến trình mà không tạo áp lực hoàn thành và cách nối các bước với lý do xã hội. |

Nhóm chọn hướng thiết kế kết hợp thư viện được chuẩn bị sẵn, trải nghiệm có nhịp do người dùng điều khiển, lời giải thích sau lựa chọn và công cụ review dành cho caregiver. Mức hữu ích của cách kết hợp này phải được kiểm tra; báo cáo chưa tuyên bố Bear Buddy vượt trội hơn các sản phẩm đối chiếu.

## 2.6 Requirements Elicitation và kế hoạch kiểm chứng

### 2.6.1 Bằng chứng hiện có và thông tin chưa được thu thập

Đầu vào hiện có gồm định hướng và nội dung do nhóm xác lập, tài liệu chính thức về ASD và Social Stories, cùng desk research ba giải pháp ở mục 2.5. Những đầu vào này giúp xác định câu hỏi nghiên cứu và ràng buộc ban đầu. Chưa có số lượng người tham gia, trích dẫn phỏng vấn, kết quả khảo sát hay quan sát sử dụng thực tế được báo cáo cho Bear Buddy.

Để đáp ứng phần requirements elicitation của đồ án, nhóm cần lưu bằng chứng cho những hoạt động thực sự thực hiện: nguồn đối chiếu, ngày xem xét, tiêu chí phân tích, ghi chép đã ẩn danh và cách kết quả được chuyển thành yêu cầu. Persona mô phỏng được giữ nhãn giả định cho đến khi được cập nhật bằng dữ liệu.

### 2.6.2 Hoạt động tìm hiểu người dùng dự kiến

Phỏng vấn phụ huynh hoặc giáo viên tập trung vào tình huống trẻ cần chuẩn bị, cách hỗ trợ hiện tại, nội dung hiệu quả hoặc khó dùng, điều kiện sử dụng thiết bị và thông tin người lớn muốn review. Quan sát nhiệm vụ với prototype tập trung vào cách người dùng hiểu và thao tác, không kiểm tra trẻ có “ngoan” hoặc đạt một chuẩn phát triển do app đặt ra hay không.

Khi có trẻ tham gia, hoạt động cần được giải thích phù hợp cách giao tiếp của trẻ, có sự đồng ý của người giám hộ và tôn trọng việc trẻ không muốn tiếp tục. Người hỗ trợ ghi rõ mức trợ giúp đã cung cấp. Các phiên có thể dừng bất kỳ lúc nào; không yêu cầu ghi âm hoặc ghi hình nếu điều đó không cần cho câu hỏi nghiên cứu và chưa có đồng ý phù hợp.

Các câu hỏi gợi ý cho người lớn gồm: tình huống nào cần chuẩn bị gần đây; cách giải thích hiện tại; trẻ dùng hình, chữ và lời nói ra sao; trẻ thể hiện cần nghỉ thế nào; điều gì khiến nội dung khó dùng; người lớn cần thấy gì sau phiên; thông tin nào không muốn gửi ra ngoài; và khi nào gợi ý AI thực sự hữu ích. Đây là kế hoạch câu hỏi, chưa phải dữ liệu trả lời.

### 2.6.3 Từ nhu cầu đến thiết kế

| Mã nhu cầu đề xuất | Nhu cầu cần kiểm chứng | Hướng thiết kế và đầu ra liên quan |
|---|---|---|
| UN01 | Hiểu bối cảnh trước khi lựa chọn. | Cảnh mở đầu rõ nhân vật và hoạt động; DD13–DD16. |
| UN02 | Tham gia khi chưa đọc độc lập. | Hình, câu ngắn, narration tùy chọn; DD7–DD12, DD20. |
| UN03 | Biết đang ở đâu và sắp làm gì. | Cấu trúc, control và progress nhất quán; DD2–DD6. |
| UN04 | Thể hiện lựa chọn mà không cần thao tác chính xác phức tạp. | Chạm, vùng lớn và phương án thay gesture; DD26–DD30. |
| UN05 | Hiểu lời giải thích và có thể xem lại. | Phản ứng, lý do, retry và replay; DD15–DD19. |
| UN06 | Kiểm soát mức kích thích và nhịp tham gia. | Điều khiển âm thanh, chuyển động, nghỉ; DD21–DD23, DD37. |
| UN07 | Người lớn tìm và xem trước nội dung phù hợp. | Thư viện và chi tiết truyện ở caregiver mode. |
| UN08 | Xem lại đúng hồ sơ và phiên bản nội dung. | Review theo phiên, liên kết quyền rõ, nội dung có phiên bản. |
| UN09 | Biết AI gợi ý dựa vào đâu và có thể chọn khác. | Giải thích gợi ý, caregiver quyết định; DD36, DD39. |
| UN10 | Trẻ có thể yêu cầu hỗ trợ hoặc dừng. | Nút Nghỉ và Cần giúp; DD37. |
| UN11 | Dữ liệu trẻ được sử dụng có mục đích rõ. | Thu thập tối thiểu, quản lý quyền; DD33–DD34. |
| UN12 | Có đường tiếp tục khi hệ thống gặp lỗi. | Giữ bối cảnh, retry và thay thế voice/AI; mục 5.6. |

Các mã UN là đầu vào nghiên cứu, chưa thay thế mã functional requirement hoặc use case ở Chương 3. Sau khi xác nhận, nhóm bổ sung mức ưu tiên, acceptance criteria và liên kết với màn hình, thành phần kiến trúc, test case. Quy trình cập nhật được thực hiện qua vòng lặp nghiên cứu → yêu cầu → prototype → đánh giá → điều chỉnh. W3C khuyến nghị kết hợp sự tham gia của người dùng với kiểm tra theo hướng dẫn accessibility, đồng thời tránh suy rộng phản hồi của một người cho toàn bộ nhóm. [W3C về nghiên cứu và đánh giá với người dùng](https://www.w3.org/WAI/planning/involving-users/)


# Chương 5 UI UX Design

## 5.1 Nguyên tắc thiết kế và UX Reasoning Framework

Thiết kế UX/UI của Bear Buddy được xây dựng theo chuỗi User Characteristics → UX Concerns → UX Principles → Design Decisions. Bốn tầng trả lời những câu hỏi khác nhau: người dùng có đặc điểm gì; đặc điểm đó có thể tạo trở ngại nào khi dùng app; trải nghiệm cần tuân theo nguyên tắc nào; và nguyên tắc được chuyển thành giao diện hoặc tương tác ra sao. Mục tiêu là làm rõ căn cứ của từng quyết định để nhóm có thể đánh giá và sửa khi có dữ liệu mới.

Các đặc điểm dưới đây là giả thuyết thiết kế dựa trên hồ sơ mục tiêu và nội dung nền tảng, chưa phải kết luận từ một mẫu người dùng Bear Buddy. Báo cáo giữ mã C1–C12, P1–P10 và DD1–DD36 của framework. Mã UX Concern được viết thành UXC1–UXC17 để phân biệt với Use Case ở Chương 3; số thứ tự và ý nghĩa được giữ nguyên.

### 5.1.1 Layer 1 User Characteristics

**C1 Khả năng xử lý thông tin vẫn đang phát triển.** Với hồ sơ mục tiêu, việc tiếp nhận đồng thời nhiều chữ, hình, control và thông tin xã hội có thể làm tăng yêu cầu xử lý. Thiết kế không mặc định trẻ có thể quét một giao diện phức tạp giống người lớn; câu chuyện cần được chia thành phần phù hợp với nhiệm vụ hiện tại.

**C2 Khả năng đọc và ngôn ngữ không đồng nhất.** Đọc và hiểu lời nói cần được xem xét riêng. Ngay cả khi trẻ đọc được một số từ, giao diện nhiều chữ vẫn có thể gây thêm trở ngại. Bear Buddy cung cấp hình ảnh và lời kể tùy chọn, đồng thời kiểm tra cách phối hợp các kênh.

**C3 Thông tin cụ thể có thể dễ tiếp cận hơn biểu diễn trừu tượng.** Icon, ẩn dụ và quy ước UI cần được học. Vì vậy, nhóm ưu tiên biểu diễn trực tiếp gắn với bối cảnh và không mặc định trẻ hiểu một biểu tượng chỉ vì người lớn thấy quen thuộc.

**C4 Người dùng có thể cần hỗ trợ hiểu thông tin xã hội ngầm.** Những thông tin như một người có thể cảm thấy gì, ý định nào được thể hiện, hành động gắn với phản ứng ra sao, vì sao phản ứng xuất hiện và điều gì có thể xảy ra tiếp theo cần được trình bày có căn cứ. Câu chuyện không dựa hoàn toàn vào việc trẻ tự suy luận các thông tin đó.

**C5 Người dùng có thể cần hỗ trợ dự đoán và xử lý thay đổi.** Khi bố cục, điều hướng hoặc cách thao tác thay đổi liên tục, trẻ phải học lại cách dùng app. Bear Buddy giữ cấu trúc nhất quán để sự thay đổi quan trọng nằm trong nội dung tình huống, còn giao diện cung cấp điểm tựa dễ nhận biết.

**C6 Mức chính xác khi thao tác cần được xem xét.** Với persona Minh, chạm vùng lớn thuận lợi hơn giữ và kéo chính xác. Vùng nhỏ, control sát nhau hoặc gesture phức tạp có thể tạo thao tác vô tình. Cần phân biệt khó khăn vận động với lựa chọn có chủ đích trong câu chuyện.

**C7 Trẻ có thể khám phá bằng cách chạm trực tiếp.** Những thành phần trông như có thể tương tác cần phản hồi đúng kỳ vọng. Hình trang trí và control phải có khác biệt đủ rõ để người dùng hiểu cách sử dụng.

**C8 Trẻ cần nhận ra phản hồi sau hành động.** Khi không thấy trạng thái thay đổi, trẻ có thể không biết hệ thống đã nhận lựa chọn và chạm tiếp. Phản hồi cần rõ, có ý nghĩa và không tạo tiếng động hoặc hiệu ứng thừa.

**C9 Một số người dùng có thể nhạy với kích thích cảm giác.** Màu, animation và âm thanh cần được lựa chọn theo mục đích. Nhiều kích thích hơn không mặc định tạo ra trải nghiệm phù hợp hơn; nhu cầu điều chỉnh được xem xét ở cấp người dùng.

**C10 Trẻ có thể cần lặp lại để củng cố hiểu biết.** Xem một tình huống một lần chưa chứng minh việc ghi nhớ hoặc vận dụng ở bối cảnh khác. Replay và retry được thiết kế như lựa chọn học tập, còn mức hữu ích cần đánh giá bằng cách tiếp nhận của trẻ.

**C11 Trẻ và caregiver có mục tiêu khác nhau.** Trẻ trải nghiệm và thực hành tình huống. Caregiver chọn nội dung, quản lý, xem lại, cấu hình và hỗ trợ. Hai nhóm được cung cấp cấu trúc tương tác phù hợp với nhiệm vụ riêng.

**C12 Bear Buddy xử lý dữ liệu nhạy cảm liên quan đến trẻ.** Hồ sơ, lịch sử lựa chọn, microphone, giọng nói và AI có thể liên quan đến thông tin cá nhân. Safety và privacy được đưa vào luồng UX, bao gồm những giải thích, quyền kiểm soát và lựa chọn cần có trước khi dữ liệu được sử dụng.

### 5.1.2 Layer 2 UX Concerns

| Mã | UX Concern | Khó khăn hoặc rủi ro cần giải quyết |
|---|---|---|
| UXC1 | Cognitive Overload | Quá nhiều thông tin hoặc thao tác cạnh tranh khiến trẻ dành công sức hiểu giao diện thay vì tình huống. |
| UXC2 | Reading Burden | Việc đọc trở thành rào cản đối với mục tiêu học nếu nội dung chỉ được truyền bằng chữ. |
| UXC3 | Abstraction Barrier | Icon, thuật ngữ và ẩn dụ đòi hỏi suy luận thêm trước khi hiểu cần làm gì. |
| UXC4 | Implicit Social Information | Bối cảnh chưa làm rõ cue, ý định có căn cứ, hệ quả và lý do nên có thể giữ nguyên khó khăn cần hỗ trợ. |
| UXC5 | Unpredictable Interaction | Cùng một thao tác có hành vi khác nhau hoặc điều hướng đổi liên tục làm mental model khó ổn định. |
| UXC6 | Loss of Orientation | Trẻ không rõ mình đang ở đâu, còn những bước nào và điều gì sắp xảy ra. |
| UXC7 | Accidental Interaction | Chạm nhầm hoặc gesture khó bị ghi nhận như quyết định có chủ đích. |
| UXC8 | Ambiguous Affordance | Chưa phân biệt được thành phần có thể bấm với phần trang trí. |
| UXC9 | Lack of Feedback | Không biết input đã được nhận nên lặp lại thao tác hoặc rời nhiệm vụ. |
| UXC10 | Sensory Overload | Âm thanh, chuyển động, màu hoặc hiệu ứng cạnh tranh với nội dung hoặc tạo khó chịu. |
| UXC11 | Punitive Learning Experience | Phản hồi chủ yếu là đúng/sai có thể tạo áp lực đoán đáp án và làm giảm việc khám phá lý do. |
| UXC12 | Memorization Without Understanding | Ghi nhớ phương án mà chưa hiểu vì sao hành động gắn với phản ứng trong bối cảnh; khó suy ra khả năng vận dụng. |
| UXC13 | Insufficient Repetition | Không thể replay, retry hoặc xem lại khi người dùng còn cần tiếp xúc với nội dung. |
| UXC14 | Context Switching | Modal, popup hoặc điều hướng không cần thiết làm đứt mạch truyện và mất bối cảnh. |
| UXC15 | Mixed Child and Caregiver Complexity | Cài đặt, quản lý và analytics xuất hiện trong luồng trẻ dù không phục vụ nhiệm vụ hiện tại. |
| UXC16 | Privacy and Safety Risk | Hồ sơ, voice, microphone và lịch sử bị thu thập hoặc chia sẻ quá mức cần thiết. |
| UXC17 | Too Much Complexity Too Early | Nhiều dạng tương tác, tín hiệu xã hội và AI voice được đưa vào cùng lúc trước khi người dùng quen cách dùng. |

### 5.1.3 Layer 3 UX Principles

**P1 Simple and Focused.** Bear Buddy giảm những yêu cầu xử lý không phục vụ nhiệm vụ hiện tại. Mỗi màn hình có trọng tâm để độ phức tạp giao diện không cạnh tranh với nội dung xã hội. Nguyên tắc giải quyết UXC1, UXC2, UXC14 và UXC17.

**P2 Predictable and Consistent.** Người dùng cần nhận ra vị trí hiện tại, thao tác khả dụng và bước tiếp theo. Control, nhãn và cấu trúc truyện giữ ổn định để hỗ trợ hình thành mental model. Nguyên tắc giải quyết UXC5, UXC6 và UXC14.

**P3 Concrete and Explicit.** Make the implicit explicit là định hướng cốt lõi: thông tin được thể hiện trực tiếp, gắn với bối cảnh và có căn cứ. Các quan hệ xã hội cần thiết cho việc hiểu tình huống được giải thích thay vì chỉ ngầm thể hiện. Nguyên tắc giải quyết UXC3, UXC4 và UXC12.

**P4 Explain, Don't Judge.** Mỗi lựa chọn là cơ hội tìm hiểu Action → Reaction → Why. Lời giải thích tập trung vào hoàn cảnh và khả năng phản hồi, giúp trẻ khám phá lý do thay vì chỉ ghi nhớ đáp án. Nguyên tắc giải quyết UXC11 và UXC12.

**P5 Multimodal and Accessible.** Hình ảnh, câu ngắn, lời kể và tương tác cung cấp những cách tiếp nhận hoặc biểu đạt có thể lựa chọn. Việc phối hợp kênh phải phù hợp người dùng; không mặc định phát tất cả cùng lúc. Nguyên tắc giải quyết UXC2 và UXC3.

**P6 Calm and Controllable.** Âm thanh và chuyển động có mục đích như định hướng chú ý, thể hiện trạng thái hoặc giải thích diễn biến. Trải nghiệm hướng đến Calm – Predictable – Controllable, với quyền điều chỉnh phù hợp của người dùng hoặc caregiver. Nguyên tắc giải quyết UXC10 và UXC1.

**P7 Immediate and Meaningful Feedback.** Tương tác có ý nghĩa cần được xác nhận bằng thay đổi trạng thái rõ ràng. Phản hồi không nhất thiết phải phóng đại hoặc có âm thanh; nó cần giúp hiểu điều vừa xảy ra. Nguyên tắc giải quyết UXC8 và UXC9.

**P8 Safe to Explore and Repeat.** Chu trình Choose → Observe → Understand → Retry được hỗ trợ mà không phạt mất điểm hoặc gán nhãn thất bại. Người dùng có thể nghe lại và thử khác khi còn muốn tham gia. Nguyên tắc giải quyết UXC11 và UXC13.

**P9 Forgiving Physical Interaction.** Giao diện thích ứng với cách trẻ cầm và chạm thiết bị, cung cấp control đủ lớn và phương án thay cho gesture khó. Nguyên tắc giải quyết UXC7 và UXC8.

**P10 Design for the Child Support the Caregiver.** Child mode tập trung vào câu chuyện; caregiver mode hỗ trợ lựa chọn, cấu hình và review. Phân tách này giảm phức tạp và hỗ trợ kiểm soát dữ liệu phù hợp. Nguyên tắc giải quyết UXC15 và một phần UXC16.

**P11 Privacy and Agency by Design bổ sung.** Trẻ và caregiver có cách hiểu, lựa chọn và dừng tương tác phù hợp. Dữ liệu chỉ được thu thập theo mục đích đã giải thích; quyền xem hồ sơ và voice được kiểm soát riêng. P11 bổ sung căn cứ trực tiếp cho UXC16 và quyền nghỉ, thay vì đặt toàn bộ privacy dưới nguyên tắc phân tách vai trò. Định hướng này tham chiếu yêu cầu bảo vệ dữ liệu, an toàn và minh bạch AI dành cho trẻ của UNICEF. [UNICEF Guidance on AI and Children](https://www.unicef.org/innocenti/reports/policy-guidance-ai-children)

### 5.1.4 Layer 4 Design Decisions

Các quyết định DD1–DD36 được giữ đủ, gồm hành vi cụ thể, chuỗi dẫn xuất và lý do. Chúng là đặc tả thiết kế cần kiểm tra, chưa phải báo cáo rằng tính năng đã hiện thực hoặc đã được chứng minh phù hợp với mọi trẻ.

#### Cấu trúc và điều hướng DD1 đến DD6

| Mã và quyết định | Dẫn xuất | Hành vi và lý do |
|---|---|---|
| DD1 One Screen One Primary Task | C1 → UXC1 → P1 | Mỗi màn hình có một mục tiêu tương tác chính để giới hạn lượng thông tin đồng thời và làm rõ phần cần chú ý. |
| DD2 Keep Story Structure Consistent | C5 → UXC5 → P2 | Dùng cấu trúc Scene → Decision → Consequence → Explanation → Next tương đối nhất quán, giúp người dùng học một cách thao tác rồi tập trung vào truyện. |
| DD3 Keep Core Controls in Consistent Positions | C5 → UXC5 → P2 | Next, Back, Replay và progress giữ vị trí tương đối và hành vi ổn định, giảm công tìm và tăng khả năng dự đoán. |
| DD4 Always Provide Story Orientation | C5 → UXC6 → P2 | Hiển thị vị trí hoặc tiến trình bằng biểu diễn dễ hiểu, giúp nhận ra phần đang học và những bước còn lại. |
| DD5 Keep Navigation Shallow | C1, C5 → UXC1, UXC14 → P1, P2 | Child flow có ít tầng, giảm việc phải ghi nhớ đường đi không liên quan đến mục tiêu học. |
| DD6 Avoid Unnecessary Modals | C1, C5 → UXC14 → P1, P2 | Hạn chế popup trong mạch truyện; dùng nội dung trong màn hình khi có thể để giữ bối cảnh. |

#### Ngôn ngữ và biểu diễn DD7 đến DD12

| Mã và quyết định | Dẫn xuất | Hành vi và lý do |
|---|---|---|
| DD7 Use Short and Concrete Language | C2, C3 → UXC2, UXC3 → P1, P3 | Câu ngắn và trực tiếp gắn với cảnh hiện tại, giảm yêu cầu giải mã từ ngữ trừu tượng trước khi hiểu nội dung. |
| DD8 Minimize Text | C1, C2 → UXC1, UXC2 → P1, P5 | Giữ lượng chữ cần để truyền nghĩa, chia phần khi cần, tránh biến hoạt động xã hội thành nhiệm vụ đọc dài. |
| DD9 Use Highly Legible Typography | C2 → UXC2 → P1 | Chữ rõ, hỗ trợ tiếng Việt và phân cấp dễ nhận, ưu tiên đọc hiểu hơn trang trí. |
| DD10 Keep Text Stable and Easy to Read | C1, C2 → UXC1, UXC2 → P1 | Chữ quan trọng đứng yên, đủ tương phản và khoảng cách, không buộc trẻ vừa đọc vừa theo chuyển động hoặc nền phức tạp. |
| DD11 Use Literal and Understandable Icons | C3 → UXC3 → P3 | Ưu tiên icon có nghĩa trực tiếp; kiểm tra với người dùng thay vì dựa vào mức quen thuộc của người lớn. |
| DD12 Pair Important Icons with Simple Labels | C2, C3 → UXC2, UXC3 → P3, P5 | Icon quan trọng có nhãn ngắn khi phù hợp; icon hỗ trợ nhận biết còn chữ hoặc lời kể giúp giảm mơ hồ. |

#### Bối cảnh phản hồi và lặp lại DD13 đến DD19

| Mã và quyết định | Dẫn xuất | Hành vi và lý do |
|---|---|---|
| DD13 Explicitly Present Social Context | C4 → UXC4 → P3 | Làm rõ ai tham gia, đang làm gì và bối cảnh hiện tại, cung cấp đầu vào trước khi yêu cầu suy luận hoặc chọn. |
| DD14 Explicitly Present Relevant Social Cues | C4 → UXC4 → P3 | Tín hiệu cần thiết được thể hiện đủ để nhận biết qua cảnh và lời kể; không chỉ để ngầm trong biểu cảm. |
| DD15 Show Consequences of Important Choices | C4 → UXC4, UXC12 → P3, P4 | Lựa chọn quan trọng dẫn đến phản ứng quan sát được trong kịch bản, cụ thể hóa quan hệ nguyên nhân và kết quả. |
| DD16 Explain Why the Consequence Happened | C4 → UXC12 → P4 | Bổ sung lý do sau phản ứng vì quan sát một diễn biến chưa bảo đảm người dùng hiểu nó. |
| DD17 Avoid Binary Correct Wrong as Primary Feedback | C4, C10 → UXC11, UXC12 → P4, P8 | Không lấy Đúng/Sai làm cơ chế phản hồi chính; giải thích bối cảnh và lựa chọn để hỗ trợ hiểu quan hệ xã hội. |
| DD18 Allow Retry Without Penalty | C10 → UXC11, UXC13 → P8 | Cho thử phản hồi khác mà không trừ điểm hoặc quy thành thất bại, giữ cơ hội khám phá. |
| DD19 Support Replay | C10 → UXC13 → P8 | Có thể phát lại lời kể, cảnh hoặc truyện, giúp xem lại cùng khái niệm mà không nhận phản hồi tiêu cực. |

#### Đa phương thức cảm giác và affordance DD20 đến DD25

| Mã và quyết định | Dẫn xuất | Hành vi và lý do |
|---|---|---|
| DD20 Use Multiple Modalities | C2 → UXC2 → P5 | Cung cấp Image + Short Text + Voice + Interaction theo lựa chọn phù hợp, phân bố khả năng tiếp nhận thay vì dựa hoàn toàn vào đọc. |
| DD21 Use Controlled Animation and Sound | C9 → UXC10 → P6 | Animation và âm thanh chỉ xuất hiện khi giúp chú ý, giải thích hoặc nhận phản hồi, không chỉ để tăng kích thích. |
| DD22 Make Audio Controllable | C9 → UXC10 → P6 | Có nghe lại, giảm hoặc tắt âm thanh khi phù hợp vì nhu cầu cảm giác khác nhau giữa người dùng. |
| DD23 Prevent Audio Overlap | C8, C9 → UXC9, UXC10 → P6, P7 | Chạm nhiều lần không tạo nhiều bản audio phát chồng; lệnh mới thay thế hoặc được kiểm soát theo trạng thái. |
| DD24 Provide Immediate Interaction Feedback | C8 → UXC9 → P7 | Chạm hoặc chọn làm thay đổi trạng thái nhìn thấy được hoặc nghe được, giúp biết hệ thống đã nhận input. |
| DD25 Make Interactive Elements Visually Obvious | C7 → UXC8 → P7, P9 | Thành phần trông có thể tương tác phải phản hồi phù hợp; thành phần trang trí không giả control. |

#### Thao tác vật lý DD26 đến DD30

| Mã và quyết định | Dẫn xuất | Hành vi và lý do |
|---|---|---|
| DD26 Prefer Tap as the Primary Gesture | C6 → UXC7 → P9 | Luồng cốt lõi ưu tiên chạm, giảm yêu cầu phối hợp vận động không cần cho mục tiêu xã hội. |
| DD27 Avoid Complex Gestures | C6 → UXC7 → P9 | Không bắt buộc double-tap, long press phức tạp, pinch hoặc gesture nhiều ngón trong nhiệm vụ cốt lõi. |
| DD28 Use Large and Forgiving Touch Targets | C6 → UXC7 → P9 | Button và lựa chọn có vùng chạm, khoảng cách đủ lớn; phân biệt kích thước hình vẽ với vùng nhận chạm. |
| DD29 Support Accidental Multi touch Without Requiring It | C6 → UXC7 → P9 | Chạm nhiều ngón vô tình không gây crash hoặc ghi nhiều lựa chọn; nhiệm vụ vẫn hoàn thành bằng một điểm chạm. |
| DD30 Avoid Accelerometer dependent Core Interaction | C6 → UXC7 → P9 | Lắc, nghiêng và xoay thiết bị không là điều kiện bắt buộc để tiếp tục truyện, tránh thêm yêu cầu vận động không liên quan. |

#### Vai trò dữ liệu và mức phức tạp DD31 đến DD36

| Mã và quyết định | Dẫn xuất | Hành vi và lý do |
|---|---|---|
| DD31 Separate Child Mode and Caregiver Mode | C11 → UXC15 → P10 | Tách trải nghiệm câu chuyện khỏi quản lý vì hai nhóm có mục tiêu và mức phức tạp cần thiết khác nhau. |
| DD32 Keep Management Controls Outside the Child Story Flow | C11 → UXC15, UXC14 → P1, P10 | Settings, analytics và configuration nằm ngoài mạch truyện, giữ tập trung vào nhiệm vụ của trẻ. |
| DD33 Collect Minimum Child Data | C12 → UXC16 → P10, bổ sung P11 | Chỉ lấy dữ liệu có mục đích sản phẩm rõ; phân biệt thông tin cần cho phiên với dữ liệu tùy chọn. |
| DD34 Avoid Dark Patterns and Forced Engagement | C12 → UXC16 → P10, bổ sung P11 | Không dùng FOMO, countdown tạo áp lực, nút gây hiểu nhầm hoặc ép tiếp tục. Thành công được xem theo sự tham gia có ý nghĩa, không tối đa hóa thời gian màn hình. |
| DD35 Introduce Complexity Gradually | C1 → UXC17 → P1 | Hướng dẫn cách dùng cơ bản trước, bổ sung loại tương tác khi cần cho mục tiêu và sau khi đã kiểm tra mức phù hợp. |
| DD36 Do Not Make Open AI Voice Interaction Mandatory Initially | C1, C2, C12 → UXC17, UXC16 → P1, P5, P10; bổ sung P11 | Giữ voice AI là phương án có giá trị học tập rõ, có giới hạn và đường thay thế. Voice mở có thể tăng yêu cầu biểu đạt, bất định, dữ liệu và thao tác; structured interaction được giữ khi đủ đáp ứng mục tiêu. |

#### Quyết định bổ sung để hoàn thiện luồng

DD37 Pause Help and Resume bổ sung: cung cấp cách Nghỉ, Cần giúp và tiếp tục khi phù hợp, từ C5, C11 và C12 → UXC6, UXC14, UXC16 → P2, P10, P11.

DD38 Describe Observations Without Diagnostic Scoring bổ sung: review ghi lựa chọn, lời giải thích đã xem và hỗ trợ được ghi nhận; không tự chuyển chúng thành điểm ASD hoặc kết luận hiểu biết, từ C4, C11 → UXC12, UXC15 → P4, P10.

DD39 Make AI Suggestions Reviewable bổ sung: caregiver thấy lý do gợi ý, có thể chọn truyện khác; lỗi nhận dạng được xác nhận và sửa bằng phương thức thay thế, từ C2, C12 → UXC16, UXC17 → P5, P10, P11.

DD40 Preserve User Control During Errors bổ sung: khi gặp lỗi, giữ bối cảnh có thể phục hồi, giải thích ngắn và cung cấp thao tác tiếp theo, từ C5, C8 → UXC6, UXC9, UXC14 → P2, P7.

Framework được áp dụng như một chuỗi lập luận cần kiểm chứng. Triết lý thiết kế được giữ là Make the implicit explicit — simply, predictably, and safely; core learning loop là Understand → Predict → Choose → Observe → Understand Why → Repeat. Những câu này thể hiện định hướng sản phẩm, không được dùng thay cho kết quả đánh giá người dùng.



## 5.2 Information Architecture và Navigation

### 5.2.1 Tổ chức thông tin theo hai chế độ

Caregiver mode chứa những nhiệm vụ chuẩn bị và quản lý: hồ sơ trẻ, liên kết, thư viện, chi tiết truyện, kế hoạch, lịch sử, review, AI gợi ý, cài đặt, accessibility và hỗ trợ. Child mode chứa câu chuyện đang được chọn cùng các thao tác trực tiếp: nghe, xem, chọn, nghe lại, quay lại khi phù hợp, tiếp tục, nghỉ và cần giúp.

Các chế độ được phân tách theo nhiệm vụ và quyền truy cập. Một thao tác chạm từ màn hình trẻ không mặc nhiên mở dữ liệu quản lý. Cách xác nhận chuyển sang caregiver mode phải phù hợp nền tảng và cơ chế tài khoản ở Chương 6; một câu hỏi toán học đơn giản không được xem là thay thế xác thực hoặc phân quyền dữ liệu.

| Khu vực | Nội dung chính | Vai trò thiết kế |
|---|---|---|
| Caregiver Home | Hồ sơ đang chọn, kế hoạch gần nhất, tiếp tục phiên hoặc chọn truyện. | Xác nhận đúng trẻ và đưa người lớn đến nhiệm vụ ưu tiên. |
| Library | Chủ đề, tìm kiếm/lọc, nội dung phổ biến và gợi ý. | Tìm theo tình huống cần chuẩn bị; không mặc định truyện phổ biến phù hợp với mọi trẻ. |
| Story Details | Mục tiêu, bối cảnh, hình thức tương tác, mức hỗ trợ dự kiến và xem trước. | Giúp caregiver quyết định trước khi trẻ bắt đầu. |
| Child Story | Cảnh, lựa chọn, diễn biến và giải thích. | Giữ trọng tâm vào hoạt động hiện tại. |
| Review and Plan | Lịch sử theo phiên, diễn biến, lựa chọn và hoạt động tiếp theo. | Hỗ trợ trao đổi dựa trên quan sát, không gán chẩn đoán. |
| Settings and Support | Accessibility, ngôn ngữ, thông báo, quyền dữ liệu, FAQ và phản hồi. | Quản lý ngoài mạch truyện. |

### 5.2.2 Các luồng điều hướng chính

Luồng chuẩn bị gồm Caregiver Home → chọn hồ sơ → Library hoặc AI gợi ý → Story Details → xem trước và thiết lập → bắt đầu Child mode. Nội dung AI có giải thích và cho phép chọn khác; caregiver quyết định truyện được sử dụng.

Luồng câu chuyện gồm giới thiệu bối cảnh → nhiệm vụ hiện tại → lựa chọn → phản ứng trong kịch bản → giải thích → tiếp tục hoặc thử lại. Back và Replay phải có hành vi rõ: nghe lại không tự ghi thêm một lựa chọn mới; quay lại để thử khác cần được phân biệt với lần tham gia trước trong thiết kế lịch sử.

Luồng review gồm xác nhận caregiver → chọn đúng hồ sơ → chọn phiên → xem các cảnh, lựa chọn và giải thích tương ứng → chọn hoạt động tiếp theo. Khi truyện đã cập nhật, review hiển thị phiên bản đã dùng thay vì âm thầm thay lời giải thích cũ bằng nội dung mới.

Luồng hỗ trợ gồm trẻ chọn Cần giúp hoặc Nghỉ → hiển thị hướng dẫn ngắn hoặc trạng thái tạm dừng → người lớn hỗ trợ → tiếp tục khi trẻ muốn. Thông báo nhắc lịch được quản lý ở khu vực người lớn, tránh popup không cần thiết trong cảnh học.

### 5.2.3 Định hướng và khả năng dự đoán

Các control cốt lõi giữ vị trí tương đối ổn định giữa các màn hình. Progress có thể dùng các bước hoặc giai đoạn được minh họa; với truyện phân nhánh, số bước chỉ hiển thị khi phản ánh đúng đường đi hiện tại. Hệ thống không tạo cảm giác khẩn cấp bằng countdown buộc trẻ trả lời.

Nhãn và cách hoạt động được kiểm tra với hồ sơ mục tiêu. Sự quen thuộc của người lớn với một icon không thay thế việc xác nhận trẻ hiểu nó. Định hướng này phù hợp với hướng dẫn W3C về cấu trúc nhất quán, control rõ mục đích và mối liên hệ giữa control với nội dung. [W3C về control và định hướng dễ hiểu](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o1-understandable/)

## 5.3 Onboarding và trải nghiệm lần đầu

### 5.3.1 Giới thiệu cho caregiver

Onboarding trước hết giải thích Bear Buddy dùng để làm quen và khám phá tình huống, cách người lớn đồng hành và giới hạn của dữ liệu review. Nội dung được chia thành bước ngắn, có thể xem lại trong Help. Người dùng được hướng dẫn tạo tài khoản hoặc sử dụng phương án truy cập mà nhóm chốt trong Chương 3.

Hồ sơ trẻ ghi tên hiển thị hoặc biệt danh cùng những tùy chọn thực sự cần cho trải nghiệm. Thiết lập phát triển được thể hiện bằng nhu cầu chức năng như thích nghe hay xem, cách chọn, hỗ trợ đọc, mức âm thanh và cần người lớn ở bước nào. Các câu hỏi này là cấu hình hỗ trợ; chúng không chấm tuổi phát triển hoặc phân loại ASD.

Quyền microphone chỉ được giải thích và yêu cầu khi người dùng chủ động mở chức năng voice đã được bật. Nhắc lịch được giới thiệu khi caregiver lập lịch hoặc chọn nhận thông báo. Nếu quyền bị từ chối, luồng học bằng hình và chạm vẫn có đường tham gia theo đặc tả.

### 5.3.2 Giới thiệu cách dùng cho trẻ

Buổi đầu sử dụng một cảnh đơn giản để làm quen với thao tác: chạm một lựa chọn, nghe hoặc xem phản hồi, phát lại và tiếp tục. Chỉ giới thiệu control cần cho bước hiện tại. Caregiver có thể hỗ trợ mà không phải đưa trẻ qua màn hình quản lý.

Nút Nghỉ và Cần giúp được giới thiệu như hành động hợp lệ. Mascot Bear Buddy có thể hỗ trợ định hướng bằng ngôn ngữ ngắn và nhất quán; nhân vật không tự phát lời khen, âm thanh hoặc animation liên tục khi chưa có mục đích rõ.

### 5.3.3 Kết thúc hoạt động đầu tiên

Màn hình kết thúc ghi nhận việc đã tham gia và cung cấp lựa chọn nghe/xem lại, nghỉ hoặc trở về cùng caregiver. Không tự chuyển sang truyện tiếp theo để kéo dài thời gian sử dụng. Người lớn được chỉ cách review phiên vừa hoàn thành và thay đổi hỗ trợ trước buổi sau.

Onboarding có thể được mở lại khi cần. Các hướng dẫn thao tác và nội dung câu chuyện cần được phân biệt để khó khăn khi làm quen giao diện không bị ghi thành kết quả hiểu tình huống xã hội.

## 5.4 Accessibility

Accessibility là yêu cầu bắt buộc của Bear Buddy và được xem xét cho cả trẻ lẫn caregiver. Nhóm sử dụng WCAG 2.2 như nguồn tham chiếu cho các tiêu chí có thể vận dụng, đồng thời theo hướng dẫn native của nền tảng được chọn. Việc đặt mục tiêu tham chiếu không đồng nghĩa sản phẩm đã được đánh giá đạt toàn bộ WCAG. [WCAG 2.2](https://www.w3.org/TR/WCAG22/)

### 5.4.1 Tiêu chí thiết kế và cách kiểm tra

| Khía cạnh | Đặc tả thiết kế đề xuất | Cách kiểm chứng dự kiến |
|---|---|---|
| Font scaling và kích thước chữ | Chữ quan trọng không nhúng cố định trong ảnh. Thiết kế hỗ trợ tăng chữ; mục tiêu ban đầu là kiểm tra đến 200% mà không mất nội dung hoặc chức năng. | Thử các màn hình chính, control và trạng thái lỗi với kích thước chữ lớn; ghi rõ thiết bị và cấu hình. |
| Màu và tương phản | Mục tiêu cho chữ thông thường là ít nhất 4,5:1 với nền. Màu không là dấu hiệu duy nhất của lựa chọn, lỗi hoặc trạng thái. | Đo cặp màu thực tế; kiểm tra trạng thái selected, disabled và focus; kết hợp nhãn, biểu tượng hoặc viền. |
| Touch target | Nếu Android, tham chiếu ít nhất 48 × 48 dp. Nếu iOS, đặt mục tiêu từ 44 × 44 pt theo kích thước control mặc định trong HIG. Có thể tăng theo thử nghiệm với hồ sơ mục tiêu. | Đo vùng nhận chạm, khoảng cách và kiểm tra bấm nhầm trên thiết bị thực; không chỉ đo icon. |
| Gesture | Nhiệm vụ cốt lõi có thể hoàn thành bằng thao tác chạm đơn. Hoạt động kéo thả có phương án chọn thứ tự bằng chạm nếu cùng mục tiêu cho phép. | Thực hiện toàn bộ luồng bằng phương án thay thế, kiểm tra không có bước bị khóa bởi gesture. |
| Âm thanh và chuyển động | Có điều khiển phát lại, tắt/giảm âm và giảm chuyển động theo phạm vi nền tảng; không phát chồng audio. | Thử chạm lặp, đổi cảnh, pause/resume và các thiết lập giảm chuyển động. |
| Ngôn ngữ và nội dung | Câu ngắn, từ cụ thể, hướng dẫn một bước; nội dung tiếng Việt đầy đủ dấu. Ngôn ngữ được chọn trong caregiver mode và giữ nhất quán. | Review nội dung và thử nhiệm vụ; kiểm tra việc dịch không làm sai ý nghĩa cảnh hoặc control. |
| Truy cập hỗ trợ | Control có tên và vai trò rõ, thứ tự focus hợp lý; hình có thông tin cần thiết có mô tả phù hợp, hình trang trí không gây đọc lặp. | Thử bằng screen reader trên nền tảng chọn, kiểm tra tên control và thông báo trạng thái. |
| Cách biểu đạt | Không bắt buộc trẻ nói để vượt qua luồng cốt lõi; có lựa chọn hình/chạm khi voice bị tắt, không rõ hoặc không phù hợp. | Từ chối microphone và hoàn thành hoạt động bằng cách thay thế. |
| Quyền kiểm soát | Có Nghỉ, Cần giúp và tiếp tục phù hợp; không dùng giới hạn thời gian tạo áp lực cho nhiệm vụ cốt lõi. | Kiểm tra thao tác dừng, quay lại và hỗ trợ mà không mất bối cảnh ngoài đặc tả. |

Mốc tương phản và tăng chữ được tham chiếu từ WCAG 2.2; chúng cần được chuyển thành acceptance criteria cụ thể ở Chương 3. Mốc vùng chạm được đối chiếu với [Android Developers](https://developer.android.com/guide/topics/ui/accessibility/views/apps-views?hl=en) và [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/accessibility). Các giá trị dp và pt là đơn vị của từng nền tảng, không được thay thế tùy ý bằng pixel ảnh mockup.

### 5.4.2 Giới hạn và cá nhân hóa

Một cấu hình mặc định không phù hợp với mọi trẻ. Font, tương phản, âm thanh và cách tương tác được điều chỉnh theo nhu cầu quan sát được. Thay đổi cỡ chữ cần đi cùng bố cục thích ứng; việc thêm một thanh tăng chữ không đủ nếu nội dung bị cắt hoặc nút không sử dụng được.

Mức dễ dùng được đánh giá cả ở khả năng thao tác lẫn khả năng hiểu nhiệm vụ. Kiểm tra accessibility bằng công cụ và tiêu chí cần được kết hợp với quan sát người dùng phù hợp. Đánh giá sơ bộ với người lớn không được dùng để khẳng định trẻ đã hiểu toàn bộ giao diện.

## 5.5 Design System và Mockup

### 5.5.1 Định hướng thị giác và bộ token ban đầu

Design system tổ chức màu, typography, khoảng cách, control và trạng thái để các màn hình dùng cùng ngôn ngữ thiết kế. Định hướng thị giác là rõ trọng tâm, ít chi tiết thừa và có thể điều chỉnh. Nhóm không gán một màu là “phù hợp với mọi trẻ tự kỷ”; màu chỉ được giữ khi đáp ứng tương phản và đánh giá sử dụng.

Bảng sau là bộ token đề xuất ban đầu để dựng mockup, chưa phải bộ nhận diện đã được kiểm chứng với người dùng.

| Token | Giá trị đề xuất | Cách sử dụng |
|---|---|---|
| Background | #F7F9FC | Nền khu vực giao diện. |
| Surface | #FFFFFF | Thẻ, panel và nền nội dung. |
| Text primary | #1F2937 | Chữ chính trên nền sáng. |
| Text secondary | #475569 | Nội dung bổ trợ vẫn cần đọc rõ. |
| Action primary | #2D6253 | Nút hành động chính với chữ trắng. |
| Accent | #F4D06F | Nhấn thông tin có chọn lọc với chữ tối; không làm nền chữ trắng. |
| Focus | #245EA8 | Viền focus hoặc chỉ báo tương tác phù hợp, không là dấu hiệu duy nhất. |

Typography đề xuất dùng font sans-serif có tiếng Việt như Noto Sans hoặc font hệ thống của nền tảng. Cỡ chữ ban đầu có thể phân cấp theo tiêu đề, nội dung và nhãn; nhóm cần kiểm tra thực tế trước khi chốt số đo. Thông tin quan trọng không dùng font trang trí, chữ chạy hoặc hiệu ứng làm người đọc phải theo chuyển động.

### 5.5.2 Các component dùng chung

| Component | Nội dung và trạng thái cần thể hiện |
|---|---|
| Primary và secondary button | Nhãn ngắn, vùng chạm rõ, default, pressed, focus, loading và disabled; không dựa riêng vào màu. |
| Choice card | Hình và nhãn khi phù hợp, selected state, xác nhận input; không biến chạm lặp thành nhiều lựa chọn. |
| Story scene | Nhân vật và bối cảnh có trọng tâm; chữ ngắn; control ổn định; nội dung phản ứng và giải thích. |
| Audio control | Phát, dừng hoặc phát lại có trạng thái rõ; chỉ báo đang nghe không phụ thuộc âm thanh. |
| Progress indicator | Thể hiện bước/giai đoạn đúng với đường truyện; có nhãn dễ hiểu khi cần. |
| Story card | Tên, chủ đề và thông tin giúp caregiver quyết định; nhãn phổ biến không thay thế tiêu chí phù hợp. |
| Profile selector | Cho biết hồ sơ đang dùng; xác nhận chuyển hồ sơ khi có dữ liệu phiên cần giữ. |
| Form và thông báo lỗi | Nhãn, hướng dẫn, kiểm tra input và lỗi gắn đúng trường; thông báo thân thiện, có thao tác tiếp theo. |
| Review record | Cảnh, lựa chọn, lời giải thích, phiên bản và thời điểm liên quan; phân biệt quan sát với suy luận. |
| Permission và support entry | Giải thích mục đích trước thao tác hệ thống; đường vào FAQ, liên hệ và phản hồi. |

Caregiver UI tham chiếu Material Design nếu chọn Android hoặc Human Interface Guidelines nếu chọn iOS, còn Child UI dùng component được điều chỉnh theo nhu cầu đã xác định. Nền tảng cuối cùng và các thay đổi so với component native được ghi thống nhất trong Chương 6.

### 5.5.3 Danh mục màn hình phục vụ dựng mockup

Danh mục này xác định nội dung cần thiết để dựng mockup hi-fi và clickable prototype. Các mã S là mã thiết kế ban đầu để truy vết; màn hình có thể là frame hoặc trạng thái của một frame tùy cách nhóm tổ chức file thiết kế. Đây là đặc tả phạm vi thiết kế; bằng chứng hoàn thành cần đi kèm hình các frame và liên kết prototype được kiểm tra.

| Mã | Màn hình hoặc frame | Nội dung trọng tâm |
|---|---|---|
| S01 | Introduction | Mục đích, hai chế độ và vai trò đồng hành. |
| S02 | Account Access | Đăng nhập và các bước tài khoản theo phạm vi chốt. |
| S03 | Child Profile and Linking | Tạo/chọn hồ sơ, liên kết và thông tin quyền. |
| S04 | Accessibility Setup | Ngôn ngữ, chữ, âm thanh, tương phản và hỗ trợ. |
| S05 | Caregiver Home | Hồ sơ hiện tại, kế hoạch và nhiệm vụ tiếp theo. |
| S06 | Story Library | Chủ đề, tìm kiếm/lọc, nội dung phổ biến. |
| S07 | Story Details and Preview | Mục tiêu, nội dung, tương tác và xem trước. |
| S08 | Child Orientation | Hướng dẫn ngắn và cách Nghỉ/Cần giúp. |
| S09 | Story Context | Ai, hoạt động gì và bối cảnh hiện tại. |
| S10 | Decision Activity | Lựa chọn hoặc dạng tương tác được chốt. |
| S11 | Consequence | Phản ứng trong kịch bản sau lựa chọn. |
| S12 | Explanation and Retry | Lý do, nghe lại, thử khác hoặc tiếp tục. |
| S13 | Pause and Help | Trạng thái nghỉ, hỗ trợ và quay lại. |
| S14 | Session End | Ghi nhận đã tham gia, lựa chọn nghỉ/xem lại. |
| S15 | Session History | Danh sách phiên của đúng hồ sơ. |
| S16 | Session Review | Lựa chọn, diễn biến, lời giải thích và phiên bản. |
| S17 | Learning Plan | Chọn hoạt động và lịch nhắc. |
| S18 | Parent AI Suggestions | Mục tiêu, danh sách gợi ý, lý do và chọn khác. |
| S19 | Settings and Notifications | Quản lý tùy chọn và lịch nhắc. |
| S20 | Privacy and Access | Quyền liên kết, dữ liệu và kiểm soát chia sẻ. |
| S21 | Help FAQ and Contact | Hướng dẫn, liên hệ hỗ trợ. |
| S22 | Feedback and Issue Report | Nội dung phản hồi, dữ liệu đính kèm tùy chọn và xác nhận. |
| S23 | System States | Loading, empty, offline, error, retry và hạn chế quyền. |
| S24 | Voice Interaction Scenario E | Frame có điều kiện; cần đặc tả tình huống E và phương án hình/chạm trước khi đưa vào prototype. |

### 5.5.4 Yêu cầu đối với clickable prototype

Prototype cần nối trọn luồng chọn hồ sơ → tìm và xem trước truyện → trẻ tham gia → nhận giải thích/thử lại → kết thúc → caregiver review. Một luồng bổ sung thể hiện onboarding và thay đổi thiết lập; một nhánh thể hiện lỗi hoặc quyền bị từ chối với đường tiếp tục rõ.

Các frame được dựng đủ nhất quán về component và trạng thái để thử nhiệm vụ. Nếu một chức năng như AI hoặc voice chỉ được mô phỏng trong prototype, nhóm ghi rõ điều đó và không trình bày như đã tích hợp dịch vụ thật. Hình minh họa, ảnh mockup, URL prototype và phiên bản thiết kế được bổ sung làm bằng chứng sau khi dựng và kiểm tra; chúng không được thay bằng ảnh stock không phản ánh luồng app.

## 5.6 Các trạng thái giao diện

Trạng thái hệ thống cần giúp người dùng hiểu việc đang xảy ra và có hành động tiếp theo. Thông tin kỹ thuật phục vụ debug được giữ ngoài thông báo trực tiếp cho trẻ. Lựa chọn trong câu chuyện được xử lý như nội dung học; nó không bị gộp với trạng thái lỗi kỹ thuật.

| Trạng thái | Thể hiện trong giao diện | Hành động và điều cần giữ |
|---|---|---|
| Loading | Chỉ báo đang tải và thông tin ngắn, không dùng hiệu ứng mạnh. | Xác nhận thao tác đã nhận, kiểm soát chạm lặp; cho quay lại khi phù hợp. |
| Empty Library or Search | Nêu chưa có truyện hoặc chưa có kết quả phù hợp. | Đổi từ khóa, bỏ lọc hoặc xem chủ đề; không tạo nội dung giả để lấp trống. |
| Empty History or Plan | Nêu chưa có phiên/kế hoạch và giải thích cách bắt đầu. | Dẫn tới chọn truyện hoặc tạo kế hoạch, không hiển thị điểm giả. |
| Offline | Phân biệt nội dung đã có trên thiết bị với chức năng cần mạng theo đặc tả. | Cho mở phần khả dụng; giải thích giới hạn và retry khi có kết nối. |
| Content Load Error | Thông báo nội dung chưa mở được bằng ngôn ngữ ngắn. | Thử lại hoặc về thư viện; giữ đúng hồ sơ và bối cảnh có thể phục hồi. |
| Save or Sync Pending | Người lớn biết kết quả đã lưu cục bộ hay còn chờ gửi theo kiến trúc chọn. | Không báo thành công đồng bộ khi chưa xác nhận; không gán lỗi cho trẻ. |
| Microphone Denied | Giải thích voice chưa dùng được. | Chọn bằng hình/chạm hoặc mở hướng dẫn quyền ở caregiver mode. |
| Speech Not Recognized | Thông báo “Chưa nghe rõ. Chọn bằng hình hoặc thử lại.” | Không chấm phát âm sai; chỉ tiếp tục bằng nội dung đã được xác nhận. |
| AI Timeout or Unavailable | Cho biết gợi ý/phản hồi chưa sẵn sàng. | Thư viện hoặc kịch bản có sẵn vẫn có đường dùng; retry tùy chọn. |
| Invalid Input | Gắn lỗi với trường caregiver đang nhập, chỉ ra cách sửa. | Giữ dữ liệu hợp lệ đã nhập khi có thể; không dùng mã lỗi kỹ thuật làm hướng dẫn. |
| Access or Linking Error | Không mở hồ sơ không có quyền; giải thích ở mức cần thiết. | Cho kiểm tra tài khoản/liên kết mà không tiết lộ dữ liệu trẻ khác. |
| Notification Disabled | Hiển thị trạng thái nhắc lịch trong caregiver mode. | Cho quản lý lựa chọn, không chặn trẻ học vì chưa bật thông báo. |
| Paused or Interrupted | Xác nhận đang nghỉ hoặc phiên bị gián đoạn. | Tiếp tục từ vị trí hợp lệ theo đặc tả hoặc quay lại có giải thích. |
| Feedback Submission | Có đang gửi, thành công hoặc chưa gửi được. | Cho thử lại; thông tin hồ sơ/log chỉ đính kèm khi cần và được người gửi kiểm soát. |

## 5.7 Đánh giá prototype và vòng lặp thiết kế

### 5.7.1 Mục tiêu và nhiệm vụ đánh giá

Đánh giá prototype tập trung vào việc người dùng có hiểu và hoàn thành nhiệm vụ với hỗ trợ phù hợp hay không. Với caregiver, nhiệm vụ gồm tìm truyện cho một hoàn cảnh cụ thể, xem trước, thiết lập, bắt đầu và review đúng hồ sơ. Với trẻ thuộc hồ sơ mục tiêu, nhiệm vụ có thể gồm nhận biết thao tác tiếp theo, chọn, xem/nghe lại, yêu cầu giúp và nghỉ. Việc quan sát được điều chỉnh theo cách giao tiếp của trẻ; không bắt buộc trẻ phải vừa thao tác vừa giải thích bằng lời.

Nhóm ghi nhận hành động, điểm dừng, chạm nhầm, yêu cầu hỗ trợ, cách hiểu phản hồi và mức trợ giúp đã cung cấp. Thời gian có thể được ghi làm thông tin bối cảnh nhưng không là tiêu chí duy nhất; nhịp tham gia và sự thoải mái cần được xem xét cùng mục tiêu. Nếu người tham gia chỉ là người lớn, báo cáo phân biệt đánh giá của họ với bằng chứng sử dụng trực tiếp của trẻ.

### 5.7.2 Cách ghi nhận và sửa thiết kế

Mỗi vòng dùng một phiên bản prototype được nhận diện rõ. Nhóm mô tả vấn đề quan sát được, bằng chứng, giả thuyết nguyên nhân, thay đổi và kết quả thử lại. Không điền số người, tỷ lệ hoàn thành hoặc câu trích dẫn khi chưa thu thập. Kiểm tra bằng tiêu chí accessibility được thực hiện cùng đánh giá nhiệm vụ để phát hiện cả lỗi hình thức lẫn trở ngại sử dụng. [W3C về đánh giá với người dùng](https://www.w3.org/WAI/test-evaluate/involving-users/)

Ví dụ giả định để minh họa cách ghi: người dùng giữ và kéo thẻ chưa ổn định → nhóm thử phương án chạm chọn thứ tự → quan sát khả năng tham gia với mức hỗ trợ tương ứng. Đây là tình huống minh họa phương pháp, chưa phải kết quả thực nghiệm của Bear Buddy.

### 5.7.3 Liên kết thiết kế với yêu cầu và kiến trúc

| Nhu cầu đầu vào | Quyết định UX | Màn hình ban đầu | Nhóm thành phần cần đối chiếu ở Chương 6 |
|---|---|---|---|
| UN01, UN05 | DD13–DD19 | S09–S12 | Bộ chạy truyện và nội dung kịch bản. |
| UN02, UN04 | DD7–DD12, DD20, DD26–DD30 | S04, S08–S12 | UI component, accessibility và xử lý input. |
| UN03, UN06, UN10 | DD2–DD6, DD21–DD23, DD37 | S09–S14 | State phiên, media và lưu vị trí theo đặc tả. |
| UN07 | DD31–DD32 | S05–S07 | Thư viện và điều hướng caregiver. |
| UN08 | DD31–DD33, DD38 | S03, S15–S16, S20 | Quyền truy cập, phiên học và lưu trữ. |
| UN09 | DD36, DD39 | S18, S24 | AI, voice và cơ chế thay thế. |
| UN11 | DD33–DD34, P11 | S03–S04, S20 | Consent, quyền và quản lý dữ liệu. |
| UN12 | DD24, DD40 | S23 và trạng thái trong luồng | Xử lý lỗi, local storage và tích hợp. |

Đây là bảng nối ban đầu cho ba chương. Nhóm cần bổ sung mã Requirement và Use Case của Chương 3, cùng mã architecture component đã chốt ở Chương 6, để hoàn thành ma trận Requirement → Use Case → Screen → Architecture component theo rubric. Kết quả thử prototype nằm trong chương thiết kế; kiểm thử bản chạy và acceptance criteria được báo cáo ở Chương 8.


# Tài liệu tham khảo

Các nguồn trực tuyến được đối chiếu ngày 03 tháng 11 năm 2026. Tài liệu sản phẩm được dùng để xác nhận mô tả chức năng công bố; tài liệu y khoa, nghiên cứu và accessibility được dùng trong phạm vi các luận điểm được dẫn, không được xem là xác nhận hiệu quả của Bear Buddy.

- CDC. Clinical Testing and Diagnosis for Autism Spectrum Disorder. [Tiêu chí và đánh giá ASD](https://www.cdc.gov/autism/hcp/diagnosis/index.html).
- CDC. Signs and Symptoms of Autism Spectrum Disorder. [Các đặc điểm có thể gặp](https://www.cdc.gov/autism/signs-symptoms/index.html).
- NIH. Autism Spectrum Disorder. [Thông tin về tự kỷ, giao tiếp và hỗ trợ](https://health.nih.gov/health-topics-a-z/autism).
- Carol Gray. Social Stories Overview. [Lịch sử phương pháp](https://carolgraysocialstories.com/social-stories/social-stories-overview/).
- Carol Gray. What is a Social Story. [Định nghĩa và cách tiếp cận](https://carolgraysocialstories.com/social-stories/what-is-a-social-story/).
- Gray, C., Faherty, C., Timmins, S., và Lanou, A. 2023. Social Stories 10.4 Criteria. [Bộ tiêu chí](https://carolgraysocialstories.com/wp-content/uploads/2023/11/2023-Social-Stories-10.4-Criteria-1.pdf).
- Wright, B., và cộng sự. 2024. Impact of Social Stories on social and emotional health of autism spectrum primary school children: the ASSSIST2 RCT with economic evaluation. NIHR Health Technology Assessment. [Báo cáo nghiên cứu](https://www.ncbi.nlm.nih.gov/books/NBK606426/).
- AssistiveWare. Pictello. [Mô tả sản phẩm](https://www.assistiveware.com/products/pictello).
- Touch Autism. Social Stories Creator and Library. [Mô tả sản phẩm](https://touchautism.com/app/social-stories-creator-library/).
- Bee Visual. Choiceworks. [Mô tả sản phẩm](https://www.beevisual.com/).
- W3C WAI. Use Clear and Understandable Content. [Hướng dẫn nhận thức](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o3-clear-content/).
- W3C WAI. Help Users Understand What Things Are and How to Use Them. [Control và định hướng](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o1-understandable/).
- W3C. Web Content Accessibility Guidelines 2.2. [Khuyến nghị WCAG 2.2](https://www.w3.org/TR/WCAG22/).
- W3C WAI. Involving Users in Web Projects for Better Easier Accessibility. [Sự tham gia của người dùng](https://www.w3.org/WAI/planning/involving-users/).
- W3C WAI. Involving Users in Evaluating Web Accessibility. [Đánh giá với người dùng](https://www.w3.org/WAI/test-evaluate/involving-users/).
- Android Developers. Make Apps More Accessible. [Control và vùng chạm](https://developer.android.com/guide/topics/ui/accessibility/views/apps-views?hl=en).
- Apple. Human Interface Guidelines Accessibility. [Hướng dẫn nền tảng](https://developer.apple.com/design/human-interface-guidelines/accessibility).
- UNICEF Innocenti. 2025. Guidance on AI and Children Version 3.0. [Quyền trẻ em trong hệ thống AI](https://www.unicef.org/innocenti/reports/policy-guidance-ai-children).
