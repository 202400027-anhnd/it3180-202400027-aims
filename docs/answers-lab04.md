# Báo cáo Thảo luận - Lab 04

## Câu 1. Vì sao chuẩn bị trên master trước, không sửa trên nhánh release?

Để đảm bảo mọi cấu hình phiên bản và tài liệu (CHANGELOG) được đồng bộ gốc trên nhánh phát triển chính. Nhánh release/* chỉ dùng để đóng băng và đóng gói, tránh việc master bị lỗi thời so với release.

---

## Câu 2: Vì sao release/* không merge vào master?

`master` luôn là nhánh đi trước: Nhánh `master` đóng vai trò là nơi tích hợp các tính năng mới liên tục. Khi một phiên bản trên master đã ổn định, nó sẽ được trích xuất (tách nhánh) sang `release/*` để đóng băng baseline phục vụ phát hành.

Tránh làm xáo trộn lịch sử: Nếu merge ngược từ `release/*` về `master`, ta sẽ mang theo các commit mang tính chất "dọn dẹp/đóng gói" (như thay đổi cấu hình release, tài liệu đặc thù của đợt phát hành đó) quay lại nhánh phát triển, gây thừa thãi lịch sử.

Ngoại lệ duy nhất: Chỉ khi có một lỗi nghiêm trọng cần sửa khẩn cấp (Hotfix) xảy ra trực tiếp trên nhánh `release/*`, lúc đó bản sửa lỗi mới được gộp ngược lại `master` để đảm bảo `master` không bị mất bản vá lỗi đó

---

## Câu 3: So sánh với GitFlow. 

| Tiêu chí | Mô hình Git trong Lab | Mô hình GitFlow tiêu chuẩn |
| :--- | :--- | :--- |
| **Nhánh tích hợp chính** | Nhánh **`master`** là nơi duy nhất tích hợp tất cả các tính năng mới sau khi PR được duyệt. | Nhánh **`develop`** mới là nơi tích hợp các tính năng phát triển hàng ngày. |
| **Vai trò của nhánh `master`** | Là nhánh hoạt động năng động, liên tục đón nhận code mới và đi trước các nhánh release. | Là nhánh "đóng băng" tuyệt đối, chỉ chứa mã nguồn cực kỳ ổn định đã phát hành ra môi trường Production. |
| **Quy trình tạo Release** | Tách nhánh `release/*` trực tiếp từ `master` khi đạt độ ổn định. | Tách nhánh `release/*` từ nhánh `develop` khi chuẩn bị đến hạn phát hành. |
| **Luồng kết thúc Release** | Đóng gói, đánh tag và xuất bản GitHub Release ngay trên nhánh `release/*` là hoàn tất. | Khi đóng release, bắt buộc phải merge ngược vào **cả 2 nhánh** `master` (để lưu bản chính thức) và `develop` (để cập nhật mã nguồn). |
| **Sửa lỗi khẩn cấp (Hotfix)** | Tạo nhánh sửa lỗi trực tiếp từ master hoặc nhánh release tương ứng tùy trường hợp. | Tạo nhánh `hotfix/*` bắt nguồn từ `master`, sau khi sửa xong phải merge vào cả `master` lẫn `develop`. |
| **Độ phức tạp quy trình** | **Thấp**, tinh gọn, ít thao tác gộp nhánh, đẩy nhanh tốc độ chuyển giao sản phẩm. | **Cao**, quản lý nghiêm ngặt qua nhiều lớp nhánh phụ, phù hợp dự án lớn có chu kỳ phát hành dài ngày. |

### Đồ thị trực quan luồng đi của mã nguồn

* **Mô hình trong bài Lab (Tuyến tính, một chiều):**
  ```text
  feature/*  ───(PR)───>  master  ───(Tách nhánh)───>  release/lab04 (Đóng băng + Đánh tag v1.0.0)
  ```

* **Mô hình GitFlow (Đa nhánh, hai chiều):**
  ```text
  feature/*  ───(PR)───>  develop  ───>  release/*  ───>  [Merge vào master] ───> Tag chính thức
                                  └───────────────────>  [Merge vào develop] ───> Tiếp tục phát triển
  ```
---

## Câu 4: Vì sao lên 1.0.0 mà không phải 0.4.0?

Các phiên bản có dạng `0.y.z` (như `v0.1.0`, `v0.2.0`, `v0.3.0`) thể hiện dự án đang trong giai đoạn thử nghiệm, phát triển ban đầu và chưa ổn định, có thể thay đổi bất cứ lúc nào.

Việc nâng lên `1.0.0` đánh dấu một cột mốc cực kỳ quan trọng: Sản phẩm đã đạt trạng thái baseline ổn định đầu tiên, sẵn sàng đưa vào môi trường production cho end-user hoặc bàn giao cho khách hàng.

Từ mốc `1.0.0` trở đi, mọi quy tắc tăng số bản vá (PATCH) khi sửa lỗi hoặc tăng phiên bản phụ (MINOR) khi thêm tính năng mới bắt đầu được áp dụng một cách nghiêm chỉnh để người sử dụng không bị ảnh hưởng. Do đó, sau khi hoàn thiện đầy đủ các tính năng nền tảng cốt lõi, hệ thống được công nhận là bản thương mại đầu tiên (1.0.0) chứ không tăng tiến tịnh tiến lên 0.4.0 nữa.


