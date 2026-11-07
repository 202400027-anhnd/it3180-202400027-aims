# Báo cáo Thảo luận - Lab 02

## Câu 1. Vì sao phải đồng bộ master trước khi PR?

Để phát hiện và giải quyết xung đột mã nguồn (Conflict) ngay tại máy cục bộ của lập trình viên, đảm bảo khi đưa lên GitHub, mã nguồn có thể tích hợp an toàn và không làm hỏng hệ thống hiện tại (bảo đảm quy trình CI/CD luôn chạy xanh).

---

## Câu 2: Khi nào không được rebase?

Không được phép sử dụng git rebase đối với các commit đã được push lên công khai trên kho chung (GitHub) và có nhiều người khác đang cùng làm việc dựa trên các commit đó, vì nó sẽ thay đổi mã băm (SHA-1 hash) và làm xáo trộn lịch sử của toàn đội nhóm.

---

## Câu 3: Feature/ khác Topic/ ra sao?

`feature/*`: Nhánh dùng để phát triển một chức năng, nghiệp vụ lớn của phần mềm (ví dụ: giỏ hàng, thanh toán).

`topic/*`: Nhánh ngắn hạn, phạm vi nhỏ dùng để xử lý các công việc kỹ thuật, tài liệu, sửa lỗi nhanh hoặc cấu hình hệ thống (ví dụ: viết tài liệu hướng dẫn, tạo template PR).
