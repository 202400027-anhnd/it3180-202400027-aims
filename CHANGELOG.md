Set-Content CHANGELOG.md @"
## [Unreleased]

## [1.0.1] - 2026-11-07
### Fixed
- Sửa lỗi hàm `search_by_title()` phân biệt hoa thường khi tìm kiếm đĩa DVD (Issue #20).

## [1.0.0] - 2026-11-07
### Added
- Thêm chức năng Cart.print_cart() in thông tin giỏ hàng.
- Thêm chức năng tìm kiếm sản phẩm search_by_title().
- Bổ sung logic tính tổng tiền có giảm giá.

### Fixed
- Sửa lỗi giỏ hàng nhận đĩa thứ 21 (Issue #8).
"@
