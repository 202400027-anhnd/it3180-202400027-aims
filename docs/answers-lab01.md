# Báo cáo Thảo luận - Lab 01

## Câu 1. cấu hình --global được lưu ở đâu? Khác gì so với --local?

Cấu hình `--global` áp dụng cho tất cả các repository của tài khoản người dùng hiện tại trên máy tính. Tệp cấu hình này được lưu tại:

* **Windows:** `C:\Users\<Tên_User>\.gitconfig` (hoặc `~/.gitconfig` trong Git Bash / WSL)
* **Linux:** `/home/<user>/.gitconfig` (hoặc `~/.gitconfig`)
* **macOS:** `/Users/<user>/.gitconfig` (hoặc `~/.gitconfig`)

| Tiêu chí | Cấu hình `--global` | Cấu hình `--local` |
| :--- | :--- | :--- |
| **Phạm vi áp dụng** | Tất cả các repository trên máy tính của người dùng hiện tại. | Chỉ áp dụng riêng cho **duy nhất một repository** hiện tại. |
| **Vị trí lưu trữ** | `~/.gitconfig` (Thư mục Home của hệ điều hành). | `.git/config` (Tệp cấu hình bên trong thư mục ẩn `.git` của repo). |
| **Mức độ ưu tiên** | Thấp hơn (`--local` ghi đè `--global`). | **Cao nhất** (Ưu tiên đè lên `--global` và `--system`). |
| **Trường hợp sử dụng** | Cấu hình mặc định cho máy tính cá nhân (ví dụ: tên hiển thị, email cá nhân, trình biên dịch mặc định, alias). | Cấu hình tùy chỉnh theo dự án (ví dụ: dùng email nhà trường/công ty cho dự án cụ thể). |

---

## Câu 2: Vì sao dùng `git mv` thay vì di chuyển tệp thủ công?

* **Bảo toàn lịch sử thay đổi:** Khi sử dụng `git mv`, Git ghi nhận ngay hành động đổi tên hoặc di chuyển đường dẫn tệp vào khu vực staging area (`index`). Điều này giúp Git theo dõi liên tục lịch sử commit của tệp (`git log --follow <file>`) trước và sau khi chuyển vị trí mà không bị đứt đoạn.
* **Tối ưu thao tác:** Nếu di chuyển tệp thủ công bằng công cụ OS hoặc lệnh `mv` thông thường, Git sẽ hiểu là tệp cũ bị xóa (`deleted`) và tệp mới được tạo ra (`untracked`). Người dùng phải thực hiện 2 thao tác riêng biệt (`git rm` tệp cũ và `git add` tệp mới). Lệnh `git mv` gộp cả hai bước này vào làm một.

---

## Câu 3: `release/lab01` có phải là Baseline không?

**Có.** 

* **Cơ sở lý thuyết:** **Baseline** (Đường cơ sở) là một trạng thái mã nguồn/cấu hình đã được xác minh, thống nhất và "đóng băng" tại một mốc thời gian cụ thể để làm chuẩn cho các đợt phát triển hoặc đánh giá tiếp theo.
* **Áp dụng:** Nhánh `release/lab01` ghi nhận trạng thái mã nguồn hoàn chỉnh của bài thực hành 1 (sau khi đã refactor và chuyển đổi cấu trúc thư mục thành công). Nhánh này được dùng làm căn cứ điểm mốc nộp bài và kiểm toán, đồng thời là nền tảng để phát triển tiếp các tính năng cho Lab 02 mà không bị ảnh hưởng bởi các thay đổi sau đó trên nhánh `master`.

---

## Câu 4: Vì sao không commit thẳng vào `master` dù làm việc một mình?

* **Tuân thủ quy trình chuẩn:** Trong các dự án thực tế, `master` đại diện cho mã nguồn sản phẩm. Việc tạo thói quen làm việc trên nhánh riêng giúp định hình tư duy phát triển chuyên nghiệp.
* **Cô lập rủi ro:** Làm việc trên nhánh riêng (`refactor/*`, `feature/*`) giúp thử nghiệm tính năng hoặc cấu trúc mới an toàn. Nếu xảy ra lỗi hoặc muốn hủy bỏ, ta có thể xóa nhánh mà không ảnh hưởng tới mã nguồn chạy ổn định trên `master`.
* **Tận dụng quy trình Review & CI/CD:** Việc đẩy mã nguồn qua Pull Request (PR) giúp ta tự rà soát lại khác biệt mã nguồn (Diff Inspection) trước khi hợp nhất, đồng thời cho phép các công cụ tự động (Automated Testing / CI) kiểm tra mã trước khi đưa vào nhánh chính.
* **Giữ lịch sử Commit sạch và dễ truy vết:** Gom nhóm các commit phát triển theo chủ đề công việc vào từng PR giúp cây lịch sử (Git Log) trên `master` minh bạch, rõ ràng và dễ dàng `revert` (hoàn tác) cả một tính năng khi cần thiết.