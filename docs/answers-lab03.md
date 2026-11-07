# Báo cáo Thảo luận - Lab 03

## Câu 1. Merge base là gì?

Là commit chung gần nhất (tổ tiên chung) giữa hai nhánh khác nhau. Git dựa vào điểm neo này để tính toán xem mỗi nhánh đã thay đổi những gì kể từ khi tách nhánh, từ đó tiến hành tự động gộp hoặc báo xung đột.

---

## Câu 2: Vì sao master/release/ phải dùng revert?

Vì các nhánh `master` hay `release/*` là lịch sử chung đã được công khai và đồng bộ về máy của nhiều thành viên. Nếu dùng `git reset`, ta sẽ "viết lại lịch sử" khiến mã băm thay đổi, gây ra lỗi đồng bộ nghiêm trọng cho toàn bộ các máy khác trong nhóm khi họ thực hiện git pull. git revert tạo ra một commit mới để sửa sai, giúp lịch sử luôn tiến về phía trước một cách an toàn.