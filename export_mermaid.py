import os
import sys
import base64
import urllib.request

# Script tự động đọc các file .mmd trong diagrams/ và tải ảnh PNG độ phân giải cao về figures/
DIAGRAMS_DIR = os.path.join(os.path.dirname(__file__), "diagrams")
FIGURES_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

MAPPING = {
    "01_use_case_diagram.mmd": "use_case_diagram.png",
    "02_context_diagram.mmd": "context_diagram.png",
    "03_dfd_level_0.mmd": "dfd_level_0.png",
    "04_story_five_stages.mmd": "story_five_stages.png",
    "05_system_architecture.mmd": "system_architecture.png",
    "06_sqlite_erd.mmd": "sqlite_erd.png",
    "07_sequence_story_learning.mmd": "sequence_story_learning.png",
    "08_sequence_voice_interaction.mmd": "sequence_voice_interaction.png",
    "09_state_machine.mmd": "state_machine.png",
}

print("=" * 60)
print("  BEAR BUDDY --- AUTOMATIC MERMAID TO PNG EXPORTER")
print("=" * 60)

for mmd_file, png_file in MAPPING.items():
    mmd_path = os.path.join(DIAGRAMS_DIR, mmd_file)
    png_path = os.path.join(FIGURES_DIR, png_file)
    
    if not os.path.exists(mmd_path):
        print(f"[-] Bỏ qua {mmd_file}: Không tìm thấy file.")
        continue

    with open(mmd_path, "r", encoding="utf-8") as f:
        mermaid_code = f.read().strip()

    print(f"[*] Đang xuất {mmd_file} -> {png_file} ...", end=" ", flush=True)

    success = False
    
    # Cách 1: Thử Kroki API (Rất nhanh, hỗ trợ định dạng Mermaid chuẩn)
    try:
        req = urllib.request.Request(
            "https://kroki.io/mermaid/png",
            data=mermaid_code.encode("utf-8"),
            headers={"Content-Type": "text/plain; charset=utf-8", "User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            if len(data) > 100:
                with open(png_path, "wb") as out_f:
                    out_f.write(data)
                print(f"THÀNH CÔNG (Kroki, {len(data):,} bytes)")
                success = True
    except Exception as e:
        pass

    # Cách 2: Nếu Kroki lỗi, thử mermaid.ink
    if not success:
        try:
            b64_str = base64.b64encode(mermaid_code.encode("utf-8")).decode("ascii")
            url = f"https://mermaid.ink/img/{b64_str}?scale=2"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                if len(data) > 100:
                    with open(png_path, "wb") as out_f:
                        out_f.write(data)
                    print(f"THÀNH CÔNG (Mermaid.ink, {len(data):,} bytes)")
                    success = True
        except Exception as e:
            pass

    if not success:
        print("THẤT BẠI (Vui lòng kiểm tra kết nối mạng).")

print("=" * 60)
print(f"Hoàn tất! Các file ảnh đã được lưu vào thư mục: {FIGURES_DIR}")
print("Bây giờ bạn có thể biên dịch lại main.tex để xem hình mới.")
print("=" * 60)

