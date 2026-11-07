# Báo cáo Thảo luận - Lab 05

## Câu 1. Vì sao ở Phần A chưa gắn tag v1.1.0? Nếu đã gắn rồi thì bây giờ phải phát hành v1.1.1?

**Chưa gắn tag `v1.1.0` ở Phần A vì:** Nhánh `release/lab05` tại Phần A mới chỉ là giai đoạn đóng băng mã nguồn để chuẩn bị kiểm thử, nộp bài hoặc chờ phát hành. Phiên bản chưa được hoàn tất/kiểm toán triệt để. Theo đúng quy trình, tag chỉ được gắn vào baseline khi bản phát hành đó đã ổn định hoàn toàn và chính thức giao cho người dùng 

**Nếu đã gắn tag `v1.1.0` từ trước thì bây giờ phải lên `v1.1.1` vì:** Theo quy tắc Semantic Versioning (SemVer), tag đã được gắn và push lên remote là một Baseline cố định. Ta không được phép di chuyển tag hay sửa đổi mã nguồn nằm dưới tag đó. Do đó, khi đưa bản vá Hotfix vào, nó đã thay đổi mã nguồn của phiên bản nên bắt buộc phải nâng số phiên bản PATCH từ `v1.1.0` lên `v1.1.1`.

---

## Câu 2: Ưu, nhược điểm của Upstream First so với Release First?

| Tiêu chí | **Upstream First** *(Sửa ở master trước $\rightarrow$ cherry-pick về release/*)* | **Release First** *(Sửa ở release/* trước $\rightarrow$ cherry-pick về master)* |
| :--- | :--- | :--- |
| **Bản chất** | Mọi bản sửa lỗi đều được đưa vào dòng mã chính (`master`) trước tiên, sau đó mới cổng (backport) về các nhánh phát hành cũ. | Sửa trực tiếp trên dòng phiên bản bị lỗi (`release/*`) để ra bản vá nhanh nhất, sau đó lan truyền ngược về `master`. |
| **Ưu điểm** | • **Tránh lặp lại lỗi:** Đảm bảo mã nguồn trên `master` luôn chứa mọi bản sửa lỗi, không sợ bị quên khi ra các phiên bản tương lai.<br>• `master` luôn giữ vai trò là "Nguồn chân lý" (Single Source of Truth). | • **Khắc phục sự cố cực nhanh:** Sửa và phát hành trực tiếp cho khách hàng/bản nộp mà không bị ảnh hưởng bởi mã nguồn mới đang dở dang ở `master`.<br>• Dễ kiểm thử cô lập trên môi trường của phiên bản bị lỗi. |
| **Nhược điểm** | • Cần cẩn trọng khi `cherry-pick` về bản cũ vì mã trên `master` có thể đã tích hợp nhiều thay đổi không tương thích với bản cũ. | • **Dễ quên lan truyền:** Rất dễ bỏ sót việc `cherry-pick` về `master` hoặc các nhánh release khác, dẫn đến việc lỗi cũ xuất hiện lại ở bản sau. |

---

## Câu 3: Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?

Lệnh Git ở **Phần F** giúp phát hiện việc quên lan truyền bản sửa là:

```bash
git cherry -v origin/master origin/release/lab05
```

* **Cơ chế hoạt động:** Lệnh `git cherry` so sánh các commit giữa 2 nhánh dựa trên **nội dung thay đổi (patch)** thay vì mã băm SHA.
  * Dấu **`-`**: Commit sửa lỗi đã có bản tương đương trên nhánh đích.
  * Dấu **`+`**: Commit chỉ có ở nhánh nguồn mà **chưa được lan truyền** sang nhánh đích. Nếu quên `cherry-pick`, commit hotfix sẽ hiển thị dấu `+`.

* **Kiểm tra tự động bằng Integration Test Script:** 
  Vòng lặp kiểm thử ở Phần F cũng sẽ phát hiện ngay lỗi chưa được sửa:
  ```bash
  for ref in v1.0.1 v1.1.0 master; do
      git switch --detach -q $ref
      python -c "from aims.dvd import DigitalVideoDisc; from aims.search import search_by_title; print(len(search_by_title([DigitalVideoDisc('The Lion King', 'Animation', 'Roger Allers', 87, 19.95)], 'lion')))"
  done
  ```
  Nếu `release/lab05` (hoặc `v1.1.0`) chưa nhận bản vá, kết quả chạy script trên ref đó sẽ trả về `0` (không tìm thấy) thay vì `1`.
