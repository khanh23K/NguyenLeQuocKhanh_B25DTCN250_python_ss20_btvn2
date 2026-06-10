player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]


def calculate_bonus(matches, mmr):
    bonus = (matches * 10) + (int(mmr) * 0.5)
    return bonus


def process_players(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:
        print("Đang xử lý:", record)

        try:
            name = record[0]
            matches = record[1]
            mmr = record[2]

            bonus = calculate_bonus(matches, mmr)

            print(f"Tuyển thủ {name} nhận được {bonus} RP")

        except IndexError:
            name = record[0]
            print(f"{name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue

        except ValueError:
            name = record[0]
            print(f"{name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue

process_players(player_records)

# Lỗi xảy ra vì dữ liệu của Levi có đủ 3 phần tử nên lấy được MMR, còn dữ liệu của SofM chỉ có 2 phần tử nên khi truy cập phần tử thứ 3 chương trình bị lỗi IndexError.
# Nếu SofM được sửa đúng dữ liệu, chương trình sẽ bị lỗi tại bước chuyển "N/A" thành số nguyên và xuất hiện lỗi ValueError.
# Lệnh này giúp xác định chính xác bản ghi nào đang được xử lý trước khi chương trình bị lỗi, từ đó tìm nguyên nhân nhanh hơn.
# Các tên biến như ds, p, t, m, r, b quá ngắn và khó hiểu, nên đổi thành player_records, record, name, matches, mmr, bonus để dễ đọc và bảo trì.
# Tách riêng hàm tính thưởng, sử dụng try...except để xử lý lỗi thiếu dữ liệu (IndexError) và dữ liệu MMR không hợp lệ (ValueError), đồng thời dùng continue để chương trình vẫn tiếp tục xử lý các tuyển thủ còn lại.