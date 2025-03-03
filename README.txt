1/ Giới thiệu:
- Đây là project 1 của môn Cơ Sở Trí Tuệ Nhân Tạo, khóa 23, khoa Công Nghệ Thông Tin (CLC).
- Ares's Adventure là 1 trò chơi giải đố sokoban, nhân vật Ares sẽ từ vị trí ban đầu di chuyển trong mê cung và đẩy những viên đá về những điểm đích (gọi là Switch).
- Trong project này, sinh viên sẽ phải vận dụng 4 thuật toán chính Breadth-First Search (BFS), Depth-First Search (DFS), Uniform Cost Search (UCS), A* để giúp Ares tìm được đường giải mã.
- Các file được đặt tên theo chức năng. Ngoài ra, file Function.py là file chứa các hàm bổ trợ cho GUI và gọi đến các thuật toán từ GUI.
2/ Cách chạy chương trình:
- Trước tiên phải tải hết những module có trong phần requirements.txt(nếu thiếu), nếu không làm điều đó thì chuơng trình sẽ không chạy được.
- Build và chạy file main.py(có thể dùng file build.bat nếu chạy bằng terminal).
3/ Cách sử dụng GUI:
- Sau khi chạy chương trình, màn hình chính sẽ hiện lên và cho phép chúng ta chọn start để bắt đầu hoặc exit để thoát khỏi chương trình.
- Sau khi nhấn bắt đầu, chương trình sẽ cho phép chúng ta chọn file input.txt bất kì từ folder “Inputs”.
- Sau khi chạy xong, một cửa sổ chứa câu đố hiện ra và cho phép chúng ta sử dụng bất kì thuật toán nào để tìm được đường đi.
_ Cửa sổ sẽ gồm một số phím cơ bản như: back, start, pause và reset giúp bạn tương tác dễ dàng hơn.
- Trong video đã có giới thiệu chi tiết về những phím này cũng như cách sử dụng của GUI.
4‌/ Lưu ý:
- Khi dùng GUI, bấm reset trước khi chọn 1 thuật toán khác.
- Nếu không chọn thuật toán thì nó sẽ mặc định là BFS.
- Từ input 6 trở đi sẽ tốn một ít thời gian để chạy. Mong thầy hãy thông cảm.
