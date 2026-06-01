"""
Input:
    Lựa chọn menu (1–7)
    Mã sổ tiết kiệm (string)
    Tên khách hàng (string)
    Số tiền gửi (int)
    Kỳ hạn gửi (int)
    Lãi suất năm (float)
    Số tháng thực gửi (int)

Output:
    Danh sách sổ tiết kiệm
    Thông báo thêm, cập nhật, tất toán thành công hoặc thất bại
    Tiền lãi dự kiến, tổng tiền nhận
    Tiền lãi thực nhận khi rút trước hạn
    Các thông báo lỗi khi dữ liệu không hợp l
"""

saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print(""" 
===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
1. Xem danh sách sổ tiết kiệm
2. Mở sổ tiết kiệm mới
3. Cập nhật thông tin sổ tiết kiệm
4. Tất toán hoặc xóa sổ tiết kiệm
5. Tính lãi dự kiến khi đến hạn
6. Kiểm tra điều kiện rút trước hạn
7. Thoát chương trình
 """)
    choose = input("Nhập lựa chọn của bạn: ")
    if choose == "1":
        if saving_accounts == []:
            print("Danh sách sổ tiết kiệm hiện đang trống!")
        else:
            for index, account in enumerate(saving_accounts):
                print(f"{index+1}. Mã sổ: {account['account_id']} | Khách hàng: {account['customer_name']} | Số tiền gửi: {account['balance']} | Kỳ hạn: {account['term_months']} | Lãi suát: {account['interest_rate']}%/năm | Trạng thái: {account['status']}")
    elif choose == "2":
        new_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
        flag = True
        for account in saving_accounts:
            if account["account_id"] == new_id:
                print("Đã có mã sổ tiết kiệm này rồi!!!")
                flag = False
                break
        if flag == True:
            while True:
                new_name = input("Nhập tên khách hàng: ").strip()
                if new_name == "":
                    print("Tên khách hàng không được để trống, hãy thử lại!")
                else:
                    break
            
            while True:
                new_balance = input("Nhập số tiền gửi: ")
                if not new_balance.isdigit() or int(new_balance) <= 0:
                    print("Số tiền gửi không hợp lệ! Hãy thử lại!")
                else:
                    new_balance = int(new_balance)
                    break
            

            while True:
                new_term_months = input("Nhập kỳ hạn gửi theo tháng: ")
                if not new_term_months.isdigit() or int(new_term_months) <= 0:
                    print("Kỳ hạn gửi không hợp lệ! Hãy thử lại!")
                else:
                    new_term_months = int(new_term_months)
                    break
            

            while True:
                new_interest_rate = input("NHập lãi suất năm: ")
                if not new_interest_rate.isdigit() or float(new_interest_rate) <= 0:
                    print("Lãi suât năm không hợp lệ! Hãy thử lại!")
                else:
                    new_interest_rate = float(new_interest_rate)
                    break
            
            new_account = {
                "account_id": new_id,
                "customer_name": new_name,
                "balance": new_balance,
                "term_months": new_term_months,
                "interest_rate": new_interest_rate,
                "status": "active"
            }

            saving_accounts.append(new_account)
            print("Thêm mới thành công!")

    elif choose == "3":
        update_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()

        flag = False

        for account in saving_accounts:
            if account["account_id"] == update_id:
                flag = True

                if account["status"] == "closed":
                    print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                    break

                while True:
                    new_name = input("Nhập tên khách hàng mới: ").strip()

                    if new_name == "":
                        print("Tên khách hàng không được để trống!")
                    else:
                        break

                while True:
                    new_balance = input("Nhập số tiền gửi mới: ")

                    if not new_balance.isdigit() or int(new_balance) <= 0:
                        print("Số tiền gửi hoặc kỳ hạn không hợp lệ!")
                    else:
                        new_balance = int(new_balance)
                        break

                while True:
                    new_term_months = input("Nhập kỳ hạn mới theo tháng: ")

                    if not new_term_months.isdigit() or int(new_term_months) <= 0:
                        print("Số tiền gửi hoặc kỳ hạn không hợp lệ!")
                    else:
                        new_term_months = int(new_term_months)
                        break

                while True:
                    new_interest_rate = input("Nhập lãi suất năm mới: ")

                    if not new_interest_rate.replace(".", "", 1).isdigit() or float(new_interest_rate) <= 0:
                        print("Lãi suất không hợp lệ!")
                    else:
                        new_interest_rate = float(new_interest_rate)
                        break

                account["customer_name"] = new_name
                account["balance"] = new_balance
                account["term_months"] = new_term_months
                account["interest_rate"] = new_interest_rate

                print("Cập nhật thành công!")
                break

        if flag == False:
            print("Không tìm thấy mã sổ tiết kiệm!")

    elif choose == "4":
        close_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()

        flag = False

        for account in saving_accounts:
            if account["account_id"] == close_id:
                flag = True
                account["status"] = "closed"
                print("Tất toán sổ tiết kiệm thành công!")
                break

        if flag == False:
            print("Không tìm thấy mã sổ tiết kiệm!")

    elif choose == "5":
        account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()

        flag = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                flag = True

                if account["status"] == "closed":
                    print("Không thể thao tác với sổ tiết kiệm đã tất toán!")
                    break

                interest = account["balance"] * account["interest_rate"] / 100 * account["term_months"] / 12
                total = account["balance"] + interest

                print(f"Tiền lãi dự kiến: {interest}")
                print(f"Tổng tiền nhận khi đến hạn: {total}")
                break

        if flag == False:
            print("Không tìm thấy mã sổ tiết kiệm!")

    elif choose == "6":
        account_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()

        flag = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                flag = True

                if account["status"] == "closed":
                    print("Không thể thao tác với sổ tiết kiệm đã tất toán!")
                    break

                while True:
                    actual_months = input("Nhập số tháng thực gửi: ")

                    if not actual_months.isdigit() or int(actual_months) <= 0:
                        print("Số tháng thực gửi không hợp lệ!")
                    else:
                        actual_months = int(actual_months)
                        break

                if actual_months < account["term_months"]:
                    print("Khách hàng rút trước hạn!")
                    applied_rate = 0.5
                else:
                    print("Khách hàng đủ điều kiện hưởng lãi đúng hạn!")
                    applied_rate = account["interest_rate"]

                interest = account["balance"] * applied_rate / 100 * actual_months / 12
                total = account["balance"] + interest

                print(f"Tiền lãi thực nhận: {interest}")
                print(f"Tổng tiền thực nhận: {total}")

                break

        if flag == False:
            print("Không tìm thấy mã sổ tiết kiệm!")

    elif choose == "7":
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        
